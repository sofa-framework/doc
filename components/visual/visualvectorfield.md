<!-- generate_doc -->
# VisualVectorField

Render a vector field.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Visual

__namespace__: sofa::component::visual

__parents__:

- VisualModel

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
		<td>enable</td>
		<td>
Display the object or not
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Starting position of the rendered vectors
		</td>
		<td></td>
	</tr>
	<tr>
		<td>vector</td>
		<td>
List of vectors to render
		</td>
		<td></td>
	</tr>
	<tr>
		<td>vectorScale</td>
		<td>
Scaling factor applied on vectors for rendering
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>color</td>
		<td>
Color of the vectors
		</td>
		<td>1 1 1 1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawMode</td>
		<td>
Draw mode for the vectors- Line: Coordinates are displayed using lines
- Cylinder: Coordinates are displayed using cylinders
- Arrow: Coordinates are displayed using arrows
		</td>
		<td>Line</td>
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

VisualVectorField.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 -9.81 0" dt="0.01">
        <DefaultAnimationLoop parallelODESolving="true"/>
        <DefaultVisualManagerLoop name="visualLoop"/>
        <VisualStyle displayFlags="showVisual showWireframe showForceFields" />
        <VisualGrid name="grid"/>
        <LineAxis size="@grid.size"/>
    
        <Node name="beam">
            <EulerImplicitSolver name="odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <ConstantSparsityPatternSystem template="CompressedRowSparseMatrixd" name="A"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixd"/>
            <MechanicalObject name="DoFs" template="Vec3" />
            <UniformMass name="mass" totalMass="320" />
            <RegularGridTopology name="grid" nx="4" ny="4" nz="10" xmin="-1" xmax="1" ymin="-1" ymax="1" zmin="0" zmax="9" />
            <BoxROI name="box" box="-2 -2 -0.0001  2 2 0.0001"/>
            <FixedProjectiveConstraint indices="@box.indices" />
            <HexahedronFEMForceField name="FEM" youngModulus="40000" poissonRatio="0.3" method="large" />
    
            <Node name="vectors">
                <VisualStyle displayFlags="showVisual hideWireframe" />
                <VisualVectorField position="@DoFs.position" vector="@DoFs.velocity" drawMode="Arrow" vectorScale="0.2" color="orange"/>
                <VisualVectorField position="@DoFs.position" vector="@DoFs.force" drawMode="Arrow" vectorScale="0.0005" color="navy"/>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.01")

       root.addObject('DefaultAnimationLoop', parallelODESolving="true")
       root.addObject('DefaultVisualManagerLoop', name="visualLoop")
       root.addObject('VisualStyle', displayFlags="showVisual showWireframe showForceFields")
       root.addObject('VisualGrid', name="grid")
       root.addObject('LineAxis', size="@grid.size")

       beam = root.addChild('beam')

       beam.addObject('EulerImplicitSolver', name="odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       beam.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrixd", name="A")
       beam.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixd")
       beam.addObject('MechanicalObject', name="DoFs", template="Vec3")
       beam.addObject('UniformMass', name="mass", totalMass="320")
       beam.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="10", xmin="-1", xmax="1", ymin="-1", ymax="1", zmin="0", zmax="9")
       beam.addObject('BoxROI', name="box", box="-2 -2 -0.0001  2 2 0.0001")
       beam.addObject('FixedProjectiveConstraint', indices="@box.indices")
       beam.addObject('HexahedronFEMForceField', name="FEM", youngModulus="40000", poissonRatio="0.3", method="large")

       vectors = beam.addChild('vectors')

       vectors.addObject('VisualStyle', displayFlags="showVisual hideWireframe")
       vectors.addObject('VisualVectorField', position="@DoFs.position", vector="@DoFs.velocity", drawMode="Arrow", vectorScale="0.2", color="orange")
       vectors.addObject('VisualVectorField', position="@DoFs.position", vector="@DoFs.force", drawMode="Arrow", vectorScale="0.0005", color="navy")
    ```

