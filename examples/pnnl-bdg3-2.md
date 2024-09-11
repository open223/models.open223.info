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
# PNNL Example Building 3 Model 2

Exammple Building 3 is a real-world medium-sized office building. 
It is approximately 67,000 square feet in size, contains 2 floors, 27 space types, and 469 rooms. Labels have been anonymized, and are not interpretable. 
It uses an underfloor air distribution system with fan-powered terminal reheat coils for perimeter zones. Four roof-top units with VAV are located on the roof. 
The lighting system uses primariliy uses fluorescent luminaires and zone-based lighting controllers that communicate with user interface devices and wireless gatetways over DALI networks. The gateways collect occupancy and light sensor data over an ISM-band wireless network. 

Example Building 3 Model 2 is provided by Pacific Northwest National Laboratory.
See [LBNL Example Building 3 model 1](../lbnl-bdg3-2.md) for a different modeling approach for the same building.

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
    
## Queries

## Model Components
