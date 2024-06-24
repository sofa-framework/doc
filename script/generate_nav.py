"""
generate_nav.py

This script visits all the files of a directory and generates a table of content for mkdocs, in the configuration
file mkdocs.yml.

Usage:
    python script.py <input_file> <input_directory>
"""


import sys
import os
import re

TAB = '  '

# Compiling the regex pattern for performance improvement
STARTING_PATTERN = re.compile(r"^\d+_")


def remove_extension(filename):
    # Split the filename by the period character
    parts = filename.split('.')
    # Join all parts except the last one to remove the extension
    name_without_extension = '.'.join(parts[:-1])
    return name_without_extension


def clean_title(s):
    if s.endswith('.md'):
        s = remove_extension(s)
    # Use regex to replace the starting substring that matches ^\d+_
    title = re.sub(r'^\d+_', '', s)
    title = title.replace("_", " ")
    return title


def contains_md_file(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                return True
    return False


def analyze_folder(yml_file, folder_path):
    with open(yml_file, "a") as file:
        nav_content = ''
        for root, dirs, files in sorted(os.walk(folder_path)):
            if root == folder_path:
                continue  # Skip the root directory
            if contains_md_file(root):
                level = root.replace(folder_path, '').count(os.sep)
                indent = TAB * level

                root_basename = os.path.basename(root)
                folder_name = clean_title(root_basename)

                nav_content += f"{indent}- {folder_name}:\n"
                subindent = TAB * (level + 1)
                for filename in sorted(files):
                    if filename.endswith('.md'):
                        relative_file_path = os.path.relpath(os.path.join(root, filename), folder_path)
                        nav_content += f"{subindent}- {clean_title(filename)}: {relative_file_path}\n"
        if nav_content != '':
            file.write('nav:\n')
            file.write(nav_content)
            print(nav_content)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <input_directory>")
        sys.exit(1)

    input_file = sys.argv[1]
    input_directory = sys.argv[2]

    print(f"Input yml file: {input_file}")
    print(f"Input directory: {input_directory}")

    analyze_folder(input_file, input_directory)
