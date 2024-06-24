# DistanceGridForceField

Force applied by a distancegrid toward the exterior, the interior, or the surface


__Templates__:

- `#!c++ Vec3d`

__Target__: `SofaDistanceGrid`

__namespace__: `#!c++ sofa::component::forcefield`

__parents__: 

- `#!c++ ForceField`

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
		<td>isCompliance</td>
		<td>
Consider the component as a compliance, else as a stiffness
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>filename</td>
		<td>
load distance grid from specified file
</td>
		<td></td>
	</tr>
	<tr>
		<td>scale</td>
		<td>
scaling factor for input file
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>box</td>
		<td>
Field bounding box defined by xmin,ymin,zmin, xmax,ymax,zmax
</td>
		<td></td>
	</tr>
	<tr>
		<td>nx</td>
		<td>
number of values on X axis
</td>
		<td>64</td>
	</tr>
	<tr>
		<td>ny</td>
		<td>
number of values on Y axis
</td>
		<td>64</td>
	</tr>
	<tr>
		<td>nz</td>
		<td>
number of values on Z axis
</td>
		<td>64</td>
	</tr>
	<tr>
		<td>stiffnessIn</td>
		<td>
force stiffness when inside of the object
</td>
		<td>500</td>
	</tr>
	<tr>
		<td>stiffnessOut</td>
		<td>
force stiffness when outside of the object
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
force damping coefficient
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>maxdist</td>
		<td>
max distance of the surface after which no more force is applied
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>minArea</td>
		<td>
minimal area for each triangle, as seen from the direction of the local surface (i.e. a flipped triangle will have a negative area)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stiffnessArea</td>
		<td>
force stiffness if a triangle have an area less than minArea
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>minVolume</td>
		<td>
minimal volume for each tetrahedron (a flipped triangle will have a negative volume)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>stiffnessVolume</td>
		<td>
force stiffness if a tetrahedron have an volume less than minVolume
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>color</td>
		<td>
display color.(default=[0.0,0.5,0.2,1.0])
</td>
		<td>0 0.5 0.2 1</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)
</td>
		<td>-1 -1</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>draw</td>
		<td>
enable/disable drawing of distancegrid
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawPoints</td>
		<td>
enable/disable drawing of distancegrid
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawSize</td>
		<td>
display size if draw is enabled
</td>
		<td>10</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|
|mechanicalStates|List of mechanical states to which this component is associated|
|mstate|MechanicalState used by this component|



## Examples

SofaDistanceGrid/share/sofa/examples/SofaDistanceGrid/DistanceGridForceField-liver.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01" showBoundingTree="0" gravity="0 -9.81 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaDistanceGrid"/> <!-- Needed to use components [DistanceGridForceField] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields showCollisionModels" />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="2" contactDistance="0.1" />
        
        <Node name="Simulation">
    
            <Node name="CubeObstacle">
                <OglModel name="cubeVisual" filename="mesh/cube.obj" color="green"/>
            </Node>
    
            <Node name="liver">
                <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="150" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
                <MeshGmshLoader name="loader" filename="mesh/liver.msh"/>
    
                <TetrahedronSetTopologyContainer name="tetras" src="@loader"/>
                <TetrahedronSetTopologyModifier   name="Modifier" />
                <TetrahedronSetGeometryAlgorithms name="GeomAlgo"  template="Vec3d" />
    
                <MechanicalObject name="meca"/>
                <DiagonalMass vertexMass="100"/>
    
                <TetrahedronFEMForceField youngModulus="1000000" poissonRatio="0.45"/>
                <DistanceGridForceField filename="mesh/cubeDistanceGrid.fmesh" stiffnessIn="100000000" stiffnessOut="0" draw="true" drawPoints="true" printLog="false" drawSize="2"/>
    
                <Node name="visual">
                    <OglModel name="visu" filename="mesh/liver.obj"/>
                    <BarycentricMapping input="@../meca" output="@visu"/>
                </Node>
    
                <PlaneForceField stiffness="1000000" d="-1"/>
    
            </Node>
    
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", showBoundingTree="0", gravity="0 -9.81 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RequiredPlugin', name="SofaDistanceGrid")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showCollisionModels")
        root.addObject('CollisionPipeline', verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField")
        root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="2", contactDistance="0.1")

        Simulation = root.addChild('Simulation')

        CubeObstacle = Simulation.addChild('CubeObstacle')
        CubeObstacle.addObject('OglModel', name="cubeVisual", filename="mesh/cube.obj", color="green")

        liver = Simulation.addChild('liver')
        liver.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        liver.addObject('CGLinearSolver', iterations="150", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        liver.addObject('MeshGmshLoader', name="loader", filename="mesh/liver.msh")
        liver.addObject('TetrahedronSetTopologyContainer', name="tetras", src="@loader")
        liver.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        liver.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo", template="Vec3d")
        liver.addObject('MechanicalObject', name="meca")
        liver.addObject('DiagonalMass', vertexMass="100")
        liver.addObject('TetrahedronFEMForceField', youngModulus="1000000", poissonRatio="0.45")
        liver.addObject('DistanceGridForceField', filename="mesh/cubeDistanceGrid.fmesh", stiffnessIn="100000000", stiffnessOut="0", draw="true", drawPoints="true", printLog="false", drawSize="2")

        visual = liver.addChild('visual')
        visual.addObject('OglModel', name="visu", filename="mesh/liver.obj")
        visual.addObject('BarycentricMapping', input="@../meca", output="@visu")
        liver.addObject('PlaneForceField', stiffness="1000000", d="-1")
    ```

