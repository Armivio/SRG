from generate_page import extract_title
import unittest

import unittest

class TestExtractTitle(unittest.TestCase):
    def test_basic(self):
        # A simple h1 header.
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_whitespace(self):
        # Extra spaces after the hash should be removed.
        self.assertEqual(extract_title("#    Hello   "), "Hello")

    def test_multiline(self):
        # Only the first h1 header is used.
        markdown = "# Hello\nSome text\nMore text"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_header_not_first_line(self):
        # The header can appear after initial text.
        markdown = "Intro text\n# Title\nMore text"
        self.assertEqual(extract_title(markdown), "Title")

    def test_multiple_headers(self):
        # Only the first valid h1 header is returned.
        markdown = "# First\n# Second"
        self.assertEqual(extract_title(markdown), "First")

    def test_ignore_non_h1_headers(self):
        # Lines starting with "##" are not considered h1 headers.
        markdown = "## Not a title\n# Valid Title"
        self.assertEqual(extract_title(markdown), "Valid Title")

    def test_no_header(self):
        # If no h1 header is found, a ValueError is raised.
        with self.assertRaises(ValueError):
            extract_title("No header here")

    def test_empty_string(self):
        # An empty markdown string should raise an exception.
        with self.assertRaises(ValueError):
            extract_title("")

if __name__ == '__main__':
    unittest.main()
