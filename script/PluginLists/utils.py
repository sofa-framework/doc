import os.path

import numpy as np
import json
import pathlib


class PresetLookup():
    presetsDict : dict
    def __init__(self, filename):
        with open(filename, 'r',encoding='utf-8-sig') as f:
            self.presetsDict = json.load(f)

    def getUsingPresetNames(self, subPresetName : str, presetList : list[str]):
        # Find presets that include it
        for preset in self.presetsDict["configurePresets"]:
            if "inherits" in  preset and subPresetName in preset["inherits"]:
                if "hidden" not in preset or not preset["hidden"]:
                    presetList.append(preset["name"])
                self.getUsingPresetNames(preset["name"],presetList)

    def getListOfPResetsContainingProject(self, projectCorrectedName: str):
        presetNames = []
        for preset in self.presetsDict["configurePresets"]:
            if "cacheVariables" in preset:
                for varName in preset["cacheVariables"].keys():
                    if projectCorrectedName in varName and preset["cacheVariables"][varName]["value"] == "ON":
                        currPresetName = preset["name"]
                        if "hidden" not in preset or not preset["hidden"]:
                            presetNames.append(currPresetName)
                        self.getUsingPresetNames(currPresetName,presetNames)
        return presetNames

class Projects():

    name : str
    type : str
    presetList = list[str]
    advancedDescription = str

    def __init__(self, name, type, advancedDescriptionFolder=""):
        self.name = name
        self.type = type
        self.presetList = []
        self.extractAdvancedDescription(advancedDescriptionFolder)

    def getCorrectedName(self):
        return self.name.upper().replace('.','_')

    def extractAdvancedDescription(self,folderPath):
        self.advancedDescription = ""
        potentialDescriptionFile = pathlib.Path(os.path.join(folderPath,self.name))
        if potentialDescriptionFile.exists():
            for line in  open(potentialDescriptionFile.absolute(), 'r').readlines():
                self.advancedDescription += line + " "


    def extractPresets(self,presets : PresetLookup):
        self.presetList = list(set(presets.getListOfPResetsContainingProject(self.getCorrectedName())))
        self.presetList = [preset for preset in self.presetList if "-dev" not in preset]
        self.presetList.sort()

    def isPluginized(self):
        return False

    def getUpperType(self):
        return self.type.upper()

    def getDisplayName(self):
        pass

    def getDescription(self):
        pass

    def getActvation(self):
        pass

    @staticmethod
    def displayFirstRow():
        return f"|Name|Description|How to activate|\n|---|---|---|\n"

    def displayDescription(self):
        return f"|{self.getDisplayName()}|{self.getDescription()}|{self.getActvation()}|"


class InternalProjects(Projects):

    def __init__(self, name, type, cmakeFolderRelativePath,advancedDescriptionFolder=""):
        Projects.__init__(self,name,type, advancedDescriptionFolder)
        self.link = "https://github.com/sofa-framework/sofa/tree/master/" + cmakeFolderRelativePath + name

    @staticmethod
    def createFromArguments(stringArg : str, cmakeFolderRelativePath, advancedDescriptionFolder=""):
        argList = stringArg.split()
        return InternalProjects(argList[1], argList[0], cmakeFolderRelativePath, advancedDescriptionFolder=advancedDescriptionFolder)

    def getDisplayName(self):
        return f"[{self.name}]({self.link})"


    def getDescription(self):
        if self.advancedDescription != "":
            return self.advancedDescription

        return f"{self.type.capitalize()} named {self.name}."

    def getActvation(self):
        activation = f"CMake flag `{self.getUpperType()}_{self.getCorrectedName()}=ON`. "
        if len(self.presetList) != 0:
            activation += f"Activated in presets {self.presetList}. "

        return activation

class ExternalProjects(Projects):

    default_tag : str
    default_repo : str

    def __init__(self, name, type, default_tag,default_repo,advancedDescriptionFolder=""):
        Projects.__init__(self,name,type,advancedDescriptionFolder)
        self.default_tag = default_tag
        self.default_repo = default_repo

    @staticmethod
    def createFromArguments(stringArg : str, advancedDescriptionFolder=""):
        argList = stringArg.split()
        tagId = argList.index("GIT_REF") + 1
        repoId = argList.index("GIT_REPOSITORY") + 1
        return ExternalProjects(argList[1], argList[0], argList[tagId], argList[repoId], advancedDescriptionFolder = advancedDescriptionFolder)

    def isPluginized(self):
        return True

    def getDisplayName(self):
        return f"[{self.name}]({self.default_repo})"

    def getDescription(self):
        if self.advancedDescription != "":
            return self.advancedDescription
        return f"External {self.type.capitalize()} named {self.name} that needs to be fetched."

    def getActvation(self):
        activation = f"CMake flags `SOFA_FETCH_{self.getCorrectedName()}=ON` and `{self.getUpperType()}_{self.getCorrectedName()}=ON`. "
        if len(self.presetList) != 0:
            activation += f"Activated in presets {self.presetList}. "

        return activation



def printTableFromProjectListToString(projectList:list[Projects]):
    output = Projects.displayFirstRow()
    for project in projectList:
        output += f"{project.displayDescription()}\n"
    return output


def sortProjectByNames(projectList: list[Projects]):
    names = [proj.name for proj in projectList]
    sortedIdx = np.argsort(names).tolist()
    return [projectList[i] for i in sortedIdx]

if __name__ == "__main__":
    lookup = PresetLookup("../../CMakePresets.json")
    outList = list(set(lookup.getListOfPResetsContainingProject("SOFA_QT")))
    print(outList)