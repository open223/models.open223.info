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

````{margin}
```{note}
Publication document is not yet publicly published
```
````

```{code-cell} python3
:tags: [remove-cell]
from datetime import datetime
import glob
import os
from myst_nb import glue
last_updated = os.path.getmtime("ontologies/223p.ttl")
last_updated_formatted = datetime.fromtimestamp(last_updated).strftime("%Y-%m-%d %H:%M:%S")
glue("last_updated", last_updated_formatted)
```

This site contains example buildings, systems, and other assets modeled in 223 with supporting documentation.

The 223P ontology used to build this site was last updated at **{glue:text}`last_updated`**.

The following models may be out of date with the latest 223P:

```{code-cell} python3
:tags: [remove-input]
# loop through all the models and find the last time they were updated
# on the file system
models = glob.glob("models/*.ttl")
outofdate = {}
for model in models:
    # if the modified time is after the last_updated time,
    # then add the model to the last_updated dictionary
    if os.path.getmtime(model) < last_updated:
        outofdate[model] = os.path.getmtime(model)

display_out_of_date_models = "The following models may be out of date with the latest 223P: \n"
for model, updated in outofdate.items():
    print(f"{model} was last updated on {datetime.fromtimestamp(updated).strftime('%Y-%m-%d %H:%M:%S')}")
```

## Table of Contents
```{tableofcontents}
```
