# MeshMatrixMass

Define a specific mass for each particle
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ CudaVec1d,CudaVec1d`
- `#!c++ CudaVec1d,CudaVec2d`
- `#!c++ CudaVec1d,CudaVec3d`
- `#!c++ CudaVec1f,CudaVec1f`
- `#!c++ CudaVec1f,CudaVec2f`
- `#!c++ CudaVec1f,CudaVec3f`
- `#!c++ CudaVec2d,CudaVec2d`
- `#!c++ CudaVec2d,CudaVec3d`
- `#!c++ CudaVec2f,CudaVec2f`
- `#!c++ CudaVec2f,CudaVec3f`
- `#!c++ CudaVec3d,CudaVec3d`
- `#!c++ CudaVec3f,CudaVec3f`

__Target__: `SofaCUDA`

__namespace__: `#!c++ sofa::component::mass`

__parents__: 

- `#!c++ Mass`

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
		<td>separateGravity</td>
		<td>
add separately gravity to velocity computation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping - mass matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>massDensity</td>
		<td>
Specify real and strictly positive value(s) for the mass density. 
If unspecified or wrongly set, the totalMass information is used.
</td>
		<td></td>
	</tr>
	<tr>
		<td>totalMass</td>
		<td>
Specify the total mass resulting from all particles. 
If unspecified or wrongly set, the default value is used: totalMass = 1.0
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>vertexMass</td>
		<td>
internal values of the particles masses on vertices, supporting topological changes
</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeMass</td>
		<td>
internal values of the particles masses on edges, supporting topological changes
</td>
		<td></td>
	</tr>
	<tr>
		<td>computeMassOnRest</td>
		<td>
If true, the mass of every element is computed based on the rest position rather than the position
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>lumping</td>
		<td>
If true, the mass matrix is lumped, meaning the mass matrix becomes diagonal (summing all mass values of a line on the diagonal)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>printMass</td>
		<td>
boolean if you want to check the mass conservation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>graph</td>
		<td>
Graph of the controlled potential
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showGravityCenter</td>
		<td>
display the center of gravity of the system
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showAxisSizeFactor</td>
		<td>
factor length of the axis displayed (only used for rigids)
</td>
		<td>1</td>
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
|topology|link to the topology container|
|geometryState|link to the MechanicalObject associated with the geometry|



## Examples

Component/Mass/MeshMatrixMass.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.005">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader SphereLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection />
    
        <MeshGmshLoader name="MeshLoader" filename="mesh/liver.msh" />
        <MeshOBJLoader name="LiverSurface" filename="mesh/liver-smooth.obj" />
    
        <Node name="Liver">
            <EulerImplicitSolver name="integration scheme" />
            <CGLinearSolver name="linear solver" iterations="1000" tolerance="1e-9" threshold="1e-9"/>
            <MechanicalObject name="dofs" src="@../MeshLoader"/>
            <!-- Container for the tetrahedra-->
            <TetrahedronSetTopologyContainer name="TetraTopo" src="@../MeshLoader"/>
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" />
            <MeshMatrixMass totalMass="60" name="SparseMass" topology="@TetraTopo" />
            <TetrahedralCorotationalFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.45" youngModulus="5000" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64" />
    
            <Node name="Visu" >
                <OglModel  name="VisualModel" src="@../../LiverSurface" color="cyan"/>
                <BarycentricMapping name="VisualMapping" input="@../dofs" output="@VisualModel" />
            </Node>
            <Node name="Surf" >
                <SphereLoader filename="mesh/liver.sph" />
                <MechanicalObject name="spheres" position="@[-1].position" />
                <SphereCollisionModel name="CollisionModel" listRadius="@[-2].listRadius"/>
                <BarycentricMapping name="CollisionMapping" input="@../dofs" output="@spheres" />
            </Node>
    
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.005")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('DefaultAnimationLoop')
        root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
        root.addObject('DiscreteIntersection')
        root.addObject('MeshGmshLoader', name="MeshLoader", filename="mesh/liver.msh")
        root.addObject('MeshOBJLoader', name="LiverSurface", filename="mesh/liver-smooth.obj")

        Liver = root.addChild('Liver')
        Liver.addObject('EulerImplicitSolver', name="integration scheme")
        Liver.addObject('CGLinearSolver', name="linear solver", iterations="1000", tolerance="1e-9", threshold="1e-9")
        Liver.addObject('MechanicalObject', name="dofs", src="@../MeshLoader")
        Liver.addObject('TetrahedronSetTopologyContainer', name="TetraTopo", src="@../MeshLoader")
        Liver.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo")
        Liver.addObject('MeshMatrixMass', totalMass="60", name="SparseMass", topology="@TetraTopo")
        Liver.addObject('TetrahedralCorotationalFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.45", youngModulus="5000")
        Liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

        Visu = Liver.addChild('Visu')
        Visu.addObject('OglModel', name="VisualModel", src="@../../LiverSurface", color="cyan")
        Visu.addObject('BarycentricMapping', name="VisualMapping", input="@../dofs", output="@VisualModel")

        Surf = Liver.addChild('Surf')
        Surf.addObject('SphereLoader', filename="mesh/liver.sph")
        Surf.addObject('MechanicalObject', name="spheres", position="@[-1].position")
        Surf.addObject('SphereCollisionModel', name="CollisionModel", listRadius="@[-2].listRadius")
        Surf.addObject('BarycentricMapping', name="CollisionMapping", input="@../dofs", output="@spheres")
    ```

