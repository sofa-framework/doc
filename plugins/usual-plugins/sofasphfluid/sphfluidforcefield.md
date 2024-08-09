# SPHFluidForceField

Smooth Particle Hydrodynamics
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Vec3d`

__Target__: `SofaSphFluid`

__namespace__: `#!c++ sofa::component::forcefield`

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
		<td>radius</td>
		<td>
Radius of a Particle
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mass</td>
		<td>
Mass of a Particle
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>pressure</td>
		<td>
Pressure
</td>
		<td>100</td>
	</tr>
	<tr>
		<td>density</td>
		<td>
Density
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>viscosity</td>
		<td>
Viscosity
</td>
		<td>0.001</td>
	</tr>
	<tr>
		<td>surfaceTension</td>
		<td>
Surface Tension
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>kernelType</td>
		<td>
0 = default kernels, 1 = cubic spline
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>pressureType</td>
		<td>
0 = none, 1 = default pressure
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>viscosityType</td>
		<td>
0 = none, 1 = default d_viscosity using kernel Laplacian, 2 = artificial d_viscosity
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>surfaceTensionType</td>
		<td>
0 = none, 1 = default surface tension using kernel Laplacian, 2 = cohesion forces surface tension from Becker et al. 2007
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>debugGrid</td>
		<td>
If true will store additionnal information on the grid to check neighbors and draw them
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

