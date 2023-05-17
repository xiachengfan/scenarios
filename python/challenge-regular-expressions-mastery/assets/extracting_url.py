import re
from typing import List


def extract_urls(html: str) -> List[str]:
    """
    Extract all the unique URLs from the given HTML string.

    :param html: The input HTML string.
    :return: A list of unique URLs found in the HTML string.
    """
    # TODO: Write your code here
    # Note: Do not change the existing code


if __name__ == "__main__":
    sample_html = """
                <html>
                <head>
                <title>Example</title>
                </head>
                <body>
                <p>Here are some links:</p>
                <ul>
                <li><a href="https://www.google.com/">Google</a></li>
                <li><a href="https://www.amazon.com/">Amazon</a></li>
                <li><a href="https://www.apple.com/">Apple</a></li>
                </ul>
                </body>
                </html>
                   """

    print(extract_urls(sample_html))
