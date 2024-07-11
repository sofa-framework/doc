# What is a Plugin?

SOFA allows to extend its feature with a plugin mechanism. A plugin is a shared library that can be loaded dynamically at run-time by SOFA. More features become available, such as new components or alternative scene loaders.

# Online plugin list

The [Online plugin list](https://www.sofa-framework.org/applications/plugins/) highlights some of the SOFA plugins. Never hesitate to request, inquire for one or to [submit your own plugin](https://www.sofa-framework.org/applications/submit/). 

# Plugin Loading

In order to use the features of a plugin, it must be loaded first. SOFA offers multiple ways to load a plugin.

## Command-line Argument

The application `runSofa` accepts an optional argument `-l,--load` to specify a list of plugins to load. A plugin can be provided as a full path, or as a name. In the latter case, the plugin library will be searched in known folders for a match.

## Automatic Loading

By default, the application `runSofa` reads the content of a configuration file to load automatically a list of plugins. This list can be edited to add the plugin you need. The file is either `plugin_list.conf` or `plugin_list.conf.default`. `plugin_list.conf.default` is generated automatically at compile-time and is not meant to be edited. To edit a list of plugins, `plugin_list.conf` must be used. If the file does not exist, it must be created based on `plugin_list.conf.default`.

## GUI: Plugin Manager

The GUI allows to load a plugin through a graphical user interface. Go to `Edit > Plugin Manager ...`. You will see the list of already loaded plugins. Click on `Add...` to load another plugin.
