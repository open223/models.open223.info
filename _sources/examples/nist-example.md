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
223P was last updated on 2024-08-20 22:45:44. The model file was last updated on 2024-08-20 22:45:44
```
        
# NIST Example Building

This is a model of the Intelligent Buildings Agents Laboratory (IBAL) at NIST.

The schematics of the air and hydronic systems can be found [here](../_static/schematics/nist-example.pdf)

## Downloads

- <a href="/compiled/nist-example.ttl">Turtle file (compiled)</a> (<a href="/nist-example.ttl">original</a>)
- <a href="/nist-example.jsonld">JSON-LD file (original)</a>
    
## Queries
| Description | Query URL |
|-------------|-----------|
| Zone/room temperature sensors | <a href='https://query.open223.info/?query=PREFIX+s223%3A+%3Chttp%3A%2F%2Fdata.ashrae.org%2Fstandard223%23%3E+PREFIX+unit%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Funit%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+quantitykind%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Fquantitykind%2F%3E+PREFIX+qudt%3A+%3Chttp%3A%2F%2Fqudt.org%2Fschema%2Fqudt%2F%3E+PREFIX+sh%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fshacl%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+SELECT+%3Flocation+%3Fsensor+WHERE+%7B%0A++++%3Fsensor+rdf%3Atype%2Frdfs%3AsubClassOf%2A+s223%3ASensor+.%0A++++%3Fsensor+s223%3Aobserves+%3Fproperty+.%0A++++%3Fproperty+qudt%3AhasQuantityKind+quantitykind%3ATemperature+.%0A++++%3Fsensor+s223%3AhasObservationLocation+%3Flocation%0A%7D%0A&url=https%3A%2F%2Fmodels.open223.info%2Fcompiled%2Fnist-example.ttl'>Query Link</a> |
| Search for all the sensors along the connections and the associated property they're observing. | <a href='https://query.open223.info/?query=PREFIX+s223%3A+%3Chttp%3A%2F%2Fdata.ashrae.org%2Fstandard223%23%3E+PREFIX+unit%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Funit%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+quantitykind%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Fquantitykind%2F%3E+PREFIX+qudt%3A+%3Chttp%3A%2F%2Fqudt.org%2Fschema%2Fqudt%2F%3E+PREFIX+sh%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fshacl%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+SELECT+%3Fsegment+%3Fchannel+%3Fproperty_id+WHERE+%7B%0A++++%3Fsegment+a+s223%3AConnection+.%0A++++%3Fchannel+a%2Frdfs%3AsubClassOf%2A+s223%3ASensor+.%0A++++%3Fchannel+s223%3Aobserves+%3Fproperty_id+.%0A%7D%0A&url=https%3A%2F%2Fmodels.open223.info%2Fcompiled%2Fnist-example.ttl'>Query Link</a> |
| Sensors in AHU1 and what units the properties are measured in | <a href='https://query.open223.info/?query=PREFIX+s223%3A+%3Chttp%3A%2F%2Fdata.ashrae.org%2Fstandard223%23%3E+PREFIX+unit%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Funit%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+quantitykind%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Fquantitykind%2F%3E+PREFIX+qudt%3A+%3Chttp%3A%2F%2Fqudt.org%2Fschema%2Fqudt%2F%3E+PREFIX+sh%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fshacl%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+SELECT+%3Fchannel+%3Fproperty_id+%3Funit+WHERE+%7B%0A++++BIND%28IBAL%3AAHU_1+as+%3Fahu%29+%7B%0A++++%7D%0A++++UNION+%7B%0A++++++++%3Fahu+s223%3Acontains+%3Fequipment+.%0A++++++++%3Fchannel+s223%3AhasObservationLocation+%3Fequipment+.%0A++++++++%3Fchannel+s223%3Aobserves+%3Fproperty_id+.%0A++++++++%3Fproperty_id+qudt%3AhasUnit+%3Funit+.%0A++++%7D%0A++++UNION+%7B%0A++++++++%3Fahu+s223%3Acontains+%3Fequipment+.%0A++++++++%3Fequipment+s223%3AconnectedThrough+%3Fconnection+.%0A++++++++%3Fchannel+s223%3AhasObservationLocation+%3Fconnection+.%0A++++++++%3Fchannel+s223%3Aobserves+%3Fproperty_id+.%0A++++++++%3Fproperty_id+qudt%3AhasUnit+%3Funit+.%0A++++%7D%0A++++UNION+%7B%0A++++++++%3Fahu+s223%3Acontains+%3Fequipment+.%0A++++++++%3Fequipment+s223%3AhasConnectionPoint+%3FconnectionPoint+.%0A++++++++%3Fchannel+s223%3AhasObservationLocation+%3FconnectionPoint+.%0A++++++++%3Fchannel+s223%3Aobserves+%3Fproperty_id+.%0A++++++++%3Fproperty_id+qudt%3AhasUnit+%3Funit+.%0A++++%7D%0A%7D%0A&url=https%3A%2F%2Fmodels.open223.info%2Fcompiled%2Fnist-example.ttl'>Query Link</a> |
| Find the downstream equipment for AHU1. | <a href='https://query.open223.info/?query=PREFIX+s223%3A+%3Chttp%3A%2F%2Fdata.ashrae.org%2Fstandard223%23%3E+PREFIX+unit%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Funit%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+quantitykind%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Fquantitykind%2F%3E+PREFIX+qudt%3A+%3Chttp%3A%2F%2Fqudt.org%2Fschema%2Fqudt%2F%3E+PREFIX+sh%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fshacl%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+SELECT+%3FconnectionDown+%3FconnectionDown2+WHERE+%7B%0A++++BIND%28IBAL%3AAHU_1+as+%3Fahu%29+%7B%0A%09%7D%0A%09UNION+%7B%0A%09%3Fahu+s223%3AhasConnectionPoint+%3FconnectionPoint+.%0A%09%3FconnectionPoint+a+s223%3AOutletConnectionPoint+.%0A%09%3FconnectionPoint+s223%3AhasMedium+s223%3AMedium-Air+.%0A%09%3FconnectionPoint+s223%3AconnectsThrough+%3Fsegment+.%0A%09%3Fsegment+s223%3AconnectsTo+%3Fjunction+.%0A++++%3Fjunction+s223%3AconnectedTo+%3FconnectionDown+.%0A++++%3FconnectionDown+a+s223%3ATerminalUnit+.%0A%09%7D%0A%09UNION+%7B%0A%09%3Fahu+s223%3AhasConnectionPoint+%3FconnectionPoint+.%0A%09%3FconnectionPoint+a+s223%3AOutletConnectionPoint+.%0A%09%3FconnectionPoint+s223%3AhasMedium+s223%3AMedium-Air+.%0A%09%3FconnectionPoint+s223%3AconnectsThrough+%3Fsegment+.%0A%09%3Fsegment+s223%3AconnectsTo+%3Fjunction+.%0A++++%3Fjunction+s223%3AconnectedTo+%3FconnectionDown+.%0A++++%3FconnectionDown+a+s223%3AJunction+.%0A%09%3FconnectionDown+s223%3AconnectedTo+%3FconnectionDown2+.%0A%09%3FconnectionDown2+a+s223%3ATerminalUnit+.%0A%09%7D%0A%7D%0A&url=https%3A%2F%2Fmodels.open223.info%2Fcompiled%2Fnist-example.ttl'>Query Link</a> |

## Model Components
| Parent Class | Class | Instances |
|------------|-------|----------------|
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [TemperatureSensor](https://explore.open223.info/s223/TemperatureSensor.html) | 48 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Controller](https://explore.open223.info/s223/Controller.html) | 40 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Damper](https://explore.open223.info/s223/Damper.html) | 19 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [FlowSensor](https://explore.open223.info/s223/FlowSensor.html) | 16 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [ElectricMeter](https://explore.open223.info/s223/ElectricMeter.html) | 11 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [PressureSensor](https://explore.open223.info/s223/PressureSensor.html) | 10 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [HumiditySensor](https://explore.open223.info/s223/HumiditySensor.html) | 9 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [HeatingCoil](https://explore.open223.info/s223/HeatingCoil.html) | 7 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [VariableFrequencyDrive](https://explore.open223.info/s223/VariableFrequencyDrive.html) | 5 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Fan](https://explore.open223.info/s223/Fan.html) | 5 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [ThreeWayValve](https://explore.open223.info/s223/ThreeWayValve.html) | 5 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [TwoWayValve](https://explore.open223.info/s223/TwoWayValve.html) | 5 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Pump](https://explore.open223.info/s223/Pump.html) | 4 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [TerminalUnit](https://explore.open223.info/s223/TerminalUnit.html) | 4 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [AirHandlingUnit](https://explore.open223.info/s223/AirHandlingUnit.html) | 3 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [CoolingCoil](https://explore.open223.info/s223/CoolingCoil.html) | 3 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Chiller](https://explore.open223.info/s223/Chiller.html) | 2 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [HeatExchanger](https://explore.open223.info/s223/HeatExchanger.html) | 2 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [Pipe](https://explore.open223.info/s223/Pipe.html) | 1 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [InletConnectionPoint](https://explore.open223.info/s223/InletConnectionPoint.html) | 160 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [OutletConnectionPoint](https://explore.open223.info/s223/OutletConnectionPoint.html) | 148 |
| [FunctionBlock](https://explore.open223.info/s223/FunctionBlock.html) | [](https://explore.open223.info/s223/.html) | 6 |
| [DomainSpace](https://explore.open223.info/s223/DomainSpace.html) | [](https://explore.open223.info/s223/.html) | 4 |
| [Zone](https://explore.open223.info/s223/Zone.html) | [](https://explore.open223.info/s223/.html) | 6 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableObservableProperty](https://explore.open223.info/s223/QuantifiableObservableProperty.html) | 137 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableProperty](https://explore.open223.info/s223/QuantifiableProperty.html) | 10 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableActuatableProperty](https://explore.open223.info/s223/QuantifiableActuatableProperty.html) | 3 |


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
model = Model.create("urn:nist-example")
model.graph.parse("https://models.open223.info/nist-example.ttl")

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