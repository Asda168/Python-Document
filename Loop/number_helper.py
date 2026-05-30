import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from helpers.helper import (
    format_number,
    format_currency,
    format_percentage,
    format_compact,
)


def _print_result(label, value):
    """Internal helper to print label + value consistently."""
    print(f"  {label:<20} → {value}")


def print_number(number, decimals=2, thousands_sep=',', decimal_sep='.', prefix='', suffix='', label=None):
    result = format_number(number, decimals, thousands_sep, decimal_sep, prefix, suffix)
    _print_result(label or "Number", result)

def print_currency(number, symbol='$', decimals=2, label=None):
    result = format_currency(number, symbol, decimals)
    _print_result(label or "Currency", result)

def print_percentage(number, decimals=1, label=None):
    result = format_percentage(number, decimals)
    _print_result(label or "Percentage", result)

def print_compact(number, label=None):
    result = format_compact(number)
    _print_result(label or "Compact", result)


if __name__ == "__main__":
    print("=== Number ===")
    print_number(1234567.891)
    print_number(1234567.891, decimals=0)
    print_number(1234567.89, thousands_sep='.', decimal_sep=',', label="EU Format")

    print("\n=== Currency ===")
    print_currency(9999.5)
    print_currency(9999.5, symbol='€', label="Euros")
    print_currency(9999.5, symbol='฿', label="Baht")

    print("\n=== Percentage ===")
    print_percentage(87.5678)
    print_percentage(12.3456, decimals=2, label="High Precision")

    print("\n=== Compact ===")
    print_compact(1_500)
    print_compact(2_300_000)
    print_compact(8_100_000_000)
    print_compact(-450_000, label="Negative")