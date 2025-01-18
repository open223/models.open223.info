import re
import string
import random
import argparse
import ontoenv
import rdflib
#import brickschema
#from brickschema import topquadrant_shacl
from brick_tq_shacl.topquadrant_shacl import infer, validate
import rdflib

graph = rdflib.Graph()
cfg = ontoenv.Config(["models", "ontologies"], offline=False, strict=False)
env = ontoenv.OntoEnv(cfg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Handle imports and perform SHACL reasoning)"
    )
    parser.add_argument("input", nargs="+")
    parser.add_argument("-o", "--output", help="Output file", required=True)
    parser.add_argument(
        "-r", "--reason", help="Run SHACL reasoning + validation", action="store_true"
    )
    parser.add_argument(
        "-i", "--do-import", help="Perform imports", action="store_true"
    )
    args = parser.parse_args()
    print(f"Input files: {args.input}")

    for f in args.input:
        graph.parse(f, format=rdflib.util.guess_format(f))

    namespaces = dict(graph.namespace_manager.namespaces())

    deps = rdflib.Graph()
    env.get_closure("http://data.ashrae.org/standard223/1.0/model/all", deps)
    env.import_dependencies(graph)
    deps.serialize("deps.ttl", format="turtle")
    graph.serialize("graph.ttl", format="turtle")

    if args.reason:
        #topquadrant_shacl._MAX_EXTERNAL_LOOPS = 2
        graph = infer(graph, graph)
        #graph.expand(profile="shacl", backend="topquadrant")
    if args.output:
        for prefix, uri in namespaces.items():
            graph.bind(prefix, uri)
        graph.serialize(args.output, format="turtle")
    else:
        print(graph.serialize(format="turtle"))
    valid, _, report = validate(graph, graph)
    if not valid:
        print(report)
        raise Exception("Validation failed: {}".format(report))
