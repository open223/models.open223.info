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
223P was last updated on 2025-04-17 14:15:45. The model file was last updated on 2024-09-14 12:12:25
```
        
# PNNL Example Building 2 Model 1

Exammple Building 2 is based on the [Department of Energy Prototype Medium Office Builiding](https://www.energycodes.gov/prototype-building-models). 
The baseline Medium Office Building is approximately 50,000 square feet in size, contains 3 identical floors, and 5 HVAC zones per floor (1 core, 4 perimeter). The baseline model was extended by a) creating unique detailed building architecture for each of the 3 building floors, making use of 12 space types to define 107 rooms, and b) designing a lighting system that complies with the ASHRAE 90.1-2019 energy code, and is comprised of 863 luminaires and 205 lighting zones.

Example Building 2 Model 1 is provided by Pacific Northwest National Laboratory.

## Contents

This model contains a complete representation of the building architecture and the electrical/lighting system, and a partial representation of the lighting control system.

In addition to the s223 ontology, the model uses the [Real Estate Core ontology](https://dev.realestatecore.io/ontology/) to describe space types. The Real Estate Core ontology is extended by defining 2 subclasses for rec:Office.
``` ttl
recx:OpenOffice rdfs:subClassOf rec:Office;
  rdfs:label "Open Office".
recx:PrivateOffice rdfs:subClassOf rec:Office;
  rdfs:label "Private Office".
```

## Source

The model was created from souce data consisting of a Revit building information model (BIM) exported via a [Speckle](https://speckle.systems/) interface.

### Speckle view of rooms and lighting fixtures
<img width="1178" alt="image" src="https://github.com/open223/models.open223.info/assets/22898727/5a5dcecb-9b87-4e84-8261-6a3a315e1265">

Model instance data have a prefix that is resolvable to a Speckle URL.
``` ttl
@prefix bdg2: <http://speckle.xyz/streams/1fed8e620e/objects/>
```

For example, the following luminaire resolves to http://speckle.xyz/streams/1fed8e620e/objects/b504da73194fd2dafccc5e91651e2066 :
```ttl
bdg2:b504da73194fd2dafccc5e91651e2066 a s223:Luminaire
```

## Downloads

- <a href="/compiled/pnnl-bdg2-1.ttl">Turtle file (compiled)</a>
- <a href="/withimports/pnnl-bdg2-1.ttl">Turtle file (with all imports)</a>
- <a href="/pnnl-bdg2-1.ttl">Turtle file (original)</a>
- <a href="/pnnl-bdg2-1.jsonld">JSON-LD file (original)</a>

<details>
<summary>What are these files?</summary>

- **Turtle file (original)**: This is the original source Turtle file that was provided to `models.open223.info`, usually as the output of some model creation tool.
- **Turtle file (compiled)**: This is the original Turtle file with all inferred relationships and values added through SHACL inference against the 223P ontology and other dependencies. **You should use this file for any further processing.** It does not contain any of the ontologies.
- **Turtle file (with all imports)**: This is the compiled Turtle file with all imports included in the file (223P ontology, QUDT ontology, and others). This is helpful when you do not want to deal with downloading and managing ontology dependencies. It is also much larger than the compiled file.
- **JSON-LD file (original)**: This is the original Turtle file converted to the JSON-LD format.

[Turtle](https://www.w3.org/TR/turtle/) is a syntax for RDF (Resource Description Framework) that is easy to read and write. It is a popular format for representing linked data. Parsers and serializers 
are available in many programming languages. [JSON-LD](https://json-ld.org) is a JSON-based format for linked data that is easy to use with JavaScript and other web technologies.
</details>
    
## Queries
| Description | Query URL |
|-------------|-----------|
| Select all triples from model. | <a href='https://query.open223.info/?query=PREFIX+s223%3A+%3Chttp%3A%2F%2Fdata.ashrae.org%2Fstandard223%23%3E+PREFIX+unit%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Funit%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+quantitykind%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Fquantitykind%2F%3E+PREFIX+qudt%3A+%3Chttp%3A%2F%2Fqudt.org%2Fschema%2Fqudt%2F%3E+PREFIX+sh%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fshacl%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+%0ASELECT+%2A+WHERE+%7B%0A%09+%3Fs+%3Fp+%3Fo+%0A%7D%0A+LIMIT+10&url=https%3A%2F%2Fmodels.open223.info%2Fcompiled%2Fpnnl-bdg2-1.ttl'>Query Link</a> |

## Model Components
| Parent Class | Class | Instances |
|------------|-------|----------------|
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Luminaire](https://explore.open223.info/s223/Luminaire.html) | 853 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [OccupantMotionSensor](https://explore.open223.info/s223/OccupantMotionSensor.html) | 204 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [ElectricBreaker](https://explore.open223.info/s223/ElectricBreaker.html) | 3 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [ElectricWire](https://explore.open223.info/s223/ElectricWire.html) | 856 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [OutletConnectionPoint](https://explore.open223.info/s223/OutletConnectionPoint.html) | 1709 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [InletConnectionPoint](https://explore.open223.info/s223/InletConnectionPoint.html) | 1709 |
| [DomainSpace](https://explore.open223.info/s223/DomainSpace.html) | [](https://explore.open223.info/s223/.html) | 311 |
| [Zone](https://explore.open223.info/s223/Zone.html) | [](https://explore.open223.info/s223/.html) | 219 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableProperty](https://explore.open223.info/s223/QuantifiableProperty.html) | 396 |
| [Property](https://explore.open223.info/s223/Property.html) | [EnumeratedObservableProperty](https://explore.open223.info/s223/EnumeratedObservableProperty.html) | 204 |


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
model = Model.create("urn:pnnl-bdg2-1")
model.graph.parse("https://models.open223.info/pnnl-bdg2-1.ttl")

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
