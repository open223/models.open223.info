import urllib.parse
import os
import sys
import re
import toml

def replace_section_in_markdown(file_path, header, new_content):
    header_pattern = re.compile(r"^## .+$", re.MULTILINE)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find the start index of the header section to be replaced
    header_start_idx = content.find(header)
    if header_start_idx == -1:
        print(f"The header '{header}' was not found in the file.")
        return

    # Find the start index of the next header (if it exists)
    headers_start = [match.start() for match in header_pattern.finditer(content)]
    next_header_idx = None
    for start in headers_start:
        if start > header_start_idx:
            next_header_idx = start
            break

    # If there's a next header, split the content, otherwise take everything until the end
    if next_header_idx is not None:
        pre_content = content[:header_start_idx]
        post_content = content[next_header_idx:]
        new_content = f"{pre_content}{header}\n{new_content}\n{post_content}"
    else:
        pre_content = content[:header_start_idx]
        new_content = f"{pre_content}{header}\n{new_content}\n"

    # Write the modified content back to the same file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)


# Check if the path to the directory is provided
if len(sys.argv) != 2:
    print("Usage: python generate-queries.py <model_directory_path>")
    sys.exit(1)

# Get directory name from command line argument
directory = sys.argv[1]

# Load the contents of the TOML file
with open('queries.toml', 'r') as f:
    toml_data = toml.load(f)

# now, for all models that don't appear in the toml file, add a row to the markdown table
# with a 'select *' query
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.ttl'):
            base_name = os.path.splitext(file)[0]
            examples_path = os.path.join("examples", f"{base_name}.md")
            print(f"Processing file: {examples_path}")
            # Check if the model is already in the TOML file and it has an "examples" section
            if base_name not in toml_data and os.path.exists(examples_path):
                # Add a default query for the model
                toml_data[base_name] = [
                    {
                        "description": "Select all model",
                        "query": "\nSELECT * WHERE {\n\t ?s ?p ?o \n}\n LIMIT 10",
                    }
                ]


# Define the base URL for the queries
base_url = "https://query.open223.info/"

# Loop over each query configuration in the TOML file and add rows to the markdown table
for key in toml_data:
    # Start creating the markdown table
    markdown_table = "| Description | Query URL |\n"
    markdown_table += "|-------------|-----------|\n"
    for query in toml_data[key]:
        description = query.get('description', '')
        raw_query = query.get('query', '')

        # Generate the query URL (URLEncoded)
        encoded_query = "PREFIX s223: <http://data.ashrae.org/standard223#> "
        encoded_query += "PREFIX unit: <http://qudt.org/vocab/unit/> "
        encoded_query += "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> "
        encoded_query += "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> "
        encoded_query += "PREFIX quantitykind: <http://qudt.org/vocab/quantitykind/> "
        encoded_query += "PREFIX qudt: <http://qudt.org/schema/qudt/> "
        encoded_query += "PREFIX sh: <http://www.w3.org/ns/shacl#> "
        encoded_query += "PREFIX owl: <http://www.w3.org/2002/07/owl#> "
        encoded_query += raw_query

        query_url = f"{base_url}?query={urllib.parse.quote_plus(encoded_query)}"
        # add a url parameter which points to models.open223.info/models/<key>.ttl
        url_param = urllib.parse.quote_plus(f"https://models.open223.info/compiled/{key.lower()}.ttl")

        query_url += "&url=" + url_param
        print(f"Query URL: {query_url}")


        # Add a row to the markdown table
        markdown_table += f"| {description} | <a href='{query_url}'>Query Link</a> |\n"
    header_to_replace = "## Queries"
    markdown_file_path = f"examples/{key}.md"
    replace_section_in_markdown(markdown_file_path, header_to_replace, markdown_table)

