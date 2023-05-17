import re
from typing import List


def extract_urls(html: str) -> List[str]:
    """
    Extract all the unique URLs from the given HTML string.

    :param html: The input HTML string.
    :return: A list of unique URLs found in the HTML string.
    """
    url_pattern = re.compile(
        r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'
    )

    urls = [url_match.group(0) for url_match in url_pattern.finditer(html)]
    unique_urls = list(set(urls))

    return unique_urls


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
