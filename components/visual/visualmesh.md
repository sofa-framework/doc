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
	<tr>
		<td>lighting</td>
		<td>
If true, light is simulated on the mesh. Otherwise, no lighting effect.
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>vertexValues</td>
		<td>
Optional list of values associated to the vertices of the mesh. If provided, the values are converted to colors.
		</td>
		<td></td>
	</tr>
	<tr>
		<td>colorMap</td>
		<td>
Color map used to convert vertex values to colors.
		</td>
		<td>#ff0000ff #ff0500ff #ff0b00ff #ff1100ff #ff1700ff #ff1d00ff #ff2300ff #ff2900ff #ff2f00ff #ff3500ff #ff3b00ff #ff4100ff #ff4700ff #ff4e00ff #ff5400ff #ff5900ff #ff5f00ff #ff6600ff #ff6c00ff #ff7100ff #ff7700ff #ff7e00ff #ff8400ff #ff8a00ff #ff9000ff #ff9600ff #ff9c00ff #ffa200ff #ffa800ff #ffae00ff #ffb400ff #ffba00ff #ffc000ff #ffc600ff #ffcc00ff #ffd200ff #ffd800ff #ffde00ff #ffe400ff #ffea00ff #fff000ff #fff600ff #fffc00ff #fbff00ff #f5ff00ff #efff00ff #e9ff00ff #e3ff00ff #ddff00ff #d7ff00ff #d1ff00ff #cbff00ff #c5ff00ff #bfff00ff #b9ff00ff #b3ff00ff #adff00ff #a7ff00ff #a1ff00ff #9bff00ff #95ff00ff #8fff00ff #89ff00ff #83ff00ff #7dff00ff #77ff00ff #71ff00ff #6bff00ff #65ff00ff #5fff00ff #59ff00ff #53ff00ff #4dff00ff #47ff00ff #41ff00ff #3bff00ff #35ff00ff #2fff00ff #29ff00ff #23ff00ff #1dff00ff #17ff00ff #11ff00ff #0bff00ff #05ff00ff #00ff00ff #00ff06ff #00ff0bff #00ff12ff #00ff17ff #00ff1eff #00ff24ff #00ff2aff #00ff2fff #00ff36ff #00ff3bff #00ff42ff #00ff48ff #00ff4eff #00ff54ff #00ff5aff #00ff60ff #00ff66ff #00ff6cff #00ff72ff #00ff78ff #00ff7eff #00ff84ff #00ff8aff #00ff90ff #00ff96ff #00ff9cff #00ffa2ff #00ffa8ff #00ffaeff #00ffb4ff #00ffbaff #00ffc0ff #00ffc6ff #00ffccff #00ffd2ff #00ffd8ff #00ffdeff #00ffe4ff #00ffeaff #00fff0ff #00fff6ff #00fffcff #00fbffff #00f5ffff #00efffff #00e9ffff #00e3ffff #00ddffff #00d7ffff #00d1ffff #00cbffff #00c5ffff #00bfffff #00b9ffff #00b3ffff #00adffff #00a7ffff #00a2ffff #009bffff #0095ffff #008fffff #0089ffff #0083ffff #007dffff #0077ffff #0071ffff #006bffff #0065ffff #005fffff #0059ffff #0053ffff #004dffff #0047ffff #0041ffff #003bffff #0035ffff #002fffff #0029ffff #0023ffff #001dffff #0017ffff #0011ffff #000bffff #0005ffff #0000ffff #0600ffff #0c00ffff #1200ffff #1700ffff #1e00ffff #2400ffff #2900ffff #2f00ffff #3600ffff #3c00ffff #4200ffff #4800ffff #4e00ffff #5400ffff #5a00ffff #5f00ffff #6600ffff #6c00ffff #7200ffff #7700ffff #7e00ffff #8400ffff #8a00ffff #9000ffff #9600ffff #9c00ffff #a200ffff #a800ffff #ae00ffff #b400ffff #ba00ffff #c000ffff #c600ffff #cc00ffff #d200ffff #d800ffff #de00ffff #e400ffff #ea00ffff #f000ffff #f600ffff #fc00ffff #ff00fbff #ff00f5ff #ff00efff #ff00e9ff #ff00e3ff #ff00ddff #ff00d7ff #ff00d1ff #ff00cbff #ff00c5ff #ff00bfff #ff00b9ff #ff00b3ff #ff00adff #ff00a7ff #ff00a1ff #ff009bff #ff0095ff #ff008fff #ff0089ff #ff0083ff #ff007dff #ff0077ff #ff0071ff #ff006bff #ff0065ff #ff005fff #ff0059ff #ff0053ff #ff004dff #ff0047ff #ff0041ff #ff003bff #ff0035ff #ff002fff #ff0029ff #ff0023ff #ff001dff #ff0017ff #ff0011ff #ff000bff #ff0005ff #ff0000ff</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
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
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" swapping="true"/>
    
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
       tetra.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo", swapping="true")
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

