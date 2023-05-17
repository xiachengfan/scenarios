import re
from collections import Counter
from typing import Dict, List


def parse_log_file(file_path: str) -> List[str]:
    """
    Read a log file and return a list of log entries as strings.

    :param file_path: The path to the log file.
    :return: A list of log entries as strings.
    """

    with open(file_path, "r") as log_file:
        log_entries = log_file.readlines()

    return log_entries


def analyze_log_entries(log_entries: List[str]) -> Dict[str, Dict]:
    """
    Analyze log entries and return statistics as a dictionary.

    :param log_entries: A list of log entries as strings.
    :return: A dictionary containing the analysis results.
    """

    pattern = re.compile(
        r"(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) .*"
        r'\[(?P<timestamp>.*?)\] "(?P<method>\w+) (?P<url>.*?) .*?'
        r' (?P<status>\d{3}) .* "(?P<user_agent>.*?)"'
    )

    parsed_entries = [pattern.match(entry).groupdict() for entry in log_entries]

    unique_ips = len(set(entry["ip"] for entry in parsed_entries))
    http_methods = Counter(entry["method"] for entry in parsed_entries)
    requested_resources = Counter(entry["url"] for entry in parsed_entries)
    status_codes = Counter(entry["status"] for entry in parsed_entries)
    user_agents = Counter(entry["user_agent"] for entry in parsed_entries)

    return {
        "unique_ips": unique_ips,
        "http_methods": dict(http_methods),
        "requested_resources": dict(requested_resources),
        "status_codes": dict(status_codes),
        "user_agents": dict(user_agents),
    }


if __name__ == "__main__":
    step1 = parse_log_file("sample_log.txt")
    print(f"{step1=}")
    step2 = analyze_log_entries(step1)
    print(f"{step2=}")
