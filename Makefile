.PHONY: all compile-models clean
                                                                                                                                                                                                                  
all: compile-models update-examples

# MODEL_SOURCES will find all .ttl files in the models directory.
MODEL_SOURCES := $(wildcard models/*.ttl)
#MODEL_SOURCES := models/nrel-example.ttl

# COMPILED_MODELS will be the list of files but in the models/compiled folder.
COMPILED_MODELS := $(patsubst models/%.ttl,models/compiled/%.ttl,$(MODEL_SOURCES))

# WITH_IMPORTS_MODELS will be the list of files but in the models/withimports folder.
WITH_IMPORTS_MODELS := $(patsubst models/%.ttl,models/withimports/%.ttl,$(MODEL_SOURCES))

# Find all example markdown files that have a corresponding model file.
EXAMPLE_MDS_WITH_MODELS := $(foreach md, $(wildcard examples/*.md), $(if $(wildcard $(patsubst examples/%.md,models/%.ttl,$(md))), $(md)))

.ontoenv:
	ontoenv init models ontologies

models/compiled/%.ttl: models/%.ttl tools/compile.py
	-uv run python tools/compile.py -r -o $@ $< 

models/withimports/%.ttl: models/compiled/%.ttl tools/compile.py
	-uv run python tools/compile.py -i -o $@ $< 

# The compile-models target will "make" all of the COMPILED_MODELS.
compile-models: $(COMPILED_MODELS) $(WITH_IMPORTS_MODELS)

# The update-examples target will check all of the example markdown files.
# It will only update the ones where the source .ttl file is newer.
update-examples: $(EXAMPLE_MDS_WITH_MODELS)

examples/%.md: models/%.ttl tools/make_count_table.py tools/make-notebook.py tools/mark-out-of-date.py tools/make_model_formats.py tools/generate-queries.py queries.toml
	uv run python tools/make_model_formats.py $<
	uv run python tools/generate-queries.py $< $@
	uv run python tools/make_count_table.py $< $@
	uv run python tools/make-notebook.py $< $@
	uv run python tools/mark-out-of-date.py $< $@

install-kernel:
	uv run python -m ipykernel install --user --name open223-models --display-name "open223-models"

# Rule to clean up the compiled models.
clean:
	rm -rf models/compiled/* models/withimports/* .ontoenv
