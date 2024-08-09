<!-- generate_doc -->
# MakeDataAlias

This object create an alias to a data field. 


__Target__: Sofa.Component.SceneUtility

__namespace__: sofa::component::sceneutility::makedataaliascomponent

__parents__:

- BaseObject

### Data

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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

## Examples 

MakeDataAlias.scn

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
    def createScene(root_node):

       root = root_node.addChild('Root', gravity="0 0 0", time="0", animate="0", bbox="-1 -1 -1 1 1 1")

       root.addObject('RequiredPlugin', name="Sofa.Component.SceneUtility")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('MakeDataAlias', componentname="MechanicalObject", dataname="position", alias="myrest_position")
       root.addObject('MechanicalObject', name="position should be 1 2 3 ", myrest_position="1 2 3")
    ```

