# RegularGridTopology

Regular grid in 3D


__Target__: `Sofa.Component.Topology.Container.Grid`

__namespace__: `#!c++ sofa::component::topology::container::grid`

__parents__: 

- `#!c++ GridTopology`

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
		<td>min</td>
		<td>
Min end of the diagonal
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>max</td>
		<td>
Max end of the diagonal
</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>p0</td>
		<td>
Offset all the grid points
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>cellWidth</td>
		<td>
if &gt; 0 : dimension of each cell in the created grid. Otherwise, the cell size is computed based on min, max, and resolution n.
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

Component/Topology/Container/Grid/RegularGridTopology_dimension.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 -9.81 0" dt="0.01">
        <Node name="RequiredPlugins" >
            <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
            <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
            <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
            <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField TriangularFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [RegularGridSpringForceField TriangularBendingSprings] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [QuadSetGeometryAlgorithms QuadSetTopologyContainer QuadSetTopologyModifier] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2QuadTopologicalMapping] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        </Node>
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <DefaultAnimationLoop/>
    
        <CollisionPipeline name="default21" verbose="0" />
        <DefaultAnimationLoop/>
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="default22" response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
    
        <EulerImplicitSolver name="cg_odesolver" printLog="0"  rayleighStiffness="0.1" rayleighMass="0.1" />
        <CGLinearSolver template="GraphScattered" name="linear solver" iterations="25" tolerance="1e-09" threshold="1e-09" />
    
    
        <Node name="Cube" gravity="0 -9.81 0">
            <RegularGridTopology name="grid" n="6 6 6" min="-10 -10 -10" max="10 10 10" p0="-30 -10 -10" computeHexaList="1"/>
            <MechanicalObject template="Vec3" name="Hexa" />
            <UniformMass template="Vec3" name="default25" vertexMass="10" />
            <HexahedronFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="500" />
            <BoxROI template="Vec3" name="box_roi" box="-31 9 -11 -9 11 11" drawSize="0" />
            <FixedProjectiveConstraint template="Vec3" name="default27" indices="@box_roi.indices" drawSize="0" />
    
            <Node name="Q">
                <QuadSetTopologyContainer  name="Container" />
                <QuadSetTopologyModifier   name="Modifier" />
                <QuadSetGeometryAlgorithms name="GeomAlgo"   template="Vec3" />
                <Hexa2QuadTopologicalMapping input="@../grid" output="@Container" />
                <TriangleCollisionModel />
                <Node name="Visu">
                    <OglModel name="Visual" color="blue" quads="@../Container.quads" />
                    <IdentityMapping input="@../../Hexa" output="@Visual" />
                </Node>
            </Node>
        </Node>
    
    
        <Node name="Square" gravity="0 -9.81 0">
            <RegularGridTopology name="grid" n="6 1 6" min="-10 -10 -10" max="10 10 10" p0="-6 10 -10" computeHexaList="0"/>
            <MechanicalObject template="Vec3" name="Tri" />
            <UniformMass template="Vec3" name="default25" vertexMass="10" />
            <TriangularFEMForceField name="FEM" youngModulus="600" poissonRatio="0.3" method="large" />
            <TriangularBendingSprings name="FEM-Bend" stiffness="300" damping="1.0" />
            <BoxROI template="Vec3" name="box_roi" box="-7 9 -11 17 11 -9" drawBoxes="0" />
            <FixedProjectiveConstraint template="Vec3" name="default27" indices="@box_roi.indices" drawSize="0" />
    
            <TriangleCollisionModel />
            <Node name="Visu">
                <OglModel name="Visual" color="blue" triangles="@../grid.triangles" />
                <IdentityMapping input="@../Tri" output="@Visual" />
            </Node>
        </Node>
    
    
        <Node name="Line" gravity="0 -9.81 0">
            <RegularGridTopology name="grid" n="1 1 6" min="-10 -10 -10" max="10 10 10" p0="18 10 -10" computeHexaList="0"/>
            <MechanicalObject template="Vec3" name="Edge" />
            <UniformMass template="Vec3" name="default25" vertexMass="10" />
    
            <RegularGridSpringForceField name="Springs" stiffness="300" damping="2" />
            <BoxROI template="Vec3" name="box_roi" box="17 9 -11 20 11 -9" drawBoxes="0" />
            <FixedProjectiveConstraint template="Vec3" name="default27" indices="@box_roi.indices" drawSize="0" />
    
            <Node name="Visu">
                <OglModel name="Visual" color="white" edges="@../grid.edges" />
                <IdentityMapping input="@../Edge" output="@Visual" />
            </Node>
        </Node>
    
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9.81 0", dt="0.01")

        RequiredPlugins = root.addChild('RequiredPlugins')
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        RequiredPlugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
        root.addObject('DefaultAnimationLoop')
        root.addObject('CollisionPipeline', name="default21", verbose="0")
        root.addObject('DefaultAnimationLoop')
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', name="default22", response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
        root.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1")
        root.addObject('CGLinearSolver', template="GraphScattered", name="linear solver", iterations="25", tolerance="1e-09", threshold="1e-09")

        Cube = root.addChild('Cube', gravity="0 -9.81 0")
        Cube.addObject('RegularGridTopology', name="grid", n="6 6 6", min="-10 -10 -10", max="10 10 10", p0="-30 -10 -10", computeHexaList="1")
        Cube.addObject('MechanicalObject', template="Vec3", name="Hexa")
        Cube.addObject('UniformMass', template="Vec3", name="default25", vertexMass="10")
        Cube.addObject('HexahedronFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="500")
        Cube.addObject('BoxROI', template="Vec3", name="box_roi", box="-31 9 -11 -9 11 11", drawSize="0")
        Cube.addObject('FixedProjectiveConstraint', template="Vec3", name="default27", indices="@box_roi.indices", drawSize="0")

        Q = Cube.addChild('Q')
        Q.addObject('QuadSetTopologyContainer', name="Container")
        Q.addObject('QuadSetTopologyModifier', name="Modifier")
        Q.addObject('QuadSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        Q.addObject('Hexa2QuadTopologicalMapping', input="@../grid", output="@Container")
        Q.addObject('TriangleCollisionModel')

        Visu = Q.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="blue", quads="@../Container.quads")
        Visu.addObject('IdentityMapping', input="@../../Hexa", output="@Visual")

        Square = root.addChild('Square', gravity="0 -9.81 0")
        Square.addObject('RegularGridTopology', name="grid", n="6 1 6", min="-10 -10 -10", max="10 10 10", p0="-6 10 -10", computeHexaList="0")
        Square.addObject('MechanicalObject', template="Vec3", name="Tri")
        Square.addObject('UniformMass', template="Vec3", name="default25", vertexMass="10")
        Square.addObject('TriangularFEMForceField', name="FEM", youngModulus="600", poissonRatio="0.3", method="large")
        Square.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="300", damping="1.0")
        Square.addObject('BoxROI', template="Vec3", name="box_roi", box="-7 9 -11 17 11 -9", drawBoxes="0")
        Square.addObject('FixedProjectiveConstraint', template="Vec3", name="default27", indices="@box_roi.indices", drawSize="0")
        Square.addObject('TriangleCollisionModel')

        Visu = Square.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="blue", triangles="@../grid.triangles")
        Visu.addObject('IdentityMapping', input="@../Tri", output="@Visual")

        Line = root.addChild('Line', gravity="0 -9.81 0")
        Line.addObject('RegularGridTopology', name="grid", n="1 1 6", min="-10 -10 -10", max="10 10 10", p0="18 10 -10", computeHexaList="0")
        Line.addObject('MechanicalObject', template="Vec3", name="Edge")
        Line.addObject('UniformMass', template="Vec3", name="default25", vertexMass="10")
        Line.addObject('RegularGridSpringForceField', name="Springs", stiffness="300", damping="2")
        Line.addObject('BoxROI', template="Vec3", name="box_roi", box="17 9 -11 20 11 -9", drawBoxes="0")
        Line.addObject('FixedProjectiveConstraint', template="Vec3", name="default27", indices="@box_roi.indices", drawSize="0")

        Visu = Line.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="white", edges="@../grid.edges")
        Visu.addObject('IdentityMapping', input="@../Edge", output="@Visual")
    ```

Component/Topology/Container/Grid/RegularGridTopology.scn

=== "XML"

    ```xml
    <!-- RegularGrid examples -->
    <Node name="root" dt="0.02">
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
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [RegularGridSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields showVisual" />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <DiscreteIntersection/>
        <DefaultAnimationLoop/>
        
        <Node name="LiverFFD-lowres">
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="100" tolerance="1e-7" threshold="1e-7"/>
            <MechanicalObject />
            <UniformMass totalMass="100.0" />
            <RegularGridTopology nx="4" ny="3" nz="3" xmin="-10.25" xmax="-3.25" ymin="0.25" ymax="5.25" zmin="-2" zmax="3" />
            <BoxConstraint box="-8.5 0 -2.5 -5 3 2" />
            <RegularGridSpringForceField name="Springs" stiffness="400" damping="4" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/liver-smooth.obj" translation="-5 0 0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="red" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Collision Surface">
    	    <SphereLoader filename="mesh/liver.sph" />
                <MechanicalObject position="@[-1].position" translation="-5 0 0" />
                <SphereCollisionModel name="Surf" listRadius="@[-2].listRadius" />
                <BarycentricMapping input="@.." output="@." />
            </Node>
        </Node>
        <Node name="LiverFFD-hires">
            <EulerImplicitSolver />
            <CGLinearSolver iterations="100" tolerance="1e-7" threshold="1e-7"/>
            <MechanicalObject />
            <UniformMass totalMass="100.0" />
            <RegularGridTopology nx="8" ny="6" nz="6" xmin="-0.25" xmax="7.25" ymin="0.25" ymax="5.25" zmin="-2" zmax="3" />
            <BoxConstraint box="2.5 0 -2.5 5 3 2" />
            <RegularGridSpringForceField name="Springs" stiffness="100" damping="4" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/liver-smooth.obj" translation="5 0 0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_1" color="red" />
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Collision Surface">
    	    <SphereLoader filename="mesh/liver.sph" />
                <MechanicalObject position="@[-1].position" translation="5 0 0" />
                <SphereCollisionModel name="Surf" listRadius="@[-2].listRadius" />
                <BarycentricMapping input="@.." output="@." />
           </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")
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
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('DiscreteIntersection')
        root.addObject('DefaultAnimationLoop')

        LiverFFD-lowres = root.addChild('LiverFFD-lowres')
        LiverFFD-lowres.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
        LiverFFD-lowres.addObject('CGLinearSolver', iterations="100", tolerance="1e-7", threshold="1e-7")
        LiverFFD-lowres.addObject('MechanicalObject')
        LiverFFD-lowres.addObject('UniformMass', totalMass="100.0")
        LiverFFD-lowres.addObject('RegularGridTopology', nx="4", ny="3", nz="3", xmin="-10.25", xmax="-3.25", ymin="0.25", ymax="5.25", zmin="-2", zmax="3")
        LiverFFD-lowres.addObject('BoxConstraint', box="-8.5 0 -2.5 -5 3 2")
        LiverFFD-lowres.addObject('RegularGridSpringForceField', name="Springs", stiffness="400", damping="4")

        Visu = LiverFFD-lowres.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver-smooth.obj", translation="-5 0 0", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Collision Surface = LiverFFD-lowres.addChild('Collision Surface')
        Collision Surface.addObject('SphereLoader', filename="mesh/liver.sph")
        Collision Surface.addObject('MechanicalObject', position="@[-1].position", translation="-5 0 0")
        Collision Surface.addObject('SphereCollisionModel', name="Surf", listRadius="@[-2].listRadius")
        Collision Surface.addObject('BarycentricMapping', input="@..", output="@.")

        LiverFFD-hires = root.addChild('LiverFFD-hires')
        LiverFFD-hires.addObject('EulerImplicitSolver')
        LiverFFD-hires.addObject('CGLinearSolver', iterations="100", tolerance="1e-7", threshold="1e-7")
        LiverFFD-hires.addObject('MechanicalObject')
        LiverFFD-hires.addObject('UniformMass', totalMass="100.0")
        LiverFFD-hires.addObject('RegularGridTopology', nx="8", ny="6", nz="6", xmin="-0.25", xmax="7.25", ymin="0.25", ymax="5.25", zmin="-2", zmax="3")
        LiverFFD-hires.addObject('BoxConstraint', box="2.5 0 -2.5 5 3 2")
        LiverFFD-hires.addObject('RegularGridSpringForceField', name="Springs", stiffness="100", damping="4")

        Visu = LiverFFD-hires.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/liver-smooth.obj", translation="5 0 0", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="red")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Collision Surface = LiverFFD-hires.addChild('Collision Surface')
        Collision Surface.addObject('SphereLoader', filename="mesh/liver.sph")
        Collision Surface.addObject('MechanicalObject', position="@[-1].position", translation="5 0 0")
        Collision Surface.addObject('SphereCollisionModel', name="Surf", listRadius="@[-2].listRadius")
        Collision Surface.addObject('BarycentricMapping', input="@..", output="@.")
    ```

Component/Topology/Container/Grid/RegularGridTopology_TrianglesMesh.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 -9 5">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        <CollisionPipeline />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        <DefaultAnimationLoop/>
    
        <Node name="SquareGravity">
            <EulerImplicitSolver name="cg_odesolver"/>
            <CGImplicit iterations="40" tolerance="1e-6" threshold="1e-10" />
                   
            <RegularGridTopology name="grid" nx="10" ny="10" nz="1" xmin="-5" xmax="5" ymin="-5" ymax="5" zmin="0" zmax="0"/>
            
            <MechanicalObject src="@grid" scale="10" />
            
            <TriangleSetTopologyContainer  name="Container" src="@grid"/>
            <TriangleSetTopologyModifier   name="Modifier" />
            <TriangleSetGeometryAlgorithms name="GeomAlgo" drawEdges="1"/>
            
            <DiagonalMass massDensity="0.15" />
            <FixedProjectiveConstraint indices="0 1 8 9 10 19" />
           
           
            <TriangularFEMForceField name="FEM" youngModulus="60" poissonRatio="0.3" method="large" />
            <TriangularBendingSprings name="FEM-Bend" stiffness="300" damping="1.0" />
            
            <TriangleCollisionModel />
            
            <Node >
              <OglModel name="Visual" color="red" />
              <IdentityMapping input="@.." output="@Visual" />
            </Node>
    
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.05", showBoundingTree="0", gravity="0 -9 5")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
        root.addObject('CollisionPipeline')
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
        root.addObject('DefaultAnimationLoop')

        SquareGravity = root.addChild('SquareGravity')
        SquareGravity.addObject('EulerImplicitSolver', name="cg_odesolver")
        SquareGravity.addObject('CGImplicit', iterations="40", tolerance="1e-6", threshold="1e-10")
        SquareGravity.addObject('RegularGridTopology', name="grid", nx="10", ny="10", nz="1", xmin="-5", xmax="5", ymin="-5", ymax="5", zmin="0", zmax="0")
        SquareGravity.addObject('MechanicalObject', src="@grid", scale="10")
        SquareGravity.addObject('TriangleSetTopologyContainer', name="Container", src="@grid")
        SquareGravity.addObject('TriangleSetTopologyModifier', name="Modifier")
        SquareGravity.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", drawEdges="1")
        SquareGravity.addObject('DiagonalMass', massDensity="0.15")
        SquareGravity.addObject('FixedProjectiveConstraint', indices="0 1 8 9 10 19")
        SquareGravity.addObject('TriangularFEMForceField', name="FEM", youngModulus="60", poissonRatio="0.3", method="large")
        SquareGravity.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="300", damping="1.0")
        SquareGravity.addObject('TriangleCollisionModel')

        SquareGravity = SquareGravity.addChild('SquareGravity')
        SquareGravity.addObject('OglModel', name="Visual", color="red")
        SquareGravity.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

