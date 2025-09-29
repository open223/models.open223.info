---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: open223-models
  language: python
  name: open223-models
---

```{warning}
This model has not been updated since the last revision of the 223P ontology and it may not pass validation.

- 223P was last updated on 2025-09-29 14:39:40
- model file was last updated on 2024-09-14 12:12:25
```
        
# PNNL Example Building 3 Model 2

Exammple Building 3 is a real-world medium-sized office building. 
It is approximately 67,000 square feet in size, contains 2 floors, 27 space types, and 469 rooms. Labels have been anonymized, and are not interpretable. 
It uses an underfloor air distribution system with fan-powered terminal reheat coils for perimeter zones. Four roof-top units with VAV are located on the roof. 
The lighting system primariliy uses fluorescent luminaires and zone-based lighting controllers that communicate with user interface devices and wireless gatetways over DALI networks. The gateways collect occupancy and light sensor data over an ISM-band wireless network. 

Example Building 3 Model 2 is provided by Pacific Northwest National Laboratory.
See [LBNL Example Building 3 model 1](lbnl-bdg3-2.md) for a different modeling approach for the same building.

## Contents

This model contains a complete representation of the building architecture and electrical/lighting system, and a partial representation of the lighting control system.

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
<img width="1378" alt="image" src="https://github.com/user-attachments/assets/57981a65-937a-4c4b-9151-978073976d14">

Model instance data have a prefix that is resolvable to a Speckle URL.
``` ttl
@prefix bdg3: <http://speckle.xyz/streams/bf7685a6aa/objects/>
```

For example, the following luminaire resolves to http://speckle.xyz/streams/bf7685a6aa/objects/978e64f766e711a6cc73f3a4d4c0a3e9 :
```ttl
bdg3:978e64f766e711a6cc73f3a4d4c0a3e9 a s223:Luminaire
```

## Downloads

- <a href="/compiled/pnnl-bdg3-2.ttl">Turtle file (compiled)</a>
- <a href="/withimports/pnnl-bdg3-2.ttl">Turtle file (with all imports)</a>
- <a href="/pnnl-bdg3-2.ttl">Turtle file (original)</a>
- <a href="/pnnl-bdg3-2.jsonld">JSON-LD file (original)</a>

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
| Select all triples from model. | <a href='https://query.open223.info/?query=PREFIX+s223%3A+%3Chttp%3A%2F%2Fdata.ashrae.org%2Fstandard223%23%3E+PREFIX+unit%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Funit%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+quantitykind%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Fquantitykind%2F%3E+PREFIX+qudt%3A+%3Chttp%3A%2F%2Fqudt.org%2Fschema%2Fqudt%2F%3E+PREFIX+sh%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fshacl%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+%0ASELECT+%2A+WHERE+%7B%0A%09+%3Fs+%3Fp+%3Fo+%0A%7D%0A+LIMIT+10&url=https%3A%2F%2Fmodels.open223.info%2Fwithimports%2Fpnnl-bdg3-2.ttl'>Query Link</a> |

## Model Components
| Parent Class | Class | Instances |
|------------|-------|----------------|
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Luminaire](https://explore.open223.info/s223/Luminaire.html) | 713 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [OccupantMotionSensor](https://explore.open223.info/s223/OccupantMotionSensor.html) | 226 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [ElectricBreaker](https://explore.open223.info/s223/ElectricBreaker.html) | 26 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [ElectricWire](https://explore.open223.info/s223/ElectricWire.html) | 739 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [OutletConnectionPoint](https://explore.open223.info/s223/OutletConnectionPoint.html) | 1452 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [InletConnectionPoint](https://explore.open223.info/s223/InletConnectionPoint.html) | 1452 |
| [DomainSpace](https://explore.open223.info/s223/DomainSpace.html) | [](https://explore.open223.info/s223/.html) | 245 |
| [Zone](https://explore.open223.info/s223/Zone.html) | [](https://explore.open223.info/s223/.html) | 236 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableProperty](https://explore.open223.info/s223/QuantifiableProperty.html) | 443 |
| [Property](https://explore.open223.info/s223/Property.html) | [EnumeratedObservableProperty](https://explore.open223.info/s223/EnumeratedObservableProperty.html) | 226 |


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
import ontoenv
import logging

# Create a BuildingMOTIF object. If you do not have Java installed, remove the "shacl_engine" parameter
bm = BuildingMOTIF('sqlite://', shacl_engine='topquadrant', log_level=logging.ERROR)

# load 223P library. We will load a recent copy from the models.open223.info
# git repository; later, we will load this from the location of the actual standard
s223 = Library.load(ontology_graph="https://open223.info/223p.ttl", infer_templates=False, run_shacl_inference=False)
unit = Library.load(ontology_graph="http://qudt.org/3.1.1/vocab/unit", infer_templates=False, run_shacl_inference=False)
quantitykind = Library.load(ontology_graph="http://qudt.org/3.1.1/vocab/quantitykind", infer_templates=False, run_shacl_inference=False)

# load the model into the BuildingMOTIF instance
model = Model.create("urn:pnnl-bdg3-2")
model.graph.parse("https://models.open223.info/pnnl-bdg3-2.ttl")

# validate the model against 223P ontology
ctx = model.validate([s223.get_shape_collection(),
                      unit.get_shape_collection(),
                      quantitykind.get_shape_collection()],
                     error_on_missing_imports=False)

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
