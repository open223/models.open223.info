.PHONY: all environment compile-models clean
                                                                                                                                                                                                                  
# Assuming 'all' should build everything. If 'environment' is a task that should be run,
# you need to add a corresponding recipe for it.
all: compile-models

# MODEL_SOURCES will find all .ttl files in the models directory.
MODEL_SOURCES := $(wildcard models/*.ttl)
#MODEL_SOURCES := models/nrel-example.ttl

# COMPILED_MODELS will be the list of files but in the models/compiled folder.
COMPILED_MODELS := $(patsubst models/%.ttl,models/compiled/%.ttl,$(MODEL_SOURCES))

# WITH_IMPORTS_MODELS will be the list of files but in the models/withimports folder.
WITH_IMPORTS_MODELS := $(patsubst models/%.ttl,models/withimports/%.ttl,$(MODEL_SOURCES))

.ontoenv:
	ontoenv init models ontologies

models/compiled/%.ttl: models/%.ttl tools/compile.py
	-uv run python tools/compile.py -r -o $@ $< 

models/withimports/%.ttl: models/compiled/%.ttl tools/compile.py
	-uv run python tools/compile.py -i -o $@ $< 

# The compile-models target will "make" all of the COMPILED_MODELS.
compile-models: $(COMPILED_MODELS) $(WITH_IMPORTS_MODELS)

install-kernel:
	python -m ipykernel install --user --name=python3

# Rule to clean up the compiled models.
clean:
	rm -rf models/compiled models/withimports .ontoenv
