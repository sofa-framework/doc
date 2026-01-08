<!-- generate_doc -->
# VisualMesh

Render a mesh


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
The position of the vertices of mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>elementSpace</td>
		<td>
The space between element (scalar between 0 and 1)
		</td>
		<td>0.15</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|topology|Link to a topology containing elements|BaseMeshTopology|

## Examples 

VisualMesh.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
    
        <Node name="tetra">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" name="state"/>
    
            <TetrahedronSetTopologyContainer name="Tetra_topo" position="@grid.position"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
    
            <VisualMesh position="@state.position" topology="@Tetra_topo"/>
        </Node>
    
        <Node name="hexa">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="grid" min="10 -5 0" max="20 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" name="state"/>
    
            <DiagonalMass massDensity="0.2" />
            <HexahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" method="large"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
    
            <VisualMesh position="@state.position" topology="@grid"/>
        </Node>
    
        <Node name="triangles">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject name="state"/>
            <MeshMatrixMass totalMass="1000" />
            <RegularGridTopology name="grid" nx="5" ny="5" nz="1" min="25 -5 0" max="35 5 0"/>
            <BoxROI box="24 4.99 -0.1 36 5.01 0.1" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices" />
            <TriangleFEMForceField name="FEM1" youngModulus="5000" poissonRatio="0.3" method="large" />
            <VisualMesh position="@state.position" topology="@grid"/>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.81 0")

       tetra = root.addChild('tetra')

       tetra.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       tetra.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       tetra.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
       tetra.addObject('MechanicalObject', template="Vec3", name="state")
       tetra.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo", position="@grid.position")
       tetra.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetra.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetra.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
       tetra.addObject('DiagonalMass', massDensity="0.2")
       tetra.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false")
       tetra.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
       tetra.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
       tetra.addObject('VisualMesh', position="@state.position", topology="@Tetra_topo")

       hexa = root.addChild('hexa')

       hexa.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       hexa.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       hexa.addObject('RegularGridTopology', name="grid", min="10 -5 0", max="20 5 40", n="5 5 20")
       hexa.addObject('MechanicalObject', template="Vec3", name="state")
       hexa.addObject('DiagonalMass', massDensity="0.2")
       hexa.addObject('HexahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", method="large")
       hexa.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
       hexa.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
       hexa.addObject('VisualMesh', position="@state.position", topology="@grid")

       triangles = root.addChild('triangles')

       triangles.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       triangles.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       triangles.addObject('MechanicalObject', name="state")
       triangles.addObject('MeshMatrixMass', totalMass="1000")
       triangles.addObject('RegularGridTopology', name="grid", nx="5", ny="5", nz="1", min="25 -5 0", max="35 5 0")
       triangles.addObject('BoxROI', box="24 4.99 -0.1 36 5.01 0.1", name="box")
       triangles.addObject('FixedProjectiveConstraint', indices="@box.indices")
       triangles.addObject('TriangleFEMForceField', name="FEM1", youngModulus="5000", poissonRatio="0.3", method="large")
       triangles.addObject('VisualMesh', position="@state.position", topology="@grid")
    ```

