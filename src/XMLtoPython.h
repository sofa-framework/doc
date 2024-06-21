#pragma once

#include <tinyxml2.h>

inline std::string indent = "    ";

inline void traversingXML(tinyxml2::XMLNode* node, std::string& pythonString, std::string& currentNode)
{
    if(node == nullptr)
    {
        return;
    }

    if(node->ToDeclaration())
    {
        //skip: no need in Python
    }
    const auto oldNode = currentNode;
    if(node->ToElement())
    {
        auto element = dynamic_cast<tinyxml2::XMLElement*>(node);
        if (std::string{element->Name()} == std::string{"Node"})
        {
            {
                const std::string parentNode = currentNode;
                const tinyxml2::XMLAttribute* attribute = element->FirstAttribute();
                while (attribute != nullptr)
                {
                    if (std::string{attribute->Name()} == "name")
                    {
                        currentNode = std::string{ attribute->Value() };
                        break;
                    }
                    attribute = attribute->Next();
                }
                pythonString += "\n" + indent + indent + currentNode + " = " + parentNode + ".addChild(";
                pythonString += "\'" + currentNode + "\'";
            }
            {
                const tinyxml2::XMLAttribute* attribute = element->FirstAttribute();
                while (attribute != nullptr)
                {
                    if (std::string{attribute->Name()} != "name")
                    {
                        pythonString += ", " + std::string{attribute->Name()} + "=\"" + std::string{attribute->Value()} + "\"";
                    }
                    attribute = attribute->Next();
                }
            }
            pythonString += ")\n";
        }
        else
        {
            pythonString += indent + indent + currentNode + ".addObject(\'" + std::string{element->Name()} + "\'";

            const tinyxml2::XMLAttribute* attribute = element->FirstAttribute();
            while (attribute != nullptr)
            {
                pythonString += ", " + std::string{attribute->Name()} + "=\"" + std::string{attribute->Value()} + "\"";
                attribute = attribute->Next();
            }
            pythonString += ")\n";
        }
    }
    if(node->ToText())
    {
        // auto text = dynamic_cast<tinyxml2::XMLText*>(node);
        // std::cout << "XML text: " << text->Value() << std::endl;
    }
    if(node->ToComment())
    {
        // auto comment = dynamic_cast<tinyxml2::XMLComment*>(node);
        // std::cout << "XML comment: " << comment->Value() << std::endl;
    }
    if(node->ToUnknown())
    {
        // auto unknown = dynamic_cast<tinyxml2::XMLUnknown*>(node);
        // std::cout << "XML unknown: " << unknown->Value() << std::endl;
    }
    if(node->ToDocument())
    {
        // auto document = dynamic_cast<tinyxml2::XMLDocument*>(node);
        // std::cout << "XML document: " << document->ErrorName() << std::endl;
    }
    
    if(node->NoChildren()) {
        return;
    }


    tinyxml2::XMLNode* child = node->FirstChild();
    while(child != nullptr)
    {
        traversingXML(child, pythonString, currentNode);
        child = child->NextSibling();
    }

    currentNode = oldNode;
}

inline void convertXMLToPython(
    const std::string& xmlFilename,
    std::string& pythonString)
{
    tinyxml2::XMLDocument doc;
    doc.LoadFile( xmlFilename.c_str() );

    pythonString += indent + "def createScene(rootNode):\n";

    std::string currentNode { "rootNode" };
    traversingXML(&doc, pythonString, currentNode);
}
