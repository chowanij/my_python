#!/usr/bin/env python3
from log_parser import LogParser
from log_validator import LogValidator

LOGS_TO_PARSE = [
    "2025-01-01T10:00:00Z INFO Created quote Q123",
    "2025-01-01T10:01:00Z ERROR Failed to bind Q123",
    "2025-01-01T10:02:00Z WARN Slow response from rating engine",
    "2025-01-01T10:03:00Z INFO Created quote Q124",
    "2025-01-01T10:04:00Z DEBUG Extra debug line",
    "MALFORMED LINE HERE"
]

def main():
    """ prepare report from logs input """
    report = {
        'INFO': 0,
        'ERROR': 0,
        'WARN': 0,
        'OTHER': 0,
        'MallformedMessages': []      
    }
    parsed_logs = [LogValidator(LogParser(log).parse()).validate() for log in LOGS_TO_PARSE]
    for log in parsed_logs:
        if log['log_lvl'] in ['INFO', 'ERROR', 'WARN']:
            report[log['log_lvl']] += 1
        if not log['is_valid']:
            report['OTHER'] += 1
            report['MallformedMessages'].append(log['message'])
    print(report)

if __name__ == "__main__":
    main()
