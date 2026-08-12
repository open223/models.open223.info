import sys
import pathlib
import markdown_utils

def generate_python_code(location):
    # rewrite the 'models/bdg1-1.ttl' location to just the file name
    location = pathlib.Path(location).name

    code_content = f"""\
from buildingmotif import BuildingMOTIF
from buildingmotif.dataclasses import Library, Model
import logging

# Create a BuildingMOTIF object. This validates with the "pyshifty" SHACL
# engine by default, so there is nothing else to install and no Java required.
bm = BuildingMOTIF('sqlite://', log_level=logging.ERROR)

# Load the 223P shapes. The model's owl:imports names the 223P ontology IRI,
# but that IRI is not resolvable on the web yet, so we load a recent copy from
# the models.open223.info git repository; later, we will load this from the
# location of the actual standard. BuildingMOTIF uses OntoEnv to resolve the
# ontologies 223P itself depends on (QUDT, SHACL, ...).
s223 = Library.from_ontology("https://open223.info/223p.ttl", infer_templates=False, run_shacl_inference=False)

# load the model into the BuildingMOTIF instance
model = Model.from_file("https://models.open223.info/{location}")

# A model's manifest is the set of libraries it claims to satisfy. Adding 223P
# to it records the requirement by *name* -- the manifest stays two triples,
# and the shapes stay in the library -- so validate() below needs no arguments.
# Without this the manifest is empty, and an empty manifest means an empty
# shapes graph: every model would trivially "pass" without being checked.
model.manifest.add(s223)

# validate the model against everything its manifest names
ctx = model.validate()

# print the validation result
print(f"Model is valid: {{ctx.valid}}")

# if the model is invalid, print the validation report
if not ctx.valid:
    print(ctx.report_string[:1000]) # first 1000 characters of the report

# BuildingMOTIF can also interpret the report to provide recommendations on fixes
for focus_node, diffs in ctx.get_reasons_with_severity("Violation").items():
    if len(diffs) == 0:
        continue
    print(focus_node)
    for diff in diffs:
        print("  - " + diff.reason())
"""
    return code_content

description = """
This code uses the [BuildingMOTIF](https://github.com/NREL/BuildingMOTIF) library to load the 223P ontology and the model file into a temporary in-memory instance.
It then validates the model against the ontology. If the model is invalid, it will print the validation report.

BuildingMOTIF resolves the ontology's dependencies with [OntoEnv](https://ontoenv.gtf.fyi) and validates with
[shifty](https://shifty.gtf.fyi), both of which are self-contained Rust extensions, so there is nothing else to install and no Java is required.

````{note} BuildingMOTIF installation
:class: dropdown
To install the `buildingmotif` library, you can use the following command:

```shell
pip install 'buildingmotif @ git+https://github.com/NREL/buildingmotif.git@gtf-buildingmotif'
```
````
"""

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python make_notebook.py <path_to_model_file> <path_to_markdown_file>")
        sys.exit(1)

    model_file_path = sys.argv[1]
    markdown_file_path = sys.argv[2]
    print(f"Generating code for model file: {model_file_path}")

    code_content = generate_python_code(model_file_path)

    code_block = f"```{{code-cell}} python3\n{code_content}\n```\n"
    header = "## Load and Validate Model"
    new_body = f"{description}\n{code_block}"

    markdown_utils.upsert_section(markdown_file_path, header, new_body)
