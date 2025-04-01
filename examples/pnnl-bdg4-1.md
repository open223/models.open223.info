# PNNL Example Building 4 Model 1

Example Building 4 is a single floor in a real-world medium-sized office building. 
It is approximately XX square feet in size, contains XX space types, and XX rooms. Labels have been anonymized, and are not interpretable. 
The lighting system uses LED luminaires with luminaire-level networked lighting controllers that communicate with each other, user interface devices and wireless gatetways over an ISM-band wireless network. 

Example Building 4 Model 1 is provided by Pacific Northwest National Laboratory.

## Contents

This model contains a complete representation of the building architecture and electrical/lighting system, and a partial representation of the lighting control system.

In addition to the s223 ontology, the model uses the [Real Estate Core ontology](https://dev.realestatecore.io/ontology/) to describe space types.

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
