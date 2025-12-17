<!-- generate_doc -->
# ImplicitSurfaceMapping

Compute an iso-surface from a set of particles.


## Vec3d,Vec3d

Templates:

- Vec3d,Vec3d

__Target__: SofaImplicitField

__namespace__: sofaimplicitfield::mapping

__parents__:

- Mapping
- MeshTopology

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
		<td>mapForces</td>
		<td>
Are forces mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapConstraints</td>
		<td>
Are constraints mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMasses</td>
		<td>
Are masses mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMatrices</td>
		<td>
Are matrix explicit mapped?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>applyRestPosition</td>
		<td>
set to true to apply this mapping to restPosition at init
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
Filename of the mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
List of point positions
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
List of edge indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
List of triangle indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
List of quad indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
List of tetrahedron indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
List of hexahedron indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>prisms</td>
		<td>
List of prisms indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pyramids</td>
		<td>
List of pyramids indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>uv</td>
		<td>
List of uv coordinates
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeAllBuffers</td>
		<td>
Option to compute all crossed topology buffers at init. False by default
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>step</td>
		<td>
Step
		</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Radius
		</td>
		<td>2</td>
	</tr>
	<tr>
		<td>isoValue</td>
		<td>
Iso Value
		</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td>min</td>
		<td>
Grid Min
		</td>
		<td>-100 -100 -100</td>
	</tr>
	<tr>
		<td>max</td>
		<td>
Grid Max
		</td>
		<td>100 100 100</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawEdges</td>
		<td>
if true, draw the topology Edges
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTriangles</td>
		<td>
if true, draw the topology Triangles
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawQuads</td>
		<td>
if true, draw the topology Quads
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTetrahedra</td>
		<td>
if true, draw the topology Tetrahedra
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawHexahedra</td>
		<td>
if true, draw the topology hexahedra
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
|input|Input object to map|State&lt;Vec3d&gt;|
|output|Output object to map|State&lt;Vec3d&gt;|

## Examples 

ImplicitSurfaceMapping.scn

=== "XML"

    ```xml
    <Node dt="0.005" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaImplicitField"/> <!-- Needed to use components [ImplicitSurfaceMapping] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <Node name="Liver">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="loader" filename="mesh/liver.msh" />
            <MechanicalObject src="@loader" name="dofs" showObject="1" showObjectScale="10.0"/>
            <UniformMass name="M1" vertexMass="1" />
            <Node id="Visual">
                <OglModel name="VModel" color="blue" />
                <ImplicitSurfaceMapping name="MarchingCube" input="@../dofs" output="@VModel"
                                        isoValue="0.1" radius="0.5" step="0.25"
                                        min="-10 -10 -10" max="10 10 10"
                />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       node = root_node.addChild('node', dt="0.005", gravity="0 -10 0")

       node.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       node.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       node.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       node.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       node.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       node.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       node.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       node.addObject('RequiredPlugin', name="SofaImplicitField")
       node.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")

       liver = node.addChild('Liver')

       liver.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       liver.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       liver.addObject('MeshGmshLoader', name="loader", filename="mesh/liver.msh")
       liver.addObject('MechanicalObject', src="@loader", name="dofs", showObject="1", showObjectScale="10.0")
       liver.addObject('UniformMass', name="M1", vertexMass="1")

       node = Liver.addChild('node', id="Visual")

       node.addObject('OglModel', name="VModel", color="blue")
       node.addObject('ImplicitSurfaceMapping', name="MarchingCube", input="@../dofs", output="@VModel", isoValue="0.1", radius="0.5", step="0.25", min="-10 -10 -10", max="10 10 10")
    ```

