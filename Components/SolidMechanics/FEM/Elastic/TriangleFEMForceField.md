# TriangleFEMForceField

Triangular finite elements for static topology


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.FEM.Elastic`

__namespace__: `#!c++ sofa::component::solidmechanics::fem::elastic`

__parents__: 

- `#!c++ ForceField`

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
		<td>initialPoints</td>
		<td>
Initial Position
</td>
		<td></td>
	</tr>
	<tr>
		<td>method</td>
		<td>
large: large displacements, small: small displacements
</td>
		<td>large</td>
	</tr>
	<tr>
		<td>poissonRatio</td>
		<td>
Poisson ratio in Hooke's law
</td>
		<td>0.3</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
Young modulus in Hooke's law
</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>thickness</td>
		<td>
Thickness of the elements
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>planeStrain</td>
		<td>
Plane strain or plane stress assumption
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
|topology|link to the topology container|



## Examples

Benchmark/Accuracy/TriangleFEMForceField_compare.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.01" gravity="0 10 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangleFEMForceField TriangularFEMForceField TriangularFEMForceFieldOptim] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [QuadSetGeometryAlgorithms QuadSetTopologyContainer QuadSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Quad2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <DefaultAnimationLoop/>
    
    
        <VisualStyle displayFlags="showBehaviorModels showVisual" />
        
        <RegularGridTopology name="grid" n="40 1 40" min="0 0 0" max="10 0 10" />
        
        <Node name="TriangularFEMForceField">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <QuadSetTopologyContainer name="Quad_topo" src="@../grid" />
            <QuadSetTopologyModifier name="Modifier" />
            <QuadSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
            
            <MechanicalObject name="TriangularFEMForceField_dof" />
            <DiagonalMass totalMass="1.0" />
            <FixedProjectiveConstraint indices="0 39" />
    
            <Node name="T">
                <TriangleSetTopologyContainer name="Triangle_topo" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
    
                <Quad2TriangleTopologicalMapping name="TriangularFEMForceField_mapTopo" input="@../Quad_topo" output="@Triangle_topo" />
                <TriangularFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" method="large" />
                
                <Node name="Visu">
                    <OglModel name="TriangularFEMForceField_visu" color="red" />
                    <IdentityMapping name="TriangularFEMForceField_mapping" input="@../.." output="@." />
                </Node>
            </Node>
            
        </Node>
        
        
        <Node name="TriangularFEMForceFieldOptim">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <QuadSetTopologyContainer name="Quad_topo" src="@../grid" />
            <QuadSetTopologyModifier name="Modifier" />
            <QuadSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
            
            <MechanicalObject name="TriangularFEMForceFieldOptim_dof" />
            <DiagonalMass totalMass="1.0" />
            <FixedProjectiveConstraint indices="0 39" />
    
            <Node name="T">
                <TriangleSetTopologyContainer name="Triangle_topo" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
    
                <Quad2TriangleTopologicalMapping name="TriangularFEMForceFieldOptim_mapTopo" input="@../Quad_topo" output="@Triangle_topo" />
                <TriangularFEMForceFieldOptim name="FEM" youngModulus="1000" poissonRatio="0.3" method="large" />
                
                <Node name="Visu">
                    <OglModel name="TriangularFEMForceFieldOptim_visu" color="blue" />
                    <IdentityMapping name="TriangularFEMForceFieldOptim_mapping" input="@../.." output="@." />
                </Node>
            </Node>
            
        </Node>
        
        
        <Node name="TriangleFEMForceField">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <QuadSetTopologyContainer name="Quad_topo" src="@../grid" />
            <QuadSetTopologyModifier name="Modifier" />
            <QuadSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
            
            <MechanicalObject name="TriangleFEMForceField_dof" />
            <DiagonalMass totalMass="1.0" />
            <FixedProjectiveConstraint indices="0 39" />
    
            <Node name="T">
                <TriangleSetTopologyContainer name="Triangle_topo" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
    
                <Quad2TriangleTopologicalMapping name="TriangleFEMForceField_mapTopo" input="@../Quad_topo" output="@Triangle_topo" />
                <TriangleFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" method="large" />
                
                <Node name="Visu">
                    <OglModel name="TriangleFEMForceField_visu" color="green" />
                    <IdentityMapping name="TriangleFEMForceField_mapping" input="@../.." output="@." />
                </Node>
            </Node>
            
        </Node>
        
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 10 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
        root.addObject('RegularGridTopology', name="grid", n="40 1 40", min="0 0 0", max="10 0 10")

        TriangularFEMForceField = root.addChild('TriangularFEMForceField')
        TriangularFEMForceField.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        TriangularFEMForceField.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TriangularFEMForceField.addObject('QuadSetTopologyContainer', name="Quad_topo", src="@../grid")
        TriangularFEMForceField.addObject('QuadSetTopologyModifier', name="Modifier")
        TriangularFEMForceField.addObject('QuadSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        TriangularFEMForceField.addObject('MechanicalObject', name="TriangularFEMForceField_dof")
        TriangularFEMForceField.addObject('DiagonalMass', totalMass="1.0")
        TriangularFEMForceField.addObject('FixedProjectiveConstraint', indices="0 39")

        T = TriangularFEMForceField.addChild('T')
        T.addObject('TriangleSetTopologyContainer', name="Triangle_topo")
        T.addObject('TriangleSetTopologyModifier', name="Modifier")
        T.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        T.addObject('Quad2TriangleTopologicalMapping', name="TriangularFEMForceField_mapTopo", input="@../Quad_topo", output="@Triangle_topo")
        T.addObject('TriangularFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", method="large")

        Visu = T.addChild('Visu')
        Visu.addObject('OglModel', name="TriangularFEMForceField_visu", color="red")
        Visu.addObject('IdentityMapping', name="TriangularFEMForceField_mapping", input="@../..", output="@.")

        TriangularFEMForceFieldOptim = root.addChild('TriangularFEMForceFieldOptim')
        TriangularFEMForceFieldOptim.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        TriangularFEMForceFieldOptim.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TriangularFEMForceFieldOptim.addObject('QuadSetTopologyContainer', name="Quad_topo", src="@../grid")
        TriangularFEMForceFieldOptim.addObject('QuadSetTopologyModifier', name="Modifier")
        TriangularFEMForceFieldOptim.addObject('QuadSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        TriangularFEMForceFieldOptim.addObject('MechanicalObject', name="TriangularFEMForceFieldOptim_dof")
        TriangularFEMForceFieldOptim.addObject('DiagonalMass', totalMass="1.0")
        TriangularFEMForceFieldOptim.addObject('FixedProjectiveConstraint', indices="0 39")

        T = TriangularFEMForceFieldOptim.addChild('T')
        T.addObject('TriangleSetTopologyContainer', name="Triangle_topo")
        T.addObject('TriangleSetTopologyModifier', name="Modifier")
        T.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        T.addObject('Quad2TriangleTopologicalMapping', name="TriangularFEMForceFieldOptim_mapTopo", input="@../Quad_topo", output="@Triangle_topo")
        T.addObject('TriangularFEMForceFieldOptim', name="FEM", youngModulus="1000", poissonRatio="0.3", method="large")

        Visu = T.addChild('Visu')
        Visu.addObject('OglModel', name="TriangularFEMForceFieldOptim_visu", color="blue")
        Visu.addObject('IdentityMapping', name="TriangularFEMForceFieldOptim_mapping", input="@../..", output="@.")

        TriangleFEMForceField = root.addChild('TriangleFEMForceField')
        TriangleFEMForceField.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        TriangleFEMForceField.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TriangleFEMForceField.addObject('QuadSetTopologyContainer', name="Quad_topo", src="@../grid")
        TriangleFEMForceField.addObject('QuadSetTopologyModifier', name="Modifier")
        TriangleFEMForceField.addObject('QuadSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        TriangleFEMForceField.addObject('MechanicalObject', name="TriangleFEMForceField_dof")
        TriangleFEMForceField.addObject('DiagonalMass', totalMass="1.0")
        TriangleFEMForceField.addObject('FixedProjectiveConstraint', indices="0 39")

        T = TriangleFEMForceField.addChild('T')
        T.addObject('TriangleSetTopologyContainer', name="Triangle_topo")
        T.addObject('TriangleSetTopologyModifier', name="Modifier")
        T.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        T.addObject('Quad2TriangleTopologicalMapping', name="TriangleFEMForceField_mapTopo", input="@../Quad_topo", output="@Triangle_topo")
        T.addObject('TriangleFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", method="large")

        Visu = T.addChild('Visu')
        Visu.addObject('OglModel', name="TriangleFEMForceField_visu", color="green")
        Visu.addObject('IdentityMapping', name="TriangleFEMForceField_mapping", input="@../..", output="@.")
    ```

Component/SolidMechanics/FEM/TriangleFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <!-- Mechanical MassSpring Group Basic Example -->
    <Node name="root" gravity="0 0 1" dt="0.05">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TriangleFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showBehaviorModels showForceFields showCollisionModels showMappings showVisual" />
        <CollisionPipeline verbose="0" name="CollisionPipeline" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" name="collision response" />
        <DiscreteIntersection />
        <DefaultAnimationLoop/>
        
        <Node name="M1">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject />
            <UniformMass vertexMass="0.1" />
            <RegularGridTopology nx="3" ny="3" nz="1" xmin="10" xmax="19" ymin="0" ymax="9" zmin="4" zmax="5" />
            <FixedProjectiveConstraint indices="0 8" />
            <TriangleFEMForceField name="FEM1" youngModulus="5000" poissonRatio="0.3" method="large" />
            <TriangleCollisionModel />
            <Node name="Visu">
                <OglModel name="Visual" color="green" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="M2">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject />
            <UniformMass vertexMass="0.1" />
            <RegularGridTopology nx="4" ny="4" nz="1" xmin="20" xmax="29" ymin="0" ymax="9" zmin="8" zmax="9" />
            <FixedProjectiveConstraint indices="0 15" />
            <TriangleFEMForceField name="FEM2" youngModulus="5000" poissonRatio="0.3" method="large" />
            <TriangleCollisionModel />
            <Node name="Visu">
                <OglModel name="Visual" color="blue" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
        <Node name="M3">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MechanicalObject />
            <UniformMass vertexMass="0.1" />
            <RegularGridTopology nx="10" ny="10" nz="1" xmin="30" xmax="39" ymin="0" ymax="9" zmin="12" zmax="13" />
            <FixedProjectiveConstraint indices="0 9 99" />
            <TriangleFEMForceField name="FEM3" youngModulus="50000" poissonRatio="0.3" method="large" />
            <TriangleCollisionModel />
            <Node name="Visu">
                <OglModel name="Visual" color="yellow" />
                <IdentityMapping input="@.." output="@Visual" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 0 1", dt="0.05")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields showCollisionModels showMappings showVisual")
        root.addObject('CollisionPipeline', verbose="0", name="CollisionPipeline")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
        root.addObject('DiscreteIntersection')
        root.addObject('DefaultAnimationLoop')

        M1 = root.addChild('M1')
        M1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        M1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        M1.addObject('MechanicalObject')
        M1.addObject('UniformMass', vertexMass="0.1")
        M1.addObject('RegularGridTopology', nx="3", ny="3", nz="1", xmin="10", xmax="19", ymin="0", ymax="9", zmin="4", zmax="5")
        M1.addObject('FixedProjectiveConstraint', indices="0 8")
        M1.addObject('TriangleFEMForceField', name="FEM1", youngModulus="5000", poissonRatio="0.3", method="large")
        M1.addObject('TriangleCollisionModel')

        Visu = M1.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="green")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")

        M2 = root.addChild('M2')
        M2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        M2.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        M2.addObject('MechanicalObject')
        M2.addObject('UniformMass', vertexMass="0.1")
        M2.addObject('RegularGridTopology', nx="4", ny="4", nz="1", xmin="20", xmax="29", ymin="0", ymax="9", zmin="8", zmax="9")
        M2.addObject('FixedProjectiveConstraint', indices="0 15")
        M2.addObject('TriangleFEMForceField', name="FEM2", youngModulus="5000", poissonRatio="0.3", method="large")
        M2.addObject('TriangleCollisionModel')

        Visu = M2.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="blue")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")

        M3 = root.addChild('M3')
        M3.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        M3.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        M3.addObject('MechanicalObject')
        M3.addObject('UniformMass', vertexMass="0.1")
        M3.addObject('RegularGridTopology', nx="10", ny="10", nz="1", xmin="30", xmax="39", ymin="0", ymax="9", zmin="12", zmax="13")
        M3.addObject('FixedProjectiveConstraint', indices="0 9 99")
        M3.addObject('TriangleFEMForceField', name="FEM3", youngModulus="50000", poissonRatio="0.3", method="large")
        M3.addObject('TriangleCollisionModel')

        Visu = M3.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="yellow")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

