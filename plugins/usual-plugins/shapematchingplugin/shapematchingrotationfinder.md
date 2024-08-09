<!-- generate_doc -->
# ShapeMatchingRotationFinder

ShapeMatchingRotationFinder


## Vec3d

Templates:

- Vec3d

__Target__: ShapeMatchingPlugin

__namespace__: sofa::component::container

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
		<td>axisToFlip</td>
		<td>
Flip Axis
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>neighborhoodLevel</td>
		<td>
Neighborhood level
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>numOfClusters</td>
		<td>
Number of clusters
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>maxIter</td>
		<td>
Number of iterations to build the neighborhood
		</td>
		<td>500</td>
	</tr>
	<tr>
		<td>epsilon</td>
		<td>
epsilon
		</td>
		<td>1e-10</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
radius between Cm and point position
		</td>
		<td>0.001</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showRotations</td>
		<td>
Show Rotations
		</td>
		<td>0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalState|link to the mechanical state|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

