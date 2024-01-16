import re
import string
import random
import argparse
import brickschema
from brickschema import topquadrant_shacl
import ontoenv
import rdflib

env = ontoenv.OntoEnv(initialize=True, search_dirs=["./ontologies/"])
graph = brickschema.Graph()

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

    for f in args.input:
        graph.parse(f, format=rdflib.util.guess_format(f))

    if args.do_import:
        env.import_dependencies(graph)

    # remove QUDT prefix because it breaks things
    graph.bind("qudtprefix21", rdflib.Namespace("http://qudt.org/2.1/vocab/prefix/"))
    graph.bind("qudtprefix", rdflib.Namespace("http://qudt.org/vocab/prefix/"))

    if args.reason:
        topquadrant_shacl._MAX_EXTERNAL_LOOPS = 0
        graph.expand(profile="shacl", backend="topquadrant")
        valid, _, report = graph.validate(engine="topquadrant")
        if not valid:
            print(report)
    if args.output:
        graph.serialize(args.output, format="turtle")
    else:
        print(graph.serialize(format="turtle"))
