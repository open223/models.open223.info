#!/bin/bash
set -ex

# for debugging ontoenv
export RUST_BACKTRACE=1

ONTOENV_LOG=info ontoenv init models ontologies -i '*.ttl' -e 'models/withimports/*.ttl' -e 'models/compiled/*.ttl' --overwrite

# run the tools/make_model_formats.py script on the models directory
uv run python tools/make_model_formats.py models

# for each filename in the examples/ directory, look for a corresponding .ttl file in the 
# models directory. If it exists, run the tools/make_count_table.py script as
# python tools/make_count_table.py models/<filename>.ttl > examples/<filename>.md
for filename in examples/*.md; do
    # check if the .ttl file exists in the models directory, making
    # sure to get the basename of the filename (i.e. strip the directory)
    # yello text
    echo -e "\e[33m=> Checking for .ttl file for $filename\e[0m"
    # make the models/<filename>.ttl filename
    ttl_filename="models/$(basename "${filename%.md}.ttl")"
    if [ ! -f "$ttl_filename" ]; then
        echo -e "\e[31m  No .ttl file found for $filename\e[0m"
        continue
    fi
    # green text
    echo "  Found $ttl_filename. Making count table"
    # make the examples/<filename>.md filename
    md_filename="examples/$(basename "${filename%.md}.md")"
    echo "  Writing to $md_filename"

    uv run python tools/make_count_table.py "$ttl_filename" "$md_filename"
    uv run python tools/make-notebook.py "$ttl_filename" "$md_filename"
    uv run python tools/mark-out-of-date.py "$ttl_filename" "$md_filename"
done

# build queries
uv run python tools/generate-queries.py models

# for each filename in the models/ directory compile models and pull imports
ontoenv update
mkdir -p models/compiled
mkdir -p models/withimports
make compile-models -j 4
uv run jb build .
