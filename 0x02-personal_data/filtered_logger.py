#!/usr/bin/env python3
""" Task 0: Write a function that returns the log message obfuscated """
""" Task 1: Update class to accept a list of strs fields constructor arg """
"""Implement the format method to filter values in incoming log records """
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Creating an instance of class above """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """ Formats the record - self.FORMAT """
        return filter_datum(
            self.fields, self.REDACTION, super().format(record),
            self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ Returns the log message obfuscated """
    for field in fields:
        message = re.sub(
            f"(?<={field}=).*?(?={separator})", redaction, message)
    return message