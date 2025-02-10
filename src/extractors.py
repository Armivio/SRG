# helper functions that extract images / links from text (received in markdown format)
# !\[(.*?)\] for ![rick roll]
# !\[(.*?)\]\((.*?)\) for the whole image link
# ended up using different variants :)

import re

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)