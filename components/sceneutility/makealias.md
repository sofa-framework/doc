# MakeAlias

This object create an alias to a component name to make the scene more readable. 


__Target__: `Sofa.Component.SceneUtility`

__namespace__: `#!c++ sofa::component::sceneutility::makealiascomponent`

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
		<td>targetcomponent</td>
		<td>
The component class for which to create an alias.
</td>
		<td></td>
	</tr>
	<tr>
		<td>alias</td>
		<td>
The new alias of the component.
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

Component/SceneUtility/MakeAlias.scn

=== "XML"

    ```xml
    <?xml version='1.0'?>                                               
    <Node 	name='Root' gravity='0 0 0' time='0' animate='0' bbox="-1 -1 -1 1 1 1"  >   
            <RequiredPlugin name="Sofa.Component.SceneUtility"/> <!-- Needed to use components [MakeAlias] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <DefaultAnimationLoop/>
            <MakeAlias targetcomponent='MechanicalObject' alias='Mecha'/>    
            <MechanicalObject  name="createdWithAlias" position="1 2 3"/>    
    </Node>                                                             
    
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        Root = rootNode.addChild('Root', gravity="0 0 0", time="0", animate="0", bbox="-1 -1 -1 1 1 1")
        Root.addObject('RequiredPlugin', name="Sofa.Component.SceneUtility")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('DefaultAnimationLoop')
        Root.addObject('MakeAlias', targetcomponent="MechanicalObject", alias="Mecha")
        Root.addObject('MechanicalObject', name="createdWithAlias", position="1 2 3")
    ```

