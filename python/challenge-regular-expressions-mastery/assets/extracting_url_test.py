import unittest
import sys

sys.path.append("/home/labex/project")
from extracting_url import extract_urls


class TestUrlExtraction(unittest.TestCase):
    def test_extract_urls(self):
        sample_html = """
            <html>
            <head>
                <title>Sample Web Page</title>
            </head>
            <body>
                <p>Visit <a href="https://www.example.com">Example</a> website.</p>
                <p>Check out our <a href="https://blog.example.com">blog</a>.</p>
                <p>Image source: <img src="https://images.example.com/sample.jpg" /></p>
                <p>Visit <a href="https://www.example.com">Example</a> website again.</p>
            </body>
            </html>
        """

        expected_output = [
            "https://www.example.com",
            "https://blog.example.com",
            "https://images.example.com/sample.jpg",
        ]

        extracted_urls = extract_urls(sample_html)
        self.assertEqual(sorted(extracted_urls), sorted(expected_output))

    def test_no_urls(self):
        sample_html = """
            <html>
            <head>
                <title>No URLs here</title>
            </head>
            <body>
                <p>This web page does not contain any URLs.</p>
            </body>
            </html>
        """

        expected_output = []

        extracted_urls = extract_urls(sample_html)
        self.assertEqual(extracted_urls, expected_output)


if __name__ == "__main__":
    unittest.main()
