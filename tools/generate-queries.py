import urllib.parse
import os
import sys
import toml
import markdown_utils

# Check if the path is provided
if len(sys.argv) != 3:
    print("Usage: python generate-queries.py <model_file_path> <markdown_file_path>")
    sys.exit(1)

# Get file paths from command line arguments
model_file_path = sys.argv[1]
markdown_file_path = sys.argv[2]


# Load the contents of the TOML file
with open('queries.toml', 'r') as f:
    toml_data = toml.load(f)

base_name = os.path.splitext(os.path.basename(model_file_path))[0]
key = base_name

# get queries for model, or use default
queries_for_model = toml_data.get(key)
if not queries_for_model:
    queries_for_model = [
        {
            "description": "Select all triples from model.",
            "query": "\nSELECT * WHERE {\n\t ?s ?p ?o \n}\n LIMIT 10",
        }
    ]

# Define the base URL for the queries
base_url = "https://query.open223.info/"

# Start creating the markdown table
markdown_table = "| Description | Query URL |\n"
markdown_table += "|-------------|-----------|\n"
for query in queries_for_model:
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
try:
    print(f"Replacing section with header '{header_to_replace}' in {markdown_file_path}")
    markdown_utils.replace_section(markdown_file_path, header_to_replace, markdown_table)
except ValueError as e:
    print(e)

