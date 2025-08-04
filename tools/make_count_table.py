import sys
import rdflib
from collections import defaultdict
import markdown_utils

# Check for the correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python make_count_table.py <path_to_ttl_file> <path_to_markdown_file>")
    sys.exit(1)

file_path = sys.argv[1]
markdown_file_path = sys.argv[2]

# Load the ontology file with root classes
ontology_path = '_static/223p.ttl'  # You mentioned the ontology as "223p.ttl" in the local directory
g = rdflib.Graph()
g.parse(file_path, format='turtle')
g.parse(ontology_path, format='turtle')

# Prepare namespace based on your ontology
S223_NAMESPACE = rdflib.Namespace('http://data.ashrae.org/standard223#')  # Please replace this with the actual namespace

# Prepare a dictionary to store counts
class_counts = defaultdict(lambda: defaultdict(int))

# Fetch all instances of specified root classes
root_classes = ['Equipment', 'Connection', 'ConnectionPoint', 'ExternalReference', 'FunctionBlock', 'PhysicalSpace', 'DomainSpace', 'Zone', 'Property']

for root_class in root_classes:
    root_class_uri = S223_NAMESPACE[root_class]
    # Fetch all subclasses of the root class
    all_subclasses = list(g.transitive_subjects(rdflib.RDFS.subClassOf, root_class_uri))
    for subclass in all_subclasses:
        # Fetch all instances of the subclass
        for instance in g.subjects(rdflib.RDF.type, subclass):
            # skip instances from the ontology itself
            if str(instance).startswith(S223_NAMESPACE):
                continue
            # if the subclass is the same as the root class, then it is a direct instance
            # and we use a blank "subclass" string but only if there are no other subclasses
            if subclass == root_class_uri:
                if len(all_subclasses) > 1:
                    continue
                subclass = ''
            # Increment the count
            class_counts[root_class][str(subclass)] += 1


# write the markdown table to a string
markdown_table = ""
markdown_table += "| Parent Class | Class | Instances |\n"
markdown_table += "|------------|-------|----------------|\n"
for root_class, subclasses in class_counts.items():
    # generate a link to the root class as https://explore.open223.info/s223/{root class}.html and use the short name
    root_class_link = f"[{root_class.split('#')[-1]}](https://explore.open223.info/s223/{root_class.split('#')[-1]}.html)"
    for subclass, count in sorted(subclasses.items(), key=lambda x: x[1], reverse=True):
        subclass_link = f"[{subclass.split('#')[-1]}](https://explore.open223.info/s223/{subclass.split('#')[-1]}.html)"
        # generate a link to the subclass as https://explore.open223.info/s223/{subclass}.html and use the short name
        markdown_table += f"| {root_class_link} | {subclass_link} | {count} |\n"

# Replace the section in the markdown file
header_to_replace = "## Model Components"
markdown_utils.replace_section(markdown_file_path, header_to_replace, markdown_table)
