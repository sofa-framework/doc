# CudaHexahedronTLEDForceField

GPU-side TLED hexahedron forcefield using CUDA


__Target__: `SofaCUDA`

__namespace__: `#!c++ sofa::gpu::cuda`

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
		<td>poissonRatio</td>
		<td>
Poisson ratio in Hooke's law
</td>
		<td>0.45</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
Young modulus in Hooke's law
</td>
		<td>3000</td>
	</tr>
	<tr>
		<td>timestep</td>
		<td>
Simulation timestep
</td>
		<td>0.001</td>
	</tr>
	<tr>
		<td>isViscoelastic</td>
		<td>
Viscoelasticity flag
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>isAnisotropic</td>
		<td>
Anisotropy flag
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>preferredDirection</td>
		<td>
Transverse isotropy direction
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
|mstate|MechanicalState used by this component|



## Examples

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/CudaHexahedronTLEDForceField_beam10x10x40_gpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 0" dt="0.001">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [CentralDifferenceSolver] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaCUDA"/> <!-- Needed to use components [BoxROI CudaTetrahedronTLEDForceField DiagonalMass FixedProjectiveConstraint IdentityMapping MechanicalObject TetrahedronSetGeometryAlgorithms TriangleSetGeometryAlgorithms] -->
        
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
    	
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
        <CollisionPipeline name="CollisionPipeline" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="collision response" response="PenalityContactForceField" />
        <DiscreteIntersection/>
        
        <Node name="Beam">
            <RegularGridTopology name="grid" n="40 10 10" min="0 6 -2" max="16 10 2" />=
        </Node>
    
        <Node name="TetrahedronFEMForceField-GPU-Green">
            <CentralDifferenceSolver rayleighMass="5"/>
            
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="CudaVec3f"/>
    
            <HexahedronSetTopologyContainer name="Container" src="@../Beam/grid"/>
            <HexahedronSetTopologyModifier name="Modifier" />
            <HexahedronSetGeometryAlgorithms name="GeomAlgo" template="CudaVec3f" />
    
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <CudaHexahedronTLEDForceField name="FEM" computeGlobalMatrix="false" method="large" poissonRatio="0.3" youngModulus="2000" />
    
            <Node name="tetra">
                <TetrahedronSetTopologyContainer name="tetra" />
                <TetrahedronSetTopologyModifier name="Modifier" />
    
                <Hexa2TetraTopologicalMapping input="@../Container" output="@tetra" />
    
                <Node name="surface">
                    <TriangleSetTopologyContainer name="Container" />
                    <TriangleSetTopologyModifier name="Modifier" />
                    <TriangleSetGeometryAlgorithms template="CudaVec3f" name="GeomAlgo" />
    
                    <Tetra2TriangleTopologicalMapping input="@../tetra" output="@Container" />
                    <Node name="Visu">
                        <OglModel name="Visual" color="green" />
                        <IdentityMapping input="@../../../Volume" output="@Visual" />
                    </Node>
                </Node>
            </Node>
    
        </Node>   
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9 0", dt="0.001")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('RequiredPlugin', name="SofaCUDA")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
        root.addObject('DefaultAnimationLoop')
        root.addObject('DefaultVisualManagerLoop')
        root.addObject('CollisionPipeline', name="CollisionPipeline", verbose="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', name="collision response", response="PenalityContactForceField")
        root.addObject('DiscreteIntersection')

        Beam = root.addChild('Beam')
        Beam.addObject('RegularGridTopology', name="grid", n="40 10 10", min="0 6 -2", max="16 10 2")

        TetrahedronFEMForceField-GPU-Green = root.addChild('TetrahedronFEMForceField-GPU-Green')
        TetrahedronFEMForceField-GPU-Green.addObject('CentralDifferenceSolver', rayleighMass="5")
        TetrahedronFEMForceField-GPU-Green.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="CudaVec3f")
        TetrahedronFEMForceField-GPU-Green.addObject('HexahedronSetTopologyContainer', name="Container", src="@../Beam/grid")
        TetrahedronFEMForceField-GPU-Green.addObject('HexahedronSetTopologyModifier', name="Modifier")
        TetrahedronFEMForceField-GPU-Green.addObject('HexahedronSetGeometryAlgorithms', name="GeomAlgo", template="CudaVec3f")
        TetrahedronFEMForceField-GPU-Green.addObject('DiagonalMass', totalMass="50.0")
        TetrahedronFEMForceField-GPU-Green.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        TetrahedronFEMForceField-GPU-Green.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        TetrahedronFEMForceField-GPU-Green.addObject('CudaHexahedronTLEDForceField', name="FEM", computeGlobalMatrix="false", method="large", poissonRatio="0.3", youngModulus="2000")

        tetra = TetrahedronFEMForceField-GPU-Green.addChild('tetra')
        tetra.addObject('TetrahedronSetTopologyContainer', name="tetra")
        tetra.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        tetra.addObject('Hexa2TetraTopologicalMapping', input="@../Container", output="@tetra")

        surface = tetra.addChild('surface')
        surface.addObject('TriangleSetTopologyContainer', name="Container")
        surface.addObject('TriangleSetTopologyModifier', name="Modifier")
        surface.addObject('TriangleSetGeometryAlgorithms', template="CudaVec3f", name="GeomAlgo")
        surface.addObject('Tetra2TriangleTopologicalMapping', input="@../tetra", output="@Container")

        Visu = surface.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="green")
        Visu.addObject('IdentityMapping', input="@../../../Volume", output="@Visual")
    ```

