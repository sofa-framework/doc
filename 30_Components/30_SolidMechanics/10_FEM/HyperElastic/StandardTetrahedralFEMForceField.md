# StandardTetrahedralFEMForceField

Generic Tetrahedral finite elements
Supports GPU-side computations using CUDA


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.SolidMechanics.FEM.HyperElastic`

__namespace__: `#!c++ sofa::component::solidmechanics::fem::hyperelastic`

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

Component/SolidMechanics/FEM/StandardTetrahedralFEMForceField.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.005", showBoundingTree="0", gravity="0 -9 0")
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
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showForceFields showBehaviorModels")

        Corrotational = root.addChild('Corrotational')
        Corrotational.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        Corrotational.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Corrotational.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="0 0 0")
        Corrotational.addObject('MechanicalObject', name="mechObj")
        Corrotational.addObject('UniformMass')
        Corrotational.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="10000", poissonRatio="0.45", method="large")
        Corrotational.addObject('BoxROI', drawBoxes="0", box="0 0 0 1 1 0.05", name="box")
        Corrotational.addObject('FixedProjectiveConstraint', indices="@box.indices")
        Corrotational.addObject('Visual3DText', text="Corrotational", position="1 0 -0.5", scale="0.2")

        ArrudaBoyce = root.addChild('ArrudaBoyce')
        ArrudaBoyce.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        ArrudaBoyce.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        ArrudaBoyce.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="2 0 0")
        ArrudaBoyce.addObject('MechanicalObject', name="mechObj")
        ArrudaBoyce.addObject('UniformMass')

        tetras = ArrudaBoyce.addChild('tetras')
        tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
        tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", printLog="0")
        tetras.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483")
        ArrudaBoyce.addObject('BoxROI', drawBoxes="1", box="2 0 0 3 1 0.05", name="box")
        ArrudaBoyce.addObject('FixedProjectiveConstraint', indices="@box.indices")
        ArrudaBoyce.addObject('Visual3DText', text="ArrudaBoyce", position="3 0 -0.5", scale="0.2")

        StVenantKirchhoff = root.addChild('StVenantKirchhoff')
        StVenantKirchhoff.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        StVenantKirchhoff.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        StVenantKirchhoff.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="4 0 0")
        StVenantKirchhoff.addObject('MechanicalObject', name="mechObj")
        StVenantKirchhoff.addObject('UniformMass')

        tetras = StVenantKirchhoff.addChild('tetras')
        tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
        tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", printLog="0")
        tetras.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483", materialName="StVenantKirchhoff")
        StVenantKirchhoff.addObject('BoxROI', drawBoxes="1", box="4 0 0 5 1 0.05", name="box")
        StVenantKirchhoff.addObject('FixedProjectiveConstraint', indices="@box.indices")
        StVenantKirchhoff.addObject('Visual3DText', text="StVenantKirchhoff", position="5 0 -0.5", scale="0.2")

        NeoHookean = root.addChild('NeoHookean')
        NeoHookean.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        NeoHookean.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        NeoHookean.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="6 0 0")
        NeoHookean.addObject('MechanicalObject', name="mechObj")
        NeoHookean.addObject('UniformMass')

        tetras = NeoHookean.addChild('tetras')
        tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
        tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", printLog="0")
        tetras.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483", materialName="NeoHookean")
        NeoHookean.addObject('BoxROI', drawBoxes="1", box="6 0 0 7 1 0.05", name="box")
        NeoHookean.addObject('FixedProjectiveConstraint', indices="@box.indices")
        NeoHookean.addObject('Visual3DText', text="NeoHookean", position="7 0 -0.5", scale="0.2")

        MooneyRivlin = root.addChild('MooneyRivlin')
        MooneyRivlin.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        MooneyRivlin.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        MooneyRivlin.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="8 0 0")
        MooneyRivlin.addObject('MechanicalObject', name="mechObj")
        MooneyRivlin.addObject('UniformMass')

        tetras = MooneyRivlin.addChild('tetras')
        tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
        tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", printLog="0")
        tetras.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="5000 7000 10", materialName="MooneyRivlin")
        MooneyRivlin.addObject('BoxROI', drawBoxes="1", box="8 0 0 9 1 0.05", name="box")
        MooneyRivlin.addObject('FixedProjectiveConstraint', indices="@box.indices")
        MooneyRivlin.addObject('Visual3DText', text="MooneyRivlin", position="9 0 -0.5", scale="0.2")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/StandardTetrahedralFEMForceFieldCPU.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01")
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
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        ChainFEM = root.addChild('ChainFEM')

        TorusFixed = ChainFEM.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader")
        TorusFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_3", color="gray")

        TorusTensorMass = ChainFEM.addChild('TorusTensorMass')
        TorusTensorMass.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        TorusTensorMass.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusTensorMass.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", createSubelements="true")
        TorusTensorMass.addObject('MeshTopology', src="@loader")
        TorusTensorMass.addObject('MechanicalObject', src="@loader", dx="2.5", template="Vec3d")
        TorusTensorMass.addObject('UniformMass', totalMass="5")
        TorusTensorMass.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="200 0.01")

        Visu = TorusTensorMass.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red", dx="2.5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusTensorMass.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="2.5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFEM_POLAR = ChainFEM.addChild('TorusFEM_POLAR')
        TorusFEM_POLAR.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusFEM_POLAR.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFEM_POLAR.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh", createSubelements="true")
        TorusFEM_POLAR.addObject('MeshTopology', src="@loader")
        TorusFEM_POLAR.addObject('MechanicalObject', src="@loader", dx="5")
        TorusFEM_POLAR.addObject('UniformMass', totalMass="5")
        TorusFEM_POLAR.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="polar")

        Visu = TorusFEM_POLAR.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="blue", dx="5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM_POLAR.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFEM_SVD = ChainFEM.addChild('TorusFEM_SVD')
        TorusFEM_SVD.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusFEM_SVD.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFEM_SVD.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", createSubelements="true")
        TorusFEM_SVD.addObject('MeshTopology', src="@loader")
        TorusFEM_SVD.addObject('MechanicalObject', src="@loader", dx="7.5")
        TorusFEM_SVD.addObject('UniformMass', totalMass="5")
        TorusFEM_SVD.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="svd")

        Visu = TorusFEM_SVD.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="yellow", dx="7.5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM_SVD.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="7.5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/StandardTetrahedralFEMForceFieldCUDA.scn

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
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01")
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
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        ChainFEM = root.addChild('ChainFEM')

        TorusFixed = ChainFEM.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader")
        TorusFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_2", color="gray")

        TorusTensorMass = ChainFEM.addChild('TorusTensorMass')
        TorusTensorMass.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        TorusTensorMass.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusTensorMass.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
        TorusTensorMass.addObject('MeshTopology', src="@loader")
        TorusTensorMass.addObject('MechanicalObject', src="@loader", dx="2.5", template="CudaVec3f")
        TorusTensorMass.addObject('UniformMass', totalMass="5")
        TorusTensorMass.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="200 0.01")

        Visu = TorusTensorMass.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red", dx="2.5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusTensorMass.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="2.5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFEM_POLAR = ChainFEM.addChild('TorusFEM_POLAR')
        TorusFEM_POLAR.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusFEM_POLAR.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFEM_POLAR.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
        TorusFEM_POLAR.addObject('MeshTopology', src="@loader")
        TorusFEM_POLAR.addObject('MechanicalObject', src="@loader", dx="5")
        TorusFEM_POLAR.addObject('UniformMass', totalMass="5")
        TorusFEM_POLAR.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="polar")

        Visu = TorusFEM_POLAR.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus2.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="blue", dx="5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM_POLAR.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        TorusFEM_SVD = ChainFEM.addChild('TorusFEM_SVD')
        TorusFEM_SVD.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false")
        TorusFEM_SVD.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFEM_SVD.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
        TorusFEM_SVD.addObject('MeshTopology', src="@loader")
        TorusFEM_SVD.addObject('MechanicalObject', src="@loader", dx="7.5")
        TorusFEM_SVD.addObject('UniformMass', totalMass="5")
        TorusFEM_SVD.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="svd")

        Visu = TorusFEM_SVD.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="yellow", dx="7.5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM_SVD.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader", dx="7.5")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')
    ```

