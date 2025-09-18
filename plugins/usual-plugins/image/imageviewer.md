<!-- generate_doc -->
# ImageViewer

Image viewer


## ImageB

Templates:

- ImageB

__Target__: image

__namespace__: sofa::component::misc

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
		<td>slicedModels</td>
		<td>
display visual models on cutPlanes
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>points</td>
		<td>

		</td>
		<td></td>
	</tr>
	<tr>
		<td>vectorvis</td>
		<td>

		</td>
		<td>551010LowerTriRowMajor</td>
	</tr>
	<tr>
		<td>scrollDirection</td>
		<td>
0 if no scrolling, 1 for up, 2 for down, 3 left, and 4 for right
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>display</td>
		<td>
true if image is displayed, false otherwise
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Image</td>
	</tr>
	<tr>
		<td>image</td>
		<td>
input image
		</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>plane</td>
		<td>

		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td colspan="3">Histogram</td>
	</tr>
	<tr>
		<td>histo</td>
		<td>

		</td>
		<td>0 1</td>
	</tr>
	<tr>
		<td colspan="3">Transform</td>
	</tr>
	<tr>
		<td>transform</td>
		<td>

		</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

<!-- generate_doc -->
## ImageD

Templates:

- ImageD

__Target__: image

__namespace__: sofa::component::misc

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
		<td>slicedModels</td>
		<td>
display visual models on cutPlanes
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>points</td>
		<td>

		</td>
		<td></td>
	</tr>
	<tr>
		<td>vectorvis</td>
		<td>

		</td>
		<td>551010LowerTriRowMajor</td>
	</tr>
	<tr>
		<td>scrollDirection</td>
		<td>
0 if no scrolling, 1 for up, 2 for down, 3 left, and 4 for right
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>display</td>
		<td>
true if image is displayed, false otherwise
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Image</td>
	</tr>
	<tr>
		<td>image</td>
		<td>
input image
		</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>plane</td>
		<td>

		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td colspan="3">Histogram</td>
	</tr>
	<tr>
		<td>histo</td>
		<td>

		</td>
		<td>-1.79769e+308 1.79769e+308</td>
	</tr>
	<tr>
		<td colspan="3">Transform</td>
	</tr>
	<tr>
		<td>transform</td>
		<td>

		</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

<!-- generate_doc -->
## ImageUC

Templates:

- ImageUC

__Target__: image

__namespace__: sofa::component::misc

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
		<td>slicedModels</td>
		<td>
display visual models on cutPlanes
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>points</td>
		<td>

		</td>
		<td></td>
	</tr>
	<tr>
		<td>vectorvis</td>
		<td>

		</td>
		<td>551010LowerTriRowMajor</td>
	</tr>
	<tr>
		<td>scrollDirection</td>
		<td>
0 if no scrolling, 1 for up, 2 for down, 3 left, and 4 for right
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>display</td>
		<td>
true if image is displayed, false otherwise
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Image</td>
	</tr>
	<tr>
		<td>image</td>
		<td>
input image
		</td>
		<td>0 0 0 0 0</td>
	</tr>
	<tr>
		<td>plane</td>
		<td>

		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td colspan="3">Histogram</td>
	</tr>
	<tr>
		<td>histo</td>
		<td>

		</td>
		<td>0 255</td>
	</tr>
	<tr>
		<td colspan="3">Transform</td>
	</tr>
	<tr>
		<td>transform</td>
		<td>

		</td>
		<td>0 0 0 0 0 0 1 1 1 0 1 0</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

