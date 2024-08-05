# NearestPointROI

Attach given pair of particles, projecting the positions of the second particles to the first ones
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Rigid2d`
- `#!c++ Rigid3d`
- `#!c++ Vec1d`
- `#!c++ Vec2d`
- `#!c++ Vec3d`
- `#!c++ Vec6d`

__Target__: `Sofa.Component.Engine.Select`

__namespace__: `#!c++ sofa::component::engine::select`

__parents__: 

- `#!c++ DataEngine`
- `#!c++ PairStateAccessor`

__categories__: 

- Engine

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
		<td>inputIndices1</td>
		<td>
Indices of the points to consider on the first model
</td>
		<td></td>
	</tr>
	<tr>
		<td>inputIndices2</td>
		<td>
Indices of the points to consider on the first model
</td>
		<td></td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Radius to search corresponding fixed point
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>useRestPosition</td>
		<td>
If true will use restPosition only at init
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>indices1</td>
		<td>
Indices from the first model associated to a dof from the second model
</td>
		<td></td>
	</tr>
	<tr>
		<td>indices2</td>
		<td>
Indices from the second model associated to a dof from the first model
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
		<td>indexPairs</td>
		<td>
list of couples (parent index + index in the parent)
</td>
		<td></td>
	</tr>
	<tr>
		<td>distances</td>
		<td>
List of distances between pairs of points
</td>
		<td></td>
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
|object1|First object associated to this component|
|object2|Second object associated to this component|



## Examples

