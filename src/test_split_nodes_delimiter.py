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

# Replace 'your_module' with the actual module name where your functions are defined.

# --- Tests for Images ---

    def test_split_nodes_image_no_image(self):
        # No markdown image present → should return the original node.
        text = "This is some text without any image."
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_image([node])
        
        self.assertEqual(result, [node])

    def test_split_nodes_image_only_image(self):
        # The node consists solely of an image markdown.
        text = "![alt](http://example.com/image.png)"
        node = TextNode(text, TextType.TEXT)
        expected = [TextNode("alt", TextType.IMAGE, "http://example.com/image.png")]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_split_nodes_image_image_at_beginning(self):
        # The image markdown appears at the very beginning.
        text = "![alt](http://example.com/image.png) suffix text"
        node = TextNode(text, TextType.TEXT)
        expected = [
            TextNode("alt", TextType.IMAGE, "http://example.com/image.png"),
            TextNode(" suffix text", TextType.TEXT)
        ]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_split_nodes_image_image_at_end(self):
        # The image markdown appears at the end.
        text = "prefix text ![alt](http://example.com/image.png)"
        node = TextNode(text, TextType.TEXT)
        expected = [
            TextNode("prefix text ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "http://example.com/image.png")
        ]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_split_nodes_image_multiple_images(self):
        # Two images in one node, with text before, between, and after.
        text = "Start ![img1](http://example.com/1.png) Middle ![img2](http://example.com/2.png) End"
        node = TextNode(text, TextType.TEXT)
        expected = [
            TextNode("Start ", TextType.TEXT),
            TextNode("img1", TextType.IMAGE, "http://example.com/1.png"),
            TextNode(" Middle ", TextType.TEXT),
            TextNode("img2", TextType.IMAGE, "http://example.com/2.png"),
            TextNode(" End", TextType.TEXT)
        ]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_split_nodes_image_consecutive_images(self):
        # Two images with no text in between; empty text nodes should be omitted.
        text = "![img1](http://example.com/1.png)![img2](http://example.com/2.png)"
        node = TextNode(text, TextType.TEXT)
        expected = [
            TextNode("img1", TextType.IMAGE, "http://example.com/1.png"),
            TextNode("img2", TextType.IMAGE, "http://example.com/2.png")
        ]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    # --- Tests for Links ---

    def test_split_nodes_link_no_link(self):
        # No markdown link → returns original node.
        text = "This is some text without any link."
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        assert result == [node]

    def test_split_nodes_link_only_link(self):
        # The node consists solely of a link markdown.
        text = "[boot.dev](https://www.boot.dev)"
        node = TextNode(text, TextType.TEXT)
        expected = [TextNode("boot.dev", TextType.LINK, "https://www.boot.dev")]
        result = split_nodes_link([node])
        assert result == expected

    def test_split_nodes_link_link_at_beginning(self):
        # The link appears at the beginning.
        text = "[boot.dev](https://www.boot.dev) and some text"
        node = TextNode(text, TextType.TEXT)
        expected = [
            TextNode("boot.dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and some text", TextType.TEXT)
        ]
        result = split_nodes_link([node])
        assert result == expected

    def test_split_nodes_link_link_at_end(self):
        # The link appears at the end.
        text = "Some text and then [youtube](https://www.youtube.com)"
        node = TextNode(text, TextType.TEXT)
        expected = [
            TextNode("Some text and then ", TextType.TEXT),
            TextNode("youtube", TextType.LINK, "https://www.youtube.com")
        ]
        result = split_nodes_link([node])
        assert result == expected

    def test_split_nodes_link_multiple_links(self):
        # Two links separated by text.
        text = "A [first](https://first.com) and [second](https://second.com) link"
        node = TextNode(text, TextType.TEXT)
        expected = [
            TextNode("A ", TextType.TEXT),
            TextNode("first", TextType.LINK, "https://first.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("second", TextType.LINK, "https://second.com"),
            TextNode(" link", TextType.TEXT)
        ]
        result = split_nodes_link([node])
        assert result == expected

    def test_split_nodes_link_consecutive_links(self):
        # Two links with no intervening text.
        text = "[first](https://first.com)[second](https://second.com)"
        node = TextNode(text, TextType.TEXT)
        expected = [
            TextNode("first", TextType.LINK, "https://first.com"),
            TextNode("second", TextType.LINK, "https://second.com")
        ]
        result = split_nodes_link([node])
        assert result == expected

if __name__ == '__main__':
    unittest.main()
