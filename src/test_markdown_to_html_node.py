import unittest

# These imports assume that you have implemented these modules/classes.
# Adjust the import names as needed.
from markdown_to_html_node import markdown_to_html_node  # Your implementation module
from htmlnode import ParentNode, LeafNode  # Your HTML node classes
from text_to_html import TextType  # E.g., TextType.CODE for code blocks

# Helper: recursively extract concatenated text from node children.
def get_text_from_children(children):
    result = ""
    if children is None:
        return result
    for child in children:
        if hasattr(child, "value") and child.value is not None:
            result += child.value
        if hasattr(child, "children") and child.children:
            result += get_text_from_children(child.children)
    return result

class TestMarkdownToHtmlInlineElements(unittest.TestCase):

    def test_bold_text(self):
        # Markdown Bold: **bold**
        markdown = "p This is **bold** text."
        html_node = markdown_to_html_node(markdown)
        # Expect a parent node with tag "content" and one child (the paragraph)
        p_node = html_node.children[0]
        found_bold = False
        for child in p_node.children:
            if getattr(child, "tag", None) == "b":
                self.assertEqual(get_text_from_children(child.children).strip(), "bold")
                found_bold = True
        

    def test_italic_text(self):
        # Markdown Italic: *italic*
        markdown = "p This is *italic* text."
        html_node = markdown_to_html_node(markdown)
        p_node = html_node.children[0]
        found_italic = False
        for child in p_node.children:
            if getattr(child, "tag", None) == "i":
                self.assertEqual(get_text_from_children(child.children).strip(), "italic")

    def test_link(self):
        # Markdown Link: [link](https://www.google.com)
        markdown = "p This is a [link](https://www.google.com)."
        html_node = markdown_to_html_node(markdown)
        p_node = html_node.children[0]
        found_link = False
        for child in p_node.children:
            if getattr(child, "tag", None) == "a":
                # The square-bracket text is the clickable text
                self.assertEqual(get_text_from_children(child.children).strip(), "link")
                # Assume that your conversion stores the href in an 'attributes' dict.
                self.assertEqual(child.attributes.get("href"), "https://www.google.com")

    def test_image(self):
        # Markdown Image: ![alt text](url/of/image.jpg)
        markdown = "p This is an image: ![alt text](url/of/image.jpg)"
        html_node = markdown_to_html_node(markdown)
        p_node = html_node.children[0]
        found_image = False
        for child in p_node.children:
            if getattr(child, "tag", None) == "img":
                # For images, the text in square brackets is the alt text.
                self.assertEqual(child.attributes.get("src"), "url/of/image.jpg")
                self.assertEqual(child.attributes.get("alt"), "alt text")

    maxDiff = None
    def test_link_vs_image(self):
        # Demonstrate the difference between a normal link and an embedded image.
        markdown_link = "p A [link](https://example.com) is a clickable text."
        markdown_image = "p An image: ![description](https://example.com/image.jpg)"

        # Test normal link conversion.
        html_node_link = markdown_to_html_node(markdown_link)
        p_node_link = html_node_link.children[0]
        link_found = False
        for child in p_node_link.children:
            if getattr(child, "tag", None) == "a":
                self.assertEqual(get_text_from_children(child.children).strip(), "link")
                self.assertEqual(child.attributes.get("href"), "https://example.com")
 
        # Test embedded image conversion.
        html_node_image = markdown_to_html_node(markdown_image)
        p_node_image = html_node_image.children[0]
        image_found = False
        for child in p_node_image.children:
            if getattr(child, "tag", None) == "img":
                self.assertEqual(child.attributes.get("src"), "https://example.com/image.jpg")
                self.assertEqual(child.attributes.get("alt"), "description")
    
    def test_markdown_to_html_full(self):
        
        self.assertEqual(markdown_to_html_node(markdown_to_check).to_html(), html_to_check)
        
markdown_to_check = """# Sample Markdown

This is some basic, sample markdown.

## Second Heading

* Unordered lists, and:
* More


1. One
2. Two
3. Three


> Blockquote

And **bold**, *italics* [A link](https://markdowntohtml.com) to somewhere.

And code highlighting:



Or an image of bears

![bears](http://placebear.com/200/200)

The end ...

"""
html_to_check = """<h1>Sample Markdown</h1><p>This is some basic, sample markdown.</p><h2>Second Heading</h2><ul><li>Unordered lists, and:</li><li>More</li></ul><ol><li>One</li><li>Two</li><li>Three</li></ol><blockquote>Blockquote</blockquote><p>And <b>bold</b>, <i>italics</i> <a href="https://markdowntohtml.com">A link</a> to somewhere.</p><p>And code highlighting:</p><p>Or an image of bears</p><p><src="http://placebear.com/200/200" alt="bears"></p><p>The end ...</p>"""
if __name__ == '__main__':
    unittest.main()
