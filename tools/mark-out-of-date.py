import sys
import datetime
import os


def generate_python_code(model_file_path):
    s223_last_updated = os.path.getmtime("ontologies/223p.ttl")
    model_last_updated = os.path.getmtime(model_file_path)
    if model_last_updated < s223_last_updated:
        s223_last_updated_formatted = datetime.datetime.fromtimestamp(s223_last_updated).strftime('%Y-%m-%d %H:%M:%S')
        model_last_updated_formatted = datetime.datetime.fromtimestamp(model_last_updated).strftime('%Y-%m-%d %H:%M:%S')
        return f"""
```{{warning}}
This model has not been updated since the last revision of the 223P ontology, and it may not pass validation.
223P was last updated on {s223_last_updated_formatted}. The model file was last updated on {model_last_updated_formatted}
```
        """
    return ""
    
def add_code_to_markdown(markdown_file_path, code_content):
    with open(markdown_file_path, "r") as file:
        content = file.read()
    # put the content right after the markdown header (after the 2nd ---)
    content = '---' + content[3:].replace("---", "---\n" + code_content, 1)
    with open(markdown_file_path, "w") as file:
        file.write(content)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python make_notebook.py <path_to_model_file> <path_to_markdown_file>")
        sys.exit(1)

    model_file_path = sys.argv[1]
    markdown_file_path = sys.argv[2]

    code_content = generate_python_code(model_file_path)
    add_code_to_markdown(markdown_file_path, code_content)
