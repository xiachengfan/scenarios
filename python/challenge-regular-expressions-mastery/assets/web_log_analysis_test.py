import unittest
import sys

sys.path.append("/home/labex/project")
from web_log_analysis import parse_log_file, analyze_log_entries


class TestWebLogAnalysis(unittest.TestCase):
    def setUp(self):
        self.sample_log = [
            '127.0.0.1 - - [26/Apr/2023:16:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024 "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"',
            '127.0.0.2 - - [26/Apr/2023:16:01:00 +0000] "POST /login HTTP/1.1" 200 512 "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"',
            '127.0.0.1 - - [26/Apr/2023:16:02:00 +0000] "GET /dashboard HTTP/1.1" 403 256 "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"',
        ]

    def test_parse_log_file(self):
        with open("sample_log.txt", "w", encoding="utf-8") as sample_file:
            sample_file.write(
                '127.0.0.1 - - [26/Apr/2023:16:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024 "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"\n'
            )
            sample_file.write(
                '127.0.0.2 - - [26/Apr/2023:16:01:00 +0000] "POST /login HTTP/1.1" 200 512 "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"\n'
            )

        log_entries = parse_log_file("sample_log.txt")
        self.assertIsInstance(log_entries, list)
        self.assertGreater(len(log_entries), 0)

    def test_analyze_log_entries(self):
        analysis = analyze_log_entries(self.sample_log)

        self.assertEqual(analysis["unique_ips"], 2)
        self.assertEqual(analysis["http_methods"]["GET"], 2)
        self.assertEqual(analysis["http_methods"]["POST"], 1)
        self.assertEqual(analysis["requested_resources"]["/index.html"], 1)
        self.assertEqual(analysis["requested_resources"]["/login"], 1)
        self.assertEqual(analysis["requested_resources"]["/dashboard"], 1)
        self.assertEqual(analysis["status_codes"]["200"], 2)
        self.assertEqual(analysis["status_codes"]["403"], 1)
        self.assertEqual(
            analysis["user_agents"]["Mozilla/5.0 (Windows NT 10.0; Win64; x64)"], 3
        )


if __name__ == "__main__":
    unittest.main()
