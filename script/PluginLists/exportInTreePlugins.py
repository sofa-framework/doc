from utils import *
import os
import sys

SOFA_SRC=sys.argv[1]

## Find all meaningful CMakeLists in applications
## This automated search is looking first in the CMakeLists at the root of {SOFA_SRC}/applications/ and for each 'add_subdirectory' it finds, it look inside of it the same way in a recursive way.
## An easier way would have been to look for all CMakeLists in applications, but this might be wrong because som in tree plugins might also use the macros.
def recFindCMakeLists(currFilename, fileList):
    currfolder = currFilename.removesuffix('CMakeLists.txt')
    with open(currFilename) as file:
        for line in [line.rstrip() for line in file]:
            if("add_subdirectory" in line and not "sofa_add_subdirectory" in line):
                folderName = line.split('(')[1].split(')')[0].split()[0]
                foundFile = os.path.join(currfolder,folderName,'CMakeLists.txt')
                fileList.append(foundFile)
                recFindCMakeLists(foundFile, fileList)

filenames=[f"{SOFA_SRC}/applications/CMakeLists.txt"]
recFindCMakeLists(filenames[0],filenames)

presetFilename=f"{SOFA_SRC}/CMakePresets.json"
descriptionFolder=f"{SOFA_SRC}/scripts/subProjectLister/AdvancedDescriptions/"

possibleTypes=["application","folder","plugin"]

applications = []
folders = []
plugins = []

presetLookup = PresetLookup(presetFilename)

def saveProject(proj:Projects):
    global applications, folders, plugins
    match proj.type:
        case "application":
            applications.append(proj)
        case "directory":
            folders.append(proj)
        case "plugin":
            plugins.append(proj)


## Extract all subprojects
lines = []
for filename in filenames:
    cmakeFolderRelativePath = filename.removeprefix(f"{SOFA_SRC}/").removesuffix("CMakeLists.txt")
    with open(filename) as file:
        ## Transform into Projects type and sort them regarding type
        for line in [line.rstrip() for line in file]:
            if("sofa_add_subdirectory" in line):
                arguments = line.split('(')[1].split(')')[0]
                proj = InternalProjects.createFromArguments(arguments, cmakeFolderRelativePath, descriptionFolder)
                proj.extractPresets(presetLookup)
                saveProject(proj)
            elif("sofa_add_external" in line):
                arguments = line.split('(')[1].split(')')[0]
                proj = ExternalProjects.createFromArguments(arguments,descriptionFolder)
                proj.extractPresets(presetLookup)

                saveProject(proj)



## Sort list regarding the name of the project
applications = sortProjectByNames(applications)
plugins = sortProjectByNames(plugins)
folders = sortProjectByNames(folders)

## Print markdown tables



print("### Applications")
print()
print(printTableFromProjectListToString(applications))
print()

print("### Plugins")
print()
print(printTableFromProjectListToString(plugins))
print()

print("### Directories")
print()
print(printTableFromProjectListToString(folders))
print()
