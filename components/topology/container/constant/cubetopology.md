<!-- generate_doc -->
# CubeTopology

Surface topology of a cube in 3D (points, edges and quads).


__Target__: Sofa.Component.Topology.Container.Constant

__namespace__: sofa::component::topology::container::constant

__parents__:

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
		<td>computeAllBuffers</td>
		<td>
Option to compute all crossed topology buffers at init. False by default
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nx</td>
		<td>
x grid resolution
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>ny</td>
		<td>
y grid resolution
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nz</td>
		<td>
z grid resolution
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>internalPoints</td>
		<td>
include internal points (allow a one-to-one mapping between points from RegularGridTopology and CubeTopology)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>splitNormals</td>
		<td>
split corner points to have planar normals
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>min</td>
		<td>
Min
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>max</td>
		<td>
Max
		</td>
		<td>1 1 1</td>
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

CubeTopology.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangleFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [CubeTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Quad2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection/>
        <DefaultAnimationLoop/>
    
        <Node name="Cubes" >
    	<VisualStyle displayFlags="showForceFields" />
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <CubeTopology internalPoints="0" splitNormals="1" name="cubeTopo" nx="3" ny="3" nz="5" min="-0.015 -0.015 -0.075" max="0.015 0.015 0.075" />
            <Node name="topoTriangle" >
                <include href="Objects/TriangleSetTopology.xml" src="@../cubeTopo"/>
                <Quad2TriangleTopologicalMapping input="@../cubeTopo" output="@Container"/>
                <MechanicalObject name="dofs" printLog="1" position="@../cubeTopo.position"/>
                <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64" />
                <TriangleFEMForceField name="FEM1" youngModulus="500" poissonRatio="0.3" method="large" />
                <TriangularBendingSprings name="FEM-Bend" stiffness="3000" damping="1.0"/>
                <UniformMass vertexMass="0.1" />
                
                <Node name="Visu">
                    <OglModel name="Visual" color="red" />
                    <IdentityMapping input="@../dofs" output="@Visual" />
                </Node>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
       root.addObject('DiscreteIntersection', )
       root.addObject('DefaultAnimationLoop', )

       cubes = root.addChild('Cubes')

       cubes.addObject('VisualStyle', displayFlags="showForceFields")
       cubes.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       cubes.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       cubes.addObject('CubeTopology', internalPoints="0", splitNormals="1", name="cubeTopo", nx="3", ny="3", nz="5", min="-0.015 -0.015 -0.075", max="0.015 0.015 0.075")

       topo_triangle = Cubes.addChild('topoTriangle')

       topo_triangle.addObject('include', href="Objects/TriangleSetTopology.xml", src="@../cubeTopo")
       topo_triangle.addObject('Quad2TriangleTopologicalMapping', input="@../cubeTopo", output="@Container")
       topo_triangle.addObject('MechanicalObject', name="dofs", printLog="1", position="@../cubeTopo.position")
       topo_triangle.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")
       topo_triangle.addObject('TriangleFEMForceField', name="FEM1", youngModulus="500", poissonRatio="0.3", method="large")
       topo_triangle.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="3000", damping="1.0")
       topo_triangle.addObject('UniformMass', vertexMass="0.1")

       visu = topoTriangle.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="red")
       visu.addObject('IdentityMapping', input="@../dofs", output="@Visual")
    ```

