# log_parser.py
"""
Log parser module for processing and parsing log entries.

This module provides functionality to parse log entries and extract
structured information including log level, timestamp, message, and quote ID.
"""

import re
from typing import TypedDict, Literal


class ParsedLog(TypedDict, total=False):
    log_lvl: Literal["ERROR", "INFO", "WARN", "DEBUG", "EMPTY"]
    timestamp: str
    message: str
    quote_id: str
    is_valid: bool


class LogParser:
    LOG_LEVELS = ["ERROR", "INFO", "WARN", "DEBUG"]

    ISO_TS_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    QUOTE_ID_REGEX = re.compile(r"\bQ\d+\b")

    def __init__(self, log_row: str):
        self.log_row = log_row
        self.log_item: ParsedLog = {
            "log_lvl": "EMPTY",
            "timestamp": "",
            "message": "",
            "quote_id": "",
            "is_valid": False,
        }

    def parse(self) -> ParsedLog:
        """Parse a single log row into a structured ParsedLog dict."""
        parts = self.log_row.split(maxsplit=2)
        self.__parse_timestamp(parts)
        self.__parse_level(parts)
        self.__parse_message(parts)
        self.__parse_quote_id()
        return self.log_item

    def __parse_timestamp(self, parts: list[str]) -> None:
        if parts and self.ISO_TS_REGEX.match(parts[0]):
            self.log_item["timestamp"] = parts[0]
        else:
            self.log_item["timestamp"] = ""

    def __parse_level(self, parts: list[str]) -> None:
        # Prefer the second token as log level (typical format)
        if len(parts) >= 2 and parts[1] in self.LOG_LEVELS:
            self.log_item["log_lvl"] = parts[1]
        # Fallback: maybe level is the first token
        elif parts and parts[0] in self.LOG_LEVELS:
            self.log_item["log_lvl"] = parts[0]
        else:
            self.log_item["log_lvl"] = "EMPTY"

    def __parse_message(self, parts: list[str]) -> None:
        # Message is whatever is left after timestamp + level
        if len(parts) == 3:
            msg = parts[2]
        elif len(parts) > 0:
            # If we have at least one token, but don't know the format,
            # treat everything after detected level/timestamp as message.
            msg = self.log_row
        else:
            msg = ""

        self.log_item["message"] = msg.strip()

    def __parse_quote_id(self) -> None:
        # Try to extract quote id from the message text
        msg = self.log_item["message"]
        match = self.QUOTE_ID_REGEX.search(msg)
        if match:
            qid = match.group(0)
            self.log_item["quote_id"] = qid
            # Optional: remove quote id from message for cleaner text
            cleaned = self.QUOTE_ID_REGEX.sub("", msg).strip()
            self.log_item["message"] = cleaned
        else:
            self.log_item["quote_id"] = ""
