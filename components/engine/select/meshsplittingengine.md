<!-- generate_doc -->
# MeshSplittingEngine

This class breaks a mesh in multiple parts, based on selected vertices or cells.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Engine.Select

__namespace__: sofa::component::engine::select

__parents__:

- DataEngine

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
		<td>position</td>
		<td>
input vertices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
input edges
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
input triangles
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
input quads
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
input tetrahedra
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
input hexahedra
		</td>
		<td></td>
	</tr>
	<tr>
		<td>nbInputs</td>
		<td>
Number of input vectors
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>indexPairs</td>
		<td>
couples for input vertices: ROI index + index in the ROI
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>position1</td>
		<td>
output vertices(1)
		</td>
		<td></td>
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

MeshSplittingEngine.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <!-- MeshSplittingEngine Example -->
    
    <Node name="root" dt="0.1">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI MeshSplittingEngine] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping SubsetMultiMapping] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.Setting"/> <!-- Needed to use components [BackgroundSetting] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        
        <VisualStyle displayFlags="showBehavior showVisual" />
        <BackgroundSetting color="1 1 1"/>
        <DefaultAnimationLoop/>
        
        <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
        <MeshTopology name="mesh" src="@loader" />
        <BoxROI template="Vec3" box="0 -2 0 5 2 5" src="@mesh" name="roi" drawBoxes="true"/>
    
        <MeshSplittingEngine name="split" src="@loader" nbInputs="1" tetrahedronIndices1="@roi.tetrahedronIndices" printLog="true"/>
    
            <Node name="rigid">
                <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="50" threshold="1e-15" tolerance="1e-15" printLog="0" />
                
                <MechanicalObject name="rigidframe" template="Rigid3" position="1 0 1 0 0 0 1" />
                <UniformMass  />
                <FixedProjectiveConstraint indices="0"/>
                
                <Node name="rigidmapped points">
                        <MechanicalObject position="@/split.position1"/>
                        <RigidMapping globalToLocalCoords="1"/>
    
                        <Node name="free points">
                            <MechanicalObject position="@/split.position2" showObject="true"/>
                            <UniformMass totalMass="1" />
        
                            <Node name="multimapped full object">
                                <MeshTopology name="mesh" src="@/mesh" />
                                <MechanicalObject src="@mesh" />
                                <SubsetMultiMapping template = "Vec3,Vec3" input="@../../ @../" output="@./" indexPairs="@/split.indexPairs"/>
                                <TetrahedronFEMForceField youngModulus="100" poissonRatio="0.3"/>
                                
                                <Node name="Visu">
                                    <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" handleSeams="1" />
                                    <OglModel name="Visual" src="@meshLoader_0" color="5E-1 5E-1 5E-1 5E-1" />
                                    <BarycentricMapping  />
                                </Node>
                            </Node>
                            
                        </Node>
    
                </Node>
            </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.1")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.Setting")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showBehavior showVisual")
       root.addObject('BackgroundSetting', color="1 1 1")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
       root.addObject('MeshTopology', name="mesh", src="@loader")
       root.addObject('BoxROI', template="Vec3", box="0 -2 0 5 2 5", src="@mesh", name="roi", drawBoxes="true")
       root.addObject('MeshSplittingEngine', name="split", src="@loader", nbInputs="1", tetrahedronIndices1="@roi.tetrahedronIndices", printLog="true")

       rigid = root.addChild('rigid')

       rigid.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       rigid.addObject('CGLinearSolver', iterations="50", threshold="1e-15", tolerance="1e-15", printLog="0")
       rigid.addObject('MechanicalObject', name="rigidframe", template="Rigid3", position="1 0 1 0 0 0 1")
       rigid.addObject('UniformMass', )
       rigid.addObject('FixedProjectiveConstraint', indices="0")

       rigidmapped_points = rigid.addChild('rigidmapped points')

       rigidmapped_points.addObject('MechanicalObject', position="@/split.position1")
       rigidmapped_points.addObject('RigidMapping', globalToLocalCoords="1")

       free_points = rigidmapped points.addChild('free points')

       free_points.addObject('MechanicalObject', position="@/split.position2", showObject="true")
       free_points.addObject('UniformMass', totalMass="1")

       multimapped_full_object = free points.addChild('multimapped full object')

       multimapped_full_object.addObject('MeshTopology', name="mesh", src="@/mesh")
       multimapped_full_object.addObject('MechanicalObject', src="@mesh")
       multimapped_full_object.addObject('SubsetMultiMapping', template="Vec3,Vec3", input="@../../ @../", output="@./", indexPairs="@/split.indexPairs")
       multimapped_full_object.addObject('TetrahedronFEMForceField', youngModulus="100", poissonRatio="0.3")

       visu = multimapped full object.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="5E-1 5E-1 5E-1 5E-1")
       visu.addObject('BarycentricMapping', )
    ```

