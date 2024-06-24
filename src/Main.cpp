
#include <cxxopts.hpp>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <mutex>
#include <thread>
#include <sofa/core/ComponentLibrary.h>

#include <sofa/helper/logging/Messaging.h>
#include <sofa/helper/system/FileSystem.h>

#include <sofa/simulation/config.h>
#include <sofa/simulation/Node.h>

#include <sofa/helper/logging/LoggingMessageHandler.h>

#include <sofa/core/ObjectFactory.h>
#include <sofa/helper/BackTrace.h>
#include <sofa/helper/system/FileRepository.h>
#include <sofa/helper/system/PluginManager.h>
#include <sofa/simulation/common/SceneLoaderXML.h>
#include <sofa/simulation/graph/DAGNode.h>
#include <sofa/simulation/graph/init.h>

#include "XMLtoPython.h"

struct FileContent
{
    std::string componentName;
    std::string directory;
    std::string content;
    std::map<std::string, std::string> templateContentMap;
};

void loadPlugins(const char* const appName, const std::vector<std::string>& pluginsToLoad);

void generateDoc(std::string outputDirectory, bool skipEmptyModuleName, const std::vector<std::string>& examplesDirectories);

void find_files_by_prefix(
    const std::string& directory, const std::string& prefix, const std::string& root,
    std::vector<std::string>& outAbsoluteFiles, std::vector<std::string>& outRelativeFiles)
{
    namespace fs = std::filesystem;

    for (const auto& entry : fs::directory_iterator(directory))
    {
        if (entry.is_regular_file() &&
            entry.path().filename().string().find(prefix) == 0)
        {
            outRelativeFiles.push_back(fs::relative(entry, fs::path(root)).string());
            outAbsoluteFiles.push_back(entry.path().string());
        }
        else if (entry.is_directory() && !fs::is_symlink(entry))
        {
            find_files_by_prefix(
                entry.path().string(), prefix, root, outAbsoluteFiles, outRelativeFiles);
        }
    }
}


int main(int argc, char** argv)
{
    constexpr const char* appName = "SofaDocGenerator";
    cxxopts::Options options(appName, "Generate SOFA documentation based on the ObjectFactory");
    options.add_options()
        ("verbose", "Verbose")
        ("h,help", "print usage")
        ("skip_empty_module_name", "skip doc generation for components with empty module name")
        ("l,load", "load given plugins", cxxopts::value<std::vector<std::string>>())
        ("o,output", "Documentation is generated in this directory [REQUIRED]", cxxopts::value<std::string>())
        ("examples", "Example files", cxxopts::value<std::vector<std::string>>())
    ;

    const auto result = options.parse(argc, argv);

    if (result.count("help") || result.count("output") == 0)
    {
        std::cout << options.help() << std::endl;
        exit(0);
    }

    sofa::helper::logging::MessageDispatcher::addHandler(&sofa::helper::logging::MainLoggingMessageHandler::getInstance());
    sofa::helper::logging::MainLoggingMessageHandler::getInstance().activate();

    sofa::helper::BackTrace::autodump();
    sofa::simulation::graph::init();

    std::vector<std::string> pluginsToLoad;
    if (result.count("load"))
    {
        pluginsToLoad = result["load"].as<std::vector<std::string>>();
    }
    loadPlugins(appName, pluginsToLoad);

    std::map<std::string, std::string > aliases; //key: alias, value: original name
    sofa::core::ObjectFactory::getInstance()->setCallback([&aliases](sofa::core::Base* o, sofa::core::objectmodel::BaseObjectDescription *arg)
    {
        const std::string typeNameInScene = arg->getAttribute("type", "");
        if ( typeNameInScene != o->getClassName() )
        {
            aliases[typeNameInScene] = o->getClassName();
        }
    });

    const auto verbose = result["verbose"].as<bool>();
    const auto skipEmptyModuleName = result["skip_empty_module_name"].as<bool>();

    msg_info_when(skipEmptyModuleName, appName) << "Components with empty module name will be skipped";

    std::vector<std::string> examplesDirectories;
    if (result.count("examples"))
    {
        examplesDirectories = result["examples"].as<std::vector<std::string>>();
    }

    generateDoc(result["output"].as<std::string>(), skipEmptyModuleName, examplesDirectories);

    sofa::simulation::graph::cleanup();
    return 0;
}

void loadPlugins(const char* const appName, const std::vector<std::string>& pluginsToLoad)
{
    for (const auto& plugin : pluginsToLoad)
    {
        sofa::helper::system::PluginManager::getInstance().loadPlugin(plugin);
    }

    std::string configPluginPath = "plugin_list.conf";
    std::string defaultConfigPluginPath = "plugin_list.conf.default";
    if (sofa::helper::system::PluginRepository.findFile(configPluginPath, "", nullptr))
    {
        msg_info(appName) << "Loading automatically plugin list in " << configPluginPath;
        sofa::helper::system::PluginManager::getInstance().readFromIniFile(configPluginPath);
    }
    if (sofa::helper::system::PluginRepository.findFile(defaultConfigPluginPath, "", nullptr))
    {
        msg_info(appName) << "Loading automatically plugin list in " << defaultConfigPluginPath;
        sofa::helper::system::PluginManager::getInstance().readFromIniFile(defaultConfigPluginPath);
    }

    msg_info(appName) << "plugins loaded";
}

