import os
import sys
import pathlib
import markdown_utils

PUBLISHED_BASE_URL = "https://models.open223.info"


def model_base_url():
    """Where the generated cell reads the model from.

    The URL is baked into the page at generation time so that the code a reader
    sees is a single, copy-pasteable Model.from_file(...) call. tools/model-base-url.sh
    picks the value: the commit under test in CI, the working tree locally.
    """
    return os.environ.get("OPEN223_MODEL_BASE_URL", PUBLISHED_BASE_URL).rstrip("/")


def is_preview(base_url):
    """Whether this build reads models from somewhere other than the canonical copy.

    tools/model-base-url.sh --preview is the authority, because only it knows
    whether a raw.githubusercontent.com URL is main's (canonical) or a branch's
    (a preview); the Makefile passes its answer through OPEN223_MODEL_PREVIEW.
    Fall back to comparing against the published site when the variable is not
    set, so running this script by hand still does something sensible.
    """
    flag = os.environ.get("OPEN223_MODEL_PREVIEW")
    if flag is not None:
        return flag.strip() != "0"
    return base_url != PUBLISHED_BASE_URL


def model_load_block(filename, base_url):
    """The commented `Model.from_file(...)` line the page shows.

    A build reads the model from the commit under test (or, locally, from the
    working tree) so that it validates what it is about to publish rather than
    what was published last time. That URL is not the one a reader wants, so
    name the published copy right above it -- it is the stable, pretty URL and
    the one to use day to day.
    """
    published = f"{PUBLISHED_BASE_URL}/{filename}"
    read_from = f"{base_url}/{filename}"

    if read_from == published:
        return f'''# load the model into the BuildingMOTIF instance
model = Model.from_file("{published}")'''

    return f'''# load the model into the BuildingMOTIF instance. This page pins the exact copy
# it was built and validated against, so it stays reproducible as the site moves
# on. To run this against the current published model, use the permanent URL:
#
#     model = Model.from_file("{published}")
#
model = Model.from_file("{read_from}")'''


def generate_python_code(location, base_url):
    # rewrite the 'models/bdg1-1.ttl' location to just the file name
    location = pathlib.Path(location).name

    code_content = f"""\
from buildingmotif import BuildingMOTIF
from buildingmotif.dataclasses import Library, Model
from datetime import datetime, timezone
import logging

# Create a BuildingMOTIF object. This validates with the "pyshifty" SHACL
# engine by default, so there is nothing else to install and no Java required.
bm = BuildingMOTIF('sqlite://', log_level=logging.ERROR)

# load 223P library. We will load a recent copy from the models.open223.info
# git repository; later, we will load this from the location of the actual standard.
# BuildingMOTIF uses OntoEnv to fetch the ontologies 223P depends on (QUDT, SHACL, ...).
s223 = Library.from_ontology("https://open223.info/223p.ttl", infer_templates=False, run_shacl_inference=False)

{model_load_block(location, base_url)}

# a model's manifest lists the libraries it should conform to
model.manifest.add(s223)

# validate the model against its manifest
ctx = model.validate()

# print when validation completed
print(f"Validation run at: {{datetime.now(timezone.utc).isoformat(timespec='seconds')}}")

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

description_template = """
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

    base_url = model_base_url()
    print(f"Reading the model from: {base_url}")

    code_content = generate_python_code(model_file_path, base_url)

    code_block = f"```{{code-cell}} python3\n{code_content}\n```\n"
    header = "## Load and Validate Model"

    description = description_template
    if is_preview(base_url):
        # A preview build of a branch: say so, since the page is not validating
        # the model that is currently published.
        description += (
            f"\n```{{warning}} Preview build\nThis page validates the model at `{base_url}/`, "
            "which is a branch copy rather than the published one.\n```\n"
        )

    new_body = f"{description}\n{code_block}"

    markdown_utils.upsert_section(markdown_file_path, header, new_body)
