<!-- generate_doc -->
# CorotationalFEMForceField

Hooke's law using the corotational approach


Templates:

- Vec2d,Edge
- Vec2d,Quad
- Vec2d,Triangle

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseElementLinearFEMForceField
- FEMForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nbThreads</td>
		<td>
If not yet initialized, the main task scheduler is initialized with this number of threads. 0 corresponds to the number of available cores on the CPU. -n (minus) corresponds to the number of available cores on the CPU minus the provided number.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>taskSchedulerType</td>
		<td>
Type of task scheduler to use.
		</td>
		<td>_default</td>
	</tr>
	<tr>
		<td>poissonRatio</td>
		<td>
FEM Poisson Ratio in Hooke's law [0,0.5[
		</td>
		<td>0.45</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
FEM Young's Modulus in Hooke's law
		</td>
		<td>5000</td>
	</tr>
	<tr>
		<td>elementStiffness</td>
		<td>
List of stiffness matrices per element
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationMethod</td>
		<td>
The method used to compute the element rotations.
- stable_polar: Stable polar decomposition
- polar: Polar decomposition
- identity: Identity rotation. Equivalent to the linear small strain FEM.
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Multithreading</td>
	</tr>
	<tr>
		<td>computeForceStrategy</td>
		<td>
The compute strategy used to compute the forces.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeForceDerivStrategy</td>
		<td>
The compute strategy used to compute the forces derivatives.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>elementSpace</td>
		<td>
When rendering, the space between elements
		</td>
		<td>0.125</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec2d&gt;|
|topology|Link to a topology|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d,Edge...

Templates:

- Vec3d,Edge
- Vec3d,Prism
- Vec3d,Quad

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseElementLinearFEMForceField
- FEMForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nbThreads</td>
		<td>
If not yet initialized, the main task scheduler is initialized with this number of threads. 0 corresponds to the number of available cores on the CPU. -n (minus) corresponds to the number of available cores on the CPU minus the provided number.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>taskSchedulerType</td>
		<td>
Type of task scheduler to use.
		</td>
		<td>_default</td>
	</tr>
	<tr>
		<td>poissonRatio</td>
		<td>
FEM Poisson Ratio in Hooke's law [0,0.5[
		</td>
		<td>0.45</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
FEM Young's Modulus in Hooke's law
		</td>
		<td>5000</td>
	</tr>
	<tr>
		<td>elementStiffness</td>
		<td>
List of stiffness matrices per element
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationMethod</td>
		<td>
The method used to compute the element rotations.
- stable_polar: Stable polar decomposition
- polar: Polar decomposition
- identity: Identity rotation. Equivalent to the linear small strain FEM.
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Multithreading</td>
	</tr>
	<tr>
		<td>computeForceStrategy</td>
		<td>
The compute strategy used to compute the forces.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeForceDerivStrategy</td>
		<td>
The compute strategy used to compute the forces derivatives.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>elementSpace</td>
		<td>
When rendering, the space between elements
		</td>
		<td>0.125</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|Link to a topology|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d,Hexahedron

Templates:

- Vec3d,Hexahedron

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseElementLinearFEMForceField
- FEMForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nbThreads</td>
		<td>
If not yet initialized, the main task scheduler is initialized with this number of threads. 0 corresponds to the number of available cores on the CPU. -n (minus) corresponds to the number of available cores on the CPU minus the provided number.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>taskSchedulerType</td>
		<td>
Type of task scheduler to use.
		</td>
		<td>_default</td>
	</tr>
	<tr>
		<td>poissonRatio</td>
		<td>
FEM Poisson Ratio in Hooke's law [0,0.5[
		</td>
		<td>0.45</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
FEM Young's Modulus in Hooke's law
		</td>
		<td>5000</td>
	</tr>
	<tr>
		<td>elementStiffness</td>
		<td>
List of stiffness matrices per element
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationMethod</td>
		<td>
The method used to compute the element rotations.
- stable_polar: Stable polar decomposition
- polar: Polar decomposition
- identity: Identity rotation. Equivalent to the linear small strain FEM.
- hexahedron: Compute the rotation based on two average edges in the hexahedron
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Multithreading</td>
	</tr>
	<tr>
		<td>computeForceStrategy</td>
		<td>
