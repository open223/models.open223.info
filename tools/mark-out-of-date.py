import sys
import re
import datetime
import subprocess
import markdown_utils

WARNING_TEXT = "This model has not been updated since the last revision of the 223P ontology"

# matches a whole ```{warning} ... ``` block containing WARNING_TEXT, plus any
# trailing blank lines, so re-running this script does not stack up copies
WARNING_BLOCK = re.compile(
    r"```\{warning\}\n(?:(?!```)[\s\S])*?"
    + re.escape(WARNING_TEXT)
    + r"[\s\S]*?```[ \t]*\n(?:[ \t]*\n)*",
)


def remove_existing_warning(file_path):
    """Drop any previously inserted out-of-date warning.

    `insert_after_frontmatter` always inserts, so without this a second
    `make update-examples` would add a second copy of the warning. Removing it
    unconditionally also clears the warning once a model is brought up to date.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    new_content, count = WARNING_BLOCK.subn("", content)
    if count:
        print(f"Removed {count} existing out-of-date warning(s) from {file_path}")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)


def get_git_last_modified_date(file_path):
    git_cmd = ["git", "log", "-1", "--format=%ci", "--", file_path]
    date_str = subprocess.check_output(git_cmd, text=True).strip()
    return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S %z')

def generate_python_code(model_file_path):
    s223_last_updated = get_git_last_modified_date("ontologies/223p.ttl")
    model_last_updated = get_git_last_modified_date(model_file_path)
    print(f"223P last updated: {s223_last_updated} Model last updated: {model_last_updated}")
    if model_last_updated < s223_last_updated:
        s223_last_updated_formatted = s223_last_updated.strftime('%Y-%m-%d %H:%M:%S')
        model_last_updated_formatted = model_last_updated.strftime('%Y-%m-%d %H:%M:%S')
        return f"""
```{{warning}}
This model has not been updated since the last revision of the 223P ontology and it may not pass validation.

- 223P was last updated on {s223_last_updated_formatted}
- model file was last updated on {model_last_updated_formatted}
```
"""
    return ""

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python make_notebook.py <path_to_model_file> <path_to_markdown_file>")
        sys.exit(1)

    model_file_path = sys.argv[1]
    markdown_file_path = sys.argv[2]

    remove_existing_warning(markdown_file_path)

    code_content = generate_python_code(model_file_path)
    if code_content:
        markdown_utils.insert_after_frontmatter(markdown_file_path, code_content)
