# NIST Example Building

This is a model of the Intelligent Buildings Agents Laboratory (IBAL) at NIST.

The schematics of the air and hydronic systems can be found [here](../_static/schematics/nist-example.pdf)

## Downloads

- <a href="/nist-example.ttl">Turtle file</a>
- <a href="/nist-example.jsonld">JSON-LD file</a>
    
## Queries
| Description | Query URL |
|-------------|-----------|
| Zone/room temperature sensors | [Query Link](https://query.open223.info/?query=PREFIX+s223%3A+%3Chttp%3A%2F%2Fdata.ashrae.org%2Fstandard223%23%3E+PREFIX+unit%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Funit%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+quantitykind%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Fquantitykind%2F%3E+PREFIX+qudt%3A+%3Chttp%3A%2F%2Fqudt.org%2Fschema%2Fqudt%2F%3E+PREFIX+sh%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fshacl%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+SELECT+%3Flocation+%3Fsensor+WHERE+%7B+++++%3Fsensor+rdf%3Atype%2Frdfs%3AsubClassOf%2A+s223%3ASensor+.+++++%3Fsensor+s223%3Aobserves+%3Fproperty+.+++++%3Fproperty+qudt%3AhasQuantityKind+quantitykind%3ATemperature+.+++++%3Fsensor+s223%3AhasObservationLocation+%3Flocation+%7D+&url=https://models.open223.info/nist-example.ttl) |

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

