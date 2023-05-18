import unittest
import sys

sys.path.append("/home/labex/project")
from extracting_information import parse_config_file


class TestConfigFileParsing(unittest.TestCase):
    def test_parse_config_file(self):
        sample_config = """
            [General]
            app_name = MyApp
            version = 1.0.0

            [Database]
            host = 127.0.0.1
            port = 5432
            user = admin
            password = secret
        """

        expected_output = {
            "General": {
                "app_name": "MyApp",
                "version": "1.0.0",
            },
            "Database": {
                "host": "127.0.0.1",
                "port": "5432",
                "user": "admin",
                "password": "secret",
            },
        }

        parsed_config = parse_config_file(sample_config)
        self.assertEqual(parsed_config, expected_output)

    def test_empty_config(self):
        sample_config = ""
        expected_output = {}

        parsed_config = parse_config_file(sample_config)
        self.assertEqual(parsed_config, expected_output)


if __name__ == "__main__":
    unittest.main()
