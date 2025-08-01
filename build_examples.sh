#!/bin/bash
set -ex

# for debugging ontoenv
export RUST_BACKTRACE=1

ONTOENV_LOG=info ontoenv init models ontologies -i '*.ttl' -e 'models/withimports/*.ttl' -e 'models/compiled/*.ttl' --overwrite

# run the tools/make_model_formats.py script on the models directory
uv run python tools/make_model_formats.py models

# build queries
uv run python tools/generate-queries.py models

# for each filename in the models/ directory compile models and pull imports
ontoenv update
mkdir -p models/compiled
mkdir -p models/withimports
make -j 2
uv run jb build .
