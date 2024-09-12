---ntelligent Buildings Agents Laboratory (IBAL)

The IBAL is a mixed system lab at NIST that is able to test commercial equipment under simulated conditions. For more information, vist the [IBAL Database](https://ibal.nist.gov/). 

### Schematic view

![image](../_static/images/ibal_schematic.png)

## Downloads

- <a href="/compiled/NIST-IBAL.ttl">Turtle file (compiled)</a> (<a href="/NIST-IBAL.ttl">original</a>)
- <a href="/NIST-IBAL.jsonld">JSON-LD file (original)</a>
    
## Queries

## Model Components
| Parent Class | Class | Instances |
|---
---------|-------|----------------|
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Actuator](https://explore.open223.info/s223/Actuator.html) | 90 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [TemperatureSensor](https://explore.open223.info/s223/TemperatureSensor.html) | 57 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [FlowSensor](https://explore.open223.info/s223/FlowSensor.html) | 28 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [PressureSensor](https://explore.open223.info/s223/PressureSensor.html) | 21 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Damper](https://explore.open223.info/s223/Damper.html) | 19 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Sensor](https://explore.open223.info/s223/Sensor.html) | 19 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Controller](https://explore.open223.info/s223/Controller.html) | 12 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [TwoWayValve](https://explore.open223.info/s223/TwoWayValve.html) | 12 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [VariableFrequencyDrive](https://explore.open223.info/s223/VariableFrequencyDrive.html) | 10 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [HumiditySensor](https://explore.open223.info/s223/HumiditySensor.html) | 9 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [ThreeWayValve](https://explore.open223.info/s223/ThreeWayValve.html) | 9 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [HeatExchanger](https://explore.open223.info/s223/HeatExchanger.html) | 7 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [HeatingCoil](https://explore.open223.info/s223/HeatingCoil.html) | 7 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Pump](https://explore.open223.info/s223/Pump.html) | 5 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Fan](https://explore.open223.info/s223/Fan.html) | 5 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [TerminalUnit](https://explore.open223.info/s223/TerminalUnit.html) | 4 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [AirHandlingUnit](https://explore.open223.info/s223/AirHandlingUnit.html) | 3 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [CoolingCoil](https://explore.open223.info/s223/CoolingCoil.html) | 3 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Chiller](https://explore.open223.info/s223/Chiller.html) | 2 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Filter](https://explore.open223.info/s223/Filter.html) | 2 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Valve](https://explore.open223.info/s223/Valve.html) | 1 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [Pipe](https://explore.open223.info/s223/Pipe.html) | 1 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [InletConnectionPoint](https://explore.open223.info/s223/InletConnectionPoint.html) | 226 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [OutletConnectionPoint](https://explore.open223.info/s223/OutletConnectionPoint.html) | 221 |
| [ExternalReference](https://explore.open223.info/s223/ExternalReference.html) | [BACnetExternalReference](https://explore.open223.info/s223/BACnetExternalReference.html) | 66 |
| [DomainSpace](https://explore.open223.info/s223/DomainSpace.html) | [](https://explore.open223.info/s223/.html) | 4 |
| [Zone](https://explore.open223.info/s223/Zone.html) | [](https://explore.open223.info/s223/.html) | 6 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableObservableProperty](https://explore.open223.info/s223/QuantifiableObservableProperty.html) | 151 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableActuatableProperty](https://explore.open223.info/s223/QuantifiableActuatableProperty.html) | 99 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableProperty](https://explore.open223.info/s223/QuantifiableProperty.html) | 10 |


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
model = Model.create("urn:NIST-IBAL")
model.graph.parse("https://models.open223.info/NIST-IBAL.ttl")

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
