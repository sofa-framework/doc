<!-- generate_doc -->
# SparseGridRamificationTopology

Sparse grid in 3D (modified)


__Target__: Sofa.Component.Topology.Container.Grid

__namespace__: sofa::component::topology::container::grid

__parents__:

- SparseGridTopology

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
		<td>fillWeighted</td>
		<td>
Is quantity of matter inside a cell taken into account? (.5 for boundary, 1 for inside)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>onlyInsideCells</td>
		<td>
Select only inside cells (exclude boundary cells)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>n</td>
		<td>
grid resolution
		</td>
		<td>2 2 2</td>
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
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>cellWidth</td>
		<td>
if > 0 : dimension of each cell in the created grid
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nbVirtualFinerLevels</td>
		<td>
create virtual (not in the animation tree) finer sparse grids in order to dispose of finest information (usefull to compute better mechanical properties for example)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>dataResolution</td>
		<td>
Dimension of the voxel File
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>voxelSize</td>
		<td>
Dimension of one voxel
		</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>marchingCubeStep</td>
		<td>
Step of the Marching Cube algorithm
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>convolutionSize</td>
		<td>
Dimension of the convolution kernel to smooth the voxels. 0 if no smoothing is required.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>facets</td>
		<td>
Input mesh facets
		</td>
		<td></td>
	</tr>
	<tr>
		<td>finestConnectivity</td>
		<td>
Test for connectivity at the finest level? (more precise but slower by testing all intersections between the model mesh and the faces between boundary cubes)
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

