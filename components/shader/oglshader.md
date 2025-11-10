<!-- generate_doc -->
# OglShader

Set custom shader for the current visual context.


__Target__: Sofa.GL.Component.Shader

__namespace__: sofa::gl::component::shader

__parents__:

- Shader
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
		<td>turnOn</td>
		<td>
Turn On the shader?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>passive</td>
		<td>
Will this shader be activated manually or automatically?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>fileVertexShaders</td>
		<td>
Set the vertex shader filename to load
		</td>
		<td>[ 'shaders/toonShading.vert' ]</td>
	</tr>
	<tr>
		<td>fileFragmentShaders</td>
		<td>
Set the fragment shader filename to load
		</td>
		<td>[ 'shaders/toonShading.frag' ]</td>
	</tr>
	<tr>
		<td>fileGeometryShaders</td>
		<td>
Set the geometry shader filename to load
		</td>
		<td></td>
	</tr>
	<tr>
		<td>fileTessellationControlShaders</td>
		<td>
Set the tessellation control filename to load
		</td>
		<td></td>
	</tr>
	<tr>
		<td>fileTessellationEvaluationShaders</td>
		<td>
Set the tessellation evaluation filename to load
		</td>
		<td></td>
	</tr>
	<tr>
		<td>geometryInputType</td>
		<td>
Set input types for the geometry shader
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>geometryOutputType</td>
		<td>
Set output types for the geometry shader
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>geometryVerticesOut</td>
		<td>
Set max number of vertices in output for the geometry shader
		</td>
		<td>-1</td>
	</tr>
	<tr>
		<td>tessellationOuterLevel</td>
		<td>
For tessellation without control shader: default outer level (edge subdivisions)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>tessellationInnerLevel</td>
		<td>
For tessellation without control shader: default inner level (face subdivisions)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>indexActiveShader</td>
		<td>
Set current active shader
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>backfaceWriting</td>
		<td>
it enables writing to gl_BackColor inside a GLSL vertex shader
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>clampVertexColor</td>
		<td>
clamp the vertex color between 0 and 1
		</td>
		<td>1</td>
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

