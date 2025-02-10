import re
import unittest
from text_to_blocks import *

class TestTextToBlocks(unittest.TestCase):

    def test_empty_string(self):
        # An empty string should return a list with no elements.
        self.assertEqual(text_to_blocks(''), [])

    def test_single_block_no_delimiter(self):
        # Text without any double newline should be a single block.
        text = "This is a block without any delimiter."
        self.assertEqual(text_to_blocks(text), [text])

    def test_two_blocks(self):
        # A simple case with one delimiter resulting in two blocks.
        text = "Block 1\n\nBlock 2"
        self.assertEqual(text_to_blocks(text), ["Block 1", "Block 2"])

    def test_blocks_with_whitespace_in_delimiter(self):
        # Delimiter may include spaces/tabs. The regex should ignore these.
        text = "Block 1\n   \nBlock 2"
        self.assertEqual(text_to_blocks(text), ["Block 1", "Block 2"])

    def test_multiple_blocks(self):
        # Example resembling Markdown text with heading, paragraph, and list block.
        text = (
            "# This is a heading\n\n"
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n"
            "* This is the first list item in a list block\n"
            "* This is a list item\n"
            "* This is another list item"
        )
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(text_to_blocks(text), expected)

    def test_leading_and_trailing_whitespace(self):
        # Blocks may have extra spaces; splitting does not strip content.
        text = "   Block 1   \n\n   Block 2   "
        expected = ["   Block 1   ", "   Block 2   "]
        self.assertEqual(text_to_blocks(text), expected)

    def test_multiple_delimiters(self):
        # When there are multiple consecutive delimiters, empty strings may not appear.
        # For instance, "Block 1" followed by two delimiters results in an empty block between.
        text = "Block 1\n\n\n\nBlock 2"
        expected = ["Block 1", "Block 2"]
        self.assertEqual(text_to_blocks(text), expected)

if __name__ == '__main__':
    unittest.main()
