<!-- generate_doc -->
# VonMisesStress

Compute and draw von Mises stress based on a local least-square projection in each element


## Vec1d,Edge

Templates:

- Vec1d,Edge

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- TopologyAccessor
- SingleStateAccessor

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
		<td>nodalStress</td>
		<td>
Local nodal von Mises stress values
		</td>
		<td></td>
	</tr>
	<tr>
		<td>colorMap</td>
		<td>
Color map
		</td>
		<td>#ff0000ff #ff0500ff #ff0b00ff #ff1100ff #ff1700ff #ff1d00ff #ff2300ff #ff2900ff #ff2f00ff #ff3500ff #ff3b00ff #ff4100ff #ff4700ff #ff4e00ff #ff5400ff #ff5900ff #ff5f00ff #ff6600ff #ff6c00ff #ff7100ff #ff7700ff #ff7e00ff #ff8400ff #ff8a00ff #ff9000ff #ff9600ff #ff9c00ff #ffa200ff #ffa800ff #ffae00ff #ffb400ff #ffba00ff #ffc000ff #ffc600ff #ffcc00ff #ffd200ff #ffd800ff #ffde00ff #ffe400ff #ffea00ff #fff000ff #fff600ff #fffc00ff #fbff00ff #f5ff00ff #efff00ff #e9ff00ff #e3ff00ff #ddff00ff #d7ff00ff #d1ff00ff #cbff00ff #c5ff00ff #bfff00ff #b9ff00ff #b3ff00ff #adff00ff #a7ff00ff #a1ff00ff #9bff00ff #95ff00ff #8fff00ff #89ff00ff #83ff00ff #7dff00ff #77ff00ff #71ff00ff #6bff00ff #65ff00ff #5fff00ff #59ff00ff #53ff00ff #4dff00ff #47ff00ff #41ff00ff #3bff00ff #35ff00ff #2fff00ff #29ff00ff #23ff00ff #1dff00ff #17ff00ff #11ff00ff #0bff00ff #05ff00ff #00ff00ff #00ff06ff #00ff0bff #00ff12ff #00ff17ff #00ff1eff #00ff24ff #00ff2aff #00ff2fff #00ff36ff #00ff3bff #00ff42ff #00ff48ff #00ff4eff #00ff54ff #00ff5aff #00ff60ff #00ff66ff #00ff6cff #00ff72ff #00ff78ff #00ff7eff #00ff84ff #00ff8aff #00ff90ff #00ff96ff #00ff9cff #00ffa2ff #00ffa8ff #00ffaeff #00ffb4ff #00ffbaff #00ffc0ff #00ffc6ff #00ffccff #00ffd2ff #00ffd8ff #00ffdeff #00ffe4ff #00ffeaff #00fff0ff #00fff6ff #00fffcff #00fbffff #00f5ffff #00efffff #00e9ffff #00e3ffff #00ddffff #00d7ffff #00d1ffff #00cbffff #00c5ffff #00bfffff #00b9ffff #00b3ffff #00adffff #00a7ffff #00a2ffff #009bffff #0095ffff #008fffff #0089ffff #0083ffff #007dffff #0077ffff #0071ffff #006bffff #0065ffff #005fffff #0059ffff #0053ffff #004dffff #0047ffff #0041ffff #003bffff #0035ffff #002fffff #0029ffff #0023ffff #001dffff #0017ffff #0011ffff #000bffff #0005ffff #0000ffff #0600ffff #0c00ffff #1200ffff #1700ffff #1e00ffff #2400ffff #2900ffff #2f00ffff #3600ffff #3c00ffff #4200ffff #4800ffff #4e00ffff #5400ffff #5a00ffff #5f00ffff #6600ffff #6c00ffff #7200ffff #7700ffff #7e00ffff #8400ffff #8a00ffff #9000ffff #9600ffff #9c00ffff #a200ffff #a800ffff #ae00ffff #b400ffff #ba00ffff #c000ffff #c600ffff #cc00ffff #d200ffff #d800ffff #de00ffff #e400ffff #ea00ffff #f000ffff #f600ffff #fc00ffff #ff00fbff #ff00f5ff #ff00efff #ff00e9ff #ff00e3ff #ff00ddff #ff00d7ff #ff00d1ff #ff00cbff #ff00c5ff #ff00bfff #ff00b9ff #ff00b3ff #ff00adff #ff00a7ff #ff00a1ff #ff009bff #ff0095ff #ff008fff #ff0089ff #ff0083ff #ff007dff #ff0077ff #ff0071ff #ff006bff #ff0065ff #ff005fff #ff0059ff #ff0053ff #ff004dff #ff0047ff #ff0041ff #ff003bff #ff0035ff #ff002fff #ff0029ff #ff0023ff #ff001dff #ff0017ff #ff0011ff #ff000bff #ff0005ff #ff0000ff</td>
	</tr>
	<tr>
		<td>lighting</td>
		<td>
