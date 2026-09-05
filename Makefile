.PHONY: all compile-models update-examples validate-model model-page publish-urls check-model-urls install-kernel clean FORCE
                                                                                                                                                                                                                  
all: compile-models update-examples

# Base URL the generated notebooks read models from: the published site on main,
# the branch's own copy on any other branch. Override by exporting
# OPEN223_MODEL_BASE_URL. See tools/model-base-url.sh.
OPEN223_MODEL_BASE_URL ?= $(shell tools/model-base-url.sh)
export OPEN223_MODEL_BASE_URL

# The base URL is written into examples/*.md when they are generated, so the
# pages must be regenerated whenever it changes -- otherwise a branch URL would
# linger in the markdown after switching back to main. This stamp file records
# the URL the pages were last generated with, and is only rewritten when it
# actually changes, so it does not force a rebuild on every run.
MODEL_BASE_URL_STAMP := .model-base-url

# MODEL_SOURCES will find all .ttl files in the models directory.
MODEL_SOURCES := $(wildcard models/*.ttl)
#MODEL_SOURCES := models/nrel-example.ttl

# COMPILED_MODELS will be the list of files but in the models/compiled folder.
COMPILED_MODELS := $(patsubst models/%.ttl,models/compiled/%.ttl,$(MODEL_SOURCES))

# WITH_IMPORTS_MODELS will be the list of files but in the models/withimports folder.
WITH_IMPORTS_MODELS := $(patsubst models/%.ttl,models/withimports/%.ttl,$(MODEL_SOURCES))

# Find all example markdown files that have a corresponding model file.
EXAMPLE_MDS_WITH_MODELS := $(foreach md, $(wildcard examples/*.md), $(if $(wildcard $(patsubst examples/%.md,models/%.ttl,$(md))), $(md)))

# compile.py opens the environment read-only, so it has to exist and be
# populated before any model is compiled. ontoenv 0.6 splits discovery out of
# connect(), hence the explicit `update` after `init`.
.ontoenv:
	uv run ontoenv init -i '*.ttl' -e 'models/withimports/*.ttl' -e 'models/compiled/*.ttl' -- models ontologies
	uv run ontoenv update

# order-only prerequisite: the environment must exist, but refreshing it should
# not by itself invalidate already-compiled models.
models/compiled/%.ttl: models/%.ttl tools/compile.py | .ontoenv
	@mkdir -p $(@D)
	-uv run python tools/compile.py -r -o $@ $<

# models/withimports/ is gitignored, so it may not exist in a fresh clone
models/withimports/%.ttl: models/compiled/%.ttl tools/compile.py | .ontoenv
	@mkdir -p $(@D)
	-uv run python tools/compile.py -i -o $@ $<

# The compile-models target will "make" all of the COMPILED_MODELS.
compile-models: $(COMPILED_MODELS) $(WITH_IMPORTS_MODELS)

# The update-examples target will check all of the example markdown files.
# It will only update the ones where the source .ttl file is newer.
update-examples: $(EXAMPLE_MDS_WITH_MODELS)

# Validate one local source model without writing compiled output:
#   make validate-model MODEL=nrel-example
validate-model:
	@test -n "$(MODEL)" || { echo "Usage: make validate-model MODEL=<model-name>"; exit 2; }
	@test -f "models/$(MODEL).ttl" || { echo "Model not found: models/$(MODEL).ttl"; exit 2; }
	@$(MAKE) .ontoenv
	uv run python tools/compile.py -r "models/$(MODEL).ttl"

# Validate the local source, then regenerate, execute, and build one model page.
#   make model-page MODEL=nrel-example
model-page:
	@test -n "$(MODEL)" || { echo "Usage: make model-page MODEL=<model-name>"; exit 2; }
	@test -f "models/$(MODEL).ttl" || { echo "Model not found: models/$(MODEL).ttl"; exit 2; }
	@$(MAKE) validate-model MODEL="$(MODEL)"
	@$(MAKE) "examples/$(MODEL).md"
	uv run jupyter book build "examples/$(MODEL).md" --html --execute --execute-parallel 1 --strict

$(MODEL_BASE_URL_STAMP): FORCE
	@printf '%s\n' '$(OPEN223_MODEL_BASE_URL)' | cmp -s - $@ 2>/dev/null \
		|| printf '%s\n' '$(OPEN223_MODEL_BASE_URL)' > $@

FORCE:

examples/%.md: models/%.ttl $(MODEL_BASE_URL_STAMP) tools/make_count_table.py tools/make-notebook.py tools/mark-out-of-date.py tools/make_model_formats.py tools/generate-queries.py queries.toml
	uv run python tools/make_model_formats.py $<
	uv run python tools/generate-queries.py $< $@
	uv run python tools/make_count_table.py $< $@
	uv run python tools/make-notebook.py $< $@
	uv run python tools/mark-out-of-date.py $< $@

# Rewrite the example pages with the published model URL. A local build points
# them at this checkout, which must not be committed; run this first.
publish-urls:
	@$(MAKE) update-examples OPEN223_MODEL_BASE_URL=https://models.open223.info
	@echo "examples/*.md now read models from https://models.open223.info"

# Guard against committing a branch's base URL into the example pages: only the
# published site belongs in the checked-in markdown. Checks the committed
# content, not the working tree, which legitimately holds branch URLs mid-build.
check-model-urls:
	@bad=$$(git grep -n 'Model\.from_file(' HEAD -- 'examples/*.md' \
		| grep -v 'Model\.from_file("https://models\.open223\.info/' || true); \
	if [ -n "$$bad" ]; then \
		echo "Committed example pages read models from somewhere other than https://models.open223.info:"; \
		echo "$$bad"; \
		echo "Regenerate them on main (make update-examples) before committing."; \
		exit 1; \
	fi
	@echo "Committed example pages all read from https://models.open223.info"

install-kernel:
	uv run python -m ipykernel install --user --name open223-models --display-name "open223-models"

# Rule to clean up the compiled models.
clean:
	rm -rf models/compiled/* models/withimports/* .ontoenv
