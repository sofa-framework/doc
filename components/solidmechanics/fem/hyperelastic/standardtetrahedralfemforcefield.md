<!-- generate_doc -->
# StandardTetrahedralFEMForceField

Generic Tetrahedral finite elements.


## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.SolidMechanics.FEM.HyperElastic

__namespace__: sofa::component::solidmechanics::fem::hyperelastic

__parents__:

- ForceField

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
		<td>materialName</td>
		<td>
the name of the material to be used
		</td>
		<td>ArrudaBoyce</td>
	</tr>
	<tr>
		<td>ParameterSet</td>
		<td>
The global parameters specifying the material
		</td>
		<td></td>
	</tr>
	<tr>
		<td>AnisotropyDirections</td>
		<td>
The global directions of anisotropy of the material
		</td>
		<td></td>
	</tr>
	<tr>
		<td>ParameterFile</td>
		<td>
the name of the file describing the material parameters for all tetrahedra
		</td>
		<td>myFile.param</td>
	</tr>
	<tr>
		<td>tetrahedronInfo</td>
		<td>
Internal tetrahedron data
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edgeInfo</td>
		<td>
Internal edge data
		</td>
		<td></td>
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

StandardTetrahedralFEMForceField.scn

=== "XML"

    ```xml
    ﻿<?xml version="1.0" ?>
    <Node name="root" dt="0.005" showBoundingTree="0" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.HyperElastic"/> <!-- Needed to use components [StandardTetrahedralFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [Visual3DText VisualStyle] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showForceFields showBehaviorModels" />
    
        <Node name="Corrotational">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="0 0 0"/>
    
            <MechanicalObject name="mechObj"/>
            <UniformMass/>
            <TetrahedronFEMForceField name="FEM" youngModulus="10000" poissonRatio="0.45" method="large" />
    
            <BoxROI drawBoxes="0" box="0 0 0 1 1 0.05" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices"/>
            <Visual3DText text="Corrotational" position="1 0 -0.5" scale="0.2" />
        </Node>
    
        <Node name="ArrudaBoyce">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="2 0 0"/>
    
            <MechanicalObject name="mechObj"/>
            <UniformMass/>
    
            <Node name="tetras">
                <TetrahedronSetTopologyContainer name="Container"/>
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <Hexa2TetraTopologicalMapping name="default28" input="@../" output="@Container" printLog="0" />
    
                <StandardTetrahedralFEMForceField name="FEM" ParameterSet="3448.2759 31034.483"/>
            </Node>
    
            <BoxROI drawBoxes="1" box="2 0 0 3 1 0.05" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices"/>
            <Visual3DText text="ArrudaBoyce" position="3 0 -0.5" scale="0.2" />
        </Node>
    
        <Node name="StVenantKirchhoff">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="4 0 0"/>
    
            <MechanicalObject name="mechObj"/>
            <UniformMass/>
    
            <Node name="tetras">
                <TetrahedronSetTopologyContainer name="Container"/>
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <Hexa2TetraTopologicalMapping name="default28" input="@../" output="@Container" printLog="0" />
    
                <StandardTetrahedralFEMForceField name="FEM" ParameterSet="3448.2759 31034.483" materialName="StVenantKirchhoff"/>
            </Node>
    
            <BoxROI drawBoxes="1" box="4 0 0 5 1 0.05" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices"/>
            <Visual3DText text="StVenantKirchhoff" position="5 0 -0.5" scale="0.2" />
        </Node>
    
    
        <Node name="NeoHookean">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="6 0 0"/>
    
            <MechanicalObject name="mechObj"/>
            <UniformMass/>
    
            <Node name="tetras">
                <TetrahedronSetTopologyContainer name="Container"/>
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <Hexa2TetraTopologicalMapping name="default28" input="@../" output="@Container" printLog="0" />
    
                <StandardTetrahedralFEMForceField name="FEM" ParameterSet="3448.2759 31034.483" materialName="NeoHookean"/>
            </Node>
    
            <BoxROI drawBoxes="1" box="6 0 0 7 1 0.05" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices"/>
            <Visual3DText text="NeoHookean" position="7 0 -0.5" scale="0.2" />
        </Node>
    
    
        <Node name="MooneyRivlin">
            <EulerImplicitSolver name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="8 0 0"/>
    
            <MechanicalObject name="mechObj"/>
            <UniformMass/>
    
            <Node name="tetras">
                <TetrahedronSetTopologyContainer name="Container"/>
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <Hexa2TetraTopologicalMapping name="default28" input="@../" output="@Container" printLog="0" />
    
                <StandardTetrahedralFEMForceField name="FEM" ParameterSet="5000 7000 10" materialName="MooneyRivlin"/>
            </Node>
    
            <BoxROI drawBoxes="1" box="8 0 0 9 1 0.05" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices"/>
            <Visual3DText text="MooneyRivlin" position="9 0 -0.5" scale="0.2" />
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.005", showBoundingTree="0", gravity="0 -9 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.HyperElastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showForceFields showBehaviorModels")

       corrotational = root.addChild('Corrotational')

       corrotational.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       corrotational.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       corrotational.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="0 0 0")
       corrotational.addObject('MechanicalObject', name="mechObj")
       corrotational.addObject('UniformMass', )
       corrotational.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="10000", poissonRatio="0.45", method="large")
       corrotational.addObject('BoxROI', drawBoxes="0", box="0 0 0 1 1 0.05", name="box")
       corrotational.addObject('FixedProjectiveConstraint', indices="@box.indices")
       corrotational.addObject('Visual3DText', text="Corrotational", position="1 0 -0.5", scale="0.2")

       arruda_boyce = root.addChild('ArrudaBoyce')

       arruda_boyce.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       arruda_boyce.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       arruda_boyce.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="2 0 0")
       arruda_boyce.addObject('MechanicalObject', name="mechObj")
       arruda_boyce.addObject('UniformMass', )

       tetras = ArrudaBoyce.addChild('tetras')

       tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", printLog="0")
       tetras.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483")

       arruda_boyce.addObject('BoxROI', drawBoxes="1", box="2 0 0 3 1 0.05", name="box")
       arruda_boyce.addObject('FixedProjectiveConstraint', indices="@box.indices")
       arruda_boyce.addObject('Visual3DText', text="ArrudaBoyce", position="3 0 -0.5", scale="0.2")

       st_venant_kirchhoff = root.addChild('StVenantKirchhoff')

       st_venant_kirchhoff.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       st_venant_kirchhoff.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       st_venant_kirchhoff.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="4 0 0")
       st_venant_kirchhoff.addObject('MechanicalObject', name="mechObj")
       st_venant_kirchhoff.addObject('UniformMass', )

       tetras = StVenantKirchhoff.addChild('tetras')

       tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", printLog="0")
       tetras.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483", materialName="StVenantKirchhoff")

       st_venant_kirchhoff.addObject('BoxROI', drawBoxes="1", box="4 0 0 5 1 0.05", name="box")
       st_venant_kirchhoff.addObject('FixedProjectiveConstraint', indices="@box.indices")
       st_venant_kirchhoff.addObject('Visual3DText', text="StVenantKirchhoff", position="5 0 -0.5", scale="0.2")

       neo_hookean = root.addChild('NeoHookean')

       neo_hookean.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       neo_hookean.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       neo_hookean.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="6 0 0")
       neo_hookean.addObject('MechanicalObject', name="mechObj")
       neo_hookean.addObject('UniformMass', )

       tetras = NeoHookean.addChild('tetras')

       tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", printLog="0")
       tetras.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483", materialName="NeoHookean")

       neo_hookean.addObject('BoxROI', drawBoxes="1", box="6 0 0 7 1 0.05", name="box")
       neo_hookean.addObject('FixedProjectiveConstraint', indices="@box.indices")
       neo_hookean.addObject('Visual3DText', text="NeoHookean", position="7 0 -0.5", scale="0.2")

       mooney_rivlin = root.addChild('MooneyRivlin')

       mooney_rivlin.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       mooney_rivlin.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       mooney_rivlin.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="8 0 0")
       mooney_rivlin.addObject('MechanicalObject', name="mechObj")
       mooney_rivlin.addObject('UniformMass', )

       tetras = MooneyRivlin.addChild('tetras')

       tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", printLog="0")
       tetras.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="5000 7000 10", materialName="MooneyRivlin")

       mooney_rivlin.addObject('BoxROI', drawBoxes="1", box="8 0 0 9 1 0.05", name="box")
       mooney_rivlin.addObject('FixedProjectiveConstraint', indices="@box.indices")
       mooney_rivlin.addObject('Visual3DText', text="MooneyRivlin", position="9 0 -0.5", scale="0.2")
    ```

