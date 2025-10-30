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

- 223P was last updated on 2025-10-30 08:50:00
- model file was last updated on 2024-09-12 16:11:46
```
        


#  Heat Pump Laboratory (HPL)

The HPL is a lab at NIST that consists of a bi-directional indoor and outdoor air system.

### Schematic view

![image](../_static/images/hpl_schematic.png)

## Downloads

- <a href="/compiled/NIST-HPL.ttl">Turtle file (compiled)</a>
- <a href="/withimports/NIST-HPL.ttl">Turtle file (with all imports)</a>
- <a href="/NIST-HPL.ttl">Turtle file (original)</a>
- <a href="/NIST-HPL.jsonld">JSON-LD file (original)</a>

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
| Find the downstream equipment for AHU1. | <a href='https://query.open223.info/?query=PREFIX+s223%3A+%3Chttp%3A%2F%2Fdata.ashrae.org%2Fstandard223%23%3E+PREFIX+unit%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Funit%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+quantitykind%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Fquantitykind%2F%3E+PREFIX+qudt%3A+%3Chttp%3A%2F%2Fqudt.org%2Fschema%2Fqudt%2F%3E+PREFIX+sh%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fshacl%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+SELECT+%3FconnectionDown+%3FconnectionDown2+WHERE+%7B%0A++++BIND%28IBAL%3AAHU_1+as+%3Fahu%29+%7B%0A%09%7D%0A%09UNION+%7B%0A%09%3Fahu+s223%3AhasConnectionPoint+%3FconnectionPoint+.%0A%09%3FconnectionPoint+a+s223%3AOutletConnectionPoint+.%0A%09%3FconnectionPoint+s223%3AhasMedium+s223%3AMedium-Air+.%0A%09%3FconnectionPoint+s223%3AconnectsThrough+%3Fsegment+.%0A%09%3Fsegment+s223%3AconnectsTo+%3Fjunction+.%0A++++%3Fjunction+s223%3AconnectedTo+%3FconnectionDown+.%0A++++%3FconnectionDown+a+s223%3ATerminalUnit+.%0A%09%7D%0A%09UNION+%7B%0A%09%3Fahu+s223%3AhasConnectionPoint+%3FconnectionPoint+.%0A%09%3FconnectionPoint+a+s223%3AOutletConnectionPoint+.%0A%09%3FconnectionPoint+s223%3AhasMedium+s223%3AMedium-Air+.%0A%09%3FconnectionPoint+s223%3AconnectsThrough+%3Fsegment+.%0A%09%3Fsegment+s223%3AconnectsTo+%3Fjunction+.%0A++++%3Fjunction+s223%3AconnectedTo+%3FconnectionDown+.%0A++++%3FconnectionDown+a+s223%3AJunction+.%0A%09%3FconnectionDown+s223%3AconnectedTo+%3FconnectionDown2+.%0A%09%3FconnectionDown2+a+s223%3ATerminalUnit+.%0A%09%7D%0A%7D%0A&url=https%3A%2F%2Fmodels.open223.info%2Fwithimports%2Fnist-hpl.ttl'>Query Link</a> |

## Model Components
| Parent Class | Class | Instances |
|------------|-------|----------------|
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [TemperatureSensor](https://explore.open223.info/s223/TemperatureSensor.html) | 34 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [PressureSensor](https://explore.open223.info/s223/PressureSensor.html) | 8 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Sensor](https://explore.open223.info/s223/Sensor.html) | 3 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [HumiditySensor](https://explore.open223.info/s223/HumiditySensor.html) | 3 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Fan](https://explore.open223.info/s223/Fan.html) | 3 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Valve](https://explore.open223.info/s223/Valve.html) | 3 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [FlowSensor](https://explore.open223.info/s223/FlowSensor.html) | 2 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [HeatExchanger](https://explore.open223.info/s223/HeatExchanger.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Coil](https://explore.open223.info/s223/Coil.html) | 1 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [Pipe](https://explore.open223.info/s223/Pipe.html) | 10 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [Duct](https://explore.open223.info/s223/Duct.html) | 9 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [BidirectionalConnectionPoint](https://explore.open223.info/s223/BidirectionalConnectionPoint.html) | 20 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [OutletConnectionPoint](https://explore.open223.info/s223/OutletConnectionPoint.html) | 15 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [InletConnectionPoint](https://explore.open223.info/s223/InletConnectionPoint.html) | 15 |
| [DomainSpace](https://explore.open223.info/s223/DomainSpace.html) | [](https://explore.open223.info/s223/.html) | 1 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableObservableProperty](https://explore.open223.info/s223/QuantifiableObservableProperty.html) | 52 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableProperty](https://explore.open223.info/s223/QuantifiableProperty.html) | 6 |


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
model = Model.create("urn:NIST-HPL")
model.graph.parse("https://models.open223.info/NIST-HPL.ttl")

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
