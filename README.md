# SofaDocGenerator

Generate the SOFA documentation automatically

The repository contains:

1. A SOFA application, called `SofaDocGenerator`:
2. Python scripts to process the documentation
3. Configuration for mkdocs

## SofaDocGenerator

SofaDocGenerator is a SOFA application. It can be built using the method described in https://www.sofa-framework.org/community/doc/plugins/build-a-plugin-from-sources/.

This plugin uses the SOFA API in order to access to the information about SOFA components, data etc.
For each component, it will generate a markdown file containing its description, the available templates (if any), the list of Data and Links, and examples.

### How to use

```bash
SofaDocGenerator --ouput path/to/output/folder --examples path/to/examples
```

## Python Scripts

### Merge docs

`merge_docs.py` merge the automated generated doc from SofaDocGenerator with the manually written doc from https://github.com/sofa-framework/doc

`title_metadata.py`  recursively processes files in a specified directory, adding metadata to files whose names start with one or more digits followed by an underscore.
The metadata includes a title extracted from the filename and added as a YAML header.

`generate_nav.py` visits all the files of a directory and generates a table of content for mkdocs, in the configuration
file `mkdocs.yml`.

## MkDocs

MkDocs generates the website from the markdown files.

It requires the installation of packages:

```
pip install mkdocs mkdocs-material
```

# Run Locally

## Simplest pipeline

This pipeline only generates a documentation website from the automatically generated documentation.

```bash
SofaDocGenerator --ouput path/to/mkdocs/docs --examples path/to/examples
cd path/to/mkdocs
mkdocs serve
```

`path/to/mkdocs` is the folder containing `mkdocs.yml`.