The compute strategy used to compute the forces.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeForceDerivStrategy</td>
		<td>
The compute strategy used to compute the forces derivatives.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>elementSpace</td>
		<td>
When rendering, the space between elements
		</td>
		<td>0.125</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|Link to a topology|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d,Tetrahedron...

Templates:

- Vec3d,Tetrahedron
- Vec3d,Triangle

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseElementLinearFEMForceField
- FEMForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>nbThreads</td>
		<td>
If not yet initialized, the main task scheduler is initialized with this number of threads. 0 corresponds to the number of available cores on the CPU. -n (minus) corresponds to the number of available cores on the CPU minus the provided number.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>taskSchedulerType</td>
		<td>
Type of task scheduler to use.
		</td>
		<td>_default</td>
	</tr>
	<tr>
		<td>poissonRatio</td>
		<td>
FEM Poisson Ratio in Hooke's law [0,0.5[
		</td>
		<td>0.45</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
FEM Young's Modulus in Hooke's law
		</td>
		<td>5000</td>
	</tr>
	<tr>
		<td>elementStiffness</td>
		<td>
List of stiffness matrices per element
		</td>
		<td></td>
	</tr>
	<tr>
		<td>rotationMethod</td>
		<td>
The method used to compute the element rotations.
- stable_polar: Stable polar decomposition
- polar: Polar decomposition
- identity: Identity rotation. Equivalent to the linear small strain FEM.
- triangle: Compute the rotation based on the Gram-Schmidt frame alignment
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Multithreading</td>
	</tr>
	<tr>
		<td>computeForceStrategy</td>
		<td>
The compute strategy used to compute the forces.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeForceDerivStrategy</td>
		<td>
The compute strategy used to compute the forces derivatives.
- parallel: The algorithm is executed in parallel
- sequenced: The algorithm is executed sequentially
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>elementSpace</td>
		<td>
When rendering, the space between elements
		</td>
		<td>0.125</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|Link to a topology|BaseMeshTopology|

## Examples 

