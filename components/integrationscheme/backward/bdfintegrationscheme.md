<!-- generate_doc -->
# BDFIntegrationScheme

Time integrator using Backward Differential Formula implicit scheme.


__Target__: Sofa.Component.IntegrationScheme.Backward

__namespace__: sofa::component::integrationscheme::backward

__parents__:

- LinearMultistepIntegrationScheme

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
		<td>firstOrder</td>
		<td>
Use this ODE to integrate first order ODE. This will replace the dynamic equation from Ma=f(x,v) to Mv=f(x), meaning that the mass component now acts as capacity.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>computeFinalAcceleration</td>
		<td>
If true the integration scheme will compute the total acceleration of the timestep after updating the positions. If false, the acceleration vector is only a result of an internal computation.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>impulseBased</td>
		<td>
If true the integration scheme will compute the right-hand-side in term of impulse instead of forces.
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>order</td>
		<td>
Order of the Backward Differential Formula.
		</td>
		<td>2</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|linearSolver|Linear solver used by this component|LinearSolver|

