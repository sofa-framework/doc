import shutil
import sys
import os
import git  # pip install gitpython
import requests  # pip install requests

from merge_docs import merge_docs
from generate_doc import generate_component_documentation


def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    # Is the error an access error?
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise


def download_guidelines_file(cloned_doc_folder):
    url = 'https://raw.githubusercontent.com/sofa-framework/sofa/master/GUIDELINES.md'
    response = requests.get(url)
    guidelines_filepath = os.path.join(cloned_doc_folder, "40_Programming_with_SOFA", "01_Guidelines.md")
    if response.status_code == 200:
        with open(guidelines_filepath, 'wb') as file:
            file.write(response.content)
        print(f'File {guidelines_filepath} downloaded successfully.')
    else:
        print(f'Failed to download file. Status code: {response.status_code}')


def download_contributing_file(cloned_doc_folder):
    url = 'https://raw.githubusercontent.com/sofa-framework/sofa/master/CONTRIBUTING.md'
    response = requests.get(url)
    contributing_filepath = os.path.join(cloned_doc_folder, "50_Contributing_to_SOFA", "01_Contributing.md")
    if response.status_code == 200:
        with open(contributing_filepath, 'wb') as file:
            file.write(response.content)
        print(f'File {contributing_filepath} downloaded successfully.')
    else:
        print(f'Failed to download file. Status code: {response.status_code}')


def download_SofaGLFW_file(cloned_doc_folder):
    url = 'https://raw.githubusercontent.com/sofa-framework/SofaGLFW/master/README.md'
    response = requests.get(url)
    sofaglfw_filepath = os.path.join(cloned_doc_folder, "15_Using_SOFA", "11_runSofa_with_ImGui.md")
    if response.status_code == 200:
        with open(sofaglfw_filepath, 'wb') as file:
            file.write(response.content)
        print(f'File {sofaglfw_filepath} downloaded successfully.')
    else:
        print(f'Failed to download file. Status code: {response.status_code}')


if __name__ == "__main__":
    tmp_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tmp")

    default_dest_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mkdocs", "docs")
    destination_directory = sys.argv[1] if len(sys.argv) >= 2 else default_dest_dir

    example_directories = sys.argv[2:] if len(sys.argv) > 2 else []

    cloned_doc_folder = os.path.join(tmp_folder, "cloned_doc")
    if not os.path.exists(cloned_doc_folder):
        print("Cloning the doc...")
        repo = git.Repo.clone_from('https://github.com/sofa-framework/doc.git',
                                   cloned_doc_folder,
                                   branch='master')
        print("Finished to clone the doc...")

    # Download and include pages as doc pages : GUIDELINES.md, CONTRIBUTING.md, README.md
    download_guidelines_file(cloned_doc_folder)
    download_contributing_file(cloned_doc_folder)
    download_SofaGLFW_file(cloned_doc_folder)

    auto_doc_folder = os.path.join(tmp_folder, "auto_doc")
    print("Generate the doc...")
    generate_component_documentation(auto_doc_folder, example_directories)

    merged_doc_folder = os.path.join(tmp_folder, "merged_doc")
    if os.path.exists(merged_doc_folder):
        print(f"Removing folder ${merged_doc_folder}...")
        shutil.rmtree(merged_doc_folder)
    print(f"Copying folder ${cloned_doc_folder} into ${merged_doc_folder}...")
    shutil.copytree(cloned_doc_folder, merged_doc_folder, ignore=shutil.ignore_patterns(".git"))

    merge_docs(os.path.join(auto_doc_folder, "Sofa", "Component"),
               os.path.join(merged_doc_folder, "30_Components"))

    merge_docs(os.path.join(auto_doc_folder, "Sofa", "GL", "Component"),
               os.path.join(merged_doc_folder, "30_Components"))

    merge_docs(os.path.join(auto_doc_folder, "Sofa", "GUI", "Component"),
               os.path.join(merged_doc_folder, "30_Components", "GUI"))

    # Merge the doc from plugins: 1) copy everything (including SOFA), 2) remove SOFA
    merge_docs(auto_doc_folder,
               os.path.join(merged_doc_folder, "35_Plugins", "50_Usual_plugins"))
    shutil.rmtree(os.path.join(merged_doc_folder, "35_Plugins", "50_Usual_plugins", "Sofa"))

    print(f"Copying from {merged_doc_folder} to {destination_directory}...")
    shutil.copytree(merged_doc_folder, destination_directory, dirs_exist_ok=True)
    shutil.rmtree(tmp_folder, onerror=onerror)
    
