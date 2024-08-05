# CudaTetrahedronTLEDForceField

GPU TLED tetrahedron forcefield using CUDA


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

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/CudaTetrahedronTLEDForceField_beam16x16x76_gpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 0" dt="0.0001">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Forward"/> <!-- Needed to use components [CentralDifferenceSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaCUDA"/> <!-- Needed to use components [BoxROI CudaTetrahedronTLEDForceField DiagonalMass FixedProjectiveConstraint IdentityMapping MechanicalObject PlaneForceField TetrahedronSetGeometryAlgorithms TriangleSetGeometryAlgorithms] -->
      
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
    	
        <DefaultAnimationLoop />
        <DefaultVisualManagerLoop />
        <CollisionPipeline name="CollisionPipeline" verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="collision response" response="PenalityContactForceField" />
        <DiscreteIntersection/>
        
        <Node name="Beam">
            <RegularGridTopology name="grid" n="76 16 16" min="0 6 -2" max="19 10 2" />
            <TetrahedronSetTopologyContainer name="BeamTopo" />
            <TetrahedronSetTopologyModifier name="Modifier" />
    
            <Hexa2TetraTopologicalMapping input="@grid" output="@BeamTopo" />
        </Node>
       
        <Node name="TetrahedronFEMForceField-GPU-Green">
            <CentralDifferenceSolver rayleighMass="5"/>
            
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="CudaVec3f"/>
    
            <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" template="CudaVec3f" />
    
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <CudaTetrahedronTLEDForceField name="FEM" computeGlobalMatrix="false" method="large" poissonRatio="0.3" youngModulus="1000" />
    		<PlaneForceField normal="0 1 0" d="2" stiffness="10000"  showPlane="1" />
            
            <Node name="surface">
                <TriangleSetTopologyContainer name="Container" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="CudaVec3f" name="GeomAlgo" />
                
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
                <Node name="Visu">
                    <OglModel name="Visual" color="green" />
                    <IdentityMapping input="@../../Volume" output="@Visual" />
                </Node>
            </Node>
        </Node>
        
        <Node name="Floor">
    		<RegularGridTopology
    			nx="4" ny="1" nz="4"
    			xmin="-10" xmax="30"
    			ymin="1.9" ymax="1.9"
    			zmin="-20" zmax="20" />
    		<MechanicalObject />
    		<Node name="Visu">
    			<OglModel name="Visual" color="white"/>
    			<IdentityMapping input="@.." output="@Visual"/>
    		</Node>
    	</Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9 0", dt="0.0001")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Forward")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
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
        Beam.addObject('RegularGridTopology', name="grid", n="76 16 16", min="0 6 -2", max="19 10 2")
        Beam.addObject('TetrahedronSetTopologyContainer', name="BeamTopo")
        Beam.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        Beam.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@BeamTopo")

        TetrahedronFEMForceField-GPU-Green = root.addChild('TetrahedronFEMForceField-GPU-Green')
        TetrahedronFEMForceField-GPU-Green.addObject('CentralDifferenceSolver', rayleighMass="5")
        TetrahedronFEMForceField-GPU-Green.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="CudaVec3f")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo", template="CudaVec3f")
        TetrahedronFEMForceField-GPU-Green.addObject('DiagonalMass', totalMass="50.0")
        TetrahedronFEMForceField-GPU-Green.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        TetrahedronFEMForceField-GPU-Green.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        TetrahedronFEMForceField-GPU-Green.addObject('CudaTetrahedronTLEDForceField', name="FEM", computeGlobalMatrix="false", method="large", poissonRatio="0.3", youngModulus="1000")
        TetrahedronFEMForceField-GPU-Green.addObject('PlaneForceField', normal="0 1 0", d="2", stiffness="10000", showPlane="1")

        surface = TetrahedronFEMForceField-GPU-Green.addChild('surface')
        surface.addObject('TriangleSetTopologyContainer', name="Container")
        surface.addObject('TriangleSetTopologyModifier', name="Modifier")
        surface.addObject('TriangleSetGeometryAlgorithms', template="CudaVec3f", name="GeomAlgo")
        surface.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")

        Visu = surface.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="green")
        Visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")

        Floor = root.addChild('Floor')
        Floor.addObject('RegularGridTopology', nx="4", ny="1", nz="4", xmin="-10", xmax="30", ymin="1.9", ymax="1.9", zmin="-20", zmax="20")
        Floor.addObject('MechanicalObject')

        Visu = Floor.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="white")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/CudaTetrahedronTLEDForceField_beam10x10x40_gpu.scn

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
            <RegularGridTopology name="grid" n="40 10 10" min="0 6 -2" max="16 10 2" />
            <TetrahedronSetTopologyContainer name="BeamTopo" />
            <TetrahedronSetTopologyModifier name="Modifier" />
    
            <Hexa2TetraTopologicalMapping input="@grid" output="@BeamTopo" />
        </Node>
        
        
        <Node name="TetrahedronFEMForceField-GPU-Green">
            <CentralDifferenceSolver rayleighMass="5"/>
            
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="CudaVec3f"/>
    
            <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" template="CudaVec3f" />
    
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <CudaTetrahedronTLEDForceField name="FEM" computeGlobalMatrix="false" method="large" poissonRatio="0.3" youngModulus="2000" />
            
            <Node name="surface">
                <TriangleSetTopologyContainer name="Container" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="CudaVec3f" name="GeomAlgo" />
                
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
                <Node name="Visu">
                    <OglModel name="Visual" color="green" />
                    <IdentityMapping input="@../../Volume" output="@Visual" />
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
        Beam.addObject('TetrahedronSetTopologyContainer', name="BeamTopo")
        Beam.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        Beam.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@BeamTopo")

        TetrahedronFEMForceField-GPU-Green = root.addChild('TetrahedronFEMForceField-GPU-Green')
        TetrahedronFEMForceField-GPU-Green.addObject('CentralDifferenceSolver', rayleighMass="5")
        TetrahedronFEMForceField-GPU-Green.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="CudaVec3f")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo", template="CudaVec3f")
        TetrahedronFEMForceField-GPU-Green.addObject('DiagonalMass', totalMass="50.0")
        TetrahedronFEMForceField-GPU-Green.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        TetrahedronFEMForceField-GPU-Green.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        TetrahedronFEMForceField-GPU-Green.addObject('CudaTetrahedronTLEDForceField', name="FEM", computeGlobalMatrix="false", method="large", poissonRatio="0.3", youngModulus="2000")

        surface = TetrahedronFEMForceField-GPU-Green.addChild('surface')
        surface.addObject('TriangleSetTopologyContainer', name="Container")
        surface.addObject('TriangleSetTopologyModifier', name="Modifier")
        surface.addObject('TriangleSetGeometryAlgorithms', template="CudaVec3f", name="GeomAlgo")
        surface.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")

        Visu = surface.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="green")
        Visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