OglShader.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader SphereLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [OglShader] -->
    
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <DiscreteIntersection />
        <DefaultAnimationLoop/>
        <Node name="Liver">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="loader" filename="mesh/liver.msh" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader" name="Liver" />
            <UniformMass name="mass" vertexMass="0.05" />
            <TetrahedronFEMForceField name="FEM" youngModulus="500" poissonRatio="0.3" computeGlobalMatrix="false" method="large" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64" />
            <Node name="Visu">
                <OglShader fileFragmentShaders="['shaders/toonShading.frag']" fileVertexShaders="['shaders/toonShading.vert']" />
                <MeshOBJLoader name="meshLoader_0" filename="mesh/liver-smooth.obj" handleSeams="1" />
                <OglModel name="VisualModel" src="@meshLoader_0" color="red" />
                <BarycentricMapping input="@.." output="@VisualModel" />
            </Node>
            <Node name="Surf">
    	    <SphereLoader filename="mesh/liver.sph" />
                <MechanicalObject position="@[-1].position" />
                <SphereCollisionModel name="CollisionModel" listRadius="@[-2].listRadius" />
                <BarycentricMapping />
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
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('DiscreteIntersection', )
       root.addObject('DefaultAnimationLoop', )

       liver = root.addChild('Liver')

       liver.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       liver.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       liver.addObject('MeshGmshLoader', name="loader", filename="mesh/liver.msh")
       liver.addObject('MeshTopology', src="@loader")
       liver.addObject('MechanicalObject', src="@loader", name="Liver")
       liver.addObject('UniformMass', name="mass", vertexMass="0.05")
       liver.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.3", computeGlobalMatrix="false", method="large")
       liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

       visu = Liver.addChild('Visu')

       visu.addObject('OglShader', fileFragmentShaders="['shaders/toonShading.frag']", fileVertexShaders="['shaders/toonShading.vert']")
       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver-smooth.obj", handleSeams="1")
       visu.addObject('OglModel', name="VisualModel", src="@meshLoader_0", color="red")
       visu.addObject('BarycentricMapping', input="@..", output="@VisualModel")

       surf = Liver.addChild('Surf')

       surf.addObject('SphereLoader', filename="mesh/liver.sph")
       surf.addObject('MechanicalObject', position="@[-1].position")
       surf.addObject('SphereCollisionModel', name="CollisionModel", listRadius="@[-2].listRadius")
       surf.addObject('BarycentricMapping', )
    ```

OglShader_tessellation.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [TaitSurfacePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangularFEMForceFieldOptim] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [FastTriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [OglFloatVariable OglShader] -->
    
        <DefaultAnimationLoop/>
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <DiscreteIntersection />
        <Node name="Liver">
            <EulerImplicitSolver name="cg_odesolver" rayleighMass="0.1" rayleighStiffness="0.2" printLog="false" />
    <!--        <CGLinearSolver template="CompressedRowSparseMatrixMat3x3" iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />-->
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshOBJLoader name="loader" filename="mesh/sphere_02b.obj" scale="0.25 0.25 0.25" rotation="-90 0 0" triangulate="1" />
            <TriangleSetTopologyContainer src="@loader" />
            <MechanicalObject src="@loader" template="Vec3" name="DOFs" />
            <TriangleSetTopologyModifier />
            <TriangleSetGeometryAlgorithms />
            <BoxConstraint box="-10 -10 -10  10 -5 10" />
            <TriangularFEMForceFieldOptim name="FEM" youngModulus="10000" poissonRatio="0.4" restScale="0.97" method="large" />
            <FastTriangularBendingSprings name="Bending" bendingStiffness="100" />
            <TaitSurfacePressureForceField name="Pressure" gamma="5" B="10000" injectedVolume="100" printLog="1" />
            <DiagonalMass name="mass" massDensity="1" printLog="0" />
            <TriangleCollisionModel name="CM" />
    
            <Node name="Visu">
    
                <OglShader fileVertexShaders="['shaders/tessellationPNTriangle.glsl']"
                           fileTessellationControlShaders="['shaders/tessellationPNTriangle.glsl']"
                           fileTessellationEvaluationShaders="['shaders/tessellationPNTriangle.glsl']"
                           fileGeometryShaders="['shaders/tessellationPNTriangle.glsl']"
                           fileFragmentShaders="['shaders/tessellationPNTriangle.glsl']"
                           printLog="1" />
                <OglFloatVariable name="TessellationLevel" value="6" />
                <OglModel name="VisualModel" src="@../loader" color="white" primitiveType="PATCHES" />
                <IdentityMapping />
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
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('DiscreteIntersection', )

       liver = root.addChild('Liver')

       liver.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighMass="0.1", rayleighStiffness="0.2", printLog="false")
       liver.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       liver.addObject('MeshOBJLoader', name="loader", filename="mesh/sphere_02b.obj", scale="0.25 0.25 0.25", rotation="-90 0 0", triangulate="1")
       liver.addObject('TriangleSetTopologyContainer', src="@loader")
       liver.addObject('MechanicalObject', src="@loader", template="Vec3", name="DOFs")
       liver.addObject('TriangleSetTopologyModifier', )
       liver.addObject('TriangleSetGeometryAlgorithms', )
       liver.addObject('BoxConstraint', box="-10 -10 -10  10 -5 10")
       liver.addObject('TriangularFEMForceFieldOptim', name="FEM", youngModulus="10000", poissonRatio="0.4", restScale="0.97", method="large")
       liver.addObject('FastTriangularBendingSprings', name="Bending", bendingStiffness="100")
       liver.addObject('TaitSurfacePressureForceField', name="Pressure", gamma="5", B="10000", injectedVolume="100", printLog="1")
       liver.addObject('DiagonalMass', name="mass", massDensity="1", printLog="0")
       liver.addObject('TriangleCollisionModel', name="CM")

       visu = Liver.addChild('Visu')

       visu.addObject('OglShader', fileVertexShaders="['shaders/tessellationPNTriangle.glsl']", fileTessellationControlShaders="['shaders/tessellationPNTriangle.glsl']", fileTessellationEvaluationShaders="['shaders/tessellationPNTriangle.glsl']", fileGeometryShaders="['shaders/tessellationPNTriangle.glsl']", fileFragmentShaders="['shaders/tessellationPNTriangle.glsl']", printLog="1")
       visu.addObject('OglFloatVariable', name="TessellationLevel", value="6")
       visu.addObject('OglModel', name="VisualModel", src="@../loader", color="white", primitiveType="PATCHES")
       visu.addObject('IdentityMapping', )
    ```

