# Example Building 1-2

Example Building 1 is a simplistic, reference tiny office building consisting of a single story with 5 rooms spanning 5 space types.

This reference building was developed for and first described in the journal article ["Metadata Schemas and Ontologies for Building Energy Applications: A Critical Review and Use Case Analysis"](https://doi.org/10.3390/en14072024).

This example Building 1-2 model is provided by Pacific Northwest National Laboratory.

### Schematic view

![image](https://github.com/steveraysteveray/models.open223.info/assets/1130189/a586b8cd-c699-42c1-9b49-0c3f8a81de55)

## Contents

The model contains a representation of the building architecture and electrical/lighting system.

In addition to the s223 ontology, the model uses the [Real Estate Core ontology](https://dev.realestatecore.io/ontology/) to describe space types.

## Source

The model was created from souce data consisting of a Revit building information model (BIM) exported via a [Speckle](https://speckle.systems/) interface.

### Speckle view of rooms and lighting fixtures
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
