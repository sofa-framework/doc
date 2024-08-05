# SparseGridTopology

Sparse grid in 3D


__Target__: `Sofa.Component.Topology.Container.Grid`

__namespace__: `#!c++ sofa::component::topology::container::grid`

__parents__: 

- `#!c++ MeshTopology`

__categories__: 

- Topology

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

Component/Topology/Container/Grid/SparseGridTopology.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <!-- SparseGrid examples -->
    <Node name="root" dt="0.02" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader SphereLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields showVisual" />
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="Response"/>
        <DiscreteIntersection/>
        
        <MeshOBJLoader name="loader" filename="mesh/dragon.obj" />
        
        <Node name="DragonCoarse">
            <SparseGridTopology n="6 5 4" fileTopology="mesh/dragon.obj" />
            <EulerImplicitSolver rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject />
            <UniformMass vertexMass="0.5" />
            <MeshSpringForceField name="Springs" stiffness="500" damping="10" />
            <BoxConstraint box="10 -10 -6 12 10 6" />
            <Node name="Visu">
                <OglModel name="Visual" src="@../../loader" color="blue" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf">
    	    <SphereLoader filename="mesh/dragon.sph" />
                <MechanicalObject position="@[-1].position" />
                <SphereCollisionModel listRadius="@[-2].listRadius" />
                <BarycentricMapping />
            </Node>
        </Node>
        <Node name="DragonMiddle">
            <SparseGridTopology n="12 9 6" fileTopology="mesh/dragon.obj" />
            <EulerImplicitSolver rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject dz="15" />
            <UniformMass vertexMass="0.5" />
            <MeshSpringForceField name="Springs" stiffness="500" damping="10" />
            <BoxConstraint box="10 -10 10 12 10 22" />
            <Node name="Visu">
                <OglModel name="Visual" src="@../../loader" color="white" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf">
    	    <SphereLoader filename="mesh/dragon.sph" />
                <MechanicalObject position="@[-1].position" />
                <SphereCollisionModel listRadius="@[-2].listRadius" />
                <BarycentricMapping />
            </Node>
        </Node>
        <Node name="DragonFine">
            <SparseGridTopology n="25 20 9" fileTopology="mesh/dragon.obj" />
            <EulerImplicitSolver rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="100" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject dz="30" />
            <UniformMass vertexMass="0.5" />
            <MeshSpringForceField name="Springs" stiffness="500" damping="10" />
            <BoxConstraint box="10 -10 26 12 10 38" />
            <Node name="Visu">
                <OglModel name="Visual" src="@../../loader" color="red" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf">
    	    <SphereLoader filename="mesh/dragon.sph" />
                <MechanicalObject position="@[-1].position" />
                <SphereCollisionModel listRadius="@[-2].listRadius" />
                <BarycentricMapping />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02", gravity="0 -9 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showVisual")
        root.addObject('DefaultAnimationLoop')
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', name="Response")
        root.addObject('DiscreteIntersection')
        root.addObject('MeshOBJLoader', name="loader", filename="mesh/dragon.obj")

        DragonCoarse = root.addChild('DragonCoarse')
        DragonCoarse.addObject('SparseGridTopology', n="6 5 4", fileTopology="mesh/dragon.obj")
        DragonCoarse.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        DragonCoarse.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
        DragonCoarse.addObject('MechanicalObject')
        DragonCoarse.addObject('UniformMass', vertexMass="0.5")
        DragonCoarse.addObject('MeshSpringForceField', name="Springs", stiffness="500", damping="10")
        DragonCoarse.addObject('BoxConstraint', box="10 -10 -6 12 10 6")

        Visu = DragonCoarse.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", src="@../../loader", color="blue")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf = DragonCoarse.addChild('Surf')
        Surf.addObject('SphereLoader', filename="mesh/dragon.sph")
        Surf.addObject('MechanicalObject', position="@[-1].position")
        Surf.addObject('SphereCollisionModel', listRadius="@[-2].listRadius")
        Surf.addObject('BarycentricMapping')

        DragonMiddle = root.addChild('DragonMiddle')
        DragonMiddle.addObject('SparseGridTopology', n="12 9 6", fileTopology="mesh/dragon.obj")
        DragonMiddle.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        DragonMiddle.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
        DragonMiddle.addObject('MechanicalObject', dz="15")
        DragonMiddle.addObject('UniformMass', vertexMass="0.5")
        DragonMiddle.addObject('MeshSpringForceField', name="Springs", stiffness="500", damping="10")
        DragonMiddle.addObject('BoxConstraint', box="10 -10 10 12 10 22")

        Visu = DragonMiddle.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", src="@../../loader", color="white")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf = DragonMiddle.addChild('Surf')
        Surf.addObject('SphereLoader', filename="mesh/dragon.sph")
        Surf.addObject('MechanicalObject', position="@[-1].position")
        Surf.addObject('SphereCollisionModel', listRadius="@[-2].listRadius")
        Surf.addObject('BarycentricMapping')

        DragonFine = root.addChild('DragonFine')
        DragonFine.addObject('SparseGridTopology', n="25 20 9", fileTopology="mesh/dragon.obj")
        DragonFine.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        DragonFine.addObject('CGLinearSolver', iterations="100", tolerance="1e-5", threshold="1e-5")
        DragonFine.addObject('MechanicalObject', dz="30")
        DragonFine.addObject('UniformMass', vertexMass="0.5")
        DragonFine.addObject('MeshSpringForceField', name="Springs", stiffness="500", damping="10")
        DragonFine.addObject('BoxConstraint', box="10 -10 26 12 10 38")

        Visu = DragonFine.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", src="@../../loader", color="red")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf = DragonFine.addChild('Surf')
        Surf.addObject('SphereLoader', filename="mesh/dragon.sph")
        Surf.addObject('MechanicalObject', position="@[-1].position")
        Surf.addObject('SphereCollisionModel', listRadius="@[-2].listRadius")
        Surf.addObject('BarycentricMapping')
    ```

