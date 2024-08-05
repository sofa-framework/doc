This page aims at detailing the steps to follow when moving, renaming or removing code in SOFA. It focuses on: components and data field.

_______________________________________________________

## Components

### Moving a Component to another module

<table>
<tbody>
  <tr>
    <td>Steps</td>
    <td>Dev-oriented changes</td>
    <td>Users-oriented changes</td>
  </tr>
  <tr>
    <td>Do the move</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Deprecation<br>(6 months)</td>
    <td>
<ul>
<li>Keep a compatibility header (with same old name and path)</li>
<li>in the header, include new header</li>
<li>add macro <code>SOFA_HEADER_DEPRECATED</code></li>
</ul>
</td>
    <td><ul><li>Add as CreatableMoved() in deprecatedComponents in ComponentChange</li></ul></td>
  </tr>
  <tr>
    <td>Deletion<br>(6 months)</td>
    <td><ul><li>In the old compatibility header, change the macro for <code>SOFA_HEADER_DISABLED</code></li></ul></td>
    <td><ul><li>Change to Removed() and move to uncreatableComponents in ComponentChange</li></ul></td>
  </tr>
  <tr>
    <td>Cleanup</td>
    <td>
<ul>
<li>Erase the class</li>
<li>Erase the alias</li>
</ul>
</td>
    <td><ul><li>Erase the ComponentChange entry in ComponentChange</li></ul></td>
  </tr>
</tbody>
</table>




### Renaming a Component


<table>
<tbody>
  <tr>
    <td>Steps</td>
    <td>Dev-oriented changes</td>
    <td>Users-oriented changes</td>
  </tr>
  <tr>
    <td>Do the renaming</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Deprecation<br>(6 months)</td>
    <td>
<ul>
<li>Let an (almost-) empty header with the old name which:<ul>
<li>includes the new file</li>
<li>Add a macro <code>SOFA_HEADER_DEPRECATED</code> after the include</li>
<li>Add a C++ <code>using</code> alias with the new component name preceeded by a macro <code>SOFA_ATTRIBUTE_DEPRECATED</code></li>
</ul>
</li>
</ul>
</td>
    <td>
<ul>
<li>Add a SOFA alias to OldName in RegisterObject in the component's registration to the factory</li>
<li>Add the SOFA alias as Deprecated() in deprecatedComponents in ComponentChange</li>
</ul>
</td>
  </tr>
  <tr>
    <td>Disabling<br>(6 months)</td>
    <td>
<ul>
<li>Change the C++ alias to be on DeprecatedOrRemoved in the component class</li>
<li>Change the macro for <code>SOFA_HEADER_DISABLED</code></li>
<li>Change the macro for <code>SOFA_ATTRIBUTE_DISABLED</code></li>
</ul></td>
    <td>
<ul>
<li>Remove the SOFA alias in the component's registration to the factory</li>
<li>change the SOFA alias to Renamed() and move to uncreatableComponents in ComponentChange</li>
</ul>
</td>
  </tr>
  <tr>
    <td>Cleanup</td>
    <td><ul><li>Remove the old-name component class</li></ul></td>
    <td></td>
  </tr>
</tbody>
</table>



### Removing a Component

<!--
2. disabale phase (6 months)
   - [dev] in Sofa.Compat
        - create a compatibility header with same name and same path
        - add macro SOFA_HEADER_DISABLED
        - add aliases for all classes, static functions, global variables
        - add a macro SOFA_ATTRIBUTE_DISABLED on these aliases
-->
<!--
3. cleanup
    - [dev] in Sofa.Compat
        - remove the compatibility header
-->


<table>
<tbody>
  <tr>
    <td>Steps</td>
    <td>Dev-oriented changes</td>
    <td>Users-oriented changes</td>
  </tr>
  <tr>
    <td>Deprecation<br>(6 months)</td>
    <td><ul><li>use a macro to deprecate the class <code>SOFA_HEADER_DEPRECATED_NOT_REPLACED</code></li></ul></td>
    <td><ul><li>Add as Deprecated() in deprecatedComponents in ComponentChange</li></ul></td>
  </tr>
  <tr>
    <td>Deletion<br>(6 months)</td>
    <td><ul><li>Empty the class and use the macro <code>SOFA_HEADER_DISABLED_NOT_REPLACED</code></li></ul></td>
    <td><ul><li>Change to Removed() and move to uncreatableComponents in ComponentChange</li></ul></td>
  </tr>
  <tr>
    <td>Cleanup</td>
    <td>
<ul>
<li>Delete the class</li>
<li>Update the associated CMakeLists</li>
</ul>
</td>
    <td></td>
  </tr>
</tbody>
</table>

_______________________________________________________

## Datafields

This section relies a lot on the DeprecatedData and RemovedData mechanism, introduced in [#3934](https://github.com/sofa-framework/sofa/pull/3934).

### Renaming a Datafield

<table>
<tbody>
  <tr>
    <td>Steps</td>
    <td>Dev-oriented changes</td>
    <td>Users-oriented changes</td>
  </tr>
  <tr>
    <td>Do the renaming</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Deprecation<br>(6 months)</td>
    <td><ul><li>Use a fake DeprecatedData with the old datafield name in the component class</li></ul></td>
    <td><ul><li>Update all scenes using the data</li></ul></td>
  </tr>
  <tr>
    <td>Renaming<br>(6 months)</td>
    <td><ul><li>Replace the DeprecatedData with RemovedData in the component class</li></ul></td>
    <td></td>
  </tr>
  <tr>
    <td>Cleanup</td>
    <td><ul><li>Remove the RemovedData member in the component class</li></ul></td>
    <td></td>
  </tr>
</tbody>
</table>




### Removing a Datafield

<table>
<tbody>
  <tr>
    <td>Steps</td>
    <td>Dev-oriented changes</td>
    <td>Users-oriented changes</td>
  </tr>
  <tr>
    <td>Deprecation<br>(6 months)</td>
    <td>
<ul>
<li>Use a fake DeprecatedData in the component class</li>
<li>Remove all references to this Data in whole codebase</li>
</ul>
</td>
    <td>
<ul><li>Update all scenes using the data</li></ul>
</td>
  </tr>
  <tr>
    <td>Deletion<br>(6 months)</td>
    <td><ul><li>Replace the DeprecatedData with RemovedData in the component class</li></ul></td>
    <td></td>
  </tr>
  <tr>
    <td>Cleanup<br>(6 months)</td>
    <td><ul><li>Remove the RemovedData member in the component class</li></ul></td>
    <td></td>
  </tr>
</tbody>
</table>


### Changing Data default value

As suggested in [#3563](https://github.com/sofa-framework/sofa/pull/3563), when the default value of a Data is changed the following warning should be added in the `init()` function:

``` cpp
msg_warning_when(!d_dataName.isSet()) << "The default value of the Data " << d_dataName.getName() << " changed in v23.06 from 0.3 to 0.45.";
```
