<!-- generate_doc -->
# VariationalSymplecticSolver

Implicit time integrator which conserves linear momentum and mechanical energy.


__Target__: Sofa.Component.ODESolver.Backward

__namespace__: sofa::component::odesolver::backward

__parents__:

- OdeSolver
- LinearSolverAccessor

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
		<td>newtonError</td>
		<td>
Error tolerance for Newton iterations
		</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>steps</td>
		<td>
Maximum number of Newton steps
		</td>
		<td>5</td>
	</tr>
	<tr>
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping coefficient related to stiffness, > 0
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>rayleighMass</td>
		<td>
Rayleigh damping coefficient related to mass, > 0
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>saveEnergyInFile</td>
		<td>
If kinetic and potential energies should be dumped in a CSV file at each iteration
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>explicitIntegration</td>
		<td>
Use explicit integration scheme
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>file</td>
		<td>
File name where kinetic and potential energies are saved in a CSV file
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeHamiltonian</td>
		<td>
Compute hamiltonian
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>hamiltonianEnergy</td>
		<td>
hamiltonian energy
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>useIncrementalPotentialEnergy</td>
		<td>
use real potential energy, if false use approximate potential energy
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>threadSafeVisitor</td>
		<td>
If true, do not use realloc and free visitors in fwdInteractionForceField.
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
|linearSolver|Linear solver used by this component|LinearSolver|

## Examples 

VariationalSymplecticSolver.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [VariationalSymplecticSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <DefaultAnimationLoop/>
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <Node name="Single">
    	<VariationalSymplecticSolver name="default0"  tags="meca" rayleighStiffness="0" rayleighMass="0" newtonError="1e-12" steps="4" file="energy.txt" saveEnergyInFile ="true"/>
            <CGLinearSolver template="GraphScattered" name="cGLinearSolver1" iterations="300"  tolerance="1e-09"  threshold="1e-9"/>
            <Node name="M1">
                <MechanicalObject />
                <UniformMass vertexMass="1" />
                <RegularGridTopology nx="4" ny="4" nz="28" xmin="-9" xmax="-6" ymin="0" ymax="3" zmin="0" zmax="27" />
                <BoxConstraint box="-9.1 -0.1 -0.1 -5.9 3.1 0.1" />
                <!--<BoxConstraint box="-9.1 -0.1 26.9 -5.9 3.1 27.1" />-->
                <TetrahedronFEMForceField name="FEM" youngModulus="100000" poissonRatio="0.3" />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")

       single = root.addChild('Single')

       single.addObject('VariationalSymplecticSolver', name="default0", tags="meca", rayleighStiffness="0", rayleighMass="0", newtonError="1e-12", steps="4", file="energy.txt", saveEnergyInFile="true")
       single.addObject('CGLinearSolver', template="GraphScattered", name="cGLinearSolver1", iterations="300", tolerance="1e-09", threshold="1e-9")

       m1 = Single.addChild('M1')

       m1.addObject('MechanicalObject', )
       m1.addObject('UniformMass', vertexMass="1")
       m1.addObject('RegularGridTopology', nx="4", ny="4", nz="28", xmin="-9", xmax="-6", ymin="0", ymax="3", zmin="0", zmax="27")
       m1.addObject('BoxConstraint', box="-9.1 -0.1 -0.1 -5.9 3.1 0.1")
       m1.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="100000", poissonRatio="0.3")
    ```

