import argparse

import rdflib
import shifty
from ontoenv import OntoEnv

# The ontology every model in this repository is validated and reasoned against.
S223 = "http://data.ashrae.org/standard223/1.0/model/all"

# Keep these in sync with the `ontoenv init` invocation in the Makefile and
# build_examples.sh. OntoEnv 0.6 persists configuration, so these only matter
# when compile.py is the first thing to touch the environment.
SEARCH_DIRECTORIES = ["models", "ontologies"]
INCLUDES = ["*.ttl"]
EXCLUDES = ["models/compiled/*.ttl", "models/withimports/*.ttl"]


def open_env():
    """Open the repository's OntoEnv read-only.

    `connect` never reads source files in 0.6, so the environment must already
    have been populated by `ontoenv init` / `ontoenv update` (see the .ontoenv
    target in the Makefile). Read-only means `make -j` can run several copies
    of this script without contending for the store lock.
    """
    try:
        return OntoEnv.connect(
            ".",
            read_only=True,
            search_directories=SEARCH_DIRECTORIES,
            includes=INCLUDES,
            excludes=EXCLUDES,
            offline=False,
            strict=False,
        )
    except ValueError as e:
        raise SystemExit(
            f"could not open the OntoEnv environment: {e}\n"
            "Run './build_examples.sh', or recreate it by hand with:\n"
            "  rm -rf .ontoenv && make .ontoenv\n"
            "(environments written by ontoenv 0.5 cannot be read by 0.6.)"
        )


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

    graph = rdflib.Graph()
    for f in args.input:
        graph.parse(f, format=rdflib.util.guess_format(f))

    namespaces = dict(graph.namespace_manager.namespaces())

    deps = rdflib.Graph()
    with open_env() as env:
        if args.reason:
            # the imports closure of 223P: the shapes and SHACL-AF rules
            # everything is compiled against
            deps, imported = env.copy_closure(S223, graph=deps)
            print(f"Loaded {len(deps)} triples from {len(imported)} ontologies")

        if args.do_import:
            print("Performing imports")
            imported = env.import_dependencies(graph)
            print(f"Imported {imported}")
            namespaces = dict(graph.namespace_manager.namespaces())

    if args.reason:
        print("Running SHACL-AF inference")
        result = shifty.infer(graph, deps)
        print(f"Inferred {result.inferred_count} triples")
        graph = result.graph()

    if args.output:
        for prefix, uri in namespaces.items():
            graph.bind(prefix, uri)
        graph.serialize(args.output, format="turtle")

    if args.reason:
        # inference already ran above, so don't pay for it a second time.
        # 223P and g36 use sh:Info / sh:Warning for advisory shapes, so only
        # sh:Violation results should fail the build.
        valid, _, report = shifty.validate(
            graph, deps, infer=False, minimum_severity="Violation"
        )
        if not valid:
            print(report)
            raise Exception("Validation failed: {}".format(report))
