# PNNL Example Building 2

This is an example building model provided by Pacific Northwest National Laboratory.

The model is based on a [Department of Energy Prototype Builiding](https://www.energycodes.gov/prototype-building-models) model. 
Specifically, the DOE Prototype Medium Office Building was extended by creating unique detailed building architecture for each of the three building floors,
and designing a lighting layout that complies with the ASHRAE 90.1-2019 energy code.

The model contains a representation of the building architecture and lighting system.

In addition to the s223 ontology, the model uses the [Real Estate Core ontology](https://dev.realestatecore.io/ontology/) to describe space types.

## Source

The model was created from souce data consisting of a Revit building information model (BIM) exported via a [Speckle](https://speckle.systems/) interface.

### The Speckle view of rooms and lighting fixtures
<img width="1178" alt="image" src="https://github.com/open223/models.open223.info/assets/22898727/5a5dcecb-9b87-4e84-8261-6a3a315e1265">

Model instance data have a prefix that is resolvable to a Speckle URL.
``` ttl
@prefix bdg1: <http://speckle.xyz/streams/1fed8e620e/objects/>
```

For example, the following luminaire resolves to https://speckle.xyz/streams/1fed8e620e/objects/05749166d93671bedf16efb52636ce38.
```ttl
bdg1:05749166d93671bedf16efb52636ce38 a s223:Luminaire
```

## Downloads
    
## Queries

## Model Components
