# StiffSpringForceField

Stiff springs for implicit integration
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Rigid3d`
- `#!c++ Vec1d`
- `#!c++ Vec2d`
- `#!c++ Vec3d`
- `#!c++ Vec6d`

__Target__: `Sofa.Component.SolidMechanics.Spring`

__namespace__: `#!c++ sofa::component::solidmechanics::spring`

__parents__: 

- `#!c++ SpringForceField`

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
		<td>stiffness</td>
		<td>
uniform stiffness for the all springs
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
uniform damping for the all springs
</td>
		<td>5</td>
	</tr>
	<tr>
		<td>spring</td>
		<td>
pairs of indices, stiffness, damping, rest length
</td>
		<td></td>
	</tr>
	<tr>
		<td>springsIndices1</td>
		<td>
List of indices in springs from the first mstate
</td>
		<td></td>
	</tr>
	<tr>
		<td>springsIndices2</td>
		<td>
List of indices in springs from the second mstate
</td>
		<td></td>
	</tr>
	<tr>
		<td>indices1</td>
		<td>
Indices of the source points on the first model
</td>
		<td></td>
	</tr>
	<tr>
		<td>indices2</td>
		<td>
Indices of the fixed points on the second model
</td>
		<td></td>
	</tr>
	<tr>
		<td>lengths</td>
		<td>
List of lengths to create the springs. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, 0 will be applied everywhere
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showArrowSize</td>
		<td>
size of the axis
</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>drawMode</td>
		<td>
The way springs will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow
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
|mechanicalStates|List of mechanical states to which this component is associated|
|object1|First object associated to this component|
|object2|Second object associated to this component|



## Examples