If true, light is simulated on the mesh. Otherwise, no lighting effect.
		</td>
		<td>1</td>
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
|topology|Link to a topology|BaseMeshTopology|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec1d&gt;|
|stressEvaluator|The component in charge of evaluating the Cauchy stress.|CauchyStressEvaluator&lt;Vec1d&gt;|

<!-- generate_doc -->
## Vec2d,Edge...

Templates:

- Vec2d,Edge
- Vec2d,Quad
- Vec2d,Triangle

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- TopologyAccessor
- SingleStateAccessor

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
		<td>nodalStress</td>
		<td>
Local nodal von Mises stress values
		</td>
		<td></td>
	</tr>
	<tr>
		<td>colorMap</td>
		<td>
Color map
		</td>
		<td>#ff0000ff #ff0500ff #ff0b00ff #ff1100ff #ff1700ff #ff1d00ff #ff2300ff #ff2900ff #ff2f00ff #ff3500ff #ff3b00ff #ff4100ff #ff4700ff #ff4e00ff #ff5400ff #ff5900ff #ff5f00ff #ff6600ff #ff6c00ff #ff7100ff #ff7700ff #ff7e00ff #ff8400ff #ff8a00ff #ff9000ff #ff9600ff #ff9c00ff #ffa200ff #ffa800ff #ffae00ff #ffb400ff #ffba00ff #ffc000ff #ffc600ff #ffcc00ff #ffd200ff #ffd800ff #ffde00ff #ffe400ff #ffea00ff #fff000ff #fff600ff #fffc00ff #fbff00ff #f5ff00ff #efff00ff #e9ff00ff #e3ff00ff #ddff00ff #d7ff00ff #d1ff00ff #cbff00ff #c5ff00ff #bfff00ff #b9ff00ff #b3ff00ff #adff00ff #a7ff00ff #a1ff00ff #9bff00ff #95ff00ff #8fff00ff #89ff00ff #83ff00ff #7dff00ff #77ff00ff #71ff00ff #6bff00ff #65ff00ff #5fff00ff #59ff00ff #53ff00ff #4dff00ff #47ff00ff #41ff00ff #3bff00ff #35ff00ff #2fff00ff #29ff00ff #23ff00ff #1dff00ff #17ff00ff #11ff00ff #0bff00ff #05ff00ff #00ff00ff #00ff06ff #00ff0bff #00ff12ff #00ff17ff #00ff1eff #00ff24ff #00ff2aff #00ff2fff #00ff36ff #00ff3bff #00ff42ff #00ff48ff #00ff4eff #00ff54ff #00ff5aff #00ff60ff #00ff66ff #00ff6cff #00ff72ff #00ff78ff #00ff7eff #00ff84ff #00ff8aff #00ff90ff #00ff96ff #00ff9cff #00ffa2ff #00ffa8ff #00ffaeff #00ffb4ff #00ffbaff #00ffc0ff #00ffc6ff #00ffccff #00ffd2ff #00ffd8ff #00ffdeff #00ffe4ff #00ffeaff #00fff0ff #00fff6ff #00fffcff #00fbffff #00f5ffff #00efffff #00e9ffff #00e3ffff #00ddffff #00d7ffff #00d1ffff #00cbffff #00c5ffff #00bfffff #00b9ffff #00b3ffff #00adffff #00a7ffff #00a2ffff #009bffff #0095ffff #008fffff #0089ffff #0083ffff #007dffff #0077ffff #0071ffff #006bffff #0065ffff #005fffff #0059ffff #0053ffff #004dffff #0047ffff #0041ffff #003bffff #0035ffff #002fffff #0029ffff #0023ffff #001dffff #0017ffff #0011ffff #000bffff #0005ffff #0000ffff #0600ffff #0c00ffff #1200ffff #1700ffff #1e00ffff #2400ffff #2900ffff #2f00ffff #3600ffff #3c00ffff #4200ffff #4800ffff #4e00ffff #5400ffff #5a00ffff #5f00ffff #6600ffff #6c00ffff #7200ffff #7700ffff #7e00ffff #8400ffff #8a00ffff #9000ffff #9600ffff #9c00ffff #a200ffff #a800ffff #ae00ffff #b400ffff #ba00ffff #c000ffff #c600ffff #cc00ffff #d200ffff #d800ffff #de00ffff #e400ffff #ea00ffff #f000ffff #f600ffff #fc00ffff #ff00fbff #ff00f5ff #ff00efff #ff00e9ff #ff00e3ff #ff00ddff #ff00d7ff #ff00d1ff #ff00cbff #ff00c5ff #ff00bfff #ff00b9ff #ff00b3ff #ff00adff #ff00a7ff #ff00a1ff #ff009bff #ff0095ff #ff008fff #ff0089ff #ff0083ff #ff007dff #ff0077ff #ff0071ff #ff006bff #ff0065ff #ff005fff #ff0059ff #ff0053ff #ff004dff #ff0047ff #ff0041ff #ff003bff #ff0035ff #ff002fff #ff0029ff #ff0023ff #ff001dff #ff0017ff #ff0011ff #ff000bff #ff0005ff #ff0000ff</td>
	</tr>
	<tr>
		<td>lighting</td>
		<td>
