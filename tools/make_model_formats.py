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
    file_name = os.path.basename(md).lower()
    # create the markdown with the links in a <a> tag
    markdown_content = f"""
- <a href="/{file_name.replace('.md', '.ttl')}">Turtle file</a> (<a href="/compiled/{file_name.replace('.md', '.ttl')}">compiled</a>)
- <a href="/{file_name.replace('.md', '.jsonld')}">JSON-LD file</a>
    """
    replace_section_in_markdown(md, '## Downloads', markdown_content)

