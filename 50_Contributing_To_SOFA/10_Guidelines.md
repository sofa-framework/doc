A **must** requirement is mandatory, a *should* is a strong
recommendation, and a *can* is a general guideline.

Good Behavior
-------------

1.  Each commit **must** build successfully.
2.  You **must** check that your changes don't introduce
    compiler warnings.
3.  You **must** check that the default Sofa scene still runs correctly
    and that you did not add any warnings during execution.
4.  When you push commits to the repository on the GForge, you **must**
    monitor the Sofa [Dashboard](http://sofa-framework.org/dash). It is
    **your** responsibility to make sure Sofa continues to compile and
    work on all the tested platforms.

Coding Rules
------------

### Naming

1.  Identifiers **must** respect the following convention:
    -   Class names are in UpperCamelCase
    -   Function names are in lowerCamelCase()
    -   namespaces names are in lowercase
    -   variables names are in lowerCamelCase (exception: mathematical
        objects, e.g. Matrix M), and must express their use more than
        their type (exceptions: local iterators variables (i, j, k), and
        usual symbols (x for positions, v for velocities))
    -   Data member variables names **must** begin with d\_
    -   Link member variables names (e.g. SingleLink) **must** begin
        with l\_
    -   Other member variables names **must** begin with m\_ (exception:
        this is not mandatory for PODs as well as public attributes)
    -   Names for booleans variables **must** answer a question:
        m\_isRed, m\_hasName

2.  C++ files **must** must have the extension .h, .cpp, or .inl
3.  Files that define a class *should* have the same name as the class,
    and they usually *should* contain only one class.
4.  Each library name *should* be prefixed with "Sofa".

### Formatting

1.  Indentation **must** use 4 spaces everywhere (C++ and Python), but
    there **must** be no indentation for namespaces
2.  Braces: use the Allman style: the opening brace associated with a
    control statement is on the next line, indented to the same level as
    the control statement, and statements within the braces are indented
    to the next level.

    ``` {.decode:true}
    while (x == y)
    {
        something();
        somethingElse();
     }
    finalThing();
        
    ```

3.  A space character should be used in the following situations:

    -   After C++ reserved words (e.g. if (true))
    -   Around binary operators (e.g. a + b)
    -   After commas (e.g. doSomething(a, b, c))
    -   After semicolons in for statements (e.g. for (unsigned int i =
        0; i &lt; container.size(); i++)

    ``` {.decode:true}
    for (unsigned int i = 0; i < container.size(); ++i )
    {
        if ((a + b) > c)
        {
            doSomething(a, b, c);
        }
    }
            
    ```

4.  Template declarations are split on two lines:

    ``` {.decode:true}
    template<class T>
    static void dynamicCast(T*& ptr, Base* b);
        
    ```

### Generic Rules

1.  Tricky code *should* not be commented but rewritten! In general, the
    use of comments *should* be minimized by making the code
    self-documenting by appropriate name choices and an explicit logical
    structure
2.  All comments **must** be written in English. In an international
    environment English is the preferred language
3.  Special characters like TAB and page break **must** be avoided
4.  The use of magic numbers in the code *should* be avoided. Numbers
    other than 0 and 1 *should* be declared as named constants instead

### C++

1.  You should try to use as few \#include directive as possible
2.  You should limit as much as possible the amount of code in included
    files (\*.h, \*.inl)
3.  All definitions *should* reside in source files. The header files
    *should* declare an interface only
4.  Variables *should* be initialized when they are declared.
5.  You *should* use const profusely
6.  You *should* use assert profusely
7.  You **must** avoid using-directives (`using namespace foo;`) in
    header files (.h and .inl)
8.  You *should* declare automatic variables only when you need them
    (not before).
9.  You **must** always initialize pointers, either to the address of
    something, or to NULL.

SOFA specific rules
-------------------

1.  All the code under development **must** be tagged SOFA\_DEV
2.  All internal data, needed by your component, and that can't be
    recomputed **must** be put inside a Data or a DataPtr. This way,
    your component can be saved. Also, this Data will be automatically
    displayed inside the GUI
3.  Use sout, serr, sendl instead of cout, cerr, endl in
    SOFA Components.
    -   serr will automatically display inside the console a message
        with a warning, the name of the component, and its class. If you
        modify the component in the graph, you will see a tabulation
        named "Warnings" with the log of all the serr done by the
        component
    -   sout will display inside the console a message ONLY if the Data
        f\_printLog is set to true. If you modify the component in the
        graph, you will see a tabulation named "Outputs" with the log of
        all the sout done by the component

4.  Use sofa::helper::vector, sofa::helper::set instead of std::vector,
    std::set
5.  Only use sofa::simulation::tree::GNode when you need to directly use
    access to the children or the parent of the node. If not, use the
    more generic sofa::simulation::Node

Documentation rules
-------------------

1.  A small description for each component **must** be provided, when it
    is added to the factory.
2.  An example showing the behavior of each component **must** be
    provided, and placed in examples/Components/. This xml file **must**
    have the exact same name as the component.
3.  Documentation in the code **must** be doxygen compliant, example for
    [C++](http://www.stack.nl/~dimitri/doxygen/manual/docblocks.html#cppblock)
    and
    [Python](http://www.stack.nl/~dimitri/doxygen/manual/docblocks.html#pythonblocks).

Version Control Rules
---------------------

1.  Each commit message **must** be meaningful and describe the change
    introduced in the commit.
2.  Each commit *should* contain only one logical modification.
3.  Mixing indentation and logical modifications in a same commit
    *should* be avoided.