StandardTetrahedralFEMForceFieldCPU.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.HyperElastic"/> <!-- Needed to use components [StandardTetrahedralFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="ChainFEM">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_3" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="gray" />
            </Node>
            <Node name="TorusTensorMass">
                <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" createSubelements="true"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="2.5" template="Vec3d" />
                <UniformMass totalMass="5" />
                <StandardTetrahedralFEMForceField name="FEM" ParameterSet="200 0.01" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_0" color="red" dx="2.5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="2.5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM_POLAR">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" createSubelements="true"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="5" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_2" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_2" color="blue" dx="5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM_SVD">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" createSubelements="true"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="7.5" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="svd" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_1" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_1" color="yellow" dx="7.5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="7.5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.HyperElastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       chain_fem = root.addChild('ChainFEM')

       torus_fixed = ChainFEM.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_3", color="gray")

       torus_tensor_mass = ChainFEM.addChild('TorusTensorMass')

       torus_tensor_mass.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       torus_tensor_mass.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_tensor_mass.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", createSubelements="true")
       torus_tensor_mass.addObject('MeshTopology', src="@loader")
       torus_tensor_mass.addObject('MechanicalObject', src="@loader", dx="2.5", template="Vec3d")
       torus_tensor_mass.addObject('UniformMass', totalMass="5")
       torus_tensor_mass.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="200 0.01")

       visu = TorusTensorMass.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red", dx="2.5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusTensorMass.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="2.5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_fem__polar = ChainFEM.addChild('TorusFEM_POLAR')

       torus_fem__polar.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       torus_fem__polar.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_fem__polar.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh", createSubelements="true")
       torus_fem__polar.addObject('MeshTopology', src="@loader")
       torus_fem__polar.addObject('MechanicalObject', src="@loader", dx="5")
       torus_fem__polar.addObject('UniformMass', totalMass="5")
       torus_fem__polar.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="polar")

       visu = TorusFEM_POLAR.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="blue", dx="5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM_POLAR.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_fem__svd = ChainFEM.addChild('TorusFEM_SVD')

       torus_fem__svd.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       torus_fem__svd.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_fem__svd.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", createSubelements="true")
       torus_fem__svd.addObject('MeshTopology', src="@loader")
       torus_fem__svd.addObject('MechanicalObject', src="@loader", dx="7.5")
       torus_fem__svd.addObject('UniformMass', totalMass="5")
       torus_fem__svd.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="svd")

       visu = TorusFEM_SVD.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="yellow", dx="7.5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM_SVD.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="7.5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )
    ```

StandardTetrahedralFEMForceFieldCUDA.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [NewProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaCUDA"/> <!-- Needed to use components [BarycentricMapping MechanicalObject StandardTetrahedralFEMForceField UniformMass] -->
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="ChainFEM">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_2" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="gray" />
            </Node>
            <Node name="TorusTensorMass">
                <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="2.5" template="CudaVec3f" />
                <UniformMass totalMass="5" />
                <StandardTetrahedralFEMForceField name="FEM" ParameterSet="200 0.01" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_0" color="red" dx="2.5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="2.5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM_POLAR">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="5" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_1" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_1" color="blue" dx="5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM_SVD">
                <EulerImplicitSolver name="cg_odesolver" printLog="false" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="7.5" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="svd" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_3" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_3" color="yellow" dx="7.5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="7.5" />
                    <TriangleCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="SofaCUDA")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       chain_fem = root.addChild('ChainFEM')

       torus_fixed = ChainFEM.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_2", color="gray")

       torus_tensor_mass = ChainFEM.addChild('TorusTensorMass')

       torus_tensor_mass.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       torus_tensor_mass.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_tensor_mass.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
       torus_tensor_mass.addObject('MeshTopology', src="@loader")
       torus_tensor_mass.addObject('MechanicalObject', src="@loader", dx="2.5", template="CudaVec3f")
       torus_tensor_mass.addObject('UniformMass', totalMass="5")
       torus_tensor_mass.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="200 0.01")

       visu = TorusTensorMass.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red", dx="2.5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusTensorMass.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="2.5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_fem__polar = ChainFEM.addChild('TorusFEM_POLAR')

       torus_fem__polar.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       torus_fem__polar.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_fem__polar.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
       torus_fem__polar.addObject('MeshTopology', src="@loader")
       torus_fem__polar.addObject('MechanicalObject', src="@loader", dx="5")
       torus_fem__polar.addObject('UniformMass', totalMass="5")
       torus_fem__polar.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="polar")

       visu = TorusFEM_POLAR.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="blue", dx="5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM_POLAR.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_fem__svd = ChainFEM.addChild('TorusFEM_SVD')

       torus_fem__svd.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
       torus_fem__svd.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       torus_fem__svd.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
       torus_fem__svd.addObject('MeshTopology', src="@loader")
       torus_fem__svd.addObject('MechanicalObject', src="@loader", dx="7.5")
       torus_fem__svd.addObject('UniformMass', totalMass="5")
       torus_fem__svd.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="svd")

       visu = TorusFEM_SVD.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="yellow", dx="7.5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM_SVD.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="7.5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('BarycentricMapping', )
    ```