void extractComponentLinks(std::string& templateContent, const sofa::core::objectmodel::BaseObject::SPtr object)
{
    const auto& links = object->getLinks();
    if (links.empty())
    {
        return;
    }

    templateContent += "Links: \n\n";

    templateContent += "| Name | Description |\n";
    templateContent += "| ---- | ----------- |\n";

    for (const auto& link : object->getLinks())
    {
        templateContent += "|" + link->getName() + "|" + link->getHelp() + "|\n";
    }
    templateContent += "\n\n";
}

void extractComponentData(std::string& templateContent, const sofa::core::objectmodel::BaseObject::SPtr object)
{
    templateContent += "Data: \n\n";

    templateContent += R"(<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Default value</th>
    </tr>
</thead>
<tbody>
)";

    std::map<std::string, std::vector<sofa::core::BaseData*> > dataGroups;
    for (const auto& data : object->getDataFields())
    {
        if (data)
        {
            dataGroups[data->group].push_back(data);
        }
    }
    for (const auto& [group, dataList] : dataGroups)
    {
        if (!group.empty())
        {
            templateContent += "\t<tr>\n";
            templateContent += "\t\t<td colspan=\"3\">" + group + "</td>\n";
            templateContent += "\t</tr>\n";
        }
        for (const auto& data : dataList)
        {
            templateContent += "\t<tr>\n";
            templateContent += "\t\t<td>" + data->getName() + "</td>\n";
            auto help = data->getHelp();
            sofa::helper::replaceAll(help, "<", "&lt;");
            sofa::helper::replaceAll(help, ">", "&gt;");
            templateContent += "\t\t<td>\n" + help + "\n</td>\n";
            templateContent += "\t\t<td>" + data->getDefaultValueString() + "</td>\n";
            templateContent += "\t</tr>\n";
        }
    }
    templateContent += "\n</tbody>\n</table>\n\n";
}

void generateComponentDoc(
    const std::string& outputDirectory,
    std::map<std::string, FileContent>& fileContent,
    const sofa::core::ClassEntry::SPtr& entry,
    sofa::core::ObjectFactory::Creator::SPtr creator,
    std::string templateName,
    std::mutex& mutex)
{
    auto targetDirectory = std::string{creator->getTarget()};

    // replace . by /
    std::replace( targetDirectory.begin(), targetDirectory.end(), '.', '/');

    std::string directory = sofa::helper::system::FileSystem::append(outputDirectory, targetDirectory);
    directory = sofa::helper::system::FileSystem::convertBackSlashesToSlashes(directory);

    const std::string filename = sofa::helper::system::FileSystem::append(directory, entry->className + ".md");

    auto it = fileContent.find(filename);
    if (it == fileContent.end())
    {
        FileContent content;
        content.componentName = entry->className;
        content.content = "# " + entry->className + "\n\n";

        content.content += entry->description + "\n\n";

        content.directory = directory;
        std::lock_guard guard(mutex);
        it = fileContent.insert({filename, content}).first;
    }

    auto& templateContent = it->second.templateContentMap[templateName];

    templateContent += "__Target__: `" + std::string{creator->getTarget()} + "`\n\n";
    templateContent += "__namespace__: `#!c++ " + creator->getClass()->namespaceName + "`\n\n";
    // templateContent += "__file__: " + std::string{creator->getHeaderFileLocation()} + "\n\n";
    if (!creator->getClass()->parents.empty())
    {
        templateContent += "__parents__: \n\n";

        for (const auto& parent : creator->getClass()->parents)
        {
            templateContent += "- `#!c++ " + parent->className + "`\n";
        }
        templateContent += "\n";
    }

    const auto tmpNode = sofa::core::objectmodel::New<sofa::simulation::graph::DAGNode>("tmp");
    if (tmpNode)
    {
        sofa::core::objectmodel::BaseObjectDescription desc;
        const auto object = creator->createInstance(tmpNode.get(), &desc);
        if (object)
        {
            extractComponentData(templateContent, object);
            extractComponentLinks(templateContent, object);
        }
    }
}

