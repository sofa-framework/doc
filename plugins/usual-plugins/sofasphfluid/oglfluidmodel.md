<!-- generate_doc -->
# OglFluidModel

Particle model for OpenGL display, using glsl


## Vec3d

Templates:

- Vec3d

__Target__: SofaSphFluid

__namespace__: sofa::component::visualmodel

__parents__:

- VisualModel

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
		<td>enable</td>
		<td>
Display the object or not
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Vertices coordinates
		</td>
		<td></td>
	</tr>
	<tr>
		<td>debugFBO</td>
		<td>
DEBUG FBO
		</td>
		<td>9</td>
	</tr>
	<tr>
		<td>spriteRadius</td>
		<td>
Radius of sprites
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>spriteThickness</td>
		<td>
Thickness of sprites
		</td>
		<td>0.01</td>
	</tr>
	<tr>
		<td>spriteBlurRadius</td>
		<td>
Blur radius (in pixels)
		</td>
		<td>10</td>
	</tr>
	<tr>
		<td>spriteBlurScale</td>
		<td>
Blur scale
		</td>
		<td>0.1</td>
	</tr>
	<tr>
		<td>spriteBlurDepthFalloff</td>
		<td>
Blur Depth Falloff
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>spriteDiffuseColor</td>
		<td>
Diffuse Color
		</td>
		<td>0 0 1 1</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|

## Examples 

