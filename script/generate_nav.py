"""
generate_nav.py

This script visits all the files of a directory and generates a table of content for mkdocs, in the configuration
file mkdocs.yml.
During the visit, it also renames the files and the folders to remove the numeric suffix. The suffixes are here
just to define the order in the table of content.

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


def clean_filename(s):
    # Use regex to replace the starting substring that matches ^\d+_
    s = re.sub(r'^\d+_', '', s)
    s = to_lowercase(s)
    return s

def to_lowercase(input_string):
    # Function to convert uppercase letters to lowercase
    return input_string.lower()


def clean_title(s):
    if s.endswith('.md'):
        s = remove_extension(s)
    s = clean_filename(s)
    s = s.replace("_", " ")
    return s

def clean_file_url(s):
    s = clean_filename(s)
    s = s.replace("_", "-")
    return s


def clean_path(path):
    # Split the path into components
    components = path.split(os.sep)

    # Apply clean_filename to each component
    cleaned_components = [clean_file_url(component) for component in components]

    # Join the cleaned components back into a path
    cleaned_path = os.sep.join(cleaned_components)

    return cleaned_path


def contains_md_file(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                return True
    return False


def rename_directory(directory):
    [dir_head, dir_basename] = os.path.split(directory)
    new_directory_name = os.path.join(dir_head, clean_file_url(dir_basename))
    if not os.path.exists(new_directory_name):
        print('rename', directory, new_directory_name)
        os.rename(directory, new_directory_name)


def analyze_folder(yml_file, folder_path):
    with open(yml_file, "a") as file:
        nav_content = ''
        for root, dirs, files in sorted(os.walk(folder_path)):
            if root == folder_path:
                continue  # Skip the root directory
            if contains_md_file(root):
                level = root.replace(folder_path, '').count(os.sep)
                indent = TAB * level

                [root_head, root_basename] = os.path.split(root)
                folder_name = clean_title(root_basename)

                nav_content += f"{indent}- {folder_name}:\n"
                subindent = TAB * (level + 1)
                for filename in sorted(files):
                    if filename.endswith('.md'):
                        cleaned_filename = clean_file_url(filename)
                        os.rename(os.path.join(root, filename), os.path.join(root, cleaned_filename))
                        relative_file_path = os.path.relpath(os.path.join(root, cleaned_filename), folder_path)
                        relative_file_path = clean_path(relative_file_path)
                        nav_content += f"{subindent}- {clean_title(filename)}: {relative_file_path}\n"

        if nav_content != '':
            file.write('nav:\n')
            file.write(nav_content)
            print(nav_content)

        for root, dirs, files in os.walk(folder_path, False):
            if root == folder_path:
                continue  # Skip the root directory
            for directory in dirs:
                full_directory = os.path.join(root, directory)
                print('visiting', full_directory)
                rename_directory(full_directory)
            rename_directory(root)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <input_directory>")
        sys.exit(1)

    input_file = sys.argv[1]
    input_directory = sys.argv[2]

    print(f"Input yml file: {input_file}")
    print(f"Input directory: {input_directory}")

    analyze_folder(input_file, input_directory)
