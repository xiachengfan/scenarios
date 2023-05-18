import re
from typing import List


def obfuscate_emails(text: str) -> str:
    """
    Obfuscate email addresses in the given text.

    :param text: The input text containing email addresses.
    :return: The obfuscated text with email addresses modified.
    """

    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    obfuscated_text = email_pattern.sub(
        lambda x: x.group(0).replace("@", " [at] ").replace(".", " [dot] "), text
    )

    return obfuscated_text


if __name__ == "__main__":
    sample_text = "You can reach me at john.doe@gmail.com or johndoe@mycompany.com."
    print(obfuscate_emails(sample_text))
