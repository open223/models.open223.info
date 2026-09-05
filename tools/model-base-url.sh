#!/bin/bash
# Print the base URL that the generated example notebooks read models from.
#
# The URL is baked into examples/*.md when the pages are generated, so whatever
# this prints is what a reader of the built page sees and can copy.
#
#   any local build  : this checkout, so a build always validates the models you
#                      are actually editing, committed or not
#   CI, main         : https://models.open223.info -- the published models
#   CI, any branch   : that branch's models on raw.githubusercontent.com, so a
#                      preview page validates (and links to) the branch copy
#
# Export OPEN223_MODEL_BASE_URL to override all of that.
set -euo pipefail

if [ -n "${OPEN223_MODEL_BASE_URL:-}" ]; then
    printf '%s\n' "${OPEN223_MODEL_BASE_URL}"
    exit 0
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [ -z "${GITHUB_ACTIONS:-}" ]; then
    # Local build: use the working tree. It is the only copy that has edits which
    # are not committed or pushed yet, and it is what you are trying to check.
    printf 'file://%s/models\n' "${repo_root}"
    exit 0
fi

# GITHUB_HEAD_REF is set for pull_request builds, GITHUB_REF_NAME for pushes.
branch="${GITHUB_HEAD_REF:-${GITHUB_REF_NAME:-}}"

case "${branch}" in
    main|master|HEAD|"")
        printf '%s\n' "https://models.open223.info"
        exit 0
        ;;
esac

# CI branch build. For a pull request the branch lives in the head repository,
# which is the fork for a fork PR; the workflow passes it as GITHUB_HEAD_REPOSITORY
# because GITHUB_REPOSITORY is always the base repository.
repo="${GITHUB_HEAD_REPOSITORY:-${GITHUB_REPOSITORY:-open223/models.open223.info}}"
printf 'https://raw.githubusercontent.com/%s/%s/models\n' "${repo}" "${branch}"
