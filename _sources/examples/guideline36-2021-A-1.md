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
- model file was last updated on 2025-08-04 10:27:34
```
        
# ASHRAE Guideline 36-2021 A-1 VAV Terminal Unit, Cooling Only

This component model is an example of the variable air volume (VAV) terminal unit with cooling only from Guideline 36-2021, Appendix A, Figure A-1.

## Downloads

- <a href="/compiled/guideline36-2021-A-1.ttl">Turtle file (compiled)</a>
- <a href="/withimports/guideline36-2021-A-1.ttl">Turtle file (with all imports)</a>
- <a href="/guideline36-2021-A-1.ttl">Turtle file (original)</a>
- <a href="/guideline36-2021-A-1.jsonld">JSON-LD file (original)</a>

<details>
<summary>What are these files?</summary>

- **Turtle file (original)**: This is the original source Turtle file that was provided to `models.open223.info`, usually as the output of some model creation tool.
- **Turtle file (compiled)**: This is the original Turtle file with all inferred relationships and values added through SHACL inference against the 223P ontology and other dependencies. **You should use this file for any further processing.** It does not contain any of the ontologies.
- **Turtle file (with all imports)**: This is the compiled Turtle file with all imports included in the file (223P ontology, QUDT ontology, and others). This is helpful when you do not want to deal with downloading and managing ontology dependencies. It is also much larger than the compiled file.
- **JSON-LD file (original)**: This is the original Turtle file converted to the JSON-LD format.

[Turtle](https://www.w3.org/TR/turtle/) is a syntax for RDF (Resource Description Framework) that is easy to read and write. It is a popular format for representing linked data. Parsers and serializers
are available in many programming languages. [JSON-LD](https://json-ld.org) is a JSON-based format for linked data that is easy to use with JavaScript and other web technologies.
</details>

## Model Components
| Parent Class | Class | Instances |
|------------|-------|----------------|
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Actuator](https://explore.open223.info/s223/Actuator.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Damper](https://explore.open223.info/s223/Damper.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Sensor](https://explore.open223.info/s223/Sensor.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [SingleDuctTerminal](https://explore.open223.info/s223/SingleDuctTerminal.html) | 1 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [Duct](https://explore.open223.info/s223/Duct.html) | 2 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [OutletConnectionPoint](https://explore.open223.info/s223/OutletConnectionPoint.html) | 3 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [InletConnectionPoint](https://explore.open223.info/s223/InletConnectionPoint.html) | 3 |
| [DomainSpace](https://explore.open223.info/s223/DomainSpace.html) | [](https://explore.open223.info/s223/.html) | 1 |
| [Zone](https://explore.open223.info/s223/Zone.html) | [](https://explore.open223.info/s223/.html) | 1 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableProperty](https://explore.open223.info/s223/QuantifiableProperty.html) | 6 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableObservableProperty](https://explore.open223.info/s223/QuantifiableObservableProperty.html) | 4 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableActuatableProperty](https://explore.open223.info/s223/QuantifiableActuatableProperty.html) | 1 |


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
model = Model.create("urn:guideline36-2021-A-1")
model.graph.parse("https://models.open223.info/guideline36-2021-A-1.ttl")

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
