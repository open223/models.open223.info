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

- <a href="/compiled/pnnl-bdg2-1.ttl">Turtle file (compiled)</a> (<a href="/pnnl-bdg2-1.ttl">original</a>)
- <a href="/pnnl-bdg2-1.jsonld">JSON-LD file (original)</a>
    
## Queries

## Model Components
| Parent Class | Class | Instances |
|------------|-------|----------------|
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [Luminaire](https://explore.open223.info/s223/Luminaire.html) | 853 |
| [Equipment](https://explore.open223.info/s223/Equipment.html) | [ElectricBreaker](https://explore.open223.info/s223/ElectricBreaker.html) | 3 |
| [Connection](https://explore.open223.info/s223/Connection.html) | [ElectricWire](https://explore.open223.info/s223/ElectricWire.html) | 856 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [OutletConnectionPoint](https://explore.open223.info/s223/OutletConnectionPoint.html) | 1709 |
| [ConnectionPoint](https://explore.open223.info/s223/ConnectionPoint.html) | [InletConnectionPoint](https://explore.open223.info/s223/InletConnectionPoint.html) | 1709 |
| [DomainSpace](https://explore.open223.info/s223/DomainSpace.html) | [](https://explore.open223.info/s223/.html) | 311 |
| [Zone](https://explore.open223.info/s223/Zone.html) | [](https://explore.open223.info/s223/.html) | 220 |
| [Property](https://explore.open223.info/s223/Property.html) | [QuantifiableProperty](https://explore.open223.info/s223/QuantifiableProperty.html) | 394 |

