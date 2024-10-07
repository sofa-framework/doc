<!-- generate_doc -->
# CylinderGridTopology

Cylinder grid in 3D.


__Target__: Sofa.Component.Topology.Container.Grid

__namespace__: sofa::component::topology::container::grid

__parents__:

- GridTopology

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
		<td>uv</td>
		<td>
List of uv coordinates
		</td>
		<td></td>
	</tr>
	<tr>
		<td>n</td>
		<td>
grid resolution. (default = 2 2 2)
		</td>
		<td>2 2 2</td>
	</tr>
	<tr>
		<td>computeHexaList</td>
		<td>
put true if the list of Hexahedra is needed during init (default=true)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeQuadList</td>
		<td>
put true if the list of Quad is needed during init (default=true)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeTriangleList</td>
		<td>
put true if the list of Triangles is needed during init (default=true)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computeEdgeList</td>
		<td>
put true if the list of Lines is needed during init (default=true)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>computePointList</td>
		<td>
put true if the list of Points is needed during init (default=true)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>createTexCoords</td>
		<td>
If set to true, virtual texture coordinates will be generated using 3D interpolation (default=false).
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>center</td>
		<td>
Center of the cylinder
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>axis</td>
		<td>
Main direction of the cylinder
		</td>
		<td>0 0 1</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Radius of the cylinder
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>length</td>
		<td>
Length of the cylinder along its axis
		</td>
		<td>1</td>
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

## Examples 

CylinderGridTopology.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02" gravity="0 0 100">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [CylinderGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields showVisual" />
        <DefaultAnimationLoop/>
        
        <Node name="Reference">
            <MeshOBJLoader name="meshLoader_0" filename="mesh/truthcylinder1-bent.obj" scale="0.95" handleSeams="1" />
            <OglModel src="@meshLoader_0" dx="20" dy="17" dz="0" color="green" />
        </Node>
        <Node name="CylinderFEMTetra">
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" tolerance="0.000001" threshold="1e-5"/>
            <MechanicalObject dx="-10" />
            <UniformMass totalMass="15" />
            <CylinderGridTopology nx="5" ny="5" nz="20" length="35.56" radius="3.75" axis="0 1 0" />
            <BoxConstraint box="-14 -0.1 -4 -6 0.1 4" fixAll="0" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1116" poissonRatio="0.3" method="polar" />
        </Node>
        <Node name="CylinderFEM">
            <EulerImplicitSolver />
            <CGLinearSolver iterations="25" tolerance="0.000001" threshold="1e-5"/>
            <MechanicalObject />
            <UniformMass totalMass="15" />
            <CylinderGridTopology nx="5" ny="5" nz="20" length="35.56" radius="3.75" axis="0 1 0" />
            <BoxConstraint box="-4 -0.1 -4 4 0.1 4" fixAll="0" />
            <HexahedronFEMForceField name="FEM" youngModulus="1116" poissonRatio="0.3" method="large" />
        </Node>
        <Node name="CylinderSpring">
            <EulerImplicitSolver />
            <CGLinearSolver iterations="25" tolerance="0.000001" threshold="1e-5"/>
            <MechanicalObject dx="10" />
            <UniformMass totalMass="15" />
            <CylinderGridTopology nx="5" ny="5" nz="20" length="35.56" radius="3.75" axis="0 1 0" />
            <BoxConstraint box="6 -0.1 -4 14 0.1 4" fixAll="0" />
            <MeshSpringForceField name="FEM" stiffness="1000" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02", gravity="0 0 100")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showVisual")
       root.addObject('DefaultAnimationLoop', )

       reference = root.addChild('Reference')

       reference.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/truthcylinder1-bent.obj", scale="0.95", handleSeams="1")
       reference.addObject('OglModel', src="@meshLoader_0", dx="20", dy="17", dz="0", color="green")

       cylinder_fem_tetra = root.addChild('CylinderFEMTetra')

       cylinder_fem_tetra.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       cylinder_fem_tetra.addObject('CGLinearSolver', iterations="25", tolerance="0.000001", threshold="1e-5")
       cylinder_fem_tetra.addObject('MechanicalObject', dx="-10")
       cylinder_fem_tetra.addObject('UniformMass', totalMass="15")
       cylinder_fem_tetra.addObject('CylinderGridTopology', nx="5", ny="5", nz="20", length="35.56", radius="3.75", axis="0 1 0")
       cylinder_fem_tetra.addObject('BoxConstraint', box="-14 -0.1 -4 -6 0.1 4", fixAll="0")
       cylinder_fem_tetra.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.3", method="polar")

       cylinder_fem = root.addChild('CylinderFEM')

       cylinder_fem.addObject('EulerImplicitSolver', )
       cylinder_fem.addObject('CGLinearSolver', iterations="25", tolerance="0.000001", threshold="1e-5")
       cylinder_fem.addObject('MechanicalObject', )
       cylinder_fem.addObject('UniformMass', totalMass="15")
       cylinder_fem.addObject('CylinderGridTopology', nx="5", ny="5", nz="20", length="35.56", radius="3.75", axis="0 1 0")
       cylinder_fem.addObject('BoxConstraint', box="-4 -0.1 -4 4 0.1 4", fixAll="0")
       cylinder_fem.addObject('HexahedronFEMForceField', name="FEM", youngModulus="1116", poissonRatio="0.3", method="large")

       cylinder_spring = root.addChild('CylinderSpring')

       cylinder_spring.addObject('EulerImplicitSolver', )
       cylinder_spring.addObject('CGLinearSolver', iterations="25", tolerance="0.000001", threshold="1e-5")
       cylinder_spring.addObject('MechanicalObject', dx="10")
       cylinder_spring.addObject('UniformMass', totalMass="15")
       cylinder_spring.addObject('CylinderGridTopology', nx="5", ny="5", nz="20", length="35.56", radius="3.75", axis="0 1 0")
       cylinder_spring.addObject('BoxConstraint', box="6 -0.1 -4 14 0.1 4", fixAll="0")
       cylinder_spring.addObject('MeshSpringForceField', name="FEM", stiffness="1000")
    ```

