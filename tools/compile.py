import re
import string
import random
import argparse
import rdflib
#import brickschema
#from brickschema import topquadrant_shacl
from brick_tq_shacl.topquadrant_shacl import infer, validate
import rdflib

graph = rdflib.Graph()

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

    s223 = rdflib.Graph()
    if args.do_import:
        s223.parse("ontologies/223p.ttl")
        namespaces.update(dict(s223.namespace_manager.namespaces()))

    # remove QUDT prefix because it breaks things
    #graph.bind("qudtprefix21", rdflib.Namespace("http://qudt.org/2.1/vocab/prefix/"))
    #graph.bind("qudtprefix", rdflib.Namespace("http://qudt.org/vocab/prefix/"))

    if args.reason:
        graph.remove((None, rdflib.OWL.imports, None))
        s223.remove((None, rdflib.OWL.imports, None))
        #topquadrant_shacl._MAX_EXTERNAL_LOOPS = 2
        graph = infer(graph, s223)
        #graph.expand(profile="shacl", backend="topquadrant")
        valid, _, report = validate(graph, s223)
        if not valid:
            print(report)
            raise Exception("Validation failed: {}".format(report))
    if args.output:
        for prefix, uri in namespaces.items():
            graph.bind(prefix, uri)
        graph.serialize(args.output, format="turtle")
    else:
        print(graph.serialize(format="turtle"))
