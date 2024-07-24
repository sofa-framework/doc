import os.path
import sys

from utils import get_root


def add_redirection_in_file(mkdocs_file):
    with open(mkdocs_file, "a") as file:
        redirect_content = ""

        file.write(redirect_content)


if __name__ == "__main__":

    mkdocs_file = ""
    if len(sys.argv) >= 2:
        mkdocs_file = sys.argv[1]
    else:
        root = get_root()
        print("ROOT:", root)

        mkdocs_file = os.path.join(root, "mkdocs", "mkdocs.yml")

    if not os.path.exists(mkdocs_file):
        print("file", mkdocs_file, "not found")
        sys.exit(1)

    print("mkdocs file:", mkdocs_file)
    add_redirection_in_file(mkdocs_file)
