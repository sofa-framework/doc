# MeshTetraStuffing

Create a tetrahedral volume mesh from a surface, using the algorithm from F. Labelle and J.R. Shewchuk, "Isosurface Stuffing: Fast Tetrahedral Meshes with Good Dihedral Angles", SIGGRAPH 2007.


__Target__: `Sofa.Component.Engine.Generate`

__namespace__: `#!c++ sofa::component::engine::generate`

__parents__: 

- `#!c++ BaseObject`

__categories__: 

- _Miscellaneous

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
		<td>vbbox</td>
		<td>
BBox to restrict the volume to
</td>
		<td></td>
	</tr>
	<tr>
		<td>size</td>
		<td>
Size of the generate tetrahedra. If negative, number of grid cells in the largest bbox dimension
</td>
		<td>-8</td>
	</tr>
	<tr>
		<td>outputPoints</td>
		<td>
Output volume mesh points
</td>
		<td></td>
	</tr>
	<tr>
		<td>outputTetrahedra</td>
		<td>
Output volume mesh tetrahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>inputPoints</td>
		<td>
Input surface mesh points
</td>
		<td></td>
	</tr>
	<tr>
		<td>inputTriangles</td>
		<td>
Input surface mesh triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>inputQuads</td>
		<td>
Input surface mesh quads
</td>
		<td></td>
	</tr>
	<tr>
		<td>alphaLong</td>
		<td>
Minimum alpha values on long edges when snapping points
</td>
		<td>0.24999</td>
	</tr>
	<tr>
		<td>alphaShort</td>
		<td>
Minimum alpha values on short edges when snapping points
</td>
		<td>0.42978</td>
	</tr>
	<tr>
		<td>snapPoints</td>
		<td>
Snap points to the surface if intersections on edges are closed to given alpha values
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>splitTetrahedra</td>
		<td>
Split tetrahedra crossing the surface
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>draw</td>
		<td>
Activate rendering of internal datasets
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

Component/Engine/Generate/MeshTetraStuffing.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node>
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [MeshTetraStuffing] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping Mesh2PointTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [PointSetTopologyContainer PointSetTopologyModifier TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <!--
        <CollisionPipeline verbose="0" name="CollisionPipeline"/>
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <DiscreteIntersection/>
        <CollisionResponse response="PenalityContactForceField" name="collision response"/>
    -->
        <DefaultAnimationLoop/>    
        <VisualStyle displayFlags="showForceFields" />
        <Node name="input">
            <MeshTopology name="surface" filename="mesh/liver-smooth.obj" />
            <MeshTetraStuffing name="stuffing" snapPoints="true" splitTetras="true" draw="true" size="0.7" alphaLong="0.3" alphaShort="0.4" inputPoints="@surface.points" inputTriangles="@surface.triangles" />
        </Node>
        <Node activated="1" name="output">
            <EulerImplicitSolver name="odesolver"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="10" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <TetrahedronSetTopologyContainer name="volume" points="@../input/stuffing.outputPoints" tetras="@../input/stuffing.outputTetras" />
            <MechanicalObject />
            <!-- Algorithms: used in DiagonalMass to compute the mass -->
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" />
            <DiagonalMass massDensity="1" name="computed using mass density" />
            <TetrahedralCorotationalFEMForceField name="FEM" youngModulus="3000" poissonRatio="0.3" method="large" />
            <BoxConstraint box="-6 0 -2 -2 1.5 3" />
            <!--<SphereCollisionModel radius="0.4" />-->
            <!--
            <Node name="Surface">
    	  <include href="Objects/TriangleSetTopology.xml" />
    	  <Tetra2TriangleTopologicalMapping input="@../volume" output="@Container"/>
              <TriangularFEMForceField name="FEM" youngModulus="60" poissonRatio="0.3" method="large" /> 
            </Node>
    -->
            <Node name="VM">
                <MeshOBJLoader name='myLoader' filename='mesh/liver-smooth.obj'/>  
                <OglModel name="visual" src="@myLoader" />
                <BarycentricMapping output="@visual" />
            </Node>
            <Node name="Circumcenters">
                <PointSetTopologyContainer name="Container2" />
                <PointSetTopologyModifier />
                <Mesh2PointTopologicalMapping input="@volume" output="@Container2" tetraBaryCoords="0.25 0.25 0.25" />
                <MechanicalObject />
                <!--<BarycentricMapping />-->
                <!--<CircumcenterMapping/>-->
                <!--<SphereCollisionModel radius="0.1" />-->
            </Node>
        </Node>
    <!--
        <Node activated="0" name="output-gpu">
            <EulerImplicitSolver name="odesolver" />
            <CGLinearSolver iterations="10" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshTopology name="volume" points="@../input/stuffing.outputPoints" tetras="@../input/stuffing.outputTetras" />
            <MechanicalObject template="CudaVec3f" />
            <UniformMass totalMass="5" name="mass" />
            <TetrahedronFEMForceField name="FEM" youngModulus="3000" poissonRatio="0.3" method="large" />
            <BoxConstraint box="-6 0 -2 -2 1.5 3" />
            <Node name="VM">
                <OglModel name="visual" filename="mesh/liver-smooth.obj" />
                <BarycentricMapping output="@visual" />
            </Node>
        </Node>
    -->
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        rootNode = rootNode.addChild('rootNode')
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        rootNode.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        rootNode.addObject('DefaultAnimationLoop')
        rootNode.addObject('VisualStyle', displayFlags="showForceFields")

        input = rootNode.addChild('input')
        input.addObject('MeshTopology', name="surface", filename="mesh/liver-smooth.obj")
        input.addObject('MeshTetraStuffing', name="stuffing", snapPoints="true", splitTetras="true", draw="true", size="0.7", alphaLong="0.3", alphaShort="0.4", inputPoints="@surface.points", inputTriangles="@surface.triangles")

        output = rootNode.addChild('output', activated="1")
        output.addObject('EulerImplicitSolver', name="odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        output.addObject('CGLinearSolver', iterations="10", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        output.addObject('TetrahedronSetTopologyContainer', name="volume", points="@../input/stuffing.outputPoints", tetras="@../input/stuffing.outputTetras")
        output.addObject('MechanicalObject')
        output.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo")
        output.addObject('DiagonalMass', massDensity="1", name="computed using mass density")
        output.addObject('TetrahedralCorotationalFEMForceField', name="FEM", youngModulus="3000", poissonRatio="0.3", method="large")
        output.addObject('BoxConstraint', box="-6 0 -2 -2 1.5 3")

        VM = output.addChild('VM')
        VM.addObject('MeshOBJLoader', name="myLoader", filename="mesh/liver-smooth.obj")
        VM.addObject('OglModel', name="visual", src="@myLoader")
        VM.addObject('BarycentricMapping', output="@visual")

        Circumcenters = output.addChild('Circumcenters')
        Circumcenters.addObject('PointSetTopologyContainer', name="Container2")
        Circumcenters.addObject('PointSetTopologyModifier')
        Circumcenters.addObject('Mesh2PointTopologicalMapping', input="@volume", output="@Container2", tetraBaryCoords="0.25 0.25 0.25")
        Circumcenters.addObject('MechanicalObject')
    ```

