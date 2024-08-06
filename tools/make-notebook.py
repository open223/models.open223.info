import sys
import re
import pathlib

def generate_python_code(location):
    # rewrite the 'models/bdg1-1.ttl' location to 'compiled/bdg1-1.ttl'
    model_path = pathlib.Path(location).name
    location = pathlib.Path('compiled') / model_path

    # remove the extension from model_name
    model_name = pathlib.Path(location).stem

    code_content = f"""\
from buildingmotif import BuildingMOTIF
from buildingmotif.dataclasses import Library, Model
import logging

# Create a BuildingMOTIF object. If you do not have Java installed, remove the "shacl_engine" parameter
bm = BuildingMOTIF('sqlite://', shacl_engine='topquadrant', log_level=logging.ERROR)

# load 223P library. We will load a recent copy from the models.open223.info
# git repository; later, we will load this from the location of the actual standard
s223 = Library.load(ontology_graph="https://github.com/open223/models.open223.info/raw/main/ontologies/223p.ttl")

# load the model into the BuildingMOTIF instance
model = Model.create("urn:{model_name}")
model.graph.parse("https://models.open223.info/{location}")

# validate the model against 223P ontology
ctx = model.validate([s223.get_shape_collection()], error_on_missing_imports=False)

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

To run this code, you need to have Java installed on your system. If you do not have Java installed, you can remove the `shacl_engine='topquadrant'` parameter from the `BuildingMOTIF` constructor.
Be warned that without the `shacl_engine='topquadrant'` parameter, the validation process will be slower.

````{note} BuildingMOTIF installation
:class: dropdown
To install the `buildingmotif` library, you can use the following command:

```shell
pip install 'buildingmotif[topquadrant] @ git+https://github.com/NREL/buildingmotif.git@develop'
```

If you do not have Java installed, you can use the following command to install the library:

```shell
pip install 'buildingmotif @ git+https://github.com/NREL/buildingmotif.git@develop'
```
````
"""

def add_code_to_markdown(markdown_file_path, code_content):
    # code_tab = """
    # ````{tab-set}
    # ```{tab-item} Tab 1 title
    # My first tab
    # ```

    # ```{tab-item} Tab 2 title
    # My second tab with `some code`!
    # ```
    # ````
    # """
    code_block = f"\n```{{code-cell}} ipython3\n{code_content}\n```\n"

    header = "## Load and Validate Model"
    new_content = f"\n{header}\n{description}\n{code_block}"

    with open(markdown_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Check if the header exists and replace its content if it does
    if header in content:
        # remove everything from this header up until the next markdown header or the end of the file (whichever is first)
        # and replace it with the new content
        content = re.sub(rf"{header}[\s\S]*?(?=##|$)", new_content, content)


    else:
        content += new_content

    with open(markdown_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python make_notebook.py <path_to_model_file> <path_to_markdown_file>")
        sys.exit(1)

    model_file_path = sys.argv[1]
    markdown_file_path = sys.argv[2]

    code_content = generate_python_code(model_file_path)
    add_code_to_markdown(markdown_file_path, code_content)
