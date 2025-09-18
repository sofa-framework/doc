<!-- generate_doc -->
# DepthMapToMeshEngine

Compute a mesh from a depth map image 


Templates:

- ImageB
- ImageD
- ImageUC

__Target__: image

__namespace__: sofa::component::engine

__parents__:

- DataEngine

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
list of the subsets the object belongs to
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
		<td>depthFactor</td>
		<td>
Intensity to depth factor
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>minThreshold</td>
		<td>
minimal depth for point creation
		</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>diffThreshold</td>
		<td>
maximal depth variation for triangle creation
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>image</td>
		<td>

		</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>transform</td>
		<td>

		</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>
	<tr>
		<td>texImage</td>
		<td>

		</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
output positions
		</td>
		<td></td>
	</tr>
	<tr>
		<td>texCoord</td>
		<td>
output texture coordinates
		</td>
		<td></td>
	</tr>
	<tr>
		<td>texOffset</td>
		<td>
texture offsets (in [0,1])
		</td>
		<td>0 0</td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
output triangles
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

