"""
Task Automation Script
=======================

This script extracts all email addresses from a given text file
and saves them into another output file.

Usage:
    python main.py --input input.txt --output emails.txt

Author: Abdul Hanan Zafar
Date: 2025-09-09
"""

import re
import argparse
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract_emails_from_file(input_file: str, output_file: str) -> None:
    """
    Extracts all email addresses from the input file and saves them into the output file.

    Args:
        input_file (str): Path to the input text file
        output_file (str): Path to save the extracted emails
    """
    try:
        # Read file content
        text = Path(input_file).read_text(encoding="utf-8")

        # Regex pattern for email
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        emails = re.findall(pattern, text)

        if emails:
            Path(output_file).write_text("\n".join(sorted(set(emails))), encoding="utf-8")
            logging.info(f" Extracted {len(set(emails))} email(s). Saved to '{output_file}'.")
        else:
            logging.warning(" No emails found in the file.")

    except FileNotFoundError:
        logging.error(f" File '{input_file}' not found.")
    except Exception as e:
        logging.error(f" An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description="Extract emails from a text file")
    parser.add_argument("--input", required=True, help="Path to input text file")
    parser.add_argument("--output", required=True, help="Path to save extracted emails")
    args = parser.parse_args()

    extract_emails_from_file(args.input, args.output)


if __name__ == "__main__":
    main()