OglFluidModel_SPH.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node dt="0.01" gravity="0 -20 0.0" >
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [EulerExplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="SofaSphFluid"/> <!-- Needed to use components [OglFluidModel SPHFluidForceField SpatialGridContainer] -->
        <VisualStyle displayFlags="hideBehaviorModels hideForceFields hideCollisionModels" />
    
        <DefaultAnimationLoop/>
        <Node name="SPH" >
            <EulerExplicitSolver symplectic="1" />
            <RegularGridTopology nx="5" ny="400" nz="5" xmin="-3.0" xmax="0" ymin="-3" ymax="36" zmin="-3.0" zmax="0" />
            <MechanicalObject name="MModel" />
            <!-- A topology is used here just to set initial particles positions. It is a bad idea because this object has no real topology, but it works... -->
            <UniformMass name="M1" vertexMass="1" />
            <SpatialGridContainer cellWidth="0.75" />
            <SPHFluidForceField radius="0.745" density="15" kernelType="1" viscosityType="2" viscosity="10" pressure="1000" surfaceTension="-1000" printLog="0" />
            <!-- The following force fields handle collision with walls and an inclined floor -->
            <PlaneForceField normal="1 0 0" d="-4" />
            <PlaneForceField normal="-1 0 0" d="-4" />
            <PlaneForceField normal="0.5 1 0.1" d="-4" />
            <PlaneForceField normal="0 0 1" d="-10" />
            <PlaneForceField normal="0 0 -1" d="-10" />
        </Node>
        
        <Node name="Fluid" >            
            <OglFluidModel template="Vec3d" position="@../SPH/MModel.position" 
                debugFBO="9"
                spriteRadius="0.5" spriteThickness="0.015" spriteBlurRadius="10" spriteBlurScale="10" spriteBlurDepthFalloff="1"  />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       node = root_node.addChild('node', dt="0.01", gravity="0 -20 0.0")

       node.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       node.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
       node.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
       node.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       node.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       node.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       node.addObject('RequiredPlugin', name="SofaSphFluid")
       node.addObject('VisualStyle', displayFlags="hideBehaviorModels hideForceFields hideCollisionModels")
       node.addObject('DefaultAnimationLoop', )

       sph = node.addChild('SPH')

       sph.addObject('EulerExplicitSolver', symplectic="1")
       sph.addObject('RegularGridTopology', nx="5", ny="400", nz="5", xmin="-3.0", xmax="0", ymin="-3", ymax="36", zmin="-3.0", zmax="0")
       sph.addObject('MechanicalObject', name="MModel")
       sph.addObject('UniformMass', name="M1", vertexMass="1")
       sph.addObject('SpatialGridContainer', cellWidth="0.75")
       sph.addObject('SPHFluidForceField', radius="0.745", density="15", kernelType="1", viscosityType="2", viscosity="10", pressure="1000", surfaceTension="-1000", printLog="0")
       sph.addObject('PlaneForceField', normal="1 0 0", d="-4")
       sph.addObject('PlaneForceField', normal="-1 0 0", d="-4")
       sph.addObject('PlaneForceField', normal="0.5 1 0.1", d="-4")
       sph.addObject('PlaneForceField', normal="0 0 1", d="-10")
       sph.addObject('PlaneForceField', normal="0 0 -1", d="-10")

       fluid = node.addChild('Fluid')

       fluid.addObject('OglFluidModel', template="Vec3d", position="@../SPH/MModel.position", debugFBO="9", spriteRadius="0.5", spriteThickness="0.015", spriteBlurRadius="10", spriteBlurScale="10", spriteBlurDepthFalloff="1")
    ```

OglFluidModel_SPHParticles.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node dt="0.01" gravity="0 -10 0" bbox="-6 -6 -6  6 6 6">
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [EulerExplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [PointSetTopologyContainer PointSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="SofaSphFluid"/> <!-- Needed to use components [OglFluidModel ParticleSink ParticleSource SPHFluidForceField SpatialGridContainer] -->
        <VisualStyle displayFlags="hideBehaviorModels hideForceFields hideWireframe" />
    
        <DefaultAnimationLoop/>
        <Node name="Particles">
            <EulerExplicitSolver symplectic="1" />
            <MechanicalObject name="MModel"/>
            <ParticleSource name="Source" translation="0 20 0" radius="0.01 0.1 0.01" velocity="0 -10 0" delay="0.02" start="0.0" stop="10" printLog="0"
            center="-0.375 0 -0.75 
                0.0 0.0 -0.75 
                0.375 0.0 -0.75 
                -0.75  0.0 -0.375 
                -0.375 0.0 -0.375 
                0.0 0.0 -0.375 
                0.375 0.0 -0.375 
                0.75 0.0 -0.375 
                -0.75 0.0 0.0 
                -0.375 0.0 0.0 
                0.0 0.0 0.0 
                0.375 0.0 0.0 
                0.75 0.0 0.0 
                -0.75 0.0 0.375 
                -0.375 0.0 0.375 
                0.0 0.0 0.375 
                0.375 0.0 0.375 
                0.75 0.0 0.375 
                -0.375 0.0 0.75 
                0.0 0.0 0.75 
                0.375 0.0 0.75"  />
            
            <UniformMass name="M1" vertexMass="1.0" />
            <PointSetTopologyContainer name="con" />
            <PointSetTopologyModifier name="mod" />
            
            <SpatialGridContainer cellWidth="0.75" />
            <SPHFluidForceField radius="0.7" density="25" kernelType="1" viscosityType="2" viscosity="10" pressure="1000" surfaceTension="-1000" printLog="0" />
    
            <ParticleSink name="sink" normal="0 1 0" d0="1" d1="0" showPlane="0" printLog="0" />
            <Node name="Fluid" >            
                <OglFluidModel template="Vec3d" position="@../MModel.position" 
                    debugFBO="9"
                    spriteRadius="0.5" spriteThickness="0.015" spriteBlurRadius="10" spriteBlurScale="10" spriteBlurDepthFalloff="1"  />
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       node = root_node.addChild('node', dt="0.01", gravity="0 -10 0", bbox="-6 -6 -6  6 6 6")

       node.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       node.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
       node.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       node.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       node.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       node.addObject('RequiredPlugin', name="SofaSphFluid")
       node.addObject('VisualStyle', displayFlags="hideBehaviorModels hideForceFields hideWireframe")
       node.addObject('DefaultAnimationLoop', )

       particles = node.addChild('Particles')

       particles.addObject('EulerExplicitSolver', symplectic="1")
       particles.addObject('MechanicalObject', name="MModel")
       particles.addObject('ParticleSource', name="Source", translation="0 20 0", radius="0.01 0.1 0.01", velocity="0 -10 0", delay="0.02", start="0.0", stop="10", printLog="0", center="-0.375 0 -0.75              0.0 0.0 -0.75              0.375 0.0 -0.75              -0.75  0.0 -0.375              -0.375 0.0 -0.375              0.0 0.0 -0.375              0.375 0.0 -0.375              0.75 0.0 -0.375              -0.75 0.0 0.0              -0.375 0.0 0.0              0.0 0.0 0.0              0.375 0.0 0.0              0.75 0.0 0.0              -0.75 0.0 0.375              -0.375 0.0 0.375              0.0 0.0 0.375              0.375 0.0 0.375              0.75 0.0 0.375              -0.375 0.0 0.75              0.0 0.0 0.75              0.375 0.0 0.75")
       particles.addObject('UniformMass', name="M1", vertexMass="1.0")
       particles.addObject('PointSetTopologyContainer', name="con")
       particles.addObject('PointSetTopologyModifier', name="mod")
       particles.addObject('SpatialGridContainer', cellWidth="0.75")
       particles.addObject('SPHFluidForceField', radius="0.7", density="25", kernelType="1", viscosityType="2", viscosity="10", pressure="1000", surfaceTension="-1000", printLog="0")
       particles.addObject('ParticleSink', name="sink", normal="0 1 0", d0="1", d1="0", showPlane="0", printLog="0")

       fluid = Particles.addChild('Fluid')

       fluid.addObject('OglFluidModel', template="Vec3d", position="@../MModel.position", debugFBO="9", spriteRadius="0.5", spriteThickness="0.015", spriteBlurRadius="10", spriteBlurScale="10", spriteBlurDepthFalloff="1")
    ```

