"""
title_metadata.py

This script recursively processes files in a specified directory, adding metadata to files
whose names start with one or more digits followed by an underscore. The metadata includes
a title extracted from the filename and added as a YAML header.

Usage:
    python script.py <input_directory>
"""

import sys
import re
import os

# Compiling the regex pattern for performance improvement
STARTING_PATTERN = re.compile(r"^\d+_")


def starts_with_digits_and_underscore(text):
    """
    Checks if the given text starts with one or more digits followed by an underscore.

    Parameters:
        text (str): The text to check.

    Returns:
        bool: True if the text matches the pattern, False otherwise.
    """
    return bool(STARTING_PATTERN.match(text))


def add_metadata(filepath):
    """
    Adds metadata to a file. The metadata includes a title extracted from the filename.

    Parameters:
        filepath (str): The path to the file to which metadata will be added.
    """
    filename = os.path.basename(filepath)
    filename = os.path.splitext(filename)[0]
    match = STARTING_PATTERN.search(filename)
    title = filename[match.end():] if match else filename
    title = title.replace("_", " ")
    header_text = f"---\ntitle: {title}\n---\n\n"

    with open(filepath, "r+", encoding='utf-8') as file:
        content = file.read()
        if not content.startswith(header_text):
            file.seek(0)
            file.write(header_text + content)
            file.truncate()


def analyze_folder(folder_path):
    """
    Recursively analyzes a folder and adds metadata to all files whose names
    start with one or more digits followed by an underscore.

    Parameters:
        folder_path (str): The path to the folder to analyze.
    """
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if starts_with_digits_and_underscore(filename):
                filepath = os.path.join(root, filename)
                print(f"Adding metadata to: {filepath}")
                add_metadata(filepath)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]

    if not os.path.isdir(input_directory):
        print(f"Error: {input_directory} is not a valid directory.")
        sys.exit(1)

    print(f"Input directory: {input_directory}")

    analyze_folder(input_directory)
