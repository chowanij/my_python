#!/usr/bin/env python3


from log_parser import LogParser
from log_validator import LogValidator

LOGS_TO_PARSE = [
    "2025-01-01T10:00:00Z INFO Created quote Q123",
    "2025-01-01T10:01:00Z ERROR Failed to bind Q123",
    "2025-01-01T10:02:00Z WARN Slow response from rating engine",
    "2025-01-01T10:03:00Z INFO Created quote Q124",
    "2025-01-01T10:04:00Z DEBUG Extra debug line",
    "MALFORMED LINE HERE",
]


def summarize_logs(log_lines: list[str]) -> dict:
    """Prepare report from provided log lines."""
    report = {
        "INFO": 0,
        "ERROR": 0,
        "WARN": 0,
        "OTHER": 0,
        "MalformedMessages": [],
    }

    parsed_logs = []
    for raw in log_lines:
        parsed = LogParser(raw).parse()
        validated = LogValidator(parsed).validate()
        parsed_logs.append((raw, validated))

    for raw, log in parsed_logs:
        lvl = log.get("log_lvl", "EMPTY")
        is_valid = log.get("is_valid", False)

        if lvl in ["INFO", "ERROR", "WARN"] and is_valid:
            report[lvl] += 1
        else:
            report["OTHER"] += 1
            report["MalformedMessages"].append(raw)

    return report


def main():
    report = summarize_logs(LOGS_TO_PARSE)
    print(report)


if __name__ == "__main__":
    main()