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
		<td>isCompliance</td>
		<td>
Consider the component as a compliance, else as a stiffness
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