CorotationalFEMForceField_tetra_cpu_gpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 0" dt="0.02">
        <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->  
        <RequiredPlugin pluginName="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->  
        <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->  
        <RequiredPlugin pluginName="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->  
        <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->  
        <RequiredPlugin pluginName="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->  
        <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronCorotationalFEMForceField] -->  
        <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->  
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetTopologyContainer,HexahedronSetTopologyModifier,QuadSetTopologyContainer,QuadSetTopologyModifier] -->  
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->  
        <RequiredPlugin pluginName="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2QuadTopologicalMapping] -->  
        <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->  
        <RequiredPlugin pluginName="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin pluginName="SofaCUDA"/> <!-- Needed to use components [OglModel] -->
      
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
        
        <Node name="TetrahedronCorotationalFEMForceField-GPU-Green">
            <Node name="Beam">
                <RegularGridTopology name="grid" n="40 10 10" min="0 6 -2" max="16 10 2" />
                <TetrahedronSetTopologyContainer name="BeamTopo" />
                <TetrahedronSetTopologyModifier name="Modifier" />
    
                <Hexa2TetraTopologicalMapping input="@grid" output="@BeamTopo" />
            </Node>
            
            <Node name="Simulated">
                <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="20" name="linear solver" tolerance="1.0e-12" threshold="1.0e-12" />
                
                <MechanicalObject position="@../Beam/grid.position" name="Volume" template="CudaVec3f"/>
    
                <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
    
                <DiagonalMass totalMass="50.0" />
                <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
                
                <FixedProjectiveConstraint indices="@ROI1.indices" />
                <TetrahedronCorotationalFEMForceField name="FEM" template="CudaVec3f" youngModulus="2000" poissonRatio="0.3" />
                <Node name="surface">
                    <TriangleSetTopologyContainer name="Container" />
                    <TriangleSetTopologyModifier name="Modifier" />
                    <TriangleSetGeometryAlgorithms template="CudaVec3f" name="GeomAlgo" />
                    
                    <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
                    <Node name="Visu">
                        <OglModel name="Visual" color="green" />
                        <IdentityMapping input="@../../Volume" output="@Visual" />
                    </Node>
                </Node>
            </Node>  
        </Node>
        
    
        <Node name="TetrahedronCorotationalFEMForceField-CPU-red">
            <Node name="Beam">
                <RegularGridTopology name="grid" n="40 10 10" min="0 6 -2" max="16 10 2" />
                <TetrahedronSetTopologyContainer name="BeamTopo" />
                <TetrahedronSetTopologyModifier name="Modifier" />
    
                <Hexa2TetraTopologicalMapping input="@grid" output="@BeamTopo" />
            </Node>
            
            <Node name="Simulated">
                <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="20" name="linear solver" tolerance="1.0e-12" threshold="1.0e-12" />
                
                <MechanicalObject position="@../Beam/grid.position" name="Volume" template="Vec3d"/>
    
                <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
    
                <DiagonalMass totalMass="50.0" />
                <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
                
                <FixedProjectiveConstraint indices="@ROI1.indices" />
                <TetrahedronCorotationalFEMForceField name="FEM" youngModulus="2000" poissonRatio="0.3" />
                <Node name="surface">
                    <TriangleSetTopologyContainer name="Container" />
                    <TriangleSetTopologyModifier name="Modifier" />
                    <TriangleSetGeometryAlgorithms template="Vec3d" name="GeomAlgo" />
                    
                    <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
                    <Node name="Visu">
                        <OglModel name="Visual" color="red" />
                        <IdentityMapping input="@../../Volume" output="@Visual" />
                    </Node>
                </Node>
            </Node> 
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9 0", dt="0.02")

       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', pluginName="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', pluginName="SofaCUDA")
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )

       tetrahedron_corotational_fem_force_field__gpu__green = root.addChild('TetrahedronCorotationalFEMForceField-GPU-Green')

       beam = TetrahedronCorotationalFEMForceField-GPU-Green.addChild('Beam')

       beam.addObject('RegularGridTopology', name="grid", n="40 10 10", min="0 6 -2", max="16 10 2")
       beam.addObject('TetrahedronSetTopologyContainer', name="BeamTopo")
       beam.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@BeamTopo")

       simulated = TetrahedronCorotationalFEMForceField-GPU-Green.addChild('Simulated')

       simulated.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       simulated.addObject('CGLinearSolver', iterations="20", name="linear solver", tolerance="1.0e-12", threshold="1.0e-12")
       simulated.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="CudaVec3f")
       simulated.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
       simulated.addObject('DiagonalMass', totalMass="50.0")
       simulated.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
       simulated.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
       simulated.addObject('TetrahedronCorotationalFEMForceField', name="FEM", template="CudaVec3f", youngModulus="2000", poissonRatio="0.3")

       surface = Simulated.addChild('surface')

       surface.addObject('TriangleSetTopologyContainer', name="Container")
       surface.addObject('TriangleSetTopologyModifier', name="Modifier")
       surface.addObject('TriangleSetGeometryAlgorithms', template="CudaVec3f", name="GeomAlgo")
       surface.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")

       visu = surface.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="green")
       visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")

       tetrahedron_corotational_fem_force_field__cpu_red = root.addChild('TetrahedronCorotationalFEMForceField-CPU-red')

       beam = TetrahedronCorotationalFEMForceField-CPU-red.addChild('Beam')

       beam.addObject('RegularGridTopology', name="grid", n="40 10 10", min="0 6 -2", max="16 10 2")
       beam.addObject('TetrahedronSetTopologyContainer', name="BeamTopo")
       beam.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       beam.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@BeamTopo")

       simulated = TetrahedronCorotationalFEMForceField-CPU-red.addChild('Simulated')

       simulated.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       simulated.addObject('CGLinearSolver', iterations="20", name="linear solver", tolerance="1.0e-12", threshold="1.0e-12")
       simulated.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="Vec3d")
       simulated.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
       simulated.addObject('DiagonalMass', totalMass="50.0")
       simulated.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
       simulated.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
       simulated.addObject('TetrahedronCorotationalFEMForceField', name="FEM", youngModulus="2000", poissonRatio="0.3")

       surface = Simulated.addChild('surface')

       surface.addObject('TriangleSetTopologyContainer', name="Container")
       surface.addObject('TriangleSetTopologyModifier', name="Modifier")
       surface.addObject('TriangleSetGeometryAlgorithms', template="Vec3d", name="GeomAlgo")
       surface.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")

       visu = surface.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="red")
       visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

