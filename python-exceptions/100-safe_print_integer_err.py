#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Prints an integer with "{:d}".format().
    If an error occurs, prints the error message to stderr.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
