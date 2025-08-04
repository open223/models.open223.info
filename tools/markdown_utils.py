import re

def replace_section(file_path, header, new_content_body):
    """
    Replaces the content of a section in a Markdown file.
    The section is identified by its header. The header itself is not replaced.
    If the header is not found, a ValueError is raised.
    """
    header_pattern = re.compile(r"^## .+$", re.MULTILINE)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    header_start_idx = content.find(header)
    if header_start_idx == -1:
        raise ValueError(f"The header '{header}' was not found in the file.")

    headers_start = [match.start() for match in header_pattern.finditer(content)]
    next_header_idx = None
    for start in headers_start:
        if start > header_start_idx:
            next_header_idx = start
            break

    if next_header_idx is not None:
        pre_content = content[:header_start_idx]
        post_content = content[next_header_idx:]
        new_content = f"{pre_content}{header}\n{new_content_body}\n{post_content}"
    else:
        pre_content = content[:header_start_idx]
        new_content = f"{pre_content}{header}\n{new_content_body}\n"

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def upsert_section(file_path, header, new_content_body):
    """
    Updates or inserts a section in a Markdown file.
    If the header is found, the entire section (including header) is replaced.
    If the header is not found, the new section is appended to the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_section_text = f"\n{header}\n{new_content_body}"

    if header in content:
        print(f"Header '{header}' found in file. Replacing section.")
        content = re.sub(rf"{header}[\s\S]*?(?=##|$)", new_section_text, content)
    else:
        print(f"Header '{header}' not found in file. Appending new section.")
        content += new_section_text

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def insert_after_frontmatter(file_path, content_to_insert):
    """
    Inserts content into a Markdown file right after the frontmatter.
    The frontmatter is identified by two '---' separators.
    """
    with open(file_path, "r", encoding='utf-8') as file:
        content = file.read()
    # put the content right after the markdown header (after the 2nd ---)
    content = '---' + content[3:].replace("---", "---\n" + content_to_insert, 1)
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(content)
