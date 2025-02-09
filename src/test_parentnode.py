import unittest
from htmlnode import LeafNode, ParentNode
from textnode import TextType

class TestParentNode(unittest.TestCase):
    def test_parent_without_tag(self):
        # Test that initializing without a tag raises an error
        leaf = LeafNode(TextType.NORMAL, "Test text")
        with self.assertRaises(ValueError):
            node = ParentNode(None, [leaf])
            node.to_html()
    
    def test_parent_without_children(self):
        # Test that initializing without children raises an error
        with self.assertRaises(ValueError):
            node = ParentNode(TextType.NORMAL, children=[])
            node.to_html()

    def test_normal_parent(self):
        # Test a paragraph with multiple text nodes
        child1 = LeafNode(None, "First")
        child2 = LeafNode(None, " and ")
        child3 = LeafNode(None, "second")
        parent = ParentNode(TextType.NORMAL, [child1, child2, child3])
        expected = "<p>First and second</p>"
        self.assertEqual(parent.to_html(), expected)

    def test_nested_formatting(self):
        # Test nested formatting (bold inside italic)
        bold_text = LeafNode(TextType.BOLD, "bold")
        italic = ParentNode(TextType.ITALIC, [
            LeafNode(None, "This is "),
            bold_text,
            LeafNode(None, " text")
        ])
        expected = "<i>This is <b>bold</b> text</i>"
        self.assertEqual(italic.to_html(), expected)

    def test_link_with_formatted_text(self):
        # Test a link containing formatted text
        link = ParentNode(TextType.LINK, [
            LeafNode(None, "Click "),
            LeafNode(TextType.BOLD, "here"),
            LeafNode(None, "!")
        ], props={"href": "https://www.example.com"})
        expected = '<a href="https://www.example.com">Click <b>here</b>!</a>'
        self.assertEqual(link.to_html(), expected)

    def test_image_with_children(self):
        # Test that creating an image with children raises an exception
        with self.assertRaises(Exception):
            node = ParentNode(TextType.IMAGE, [LeafNode(None, "test")])
            node.to_html()

if __name__ == "__main__":
    unittest.main()