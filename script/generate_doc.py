import os
import sys
import json
from pathlib import Path
from typing import Dict, Any

from scnToPython3 import convert_xml_file_to_python


class ComponentContent:
    """Class to encapsulate the content, filepath, and description of a component."""
    def __init__(self, content: str, filepath: str, description: str) -> None:
        self.content = content
        self.filepath = filepath
        self.description = description

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ComponentContent):
            return (self.content == other.content and
                    self.filepath == other.filepath and
                    self.description == other.description)
        return False

    def __hash__(self) -> int:
        return hash((self.content, self.filepath, self.description))

    def __str__(self):
        return f"{self.content}\n{self.filepath}\n{self.description}"

    def __repr__(self):
        return f"\n{self.content}\n\n{self.filepath}\n{self.description[:8]}..."


def add_to_content_map(content_map: Dict[str, Dict[str, ComponentContent]],
                       component_name: str, template_name: str, content: ComponentContent) -> None:
    """Add content to the content map for a specific component and template."""
    if component_name not in content_map:
        content_map[component_name] = {}
    content_map[component_name][template_name] = content


def ensure_file_path_exists(filepath: str) -> None:
    """Ensure the file and its parent directories exist."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)


def merge_content_entries(content_map: Dict[str, Dict[str, ComponentContent]]) -> Dict[str, Dict[str, ComponentContent]]:
    """Merge content map entries with the same content under different templates."""
    merged_content_map = {}

    for component_name, templates in content_map.items():
        seen_contents = {}
        for template_name, content in templates.items():
            if content not in seen_contents:
                seen_contents[content] = []
            seen_contents[content].append(template_name)

        merged_templates = {}
        for content, template_names in seen_contents.items():
            merged_templates["\n- ".join(template_names)] = content

        merged_content_map[component_name] = merged_templates

    return merged_content_map


data_table_header = """<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Default value</th>
        </tr>
    </thead>
    <tbody>\n"""

link_table_header = """
| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
"""

def extract_data_list_to_content(content, creator):
    content += "### Data\n\n"
    content += data_table_header
    group_data = dict()
    for data in creator['object']['data']:
        if data['group'] not in group_data:
            group_data[data['group']] = []
        group_data[data['group']].append(data)
    for group_name, data_list in group_data.items():
        if len(group_name) > 0:
            content += "\t<tr>\n"
            content += "\t\t<td colspan=\"3\">" + group_name + "</td>\n"
            content += "\t</tr>\n"
        for data in data_list:
            content += "\t<tr>\n"
            content += f"\t\t<td>{data['name']}</td>\n"
            data_description = data['help']
            data_description.replace('<', '&lt;')
            data_description.replace('>', '&gt;')
            content += f"\t\t<td>\n{data_description}\n\t\t</td>\n"
            content += f"\t\t<td>{data['defaultValue']}</td>\n"
            content += "\t</tr>\n"
    content += "\n</tbody>\n</table>\n\n"
    return content


def extract_link_list_to_content(content, creator):
    content += "### Links\n\n"
    content += link_table_header

    for link in creator['object']['link']:
        destination_type_name = link['destinationTypeName']
        destination_type_name = destination_type_name.replace('<', '&lt;')
        destination_type_name = destination_type_name.replace('>', '&gt;')
        content += f"|{link['name']}|{link['help']}|{destination_type_name}|\n"
    content += "\n"
    return content


def process_component(component: Dict[str, Any], destination_directory: str, content_map: Dict[str, Dict[str, ComponentContent]]) -> None:
    """Process a single component and add its content to the content map."""
    component_name = component['className']

    for template_name, creator in component['creator'].items():
        target = creator['target']
        target_path = target.replace('.', os.path.sep)
        filename = f"{component_name}.md"
        filepath = os.path.join(destination_directory, target_path, filename)

        if os.path.exists(filepath):
            os.remove(filepath)

        content = f"__Target__: {target}\n\n"
        content += f"__namespace__: {creator['class']['namespaceName']}\n\n"

        if creator['class']['parents']:
            parent_classes = "\n".join(f"- {parent.split('<')[0]}" for parent in creator['class']['parents'])
            content += f"__parents__:\n\n{parent_classes}\n\n"

        content = extract_data_list_to_content(content, creator)
        content = extract_link_list_to_content(content, creator)


        description = component['description']
        component_content = ComponentContent(content, filepath, description)
        add_to_content_map(content_map, component_name, template_name, component_content)


def write_merged_content(merged_content_map: Dict[str, Dict[str, ComponentContent]]) -> None:
    """Write the merged content to their respective files."""
    for component_name, templates in merged_content_map.items():
        for template_names, content_info in templates.items():
            if os.path.exists(content_info.filepath):
                with open(content_info.filepath, "a", encoding="utf-8") as file:
                    file.write(f'<!-- generate_doc -->\n')
                    if len(template_names) > 0:
                        template_list = template_names.split('\n- ')
                        if len(template_list) > 1:
                            file.write(f'## {template_list[0]}...\n\n')
                        else:
                            file.write(f'## {template_names}\n\n')
                        file.write(f'Templates:\n\n- {template_names}\n\n')
                    file.write(content_info.content)
            else:
                ensure_file_path_exists(content_info.filepath)
                with open(content_info.filepath, "w", encoding="utf-8") as file:
                    file.write(f'<!-- generate_doc -->\n')
                    file.write(f"# {component_name}\n\n")
                    file.write(f"{content_info.description}\n\n")
                    if len(template_names) > 0:
                        template_list = template_names.split('\n- ')
                        if len(template_list) == 1:
                            file.write(f'## {template_names}\n\n')
                        file.write(f'Templates:\n\n- {template_names}\n\n')
                    file.write(content_info.content)


def read_file_to_string(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        indented_lines = ['    ' + line for line in lines]  # Add 4 spaces to each line
        content = ''.join(indented_lines)
    return content


def generate_component_documentation(destination_directory, example_directories) -> None:
    """Main function to process the components and write content to files."""

    print("Importing Sofa module...")
    import Sofa

    print("Importing SofaRuntime module...")
    import SofaRuntime

    print("Importing SOFA plugins...")
    SofaRuntime.importPlugin("Sofa.Component")
    SofaRuntime.importPlugin("Sofa.GL.Component")
    SofaRuntime.importPlugin("Sofa.GUI.Component")
    SofaRuntime.importPlugin("MultiThreading")
    SofaRuntime.importPlugin("Sofa.Metis")
    SofaRuntime.importPlugin("CollisionOBBCapsule")
    SofaRuntime.importPlugin("CImgPlugin")
    SofaRuntime.importPlugin("ArticulatedSystemPlugin")
    SofaRuntime.importPlugin("SofaEulerianFluid")
    SofaRuntime.importPlugin("SofaSphFluid")
    SofaRuntime.importPlugin("SofaDistanceGrid")
    SofaRuntime.importPlugin("SofaImplicitField")
    SofaRuntime.importPlugin("DiffusionSolver")
    # SofaRuntime.importPlugin("image")
    # SofaRuntime.importPlugin("image_gui")
    SofaRuntime.importPlugin("CGALPlugin")
    SofaRuntime.importPlugin("Registration")
    SofaRuntime.importPlugin("InvertibleFVM")
    SofaRuntime.importPlugin("PluginExample")
    SofaRuntime.importPlugin("ManifoldTopologies")
    SofaRuntime.importPlugin("SensableEmulation")
    SofaRuntime.importPlugin("SofaCarving")
    SofaRuntime.importPlugin("Geomagic")
    SofaRuntime.importPlugin("SofaMatrix")
    SofaRuntime.importPlugin("BeamAdapter")
    SofaRuntime.importPlugin("STLIB")
    SofaRuntime.importPlugin("SoftRobots")
    SofaRuntime.importPlugin("ShapeMatchingPlugin")
    SofaRuntime.importPlugin("CSparseSolvers")
    # SofaRuntime.importPlugin("ModelOrderReduction")
    SofaRuntime.importPlugin("VolumetricRendering")
    # if "auto_load_plugins" in dir(SofaRuntime):
    #     SofaRuntime.auto_load_plugins()
    # else:
    #     print("Cannot auto-load plugins")

    print("Dumping ObjectFactory in json...")
    object_factory_data = Sofa.Core.ObjectFactory.dump_json()
    print("Loading json string...")
    object_factory = json.loads(object_factory_data)

    content_map = {}

    for component in object_factory:
        print(f"Processing component {component['className']}")
        process_component(component, destination_directory, content_map)

    print("Merging component contents...")
    merged_content_map = merge_content_entries(content_map)
    print("Writing files...")
    write_merged_content(merged_content_map)

    print("Writing examples...")
    write_examples(destination_directory, example_directories, object_factory)


def write_examples(destination_directory, example_directories, object_factory):
    for component in object_factory:
        component_name = component['className']
        file_paths = []
        for template_name, creator in component['creator'].items():
            target = creator['target']
            target_path = target.replace('.', os.path.sep)
            filename = f"{component_name}.md"
            filepath = os.path.join(destination_directory, target_path, filename)
            if os.path.exists(filepath):
                if os.path.isfile(filepath):
                    if filepath not in file_paths:
                        file_paths.append(filepath)

        component_examples = []
        for example_dir in example_directories:
            for root, dirs, files in os.walk(example_dir):
                for file in files:
                    if file.startswith(component_name) and file.endswith(('.xml', '.scn')):
                        try:
                            xml_string = read_file_to_string(os.path.join(root, file))
                            python_string = convert_xml_file_to_python(os.path.join(root, file), '    ')
                            component_examples.append((xml_string, python_string, file))
                        except Exception as e:
                            print(e, os.path.join(root, file))

        if component_examples:
            for filepath in file_paths:
                with open(filepath, "a", encoding="utf-8") as file:
                    file.write("## Examples \n\n")
                    for xml, python, source_file in component_examples:
                        file.write(f"{source_file}\n\n")
                        file.write("=== \"XML\"\n\n")
                        file.write('    ```xml\n')
                        try:
                            file.write(xml + '\n')
                        except Exception as e:
                            print(e, component_examples)
                        file.write('    ```\n\n')

                        file.write("=== \"Python\"\n\n")
                        file.write('    ```python\n')
                        file.write(python + '\n')
                        file.write('    ```\n\n')


if __name__ == "__main__":
    default_dest_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "markdown")
    destination_directory = sys.argv[1] if len(sys.argv) >= 2 else default_dest_dir

    example_directories = sys.argv[2:] if len(sys.argv) > 2 else []

    generate_component_documentation(destination_directory, example_directories)
