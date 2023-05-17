import unittest
import sys

sys.path.append("/home/labex/project")
from email_obfuscation import obfuscate_emails


class TestEmailObfuscation(unittest.TestCase):
    def test_obfuscate_emails(self):
        sample_text = "Please contact us at support@example.com or admin@example.org for assistance."
        expected_output = "Please contact us at support [at] example [dot] com or admin [at] example [dot] org for assistance."

        obfuscated_text = obfuscate_emails(sample_text)
        self.assertEqual(obfuscated_text, expected_output)

    def test_no_emails(self):
        sample_text = "This text contains no email addresses."
        obfuscated_text = obfuscate_emails(sample_text)
        self.assertEqual(obfuscated_text, sample_text)


if __name__ == "__main__":
    unittest.main()
