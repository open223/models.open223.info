from dataclasses import dataclass, field
from rdflib import Graph, Namespace, URIRef, SH
from typing import Optional

g = Graph()
g.parse("Brick.ttl")

# property shape class
@dataclass
class PropertyShape:
    uri: URIRef
    path: URIRef
    constraint_components: list[URIRef] = field(default_factory=list)


@dataclass
class NodeShape:
    uri: URIRef
    target_class: Optional[URIRef] = None
    property_shapes: list[PropertyShape] = field(default_factory=list)

    def __str__(self):
        return f"NodeShape: {self.uri}\n" + "\n".join(
            [f"\t{p.path}" for p in self.property_shapes]
        )

# find all of the node shapes
node_shapes = g.query("SELECT ?s WHERE { ?s a sh:NodeShape }")
node_shapes = [NodeShape(uri) for (uri,) in node_shapes]

# for each node shape, find its target class
for node_shape in node_shapes:
    target_class = g.value(node_shape.uri, SH.targetClass)
    node_shape.target_class = target_class

# for each node shape, find the objects of sh:property, and create a property shape with its path
for node_shape in node_shapes:
    property_shapes = g.objects(node_shape.uri, SH.property)
    property_shapes = [PropertyShape(uri, g.value(uri, SH.path)) for uri in property_shapes]
    node_shape.property_shapes = property_shapes

# dump all of the node shapes if they have a target class
for node_shape in node_shapes:
    if node_shape.target_class:
        print(node_shape)
