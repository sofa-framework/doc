# ParallelMeshSpringForceField

Parallel stiff springs acting along the edges of a mesh


__Templates__:

- `#!c++ Vec1d`
- `#!c++ Vec2d`
- `#!c++ Vec3d`

__Target__: `MultiThreading`

__namespace__: `#!c++ multithreading::component::solidmechanics::spring`

__parents__: 

- `#!c++ MeshSpringForceField`
- `#!c++ ParallelStiffSpringForceField`

__categories__: 

- ForceField
- InteractionForceField

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
		<td>linesStiffness</td>
		<td>
Stiffness for the Lines
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>linesDamping</td>
		<td>
Damping for the Lines
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>trianglesStiffness</td>
		<td>
Stiffness for the Triangles
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>trianglesDamping</td>
		<td>
Damping for the Triangles
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>quadsStiffness</td>
		<td>
Stiffness for the Quads
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>quadsDamping</td>
		<td>
Damping for the Quads
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tetrahedraStiffness</td>
		<td>
Stiffness for the Tetrahedra
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tetrahedraDamping</td>
		<td>
Damping for the Tetrahedra
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>cubesStiffness</td>
		<td>
Stiffness for the Cubes
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>cubesDamping</td>
		<td>
Damping for the Cubes
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>noCompression</td>
		<td>
Only consider elongation
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>localRange</td>
		<td>
optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)
</td>
		<td>4294967295 4294967295</td>
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
	<tr>
		<td>drawMinElongationRange</td>
		<td>
Min range of elongation (red eongation - blue neutral - green compression)
</td>
		<td>8</td>
	</tr>
	<tr>
		<td>drawMaxElongationRange</td>
		<td>
Max range of elongation (red eongation - blue neutral - green compression)
</td>
		<td>15</td>
	</tr>
	<tr>
		<td>drawSpringSize</td>
		<td>
Size of drawed lines
</td>
		<td>8</td>
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
|topology|link to the topology container|



## Examples

MultiThreading/share/sofa/examples/MultiThreading/ParallelMeshSpringForceField.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 -9.81 0" dt="0.04">
    
        <Node name="plugins">
            <RequiredPlugin name="MultiThreading"/> <!-- Needed to use components [ParallelMeshSpringForceField] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetGeometryAlgorithms, QuadSetTopologyContainer, QuadSetTopologyModifier] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2QuadTopologicalMapping] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        </Node>
    
    
        <VisualStyle displayFlags="showBehaviorModels hideForceFields" />
        <DefaultAnimationLoop computeBoundingBox="false"/>
    
        <Node name="DeformableObject">
    
            <EulerImplicitSolver name="odeSolver"/>
            <CGLinearSolver iterations="25" name="linearSolver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <MechanicalObject name="dofs"/>
    
            <RegularGridTopology name="topology" nx="16" ny="16" nz="44" xmin="-1.5" xmax="1.5" ymin="-1.5" ymax="1.5" zmin="0" zmax="10" />
            <HexahedronSetGeometryAlgorithms/>
            <UniformMass totalMass="150"/>
    
            <BoxROI box="-1.5 -1.5 0 1.5 1.5 0.0001" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices" />
            <ParallelMeshSpringForceField stiffness="3E2" drawSpringSize="1"/>
    
            <Node name="visual">
                <QuadSetTopologyContainer  name="Container" />
                <QuadSetTopologyModifier/>
                <Hexa2QuadTopologicalMapping input="@../topology" output="@Container" />
                <OglModel name="Visual" color="yellow" quads="@Container.quads" />
                <IdentityMapping input="@../dofs" output="@Visual" />
            </Node>
    
        </Node>
    
        <Node name="floor-visual">
            <MeshOBJLoader name="meshLoader" filename="mesh/floorFlat.obj" scale3d="0.5 0.5 0.5"/>
            <OglModel src="@meshLoader" dy="-8" dz="10"/>
            <OglModel src="@meshLoader" rx="90" dy="2"/>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9.81 0", dt="0.04")

        plugins = root.addChild('plugins')
        plugins.addObject('RequiredPlugin', name="MultiThreading")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels hideForceFields")
        root.addObject('DefaultAnimationLoop', computeBoundingBox="false")

        DeformableObject = root.addChild('DeformableObject')
        DeformableObject.addObject('EulerImplicitSolver', name="odeSolver")
        DeformableObject.addObject('CGLinearSolver', iterations="25", name="linearSolver", tolerance="1.0e-9", threshold="1.0e-9")
        DeformableObject.addObject('MechanicalObject', name="dofs")
        DeformableObject.addObject('RegularGridTopology', name="topology", nx="16", ny="16", nz="44", xmin="-1.5", xmax="1.5", ymin="-1.5", ymax="1.5", zmin="0", zmax="10")
        DeformableObject.addObject('HexahedronSetGeometryAlgorithms')
        DeformableObject.addObject('UniformMass', totalMass="150")
        DeformableObject.addObject('BoxROI', box="-1.5 -1.5 0 1.5 1.5 0.0001", name="box")
        DeformableObject.addObject('FixedProjectiveConstraint', indices="@box.indices")
        DeformableObject.addObject('ParallelMeshSpringForceField', stiffness="3E2", drawSpringSize="1")

        visual = DeformableObject.addChild('visual')
        visual.addObject('QuadSetTopologyContainer', name="Container")
        visual.addObject('QuadSetTopologyModifier')
        visual.addObject('Hexa2QuadTopologicalMapping', input="@../topology", output="@Container")
        visual.addObject('OglModel', name="Visual", color="yellow", quads="@Container.quads")
        visual.addObject('IdentityMapping', input="@../dofs", output="@Visual")

        floor-visual = root.addChild('floor-visual')
        floor-visual.addObject('MeshOBJLoader', name="meshLoader", filename="mesh/floorFlat.obj", scale3d="0.5 0.5 0.5")
        floor-visual.addObject('OglModel', src="@meshLoader", dy="-8", dz="10")
        floor-visual.addObject('OglModel', src="@meshLoader", rx="90", dy="2")
    ```

