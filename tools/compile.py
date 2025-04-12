import re
import string
import random
import argparse
import ontoenv
import rdflib
from brick_tq_shacl import topquadrant_shacl
from brick_tq_shacl.topquadrant_shacl import infer, validate
import rdflib

graph = rdflib.Graph()
cfg = ontoenv.Config(["models", "ontologies"], offline=False, strict=False, includes=['*.ttl'])
env = ontoenv.OntoEnv(cfg, read_only=True, recreate=False)

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
    deps.serialize("deps.ttl", format="turtle")
    graph.serialize("graph.ttl", format="turtle")

    if args.reason:
        topquadrant_shacl._MAX_EXTERNAL_LOOPS = 10
        graph = infer(graph, deps)
    if args.output:
        for prefix, uri in namespaces.items():
            graph.bind(prefix, uri)
        graph.serialize(args.output, format="turtle")

        # replace .ttl with -with-imports.ttl
        new_file = re.sub(r"\.ttl$", "-with-imports.ttl", args.output)
        env.import_dependencies(graph)
        graph.serialize(new_file, format="turtle")

    valid, _, report = validate(graph, graph)
    if not valid:
        print(report)
        raise Exception("Validation failed: {}".format(report))
