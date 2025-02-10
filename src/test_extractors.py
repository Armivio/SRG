import unittest
from extractors import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):
    # Tests for extract_markdown_images

    def test_single_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_multiple_images(self):
        text = ("First image: ![img1](https://example.com/1.png) "
                "and second image: ![img2](https://example.com/2.png)")
        expected = [("img1", "https://example.com/1.png"),
                    ("img2", "https://example.com/2.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_no_images(self):
        text = "There are no images in this text."
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_empty_alt_image(self):
        text = "Empty alt image: ![](https://example.com/empty.png)"
        expected = [("", "https://example.com/empty.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_malformed_image_markdown(self):
        text = "Malformed image markdown: ![alt](https://example.com/missing_end"
        expected = []  # Missing closing parenthesis; no match expected.
        self.assertEqual(extract_markdown_images(text), expected)

    # Tests for extract_markdown_links

    def test_single_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        expected = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_multiple_links(self):
        text = ("Visit [Google](https://google.com) and "
                "[Bing](https://bing.com) for search options.")
        expected = [("Google", "https://google.com"),
                    ("Bing", "https://bing.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_links_exclude_images(self):
        text = ("Mixing an image and a link: ![img](https://example.com/img.png) "
                "and a link [example](https://example.com/link)")
        expected_images = [("img", "https://example.com/img.png")]
        expected_links = [("example", "https://example.com/link")]
        self.assertEqual(extract_markdown_images(text), expected_images)
        self.assertEqual(extract_markdown_links(text), expected_links)

    def test_no_links(self):
        text = "This text does not contain any markdown links."
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

    def test_empty_link_text(self):
        text = "Empty link text: [](https://example.com/empty)"
        expected = [("", "https://example.com/empty")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_malformed_link_markdown(self):
        text = "Malformed link markdown: [broken](https://example.com/missing_end"
        expected = []  # No match due to missing closing parenthesis.
        self.assertEqual(extract_markdown_links(text), expected)

if __name__ == "__main__":
    unittest.main()