Component/Engine/Select/NearestPointROI.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02">
        <Node name="requiredPlugins">
            <RequiredPlugin name="Sofa.Component.AnimationLoop"/> <!-- Needed to use components [FreeMotionAnimationLoop] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [UncoupledConstraintCorrection] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [BilateralLagrangianConstraint] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Solver"/> <!-- Needed to use components [GenericConstraintSolver] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI NearestPointROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [SubsetMultiMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [EdgeSetTopologyContainer] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        </Node>
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields showInteractionForceFields" />
    
        <FreeMotionAnimationLoop parallelODESolving="true"/>
        <GenericConstraintSolver tolerance="0.001" maxIterations="1000" resolutionMethod="UnbuildGaussSeidel" multithreading="true"/>
    
        <!--
            This Node shows how NearestPointROI is used to create constraints to link close vertices
        -->
        <Node name="ObjectsAttachedWithConstraints">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <Node name="M1">
                <MechanicalObject name="mo"/>
                <UniformMass totalMass="160" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="0" xmax="3" ymin="0" ymax="3" zmin="0" zmax="9" />
                <BoxROI box="-0.1 -0.1 -0.1 3.1 3.1 0.1" name="box"/>
                <FixedProjectiveConstraint indices="@box.indices"/>
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" computeVonMisesStress="1" showVonMisesStressPerElement="true"/>
                <UncoupledConstraintCorrection useOdeSolverIntegrationFactors="0"/>
            </Node>
            <Node name="M2">
                <MechanicalObject name="mo"/>
                <UniformMass totalMass="160" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="0" xmax="3" ymin="0" ymax="3" zmin="9" zmax="18" />
                <TetrahedronFEMForceField name="FEM" youngModulus="20000" poissonRatio="0.3" computeVonMisesStress="1" showVonMisesStressPerElement="true"/>
                <UncoupledConstraintCorrection useOdeSolverIntegrationFactors="0"/>
            </Node>
            <Node name="M3">
                <MechanicalObject name="mo"/>
                <UniformMass totalMass="160" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="0" xmax="3" ymin="0" ymax="3" zmin="18" zmax="27" />
                <BoxROI box="-0.1 -0.1 26.99 3.1 3.1 27.1" name="box"/>
                <FixedProjectiveConstraint indices="@box.indices"/>
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" computeVonMisesStress="1" showVonMisesStressPerElement="true"/>
                <UncoupledConstraintCorrection useOdeSolverIntegrationFactors="0"/>
            </Node>
    
            <NearestPointROI template="Vec3" name="np1" object1="@./M1/mo" object2="@./M2/mo" radius="0.1"/>
            <NearestPointROI template="Vec3" name="np2" object1="@./M2/mo" object2="@./M3/mo" radius="0.1"/>
    
            <BilateralLagrangianConstraint template="Vec3" object1="@M1" object2="@M2" first_point="@np1.indices1" second_point="@np1.indices2" />
            <BilateralLagrangianConstraint template="Vec3" object1="@M2" object2="@M3" first_point="@np2.indices1" second_point="@np2.indices2" />
        </Node>
    
        <!--
            This Node shows how NearestPointROI is used to create SubsetMultiMapping and EdgeSetTopologyContainer.
        -->
        <Node name="Springs">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <Node name="M1">
                <MechanicalObject name="mo"/>
                <UniformMass totalMass="160" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="4" xmax="7" ymin="0" ymax="3" zmin="0" zmax="9" />
                <BoxROI box="3.9 -0.1 -0.1 7.1 3.1 0.1" name="box"/>
                <FixedProjectiveConstraint indices="@box.indices"/>
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" computeVonMisesStress="1" showVonMisesStressPerElement="true"/>
                <UncoupledConstraintCorrection useOdeSolverIntegrationFactors="0"/>
            </Node>
            <Node name="M2"> <!-- This object has a higher resolution than the others -->
                <MechanicalObject name="mo"/>
                <UniformMass totalMass="160" />
                <RegularGridTopology nx="8" ny="8" nz="20" xmin="4" xmax="7" ymin="0" ymax="3" zmin="9" zmax="18" />
                <TetrahedronFEMForceField name="FEM" youngModulus="20000" poissonRatio="0.3" computeVonMisesStress="1" showVonMisesStressPerElement="true"/>
                <UncoupledConstraintCorrection useOdeSolverIntegrationFactors="0"/>
            </Node>
            <Node name="M3">
                <MechanicalObject name="mo"/>
                <UniformMass totalMass="160" />
                <RegularGridTopology nx="4" ny="4" nz="10" xmin="4" xmax="7" ymin="0" ymax="3" zmin="18" zmax="27" />
                <BoxROI box="3.9 -0.1 26.99 7.1 3.1 27.1" name="box"/>
                <FixedProjectiveConstraint indices="@box.indices"/>
                <TetrahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" computeVonMisesStress="1" showVonMisesStressPerElement="true"/>
                <UncoupledConstraintCorrection useOdeSolverIntegrationFactors="0"/>
            </Node>
    
            <!--
                In the following Nodes, dofs from 2 mechanical objects are fused into a new mechanical object, based on the
                minimal distance between points.
                A mapping links the three objects. An edge topology is created.
                Springs are created based on the topology.
            -->
            <Node name="merge1">
                <BoxROI name="box1" position="@../M1/mo.position" box="3.9 -0.1 8.9 7.1 3.1 9.1"/>
                <BoxROI name="box2" position="@../M2/mo.position" box="3.9 -0.1 8.9 7.1 3.1 9.1"/>
                <NearestPointROI template="Vec3" name="np" object1="@../M1/mo" object2="@../M2/mo" radius="1e5" inputIndices1="@box1.indices" inputIndices2="@box2.indices"/>
                <MechanicalObject name="dofs"/>
                <SubsetMultiMapping input="@../M1/mo @../M2/mo" output="@dofs" indexPairs="@np.indexPairs"/>
                <EdgeSetTopologyContainer edges="@np.edges"/>
                <MeshSpringForceField stiffness="10000" damping="1" linesStiffness="10000" linesDamping="1" drawMode="1" drawSpringSize="1"/>
            </Node>
    
            <Node name="merge2">
                <BoxROI name="box1" position="@../M2/mo.position" box="3.9 -0.1 17.9 7.1 3.1 18.1"/>
                <BoxROI name="box2" position="@../M3/mo.position" box="3.9 -0.1 17.9 7.1 3.1 18.1"/>
                <NearestPointROI template="Vec3" name="np" object1="@../M2/mo" object2="@../M3/mo" radius="1e5" inputIndices1="@box1.indices" inputIndices2="@box2.indices"/>
                <MechanicalObject name="dofs"/>
                <SubsetMultiMapping input="@../M2/mo @../M3/mo" output="@dofs" indexPairs="@np.indexPairs"/>
                <EdgeSetTopologyContainer edges="@np.edges"/>
                <MeshSpringForceField stiffness="10000" damping="1" linesStiffness="10000" linesDamping="1" drawMode="1" drawSpringSize="1"/>
            </Node>
    
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.02")

        requiredPlugins = root.addChild('requiredPlugins')
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.AnimationLoop")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Solver")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        requiredPlugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showInteractionForceFields")
        root.addObject('FreeMotionAnimationLoop', parallelODESolving="true")
        root.addObject('GenericConstraintSolver', tolerance="0.001", maxIterations="1000", resolutionMethod="UnbuildGaussSeidel", multithreading="true")

        ObjectsAttachedWithConstraints = root.addChild('ObjectsAttachedWithConstraints')
        ObjectsAttachedWithConstraints.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        ObjectsAttachedWithConstraints.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")

        M1 = ObjectsAttachedWithConstraints.addChild('M1')
        M1.addObject('MechanicalObject', name="mo")
        M1.addObject('UniformMass', totalMass="160")
        M1.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="0", xmax="3", ymin="0", ymax="3", zmin="0", zmax="9")
        M1.addObject('BoxROI', box="-0.1 -0.1 -0.1 3.1 3.1 0.1", name="box")
        M1.addObject('FixedProjectiveConstraint', indices="@box.indices")
        M1.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", computeVonMisesStress="1", showVonMisesStressPerElement="true")
        M1.addObject('UncoupledConstraintCorrection', useOdeSolverIntegrationFactors="0")

        M2 = ObjectsAttachedWithConstraints.addChild('M2')
        M2.addObject('MechanicalObject', name="mo")
        M2.addObject('UniformMass', totalMass="160")
        M2.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="0", xmax="3", ymin="0", ymax="3", zmin="9", zmax="18")
        M2.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="20000", poissonRatio="0.3", computeVonMisesStress="1", showVonMisesStressPerElement="true")
        M2.addObject('UncoupledConstraintCorrection', useOdeSolverIntegrationFactors="0")

        M3 = ObjectsAttachedWithConstraints.addChild('M3')
        M3.addObject('MechanicalObject', name="mo")
        M3.addObject('UniformMass', totalMass="160")
        M3.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="0", xmax="3", ymin="0", ymax="3", zmin="18", zmax="27")
        M3.addObject('BoxROI', box="-0.1 -0.1 26.99 3.1 3.1 27.1", name="box")
        M3.addObject('FixedProjectiveConstraint', indices="@box.indices")
        M3.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", computeVonMisesStress="1", showVonMisesStressPerElement="true")
        M3.addObject('UncoupledConstraintCorrection', useOdeSolverIntegrationFactors="0")
        ObjectsAttachedWithConstraints.addObject('NearestPointROI', template="Vec3", name="np1", object1="@./M1/mo", object2="@./M2/mo", radius="0.1")
        ObjectsAttachedWithConstraints.addObject('NearestPointROI', template="Vec3", name="np2", object1="@./M2/mo", object2="@./M3/mo", radius="0.1")
        ObjectsAttachedWithConstraints.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@M1", object2="@M2", first_point="@np1.indices1", second_point="@np1.indices2")
        ObjectsAttachedWithConstraints.addObject('BilateralLagrangianConstraint', template="Vec3", object1="@M2", object2="@M3", first_point="@np2.indices1", second_point="@np2.indices2")

        Springs = root.addChild('Springs')
        Springs.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        Springs.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")

        M1 = Springs.addChild('M1')
        M1.addObject('MechanicalObject', name="mo")
        M1.addObject('UniformMass', totalMass="160")
        M1.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="4", xmax="7", ymin="0", ymax="3", zmin="0", zmax="9")
        M1.addObject('BoxROI', box="3.9 -0.1 -0.1 7.1 3.1 0.1", name="box")
        M1.addObject('FixedProjectiveConstraint', indices="@box.indices")
        M1.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", computeVonMisesStress="1", showVonMisesStressPerElement="true")
        M1.addObject('UncoupledConstraintCorrection', useOdeSolverIntegrationFactors="0")

        M2 = Springs.addChild('M2')
        M2.addObject('MechanicalObject', name="mo")
        M2.addObject('UniformMass', totalMass="160")
        M2.addObject('RegularGridTopology', nx="8", ny="8", nz="20", xmin="4", xmax="7", ymin="0", ymax="3", zmin="9", zmax="18")
        M2.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="20000", poissonRatio="0.3", computeVonMisesStress="1", showVonMisesStressPerElement="true")
        M2.addObject('UncoupledConstraintCorrection', useOdeSolverIntegrationFactors="0")

        M3 = Springs.addChild('M3')
        M3.addObject('MechanicalObject', name="mo")
        M3.addObject('UniformMass', totalMass="160")
        M3.addObject('RegularGridTopology', nx="4", ny="4", nz="10", xmin="4", xmax="7", ymin="0", ymax="3", zmin="18", zmax="27")
        M3.addObject('BoxROI', box="3.9 -0.1 26.99 7.1 3.1 27.1", name="box")
        M3.addObject('FixedProjectiveConstraint', indices="@box.indices")
        M3.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", computeVonMisesStress="1", showVonMisesStressPerElement="true")
        M3.addObject('UncoupledConstraintCorrection', useOdeSolverIntegrationFactors="0")

        merge1 = Springs.addChild('merge1')
        merge1.addObject('BoxROI', name="box1", position="@../M1/mo.position", box="3.9 -0.1 8.9 7.1 3.1 9.1")
        merge1.addObject('BoxROI', name="box2", position="@../M2/mo.position", box="3.9 -0.1 8.9 7.1 3.1 9.1")
        merge1.addObject('NearestPointROI', template="Vec3", name="np", object1="@../M1/mo", object2="@../M2/mo", radius="1e5", inputIndices1="@box1.indices", inputIndices2="@box2.indices")
        merge1.addObject('MechanicalObject', name="dofs")
        merge1.addObject('SubsetMultiMapping', input="@../M1/mo @../M2/mo", output="@dofs", indexPairs="@np.indexPairs")
        merge1.addObject('EdgeSetTopologyContainer', edges="@np.edges")
        merge1.addObject('MeshSpringForceField', stiffness="10000", damping="1", linesStiffness="10000", linesDamping="1", drawMode="1", drawSpringSize="1")

        merge2 = Springs.addChild('merge2')
        merge2.addObject('BoxROI', name="box1", position="@../M2/mo.position", box="3.9 -0.1 17.9 7.1 3.1 18.1")
        merge2.addObject('BoxROI', name="box2", position="@../M3/mo.position", box="3.9 -0.1 17.9 7.1 3.1 18.1")
        merge2.addObject('NearestPointROI', template="Vec3", name="np", object1="@../M2/mo", object2="@../M3/mo", radius="1e5", inputIndices1="@box1.indices", inputIndices2="@box2.indices")
        merge2.addObject('MechanicalObject', name="dofs")
        merge2.addObject('SubsetMultiMapping', input="@../M2/mo @../M3/mo", output="@dofs", indexPairs="@np.indexPairs")
        merge2.addObject('EdgeSetTopologyContainer', edges="@np.edges")
        merge2.addObject('MeshSpringForceField', stiffness="10000", damping="1", linesStiffness="10000", linesDamping="1", drawMode="1", drawSpringSize="1")
    ```

