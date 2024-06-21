# SparseGridMultipleTopology

Sparse grid in 3D


__Target__: `Sofa.Component.Topology.Container.Grid`

__namespace__: `#!c++ sofa::component::topology::container::grid`

__parents__: 

- `#!c++ SparseGridRamificationTopology`

Data: 

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
if &gt; 0 : dimension of each cell in the created grid
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
		<td>fileTopologies</td>
		<td>
All topology filenames
</td>
		<td>[]</td>
	</tr>
	<tr>
		<td>stiffnessCoefs</td>
		<td>
A stiffness coefficient for each topology filename
</td>
		<td></td>
	</tr>
	<tr>
		<td>massCoefs</td>
		<td>
A mass coefficient for each topology filename
</td>
		<td></td>
	</tr>
	<tr>
		<td>computeRamifications</td>
		<td>
Are ramifications wanted?
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>erasePreviousCoef</td>
		<td>
Does a new stiffness/mass coefficient replace the previous or blend half/half with it?
</td>
		<td>0</td>
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

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



## Examples

Component/Topology/Container/Grid/SparseGridMultipleTopology.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 0 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridMultipleTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.5" contactDistance="0.3" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <DefaultAnimationLoop/>
        
        <Node name="frog with several stiffnesses">
            <SparseGridMultipleTopology n="9 9 7" fileTopology="mesh/frog_body.obj" fileTopologies="mesh/frog_body.obj mesh/frog_eyes.obj mesh/frog_eyebrows.obj mesh/frog_lips.obj" stiffnessCoefs="10 100 100 .2" massCoefs="1 1 1 1" nbVirtualFinerLevels="1" />
            <!-- body=soft, lips=very soft, eyes=very stiff-->
            <!-- the order is important: included elements must appear after (lips is included in boby so it appears after)-->
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="10" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject />
            <UniformMass vertexMass="1" />
            <HexahedronFEMForceField youngModulus="3000" poissonRatio="0.3" method="large" updateStiffnessMatrix="false" printLog="0" />
            <Node name="Visu1">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/frog_body.obj" handleSeams="1" />
                <OglModel name="VisualBody" src="@meshLoader_0" normals="0" color="0.17 0.70 0.05" />
                <BarycentricMapping input="@.." output="@VisualBody" />
            </Node>
            <Node name="Visu2">
                <MeshOBJLoader name="meshLoader_2" filename="mesh/frog_eyes.obj" handleSeams="1" />
                <OglModel name="VisualEyes" src="@meshLoader_2" normals="0" color="0.04 0.19 0.52" />
                <BarycentricMapping input="@.." output="@VisualEyes" />
            </Node>
            <Node name="Visu3">
                <MeshOBJLoader name="meshLoader_3" filename="mesh/frog_eyebrows.obj" handleSeams="1" />
                <OglModel name="VisualEyebrows" src="@meshLoader_3" normals="0" color="0.44 0.43 0.00" />
                <BarycentricMapping input="@.." output="@VisualEyebrows" />
            </Node>
            <Node name="Visu4">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/frog_lips.obj" handleSeams="1" />
                <OglModel name="VisualLips" src="@meshLoader_1" normals="0" color="0.47 0.25 0.03" />
                <BarycentricMapping input="@.." output="@VisualLips" />
            </Node>
            <Node name="Surf">
                <MeshOBJLoader name="loader" filename="mesh/frog-push25.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <BarycentricMapping />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 0 0", dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.3")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
        root.addObject('DefaultAnimationLoop')

        frog with several stiffnesses = root.addChild('frog with several stiffnesses')
        frog with several stiffnesses.addObject('SparseGridMultipleTopology', n="9 9 7", fileTopology="mesh/frog_body.obj", fileTopologies="mesh/frog_body.obj mesh/frog_eyes.obj mesh/frog_eyebrows.obj mesh/frog_lips.obj", stiffnessCoefs="10 100 100 .2", massCoefs="1 1 1 1", nbVirtualFinerLevels="1")
        frog with several stiffnesses.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        frog with several stiffnesses.addObject('CGLinearSolver', iterations="10", tolerance="1e-5", threshold="1e-5")
        frog with several stiffnesses.addObject('MechanicalObject')
        frog with several stiffnesses.addObject('UniformMass', vertexMass="1")
        frog with several stiffnesses.addObject('HexahedronFEMForceField', youngModulus="3000", poissonRatio="0.3", method="large", updateStiffnessMatrix="false", printLog="0")

        Visu1 = frog with several stiffnesses.addChild('Visu1')
        Visu1.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/frog_body.obj", handleSeams="1")
        Visu1.addObject('OglModel', name="VisualBody", src="@meshLoader_0", normals="0", color="0.17 0.70 0.05")
        Visu1.addObject('BarycentricMapping', input="@..", output="@VisualBody")

        Visu2 = frog with several stiffnesses.addChild('Visu2')
        Visu2.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/frog_eyes.obj", handleSeams="1")
        Visu2.addObject('OglModel', name="VisualEyes", src="@meshLoader_2", normals="0", color="0.04 0.19 0.52")
        Visu2.addObject('BarycentricMapping', input="@..", output="@VisualEyes")

        Visu3 = frog with several stiffnesses.addChild('Visu3')
        Visu3.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/frog_eyebrows.obj", handleSeams="1")
        Visu3.addObject('OglModel', name="VisualEyebrows", src="@meshLoader_3", normals="0", color="0.44 0.43 0.00")
        Visu3.addObject('BarycentricMapping', input="@..", output="@VisualEyebrows")

        Visu4 = frog with several stiffnesses.addChild('Visu4')
        Visu4.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/frog_lips.obj", handleSeams="1")
        Visu4.addObject('OglModel', name="VisualLips", src="@meshLoader_1", normals="0", color="0.47 0.25 0.03")
        Visu4.addObject('BarycentricMapping', input="@..", output="@VisualLips")

        Surf = frog with several stiffnesses.addChild('Surf')
        Surf.addObject('MeshOBJLoader', name="loader", filename="mesh/frog-push25.obj")
        Surf.addObject('MeshTopology', src="@loader")
        Surf.addObject('MechanicalObject', src="@loader")
        Surf.addObject('TriangleCollisionModel')
        Surf.addObject('LineCollisionModel')
        Surf.addObject('PointCollisionModel')
        Surf.addObject('BarycentricMapping')
    ```

