#!/bin/bash
set -euo pipefail

# Accept an explicit publish directory, or detect the output used by the
# installed Jupyter Book/MyST version.
if [ "$#" -gt 1 ]; then
    echo "Usage: $0 [site-directory]" >&2
    exit 2
fi

if [ "$#" -eq 1 ]; then
    site_dir="$1"
elif [ -f _build/html/index.html ]; then
    site_dir="_build/html"
elif [ -f _build/site/public/index.html ]; then
    site_dir="_build/site/public"
else
    echo "Could not find a publishable site with index.html in _build/html or _build/site/public" >&2
    find _build -maxdepth 3 -type f | sed -n '1,200p' >&2
    exit 1
fi

if [ ! -f "${site_dir}/index.html" ]; then
    echo "Site directory does not contain index.html: ${site_dir}" >&2
    exit 1
fi

cp CNAME "${site_dir}/"
mkdir -p "${site_dir}/models" "${site_dir}/compiled" "${site_dir}/withimports"

# Keep source model downloads at both legacy root paths and /models/.
find models -maxdepth 1 -type f \( -name '*.ttl' -o -name '*.jsonld' \) -exec cp {} "${site_dir}/" \;
find models -maxdepth 1 -type f \( -name '*.ttl' -o -name '*.jsonld' \) -exec cp {} "${site_dir}/models/" \;
find models/compiled -maxdepth 1 -type f -name '*.ttl' -exec cp {} "${site_dir}/compiled/" \;
find models/withimports -maxdepth 1 -type f -name '*.ttl' -exec cp {} "${site_dir}/withimports/" \;

# Print only the resolved path on stdout so callers can capture it.
printf '%s\n' "${site_dir}"
