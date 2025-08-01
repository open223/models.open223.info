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
# NIST Example Building 1 Model 1

Example Building 1 is a simplistic, reference tiny office building consisting of a single story with 5 rooms spanning 5 space types.

This reference building was developed for and first described in the journal article ["Metadata Schemas and Ontologies for Building Energy Applications: A Critical Review and Use Case Analysis"](https://doi.org/10.3390/en14072024).

Example Building 1 Model 1 is provided by current and former NIST staff and Pacific Northwest National Laboratory. See also [PNNL Example Building 1 Model 2](pnnl-bdg1-2.md) for a different modeling approach for the same building.

### Schematic view

![image](../_static/images/ExampleBuilding1.png)

## Contents

This model contains a representation of the building architecture, mechanical system, and electrical/lighting system.

## Source

The model was created using [TopQuadrant](https://www.topquadrant.com/) TopBraid Composer Maestro Edition.

## Downloads

- <a href="/compiled/nist-bdg1-1.ttl">Turtle file (compiled)</a>
- <a href="/withimports/nist-bdg1-1.ttl">Turtle file (with all imports)</a>
- <a href="/nist-bdg1-1.ttl">Turtle file (original)</a>
- <a href="/nist-bdg1-1.jsonld">JSON-LD file (original)</a>

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
| Select all triples from model. | <a href='https://query.open223.info/?query=PREFIX+s223%3A+%3Chttp%3A%2F%2Fdata.ashrae.org%2Fstandard223%23%3E+PREFIX+unit%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Funit%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+quantitykind%3A+%3Chttp%3A%2F%2Fqudt.org%2Fvocab%2Fquantitykind%2F%3E+PREFIX+qudt%3A+%3Chttp%3A%2F%2Fqudt.org%2Fschema%2Fqudt%2F%3E+PREFIX+sh%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fshacl%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+%0ASELECT+%2A+WHERE+%7B%0A%09+%3Fs+%3Fp+%3Fo+%0A%7D%0A+LIMIT+10&url=https%3A%2F%2Fmodels.open223.info%2Fcompiled%2Fnist-bdg1-1.ttl'>Query Link</a> |

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