SparseGridRamificationTopology.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 0 -9" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceFieldAndMass] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridRamificationTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showVisual showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.5" contactDistance="0.3" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="UniformC Rough">
            <SparseGridRamificationTopology n="5 2 2" fileTopology="mesh/c.obj" nbVirtualFinerLevels="3" finestConnectivity="0" />
            <EulerImplicitSolver rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="10" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject />
            <HexahedronFEMForceFieldAndMass youngModulus="100000" poissonRatio="0.3" method="large" density="3" updateStiffnessMatrix="false" printLog="0" />
            <BoxConstraint box="-16 -10 -3 -14 10 3" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/c.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="blue" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf">
                <MeshOBJLoader name="loader" filename="mesh/c.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel />
                <PointCollisionModel />
                <LineCollisionModel />
                <BarycentricMapping />
            </Node>
        </Node>
        <Node name="UniformC">
            <SparseGridRamificationTopology n="5 2 2" fileTopology="mesh/c.obj" nbVirtualFinerLevels="3" finestConnectivity="0" />
            <EulerImplicitSolver rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="10" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject dx="40" />
            <HexahedronFEMForceFieldAndMass youngModulus="100000" poissonRatio="0.3" method="large" density="3" updateStiffnessMatrix="false" printLog="0" />
            <BoxConstraint box="24 -10 -3 26 10 3" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/c.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="red" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf">
                <MeshOBJLoader name="loader" filename="mesh/c.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel />
                <PointCollisionModel />
                <LineCollisionModel />
                <BarycentricMapping />
            </Node>
        </Node>
        <Node name="UniformC and finestConnectivity">
            <SparseGridRamificationTopology n="5 3 3" fileTopology="mesh/c.obj" nbVirtualFinerLevels="0" finestConnectivity="1" />
            <EulerImplicitSolver rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="10" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject dx="80" />
            <HexahedronFEMForceFieldAndMass youngModulus="100000" poissonRatio="0.3" method="large" density="3" updateStiffnessMatrix="false" printLog="0" />
            <BoxConstraint box="64 -10 -3 66 10 3" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_2" filename="mesh/c.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="yellow" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf">
                <MeshOBJLoader name="loader" filename="mesh/c.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel />
                <PointCollisionModel />
                <LineCollisionModel />
                <BarycentricMapping />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 -9", dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showForceFields")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.3")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       uniform_c__rough = root.addChild('UniformC Rough')

       uniform_c__rough.addObject('SparseGridRamificationTopology', n="5 2 2", fileTopology="mesh/c.obj", nbVirtualFinerLevels="3", finestConnectivity="0")
       uniform_c__rough.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       uniform_c__rough.addObject('CGLinearSolver', iterations="10", tolerance="1e-5", threshold="1e-5")
       uniform_c__rough.addObject('MechanicalObject', )
       uniform_c__rough.addObject('HexahedronFEMForceFieldAndMass', youngModulus="100000", poissonRatio="0.3", method="large", density="3", updateStiffnessMatrix="false", printLog="0")
       uniform_c__rough.addObject('BoxConstraint', box="-16 -10 -3 -14 10 3")

       visu = UniformC Rough.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/c.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="blue")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf = UniformC Rough.addChild('Surf')

       surf.addObject('MeshOBJLoader', name="loader", filename="mesh/c.obj")
       surf.addObject('MeshTopology', src="@loader")
       surf.addObject('MechanicalObject', src="@loader")
       surf.addObject('TriangleCollisionModel', )
       surf.addObject('PointCollisionModel', )
       surf.addObject('LineCollisionModel', )
       surf.addObject('BarycentricMapping', )

       uniform_c = root.addChild('UniformC')

       uniform_c.addObject('SparseGridRamificationTopology', n="5 2 2", fileTopology="mesh/c.obj", nbVirtualFinerLevels="3", finestConnectivity="0")
       uniform_c.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       uniform_c.addObject('CGLinearSolver', iterations="10", tolerance="1e-5", threshold="1e-5")
       uniform_c.addObject('MechanicalObject', dx="40")
       uniform_c.addObject('HexahedronFEMForceFieldAndMass', youngModulus="100000", poissonRatio="0.3", method="large", density="3", updateStiffnessMatrix="false", printLog="0")
       uniform_c.addObject('BoxConstraint', box="24 -10 -3 26 10 3")

       visu = UniformC.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/c.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf = UniformC.addChild('Surf')

       surf.addObject('MeshOBJLoader', name="loader", filename="mesh/c.obj")
       surf.addObject('MeshTopology', src="@loader")
       surf.addObject('MechanicalObject', src="@loader")
       surf.addObject('TriangleCollisionModel', )
       surf.addObject('PointCollisionModel', )
       surf.addObject('LineCollisionModel', )
       surf.addObject('BarycentricMapping', )

       uniform_c_and_finest_connectivity = root.addChild('UniformC and finestConnectivity')

       uniform_c_and_finest_connectivity.addObject('SparseGridRamificationTopology', n="5 3 3", fileTopology="mesh/c.obj", nbVirtualFinerLevels="0", finestConnectivity="1")
       uniform_c_and_finest_connectivity.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       uniform_c_and_finest_connectivity.addObject('CGLinearSolver', iterations="10", tolerance="1e-5", threshold="1e-5")
       uniform_c_and_finest_connectivity.addObject('MechanicalObject', dx="80")
       uniform_c_and_finest_connectivity.addObject('HexahedronFEMForceFieldAndMass', youngModulus="100000", poissonRatio="0.3", method="large", density="3", updateStiffnessMatrix="false", printLog="0")
       uniform_c_and_finest_connectivity.addObject('BoxConstraint', box="64 -10 -3 66 10 3")

       visu = UniformC and finestConnectivity.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/c.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="yellow")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf = UniformC and finestConnectivity.addChild('Surf')

       surf.addObject('MeshOBJLoader', name="loader", filename="mesh/c.obj")
       surf.addObject('MeshTopology', src="@loader")
       surf.addObject('MechanicalObject', src="@loader")
       surf.addObject('TriangleCollisionModel', )
       surf.addObject('PointCollisionModel', )
       surf.addObject('LineCollisionModel', )
       surf.addObject('BarycentricMapping', )
    ```