SofaSphFluid/share/sofa/examples/SofaSphFluid/SPHFluidForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node dt="0.01" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [EulerExplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="SofaSphFluid"/> <!-- Needed to use components [SPHFluidForceField SpatialGridContainer] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields showCollisionModels" />
    
        <DefaultAnimationLoop/>
        <Node>
            <EulerExplicitSolver symplectic="1" />
            <MechanicalObject name="MModel" />
            <!-- A topology is used here just to set initial particles positions. It is a bad idea because this object has no real topology, but it works... -->
            <RegularGridTopology nx="5" ny="40" nz="5" xmin="-1.5" xmax="0" ymin="-3" ymax="12" zmin="-1.5" zmax="0"/>
            <UniformMass name="M1" vertexMass="1" />
            <SpatialGridContainer cellWidth="0.75" />
            <SPHFluidForceField radius="0.745" density="15" kernelType="1" viscosityType="2" viscosity="10" pressure="1000" surfaceTension="-1000" printLog="0" />
            <!-- The following force fields handle collision with walls and an inclined floor -->
            <PlaneForceField normal="1 0 0" d="-4" showPlane="1"/>
            <PlaneForceField normal="-1 0 0" d="-4" showPlane="1"/>
            <PlaneForceField normal="0.5 1 0.1" d="-4" showPlane="1"/>
            <PlaneForceField normal="0 0 1" d="-4" showPlane="1"/>
            <PlaneForceField normal="0 0 -1" d="-4" showPlane="1"/>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        rootNode = rootNode.addChild('rootNode', dt="0.01", gravity="0 -10 0")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        rootNode.addObject('RequiredPlugin', name="SofaSphFluid")
        rootNode.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showCollisionModels")
        rootNode.addObject('DefaultAnimationLoop')

        rootNode = rootNode.addChild('rootNode')
        rootNode.addObject('EulerExplicitSolver', symplectic="1")
        rootNode.addObject('MechanicalObject', name="MModel")
        rootNode.addObject('RegularGridTopology', nx="5", ny="40", nz="5", xmin="-1.5", xmax="0", ymin="-3", ymax="12", zmin="-1.5", zmax="0")
        rootNode.addObject('UniformMass', name="M1", vertexMass="1")
        rootNode.addObject('SpatialGridContainer', cellWidth="0.75")
        rootNode.addObject('SPHFluidForceField', radius="0.745", density="15", kernelType="1", viscosityType="2", viscosity="10", pressure="1000", surfaceTension="-1000", printLog="0")
        rootNode.addObject('PlaneForceField', normal="1 0 0", d="-4", showPlane="1")
        rootNode.addObject('PlaneForceField', normal="-1 0 0", d="-4", showPlane="1")
        rootNode.addObject('PlaneForceField', normal="0.5 1 0.1", d="-4", showPlane="1")
        rootNode.addObject('PlaneForceField', normal="0 0 1", d="-4", showPlane="1")
        rootNode.addObject('PlaneForceField', normal="0 0 -1", d="-4", showPlane="1")
    ```

SofaSphFluid/share/sofa/examples/SofaSphFluid/SPHFluidForceField_benchmarks.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node dt="0.01" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="SofaSphFluid"/> <!-- Needed to use components [SPHFluidForceField SpatialGridContainer] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields showCollisionModels" />
    
        <DefaultAnimationLoop/>
        <Node name="Less_pressure">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <MechanicalObject name="Model" />
            <RegularGridTopology nx="5" ny="40" nz="5" xmin="-1.5" xmax="0" ymin="0" ymax="15" zmin="10" zmax="11.5"/>
            <UniformMass name="M1" vertexMass="1" />
            <SpatialGridContainer cellWidth="0.75"/>
            <SPHFluidForceField radius="0.745" density="15" kernelType="1" viscosityType="2" viscosity="10" pressure="10" surfaceTension="-1000" printLog="0" />
    
            <PlaneForceField normal="1 0 0" d="-4" showPlane="0"/>
            <PlaneForceField normal="-1 0 0" d="-14" showPlane="0"/>
            <PlaneForceField normal="0.3 1 0" d="-4" showPlane="1"/>
            <PlaneForceField normal="0 0 1" d="6" showPlane="1"/>
            <PlaneForceField normal="0 0 -1" d="-14" showPlane="1"/>
        </Node> 
        
        <Node name="Normal">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <MechanicalObject name="MModel" />
            <RegularGridTopology nx="5" ny="40" nz="5" xmin="-1.5" xmax="0" ymin="0" ymax="15" zmin="-1.5" zmax="0"/>
            <UniformMass name="M1" vertexMass="1" />
            <SpatialGridContainer cellWidth="0.75"/>
            <SPHFluidForceField radius="0.745" density="15" kernelType="1" viscosityType="2" viscosity="10" pressure="1000" surfaceTension="-1000" printLog="0" />
            
            <PlaneForceField normal="1 0 0" d="-4" showPlane="0"/>
            <PlaneForceField normal="-1 0 0" d="-14" showPlane="0"/>
            <PlaneForceField normal="0.3 1 0" d="-4" showPlane="1"/>
            <PlaneForceField normal="0 0 1" d="-4" showPlane="1"/>
            <PlaneForceField normal="0 0 -1" d="-4" showPlane="1"/>
        </Node>
        
        
        <Node name="Double">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <MechanicalObject name="MModel" />
            <RegularGridTopology nx="5" ny="80" nz="5" xmin="-1.5" xmax="0" ymin="0" ymax="15" zmin="-11.5" zmax="-10"/>
            <UniformMass name="M1" vertexMass="1" />
            <SpatialGridContainer cellWidth="0.75"/>
            <SPHFluidForceField radius="0.745" density="30" kernelType="1" viscosityType="2" viscosity="10" pressure="1000" surfaceTension="-1000" printLog="0" />
            
            <PlaneForceField normal="1 0 0" d="-4" showPlane="0"/>
            <PlaneForceField normal="-1 0 0" d="-14" showPlane="0"/>
            <PlaneForceField normal="0.3 1 0" d="-4" showPlane="1"/>
            <PlaneForceField normal="0 0 1" d="-14" showPlane="1"/>
            <PlaneForceField normal="0 0 -1" d="6" showPlane="1"/>
        </Node>
        
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        rootNode = rootNode.addChild('rootNode', dt="0.01", gravity="0 -10 0")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        rootNode.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        rootNode.addObject('RequiredPlugin', name="SofaSphFluid")
        rootNode.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showCollisionModels")
        rootNode.addObject('DefaultAnimationLoop')

        Less_pressure = rootNode.addChild('Less_pressure')
        Less_pressure.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        Less_pressure.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Less_pressure.addObject('MechanicalObject', name="Model")
        Less_pressure.addObject('RegularGridTopology', nx="5", ny="40", nz="5", xmin="-1.5", xmax="0", ymin="0", ymax="15", zmin="10", zmax="11.5")
        Less_pressure.addObject('UniformMass', name="M1", vertexMass="1")
        Less_pressure.addObject('SpatialGridContainer', cellWidth="0.75")
        Less_pressure.addObject('SPHFluidForceField', radius="0.745", density="15", kernelType="1", viscosityType="2", viscosity="10", pressure="10", surfaceTension="-1000", printLog="0")
        Less_pressure.addObject('PlaneForceField', normal="1 0 0", d="-4", showPlane="0")
        Less_pressure.addObject('PlaneForceField', normal="-1 0 0", d="-14", showPlane="0")
        Less_pressure.addObject('PlaneForceField', normal="0.3 1 0", d="-4", showPlane="1")
        Less_pressure.addObject('PlaneForceField', normal="0 0 1", d="6", showPlane="1")
        Less_pressure.addObject('PlaneForceField', normal="0 0 -1", d="-14", showPlane="1")

        Normal = rootNode.addChild('Normal')
        Normal.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        Normal.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Normal.addObject('MechanicalObject', name="MModel")
        Normal.addObject('RegularGridTopology', nx="5", ny="40", nz="5", xmin="-1.5", xmax="0", ymin="0", ymax="15", zmin="-1.5", zmax="0")
        Normal.addObject('UniformMass', name="M1", vertexMass="1")
        Normal.addObject('SpatialGridContainer', cellWidth="0.75")
        Normal.addObject('SPHFluidForceField', radius="0.745", density="15", kernelType="1", viscosityType="2", viscosity="10", pressure="1000", surfaceTension="-1000", printLog="0")
        Normal.addObject('PlaneForceField', normal="1 0 0", d="-4", showPlane="0")
        Normal.addObject('PlaneForceField', normal="-1 0 0", d="-14", showPlane="0")
        Normal.addObject('PlaneForceField', normal="0.3 1 0", d="-4", showPlane="1")
        Normal.addObject('PlaneForceField', normal="0 0 1", d="-4", showPlane="1")
        Normal.addObject('PlaneForceField', normal="0 0 -1", d="-4", showPlane="1")

        Double = rootNode.addChild('Double')
        Double.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        Double.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Double.addObject('MechanicalObject', name="MModel")
        Double.addObject('RegularGridTopology', nx="5", ny="80", nz="5", xmin="-1.5", xmax="0", ymin="0", ymax="15", zmin="-11.5", zmax="-10")
        Double.addObject('UniformMass', name="M1", vertexMass="1")
        Double.addObject('SpatialGridContainer', cellWidth="0.75")
        Double.addObject('SPHFluidForceField', radius="0.745", density="30", kernelType="1", viscosityType="2", viscosity="10", pressure="1000", surfaceTension="-1000", printLog="0")
        Double.addObject('PlaneForceField', normal="1 0 0", d="-4", showPlane="0")
        Double.addObject('PlaneForceField', normal="-1 0 0", d="-14", showPlane="0")
        Double.addObject('PlaneForceField', normal="0.3 1 0", d="-4", showPlane="1")
        Double.addObject('PlaneForceField', normal="0 0 1", d="-14", showPlane="1")
        Double.addObject('PlaneForceField', normal="0 0 -1", d="6", showPlane="1")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/SPHFluidForceFieldCUDA.scn

=== "XML"

    ```xml
    <Node dt="0.005" showBehaviorModels="1" showCollisionModels="1" showMappings="0" showForceFields="1" gravity="0 -10 0" >
        <RequiredPlugin name="SofaOpenglVisual"/>
        <RequiredPlugin name="CUDA computing" pluginName="SofaCUDA" />
    	<Node>
    		<RungeKutta4Solver/>
    		<!--<CentralDifferenceSolver/>-->
            <!--<EulerImplicitSolver rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" tolerance="1e-5" threshold="1e-5"/>-->
    		<MechanicalObject name="MModel" template="CudaVec3f" />
    		<!-- A topology is used here just to set initial particles positions. It is a bad idea because this object has no real topology, but it works... -->
    		<RegularGridTopology
    			nx="5" ny="40" nz="5"
    			xmin="-1.5" xmax="0"
    			ymin="-3" ymax="12"
    			zmin="-1.5" zmax="0"
    		/>
    		<UniformMass name="M1" mass="1" />
    		<SpatialGridContainer cellWidth="1.5" />
    		<SPHFluidForceField radius="0.75" density="15" viscosity="10" pressure="1000" surfaceTension="-1000" />
    		<!-- The following force fields handle collision with walls and an inclined floor -->
    		<PlaneForceField normal="1 0 0" d="-4"/>
    		<PlaneForceField normal="-1 0 0" d="-4"/>
    		<PlaneForceField normal="0.5 1 0.1" d="-4"/>
    		<PlaneForceField normal="0 0 1" d="-4"/>
    		<PlaneForceField normal="0 0 -1" d="-4"/>
    <!--
    		<Node id="Visual">
    			<OglModel name="VModel" color="blue" useVBO="false"/>
    			<SPHFluidSurfaceMapping name="MarchingCube" input="@../MModel" output="@VModel" isoValue="0.5" radius="0.75" step="0.25"/>
    		</Node>
    -->
    	</Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        rootNode = rootNode.addChild('rootNode', dt="0.005", showBehaviorModels="1", showCollisionModels="1", showMappings="0", showForceFields="1", gravity="0 -10 0")
        rootNode.addObject('RequiredPlugin', name="SofaOpenglVisual")
        rootNode.addObject('RequiredPlugin', name="CUDA computing", pluginName="SofaCUDA")

        rootNode = rootNode.addChild('rootNode')
        rootNode.addObject('RungeKutta4Solver')
        rootNode.addObject('MechanicalObject', name="MModel", template="CudaVec3f")
        rootNode.addObject('RegularGridTopology', nx="5", ny="40", nz="5", xmin="-1.5", xmax="0", ymin="-3", ymax="12", zmin="-1.5", zmax="0")
        rootNode.addObject('UniformMass', name="M1", mass="1")
        rootNode.addObject('SpatialGridContainer', cellWidth="1.5")
        rootNode.addObject('SPHFluidForceField', radius="0.75", density="15", viscosity="10", pressure="1000", surfaceTension="-1000")
        rootNode.addObject('PlaneForceField', normal="1 0 0", d="-4")
        rootNode.addObject('PlaneForceField', normal="-1 0 0", d="-4")
        rootNode.addObject('PlaneForceField', normal="0.5 1 0.1", d="-4")
        rootNode.addObject('PlaneForceField', normal="0 0 1", d="-4")
        rootNode.addObject('PlaneForceField', normal="0 0 -1", d="-4")
    ```

