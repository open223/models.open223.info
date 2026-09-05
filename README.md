## Contributing a Model

1. Put the model's `.ttl` file in the `models/` directory
2. Create a `.md` file *with the same base name as the `.ttl` file* in the `examples/` directory:
    - This `.md` file should have at least the following 3 *empty* sections, in this order:
    - `## Downloads`
    - `## Queries`
    - `## Model Components`
    - there should also be a "header" section at the top of the file which allows executable code to be embedded in the markdown file (see below)
3. Add this `.md` file to the `toc:` in `myst.yml` under the appropriate section (Example Buildings or Example Systems)
4. If you want to add queries to the model, add them in `queries.toml`. The section name should have the same base name as the `.ttl` and `.md` file.


### Example

For a model called `mybuilding.ttl`, the following files would be created:
- `models/mybuilding.ttl`
- `examples/mybuilding.md`

The `examples/mybuilding.md` file would look like this:

```
---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: open223-models
  language: python
  name: open223-models
---
# My Example Building

<description of the building>

## Downloads

## Queries

## Model Components
```

The `queries.toml` file might look like this:

```toml
[[mybuilding]]
description="Zone/room temperature sensors"
query="""
SELECT ?location ?sensor WHERE {
    ?sensor rdf:type/rdfs:subClassOf* s223:Sensor .
    ?sensor s223:observes ?property .
    ?property qudt:hasQuantityKind quantitykind:Temperature .
    ?sensor s223:hasObservationLocation ?location
}
"""
```

## How the build works

`./build_examples.sh` contains the whole pipeline. Everything
it does is logged to `build-examples.log` (CI uploads that as the
`example-build-log` artifact), and on failure it prints the error-related lines
and the tail of the log. The stages, in order:

1. **Resolve ontology dependencies**: `uv run ontoenv init` then `ontoenv update`
   to populate `.ontoenv/` with the ontologies under `models/` and `ontologies/`.
2. **Compile models and regenerate pages**: `make -j 2` (feel free to increase 2 for more parallelism)
3. **Install the Jupyter kernel**: `make install-kernel` registers the
   `open223-models` kernel used in the jupyter book to run the code samples
4. **Build and execute the book**: `uv run jupyter book build --html --execute
   --execute-parallel 1 --strict`,writes the site to `_build/html/`

CI then runs `tools/stage-site-assets.sh`, which copies `CNAME` and the model
files into the built site (`/`, `/models/`, `/compiled/`, `/withimports/`), checks
the copies landed, and deploys to `gh-pages`.

### What `make` does

**Compiling** (`make compile-models`), once per `models/<name>.ttl`:

| Output | Command | Purpose |
| --- | --- | --- |
| `models/compiled/<name>.ttl` | `tools/compile.py -r` | SHACL inference + validation against 223P |
| `models/withimports/<name>.ttl` | `tools/compile.py -i` | the compiled model with all imports inlined |

Both rules are prefixed with `-` in the Makefile, so a model that fails SHACL
validation does **not** stop the site build. Use `make validate-model MODEL=<name>`
to see those violations and get a nonzero exit.

