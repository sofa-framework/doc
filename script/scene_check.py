"""
Append the table composed of the list of SceneCheck to a file
"""

import sys

def main():

    if len(sys.argv) < 2:
        print('Usage: scene_check.py <output_file>')
        exit(1)

    import Sofa
    import SofaRuntime

    SofaRuntime.importPlugin("SceneChecking")

    table = "| Name | Description |\n"
    table += "| ---- | ----------- |\n"
    for scene_check in Sofa.Simulation.SceneCheckMainRegistry.getRegisteredSceneChecks():
        table += f"| {scene_check.getName()} | {scene_check.getDesc()} |\n"

    with open(sys.argv[1], 'a', encoding="utf-8") as output_file:
        output_file.write(table)

if __name__ == '__main__':
    main()
