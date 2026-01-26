#!/bin/bash
set -ex

# for debugging ontoenv
export RUST_BACKTRACE=1

ONTOENV_LOG=info uv run ontoenv init -i '*.ttl' -e 'models/withimports/*.ttl' -e 'models/compiled/*.ttl' --overwrite -- models ontologies


# for each filename in the models/ directory compile models and pull imports
uv run ontoenv update
mkdir -p models/compiled
mkdir -p models/withimports
make -j 2
make install-kernel
uv run jb build .
