# SphereForceField

Repulsion applied by a sphere toward the exterior
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Vec1d`
- `#!c++ Vec2d`
- `#!c++ Vec3d`

__Target__: `Sofa.Component.MechanicalLoad`

__namespace__: `#!c++ sofa::component::mechanicalload`

__parents__: 

- `#!c++ ForceField`

__categories__: 

- ForceField

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
		<td>rayleighStiffness</td>
		<td>
Rayleigh damping - stiffness matrix coefficient
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>contacts</td>
		<td>
Contacts
</td>
		<td></td>
	</tr>
	<tr>
		<td>center</td>
		<td>
sphere center
</td>
		<td></td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
sphere radius
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>stiffness</td>
		<td>
force stiffness
</td>
		<td>500</td>
	</tr>
	<tr>
		<td>damping</td>
		<td>
force damping
</td>
		<td>5</td>
	</tr>
	<tr>
		<td>color</td>
		<td>
sphere color. (default=[0,0,1,1])
</td>
		<td>0 0 1 1</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)
</td>
		<td>-1 -1</td>
	</tr>
	<tr>
		<td>bilateral</td>
		<td>
if true the sphere force field is applied on both sides
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
|mstate|MechanicalState used by this component|



## Examples

Component/MechanicalLoad/SphereForceField.scn

=== "XML"

    ```xml
    <!-- Mechanical SphereForceField Example -->
    <Node name="root" gravity="0.0 -2.0 0.0" dt="0.04">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField SphereForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField QuadBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="hideBehaviorModels showForceFields hideCollisionModels hideVisualModels" />
    
        <Node name="Floor">
            <RegularGridTopology nx="2" ny="1" nz="2" xmin="20" xmax="-20" ymin="-3.05" ymax="-3.05" zmin="-20" zmax="20" />
            <MechanicalObject />
    
            <Node name="Visu">
                <OglModel name="Visual" color="red" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        
        <Node name="SquareCloth1">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <RegularGridTopology nx="20" ny="1" nz="20" xmin="12" xmax="-12" ymin="7" ymax="7" zmin="-12" zmax="12" />
            <MechanicalObject />
            <UniformMass totalMass="100" />
            <BoxConstraint box="-12 7 12 -10 7 12    10 7 12 12 7 12" />
            <MeshSpringForceField name="Springs" stiffness="1000" damping="0" />
            <QuadBendingSprings name="Bend" stiffness="2000" damping="1" />
    
            <!-- Two ForceFields mimicking collision : a sphere and plane model -->
            <SphereForceField stiffness="1000" damping="1" center="0 1 3" radius="4"  />
            <PlaneForceField stiffness="1000" damping="20" normal="0 1 0" d="-3" />
            
            <Node name="Visu">
                <OglModel name="Visual" color="green" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        
        <Node name="Sphere">
            <MeshOBJLoader name="meshLoader_0" filename="mesh/sphere.obj" scale="3.95" handleSeams="1" />
            <OglModel name="Visual" src="@meshLoader_0" dx="0" dy="1" dz="3" color="blue" />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0.0 -2.0 0.0", dt="0.04")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="hideBehaviorModels showForceFields hideCollisionModels hideVisualModels")

        Floor = root.addChild('Floor')
        Floor.addObject('RegularGridTopology', nx="2", ny="1", nz="2", xmin="20", xmax="-20", ymin="-3.05", ymax="-3.05", zmin="-20", zmax="20")
        Floor.addObject('MechanicalObject')

        Visu = Floor.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="red")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")

        SquareCloth1 = root.addChild('SquareCloth1')
        SquareCloth1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        SquareCloth1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        SquareCloth1.addObject('RegularGridTopology', nx="20", ny="1", nz="20", xmin="12", xmax="-12", ymin="7", ymax="7", zmin="-12", zmax="12")
        SquareCloth1.addObject('MechanicalObject')
        SquareCloth1.addObject('UniformMass', totalMass="100")
        SquareCloth1.addObject('BoxConstraint', box="-12 7 12 -10 7 12    10 7 12 12 7 12")
        SquareCloth1.addObject('MeshSpringForceField', name="Springs", stiffness="1000", damping="0")
        SquareCloth1.addObject('QuadBendingSprings', name="Bend", stiffness="2000", damping="1")
        SquareCloth1.addObject('SphereForceField', stiffness="1000", damping="1", center="0 1 3", radius="4")
        SquareCloth1.addObject('PlaneForceField', stiffness="1000", damping="20", normal="0 1 0", d="-3")

        Visu = SquareCloth1.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="green")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")

        Sphere = root.addChild('Sphere')
        Sphere.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/sphere.obj", scale="3.95", handleSeams="1")
        Sphere.addObject('OglModel', name="Visual", src="@meshLoader_0", dx="0", dy="1", dz="3", color="blue")
    ```

