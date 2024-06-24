# ParallelTetrahedronFEMForceField

Parallel tetrahedral finite elements


__Templates__:

- `#!c++ Vec3d`

__Target__: `MultiThreading`

__namespace__: `#!c++ multithreading::component::solidmechanics::fem::elastic`

__parents__: 

- `#!c++ TetrahedronFEMForceField`

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
		<td>initialPoints</td>
		<td>
Initial Position
</td>
		<td></td>
	</tr>
	<tr>
		<td>method</td>
		<td>
"small", "large" (by QR), "polar" or "svd" displacements
</td>
		<td>large</td>
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
		<td></td>
	</tr>
	<tr>
		<td>localStiffnessFactor</td>
		<td>
Allow specification of different stiffness per element. If there are N element and M values are specified, the youngModulus factor for element i would be localStiffnessFactor[i*M/N]
</td>
		<td></td>
	</tr>
	<tr>
		<td>updateStiffnessMatrix</td>
		<td>

</td>
		<td>0</td>
	</tr>
	<tr>
		<td>computeGlobalMatrix</td>
		<td>

</td>
		<td>0</td>
	</tr>
	<tr>
		<td>plasticMaxThreshold</td>
		<td>
Plastic Max Threshold (2-norm of the strain)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>plasticYieldThreshold</td>
		<td>
Plastic Yield Threshold (2-norm of the strain)
</td>
		<td>0.0001</td>
	</tr>
	<tr>
		<td>plasticCreep</td>
		<td>
Plastic Creep Factor * dt [0,1]. Warning this factor depends on dt.
</td>
		<td>0.9</td>
	</tr>
	<tr>
		<td>gatherPt</td>
		<td>
number of dof accumulated per threads during the gather operation (Only use in GPU version)
</td>
		<td></td>
	</tr>
	<tr>
		<td>gatherBsize</td>
		<td>
number of dof accumulated per threads during the gather operation (Only use in GPU version)
</td>
		<td></td>
	</tr>
	<tr>
		<td>computeVonMisesStress</td>
		<td>
compute and display von Mises stress: 0: no computations, 1: using corotational strain, 2: using full Green strain. Set listening=1
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>vonMisesPerElement</td>
		<td>
von Mises Stress per element
</td>
		<td></td>
	</tr>
	<tr>
		<td>vonMisesPerNode</td>
		<td>
von Mises Stress per node
</td>
		<td></td>
	</tr>
	<tr>
		<td>vonMisesStressColors</td>
		<td>
Vector of colors describing the VonMises stress
</td>
		<td></td>
	</tr>
	<tr>
		<td>updateStiffness</td>
		<td>
udpate structures (precomputed in init) using stiffness parameters in each iteration (set listening=1)
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
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawHeterogeneousTetra</td>
		<td>
Draw Heterogeneous Tetra in different color
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showStressColorMap</td>
		<td>
Color map used to show stress values
</td>
		<td>Blue to Red</td>
	</tr>
	<tr>
		<td>showStressAlpha</td>
		<td>
Alpha for vonMises visualisation
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>showVonMisesStressPerNode</td>
		<td>
draw points showing vonMises stress interpolated in nodes
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showVonMisesStressPerNodeColorMap</td>
		<td>
draw elements showing vonMises stress interpolated in nodes
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showVonMisesStressPerElement</td>
		<td>
draw triangles showing vonMises stress interpolated in elements
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showElementGapScale</td>
		<td>
draw gap between elements (when showWireFrame is disabled) [0,1]: 0: no gap, 1: no element
</td>
		<td>0.333</td>
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
|topology|link to the tetrahedron topology container|



## Examples

MultiThreading/share/sofa/examples/MultiThreading/ParallelTetrahedronFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <Node name="BeamFEM_LARGE">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9"/>
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3d" translation="11 0 0"/>
    
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3d" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <ParallelTetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false"
                                      method="large" computeVonMisesStress="1" showVonMisesStressPerElement="true"/>
    
            <BoxROI template="Vec3d" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3d" indices="@box_roi.indices" />
        </Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 -9 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")

        BeamFEM_LARGE = root.addChild('BeamFEM_LARGE')
        BeamFEM_LARGE.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        BeamFEM_LARGE.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        BeamFEM_LARGE.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
        BeamFEM_LARGE.addObject('MechanicalObject', template="Vec3d", translation="11 0 0")
        BeamFEM_LARGE.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
        BeamFEM_LARGE.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        BeamFEM_LARGE.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3d", name="GeomAlgo")
        BeamFEM_LARGE.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
        BeamFEM_LARGE.addObject('DiagonalMass', massDensity="0.2")
        BeamFEM_LARGE.addObject('ParallelTetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large", computeVonMisesStress="1", showVonMisesStressPerElement="true")
        BeamFEM_LARGE.addObject('BoxROI', template="Vec3d", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
        BeamFEM_LARGE.addObject('FixedProjectiveConstraint', template="Vec3d", indices="@box_roi.indices")
    ```