If true, light is simulated on the mesh. Otherwise, no lighting effect.
		</td>
		<td>1</td>
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
|topology|Link to a topology|BaseMeshTopology|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec2d&gt;|
|stressEvaluator|The component in charge of evaluating the Cauchy stress.|CauchyStressEvaluator&lt;Vec2d&gt;|

<!-- generate_doc -->
## Vec3d,Edge...

Templates:

- Vec3d,Edge
- Vec3d,Hexahedron
- Vec3d,Prism
- Vec3d,Pyramid
- Vec3d,Quad
- Vec3d,Tetrahedron
- Vec3d,Triangle

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- TopologyAccessor
- SingleStateAccessor

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
		<td>nodalStress</td>
		<td>
Local nodal von Mises stress values
		</td>
		<td></td>
	</tr>
	<tr>
		<td>colorMap</td>
		<td>
Color map
		</td>
		<td>#ff0000ff #ff0500ff #ff0b00ff #ff1100ff #ff1700ff #ff1d00ff #ff2300ff #ff2900ff #ff2f00ff #ff3500ff #ff3b00ff #ff4100ff #ff4700ff #ff4e00ff #ff5400ff #ff5900ff #ff5f00ff #ff6600ff #ff6c00ff #ff7100ff #ff7700ff #ff7e00ff #ff8400ff #ff8a00ff #ff9000ff #ff9600ff #ff9c00ff #ffa200ff #ffa800ff #ffae00ff #ffb400ff #ffba00ff #ffc000ff #ffc600ff #ffcc00ff #ffd200ff #ffd800ff #ffde00ff #ffe400ff #ffea00ff #fff000ff #fff600ff #fffc00ff #fbff00ff #f5ff00ff #efff00ff #e9ff00ff #e3ff00ff #ddff00ff #d7ff00ff #d1ff00ff #cbff00ff #c5ff00ff #bfff00ff #b9ff00ff #b3ff00ff #adff00ff #a7ff00ff #a1ff00ff #9bff00ff #95ff00ff #8fff00ff #89ff00ff #83ff00ff #7dff00ff #77ff00ff #71ff00ff #6bff00ff #65ff00ff #5fff00ff #59ff00ff #53ff00ff #4dff00ff #47ff00ff #41ff00ff #3bff00ff #35ff00ff #2fff00ff #29ff00ff #23ff00ff #1dff00ff #17ff00ff #11ff00ff #0bff00ff #05ff00ff #00ff00ff #00ff06ff #00ff0bff #00ff12ff #00ff17ff #00ff1eff #00ff24ff #00ff2aff #00ff2fff #00ff36ff #00ff3bff #00ff42ff #00ff48ff #00ff4eff #00ff54ff #00ff5aff #00ff60ff #00ff66ff #00ff6cff #00ff72ff #00ff78ff #00ff7eff #00ff84ff #00ff8aff #00ff90ff #00ff96ff #00ff9cff #00ffa2ff #00ffa8ff #00ffaeff #00ffb4ff #00ffbaff #00ffc0ff #00ffc6ff #00ffccff #00ffd2ff #00ffd8ff #00ffdeff #00ffe4ff #00ffeaff #00fff0ff #00fff6ff #00fffcff #00fbffff #00f5ffff #00efffff #00e9ffff #00e3ffff #00ddffff #00d7ffff #00d1ffff #00cbffff #00c5ffff #00bfffff #00b9ffff #00b3ffff #00adffff #00a7ffff #00a2ffff #009bffff #0095ffff #008fffff #0089ffff #0083ffff #007dffff #0077ffff #0071ffff #006bffff #0065ffff #005fffff #0059ffff #0053ffff #004dffff #0047ffff #0041ffff #003bffff #0035ffff #002fffff #0029ffff #0023ffff #001dffff #0017ffff #0011ffff #000bffff #0005ffff #0000ffff #0600ffff #0c00ffff #1200ffff #1700ffff #1e00ffff #2400ffff #2900ffff #2f00ffff #3600ffff #3c00ffff #4200ffff #4800ffff #4e00ffff #5400ffff #5a00ffff #5f00ffff #6600ffff #6c00ffff #7200ffff #7700ffff #7e00ffff #8400ffff #8a00ffff #9000ffff #9600ffff #9c00ffff #a200ffff #a800ffff #ae00ffff #b400ffff #ba00ffff #c000ffff #c600ffff #cc00ffff #d200ffff #d800ffff #de00ffff #e400ffff #ea00ffff #f000ffff #f600ffff #fc00ffff #ff00fbff #ff00f5ff #ff00efff #ff00e9ff #ff00e3ff #ff00ddff #ff00d7ff #ff00d1ff #ff00cbff #ff00c5ff #ff00bfff #ff00b9ff #ff00b3ff #ff00adff #ff00a7ff #ff00a1ff #ff009bff #ff0095ff #ff008fff #ff0089ff #ff0083ff #ff007dff #ff0077ff #ff0071ff #ff006bff #ff0065ff #ff005fff #ff0059ff #ff0053ff #ff004dff #ff0047ff #ff0041ff #ff003bff #ff0035ff #ff002fff #ff0029ff #ff0023ff #ff001dff #ff0017ff #ff0011ff #ff000bff #ff0005ff #ff0000ff</td>
	</tr>
	<tr>
		<td>lighting</td>
		<td>
