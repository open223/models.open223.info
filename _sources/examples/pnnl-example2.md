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

```{warning}
This model has not been updated since the last revision of the 223P ontology, and it may not pass validation.
223P was last updated on 2024-08-21 17:06:22. The model file was last updated on 2024-08-21 17:06:22
```
        
# PNNL Example Building 2

This is an example building model provided by Pacific Northwest National Laboratory.

The model is based on a [Department of Energy Prototype Builiding](https://www.energycodes.gov/prototype-building-models) model. 
Specifically, the DOE Prototype Medium Office Building was extended by creating unique detailed building architecture for each of the three building floors,
and designing a lighting layout that complies with the ASHRAE 90.1-2019 energy code.

The model contains a representation of the building architecture and lighting system.

In addition to the s223 ontology, the model uses the [Real Estate Core ontology](https://dev.realestatecore.io/ontology/) to describe space types.

## Source

The model was created from souce data consisting of a Revit building information model (BIM) exported via a [Speckle](https://speckle.systems/) interface.

### The Speckle view of rooms and lighting fixtures
<img width="1178" alt="image" src="https://github.com/open223/models.open223.info/assets/22898727/5a5dcecb-9b87-4e84-8261-6a3a315e1265">

Model instance data have a prefix that is resolvable to a Speckle URL.
``` ttl
@prefix bdg1: <http://speckle.xyz/streams/1fed8e620e/objects/>
```

For example, the following luminaire resolves to https://speckle.xyz/streams/1fed8e620e/objects/05749166d93671bedf16efb52636ce38 :
```ttl
bdg1:05749166d93671bedf16efb52636ce38 a s223:Luminaire
```

## Downloads

- <a href="/compiled/pnnl-example2.ttl">Turtle file (compiled)</a> (<a href="/pnnl-example2.ttl">original</a>)
- <a href="/pnnl-example2.jsonld">JSON-LD file (original)</a>
    
## Queries

## Model Components
| Parent Class | Class | Instances |
|------------|-------|----------------|
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Luminaire](https://explore.open223.info/s223/Luminaire.html) | 853 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [ElectricBreaker](https://explore.open223.info/s223/ElectricBreaker.html) | 3 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [ElectricWire](https://explore.open223.info/s223/ElectricWire.html) | 856 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [OutletConnectionPoint](https://explore.open223.info/s223/OutletConnectionPoint.html) | 1709 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [InletConnectionPoint](https://explore.open223.info/s223/InletConnectionPoint.html) | 1709 |
| [DomainSpace](https://explore.open223.info/s223/DomainSpace.html) | [](https://explore.open223.info/s223/.html) | 311 |
| [Zone](https://explore.open223.info/s223/Zone.html) | [](https://explore.open223.info/s223/.html) | 220 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableProperty](https://explore.open223.info/s223/QuantifiableProperty.html) | 394 |


## Load and Validate Model

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


```{code-cell} python3
from buildingmotif import BuildingMOTIF
from buildingmotif.dataclasses import Library, Model
import logging

# Create a BuildingMOTIF object. If you do not have Java installed, remove the "shacl_engine" parameter
bm = BuildingMOTIF('sqlite://', shacl_engine='topquadrant', log_level=logging.ERROR)

# load 223P library. We will load a recent copy from the models.open223.info
# git repository; later, we will load this from the location of the actual standard
s223 = Library.load(ontology_graph="https://github.com/open223/models.open223.info/raw/main/ontologies/223p.ttl")

# load the model into the BuildingMOTIF instance
model = Model.create("urn:pnnl-example2")
model.graph.parse("https://models.open223.info/pnnl-example2.ttl")

# validate the model against 223P ontology
ctx = model.validate([s223.get_shape_collection()], error_on_missing_imports=False)

# print the validation result
print(f"Model is valid: {ctx.valid}")

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

```
