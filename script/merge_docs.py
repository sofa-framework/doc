"""
merge_docs.py

This script merges the manual SOFA documentation with the automatically generated documentation. This assumes the
same folder structure.

Usage:
    python merge_docs.py <source_dir> <dest_dir>

<source_dir>: Directory containing the automatically generated documentation
<dest_dir>: Directory containing the manual SOFA documentation
"""


import shutil
import os
import sys


def extract_content(filename, starting_content, ending_content):
    with open(filename, 'r') as f:
        in_target_block = False
        target_content = []
        for line in f:
            if line.startswith(starting_content):
                in_target_block = True
            if in_target_block:
                if ending_content and line.startswith(ending_content):
                    in_target_block = False
                else:
                    if not line.startswith('# '):
                        target_content.append(line)
    return ''.join(target_content)


def replace_target_content(filename, starting_content, ending_content, replacement):
    with open(filename, 'r') as f:
        in_target_block = False
        new_content = []
        for line in f:
            if line.startswith(starting_content):
                new_content.append(line)
                in_target_block = True
            if in_target_block:
                if line.startswith(ending_content):
                    in_target_block = False
                    new_content.append(replacement)  # Replace target lines
                    new_content.append(line)
            else:
                new_content.append(line)
    new_file_content = ''.join(new_content)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_file_content)


def merge_files(source_file, target_file):
    print('Extracting content from source', source_file)
    source_content = extract_content(source_file, "<!-- generate_doc -->", "")

    start_autodoc = "<!-- automatically generated doc START -->"
    end_autodoc = "<!-- automatically generated doc END -->"

    print('Extracting content from target', target_file)
    target_content = extract_content(target_file, start_autodoc, end_autodoc)

    if target_content:
        print('Replacing content in', target_file)
        replace_target_content(target_file, start_autodoc, end_autodoc, source_content)
    else:
        print('Writing content in', target_file)
        with open(target_file, "a", encoding='utf-8') as f:
            f.write(start_autodoc + '\n')
            f.write(source_content + '\n')
            f.write(end_autodoc + '\n')


def copy_subfolder(source_dir, source_subfolder, dest_dir, dest_subfolder):
    """
    Copies a subfolder from source directory to destination directory,
    handling conflicts with prefixed filenames and folders in destination.

    Args:
      source_dir: Path to the source directory.
      source_subfolder: Name of the subfolder to copy from source directory.
      dest_dir: Path to the destination directory.
      dest_subfolder: Name of the subfolder to copy to in destination directory.
    """
    # Construct full paths for source and destination subfolders
    source_path = os.path.join(source_dir, source_subfolder)
    dest_path = os.path.join(dest_dir, dest_subfolder)

    # Check if source subfolder exists
    if not os.path.isdir(source_path):
        raise ValueError(f"Subfolder '{source_subfolder}' does not exist in source directory '{source_dir}'.")

    # Create the destination subfolder if it doesn't exist
    os.makedirs(dest_path, exist_ok=True)

    for item in os.listdir(source_path):
        source_item_path = os.path.join(source_path, item)
        # Check if item is a directory
        if os.path.isdir(source_item_path):

            existing_dest_item = item
            
            for dest_item in os.listdir(dest_path):

                compare_dest_item = dest_item
                underscore_index = compare_dest_item.find('_')

                if underscore_index != -1:
                    compare_dest_item = compare_dest_item[underscore_index + 1:]

                if compare_dest_item == item:
                    existing_dest_item = dest_item
                    break

            # Recursively call copy_subfolder for subdirectories
            copy_subfolder(source_path, item, dest_path, existing_dest_item)
        else:

            existing_dest_item = item

            existing_items = []
            for dest_item in os.listdir(dest_path):
                if dest_item.endswith(item):
                    start = dest_item.replace(item, '')
                    if not start or start[-1] == '_':
                        existing_items.append(dest_item)

            if existing_items:
                def length_diff(string):
                    return abs(len(string) - len(item[0]))
                existing_dest_item = min(existing_items, key=length_diff)

            dest_item_path = os.path.join(dest_path, existing_dest_item)

            if not os.path.exists(dest_item_path):
                # Copy the file with potentially modified name
                print(f"Copying {source_item_path} to {dest_item_path}")
                shutil.copy2(source_item_path, dest_item_path)
            else:
                print(f"Merging {source_item_path} to {dest_item_path}")
                merge_files(source_item_path, dest_item_path)


    print(f"Subfolder '{source_subfolder}' copied from '{source_dir}' to '{dest_path}'.")


def merge_docs(source_dir, dest_dir):
    if os.path.exists(source_dir):
        print(f"Merging docs from '{source_dir}' to '{dest_dir}'")
        copy_subfolder(source_dir, '', dest_dir, '')
    else:
        print(f"Source directory '{source_dir}' does not exist.")


if __name__ == "__main__":
    # Get folder paths from command line arguments (assuming 2 arguments provided)
    if len(sys.argv) != 3:
        print("Usage: python merge_docs.py <source_dir> <dest_dir>")
        exit(1)

    source_dir, dest_dir = sys.argv[1:]

    print(f"Source dir: {source_dir}")
    print(f"Dest dir: {dest_dir}")

    merge_docs(source_dir, dest_dir)
