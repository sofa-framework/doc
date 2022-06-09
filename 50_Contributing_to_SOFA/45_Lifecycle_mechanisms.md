This page aims at detailing the steps to follow when moving, renaming or removing code in SOFA. It focuses on: components and data field.

_______________________________________________________

## Components

### Moving a Component to another module

0. do the move
1. deprecated phase (6 months)
    - [dev] in Sofa.Compat
        - create a compatibility header with same name and same path
        - in compat header, include new header
        - add macro SOFA_DEPRECATED_HEADER
        - add aliases for all classes, static functions, global variables
        - add a macro SOFA_ATTRIBUTE_DEPRECATED on these aliases
    - [user] in ComponentChange
        - add as CreatableMoved() in deprecatedComponents
2. deleted phase (6 months)
    - [dev] in Sofa.Compat
        - change the macro for SOFA_DISABLED_HEADER
        - change the alias to be on DeprecatedOrRemoved
        - change the alias macro for SOFA_ATTRIBUTE_DISABLED
    - [user] in ComponentChange
        - changed to Removed() and move to uncreatableComponents
3. remove the compat + cleanup
    - [dev] in the component class
        - erase the class
        - erase the alias
    - [user] in ComponentChange
        - erase the ComponentChange entry

### Renaming a Component

0. do the renaming
1. deprecated phase (6 months)
    - [dev] in the component class
        - <span style="color:red">create an empty header with old name including the new file</span>
        - add a C++ alias for the component name
        - add a macro SOFA_ATTRIBUTE_DEPRECATED on this alias
    - [user] in the component's registration to the factory
        - add a SOFA alias to OldName in RegisterObject
    - [user] in ComponentChange
        - add the SOFA alias as Deprecated() in deprecatedComponents
2. renamed phase (6 months)
    - [dev] in the component class
        - change the C++ alias to be on DeprecatedOrRemoved
        - change the macro for SOFA_ATTRIBUTE_DISABLED
    - [user] in the component's registration to the factory
        - remove the SOFA alias
    - [user] in ComponentChange
        - change the SOFA alias to Renamed() and move to uncreatableComponents
3. cleanup
    - [dev] in the component class
        - remove the C++ alias
    - [user] in ComponentChange
        - remove the SOFA alias entry

### Removing a Component

1. deprecated phase (6 months)
    - [dev] in the component class
        - use a macro to deprecate the class
    - [user] in ComponentChange
        - add as Deprecated() in deprecatedComponents
2. deleted phase (6 months)
    - [dev] in the component class
        - delete the class
    - [dev] in Sofa.Compat
        - create a compatibility header with same name and same path
        - add macro SOFA_DISABLED_HEADER
        - add aliases for all classes, static functions, global variables
        - add a macro SOFA_ATTRIBUTE_DISABLED on these aliases
    - [user] in ComponentChange
        - change to Removed() and move to uncreatableComponents
3. cleanup
    - [dev] in Sofa.Compat
        - remove the compatibility header
    - [user] in ComponentChange
        - remove the entry

_______________________________________________________

## Datafields

### Renaming a Datafield


0. do the renaming
1. deprecated phase (6 months)
    - [user] in the component `parse()` method
        - add the macro <span style="color:red">NOT YET existing: warn about deprecation and renaming to come + copy value in the new data</span>
    - [user] update all scenes using the data
2. renamed phase (6 months)
    - [user] in the component `parse()` method
        - add the macro <span style="color:red">NOT YET existing: error about renaming</span>
3. cleanup
    - [user] in the component `parse()` method
        - remove the macro

### Removing a Datafield

1. deprecated phase (6 months)
    - [dev] in the component class
        - add macro SOFA_ATTRIBUTE_DEPRECATED on the Data member
    - [dev] in whole codebase
        - remove all references to this Datafield
    - [user] in component constructor
        - remove initData
    - [user] in the component `parse()` method
        - add the macro <span style="color:red">NOT YET existing: warn about deprecation and deletion to come</span>
    - [user] update all scenes using the data
2. deleted phase (6 months)
    - [dev] in the component class
        - change macro to SOFA_ATTRIBUTE_DISABLED and member type to DeprecatedOrRemoved
    - [user] in the component `parse()` method
        - change the macro <span style="color:red">NOT YET existing: error about deletion</span>
3. cleanup
    - [dev] in the component class
        - remove the member
    - [user] in the component `parse()` method
        - remove the macro

