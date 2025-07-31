import os
import glob
import re
import sys
import rdflib
from rdflib import Graph

# Check if the path to the directory is provided
if len(sys.argv) != 2:
    print("Usage: python make-models.py <directory_path>")
    sys.exit(1)

# Get directory name from command line argument
directory = sys.argv[1]

# Check if the provided directory exists
if not os.path.isdir(directory):
    print(f"The provided directory does not exist: {directory}")
    sys.exit(1)

# Function to convert ttl files to json-ld
def convert_ttl_to_jsonld(file_path):
    # Initialize the graph
    g = Graph()
    # Parse the ttl file
    g.parse(file_path, format='turtle')
    # Convert the file name to json-ld format
    jsonld_file_path = file_path.rsplit('.', 1)[0] + '.jsonld'
    # Serialize the graph into json-ld
    g.serialize(destination=jsonld_file_path, format='json-ld', indent=4)
    print(f"Converted {file_path} to {jsonld_file_path}")

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

# Walk through the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.ttl'):
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Convert the file
            convert_ttl_to_jsonld(file_path)

# for each each .md file in the examples/ directory, write the turtle and json-ld links
# into the '## Downloads' folder
for md in glob.glob('examples/*.md'):
    # Extract the file name from the path
    file_name = os.path.basename(md)
    # create the markdown with the links in a <a> tag
    markdown_content = f"""
- <a href="/compiled/{file_name.replace('.md', '.ttl')}">Turtle file (compiled)</a>
- <a href="/withimports/{file_name.replace('.md', '.ttl')}">Turtle file (with all imports)</a>
- <a href="/{file_name.replace('.md', '.ttl')}">Turtle file (original)</a>
- <a href="/{file_name.replace('.md', '.jsonld')}">JSON-LD file (original)</a>

<details>
<summary>What are these files?</summary>

- **Turtle file (original)**: This is the original source Turtle file that was provided to `models.open223.info`, usually as the output of some model creation tool.
- **Turtle file (compiled)**: This is the original Turtle file with all inferred relationships and values added through SHACL inference against the 223P ontology and other dependencies. **You should use this file for any further processing.** It does not contain any of the ontologies.
- **Turtle file (with all imports)**: This is the compiled Turtle file with all imports included in the file (223P ontology, QUDT ontology, and others). This is helpful when you do not want to deal with downloading and managing ontology dependencies. It is also much larger than the compiled file.
- **JSON-LD file (original)**: This is the original Turtle file converted to the JSON-LD format.

[Turtle](https://www.w3.org/TR/turtle/) is a syntax for RDF (Resource Description Framework) that is easy to read and write. It is a popular format for representing linked data. Parsers and serializers
are available in many programming languages. [JSON-LD](https://json-ld.org) is a JSON-based format for linked data that is easy to use with JavaScript and other web technologies.
</details>
    """
    replace_section_in_markdown(md, '## Downloads', markdown_content)

