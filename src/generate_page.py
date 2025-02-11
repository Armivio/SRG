from htmlnode import *
from markdown_to_html_node import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No h1 header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file_markdown = open(from_path, 'r')
    markdown = file_markdown.read()

    file_template = open(template_path, 'r')
    template = file_template.read()
    html_content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)

    # Ensure the destination directory exists.
    directory = os.path.dirname(dest_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    # Write the full HTML (stored in the variable 'result') to the file.
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for directory in os.listdir(dir_path_content):
        # print("the current file to be deleted is " + directory)
        if os.path.isfile(f"{dir_path_content}/{directory}"):
            if directory[-3:] == ".md":
                generate_page(os.path.join(dir_path_content, directory), template_path, os.path.join(dest_dir_path, directory[:-3] + ".html"))
        else:
            os.makedirs(os.path.join(dest_dir_path, directory), exist_ok=True)
            generate_pages_recursive(os.path.join(dir_path_content, directory), template_path, os.path.join(dest_dir_path, directory))
                