import unittest
from textnode import TextNode, TextType
from text_to_html import text_node_to_html_node

class TestTextNodeToHTML(unittest.TestCase):
    def test_text_node_to_html_text(self):
        node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello, world!")
        self.assertEqual(html_node.props, None)

    def test_text_node_to_html_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, TextType.BOLD)
        self.assertEqual(html_node.value, "Bold text")
        self.assertEqual(html_node.props, None)

    def test_text_node_to_html_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, TextType.ITALIC)
        self.assertEqual(html_node.value, "Italic text")
        self.assertEqual(html_node.props, None)

    def test_text_node_to_html_code(self):
        node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, TextType.CODE)
        self.assertEqual(html_node.value, "Code text")
        self.assertEqual(html_node.props, None)

    def test_text_node_to_html_link(self):
        node = TextNode("Click me", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, TextType.LINK)
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_text_node_to_html_image(self):
        node = TextNode("Alt text", TextType.IMAGE, "image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, TextType.IMAGE)
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "image.png", "alt": "Alt text"})

if __name__ == "__main__":
    unittest.main()