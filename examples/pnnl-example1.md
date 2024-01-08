# PNNL Example Building 1

This is an example building model provided by Pacific Northwest National Laboratory.

The model is a simplistic, reference building consisting of a single story with 5 rooms: open office, private office, bathroom, kitchenette, corridor.

The model contains a representation of the building architecture and lighting system.

In addition to the s223 ontology, the model uses the [Real Estate Core ontology](https://dev.realestatecore.io/ontology/) to describe space types.

## Source

The model was created from souce data consisting of a Revit building information model (BIM) exported via a [Speckle](https://speckle.systems/) interface.

### The Speckle view of rooms and lighting fixtures
<img width="1212" alt="image" src="https://github.com/open223/models.open223.info/assets/22898727/92b1afd2-b3c3-492b-a7c7-61dea827a246">

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
