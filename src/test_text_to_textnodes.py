import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_plain_text(self):
        text = "Hello world"
        expected = [TextNode("Hello world", TextType.TEXT)]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_bold_text(self):
        text = "This is **bold** text"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_italic_text(self):
        text = "This is *italic* text"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_inline_code(self):
        text = "This is `code`"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE)
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_image(self):
        text = "![alt text](http://example.com/image.png)"
        expected = [
            TextNode("alt text", TextType.IMAGE, "http://example.com/image.png")
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_link(self):
        text = "[example](http://example.com)"
        expected = [
            TextNode("example", TextType.LINK, "http://example.com")
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_assignment_example(self):
        # This is the example provided in the assignment.
        text = ("This is **text** with an *italic* word and a `code block` and an "
                "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_complex_formatting(self):
        text = ("This is **bold** and *italic* and `code` with ![image alt](http://image.com) "
                "and a [link](http://link.com).")
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" with ", TextType.TEXT),
            TextNode("image alt", TextType.IMAGE, "http://image.com"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "http://link.com"),
            TextNode(".", TextType.TEXT)
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        text = ""
        expected = []
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_unclosed_bold(self):
        with self.assertRaises(Exception): 
            # If the bold delimiter isn't closed, catch error
            text = "This is **bold text"
            expected = [TextNode("This is **bold text", TextType.TEXT)]
            result = text_to_textnodes(text)


    def test_formatting_inside_image(self):
        # If an image node contains formatting markers inside, those markers should not be split.
        text = "![**bold image**](http://example.com)"
        expected = [TextNode("**bold image**", TextType.IMAGE, "http://example.com")]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_formatting_inside_link(self):
        # Similarly for link nodes.
        text = "[*italic link*](http://example.com)"
        expected = [TextNode("*italic link*", TextType.LINK, "http://example.com")]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
