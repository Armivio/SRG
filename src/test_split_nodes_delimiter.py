import unittest
from textnode import *
from split_nodes_delimiter import *

# Test cases for split_nodes_delimiter.
class TestSplitNodesDelimiter(unittest.TestCase):

    def test_no_delimiter(self):
        # When no delimiter is present, the node should be returned unchanged.
        node = TextNode("Hello world", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])

    def test_single_code_split(self):
        # Splitting a code block delimited by backticks.
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, expected)

    def test_bold_split(self):
        # Splitting bold text delimited by '**'
        node = TextNode("This is **bolded** text", TextType.TEXT)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_italic_split(self):
        # Splitting italic text delimited by '*'
        node = TextNode("This is *italic* text", TextType.TEXT)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(result, expected)

    def test_delimiter_at_beginning(self):
        # When the delimiter is at the very beginning (or end),
        # empty strings are produced.
        node = TextNode("`code`", TextType.TEXT)
        expected = [
            TextNode("", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("", TextType.TEXT)
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, expected)

    def test_invalid_markdown(self):
        # Odd number of delimiters should raise an Exception.
        node = TextNode("This is a `test", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertIn("Invalid Markdown Syntax", str(context.exception))

    def test_multiple_occurrences(self):
        # The string contains two separate code blocks.
        node = TextNode("Hello `code` and `more code`", TextType.TEXT)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("more code", TextType.CODE),
            TextNode("", TextType.TEXT)
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, expected)

    # def test_no_split_for_non_text_type(self):
    #     # Nodes that are not of type TEXT should be left unchanged.
    #     node = TextNode("Hello `code`", TextType.BOLD)
    #     result = split_nodes_delimiter([node], "`", TextType.CODE)
    #    # Expected: no splitting, even though the text contains the delimiter.
    #     self.assertEqual(result, [node])

if __name__ == '__main__':
    unittest.main()