Component/SolidMechanics/Spring/StiffSpringForceField_simple.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.005">
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [StiffSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <VisualStyle displayFlags="showCollision showInteractionForceFields showForceFields" />
    
        <DefaultAnimationLoop/>
        <DefaultVisualManagerLoop/>
    
        <EulerImplicitSolver name="odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
        <SparseLDLSolver template="CompressedRowSparseMatrixMat3x3"/>
    
        <Node name="fix">
            <MechanicalObject template="Vec3" name="dofs" position="0 0 0" showObject="true"/>
            <FixedProjectiveConstraint indices="0"/>
        </Node>
    
        <Node name="sphere1">
            <MechanicalObject template="Vec3" name="dofs" position="1 0 0" showObject="true"/>
            <UniformMass/>
            <SphereCollisionModel listRadius="0.25"/>
        </Node>
    
        <Node name="sphere2">
            <MechanicalObject template="Vec3" name="dofs" position="2 0 0" showObject="true"/>
            <UniformMass/>
            <SphereCollisionModel listRadius="0.25"/>
        </Node>
    
        <Node name="sphere3-4">
            <MechanicalObject template="Vec3" name="dofs" position="3 0 0 4 0 0" showObject="true"/>
            <UniformMass/>
            <SphereCollisionModel listRadius="0.25 0.25"/>
        </Node>
    
        <Node name="sphere5-6">
            <MechanicalObject template="Vec3" name="dofs" position="5 0 0 6 0 0" showObject="true"/>
            <UniformMass/>
            <SphereCollisionModel listRadius="0.25 0.25"/>
            <StiffSpringForceField template="Vec3" name="spring" spring="0 1 50 1 1" showArrowSize="0.05" drawMode="2"/>
        </Node>
    
        <StiffSpringForceField template="Vec3" name="spring1" object1="@fix/dofs"       object2="@sphere1/dofs"   spring="0 0 50 1 1"             showArrowSize="0.05" drawMode="2"/>
        <StiffSpringForceField template="Vec3" name="spring2" object1="@sphere1/dofs"   object2="@sphere2/dofs"   spring="0 0 50 1 1"             showArrowSize="0.05" drawMode="2"/>
        <StiffSpringForceField template="Vec3" name="spring3" object1="@sphere2/dofs"   object2="@sphere3-4/dofs" spring="0 0 50 1 1  0 1 50 1 1" showArrowSize="0.05" drawMode="2"/>
        <StiffSpringForceField template="Vec3" name="spring5" object1="@sphere3-4/dofs" object2="@sphere3-4/dofs" spring="0 1 50 1 1"             showArrowSize="0.05" drawMode="2"/>
        <StiffSpringForceField template="Vec3" name="spring6" object1="@sphere3-4/dofs" object2="@sphere5-6/dofs" spring="0 0 50 1 1  1 1 50 1 1" showArrowSize="0.05" drawMode="2"/>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.005")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showCollision showInteractionForceFields showForceFields")
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('EulerImplicitSolver', name="odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        root.addObject('SparseLDLSolver', template="CompressedRowSparseMatrixMat3x3")

        fix = root.addChild('fix')
        fix.addObject('MechanicalObject', template="Vec3", name="dofs", position="0 0 0", showObject="true")
        fix.addObject('FixedProjectiveConstraint', indices="0")

        sphere1 = root.addChild('sphere1')
        sphere1.addObject('MechanicalObject', template="Vec3", name="dofs", position="1 0 0", showObject="true")
        sphere1.addObject('UniformMass')
        sphere1.addObject('SphereCollisionModel', listRadius="0.25")

        sphere2 = root.addChild('sphere2')
        sphere2.addObject('MechanicalObject', template="Vec3", name="dofs", position="2 0 0", showObject="true")
        sphere2.addObject('UniformMass')
        sphere2.addObject('SphereCollisionModel', listRadius="0.25")

        sphere3-4 = root.addChild('sphere3-4')
        sphere3-4.addObject('MechanicalObject', template="Vec3", name="dofs", position="3 0 0 4 0 0", showObject="true")
        sphere3-4.addObject('UniformMass')
        sphere3-4.addObject('SphereCollisionModel', listRadius="0.25 0.25")

        sphere5-6 = root.addChild('sphere5-6')
        sphere5-6.addObject('MechanicalObject', template="Vec3", name="dofs", position="5 0 0 6 0 0", showObject="true")
        sphere5-6.addObject('UniformMass')
        sphere5-6.addObject('SphereCollisionModel', listRadius="0.25 0.25")
        sphere5-6.addObject('StiffSpringForceField', template="Vec3", name="spring", spring="0 1 50 1 1", showArrowSize="0.05", drawMode="2")
        root.addObject('StiffSpringForceField', template="Vec3", name="spring1", object1="@fix/dofs", object2="@sphere1/dofs", spring="0 0 50 1 1", showArrowSize="0.05", drawMode="2")
        root.addObject('StiffSpringForceField', template="Vec3", name="spring2", object1="@sphere1/dofs", object2="@sphere2/dofs", spring="0 0 50 1 1", showArrowSize="0.05", drawMode="2")
        root.addObject('StiffSpringForceField', template="Vec3", name="spring3", object1="@sphere2/dofs", object2="@sphere3-4/dofs", spring="0 0 50 1 1  0 1 50 1 1", showArrowSize="0.05", drawMode="2")
        root.addObject('StiffSpringForceField', template="Vec3", name="spring5", object1="@sphere3-4/dofs", object2="@sphere3-4/dofs", spring="0 1 50 1 1", showArrowSize="0.05", drawMode="2")
        root.addObject('StiffSpringForceField', template="Vec3", name="spring6", object1="@sphere3-4/dofs", object2="@sphere5-6/dofs", spring="0 0 50 1 1  1 1 50 1 1", showArrowSize="0.05", drawMode="2")
    ```

Component/SolidMechanics/Spring/StiffSpringForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node 	 name="root"  dt="0.005"  >
    	<RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
    	<RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
    	<RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
    	<RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
    	<RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
    	<RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [StiffSpringForceField] -->
    	<RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
    	<RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
    	<VisualStyle name="visualStyle1"  displayFlags="showBehaviorModels showForceFields showCollisionModels showMappings" />
    	<Node 	 name="Poutre1"  >
    		<EulerImplicitSolver name="cg_odesolver"  printLog="0"  rayleighStiffness="0.1" rayleighMass="0.1" />
    		<CGLinearSolver template="GraphScattered" name="linear solver"  iterations="25"  tolerance="1e-09"  threshold="1e-09" />
    		<Node 	 name="M1"  >
    			<MeshGmshLoader name="loader"  filename="mesh/smCube27.msh" />
    			<MechanicalObject template="Vec3" showObject="1" name="mObject1"  position="@loader.position"  velocity="0 0 0"  force="0 0 0"  externalForce="0 0 0"  derivX="0 0 0"  restScale="1" />
    			<UniformMass name="uniformMass1"  vertexMass="0.1" />
    			<FixedProjectiveConstraint template="Vec3" name="fixedProjectiveConstraint1"  indices="0 3 6 9 12 15 18 21 24" />
    			<StiffSpringForceField template="Vec3" name="InternalSprings1"  spring="0 9 100 5 3.5
     1 10 500 5 3.5
     2 11 500 5 3.5
     3 12 500 5 3.5
     4 13 500 5 3.5
     5 14 500 5 3.5
     6 15 500 5 3.5
     7 16 500 5 3.5
     8 17 500 5 3.5
     9 18 500 5 3.5
     10 19 500 5 3.5
     11 20 500 5 3.5
     12 21 500 5 3.5
     13 22 500 5 3.5
     14 23 500 5 3.5
     15 24 500 5 3.5
     16 25 500 5 3.5
     17 26 500 5 3.5
     0 3 500 5 3.5
     1 4 500 5 3.5
     2 5 500 5 3.5
     3 6 500 5 3.5
     4 7 500 5 3.5
     5 8 500 5 3.5
     9 12 500 5 3.5
     10 13 500 5 3.5
     11 14 500 5 3.5
     12 15 500 5 3.5
     13 16 500 5 3.5
     14 17 500 5 3.5
     18 21 500 5 3.5
     19 22 500 5 3.5
     20 23 500 5 3.5
     21 24 500 5 3.5
     22 25 500 5 3.5
     23 26 500 5 3.5
     0 1 500 5 3.5
     1 2 500 5 3.5
     3 4 500 5 3.5
     4 5 500 5 3.5
     6 7 500 5 3.5
     7 8 500 5 3.5
     9 10 500 5 3.5
     10 11 500 5 3.5
     12 13 500 5 3.5
     13 14 500 5 3.5
     15 16 500 5 3.5
     16 17 500 5 3.5
     18 19 500 5 3.5
     19 20 500 5 3.5
     21 22 500 5 3.5
     22 23 500 5 3.5
     24 25 500 5 3.5
     25 26 100 5 3.5
     0 13 500 5 6.06218
     1 14 500 5 6.06218
     3 16 500 5 6.06218
     4 17 500 5 6.06218
     9 22 500 5 6.06218
     10 23 500 5 6.06218
     12 25 500 5 6.06218
     13 26 500 5 6.06218
     9 4 500 5 6.06218
     10 5 500 5 6.06218
     12 7 500 5 6.06218
     13 8 500 5 6.06218
     18 13 500 5 6.06218
     19 14 500 5 6.06218
     21 16 500 5 6.06218
     22 17 500 5 6.06218
     3 10 500 5 6.06218
     4 11 500 5 6.06218
     6 13 500 5 6.06218
     7 14 500 5 6.06218
     12 19 500 5 6.06218
     13 20 500 5 6.06218
     15 22 500 5 6.06218
     16 23 500 5 6.06218
     12 1 500 5 6.06218
     13 2 500 5 6.06218
     15 4 500 5 6.06218
     16 5 500 5 6.06218
     21 10 500 5 6.06218
     22 11 500 5 6.06218
     24 13 500 5 6.06218
     25 14 500 5 6.06218
     0 12 500 5 4.94975
     1 13 500 5 4.94975
     2 14 500 5 4.94975
     3 15 500 5 4.94975
     4 16 500 5 4.94975
     5 17 500 5 4.94975
     9 21 500 5 4.94975
     10 22 500 5 4.94975
     11 23 500 5 4.94975
     12 24 500 5 4.94975
     13 25 500 5 4.94975
     14 26 500 5 4.94975
     3 9 500 5 4.94975
     4 10 500 5 4.94975
     5 11 500 5 4.94975
     6 12 500 5 4.94975
     7 13 500 5 4.94975
     8 14 500 5 4.94975
     12 18 500 5 4.94975
     13 19 500 5 4.94975
     14 20 500 5 4.94975
     15 21 500 5 4.94975
     16 22 500 5 4.94975
     17 23 500 5 4.94975
     0 10 500 5 4.94975
     1 11 500 5 4.94975
     3 13 500 5 4.94975
     4 14 500 5 4.94975
     6 16 500 5 4.94975
     7 17 500 5 4.94975
     9 19 500 5 4.94975
     10 20 500 5 4.94975
     12 22 500 5 4.94975
     13 23 500 5 4.94975
     15 25 500 5 4.94975
     16 26 500 5 4.94975
     9 1 500 5 4.94975
     10 2 500 5 4.94975
     12 4 500 5 4.94975
     13 5 500 5 4.94975
     15 7 500 5 4.94975
     16 8 500 5 4.94975
     18 10 500 5 4.94975
     19 11 500 5 4.94975
     21 13 500 5 4.94975
     22 14 500 5 4.94975
     24 16 500 5 4.94975
     25 17 500 5 4.94975
     0 4 500 5 4.94975
     1 5 500 5 4.94975
     3 7 500 5 4.94975
     4 8 500 5 4.94975
     9 13 500 5 4.94975
     10 14 500 5 4.94975
     12 16 500 5 4.94975
     13 17 500 5 4.94975
     18 22 500 5 4.94975
     19 23 500 5 4.94975
     21 25 500 5 4.94975
     22 26 500 5 4.94975
     3 1 500 5 4.94975
     4 2 500 5 4.94975
     6 4 500 5 4.94975
     7 5 500 5 4.94975
     12 10 500 5 4.94975
     13 11 500 5 4.94975
     15 13 500 5 4.94975
     16 14 500 5 4.94975
     21 19 500 5 4.94975
     22 20 500 5 4.94975
     24 22 500 5 4.94975
     25 23 500 5 4.94975
    "  />
    		</Node>
    		<Node 	 name="M5"  >
    			<MeshGmshLoader name="loader"  filename="mesh/smCube27.msh" />
    			<MechanicalObject template="Vec3" name="mObject5" showObject="1" position="@loader.position"  velocity="0 0 0"  force="0 0 0"  externalForce="0 0 0"  derivX="0 0 0"  restScale="1"  translation="0 0 42" />
    			<UniformMass name="uniformMass5"  vertexMass="0.1" />
    			<StiffSpringForceField template="Vec3" name="InternalSprings5"  spring="0 9 100 5 3.5
     1 10 500 5 3.5
     2 11 500 5 3.5
     3 12 500 5 3.5
     4 13 500 5 3.5
     5 14 500 5 3.5
     6 15 500 5 3.5
     7 16 500 5 3.5
     8 17 500 5 3.5
     9 18 500 5 3.5
     10 19 500 5 3.5
     11 20 500 5 3.5
     12 21 500 5 3.5
     13 22 500 5 3.5
     14 23 500 5 3.5
     15 24 500 5 3.5
     16 25 500 5 3.5
     17 26 500 5 3.5
     0 3 500 5 3.5
     1 4 500 5 3.5
     2 5 500 5 3.5
     3 6 500 5 3.5
     4 7 500 5 3.5
     5 8 500 5 3.5
     9 12 500 5 3.5
     10 13 500 5 3.5
     11 14 500 5 3.5
     12 15 500 5 3.5
     13 16 500 5 3.5
     14 17 500 5 3.5
     18 21 500 5 3.5
     19 22 500 5 3.5
     20 23 500 5 3.5
     21 24 500 5 3.5
     22 25 500 5 3.5
     23 26 500 5 3.5
     0 1 500 5 3.5
     1 2 500 5 3.5
     3 4 500 5 3.5
     4 5 500 5 3.5
     6 7 500 5 3.5
     7 8 500 5 3.5
     9 10 500 5 3.5
     10 11 500 5 3.5
     12 13 500 5 3.5
     13 14 500 5 3.5
     15 16 500 5 3.5
     16 17 500 5 3.5
     18 19 500 5 3.5
     19 20 500 5 3.5
     21 22 500 5 3.5
     22 23 500 5 3.5
     24 25 500 5 3.5
     25 26 100 5 3.5
     0 13 500 5 6.06218
     1 14 500 5 6.06218
     3 16 500 5 6.06218
     4 17 500 5 6.06218
     9 22 500 5 6.06218
     10 23 500 5 6.06218
     12 25 500 5 6.06218
     13 26 500 5 6.06218
     9 4 500 5 6.06218
     10 5 500 5 6.06218
     12 7 500 5 6.06218
     13 8 500 5 6.06218
     18 13 500 5 6.06218
     19 14 500 5 6.06218
     21 16 500 5 6.06218
     22 17 500 5 6.06218
     3 10 500 5 6.06218
     4 11 500 5 6.06218
     6 13 500 5 6.06218
     7 14 500 5 6.06218
     12 19 500 5 6.06218
     13 20 500 5 6.06218
     15 22 500 5 6.06218
     16 23 500 5 6.06218
     12 1 500 5 6.06218
     13 2 500 5 6.06218
     15 4 500 5 6.06218
     16 5 500 5 6.06218
     21 10 500 5 6.06218
     22 11 500 5 6.06218
     24 13 500 5 6.06218
     25 14 500 5 6.06218
     0 12 500 5 4.94975
     1 13 500 5 4.94975
     2 14 500 5 4.94975
     3 15 500 5 4.94975
     4 16 500 5 4.94975
     5 17 500 5 4.94975
     9 21 500 5 4.94975
     10 22 500 5 4.94975
     11 23 500 5 4.94975
     12 24 500 5 4.94975
     13 25 500 5 4.94975
     14 26 500 5 4.94975
     3 9 500 5 4.94975
     4 10 500 5 4.94975
     5 11 500 5 4.94975
     6 12 500 5 4.94975
     7 13 500 5 4.94975
     8 14 500 5 4.94975
     12 18 500 5 4.94975
     13 19 500 5 4.94975
     14 20 500 5 4.94975
     15 21 500 5 4.94975
     16 22 500 5 4.94975
     17 23 500 5 4.94975
     0 10 500 5 4.94975
     1 11 500 5 4.94975
     3 13 500 5 4.94975
     4 14 500 5 4.94975
     6 16 500 5 4.94975
     7 17 500 5 4.94975
     9 19 500 5 4.94975
     10 20 500 5 4.94975
     12 22 500 5 4.94975
     13 23 500 5 4.94975
     15 25 500 5 4.94975
     16 26 500 5 4.94975
     9 1 500 5 4.94975
     10 2 500 5 4.94975
     12 4 500 5 4.94975
     13 5 500 5 4.94975
     15 7 500 5 4.94975
     16 8 500 5 4.94975
     18 10 500 5 4.94975
     19 11 500 5 4.94975
     21 13 500 5 4.94975
     22 14 500 5 4.94975
     24 16 500 5 4.94975
     25 17 500 5 4.94975
     0 4 500 5 4.94975
     1 5 500 5 4.94975
     3 7 500 5 4.94975
     4 8 500 5 4.94975
     9 13 500 5 4.94975
     10 14 500 5 4.94975
     12 16 500 5 4.94975
     13 17 500 5 4.94975
     18 22 500 5 4.94975
     19 23 500 5 4.94975
     21 25 500 5 4.94975
     22 26 500 5 4.94975
     3 1 500 5 4.94975
     4 2 500 5 4.94975
     6 4 500 5 4.94975
     7 5 500 5 4.94975
     12 10 500 5 4.94975
     13 11 500 5 4.94975
     15 13 500 5 4.94975
     16 14 500 5 4.94975
     21 19 500 5 4.94975
     22 20 500 5 4.94975
     24 22 500 5 4.94975
     25 23 500 5 4.94975
    "   />
    		</Node>
    		<Node 	 name="M4"  >
    			<MeshGmshLoader name="loader"  filename="mesh/smCube27.msh" />
    			<MechanicalObject template="Vec3" name="mObject4" showObject="1" position="@loader.position"  velocity="0 0 0"  force="0 0 0"  externalForce="0 0 0"  derivX="0 0 0"  restScale="1"  translation="0 0 31.5" />
    			<UniformMass name="uniformMass4"  vertexMass="0.1" />
    			<StiffSpringForceField template="Vec3" name="InternalSprings4"  spring="0 9 100 5 3.5
     1 10 500 5 3.5
     2 11 500 5 3.5
     3 12 500 5 3.5
     4 13 500 5 3.5
     5 14 500 5 3.5
     6 15 500 5 3.5
     7 16 500 5 3.5
     8 17 500 5 3.5
     9 18 500 5 3.5
     10 19 500 5 3.5
     11 20 500 5 3.5
     12 21 500 5 3.5
     13 22 500 5 3.5
     14 23 500 5 3.5
     15 24 500 5 3.5
     16 25 500 5 3.5
     17 26 500 5 3.5
     0 3 500 5 3.5
     1 4 500 5 3.5
     2 5 500 5 3.5
     3 6 500 5 3.5
     4 7 500 5 3.5
     5 8 500 5 3.5
     9 12 500 5 3.5
     10 13 500 5 3.5
     11 14 500 5 3.5
     12 15 500 5 3.5
     13 16 500 5 3.5
     14 17 500 5 3.5
     18 21 500 5 3.5
     19 22 500 5 3.5
     20 23 500 5 3.5
     21 24 500 5 3.5
     22 25 500 5 3.5
     23 26 500 5 3.5
     0 1 500 5 3.5
     1 2 500 5 3.5
     3 4 500 5 3.5
     4 5 500 5 3.5
     6 7 500 5 3.5
     7 8 500 5 3.5
     9 10 500 5 3.5
     10 11 500 5 3.5
     12 13 500 5 3.5
     13 14 500 5 3.5
     15 16 500 5 3.5
     16 17 500 5 3.5
     18 19 500 5 3.5
     19 20 500 5 3.5
     21 22 500 5 3.5
     22 23 500 5 3.5
     24 25 500 5 3.5
     25 26 100 5 3.5
     0 13 500 5 6.06218
     1 14 500 5 6.06218
     3 16 500 5 6.06218
     4 17 500 5 6.06218
     9 22 500 5 6.06218
     10 23 500 5 6.06218
     12 25 500 5 6.06218
     13 26 500 5 6.06218
     9 4 500 5 6.06218
     10 5 500 5 6.06218
     12 7 500 5 6.06218
     13 8 500 5 6.06218
     18 13 500 5 6.06218
     19 14 500 5 6.06218
     21 16 500 5 6.06218
     22 17 500 5 6.06218
     3 10 500 5 6.06218
     4 11 500 5 6.06218
     6 13 500 5 6.06218
     7 14 500 5 6.06218
     12 19 500 5 6.06218
     13 20 500 5 6.06218
     15 22 500 5 6.06218
     16 23 500 5 6.06218
     12 1 500 5 6.06218
     13 2 500 5 6.06218
     15 4 500 5 6.06218
     16 5 500 5 6.06218
     21 10 500 5 6.06218
     22 11 500 5 6.06218
     24 13 500 5 6.06218
     25 14 500 5 6.06218
     0 12 500 5 4.94975
     1 13 500 5 4.94975
     2 14 500 5 4.94975
     3 15 500 5 4.94975
     4 16 500 5 4.94975
     5 17 500 5 4.94975
     9 21 500 5 4.94975
     10 22 500 5 4.94975
     11 23 500 5 4.94975
     12 24 500 5 4.94975
     13 25 500 5 4.94975
     14 26 500 5 4.94975
     3 9 500 5 4.94975
     4 10 500 5 4.94975
     5 11 500 5 4.94975
     6 12 500 5 4.94975
     7 13 500 5 4.94975
     8 14 500 5 4.94975
     12 18 500 5 4.94975
     13 19 500 5 4.94975
     14 20 500 5 4.94975
     15 21 500 5 4.94975
     16 22 500 5 4.94975
     17 23 500 5 4.94975
     0 10 500 5 4.94975
     1 11 500 5 4.94975
     3 13 500 5 4.94975
     4 14 500 5 4.94975
     6 16 500 5 4.94975
     7 17 500 5 4.94975
     9 19 500 5 4.94975
     10 20 500 5 4.94975
     12 22 500 5 4.94975
     13 23 500 5 4.94975
     15 25 500 5 4.94975
     16 26 500 5 4.94975
     9 1 500 5 4.94975
     10 2 500 5 4.94975
     12 4 500 5 4.94975
     13 5 500 5 4.94975
     15 7 500 5 4.94975
     16 8 500 5 4.94975
     18 10 500 5 4.94975
     19 11 500 5 4.94975
     21 13 500 5 4.94975
     22 14 500 5 4.94975
     24 16 500 5 4.94975
     25 17 500 5 4.94975
     0 4 500 5 4.94975
     1 5 500 5 4.94975
     3 7 500 5 4.94975
     4 8 500 5 4.94975
     9 13 500 5 4.94975
     10 14 500 5 4.94975
     12 16 500 5 4.94975
     13 17 500 5 4.94975
     18 22 500 5 4.94975
     19 23 500 5 4.94975
     21 25 500 5 4.94975
     22 26 500 5 4.94975
     3 1 500 5 4.94975
     4 2 500 5 4.94975
     6 4 500 5 4.94975
     7 5 500 5 4.94975
     12 10 500 5 4.94975
     13 11 500 5 4.94975
     15 13 500 5 4.94975
     16 14 500 5 4.94975
     21 19 500 5 4.94975
     22 20 500 5 4.94975
     24 22 500 5 4.94975
     25 23 500 5 4.94975
    "   />
    		</Node>
    		<Node 	 name="M3"  >
    			<MeshGmshLoader name="loader"  filename="mesh/smCube27.msh" />
    			<MechanicalObject template="Vec3" showObject="1" name="mObject3"  position="@loader.position"  velocity="0 0 0"  force="0 0 0"  externalForce="0 0 0"  derivX="0 0 0"  restScale="1"  translation="0 0 21" />
    			<UniformMass name="uniformMass3"  vertexMass="0.1" />
    			<StiffSpringForceField template="Vec3" name="InternalSprings3"  spring="0 9 100 5 3.5
     1 10 500 5 3.5
     2 11 500 5 3.5
     3 12 500 5 3.5
     4 13 500 5 3.5
     5 14 500 5 3.5
     6 15 500 5 3.5
     7 16 500 5 3.5
     8 17 500 5 3.5
     9 18 500 5 3.5
     10 19 500 5 3.5
     11 20 500 5 3.5
     12 21 500 5 3.5
     13 22 500 5 3.5
     14 23 500 5 3.5
     15 24 500 5 3.5
     16 25 500 5 3.5
     17 26 500 5 3.5
     0 3 500 5 3.5
     1 4 500 5 3.5
     2 5 500 5 3.5
     3 6 500 5 3.5
     4 7 500 5 3.5
     5 8 500 5 3.5
     9 12 500 5 3.5
     10 13 500 5 3.5
     11 14 500 5 3.5
     12 15 500 5 3.5
     13 16 500 5 3.5
     14 17 500 5 3.5
     18 21 500 5 3.5
     19 22 500 5 3.5
     20 23 500 5 3.5
     21 24 500 5 3.5
     22 25 500 5 3.5
     23 26 500 5 3.5
     0 1 500 5 3.5
     1 2 500 5 3.5
     3 4 500 5 3.5
     4 5 500 5 3.5
     6 7 500 5 3.5
     7 8 500 5 3.5
     9 10 500 5 3.5
     10 11 500 5 3.5
     12 13 500 5 3.5
     13 14 500 5 3.5
     15 16 500 5 3.5
     16 17 500 5 3.5
     18 19 500 5 3.5
     19 20 500 5 3.5
     21 22 500 5 3.5
     22 23 500 5 3.5
     24 25 500 5 3.5
     25 26 100 5 3.5
     0 13 500 5 6.06218
     1 14 500 5 6.06218
     3 16 500 5 6.06218
     4 17 500 5 6.06218
     9 22 500 5 6.06218
     10 23 500 5 6.06218
     12 25 500 5 6.06218
     13 26 500 5 6.06218
     9 4 500 5 6.06218
     10 5 500 5 6.06218
     12 7 500 5 6.06218
     13 8 500 5 6.06218
     18 13 500 5 6.06218
     19 14 500 5 6.06218
     21 16 500 5 6.06218
     22 17 500 5 6.06218
     3 10 500 5 6.06218
     4 11 500 5 6.06218
     6 13 500 5 6.06218
     7 14 500 5 6.06218
     12 19 500 5 6.06218
     13 20 500 5 6.06218
     15 22 500 5 6.06218
     16 23 500 5 6.06218
     12 1 500 5 6.06218
     13 2 500 5 6.06218
     15 4 500 5 6.06218
     16 5 500 5 6.06218
     21 10 500 5 6.06218
     22 11 500 5 6.06218
     24 13 500 5 6.06218
     25 14 500 5 6.06218
     0 12 500 5 4.94975
     1 13 500 5 4.94975
     2 14 500 5 4.94975
     3 15 500 5 4.94975
     4 16 500 5 4.94975
     5 17 500 5 4.94975
     9 21 500 5 4.94975
     10 22 500 5 4.94975
     11 23 500 5 4.94975
     12 24 500 5 4.94975
     13 25 500 5 4.94975
     14 26 500 5 4.94975
     3 9 500 5 4.94975
     4 10 500 5 4.94975
     5 11 500 5 4.94975
     6 12 500 5 4.94975
     7 13 500 5 4.94975
     8 14 500 5 4.94975
     12 18 500 5 4.94975
     13 19 500 5 4.94975
     14 20 500 5 4.94975
     15 21 500 5 4.94975
     16 22 500 5 4.94975
     17 23 500 5 4.94975
     0 10 500 5 4.94975
     1 11 500 5 4.94975
     3 13 500 5 4.94975
     4 14 500 5 4.94975
     6 16 500 5 4.94975
     7 17 500 5 4.94975
     9 19 500 5 4.94975
     10 20 500 5 4.94975
     12 22 500 5 4.94975
     13 23 500 5 4.94975
     15 25 500 5 4.94975
     16 26 500 5 4.94975
     9 1 500 5 4.94975
     10 2 500 5 4.94975
     12 4 500 5 4.94975
     13 5 500 5 4.94975
     15 7 500 5 4.94975
     16 8 500 5 4.94975
     18 10 500 5 4.94975
     19 11 500 5 4.94975
     21 13 500 5 4.94975
     22 14 500 5 4.94975
     24 16 500 5 4.94975
     25 17 500 5 4.94975
     0 4 500 5 4.94975
     1 5 500 5 4.94975
     3 7 500 5 4.94975
     4 8 500 5 4.94975
     9 13 500 5 4.94975
     10 14 500 5 4.94975
     12 16 500 5 4.94975
     13 17 500 5 4.94975
     18 22 500 5 4.94975
     19 23 500 5 4.94975
     21 25 500 5 4.94975
     22 26 500 5 4.94975
     3 1 500 5 4.94975
     4 2 500 5 4.94975
     6 4 500 5 4.94975
     7 5 500 5 4.94975
     12 10 500 5 4.94975
     13 11 500 5 4.94975
     15 13 500 5 4.94975
     16 14 500 5 4.94975
     21 19 500 5 4.94975
     22 20 500 5 4.94975
     24 22 500 5 4.94975
     25 23 500 5 4.94975
    "  />
    		</Node>
    		<Node 	 name="M2"  >
    			<MeshGmshLoader name="loader"  filename="mesh/smCube27.msh" />
    			<MechanicalObject template="Vec3" showObject="1" name="mObject2"  position="@loader.position"  velocity="0 0 0"  force="0 0 0"  externalForce="0 0 0"  derivX="0 0 0"  restScale="1"  translation="0 0 10.5" />
    			<UniformMass name="uniformMass2"  vertexMass="0.1" />
    			<StiffSpringForceField template="Vec3" name="InternalSprings2"  spring="0 9 100 5 3.5
     1 10 500 5 3.5
     2 11 500 5 3.5
     3 12 500 5 3.5
     4 13 500 5 3.5
     5 14 500 5 3.5
     6 15 500 5 3.5
     7 16 500 5 3.5
     8 17 500 5 3.5
     9 18 500 5 3.5
     10 19 500 5 3.5
     11 20 500 5 3.5
     12 21 500 5 3.5
     13 22 500 5 3.5
     14 23 500 5 3.5
     15 24 500 5 3.5
     16 25 500 5 3.5
     17 26 500 5 3.5
     0 3 500 5 3.5
     1 4 500 5 3.5
     2 5 500 5 3.5
     3 6 500 5 3.5
     4 7 500 5 3.5
     5 8 500 5 3.5
     9 12 500 5 3.5
     10 13 500 5 3.5
     11 14 500 5 3.5
     12 15 500 5 3.5
     13 16 500 5 3.5
     14 17 500 5 3.5
     18 21 500 5 3.5
     19 22 500 5 3.5
     20 23 500 5 3.5
     21 24 500 5 3.5
     22 25 500 5 3.5
     23 26 500 5 3.5
     0 1 500 5 3.5
     1 2 500 5 3.5
     3 4 500 5 3.5
     4 5 500 5 3.5
     6 7 500 5 3.5
     7 8 500 5 3.5
     9 10 500 5 3.5
     10 11 500 5 3.5
     12 13 500 5 3.5
     13 14 500 5 3.5
     15 16 500 5 3.5
     16 17 500 5 3.5
     18 19 500 5 3.5
     19 20 500 5 3.5
     21 22 500 5 3.5
     22 23 500 5 3.5
     24 25 500 5 3.5
     25 26 100 5 3.5
     0 13 500 5 6.06218
     1 14 500 5 6.06218
     3 16 500 5 6.06218
     4 17 500 5 6.06218
     9 22 500 5 6.06218
     10 23 500 5 6.06218
     12 25 500 5 6.06218
     13 26 500 5 6.06218
     9 4 500 5 6.06218
     10 5 500 5 6.06218
     12 7 500 5 6.06218
     13 8 500 5 6.06218
     18 13 500 5 6.06218
     19 14 500 5 6.06218
     21 16 500 5 6.06218
     22 17 500 5 6.06218
     3 10 500 5 6.06218
     4 11 500 5 6.06218
     6 13 500 5 6.06218
     7 14 500 5 6.06218
     12 19 500 5 6.06218
     13 20 500 5 6.06218
     15 22 500 5 6.06218
     16 23 500 5 6.06218
     12 1 500 5 6.06218
     13 2 500 5 6.06218
     15 4 500 5 6.06218
     16 5 500 5 6.06218
     21 10 500 5 6.06218
     22 11 500 5 6.06218
     24 13 500 5 6.06218
     25 14 500 5 6.06218
     0 12 500 5 4.94975
     1 13 500 5 4.94975
     2 14 500 5 4.94975
     3 15 500 5 4.94975
     4 16 500 5 4.94975
     5 17 500 5 4.94975
     9 21 500 5 4.94975
     10 22 500 5 4.94975
     11 23 500 5 4.94975
     12 24 500 5 4.94975
     13 25 500 5 4.94975
     14 26 500 5 4.94975
     3 9 500 5 4.94975
     4 10 500 5 4.94975
     5 11 500 5 4.94975
     6 12 500 5 4.94975
     7 13 500 5 4.94975
     8 14 500 5 4.94975
     12 18 500 5 4.94975
     13 19 500 5 4.94975
     14 20 500 5 4.94975
     15 21 500 5 4.94975
     16 22 500 5 4.94975
     17 23 500 5 4.94975
     0 10 500 5 4.94975
     1 11 500 5 4.94975
     3 13 500 5 4.94975
     4 14 500 5 4.94975
     6 16 500 5 4.94975
     7 17 500 5 4.94975
     9 19 500 5 4.94975
     10 20 500 5 4.94975
     12 22 500 5 4.94975
     13 23 500 5 4.94975
     15 25 500 5 4.94975
     16 26 500 5 4.94975
     9 1 500 5 4.94975
     10 2 500 5 4.94975
     12 4 500 5 4.94975
     13 5 500 5 4.94975
     15 7 500 5 4.94975
     16 8 500 5 4.94975
     18 10 500 5 4.94975
     19 11 500 5 4.94975
     21 13 500 5 4.94975
     22 14 500 5 4.94975
     24 16 500 5 4.94975
     25 17 500 5 4.94975
     0 4 500 5 4.94975
     1 5 500 5 4.94975
     3 7 500 5 4.94975
     4 8 500 5 4.94975
     9 13 500 5 4.94975
     10 14 500 5 4.94975
     12 16 500 5 4.94975
     13 17 500 5 4.94975
     18 22 500 5 4.94975
     19 23 500 5 4.94975
     21 25 500 5 4.94975
     22 26 500 5 4.94975
     3 1 500 5 4.94975
     4 2 500 5 4.94975
     6 4 500 5 4.94975
     7 5 500 5 4.94975
     12 10 500 5 4.94975
     13 11 500 5 4.94975
     15 13 500 5 4.94975
     16 14 500 5 4.94975
     21 19 500 5 4.94975
     22 20 500 5 4.94975
     24 22 500 5 4.94975
     25 23 500 5 4.94975
    "  />
    		</Node>
    		<StiffSpringForceField template="Vec3" name="ExternalSprings1"  spring="2 0 500 5 3.5
     5 3 500 5 3.5
     8 6 500 5 3.5
     11 9 500 5 3.5
     14 12 500 5 3.5
     17 15 500 5 3.5
     20 18 500 5 3.5
     23 21 500 5 3.5
     26 24 500 5 3.5
     14 0 500 5 6.06218
     17 3 500 5 6.06218
     23 9 500 5 6.06218
     26 12 500 5 6.06218
     5 9 500 5 6.06218
     8 12 500 5 6.06218
     14 18 500 5 6.06218
     17 21 500 5 6.06218
     11 3 500 5 6.06218
     14 6 500 5 6.06218
     20 12 500 5 6.06218
     23 15 500 5 6.06218
     2 12 500 5 6.06218
     5 15 500 5 6.06218
     11 21 500 5 6.06218
     14 24 500 5 6.06218
     11 0 500 5 4.94975
     14 3 500 5 4.94975
     17 6 500 5 4.94975
     20 9 500 5 4.94975
     23 12 500 5 4.94975
     26 15 500 5 4.94975
     2 9 500 5 4.94975
     5 12 500 5 4.94975
     8 15 500 5 4.94975
     11 18 500 5 4.94975
     14 21 500 5 4.94975
     17 24 500 5 4.94975
     5 0 500 5 4.94975
     8 3 500 5 4.94975
     14 9 500 5 4.94975
     17 12 500 5 4.94975
     23 18 500 5 4.94975
     26 21 500 5 4.94975
     2 3 500 5 4.94975
     5 6 500 5 4.94975
     11 12 500 5 4.94975
     14 15 500 5 4.94975
     20 21 500 5 4.94975
     23 24 500 5 4.94975
    "  object1="@M1/mObject1"  object2="@M2/mObject2" />
    		<StiffSpringForceField template="Vec3" name="ExternalSprings2"  spring="2 0 500 5 3.5
     5 3 500 5 3.5
     8 6 500 5 3.5
     11 9 500 5 3.5
     14 12 500 5 3.5
     17 15 500 5 3.5
     20 18 500 5 3.5
     23 21 500 5 3.5
     26 24 500 5 3.5
     14 0 500 5 6.06218
     17 3 500 5 6.06218
     23 9 500 5 6.06218
     26 12 500 5 6.06218
     5 9 500 5 6.06218
     8 12 500 5 6.06218
     14 18 500 5 6.06218
     17 21 500 5 6.06218
     11 3 500 5 6.06218
     14 6 500 5 6.06218
     20 12 500 5 6.06218
     23 15 500 5 6.06218
     2 12 500 5 6.06218
     5 15 500 5 6.06218
     11 21 500 5 6.06218
     14 24 500 5 6.06218
     11 0 500 5 4.94975
     14 3 500 5 4.94975
     17 6 500 5 4.94975
     20 9 500 5 4.94975
     23 12 500 5 4.94975
     26 15 500 5 4.94975
     2 9 500 5 4.94975
     5 12 500 5 4.94975
     8 15 500 5 4.94975
     11 18 500 5 4.94975
     14 21 500 5 4.94975
     17 24 500 5 4.94975
     5 0 500 5 4.94975
     8 3 500 5 4.94975
     14 9 500 5 4.94975
     17 12 500 5 4.94975
     23 18 500 5 4.94975
     26 21 500 5 4.94975
     2 3 500 5 4.94975
     5 6 500 5 4.94975
     11 12 500 5 4.94975
     14 15 500 5 4.94975
     20 21 500 5 4.94975
     23 24 500 5 4.94975
    "  object1="@M2/mObject2"  object2="@M3/mObject3" />
    		<StiffSpringForceField template="Vec3" name="ExternalSprings3"  spring="2 0 500 5 3.5
     5 3 500 5 3.5
     8 6 500 5 3.5
     11 9 500 5 3.5
     14 12 500 5 3.5
     17 15 500 5 3.5
     20 18 500 5 3.5
     23 21 500 5 3.5
     26 24 500 5 3.5
     14 0 500 5 6.06218
     17 3 500 5 6.06218
     23 9 500 5 6.06218
     26 12 500 5 6.06218
     5 9 500 5 6.06218
     8 12 500 5 6.06218
     14 18 500 5 6.06218
     17 21 500 5 6.06218
     11 3 500 5 6.06218
     14 6 500 5 6.06218
     20 12 500 5 6.06218
     23 15 500 5 6.06218
     2 12 500 5 6.06218
     5 15 500 5 6.06218
     11 21 500 5 6.06218
     14 24 500 5 6.06218
     11 0 500 5 4.94975
     14 3 500 5 4.94975
     17 6 500 5 4.94975
     20 9 500 5 4.94975
     23 12 500 5 4.94975
     26 15 500 5 4.94975
     2 9 500 5 4.94975
     5 12 500 5 4.94975
     8 15 500 5 4.94975
     11 18 500 5 4.94975
     14 21 500 5 4.94975
     17 24 500 5 4.94975
     5 0 500 5 4.94975
     8 3 500 5 4.94975
     14 9 500 5 4.94975
     17 12 500 5 4.94975
     23 18 500 5 4.94975
     26 21 500 5 4.94975
     2 3 500 5 4.94975
     5 6 500 5 4.94975
     11 12 500 5 4.94975
     14 15 500 5 4.94975
     20 21 500 5 4.94975
     23 24 500 5 4.94975
    "  object1="@M3/mObject3"  object2="@M4/mObject4" />
    		<StiffSpringForceField template="Vec3" name="ExternalSprings4"  spring="2 0 500 5 3.5
     5 3 500 5 3.5
     8 6 500 5 3.5
     11 9 500 5 3.5
     14 12 500 5 3.5
     17 15 500 5 3.5
     20 18 500 5 3.5
     23 21 500 5 3.5
     26 24 500 5 3.5
     14 0 500 5 6.06218
     17 3 500 5 6.06218
     23 9 500 5 6.06218
     26 12 500 5 6.06218
     5 9 500 5 6.06218
     8 12 500 5 6.06218
     14 18 500 5 6.06218
     17 21 500 5 6.06218
     11 3 500 5 6.06218
     14 6 500 5 6.06218
     20 12 500 5 6.06218
     23 15 500 5 6.06218
     2 12 500 5 6.06218
     5 15 500 5 6.06218
     11 21 500 5 6.06218
     14 24 500 5 6.06218
     11 0 500 5 4.94975
     14 3 500 5 4.94975
     17 6 500 5 4.94975
     20 9 500 5 4.94975
     23 12 500 5 4.94975
     26 15 500 5 4.94975
     2 9 500 5 4.94975
     5 12 500 5 4.94975
     8 15 500 5 4.94975
     11 18 500 5 4.94975
     14 21 500 5 4.94975
     17 24 500 5 4.94975
     5 0 500 5 4.94975
     8 3 500 5 4.94975
     14 9 500 5 4.94975
     17 12 500 5 4.94975
     23 18 500 5 4.94975
     26 21 500 5 4.94975
     2 3 500 5 4.94975
     5 6 500 5 4.94975
     11 12 500 5 4.94975
     14 15 500 5 4.94975
     20 21 500 5 4.94975
     23 24 500 5 4.94975
    "  object1="@M4/mObject4"  object2="@M5/mObject5" />
    	</Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.005")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', name="visualStyle1", displayFlags="showBehaviorModels showForceFields showCollisionModels showMappings")

        Poutre1 = root.addChild('Poutre1')
        Poutre1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="0", rayleighStiffness="0.1", rayleighMass="0.1")
        Poutre1.addObject('CGLinearSolver', template="GraphScattered", name="linear solver", iterations="25", tolerance="1e-09", threshold="1e-09")

        M1 = Poutre1.addChild('M1')
        M1.addObject('MeshGmshLoader', name="loader", filename="mesh/smCube27.msh")
        M1.addObject('MechanicalObject', template="Vec3", showObject="1", name="mObject1", position="@loader.position", velocity="0 0 0", force="0 0 0", externalForce="0 0 0", derivX="0 0 0", restScale="1")
        M1.addObject('UniformMass', name="uniformMass1", vertexMass="0.1")
        M1.addObject('FixedProjectiveConstraint', template="Vec3", name="fixedProjectiveConstraint1", indices="0 3 6 9 12 15 18 21 24")
        M1.addObject('StiffSpringForceField', template="Vec3", name="InternalSprings1", spring="0 9 100 5 3.5
 1 10 500 5 3.5
 2 11 500 5 3.5
 3 12 500 5 3.5
 4 13 500 5 3.5
 5 14 500 5 3.5
 6 15 500 5 3.5
 7 16 500 5 3.5
 8 17 500 5 3.5
 9 18 500 5 3.5
 10 19 500 5 3.5
 11 20 500 5 3.5
 12 21 500 5 3.5
 13 22 500 5 3.5
 14 23 500 5 3.5
 15 24 500 5 3.5
 16 25 500 5 3.5
 17 26 500 5 3.5
 0 3 500 5 3.5
 1 4 500 5 3.5
 2 5 500 5 3.5
 3 6 500 5 3.5
 4 7 500 5 3.5
 5 8 500 5 3.5
 9 12 500 5 3.5
 10 13 500 5 3.5
 11 14 500 5 3.5
 12 15 500 5 3.5
 13 16 500 5 3.5
 14 17 500 5 3.5
 18 21 500 5 3.5
 19 22 500 5 3.5
 20 23 500 5 3.5
 21 24 500 5 3.5
 22 25 500 5 3.5
 23 26 500 5 3.5
 0 1 500 5 3.5
 1 2 500 5 3.5
 3 4 500 5 3.5
 4 5 500 5 3.5
 6 7 500 5 3.5
 7 8 500 5 3.5
 9 10 500 5 3.5
 10 11 500 5 3.5
 12 13 500 5 3.5
 13 14 500 5 3.5
 15 16 500 5 3.5
 16 17 500 5 3.5
 18 19 500 5 3.5
 19 20 500 5 3.5
 21 22 500 5 3.5
 22 23 500 5 3.5
 24 25 500 5 3.5
 25 26 100 5 3.5
 0 13 500 5 6.06218
 1 14 500 5 6.06218
 3 16 500 5 6.06218
 4 17 500 5 6.06218
 9 22 500 5 6.06218
 10 23 500 5 6.06218
 12 25 500 5 6.06218
 13 26 500 5 6.06218
 9 4 500 5 6.06218
 10 5 500 5 6.06218
 12 7 500 5 6.06218
 13 8 500 5 6.06218
 18 13 500 5 6.06218
 19 14 500 5 6.06218
 21 16 500 5 6.06218
 22 17 500 5 6.06218
 3 10 500 5 6.06218
 4 11 500 5 6.06218
 6 13 500 5 6.06218
 7 14 500 5 6.06218
 12 19 500 5 6.06218
 13 20 500 5 6.06218
 15 22 500 5 6.06218
 16 23 500 5 6.06218
 12 1 500 5 6.06218
 13 2 500 5 6.06218
 15 4 500 5 6.06218
 16 5 500 5 6.06218
 21 10 500 5 6.06218
 22 11 500 5 6.06218
 24 13 500 5 6.06218
 25 14 500 5 6.06218
 0 12 500 5 4.94975
 1 13 500 5 4.94975
 2 14 500 5 4.94975
 3 15 500 5 4.94975
 4 16 500 5 4.94975
 5 17 500 5 4.94975
 9 21 500 5 4.94975
 10 22 500 5 4.94975
 11 23 500 5 4.94975
 12 24 500 5 4.94975
 13 25 500 5 4.94975
 14 26 500 5 4.94975
 3 9 500 5 4.94975
 4 10 500 5 4.94975
 5 11 500 5 4.94975
 6 12 500 5 4.94975
 7 13 500 5 4.94975
 8 14 500 5 4.94975
 12 18 500 5 4.94975
 13 19 500 5 4.94975
 14 20 500 5 4.94975
 15 21 500 5 4.94975
 16 22 500 5 4.94975
 17 23 500 5 4.94975
 0 10 500 5 4.94975
 1 11 500 5 4.94975
 3 13 500 5 4.94975
 4 14 500 5 4.94975
 6 16 500 5 4.94975
 7 17 500 5 4.94975
 9 19 500 5 4.94975
 10 20 500 5 4.94975
 12 22 500 5 4.94975
 13 23 500 5 4.94975
 15 25 500 5 4.94975
 16 26 500 5 4.94975
 9 1 500 5 4.94975
 10 2 500 5 4.94975
 12 4 500 5 4.94975
 13 5 500 5 4.94975
 15 7 500 5 4.94975
 16 8 500 5 4.94975
 18 10 500 5 4.94975
 19 11 500 5 4.94975
 21 13 500 5 4.94975
 22 14 500 5 4.94975
 24 16 500 5 4.94975
 25 17 500 5 4.94975
 0 4 500 5 4.94975
 1 5 500 5 4.94975
 3 7 500 5 4.94975
 4 8 500 5 4.94975
 9 13 500 5 4.94975
 10 14 500 5 4.94975
 12 16 500 5 4.94975
 13 17 500 5 4.94975
 18 22 500 5 4.94975
 19 23 500 5 4.94975
 21 25 500 5 4.94975
 22 26 500 5 4.94975
 3 1 500 5 4.94975
 4 2 500 5 4.94975
 6 4 500 5 4.94975
 7 5 500 5 4.94975
 12 10 500 5 4.94975
 13 11 500 5 4.94975
 15 13 500 5 4.94975
 16 14 500 5 4.94975
 21 19 500 5 4.94975
 22 20 500 5 4.94975
 24 22 500 5 4.94975
 25 23 500 5 4.94975
")

        M5 = Poutre1.addChild('M5')
        M5.addObject('MeshGmshLoader', name="loader", filename="mesh/smCube27.msh")
        M5.addObject('MechanicalObject', template="Vec3", name="mObject5", showObject="1", position="@loader.position", velocity="0 0 0", force="0 0 0", externalForce="0 0 0", derivX="0 0 0", restScale="1", translation="0 0 42")
        M5.addObject('UniformMass', name="uniformMass5", vertexMass="0.1")
        M5.addObject('StiffSpringForceField', template="Vec3", name="InternalSprings5", spring="0 9 100 5 3.5
 1 10 500 5 3.5
 2 11 500 5 3.5
 3 12 500 5 3.5
 4 13 500 5 3.5
 5 14 500 5 3.5
 6 15 500 5 3.5
 7 16 500 5 3.5
 8 17 500 5 3.5
 9 18 500 5 3.5
 10 19 500 5 3.5
 11 20 500 5 3.5
 12 21 500 5 3.5
 13 22 500 5 3.5
 14 23 500 5 3.5
 15 24 500 5 3.5
 16 25 500 5 3.5
 17 26 500 5 3.5
 0 3 500 5 3.5
 1 4 500 5 3.5
 2 5 500 5 3.5
 3 6 500 5 3.5
 4 7 500 5 3.5
 5 8 500 5 3.5
 9 12 500 5 3.5
 10 13 500 5 3.5
 11 14 500 5 3.5
 12 15 500 5 3.5
 13 16 500 5 3.5
 14 17 500 5 3.5
 18 21 500 5 3.5
 19 22 500 5 3.5
 20 23 500 5 3.5
 21 24 500 5 3.5
 22 25 500 5 3.5
 23 26 500 5 3.5
 0 1 500 5 3.5
 1 2 500 5 3.5
 3 4 500 5 3.5
 4 5 500 5 3.5
 6 7 500 5 3.5
 7 8 500 5 3.5
 9 10 500 5 3.5
 10 11 500 5 3.5
 12 13 500 5 3.5
 13 14 500 5 3.5
 15 16 500 5 3.5
 16 17 500 5 3.5
 18 19 500 5 3.5
 19 20 500 5 3.5
 21 22 500 5 3.5
 22 23 500 5 3.5
 24 25 500 5 3.5
 25 26 100 5 3.5
 0 13 500 5 6.06218
 1 14 500 5 6.06218
 3 16 500 5 6.06218
 4 17 500 5 6.06218
 9 22 500 5 6.06218
 10 23 500 5 6.06218
 12 25 500 5 6.06218
 13 26 500 5 6.06218
 9 4 500 5 6.06218
 10 5 500 5 6.06218
 12 7 500 5 6.06218
 13 8 500 5 6.06218
 18 13 500 5 6.06218
 19 14 500 5 6.06218
 21 16 500 5 6.06218
 22 17 500 5 6.06218
 3 10 500 5 6.06218
 4 11 500 5 6.06218
 6 13 500 5 6.06218
 7 14 500 5 6.06218
 12 19 500 5 6.06218
 13 20 500 5 6.06218
 15 22 500 5 6.06218
 16 23 500 5 6.06218
 12 1 500 5 6.06218
 13 2 500 5 6.06218
 15 4 500 5 6.06218
 16 5 500 5 6.06218
 21 10 500 5 6.06218
 22 11 500 5 6.06218
 24 13 500 5 6.06218
 25 14 500 5 6.06218
 0 12 500 5 4.94975
 1 13 500 5 4.94975
 2 14 500 5 4.94975
 3 15 500 5 4.94975
 4 16 500 5 4.94975
 5 17 500 5 4.94975
 9 21 500 5 4.94975
 10 22 500 5 4.94975
 11 23 500 5 4.94975
 12 24 500 5 4.94975
 13 25 500 5 4.94975
 14 26 500 5 4.94975
 3 9 500 5 4.94975
 4 10 500 5 4.94975
 5 11 500 5 4.94975
 6 12 500 5 4.94975
 7 13 500 5 4.94975
 8 14 500 5 4.94975
 12 18 500 5 4.94975
 13 19 500 5 4.94975
 14 20 500 5 4.94975
 15 21 500 5 4.94975
 16 22 500 5 4.94975
 17 23 500 5 4.94975
 0 10 500 5 4.94975
 1 11 500 5 4.94975
 3 13 500 5 4.94975
 4 14 500 5 4.94975
 6 16 500 5 4.94975
 7 17 500 5 4.94975
 9 19 500 5 4.94975
 10 20 500 5 4.94975
 12 22 500 5 4.94975
 13 23 500 5 4.94975
 15 25 500 5 4.94975
 16 26 500 5 4.94975
 9 1 500 5 4.94975
 10 2 500 5 4.94975
 12 4 500 5 4.94975
 13 5 500 5 4.94975
 15 7 500 5 4.94975
 16 8 500 5 4.94975
 18 10 500 5 4.94975
 19 11 500 5 4.94975
 21 13 500 5 4.94975
 22 14 500 5 4.94975
 24 16 500 5 4.94975
 25 17 500 5 4.94975
 0 4 500 5 4.94975
 1 5 500 5 4.94975
 3 7 500 5 4.94975
 4 8 500 5 4.94975
 9 13 500 5 4.94975
 10 14 500 5 4.94975
 12 16 500 5 4.94975
 13 17 500 5 4.94975
 18 22 500 5 4.94975
 19 23 500 5 4.94975
 21 25 500 5 4.94975
 22 26 500 5 4.94975
 3 1 500 5 4.94975
 4 2 500 5 4.94975
 6 4 500 5 4.94975
 7 5 500 5 4.94975
 12 10 500 5 4.94975
 13 11 500 5 4.94975
 15 13 500 5 4.94975
 16 14 500 5 4.94975
 21 19 500 5 4.94975
 22 20 500 5 4.94975
 24 22 500 5 4.94975
 25 23 500 5 4.94975
")

        M4 = Poutre1.addChild('M4')
        M4.addObject('MeshGmshLoader', name="loader", filename="mesh/smCube27.msh")
        M4.addObject('MechanicalObject', template="Vec3", name="mObject4", showObject="1", position="@loader.position", velocity="0 0 0", force="0 0 0", externalForce="0 0 0", derivX="0 0 0", restScale="1", translation="0 0 31.5")
        M4.addObject('UniformMass', name="uniformMass4", vertexMass="0.1")
        M4.addObject('StiffSpringForceField', template="Vec3", name="InternalSprings4", spring="0 9 100 5 3.5
 1 10 500 5 3.5
 2 11 500 5 3.5
 3 12 500 5 3.5
 4 13 500 5 3.5
 5 14 500 5 3.5
 6 15 500 5 3.5
 7 16 500 5 3.5
 8 17 500 5 3.5
 9 18 500 5 3.5
 10 19 500 5 3.5
 11 20 500 5 3.5
 12 21 500 5 3.5
 13 22 500 5 3.5
 14 23 500 5 3.5
 15 24 500 5 3.5
 16 25 500 5 3.5
 17 26 500 5 3.5
 0 3 500 5 3.5
 1 4 500 5 3.5
 2 5 500 5 3.5
 3 6 500 5 3.5
 4 7 500 5 3.5
 5 8 500 5 3.5
 9 12 500 5 3.5
 10 13 500 5 3.5
 11 14 500 5 3.5
 12 15 500 5 3.5
 13 16 500 5 3.5
 14 17 500 5 3.5
 18 21 500 5 3.5
 19 22 500 5 3.5
 20 23 500 5 3.5
 21 24 500 5 3.5
 22 25 500 5 3.5
 23 26 500 5 3.5
 0 1 500 5 3.5
 1 2 500 5 3.5
 3 4 500 5 3.5
 4 5 500 5 3.5
 6 7 500 5 3.5
 7 8 500 5 3.5
 9 10 500 5 3.5
 10 11 500 5 3.5
 12 13 500 5 3.5
 13 14 500 5 3.5
 15 16 500 5 3.5
 16 17 500 5 3.5
 18 19 500 5 3.5
 19 20 500 5 3.5
 21 22 500 5 3.5
 22 23 500 5 3.5
 24 25 500 5 3.5
 25 26 100 5 3.5
 0 13 500 5 6.06218
 1 14 500 5 6.06218
 3 16 500 5 6.06218
 4 17 500 5 6.06218
 9 22 500 5 6.06218
 10 23 500 5 6.06218
 12 25 500 5 6.06218
 13 26 500 5 6.06218
 9 4 500 5 6.06218
 10 5 500 5 6.06218
 12 7 500 5 6.06218
 13 8 500 5 6.06218
 18 13 500 5 6.06218
 19 14 500 5 6.06218
 21 16 500 5 6.06218
 22 17 500 5 6.06218
 3 10 500 5 6.06218
 4 11 500 5 6.06218
 6 13 500 5 6.06218
 7 14 500 5 6.06218
 12 19 500 5 6.06218
 13 20 500 5 6.06218
 15 22 500 5 6.06218
 16 23 500 5 6.06218
 12 1 500 5 6.06218
 13 2 500 5 6.06218
 15 4 500 5 6.06218
 16 5 500 5 6.06218
 21 10 500 5 6.06218
 22 11 500 5 6.06218
 24 13 500 5 6.06218
 25 14 500 5 6.06218
 0 12 500 5 4.94975
 1 13 500 5 4.94975
 2 14 500 5 4.94975
 3 15 500 5 4.94975
 4 16 500 5 4.94975
 5 17 500 5 4.94975
 9 21 500 5 4.94975
 10 22 500 5 4.94975
 11 23 500 5 4.94975
 12 24 500 5 4.94975
 13 25 500 5 4.94975
 14 26 500 5 4.94975
 3 9 500 5 4.94975
 4 10 500 5 4.94975
 5 11 500 5 4.94975
 6 12 500 5 4.94975
 7 13 500 5 4.94975
 8 14 500 5 4.94975
 12 18 500 5 4.94975
 13 19 500 5 4.94975
 14 20 500 5 4.94975
 15 21 500 5 4.94975
 16 22 500 5 4.94975
 17 23 500 5 4.94975
 0 10 500 5 4.94975
 1 11 500 5 4.94975
 3 13 500 5 4.94975
 4 14 500 5 4.94975
 6 16 500 5 4.94975
 7 17 500 5 4.94975
 9 19 500 5 4.94975
 10 20 500 5 4.94975
 12 22 500 5 4.94975
 13 23 500 5 4.94975
 15 25 500 5 4.94975
 16 26 500 5 4.94975
 9 1 500 5 4.94975
 10 2 500 5 4.94975
 12 4 500 5 4.94975
 13 5 500 5 4.94975
 15 7 500 5 4.94975
 16 8 500 5 4.94975
 18 10 500 5 4.94975
 19 11 500 5 4.94975
 21 13 500 5 4.94975
 22 14 500 5 4.94975
 24 16 500 5 4.94975
 25 17 500 5 4.94975
 0 4 500 5 4.94975
 1 5 500 5 4.94975
 3 7 500 5 4.94975
 4 8 500 5 4.94975
 9 13 500 5 4.94975
 10 14 500 5 4.94975
 12 16 500 5 4.94975
 13 17 500 5 4.94975
 18 22 500 5 4.94975
 19 23 500 5 4.94975
 21 25 500 5 4.94975
 22 26 500 5 4.94975
 3 1 500 5 4.94975
 4 2 500 5 4.94975
 6 4 500 5 4.94975
 7 5 500 5 4.94975
 12 10 500 5 4.94975
 13 11 500 5 4.94975
 15 13 500 5 4.94975
 16 14 500 5 4.94975
 21 19 500 5 4.94975
 22 20 500 5 4.94975
 24 22 500 5 4.94975
 25 23 500 5 4.94975
")

        M3 = Poutre1.addChild('M3')
        M3.addObject('MeshGmshLoader', name="loader", filename="mesh/smCube27.msh")
        M3.addObject('MechanicalObject', template="Vec3", showObject="1", name="mObject3", position="@loader.position", velocity="0 0 0", force="0 0 0", externalForce="0 0 0", derivX="0 0 0", restScale="1", translation="0 0 21")
        M3.addObject('UniformMass', name="uniformMass3", vertexMass="0.1")
        M3.addObject('StiffSpringForceField', template="Vec3", name="InternalSprings3", spring="0 9 100 5 3.5
 1 10 500 5 3.5
 2 11 500 5 3.5
 3 12 500 5 3.5
 4 13 500 5 3.5
 5 14 500 5 3.5
 6 15 500 5 3.5
 7 16 500 5 3.5
 8 17 500 5 3.5
 9 18 500 5 3.5
 10 19 500 5 3.5
 11 20 500 5 3.5
 12 21 500 5 3.5
 13 22 500 5 3.5
 14 23 500 5 3.5
 15 24 500 5 3.5
 16 25 500 5 3.5
 17 26 500 5 3.5
 0 3 500 5 3.5
 1 4 500 5 3.5
 2 5 500 5 3.5
 3 6 500 5 3.5
 4 7 500 5 3.5
 5 8 500 5 3.5
 9 12 500 5 3.5
 10 13 500 5 3.5
 11 14 500 5 3.5
 12 15 500 5 3.5
 13 16 500 5 3.5
 14 17 500 5 3.5
 18 21 500 5 3.5
 19 22 500 5 3.5
 20 23 500 5 3.5
 21 24 500 5 3.5
 22 25 500 5 3.5
 23 26 500 5 3.5
 0 1 500 5 3.5
 1 2 500 5 3.5
 3 4 500 5 3.5
 4 5 500 5 3.5
 6 7 500 5 3.5
 7 8 500 5 3.5
 9 10 500 5 3.5
 10 11 500 5 3.5
 12 13 500 5 3.5
 13 14 500 5 3.5
 15 16 500 5 3.5
 16 17 500 5 3.5
 18 19 500 5 3.5
 19 20 500 5 3.5
 21 22 500 5 3.5
 22 23 500 5 3.5
 24 25 500 5 3.5
 25 26 100 5 3.5
 0 13 500 5 6.06218
 1 14 500 5 6.06218
 3 16 500 5 6.06218
 4 17 500 5 6.06218
 9 22 500 5 6.06218
 10 23 500 5 6.06218
 12 25 500 5 6.06218
 13 26 500 5 6.06218
 9 4 500 5 6.06218
 10 5 500 5 6.06218
 12 7 500 5 6.06218
 13 8 500 5 6.06218
 18 13 500 5 6.06218
 19 14 500 5 6.06218
 21 16 500 5 6.06218
 22 17 500 5 6.06218
 3 10 500 5 6.06218
 4 11 500 5 6.06218
 6 13 500 5 6.06218
 7 14 500 5 6.06218
 12 19 500 5 6.06218
 13 20 500 5 6.06218
 15 22 500 5 6.06218
 16 23 500 5 6.06218
 12 1 500 5 6.06218
 13 2 500 5 6.06218
 15 4 500 5 6.06218
 16 5 500 5 6.06218
 21 10 500 5 6.06218
 22 11 500 5 6.06218
 24 13 500 5 6.06218
 25 14 500 5 6.06218
 0 12 500 5 4.94975
 1 13 500 5 4.94975
 2 14 500 5 4.94975
 3 15 500 5 4.94975
 4 16 500 5 4.94975
 5 17 500 5 4.94975
 9 21 500 5 4.94975
 10 22 500 5 4.94975
 11 23 500 5 4.94975
 12 24 500 5 4.94975
 13 25 500 5 4.94975
 14 26 500 5 4.94975
 3 9 500 5 4.94975
 4 10 500 5 4.94975
 5 11 500 5 4.94975
 6 12 500 5 4.94975
 7 13 500 5 4.94975
 8 14 500 5 4.94975
 12 18 500 5 4.94975
 13 19 500 5 4.94975
 14 20 500 5 4.94975
 15 21 500 5 4.94975
 16 22 500 5 4.94975
 17 23 500 5 4.94975
 0 10 500 5 4.94975
 1 11 500 5 4.94975
 3 13 500 5 4.94975
 4 14 500 5 4.94975
 6 16 500 5 4.94975
 7 17 500 5 4.94975
 9 19 500 5 4.94975
 10 20 500 5 4.94975
 12 22 500 5 4.94975
 13 23 500 5 4.94975
 15 25 500 5 4.94975
 16 26 500 5 4.94975
 9 1 500 5 4.94975
 10 2 500 5 4.94975
 12 4 500 5 4.94975
 13 5 500 5 4.94975
 15 7 500 5 4.94975
 16 8 500 5 4.94975
 18 10 500 5 4.94975
 19 11 500 5 4.94975
 21 13 500 5 4.94975
 22 14 500 5 4.94975
 24 16 500 5 4.94975
 25 17 500 5 4.94975
 0 4 500 5 4.94975
 1 5 500 5 4.94975
 3 7 500 5 4.94975
 4 8 500 5 4.94975
 9 13 500 5 4.94975
 10 14 500 5 4.94975
 12 16 500 5 4.94975
 13 17 500 5 4.94975
 18 22 500 5 4.94975
 19 23 500 5 4.94975
 21 25 500 5 4.94975
 22 26 500 5 4.94975
 3 1 500 5 4.94975
 4 2 500 5 4.94975
 6 4 500 5 4.94975
 7 5 500 5 4.94975
 12 10 500 5 4.94975
 13 11 500 5 4.94975
 15 13 500 5 4.94975
 16 14 500 5 4.94975
 21 19 500 5 4.94975
 22 20 500 5 4.94975
 24 22 500 5 4.94975
 25 23 500 5 4.94975
")

        M2 = Poutre1.addChild('M2')
        M2.addObject('MeshGmshLoader', name="loader", filename="mesh/smCube27.msh")
        M2.addObject('MechanicalObject', template="Vec3", showObject="1", name="mObject2", position="@loader.position", velocity="0 0 0", force="0 0 0", externalForce="0 0 0", derivX="0 0 0", restScale="1", translation="0 0 10.5")
        M2.addObject('UniformMass', name="uniformMass2", vertexMass="0.1")
        M2.addObject('StiffSpringForceField', template="Vec3", name="InternalSprings2", spring="0 9 100 5 3.5
 1 10 500 5 3.5
 2 11 500 5 3.5
 3 12 500 5 3.5
 4 13 500 5 3.5
 5 14 500 5 3.5
 6 15 500 5 3.5
 7 16 500 5 3.5
 8 17 500 5 3.5
 9 18 500 5 3.5
 10 19 500 5 3.5
 11 20 500 5 3.5
 12 21 500 5 3.5
 13 22 500 5 3.5
 14 23 500 5 3.5
 15 24 500 5 3.5
 16 25 500 5 3.5
 17 26 500 5 3.5
 0 3 500 5 3.5
 1 4 500 5 3.5
 2 5 500 5 3.5
 3 6 500 5 3.5
 4 7 500 5 3.5
 5 8 500 5 3.5
 9 12 500 5 3.5
 10 13 500 5 3.5
 11 14 500 5 3.5
 12 15 500 5 3.5
 13 16 500 5 3.5
 14 17 500 5 3.5
 18 21 500 5 3.5
 19 22 500 5 3.5
 20 23 500 5 3.5
 21 24 500 5 3.5
 22 25 500 5 3.5
 23 26 500 5 3.5
 0 1 500 5 3.5
 1 2 500 5 3.5
 3 4 500 5 3.5
 4 5 500 5 3.5
 6 7 500 5 3.5
 7 8 500 5 3.5
 9 10 500 5 3.5
 10 11 500 5 3.5
 12 13 500 5 3.5
 13 14 500 5 3.5
 15 16 500 5 3.5
 16 17 500 5 3.5
 18 19 500 5 3.5
 19 20 500 5 3.5
 21 22 500 5 3.5
 22 23 500 5 3.5
 24 25 500 5 3.5
 25 26 100 5 3.5
 0 13 500 5 6.06218
 1 14 500 5 6.06218
 3 16 500 5 6.06218
 4 17 500 5 6.06218
 9 22 500 5 6.06218
 10 23 500 5 6.06218
 12 25 500 5 6.06218
 13 26 500 5 6.06218
 9 4 500 5 6.06218
 10 5 500 5 6.06218
 12 7 500 5 6.06218
 13 8 500 5 6.06218
 18 13 500 5 6.06218
 19 14 500 5 6.06218
 21 16 500 5 6.06218
 22 17 500 5 6.06218
 3 10 500 5 6.06218
 4 11 500 5 6.06218
 6 13 500 5 6.06218
 7 14 500 5 6.06218
 12 19 500 5 6.06218
 13 20 500 5 6.06218
 15 22 500 5 6.06218
 16 23 500 5 6.06218
 12 1 500 5 6.06218
 13 2 500 5 6.06218
 15 4 500 5 6.06218
 16 5 500 5 6.06218
 21 10 500 5 6.06218
 22 11 500 5 6.06218
 24 13 500 5 6.06218
 25 14 500 5 6.06218
 0 12 500 5 4.94975
 1 13 500 5 4.94975
 2 14 500 5 4.94975
 3 15 500 5 4.94975
 4 16 500 5 4.94975
 5 17 500 5 4.94975
 9 21 500 5 4.94975
 10 22 500 5 4.94975
 11 23 500 5 4.94975
 12 24 500 5 4.94975
 13 25 500 5 4.94975
 14 26 500 5 4.94975
 3 9 500 5 4.94975
 4 10 500 5 4.94975
 5 11 500 5 4.94975
 6 12 500 5 4.94975
 7 13 500 5 4.94975
 8 14 500 5 4.94975
 12 18 500 5 4.94975
 13 19 500 5 4.94975
 14 20 500 5 4.94975
 15 21 500 5 4.94975
 16 22 500 5 4.94975
 17 23 500 5 4.94975
 0 10 500 5 4.94975
 1 11 500 5 4.94975
 3 13 500 5 4.94975
 4 14 500 5 4.94975
 6 16 500 5 4.94975
 7 17 500 5 4.94975
 9 19 500 5 4.94975
 10 20 500 5 4.94975
 12 22 500 5 4.94975
 13 23 500 5 4.94975
 15 25 500 5 4.94975
 16 26 500 5 4.94975
 9 1 500 5 4.94975
 10 2 500 5 4.94975
 12 4 500 5 4.94975
 13 5 500 5 4.94975
 15 7 500 5 4.94975
 16 8 500 5 4.94975
 18 10 500 5 4.94975
 19 11 500 5 4.94975
 21 13 500 5 4.94975
 22 14 500 5 4.94975
 24 16 500 5 4.94975
 25 17 500 5 4.94975
 0 4 500 5 4.94975
 1 5 500 5 4.94975
 3 7 500 5 4.94975
 4 8 500 5 4.94975
 9 13 500 5 4.94975
 10 14 500 5 4.94975
 12 16 500 5 4.94975
 13 17 500 5 4.94975
 18 22 500 5 4.94975
 19 23 500 5 4.94975
 21 25 500 5 4.94975
 22 26 500 5 4.94975
 3 1 500 5 4.94975
 4 2 500 5 4.94975
 6 4 500 5 4.94975
 7 5 500 5 4.94975
 12 10 500 5 4.94975
 13 11 500 5 4.94975
 15 13 500 5 4.94975
 16 14 500 5 4.94975
 21 19 500 5 4.94975
 22 20 500 5 4.94975
 24 22 500 5 4.94975
 25 23 500 5 4.94975
")
        Poutre1.addObject('StiffSpringForceField', template="Vec3", name="ExternalSprings1", spring="2 0 500 5 3.5
 5 3 500 5 3.5
 8 6 500 5 3.5
 11 9 500 5 3.5
 14 12 500 5 3.5
 17 15 500 5 3.5
 20 18 500 5 3.5
 23 21 500 5 3.5
 26 24 500 5 3.5
 14 0 500 5 6.06218
 17 3 500 5 6.06218
 23 9 500 5 6.06218
 26 12 500 5 6.06218
 5 9 500 5 6.06218
 8 12 500 5 6.06218
 14 18 500 5 6.06218
 17 21 500 5 6.06218
 11 3 500 5 6.06218
 14 6 500 5 6.06218
 20 12 500 5 6.06218
 23 15 500 5 6.06218
 2 12 500 5 6.06218
 5 15 500 5 6.06218
 11 21 500 5 6.06218
 14 24 500 5 6.06218
 11 0 500 5 4.94975
 14 3 500 5 4.94975
 17 6 500 5 4.94975
 20 9 500 5 4.94975
 23 12 500 5 4.94975
 26 15 500 5 4.94975
 2 9 500 5 4.94975
 5 12 500 5 4.94975
 8 15 500 5 4.94975
 11 18 500 5 4.94975
 14 21 500 5 4.94975
 17 24 500 5 4.94975
 5 0 500 5 4.94975
 8 3 500 5 4.94975
 14 9 500 5 4.94975
 17 12 500 5 4.94975
 23 18 500 5 4.94975
 26 21 500 5 4.94975
 2 3 500 5 4.94975
 5 6 500 5 4.94975
 11 12 500 5 4.94975
 14 15 500 5 4.94975
 20 21 500 5 4.94975
 23 24 500 5 4.94975
", object1="@M1/mObject1", object2="@M2/mObject2")
        Poutre1.addObject('StiffSpringForceField', template="Vec3", name="ExternalSprings2", spring="2 0 500 5 3.5
 5 3 500 5 3.5
 8 6 500 5 3.5
 11 9 500 5 3.5
 14 12 500 5 3.5
 17 15 500 5 3.5
 20 18 500 5 3.5
 23 21 500 5 3.5
 26 24 500 5 3.5
 14 0 500 5 6.06218
 17 3 500 5 6.06218
 23 9 500 5 6.06218
 26 12 500 5 6.06218
 5 9 500 5 6.06218
 8 12 500 5 6.06218
 14 18 500 5 6.06218
 17 21 500 5 6.06218
 11 3 500 5 6.06218
 14 6 500 5 6.06218
 20 12 500 5 6.06218
 23 15 500 5 6.06218
 2 12 500 5 6.06218
 5 15 500 5 6.06218
 11 21 500 5 6.06218
 14 24 500 5 6.06218
 11 0 500 5 4.94975
 14 3 500 5 4.94975
 17 6 500 5 4.94975
 20 9 500 5 4.94975
 23 12 500 5 4.94975
 26 15 500 5 4.94975
 2 9 500 5 4.94975
 5 12 500 5 4.94975
 8 15 500 5 4.94975
 11 18 500 5 4.94975
 14 21 500 5 4.94975
 17 24 500 5 4.94975
 5 0 500 5 4.94975
 8 3 500 5 4.94975
 14 9 500 5 4.94975
 17 12 500 5 4.94975
 23 18 500 5 4.94975
 26 21 500 5 4.94975
 2 3 500 5 4.94975
 5 6 500 5 4.94975
 11 12 500 5 4.94975
 14 15 500 5 4.94975
 20 21 500 5 4.94975
 23 24 500 5 4.94975
", object1="@M2/mObject2", object2="@M3/mObject3")
        Poutre1.addObject('StiffSpringForceField', template="Vec3", name="ExternalSprings3", spring="2 0 500 5 3.5
 5 3 500 5 3.5
 8 6 500 5 3.5
 11 9 500 5 3.5
 14 12 500 5 3.5
 17 15 500 5 3.5
 20 18 500 5 3.5
 23 21 500 5 3.5
 26 24 500 5 3.5
 14 0 500 5 6.06218
 17 3 500 5 6.06218
 23 9 500 5 6.06218
 26 12 500 5 6.06218
 5 9 500 5 6.06218
 8 12 500 5 6.06218
 14 18 500 5 6.06218
 17 21 500 5 6.06218
 11 3 500 5 6.06218
 14 6 500 5 6.06218
 20 12 500 5 6.06218
 23 15 500 5 6.06218
 2 12 500 5 6.06218
 5 15 500 5 6.06218
 11 21 500 5 6.06218
 14 24 500 5 6.06218
 11 0 500 5 4.94975
 14 3 500 5 4.94975
 17 6 500 5 4.94975
 20 9 500 5 4.94975
 23 12 500 5 4.94975
 26 15 500 5 4.94975
 2 9 500 5 4.94975
 5 12 500 5 4.94975
 8 15 500 5 4.94975
 11 18 500 5 4.94975
 14 21 500 5 4.94975
 17 24 500 5 4.94975
 5 0 500 5 4.94975
 8 3 500 5 4.94975
 14 9 500 5 4.94975
 17 12 500 5 4.94975
 23 18 500 5 4.94975
 26 21 500 5 4.94975
 2 3 500 5 4.94975
 5 6 500 5 4.94975
 11 12 500 5 4.94975
 14 15 500 5 4.94975
 20 21 500 5 4.94975
 23 24 500 5 4.94975
", object1="@M3/mObject3", object2="@M4/mObject4")
        Poutre1.addObject('StiffSpringForceField', template="Vec3", name="ExternalSprings4", spring="2 0 500 5 3.5
 5 3 500 5 3.5
 8 6 500 5 3.5
 11 9 500 5 3.5
 14 12 500 5 3.5
 17 15 500 5 3.5
 20 18 500 5 3.5
 23 21 500 5 3.5
 26 24 500 5 3.5
 14 0 500 5 6.06218
 17 3 500 5 6.06218
 23 9 500 5 6.06218
 26 12 500 5 6.06218
 5 9 500 5 6.06218
 8 12 500 5 6.06218
 14 18 500 5 6.06218
 17 21 500 5 6.06218
 11 3 500 5 6.06218
 14 6 500 5 6.06218
 20 12 500 5 6.06218
 23 15 500 5 6.06218
 2 12 500 5 6.06218
 5 15 500 5 6.06218
 11 21 500 5 6.06218
 14 24 500 5 6.06218
 11 0 500 5 4.94975
 14 3 500 5 4.94975
 17 6 500 5 4.94975
 20 9 500 5 4.94975
 23 12 500 5 4.94975
 26 15 500 5 4.94975
 2 9 500 5 4.94975
 5 12 500 5 4.94975
 8 15 500 5 4.94975
 11 18 500 5 4.94975
 14 21 500 5 4.94975
 17 24 500 5 4.94975
 5 0 500 5 4.94975
 8 3 500 5 4.94975
 14 9 500 5 4.94975
 17 12 500 5 4.94975
 23 18 500 5 4.94975
 26 21 500 5 4.94975
 2 3 500 5 4.94975
 5 6 500 5 4.94975
 11 12 500 5 4.94975
 14 15 500 5 4.94975
 20 21 500 5 4.94975
 23 24 500 5 4.94975
", object1="@M4/mObject4", object2="@M5/mObject5")
    ```

