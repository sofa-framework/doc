SOFA Documentation
==================

This documentation contains all informations about SOFA, from historical presentation to developper instructions.  
It is automatically rendered in SOFA website: https://www.sofa-framework.org/doc


## Content ##
- **Getting Started**: instructions about building and installing SOFA.
- **Main Principles**: everything you need to know about what is SOFA and how it works.
- **Video Tutorials**: list videos helping new users starting with SOFA.
- **Using SOFA**: how to use SOFA to build and run simulation scenes (user documentation).
- **Programming with SOFA**: how to write your own code and then contribute it to SOFA (developper documentation).


## Contribution ##
Everyone is very welcome to contribute to this documentation. Here are some information you have to read.  
Files are written in Markdown. If you don't understand the syntax, you can refer to [this usefull cheatsheet] (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

### Hierarchy ###
Files are parsed in alphabetical order to generate the online documentation. To change some file/folder order in the hierarchy, you can simply edit its number.
- 10_Folder_A
  - 10_File_AA.md
  - 20_File_AB.md
  - 30_File_AC.md
- 20_Folder_B
  - 21_File_BA.md

Will become
- Folder A
  - File AA
  - File AB
  - File AC
- Folder B
  - File BA
  
### Naming ###
Page title and URL depend on file name.  
File name become page title following this principles: 10_Folder_A -> Folder A  and  10_File_AA.md -> File AA  
File name become page url following this principles: 10_Folder_A -> folder-a  and  10_File_AA.md -> file-aa  

**WARNING**: Changing file or folder names (except numbers and case) will change page URL. Use with caution.
