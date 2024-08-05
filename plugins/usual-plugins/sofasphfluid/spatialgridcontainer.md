# SpatialGridContainer

Hashing spatial grid container, used for SPH fluids for instance.
GPU support using CUDA.


__Templates__:

- `#!c++ Vec3d`

__Target__: `SofaSphFluid`

__namespace__: `#!c++ sofa::component::container`

__parents__: 

- `#!c++ BaseObject`

__categories__: 

- _Miscellaneous

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
		<td>cellWidth</td>
		<td>
Width each cell in the grid. If it is used to compute neighboors, it should be greater than the max radius considered.
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>autoUpdate</td>
		<td>
Automatically update the grid at each iteration.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>sortPoints</td>
		<td>
Sort points depending on which cell they are in the grid. This is required for efficient collision detection.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showGrid</td>
		<td>
activate rendering of the grid
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



## Examples

SofaSphFluid/share/sofa/examples/SofaSphFluid/SpatialGridContainer.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node dt="0.005" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="SofaSphFluid"/> <!-- Needed to use components [SPHFluidForceField SpatialGridContainer] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <DefaultAnimationLoop/>
        <Node name="Liver">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <!-- A topology is used here just to set initial particles positions. It is a bad idea because this object has no real topology, but it works... -->
            <RegularGridTopology nx="5" ny="40" nz="5" xmin="-1.5" xmax="0" ymin="-3" ymax="12" zmin="-1.5" zmax="0"/>
            
            <MechanicalObject name="MModel" />
            <UniformMass name="M1" vertexMass="1" />
            
            <SpatialGridContainer showGrid="1"/>
            <SPHFluidForceField radius="0.745" density="15" kernelType="1" viscosityType="2" viscosity="10" pressure="1000" surfaceTension="-1000" printLog="0" />
            
            <!-- The following force fields handle collision with walls and an inclined floor -->
            <PlaneForceField normal="0.5 1 0.1" d="-4" showPlane="1"/>        
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        rootNode = rootNode.addChild('rootNode', dt="0.005", gravity="0 -10 0")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        rootNode.addObject('RequiredPlugin', name="SofaSphFluid")
        rootNode.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        rootNode.addObject('DefaultAnimationLoop')

        Liver = rootNode.addChild('Liver')
        Liver.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        Liver.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Liver.addObject('RegularGridTopology', nx="5", ny="40", nz="5", xmin="-1.5", xmax="0", ymin="-3", ymax="12", zmin="-1.5", zmax="0")
        Liver.addObject('MechanicalObject', name="MModel")
        Liver.addObject('UniformMass', name="M1", vertexMass="1")
        Liver.addObject('SpatialGridContainer', showGrid="1")
        Liver.addObject('SPHFluidForceField', radius="0.745", density="15", kernelType="1", viscosityType="2", viscosity="10", pressure="1000", surfaceTension="-1000", printLog="0")
        Liver.addObject('PlaneForceField', normal="0.5 1 0.1", d="-4", showPlane="1")
    ```

