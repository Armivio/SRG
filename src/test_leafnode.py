import unittest
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_print_normal(self):
        node = LeafNode(TextType.TEXT, "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected)

    def test_print_bold(self):
        node = LeafNode(TextType.BOLD, "This is a paragraph of text.")
        expected = "<b>This is a paragraph of text.</b>"
        self.assertEqual(node.to_html(), expected)

    def test_print_italic(self):
        node = LeafNode(TextType.ITALIC, "This is a paragraph of text.")
        expected = "<i>This is a paragraph of text.</i>"
        self.assertEqual(node.to_html(), expected)

    def test_print_code(self):
        node = LeafNode(TextType.CODE, "This is a paragraph of text.")
        expected = "<code>This is a paragraph of text.</code>"
        self.assertEqual(node.to_html(), expected)

    def test_print_link(self):
        node = LeafNode(TextType.LINK, "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_print_image(self):
        node = LeafNode(TextType.IMAGE, "Bad description of image", {"img src":"url/of/image.jpg", "alt":"Description of image"})
        expected = '<img src="url/of/image.jpg" alt="Description of image">'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_no_children(self):
        node = LeafNode(TextType.TEXT, "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")



if __name__ == "__main__":
    unittest.main()