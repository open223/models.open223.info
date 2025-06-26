---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Open223 Models

ASHRAE standard 223P is a proposed standard that formally defines knowledge concepts for representing building system information such as the connections between mechanical equipment, spaces within a building, and their measurement and control points. It is a metadata schema and semantic ontology that defines the modeling constructs and rules needed to construct semantically interoperable, machine-readable semantic models that provide software applications the ability to determine essential information about the meaning and context of building data to support the deployment of various advanced features such as advanced building controls, fault detection and diagnostics, and automated commissioning.

Most models are available in two variants: "original" and "compiled" where in the latter, SHACL Rules defined by the 223P ontology are applied to extend RDF instance data.

````{margin}
```{note}
The 223P standard is not yet finalized and is still under development.
```
````

```{code-cell} python3
:tags: [remove-cell]
from datetime import datetime
import glob
import os
from myst_nb import glue
import subprocess

def get_git_last_modified_date(file_path):
    """Gets the last modified date of a file from git."""
    git_cmd = ["git", "log", "-1", "--format=%ci", "--", file_path]
    date_str = subprocess.check_output(git_cmd, text=True).strip()
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S %z')

last_updated_dt = get_git_last_modified_date("ontologies/223p.ttl")
last_updated_formatted = last_updated_dt.strftime("%Y-%m-%d %H:%M:%S")
glue("last_updated", last_updated_formatted)
```

This site contains example buildings, systems, and other assets modeled in 223 with supporting documentation.

The 223P ontology used to build this site was last updated at **{glue:text}`last_updated`**.

The following models may be out of date with the latest 223P:

```{code-cell} python3
:tags: [remove-input]
# loop through all the models and find the last time they were updated
# from git
models = glob.glob("models/*.ttl")
outofdate = {}
for model in models:
    # if the modified time is before the last_updated_dt time,
    # then add the model to the outofdate dictionary
    model_last_updated_dt = get_git_last_modified_date(model)
    if model_last_updated_dt < last_updated_dt:
        outofdate[model] = model_last_updated_dt

# sort by date, descending
sorted_outofdate = sorted(outofdate.items(), key=lambda item: item[1], reverse=True)

for model, updated in sorted_outofdate:
    print(f"- {model} was last updated on {updated.strftime('%Y-%m-%d %H:%M:%S')}")
```

## Table of Contents
```{tableofcontents}
```