**Regenerating pages** (`make update-examples`), once per `examples/<name>.md`.
Each script rewrites one section of the page in place (via
`tools/markdown_utils.py`'s `upsert_section`), so the prose you write around them
is preserved:

| Script | What it writes |
| --- | --- |
| `tools/make_model_formats.py` | `models/<name>.jsonld` next to the Turtle source |
| `tools/generate-queries.py` | the `## Queries` table, from `queries.toml` |
| `tools/make_count_table.py` | the `## Model Components` counts, from the model |
| `tools/make-notebook.py` | the `## Load and Validate Model` code cell, with the model URL baked in |
| `tools/mark-out-of-date.py` | adds or removes the "not updated since the last 223P revision" warning |

Two other pieces are not part of `make`: `tools/model-base-url.sh` (below) and
`tools/copy-validation-output.mjs`, a MyST plugin registered in `myst.yml` that
turns the validation cell's stdout into a copyable text block.

### Generated vs. tracked

Generated and gitignored: `models/withimports/`, `_build/`, `.ontoenv/`,
`.model-base-url`, `build-examples.log`.

Generated but **committed**: `models/compiled/*.ttl`, `models/*.jsonld`, and the
generated sections of `examples/*.md`. Regenerate them rather than editing them by
hand.

### When it breaks

- **`ValueError: Graph does not contain an ontology declaration`**: the model the
  page loaded has no `a owl:Ontology` subject. Check the URL in the failing cell:
  it may be pointing at a published copy that predates your fix (see below).
- **A page fails the book build**: `--strict` fails on cell exceptions, not on a
  model reporting `Model is valid: False`. The traceback is in `build-examples.log`.
- **A page did not pick up your change**: `make` only regenerates
  `examples/<name>.md` when `models/<name>.ttl`, one of the `tools/` scripts, or
  `.model-base-url` is newer. Force it with `touch models/<name>.ttl`.
- **`OntologyImportsNotFound: ... http://www.w3.org/ns/shacl#`** (or
  `.../2004/02/skos/core`): a transient fetch failure, not a problem with the
  model. Each notebook builds its own BuildingMOTIF instance, and each of those
  resolves 223P's imports over the network from scratch, so one build asks
  `www.w3.org` for the same file once per model. It sits behind Cloudflare and
  throttles datacenter egress, so a GitHub Actions build intermittently loses a
  few pages this way while the identical build passes from a laptop.
  `build_examples.sh` retries the book build up to three times; MyST does not
  cache a notebook whose execution raised, so a retry re-runs only the pages
  that actually failed and costs seconds rather than minutes.
- **`--execute-parallel` does not appear to work**: `build_examples.sh` asks for
  1, but jupyter-book 2.1.6 ignores the value — a local build of these pages
  starts 15 kernels at once (MyST's own default) and a GitHub Actions build
  starts 4. The flag documents the intent and nothing more. In particular, do
  not give the notebooks anything that tolerates only one writer, such as a
  shared persistent OntoEnv: they will run concurrently.
- **OntoEnv errors after an upgrade**: environments written by ontoenv 0.5 cannot
  be read by 0.6. `rm -rf .ontoenv` and rebuild.
- **Everything is stale or wrong**: `make clean` removes the compiled models and
  `.ontoenv`, then rebuild.

### Validate or build one model

To validate a local model directly against 223P without rebuilding the site:

```shell
make validate-model MODEL=mybuilding
```

To regenerate, execute, and build only that model's page:

```shell
make model-page MODEL=mybuilding
```

The single-page build first validates the local `models/mybuilding.ttl` and
exits nonzero if that validation fails. The rendered page is written under
`_build/html/`. Executable-cell errors and exceptions also fail book builds; a
model reporting that it does not validate does not.

### Where the executable page reads the model from

Each example page ends in a `Model.from_file("...")` cell. That URL is written
into `examples/*.md` when the page is generated, by `tools/model-base-url.sh`:

| Build | Model URL |
| --- | --- |
| any local build (`./build_examples.sh`, `make model-page`, `make update-examples`) | `file://` this checkout, so you validate the models you are editing |
| CI (`main`, a branch, or a pull request) | the exact commit under test on `raw.githubusercontent.com` |

No build reads `https://models.open223.info`, `main` included. That copy is
whatever the last *successful* deploy left behind, so validating against it
deadlocks: a commit that fixes a broken model file is checked against the old
broken file, the build fails, the site is never updated, and the next build
checks the same stale file again. `pnnl-bdg1-2.ttl` was stuck exactly there —
its `owl:Ontology` declaration was restored in #75, but every `main` build
afterwards failed validating the pre-#75 published copy. Reading the commit
under test also makes a built page reproducible: its URL keeps resolving to the
bytes that page was validated against, even after `main` moves on.

The published URL is still the one a reader wants, so the generated cell names
it in a comment directly above the `Model.from_file(...)` line.

Export `OPEN223_MODEL_BASE_URL` to override it, for instance to reproduce the
published site locally:

```shell
OPEN223_MODEL_BASE_URL=https://models.open223.info ./build_examples.sh
```

While a local build runs, `examples/*.md` point at your checkout and carry a
"Preview build" warning admonition; so do branch and pull request builds, whose
pages validate a copy that is not going to be published. A `main` build is
building what is about to be published, so it carries no such note. Only the published URL belongs in the
repository, so three things keep it out:

1. `./build_examples.sh` restores the published URL when it exits, however it
   exits. A finished local build leaves no URL churn in `git status`.
2. `make install-hooks` (once per clone) points git at `.githooks/`, whose
   `pre-commit` hook rejects a commit that stages a non-published URL.
3. `make check-model-urls` fails the CI build if one was committed anyway.

To fix the pages by hand at any point, run `make publish-urls`: it regenerates
them with `https://models.open223.info`, keeping real content changes such as
query tables and component counts. (`git checkout -- examples/` also works, but
throws those away too.)

Nothing rewrites these files on merge: CI regenerates the pages in its own
workspace and publishes only the built HTML, so a committed `file://` URL stays
in the repository until someone regenerates it.
