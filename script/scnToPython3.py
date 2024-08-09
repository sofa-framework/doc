#!/usr/bin/python

import xml.etree.ElementTree as ET
import sys
import os
from re import sub

root_node_name = 'root_node'


def change_file_extension(path, new_extension):
    """
    Changes the file extension of the given file path to the new extension.
    """
    # Split the path into root and extension
    root, _ = os.path.splitext(path)
    # Concatenate the root with the new extension
    new_path = root + new_extension
    return new_path


# Define a function to convert a string to snake case
def snake_case(s):
    # Replace hyphens with spaces, then apply regular expression substitutions for title case conversion
    # and add an underscore between words, finally convert the result to lowercase
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
                s.replace('-', ' '))).split()).lower()


def replace_multiple_newlines(text):
    # Replace sequences of more than 2 newlines with exactly 2 newlines
    return sub(r'\n{3,}', '\n\n', text)


def convert_xml_to_python(xml_string, line_prefix='', indent='   '):
    def process_node(node, parent_variable_name):

        if parent_variable_name is None:
            parent_variable_name = root_node_name

        python_code = ""
        node_variable_name = node.attrib.get('name', 'node')
        cleaned_node_variable_name = snake_case(node_variable_name.replace('.', '_').replace('-', '_').replace(' ', '_'))

        python_code += (f"\n{line_prefix}{indent}{cleaned_node_variable_name} = "
                        f"{parent_variable_name}.addChild('{node_variable_name}'")

        node_attributes = ", ".join(f'{key}="{value}"' for key, value in node.attrib.items() if key != 'name')
        if node_attributes:
            python_code += f", {node_attributes}"
        python_code += ")\n\n"

        parent_variable_name = cleaned_node_variable_name

        for child in node:
            if child.tag == 'Node':
                python_code += process_node(child, node_variable_name) + "\n"
            else:
                object_attributes = ", ".join(f'{key}="{value}"' for key, value in child.attrib.items())
                python_code += f"{line_prefix}{indent}{parent_variable_name}.addObject('{child.tag}', {object_attributes})\n"

        return python_code

    parser = ET.XMLParser(encoding="utf-8")
    root = ET.fromstring(xml_string, parser=parser)
    converted_python_code = process_node(root, None)
    converted_python_code = replace_multiple_newlines(converted_python_code)
    converted_python_code = f"{line_prefix}def createScene({root_node_name}):\n" + converted_python_code
    return converted_python_code.rstrip()


def convert_xml_file_to_python(xml_file, line_prefix='', indent='   '):
    with open(xml_file, 'r', encoding="utf-8") as input_file:
        xml_string = input_file.read().encode('utf-8')
        python_code = convert_xml_to_python(xml_string, line_prefix, indent)
        return python_code


def main():

    if len(sys.argv) < 2:
        print('Usage: scnToPython3.py <input_xml_file>')
        exit(1)
    input_xml_file = sys.argv[1]
    print(f"Converting {input_xml_file}")

    output_python_code = convert_xml_file_to_python(input_xml_file)

    if output_python_code:
        output_python_file = change_file_extension(input_xml_file, '.py')
        print(f"Writing {output_python_file}")
        with open(output_python_file, 'w', encoding="utf-8") as output_file:
            output_file.write(output_python_code)


if __name__ == '__main__':
    main()