If true, light is simulated on the mesh. Otherwise, no lighting effect.
		</td>
		<td>1</td>
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
|topology|Link to a topology|BaseMeshTopology|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|stressEvaluator|The component in charge of evaluating the Cauchy stress.|CauchyStressEvaluator&lt;Vec3d&gt;|

## Examples 

VonMisesStress.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9.81 0" dt="0.01">
    
        <Node name="plugins">
            <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin pluginName="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
            <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [FEMMass,NodalMassDensity] -->
            <RequiredPlugin pluginName="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [LinearSmallStrainFEMForceField,VonMisesStress] -->
            <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        </Node>
    
        <DefaultAnimationLoop/>
    
        <VisualStyle displayFlags="showBehaviorModels showVisualModels" />
    
        <EulerImplicitSolver name="ODE_solver" rayleighStiffness="0.01" rayleighMass="0.01" />
        <SparseLDLSolver name="linear_solver" template="CompressedRowSparseMatrixMat3x3"/>
    
        <RegularGridTopology name="grid" n="20 5 5" min="0 -0.05 -0.05" max="0.4 0.05 0.05" />
        <MechanicalObject template="Vec3" name="state"/>
    
        <BoxROI name="boxLeft" box="-0.01 -0.51 -0.51  0.001 0.51 0.51"/>
        <FixedProjectiveConstraint indices="@boxLeft.indices"/>
    
        <NodalMassDensity property="1100"/>
        <FEMMass template="Vec3,Hexahedron" topology="@grid"/>
    
        <LinearSmallStrainFEMForceField name="FEM" template="Vec3,Hexahedron"
                                        youngModulus="500000" poissonRatio="0.45"/>
    
        <VonMisesStress template="Vec3,Hexahedron" name="stress" topology="@grid" stressEvaluator="@FEM"
                        colorMap="green yellow orange red purple #221C35"/>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.01")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")

       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisualModels")
       root.addObject('EulerImplicitSolver', name="ODE_solver", rayleighStiffness="0.01", rayleighMass="0.01")
       root.addObject('SparseLDLSolver', name="linear_solver", template="CompressedRowSparseMatrixMat3x3")
       root.addObject('RegularGridTopology', name="grid", n="20 5 5", min="0 -0.05 -0.05", max="0.4 0.05 0.05")
       root.addObject('MechanicalObject', template="Vec3", name="state")
       root.addObject('BoxROI', name="boxLeft", box="-0.01 -0.51 -0.51  0.001 0.51 0.51")
       root.addObject('FixedProjectiveConstraint', indices="@boxLeft.indices")
       root.addObject('NodalMassDensity', property="1100")
       root.addObject('FEMMass', template="Vec3,Hexahedron", topology="@grid")
       root.addObject('LinearSmallStrainFEMForceField', name="FEM", template="Vec3,Hexahedron", youngModulus="500000", poissonRatio="0.45")
       root.addObject('VonMisesStress', template="Vec3,Hexahedron", name="stress", topology="@grid", stressEvaluator="@FEM", colorMap="green yellow orange red purple #221C35")
    ```

