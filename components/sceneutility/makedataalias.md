# MakeDataAlias

This object create an alias to a data field. 


__Target__: `Sofa.Component.SceneUtility`

__namespace__: `#!c++ sofa::component::sceneutility::makedataaliascomponent`

__parents__: 

- `#!c++ BaseObject`

__categories__: 

- _Miscellaneous

Data: 

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Default value</th>
    </tr>
</thead>
<tbody>
	<tr>
		<td>name</td>
		<td>
object name
</td>
		<td>unnamed</td>
	</tr>
	<tr>
		<td>printLog</td>
		<td>
if true, emits extra messages at runtime.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tags</td>
		<td>
list of the subsets the objet belongs to
</td>
		<td></td>
	</tr>
	<tr>
		<td>bbox</td>
		<td>
this object bounding box
</td>
		<td></td>
	</tr>
	<tr>
		<td>componentState</td>
		<td>
The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
</td>
		<td>Undefined</td>
	</tr>
	<tr>
		<td>listening</td>
		<td>
if true, handle the events, otherwise ignore the events
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>componentname</td>
		<td>
The component class for which to create an alias.
</td>
		<td></td>
	</tr>
	<tr>
		<td>dataname</td>
		<td>
The data field for which to create an alias.
</td>
		<td></td>
	</tr>
	<tr>
		<td>alias</td>
		<td>
The alias of the data field.
</td>
		<td></td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



## Examples

Component/SceneUtility/MakeDataAlias.scn

=== "XML"

    ```xml
    <?xml version='1.0'?>                                               
    <Node 	name='Root' gravity='0 0 0' time='0' animate='0' bbox="-1 -1 -1 1 1 1"  >   
           <RequiredPlugin name="Sofa.Component.SceneUtility"/> <!-- Needed to use components [MakeDataAlias] -->
           <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
           <DefaultAnimationLoop/>      
           <MakeDataAlias componentname='MechanicalObject' dataname='position' alias='myrest_position'/> 
           <MechanicalObject name="position should be 1 2 3 " myrest_position='1 2 3'/>                                                 
    </Node>                                                             
    
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        Root = rootNode.addChild('Root', gravity="0 0 0", time="0", animate="0", bbox="-1 -1 -1 1 1 1")
        Root.addObject('RequiredPlugin', name="Sofa.Component.SceneUtility")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('DefaultAnimationLoop')
        Root.addObject('MakeDataAlias', componentname="MechanicalObject", dataname="position", alias="myrest_position")
        Root.addObject('MechanicalObject', name="position should be 1 2 3 ", myrest_position="1 2 3")
    ```

