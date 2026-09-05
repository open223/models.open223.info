#!/bin/bash
set -Eeuo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# The generated notebooks read each model from ${OPEN223_MODEL_BASE_URL}. On main
# that is the published site; on a branch it is that branch's own copy, so a model
# is validated here before it is published. See tools/model-base-url.sh.
OPEN223_MODEL_BASE_URL="$("${script_dir}/tools/model-base-url.sh")"
export OPEN223_MODEL_BASE_URL
echo "Models will be read from: ${OPEN223_MODEL_BASE_URL}"

build_log="${BUILD_EXAMPLES_LOG:-build-examples.log}"
: > "${build_log}"

summarize_failure() {
    local step="$1"
    local status="$2"

    echo "::error title=Example build failed::${step} exited with status ${status}. See ${build_log} for the complete output."
    echo
    echo "Error-related log lines (up to 80):"
    grep -Ein 'error|exception|traceback|fatal|failed|failure' "${build_log}" | tail -n 80 || true
    echo
    echo "Last 80 log lines:"
    tail -n 80 "${build_log}"
}

run_step() {
    local name="$1"
    shift
    local started="${SECONDS}"

    {
        echo
        echo "===== ${name} ====="
        printf 'Command:'
        printf ' %q' "$@"
        echo
    } >> "${build_log}"

    echo "==> ${name}"
    if "$@" >> "${build_log}" 2>&1; then
        echo "    completed in $((SECONDS - started))s"
    else
        local status="$?"
        summarize_failure "${name}" "${status}"
        return "${status}"
    fi
}

# for debugging ontoenv
export RUST_BACKTRACE=1

# ontoenv 0.6: `init` creates the environment, `update` is what actually reads
# the source files and resolves imports.
run_step "Initialize OntoEnv" uv run ontoenv -v init -i '*.ttl' -e 'models/withimports/*.ttl' -e 'models/compiled/*.ttl' --overwrite -- models ontologies
run_step "Update OntoEnv" uv run ontoenv -v update

# for each filename in the models/ directory compile models and pull imports
mkdir -p models/compiled
mkdir -p models/withimports
run_step "Compile models and update examples" make -j 2
run_step "Install notebook kernel" make install-kernel
# Execute notebooks one at a time. myst defaults to --execute-parallel 7, and
# every notebook loads its own copy of 223P plus the full QUDT closure into a
# separate kernel; at that concurrency the build deadlocks (a kernel drops out
# and myst waits on it forever, with no execution timeout).
run_step "Build and execute Jupyter Book" uv run jupyter book build --html --execute --execute-parallel 1 --strict

echo "Example build completed successfully. Full output: ${build_log}"

if [ "${OPEN223_MODEL_BASE_URL}" != "https://models.open223.info" ]; then
    echo
    echo "Note: examples/*.md now read models from ${OPEN223_MODEL_BASE_URL}."
    echo "Run 'make publish-urls' before committing them."
fi
