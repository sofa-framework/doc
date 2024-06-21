# SofaDocGenerator

Generate the SOFA documentation automatically

The repository contains:

1. A SOFA application, called `SofaDocGenerator`:
2. Python script to process the documentation
3. Configuration for mkdocs

## SofaDocGenerator

SofaDocGenerator is a SOFA application. It can be built using the method described in https://www.sofa-framework.org/community/doc/plugins/build-a-plugin-from-sources/.

This plugin uses the SOFA API in order to access to the information about SOFA components, data etc.
For each component, it will generate markdown file.

### How to use

```bash
SofaDocGenerator --ouput path/to/output/folder --examples path/to/examples
```

## Python Scripts

### Merge docs

`merge_docs.py` merge the automated generated doc from SofaDocGenerator with the manually written doc from https://github.com/sofa-framework/doc

## MkDocs

MkDocs generates the website from the markdown files
