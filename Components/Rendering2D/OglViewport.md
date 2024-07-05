# OglViewport

OglViewport


__Target__: `Sofa.GL.Component.Rendering2D`

__namespace__: `#!c++ sofa::gl::component::rendering2d`

__parents__: 

- `#!c++ VisualManager`

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
		<td>enable</td>
		<td>
Display the object or not
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>screenPosition</td>
		<td>
Viewport position
</td>
		<td></td>
	</tr>
	<tr>
		<td>screenSize</td>
		<td>
Viewport size
</td>
		<td></td>
	</tr>
	<tr>
		<td>cameraPosition</td>
		<td>
Camera's position in eye's space
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>cameraOrientation</td>
		<td>
Camera's orientation
</td>
		<td>0 0 0 1</td>
	</tr>
	<tr>
		<td>cameraRigid</td>
		<td>
Camera's rigid coord
</td>
		<td></td>
	</tr>
	<tr>
		<td>zNear</td>
		<td>
Camera's ZNear
</td>
		<td></td>
	</tr>
	<tr>
		<td>zFar</td>
		<td>
Camera's ZFar
</td>
		<td></td>
	</tr>
	<tr>
		<td>fovy</td>
		<td>
Field of View (Y axis)
</td>
		<td>60</td>
	</tr>
	<tr>
		<td>enabled</td>
		<td>
Enable visibility of the viewport
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>advancedRendering</td>
		<td>
If true, viewport will be hidden if advancedRendering visual flag is not enabled
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useFBO</td>
		<td>
Use a FBO to render the viewport
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>swapMainView</td>
		<td>
Swap this viewport with the main view
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawCamera</td>
		<td>
Draw a frame representing the camera (see it in main viewport)
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

Component/Visual/OglViewport.scn

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
        <RequiredPlugin name="Sofa.GL.Component.Rendering2D"/> <!-- Needed to use components [OglViewport] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection />
        <Node name="Liver" depend="topo dofs">
            <!--<CGImplicit iterations="25"/>-->
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="loader" filename="mesh/liver.msh" />
            <!-- Container for the tetrahedra-->
            <TetrahedronSetTopologyContainer src="@loader" name="topo" />
            <MechanicalObject src="@loader" name="dofs" />
            <!-- Algorithms: used in DiagonalMass to compute the mass -->
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" />
            <DiagonalMass massDensity="1" name="computed using mass density" />
            <TetrahedralCorotationalFEMForceField name="FEM" youngModulus="3000" poissonRatio="0.3" computeGlobalMatrix="false" method="large" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64" />
            <Node name="Visu" tags="Visual">
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
        <OglViewport screenPosition="0 0" screenSize="250 250" cameraPosition="-1 2.7 5" cameraOrientation="-0 -0 -0 1" />
        <OglViewport screenPosition="300 0" screenSize="400 400" cameraRigid="-1 2.7 13 -0 -0 -0 1" />
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
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering2D")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
        root.addObject('DiscreteIntersection')

        Liver = root.addChild('Liver', depend="topo dofs")
        Liver.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        Liver.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Liver.addObject('MeshGmshLoader', name="loader", filename="mesh/liver.msh")
        Liver.addObject('TetrahedronSetTopologyContainer', src="@loader", name="topo")
        Liver.addObject('MechanicalObject', src="@loader", name="dofs")
        Liver.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo")
        Liver.addObject('DiagonalMass', massDensity="1", name="computed using mass density")
        Liver.addObject('TetrahedralCorotationalFEMForceField', name="FEM", youngModulus="3000", poissonRatio="0.3", computeGlobalMatrix="false", method="large")
        Liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

        Visu = Liver.addChild('Visu', tags="Visual")
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver-smooth.obj", handleSeams="1")
        Visu.addObject('OglModel', name="VisualModel", src="@meshLoader_0")
        Visu.addObject('BarycentricMapping', input="@..", output="@VisualModel", name="visual mapping")

        Surf = Liver.addChild('Surf')
        Surf.addObject('SphereLoader', filename="mesh/liver.sph")
        Surf.addObject('MechanicalObject', position="@[-1].position")
        Surf.addObject('SphereCollisionModel', name="CollisionModel", listRadius="@[-2].listRadius")
        Surf.addObject('BarycentricMapping', name="sphere mapping")
        root.addObject('OglViewport', screenPosition="0 0", screenSize="250 250", cameraPosition="-1 2.7 5", cameraOrientation="-0 -0 -0 1")
        root.addObject('OglViewport', screenPosition="300 0", screenSize="400 400", cameraRigid="-1 2.7 13 -0 -0 -0 1")
    ```

