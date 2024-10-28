<!-- generate_doc -->
# PostProcessManager

PostProcessManager


__Target__: Sofa.GL.Component.Shader

__namespace__: sofa::gl::component::shader

__parents__:

- VisualModel

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
		<td>enable</td>
		<td>
Display the object or not
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>zNear</td>
		<td>
Set zNear distance (for Depth Buffer)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>zFar</td>
		<td>
Set zFar distance (for Depth Buffer)
		</td>
		<td>100</td>
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

PostProcessManager_DepthOfField.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader SphereLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [OglFloatVariable OglIntVariable OglShader PostProcessManager] -->
        
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection />
        <DefaultAnimationLoop/>
        
        <Node name="Liver" depend="topo dofs">
            <!--<CGImplicit iterations="25"/>-->
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="loader" filename="mesh/liver.msh" />
            <MechanicalObject src="@loader" name="dofs" />
            <!-- Container for the tetrahedra-->
            <TetrahedronSetTopologyContainer src="@loader" name="topo" />
            <!-- Algorithms: used in DiagonalMass to compute the mass -->
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" />
            <DiagonalMass massDensity="1" name="computed using mass density" />
            <TetrahedralCorotationalFEMForceField name="FEM" youngModulus="3000" poissonRatio="0.3" computeGlobalMatrix="false" method="large" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64" />
            <Node name="Visu">
                <!-- Using material contained in liver-smooth.obj -->
                <MeshOBJLoader name="meshLoader_0" filename="mesh/liver-smooth.obj" handleSeams="1" />
                <OglModel name="VisualModel" src="@meshLoader_0" />
                <BarycentricMapping input="@.." output="@VisualModel" name="visual mapping" />
            </Node>
            <Node name="Surf">
    	    <SphereLoader filename="mesh/liver.sph" />
                <MechanicalObject position="@[-1].position" />
                <SphereCollisionModel name="CollisionModel" listRadius="@[-2].listRadius" />
                <BarycentricMapping name="sphere mapping" />
            </Node>
        </Node>
        <MeshOBJLoader name='myLoaderDragon' filename='mesh/dragon.obj'/>  
        <MeshOBJLoader name='myLoaderFloor' filename='mesh/floor.obj'/>  
        <OglModel name="VisualModel" src='@myLoaderDragon' color="green" dz="-25.0" scale="0.3 0.3 0.3"/>
        <OglModel name="FloorV" src='@myLoaderFloor' color="0.5 0.5 0.5" dy="-2.5"/>
        <!--<LightManager listening="true"/>
    	<SpotLight position="0 30 0.0001" direction="0 -1 0" />
    	<SpotLight position="0 5 15" direction="0 0 -1" />
    	<OglShadowShader/>-->
        <OglShader name="dof" passive="true" fileFragmentShaders="['shaders/depthOfField.frag']" fileVertexShaders="['shaders/depthOfField.vert']" />
        <OglFloatVariable id="blurIntensity" value="0.2" />
        <OglFloatVariable id="focusDistance" value="0.9" />
        <OglFloatVariable id="focusLength" value="0.05" />
        <OglIntVariable id="showDepthMap" value="0" />
        <PostProcessManager zFar="1000" />
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

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
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
       root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
       root.addObject('DiscreteIntersection', )
       root.addObject('DefaultAnimationLoop', )

       liver = root.addChild('Liver', depend="topo dofs")

       liver.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       liver.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       liver.addObject('MeshGmshLoader', name="loader", filename="mesh/liver.msh")
       liver.addObject('MechanicalObject', src="@loader", name="dofs")
       liver.addObject('TetrahedronSetTopologyContainer', src="@loader", name="topo")
       liver.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo")
       liver.addObject('DiagonalMass', massDensity="1", name="computed using mass density")
       liver.addObject('TetrahedralCorotationalFEMForceField', name="FEM", youngModulus="3000", poissonRatio="0.3", computeGlobalMatrix="false", method="large")
       liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

       visu = Liver.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver-smooth.obj", handleSeams="1")
       visu.addObject('OglModel', name="VisualModel", src="@meshLoader_0")
       visu.addObject('BarycentricMapping', input="@..", output="@VisualModel", name="visual mapping")

       surf = Liver.addChild('Surf')

       surf.addObject('SphereLoader', filename="mesh/liver.sph")
       surf.addObject('MechanicalObject', position="@[-1].position")
       surf.addObject('SphereCollisionModel', name="CollisionModel", listRadius="@[-2].listRadius")
       surf.addObject('BarycentricMapping', name="sphere mapping")

       root.addObject('MeshOBJLoader', name="myLoaderDragon", filename="mesh/dragon.obj")
       root.addObject('MeshOBJLoader', name="myLoaderFloor", filename="mesh/floor.obj")
       root.addObject('OglModel', name="VisualModel", src="@myLoaderDragon", color="green", dz="-25.0", scale="0.3 0.3 0.3")
       root.addObject('OglModel', name="FloorV", src="@myLoaderFloor", color="0.5 0.5 0.5", dy="-2.5")
       root.addObject('OglShader', name="dof", passive="true", fileFragmentShaders="['shaders/depthOfField.frag']", fileVertexShaders="['shaders/depthOfField.vert']")
       root.addObject('OglFloatVariable', id="blurIntensity", value="0.2")
       root.addObject('OglFloatVariable', id="focusDistance", value="0.9")
       root.addObject('OglFloatVariable', id="focusLength", value="0.05")
       root.addObject('OglIntVariable', id="showDepthMap", value="0")
       root.addObject('PostProcessManager', zFar="1000")
    ```

