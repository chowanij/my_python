"""Log parser module for processing and parsing log entries.

This module provides functionality to parse log entries and extract
structured information including log type, timestamp, message, and quote ID.
"""
import re
from typing import TypedDict, Literal

class ParsedLogs(TypedDict, total = False):
    log_lvl: Literal['ERROR', 'INFO', 'WARN', 'DEBUG', 'EMPTY']
    timestamp: str
    message: str
    qoute_id: str
    is_valid: bool


class LogParser:
    LOG_LVLS = ['ERROR', 'INFO', 'WARN', 'DEBUG']
    def __init__(self, log_row: str):
        self.log_row = log_row
        self.log_item: ParsedLogs = {
            'log_lvl': 'INFO',
            'timestamp': '',
            'message': '',
            'quote_id': '',
            'is_valid': False
        }

    def parse(self) -> ParsedLogs:
        """parse log row passed into constructor and save result into log_item structure"""
        self.__parse_timestamp()
        self.__parse_level()
        self.__parse_quote_id()
        self.__parse_msg()
        return self.log_item

    def __parse_timestamp(self):
        [checked, _] =self.log_row.split(' ', 1)
        iso_reg = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$'
        regex_pattern = re.compile(iso_reg)
        self.log_item['timestamp'] = checked if regex_pattern.match(checked) else ''

    def __parse_level(self):
        [*check_parts, _] = self.log_row.split(' ', 2)
        if check_parts[1] in LogParser.LOG_LVLS:
            self.log_item['log_lvl']=check_parts[1]
        elif check_parts[0] in LogParser.LOG_LVLS:
            self.log_item['log_lvl']=check_parts[0]
        else:
            self.log_item['log_lvl']='EMPTY'

    def __parse_quote_id(self):
        [checked, _] =self.log_row.rsplit(' ', 1)
        qid_reg = r'^Q\d\d\d'
        regex_pattern = re.compile(qid_reg)
        if regex_pattern.match(checked):
            self.log_item['quote_id'] = checked

    def __parse_msg(self):
        self.log_item['message'] = (
            self.log_row
            .replace(self.log_item['timestamp'], '')
            .replace(self.log_item['log_lvl'], '')
            .replace(self.log_item['quote_id'], '')
        )
lp = LogParser('2025-01-01T10:00:00Z INFO Created quote Q123')
lp.parse()
