#!/bin/bash
set -ex

# for debugging ontoenv
export RUST_BACKTRACE=1

# ontoenv 0.6: `init` creates the environment, `update` is what actually reads
# the source files and resolves imports.
uv run ontoenv -v init -i '*.ttl' -e 'models/withimports/*.ttl' -e 'models/compiled/*.ttl' --overwrite -- models ontologies
uv run ontoenv -v update

# for each filename in the models/ directory compile models and pull imports
mkdir -p models/compiled
mkdir -p models/withimports
make -j 2
make install-kernel
# Execute notebooks one at a time. myst defaults to --execute-parallel 7, and
# every notebook loads its own copy of 223P plus the full QUDT closure into a
# separate kernel; at that concurrency the build deadlocks (a kernel drops out
# and myst waits on it forever, with no execution timeout).
uv run jupyter book build --html --execute --execute-parallel 1
