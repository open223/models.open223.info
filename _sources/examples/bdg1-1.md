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
        
# Example Building 1 model 1

Example Building 1 is a simplistic, reference tiny office building consisting of a single story with 5 rooms spanning 5 space types.

This reference building was developed for and first described in the journal article ["Metadata Schemas and Ontologies for Building Energy Applications: A Critical Review and Use Case Analysis"](https://doi.org/10.3390/en14072024).

This example Building 1 model 1 is provided by current and former NIST staff and Pacific Northwest National Laboratory. See also [Building 1 model 2](../bdg1-2.md) for a different modeling approach for the same building.

### Schematic view

![image](../_static/images/ExampleBuilding1.png)

## Contents

The model contains a representation of the building architecture, mechanical system, and electrical/lighting system.

## Source

The model was created using [TopQuadrant](https://www.topquadrant.com/) TopBraid Composer Maestro Edition.

## Downloads

- <a href="/compiled/bdg1-1.ttl">Turtle file (compiled)</a> (<a href="/bdg1-1.ttl">original</a>)
- <a href="/bdg1-1.jsonld">JSON-LD file (original)</a>
    
## Queries

## Model Components
| Parent Class | Class | Instances |
|------------|-------|----------------|
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Actuator](https://explore.open223.info/s223/Actuator.html) | 12 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Luminaire](https://explore.open223.info/s223/Luminaire.html) | 12 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [TemperatureSensor](https://explore.open223.info/s223/TemperatureSensor.html) | 10 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [ElectricBreaker](https://explore.open223.info/s223/ElectricBreaker.html) | 6 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Damper](https://explore.open223.info/s223/Damper.html) | 6 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [HeatingCoil](https://explore.open223.info/s223/HeatingCoil.html) | 3 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [FlowSensor](https://explore.open223.info/s223/FlowSensor.html) | 3 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Fan](https://explore.open223.info/s223/Fan.html) | 3 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Valve](https://explore.open223.info/s223/Valve.html) | 3 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [PressureSensor](https://explore.open223.info/s223/PressureSensor.html) | 2 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [OccupantMotionSensor](https://explore.open223.info/s223/OccupantMotionSensor.html) | 2 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [OccupantPresenceSensor](https://explore.open223.info/s223/OccupantPresenceSensor.html) | 2 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [SingleDuctTerminal](https://explore.open223.info/s223/SingleDuctTerminal.html) | 2 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [AirHandlingUnit](https://explore.open223.info/s223/AirHandlingUnit.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Boiler](https://explore.open223.info/s223/Boiler.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Chiller](https://explore.open223.info/s223/Chiller.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Filter](https://explore.open223.info/s223/Filter.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Generator](https://explore.open223.info/s223/Generator.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Thermostat](https://explore.open223.info/s223/Thermostat.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Window](https://explore.open223.info/s223/Window.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [CoolingCoil](https://explore.open223.info/s223/CoolingCoil.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Sensor](https://explore.open223.info/s223/Sensor.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [IlluminanceSensor](https://explore.open223.info/s223/IlluminanceSensor.html) | 1 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [OccupantCounter](https://explore.open223.info/s223/OccupantCounter.html) | 1 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [ElectricWire](https://explore.open223.info/s223/ElectricWire.html) | 10 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [Duct](https://explore.open223.info/s223/Duct.html) | 1 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [Pipe](https://explore.open223.info/s223/Pipe.html) | 1 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [InletConnectionPoint](https://explore.open223.info/s223/InletConnectionPoint.html) | 71 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [OutletConnectionPoint](https://explore.open223.info/s223/OutletConnectionPoint.html) | 68 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [BidirectionalConnectionPoint](https://explore.open223.info/s223/BidirectionalConnectionPoint.html) | 2 |
| [FunctionBlock](https://explore.open223.info/s223/FunctionBlock.html) | [](https://explore.open223.info/s223/.html) | 3 |
| [PhysicalSpace](https://explore.open223.info/s223/PhysicalSpace.html) | [OutsidePhysicalSpace](https://explore.open223.info/s223/OutsidePhysicalSpace.html) | 1 |
| [DomainSpace](https://explore.open223.info/s223/DomainSpace.html) | [](https://explore.open223.info/s223/.html) | 19 |
| [Zone](https://explore.open223.info/s223/Zone.html) | [](https://explore.open223.info/s223/.html) | 8 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableObservableProperty](https://explore.open223.info/s223/QuantifiableObservableProperty.html) | 20 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableActuatableProperty](https://explore.open223.info/s223/QuantifiableActuatableProperty.html) | 18 |
| [Property](https://explore.open223.info/s223/Property.html) | [EnumerableProperty](https://explore.open223.info/s223/EnumerableProperty.html) | 16 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableProperty](https://explore.open223.info/s223/QuantifiableProperty.html) | 14 |
| [Property](https://explore.open223.info/s223/Property.html) | [EnumeratedActuatableProperty](https://explore.open223.info/s223/EnumeratedActuatableProperty.html) | 5 |
| [Property](https://explore.open223.info/s223/Property.html) | [EnumeratedObservableProperty](https://explore.open223.info/s223/EnumeratedObservableProperty.html) | 4 |


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
model = Model.create("urn:bdg1-1")
model.graph.parse("https://models.open223.info/bdg1-1.ttl")

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