void generateDoc(std::string outputDirectory, bool skipEmptyModuleName, const std::vector<std::string>& examplesDirectories)
{
    outputDirectory = sofa::helper::system::FileSystem::convertBackSlashesToSlashes(outputDirectory);
    std::cout << "output directory: " << outputDirectory << std::endl;

    static std::vector<sofa::core::ClassEntry::SPtr> entries;
    sofa::core::ObjectFactory::getInstance()->getAllEntries(entries);

    std::map<std::string, FileContent> fileContent;

    static const std::vector<std::string> skippedComponents {
        "CapsuleCollisionModel",
        "MORUnilateralInteractionConstraint"
    };

    const bool isCudaLoaded = sofa::helper::system::PluginManager::getInstance().pluginIsLoaded("SofaCUDA");
    const auto isCudaTemplate = [](std::string t)
    {
        return t == "CudaRigid3d" || t == "CudaRigid3f" ||
            t == "CudaRigid2d" || t == "CudaRigid2f" ||
            t == "CudaVec3d" || t == "CudaVec3d1" || t == "CudaVec3f" || t == "CudaVec3f1" ||
            t == "CudaVec2d" || t == "CudaVec2f" ||
            t == "CudaVec1d" || t == "CudaVec1f" ||
            t == "CudaVec6d" || t == "CudaVec6f";
    };

    std::mutex mutex;
    for (const auto& entry : entries)
    {
        if (std::find(skippedComponents.begin(), skippedComponents.end(), entry->className) == skippedComponents.end()) //skip because these components are buggy
        {
            std::cout << entry->className << std::endl;

            sofa::core::ObjectFactory::CreatorMap filteredCreatorMap;
            for (const auto& [templateInstance, creator] : entry->creatorMap)
            {
                const auto moduleName = std::string{creator->getTarget()};
                if (moduleName.empty() && skipEmptyModuleName)
                {
                    continue;
                }

                const bool isCudaT = isCudaTemplate(creator->getClass()->templateName);
                if (isCudaT && isCudaLoaded || !isCudaT)
                {
                    filteredCreatorMap.insert({templateInstance, creator});
                }

            }

            for (const auto& [templateInstance, creator] : filteredCreatorMap)
            {
                generateComponentDoc(outputDirectory, fileContent, entry, creator, creator->getClass()->templateName, mutex);
            }
        }
    }

    for (const auto& [filename, content] : fileContent)
    {
        std::cout << "Writing " << filename << std::endl;
        sofa::helper::system::FileSystem::findOrCreateAValidPath(content.directory);
        std::ofstream f(filename);
        f << content.content;

        std::map<std::string, std::set<std::string> > fusedTemplates;

        for (const auto& [templateName, templateContent] : content.templateContentMap)
        {
            fusedTemplates[templateContent].insert(templateName);
        }

        for (const auto& [templateContent, templateNames] : fusedTemplates)
        {
            if (!templateNames.empty() && std::all_of(templateNames.begin(), templateNames.end(), [](const std::string& templateName){return !templateName.empty();}))
            {
                f << "__Templates__:\n\n";
                for (const auto& templateName : templateNames)
                {
                    f << "- `#!c++ " << templateName << "`\n";
                }
                f << '\n';
            }
            f << templateContent << '\n';
        }

        std::stringstream ss;
        for (const auto& dir : examplesDirectories)
        {
            if (!sofa::helper::system::FileSystem::exists(dir))
            {
                continue;
            }

            std::vector<std::string> absoluteFiles, relativeFiles;
            find_files_by_prefix(dir, content.componentName, dir, absoluteFiles, relativeFiles);

            sofa::simulation::SceneLoader::ExtensionList extensions;
            sofa::simulation::SceneLoaderXML xmlloader;
            xmlloader.getExtensionList(&extensions);

            std::vector<std::string> filteredAbsoluteFiles, filteredRelativeFiles;

            for (std::size_t i = 0; i < absoluteFiles.size(); ++i)
            {
                const auto& absoluteFile = absoluteFiles[i];
                const auto& relativeFile = relativeFiles[i];

                const auto extension = sofa::helper::system::FileSystem::getExtension(absoluteFile);
                if (std::find(extensions.begin(), extensions.end(), extension) != extensions.end())
                {
                    filteredAbsoluteFiles.push_back(absoluteFile);
                    filteredRelativeFiles.push_back(relativeFile);
                }
            }

            if (!filteredAbsoluteFiles.empty())
            {
                for (std::size_t i = 0; i < filteredAbsoluteFiles.size(); ++i)
                {
                    const auto& absoluteFile = filteredAbsoluteFiles[i];
                    const auto& relativeFile = filteredRelativeFiles[i];

                    ss << relativeFile << "\n\n";
                    {
                        ss << "=== \"XML\"\n\n";
                        ss << "    ```xml\n";
                        std::string line;
                        std::ifstream exFile(absoluteFile);
                        while (std::getline (exFile, line))
                        {
                            ss << "    " << line << "\n";
                        }
                        ss << "    ```\n\n";
                    }

                    {
                        std::string pythonString;
                        convertXMLToPython(absoluteFile, pythonString);

                        ss << "=== \"Python\"\n\n";
                        ss << "    ```python\n";
                        ss << pythonString;
                        ss << "    ```\n\n";
                    }
                }
            }
        }

        if (!ss.str().empty())
        {
            f << "## Examples\n\n";
            f << ss.str();
        }
    }

}
