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
223P was last updated on 2025-04-11 13:03:25. The model file was last updated on 2024-09-15 23:37:32
```
        
# ASHRAE Guideline 36-2021 A-4 Parallel Fan-Powered Terminal Unit, Variable Volume Fan

This component model is an example of the parallel fan-powered terminal unit with variable volume fan from Guideline 36-2021, Appendix A, Figure A-4.

## Downloads

- <a href="/compiled/guideline36-2021-A-4.ttl">Turtle file (compiled)</a>
- <a href="/withimports/guideline36-2021-A-4.ttl">Turtle file (with all imports)</a>
- <a href="/guideline36-2021-A-4.ttl">Turtle file (original)</a>
- <a href="/guideline36-2021-A-4.jsonld">JSON-LD file (original)</a>
    
## Model Components
| Parent Class | Class | Instances |
|------------|-------|----------------|
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Sensor](https://explore.open223.info/s223/Sensor.html) | 4 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Actuator](https://explore.open223.info/s223/Actuator.html) | 2 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Damper](https://explore.open223.info/s223/Damper.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [HeatingCoil](https://explore.open223.info/s223/HeatingCoil.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Fan](https://explore.open223.info/s223/Fan.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Valve](https://explore.open223.info/s223/Valve.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [FanPoweredTerminal](https://explore.open223.info/s223/FanPoweredTerminal.html) | 1 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [Duct](https://explore.open223.info/s223/Duct.html) | 5 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [Pipe](https://explore.open223.info/s223/Pipe.html) | 1 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [InletConnectionPoint](https://explore.open223.info/s223/InletConnectionPoint.html) | 11 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [OutletConnectionPoint](https://explore.open223.info/s223/OutletConnectionPoint.html) | 9 |
| [DomainSpace](https://explore.open223.info/s223/DomainSpace.html) | [](https://explore.open223.info/s223/.html) | 1 |
| [Zone](https://explore.open223.info/s223/Zone.html) | [](https://explore.open223.info/s223/.html) | 1 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableObservableProperty](https://explore.open223.info/s223/QuantifiableObservableProperty.html) | 8 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableProperty](https://explore.open223.info/s223/QuantifiableProperty.html) | 6 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableActuatableProperty](https://explore.open223.info/s223/QuantifiableActuatableProperty.html) | 3 |
| [Property](https://explore.open223.info/s223/Property.html) | [EnumeratedActuatableProperty](https://explore.open223.info/s223/EnumeratedActuatableProperty.html) | 1 |
| [Property](https://explore.open223.info/s223/Property.html) | [EnumeratedObservableProperty](https://explore.open223.info/s223/EnumeratedObservableProperty.html) | 1 |


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
model = Model.create("urn:guideline36-2021-A-4")
model.graph.parse("https://models.open223.info/guideline36-2021-A-4.ttl")

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
