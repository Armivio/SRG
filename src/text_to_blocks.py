import re

def text_to_blocks(text):
    blocks = re.split(r'\n\s*\n', text)
    blocks = [block for block in blocks if block]
    return blocks