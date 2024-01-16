.PHONY: all environment compile-models clean refresh-ontoenv
                                                                                                                                                                                                                  
# Assuming 'all' should build everything. If 'environment' is a task that should be run,
# you need to add a corresponding recipe for it.
all: refresh-ontoenv compile-models

# MODEL_SOURCES will find all .ttl files in the models directory.
MODEL_SOURCES := $(wildcard models/*.ttl)

# COMPILED_MODELS will be the list of files but in the models/compiled folder.
COMPILED_MODELS := $(patsubst models/%.ttl,models/compiled/%.ttl,$(MODEL_SOURCES))

refresh-ontoenv:
	ontoenv init -s ontologies/ -v

# Rule to compile each model.
# The prerequisite 'models/%.ttl' means it will match each .ttl file in the models directory.
# 'tools/compile.py' ensures the compile script is present, but should be a prerequisite only if you want to track changes on it.
# 'ontologies/*.ttl' captures changes in any .ttl file in the ontologies directory.
models/compiled/%.ttl: models/%.ttl tools/compile.py
	python tools/compile.py -r -i -o $@ $< ontologies/223p.ttl

# The compile-models target will "make" all of the COMPILED_MODELS.
compile-models: $(COMPILED_MODELS)

# Rule to clean up the compiled models.
clean:
	rm -f models/compiled/*.ttl
