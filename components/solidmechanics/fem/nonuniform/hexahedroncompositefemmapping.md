<!-- generate_doc -->
# HexahedronCompositeFEMMapping

Set the point to the center of mass of the DOFs it is attached to.


## Mapping<StdVectorTypes<Vec<3u,double>,Vec<3u,double>,double>,StdVectorTypes<Vec<3u,double>,Vec<3u,double>,double>>

Templates:

- Mapping<StdVectorTypes<Vec<3u,double>,Vec<3u,double>,double>,StdVectorTypes<Vec<3u,double>,Vec<3u,double>,double>>

__Target__: Sofa.Component.SolidMechanics.FEM.NonUniform

__namespace__: sofa::component::solidmechanics::fem::nonuniform

__parents__:

- Mapping

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
		<td>mapForces</td>
		<td>
Are forces mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapConstraints</td>
		<td>
Are constraints mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMasses</td>
		<td>
Are masses mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMatrices</td>
		<td>
Are matrix explicit mapped?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>applyRestPosition</td>
		<td>
set to true to apply this mapping to restPosition at init
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
|input|Input object to map|State&lt;Vec3d&gt;|
|output|Output object to map|State&lt;Vec3d&gt;|

## Examples 

HexahedronCompositeFEMMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 0 0" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [ConstantForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.NonUniform"/> <!-- Needed to use components [HexahedronCompositeFEMForceFieldAndMass HexahedronCompositeFEMMapping] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridMultipleTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <!-- A soft grape containing a very stiff seed is deformed by using only one element. By using the HexahedronCompositeFEMMapping, the seed does not deform.  -->
        <VisualStyle displayFlags="showVisual showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        <MeshOBJLoader name="meshLoader_2" filename="mesh/plane_loop_2.obj" scale="1" handleSeams="1" />
        <OglModel name="plan" src="@meshLoader_2" rx="90" rz="90" dy="-10.2" material="Default Diffuse 1 1 0.4 0.4 1 Ambient 1 0.8 0.8 0.8 1 Specular 0 1 1 1 1 Emissive 0 1 1 1 1 Shininess 0 45"/>
        <Node name="HexahedronCompositeFEMMapping">
            <SparseGridMultipleTopology n="2 2 2" fileTopology="mesh/grape_out.obj" fileTopologies="mesh/grape_out.obj mesh/grape_in.obj" stiffnessCoefs="1 1000000" massCoefs="1 1" nbVirtualFinerLevels="4" finestConnectivity="false" />
            <EulerImplicitSolver rayleighMass="0" rayleighStiffness="0" />
            <CGLinearSolver iterations="2000" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject dx="15" />
            <HexahedronCompositeFEMForceFieldAndMass completeInterpolation="false" nbVirtualFinerLevels="3" youngModulus="100" poissonRatio="0.35" method="large" density="2" updateStiffnessMatrix="false" printLog="0" useMass="false" totalMass="1" drawSize=".5" />
            <BoxConstraint box="-30 -11 -30   100 -9 30" drawSize="0.75" />
            <Node name="Collinonunif">
                <MeshOBJLoader name="loader" filename="mesh/grape_out.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <HexahedronCompositeFEMMapping/>
                <Node name="f1">
                    <ConstantForceField indices="340" forces="1000 8000 0" showArrowSize=".001" />
                </Node>
                <Node name="Visu2">
                    <MeshOBJLoader name="meshLoader_3" filename="mesh/grape_out.obj" handleSeams="1" />
                    <OglModel name="VisualEyes" src="@meshLoader_3" normals="0" color="0.1 .8 .3 .5" />
                    <IdentityMapping input="@.." output="@VisualEyes" />
                </Node>
            </Node>
            <Node name="Visu1">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/grape_in.obj" handleSeams="1" />
                <OglModel name="VisualBody" src="@meshLoader_0" normals="0" color="0 0 .6 1" />
                <HexahedronCompositeFEMMapping input="@.." output="@VisualBody" />
            </Node>
        </Node>
        <Node name="BarycentricMapping">
            <SparseGridMultipleTopology n="2 2 2" fileTopology="mesh/grape_out.obj" fileTopologies="mesh/grape_out.obj mesh/grape_in.obj" stiffnessCoefs="1 1000000" massCoefs="1 1" nbVirtualFinerLevels="4" finestConnectivity="false" />
            <EulerImplicitSolver rayleighMass="0" rayleighStiffness="0" />
            <CGLinearSolver iterations="2000" tolerance="1e-5" threshold="1e-5"/>
            <MechanicalObject dx="-15" />
            <HexahedronCompositeFEMForceFieldAndMass completeInterpolation="true" nbVirtualFinerLevels="3" youngModulus="100" poissonRatio="0.35" method="large" density="2" updateStiffnessMatrix="false" printLog="0" useMass="false" totalMass="1" drawSize=".5" />
            <BoxConstraint box="-100 -11 -30   30 -9 30" drawSize="0.75"/>
            <Node name="Collinonunif">
                <MeshOBJLoader name="loader" filename="mesh/grape_out.obj"/>
                <MeshTopology src="@loader"/>
                <MechanicalObject src="@loader"/>
                <BarycentricMapping/>
                <Node name="f2">
                    <ConstantForceField indices="340" forces="1000 8000 0" showArrowSize=".001" />
                </Node>
                <Node name="Visu2">
                    <MeshOBJLoader name="meshLoader_4" filename="mesh/grape_out.obj" handleSeams="1" />
                    <OglModel name="VisualEyes" src="@meshLoader_4" normals="0" color="0.1 .8 .3 .5" />
                    <IdentityMapping input="@.." output="@VisualEyes" />
                </Node>
            </Node>
            <Node name="Visu1">
                <MeshOBJLoader name="meshLoader_1" filename="mesh/grape_in.obj" handleSeams="1" />
                <OglModel name="VisualBody" src="@meshLoader_1" normals="0" color="0 0 .6 1" />
                <BarycentricMapping input="@.." output="@VisualBody" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 0", dt="0.01")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.NonUniform")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showForceFields")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/plane_loop_2.obj", scale="1", handleSeams="1")
       root.addObject('OglModel', name="plan", src="@meshLoader_2", rx="90", rz="90", dy="-10.2", material="Default Diffuse 1 1 0.4 0.4 1 Ambient 1 0.8 0.8 0.8 1 Specular 0 1 1 1 1 Emissive 0 1 1 1 1 Shininess 0 45")

       hexahedron_composite_fem_mapping = root.addChild('HexahedronCompositeFEMMapping')

       hexahedron_composite_fem_mapping.addObject('SparseGridMultipleTopology', n="2 2 2", fileTopology="mesh/grape_out.obj", fileTopologies="mesh/grape_out.obj mesh/grape_in.obj", stiffnessCoefs="1 1000000", massCoefs="1 1", nbVirtualFinerLevels="4", finestConnectivity="false")
       hexahedron_composite_fem_mapping.addObject('EulerImplicitSolver', rayleighMass="0", rayleighStiffness="0")
       hexahedron_composite_fem_mapping.addObject('CGLinearSolver', iterations="2000", tolerance="1e-5", threshold="1e-5")
       hexahedron_composite_fem_mapping.addObject('MechanicalObject', dx="15")
       hexahedron_composite_fem_mapping.addObject('HexahedronCompositeFEMForceFieldAndMass', completeInterpolation="false", nbVirtualFinerLevels="3", youngModulus="100", poissonRatio="0.35", method="large", density="2", updateStiffnessMatrix="false", printLog="0", useMass="false", totalMass="1", drawSize=".5")
       hexahedron_composite_fem_mapping.addObject('BoxConstraint', box="-30 -11 -30   100 -9 30", drawSize="0.75")

       collinonunif = HexahedronCompositeFEMMapping.addChild('Collinonunif')

       collinonunif.addObject('MeshOBJLoader', name="loader", filename="mesh/grape_out.obj")
       collinonunif.addObject('MeshTopology', src="@loader")
       collinonunif.addObject('MechanicalObject', src="@loader")
       collinonunif.addObject('HexahedronCompositeFEMMapping', )

       f1 = Collinonunif.addChild('f1')

       f1.addObject('ConstantForceField', indices="340", forces="1000 8000 0", showArrowSize=".001")

       visu2 = Collinonunif.addChild('Visu2')

       visu2.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/grape_out.obj", handleSeams="1")
       visu2.addObject('OglModel', name="VisualEyes", src="@meshLoader_3", normals="0", color="0.1 .8 .3 .5")
       visu2.addObject('IdentityMapping', input="@..", output="@VisualEyes")

       visu1 = HexahedronCompositeFEMMapping.addChild('Visu1')

       visu1.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/grape_in.obj", handleSeams="1")
       visu1.addObject('OglModel', name="VisualBody", src="@meshLoader_0", normals="0", color="0 0 .6 1")
       visu1.addObject('HexahedronCompositeFEMMapping', input="@..", output="@VisualBody")

       barycentric_mapping = root.addChild('BarycentricMapping')

       barycentric_mapping.addObject('SparseGridMultipleTopology', n="2 2 2", fileTopology="mesh/grape_out.obj", fileTopologies="mesh/grape_out.obj mesh/grape_in.obj", stiffnessCoefs="1 1000000", massCoefs="1 1", nbVirtualFinerLevels="4", finestConnectivity="false")
       barycentric_mapping.addObject('EulerImplicitSolver', rayleighMass="0", rayleighStiffness="0")
       barycentric_mapping.addObject('CGLinearSolver', iterations="2000", tolerance="1e-5", threshold="1e-5")
       barycentric_mapping.addObject('MechanicalObject', dx="-15")
       barycentric_mapping.addObject('HexahedronCompositeFEMForceFieldAndMass', completeInterpolation="true", nbVirtualFinerLevels="3", youngModulus="100", poissonRatio="0.35", method="large", density="2", updateStiffnessMatrix="false", printLog="0", useMass="false", totalMass="1", drawSize=".5")
       barycentric_mapping.addObject('BoxConstraint', box="-100 -11 -30   30 -9 30", drawSize="0.75")

       collinonunif = BarycentricMapping.addChild('Collinonunif')

       collinonunif.addObject('MeshOBJLoader', name="loader", filename="mesh/grape_out.obj")
       collinonunif.addObject('MeshTopology', src="@loader")
       collinonunif.addObject('MechanicalObject', src="@loader")
       collinonunif.addObject('BarycentricMapping', )

       f2 = Collinonunif.addChild('f2')

       f2.addObject('ConstantForceField', indices="340", forces="1000 8000 0", showArrowSize=".001")

       visu2 = Collinonunif.addChild('Visu2')

       visu2.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/grape_out.obj", handleSeams="1")
       visu2.addObject('OglModel', name="VisualEyes", src="@meshLoader_4", normals="0", color="0.1 .8 .3 .5")
       visu2.addObject('IdentityMapping', input="@..", output="@VisualEyes")

       visu1 = BarycentricMapping.addChild('Visu1')

       visu1.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/grape_in.obj", handleSeams="1")
       visu1.addObject('OglModel', name="VisualBody", src="@meshLoader_1", normals="0", color="0 0 .6 1")
       visu1.addObject('BarycentricMapping', input="@..", output="@VisualBody")
    ```

