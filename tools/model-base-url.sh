#!/bin/bash
# Print the base URL that the generated example notebooks read models from.
#
# The URL is baked into examples/*.md when the pages are generated, so whatever
# this prints is what a reader of the built page sees and can copy.
#
#   any local build : this checkout, so a build always validates the models you
#                     are actually editing, committed or not
#   CI              : the exact commit under test on raw.githubusercontent.com
#
# CI deliberately does NOT read from https://models.open223.info. That copy is
# whatever the last *successful* deploy left behind, so validating against it
# deadlocks: a commit that fixes a bad model file is validated against the old
# bad file, the build fails, the site is never updated, and the next build
# re-validates the same stale file. This is exactly what happened to
# pnnl-bdg1-2.ttl, whose owl:Ontology declaration was restored in #75 but never
# published, because every main build since has failed against the pre-#75 copy.
#
# Pinning the commit rather than the branch also makes a built page reproducible:
# the URL in it keeps resolving to the bytes that page was built from, even after
# main moves on. The page still names https://models.open223.info in a comment as
# the URL to use day to day -- see tools/make-notebook.py.
#
# Export OPEN223_MODEL_BASE_URL to override all of that.
#
# With --preview, print 1 if the page should carry a "preview build" note -- that
# is, if this build is not the canonical repository's main branch -- or 0 if it
# is building what is about to be published.
set -euo pipefail

PUBLISHED_URL="https://models.open223.info"
CANONICAL_REPO="open223/models.open223.info"
CANONICAL_BRANCH="main"

# The repository and commit CI is building. For a pull request the head commit
# lives in the head repository, which is the fork for a fork PR; the workflow
# passes both as GITHUB_HEAD_REPOSITORY/GITHUB_HEAD_SHA because GITHUB_REPOSITORY
# is always the base repository and GITHUB_SHA is the ephemeral merge commit.
ci_repo() { printf '%s' "${GITHUB_HEAD_REPOSITORY:-${GITHUB_REPOSITORY:-${CANONICAL_REPO}}}"; }
ci_sha()  { printf '%s' "${GITHUB_HEAD_SHA:-${GITHUB_SHA:-}}"; }
# GITHUB_HEAD_REF is set for pull_request builds, GITHUB_REF_NAME for pushes.
ci_ref()  { printf '%s' "${GITHUB_HEAD_REF:-${GITHUB_REF_NAME:-}}"; }

# The URL this build would use if nothing had overridden it.
natural_url() {
    local repo_root
    repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

    if [ -z "${GITHUB_ACTIONS:-}" ]; then
        # Local build: use the working tree. It is the only copy that has edits
        # which are not committed or pushed yet, and it is what you are trying
        # to check.
        printf 'file://%s/models\n' "${repo_root}"
        return
    fi

    local sha
    sha="$(ci_sha)"
    if [ -z "${sha}" ]; then
        # No commit to pin (should not happen on Actions). Fall back to the ref
        # so the build still reads the code under test rather than the site.
        sha="$(ci_ref)"
        [ -n "${sha}" ] || sha="${CANONICAL_BRANCH}"
    fi

    printf 'https://raw.githubusercontent.com/%s/%s/models\n' "$(ci_repo)" "${sha}"
}

resolve_url() {
    if [ -n "${OPEN223_MODEL_BASE_URL:-}" ]; then
        printf '%s\n' "${OPEN223_MODEL_BASE_URL}"
        return
    fi
    natural_url
}

is_preview() {
    local url
    url="$(resolve_url)"

    # The published site is never a preview, however it was arrived at. This is
    # what `make publish-urls` writes into the committed pages.
    if [ "${url}" = "${PUBLISHED_URL}" ]; then
        return 1
    fi

    # Only a CI build of the canonical repository's main branch is building the
    # models that are about to be published. Everything else -- a branch, a fork,
    # a local checkout -- is a preview and should say so.
    #
    # The URL has to be the one this script chose, not an override: build_examples.sh
    # exports OPEN223_MODEL_BASE_URL for the whole build, so "was it overridden?"
    # cannot distinguish CI from a human, but "is it still the URL I would have
    # picked?" can.
    [ "${url}" = "$(natural_url)" ] || return 0
    [ -n "${GITHUB_ACTIONS:-}" ] || return 0
    [ "$(ci_repo)" = "${CANONICAL_REPO}" ] || return 0
    [ "$(ci_ref)" = "${CANONICAL_BRANCH}" ] || return 0
    return 1
}

if [ "${1:-}" = "--preview" ]; then
    if is_preview; then printf '1\n'; else printf '0\n'; fi
    exit 0
fi

resolve_url
