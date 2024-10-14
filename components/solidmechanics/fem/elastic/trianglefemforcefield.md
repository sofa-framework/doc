<!-- generate_doc -->
# TriangleFEMForceField

Triangular finite elements for static topology.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.FEM.Elastic

__namespace__: sofa::component::solidmechanics::fem::elastic

__parents__:

- BaseLinearElasticityFEMForceField

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
FEM Poisson Ratio in Hooke's law [0,0.5[
		</td>
		<td>0.45</td>
	</tr>
	<tr>
		<td>youngModulus</td>
		<td>
FEM Young's Modulus in Hooke's law
		</td>
		<td>5000</td>
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

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

TriangleFEMForceField.scn

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
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 0 1", dt="0.05")

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
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField", name="collision response")
       root.addObject('DiscreteIntersection', )
       root.addObject('DefaultAnimationLoop', )

       m1 = root.addChild('M1')

       m1.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       m1.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       m1.addObject('MechanicalObject', )
       m1.addObject('UniformMass', vertexMass="0.1")
       m1.addObject('RegularGridTopology', nx="3", ny="3", nz="1", xmin="10", xmax="19", ymin="0", ymax="9", zmin="4", zmax="5")
       m1.addObject('FixedProjectiveConstraint', indices="0 8")
       m1.addObject('TriangleFEMForceField', name="FEM1", youngModulus="5000", poissonRatio="0.3", method="large")
       m1.addObject('TriangleCollisionModel', )

       visu = M1.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="green")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")

       m2 = root.addChild('M2')

       m2.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       m2.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       m2.addObject('MechanicalObject', )
       m2.addObject('UniformMass', vertexMass="0.1")
       m2.addObject('RegularGridTopology', nx="4", ny="4", nz="1", xmin="20", xmax="29", ymin="0", ymax="9", zmin="8", zmax="9")
       m2.addObject('FixedProjectiveConstraint', indices="0 15")
       m2.addObject('TriangleFEMForceField', name="FEM2", youngModulus="5000", poissonRatio="0.3", method="large")
       m2.addObject('TriangleCollisionModel', )

       visu = M2.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="blue")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")

       m3 = root.addChild('M3')

       m3.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       m3.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       m3.addObject('MechanicalObject', )
       m3.addObject('UniformMass', vertexMass="0.1")
       m3.addObject('RegularGridTopology', nx="10", ny="10", nz="1", xmin="30", xmax="39", ymin="0", ymax="9", zmin="12", zmax="13")
       m3.addObject('FixedProjectiveConstraint', indices="0 9 99")
       m3.addObject('TriangleFEMForceField', name="FEM3", youngModulus="50000", poissonRatio="0.3", method="large")
       m3.addObject('TriangleCollisionModel', )

       visu = M3.addChild('Visu')

       visu.addObject('OglModel', name="Visual", color="yellow")
       visu.addObject('IdentityMapping', input="@..", output="@Visual")
    ```

TriangleFEMForceField_compare.scn

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
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 10 0")

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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showVisual")
       root.addObject('RegularGridTopology', name="grid", n="40 1 40", min="0 0 0", max="10 0 10")

       triangular_fem_force_field = root.addChild('TriangularFEMForceField')

       triangular_fem_force_field.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       triangular_fem_force_field.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       triangular_fem_force_field.addObject('QuadSetTopologyContainer', name="Quad_topo", src="@../grid")
       triangular_fem_force_field.addObject('QuadSetTopologyModifier', name="Modifier")
       triangular_fem_force_field.addObject('QuadSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
       triangular_fem_force_field.addObject('MechanicalObject', name="TriangularFEMForceField_dof")
       triangular_fem_force_field.addObject('DiagonalMass', totalMass="1.0")
       triangular_fem_force_field.addObject('FixedProjectiveConstraint', indices="0 39")

       t = TriangularFEMForceField.addChild('T')

       t.addObject('TriangleSetTopologyContainer', name="Triangle_topo")
       t.addObject('TriangleSetTopologyModifier', name="Modifier")
       t.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
       t.addObject('Quad2TriangleTopologicalMapping', name="TriangularFEMForceField_mapTopo", input="@../Quad_topo", output="@Triangle_topo")
       t.addObject('TriangularFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", method="large")

       visu = T.addChild('Visu')

       visu.addObject('OglModel', name="TriangularFEMForceField_visu", color="red")
       visu.addObject('IdentityMapping', name="TriangularFEMForceField_mapping", input="@../..", output="@.")

       triangular_fem_force_field_optim = root.addChild('TriangularFEMForceFieldOptim')

       triangular_fem_force_field_optim.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       triangular_fem_force_field_optim.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       triangular_fem_force_field_optim.addObject('QuadSetTopologyContainer', name="Quad_topo", src="@../grid")
       triangular_fem_force_field_optim.addObject('QuadSetTopologyModifier', name="Modifier")
       triangular_fem_force_field_optim.addObject('QuadSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
       triangular_fem_force_field_optim.addObject('MechanicalObject', name="TriangularFEMForceFieldOptim_dof")
       triangular_fem_force_field_optim.addObject('DiagonalMass', totalMass="1.0")
       triangular_fem_force_field_optim.addObject('FixedProjectiveConstraint', indices="0 39")

       t = TriangularFEMForceFieldOptim.addChild('T')

       t.addObject('TriangleSetTopologyContainer', name="Triangle_topo")
       t.addObject('TriangleSetTopologyModifier', name="Modifier")
       t.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
       t.addObject('Quad2TriangleTopologicalMapping', name="TriangularFEMForceFieldOptim_mapTopo", input="@../Quad_topo", output="@Triangle_topo")
       t.addObject('TriangularFEMForceFieldOptim', name="FEM", youngModulus="1000", poissonRatio="0.3", method="large")

       visu = T.addChild('Visu')

       visu.addObject('OglModel', name="TriangularFEMForceFieldOptim_visu", color="blue")
       visu.addObject('IdentityMapping', name="TriangularFEMForceFieldOptim_mapping", input="@../..", output="@.")

       triangle_fem_force_field = root.addChild('TriangleFEMForceField')

       triangle_fem_force_field.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       triangle_fem_force_field.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       triangle_fem_force_field.addObject('QuadSetTopologyContainer', name="Quad_topo", src="@../grid")
       triangle_fem_force_field.addObject('QuadSetTopologyModifier', name="Modifier")
       triangle_fem_force_field.addObject('QuadSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
       triangle_fem_force_field.addObject('MechanicalObject', name="TriangleFEMForceField_dof")
       triangle_fem_force_field.addObject('DiagonalMass', totalMass="1.0")
       triangle_fem_force_field.addObject('FixedProjectiveConstraint', indices="0 39")

       t = TriangleFEMForceField.addChild('T')

       t.addObject('TriangleSetTopologyContainer', name="Triangle_topo")
       t.addObject('TriangleSetTopologyModifier', name="Modifier")
       t.addObject('TriangleSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
       t.addObject('Quad2TriangleTopologicalMapping', name="TriangleFEMForceField_mapTopo", input="@../Quad_topo", output="@Triangle_topo")
       t.addObject('TriangleFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", method="large")

       visu = T.addChild('Visu')

       visu.addObject('OglModel', name="TriangleFEMForceField_visu", color="green")
       visu.addObject('IdentityMapping', name="TriangleFEMForceField_mapping", input="@../..", output="@.")
    ```

