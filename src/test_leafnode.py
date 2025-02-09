import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_print_normal(self):
        node = LeafNode(TextType.NORMAL, "This is a paragraph of text.")
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
        node = LeafNode(TextType.IMAGE, "Description of image", {"img src":"url/of/image.jpg", "alt":"Description of image"})
        expected = '<img src="url/of/image.jpg" alt="Description of image">'
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()