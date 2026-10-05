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
|slaves|Sub-objects used internally by this object|BaseComponent|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseComponent|
|mechanicalStates|List of mechanical states to which this component is associated|BaseMechanicalState|
|mstate|MechanicalState used by this component|MechanicalState&lt;Vec3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

StandardTetrahedralFEMForceField.scn

=== "XML"

    ```xml
    ﻿<?xml version="1.0" ?>
    <Node name="root" dt="0.005" showBoundingTree="0" gravity="0 -9 0">
        <RequiredPlugin pluginName="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin pluginName="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin pluginName="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin pluginName="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin pluginName="Sofa.Component.IntegrationScheme.Backward"/> <!-- Needed to use components [EulerImplicitIntegrationScheme] -->
        <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin pluginName="Sofa.Component.SolidMechanics.FEM.HyperElastic"/> <!-- Needed to use components [StandardTetrahedralFEMForceField] -->
        <RequiredPlugin pluginName="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin pluginName="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin pluginName="Sofa.Component.Visual"/> <!-- Needed to use components [Visual3DText VisualStyle] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showForceFields showBehaviorModels" />
    
        <Node name="Corrotational">
            <EulerImplicitIntegrationScheme name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="0 0 0"/>
    
            <MechanicalObject name="mechObj"/>
            <UniformMass totalMass="1.0"/>
            <TetrahedronFEMForceField name="FEM" youngModulus="10000" poissonRatio="0.45" method="large" />
    
            <BoxROI drawBoxes="0" box="0 0 0 1 1 0.05" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices"/>
            <Visual3DText text="Corrotational" position="1 0 -0.5" scale="0.2" />
        </Node>
    
        <Node name="ArrudaBoyce">
            <EulerImplicitIntegrationScheme name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="2 0 0"/>
    
            <MechanicalObject name="mechObj"/>
            <UniformMass totalMass="1.0"/>
    
            <Node name="tetras">
                <TetrahedronSetTopologyContainer name="Container"/>
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <Hexa2TetraTopologicalMapping name="default28" input="@../" output="@Container" swapping="true"/>
    
                <StandardTetrahedralFEMForceField name="FEM" ParameterSet="3448.2759 31034.483"/>
            </Node>
    
            <BoxROI drawBoxes="1" box="2 0 0 3 1 0.05" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices"/>
            <Visual3DText text="ArrudaBoyce" position="3 0 -0.5" scale="0.2" />
        </Node>
    
        <Node name="StVenantKirchhoff">
            <EulerImplicitIntegrationScheme name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="4 0 0"/>
    
            <MechanicalObject name="mechObj"/>
            <UniformMass totalMass="1.0"/>
    
            <Node name="tetras">
                <TetrahedronSetTopologyContainer name="Container"/>
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <Hexa2TetraTopologicalMapping name="default28" input="@../" output="@Container" swapping="true"/>
    
                <StandardTetrahedralFEMForceField name="FEM" ParameterSet="3448.2759 31034.483" materialName="StVenantKirchhoff"/>
            </Node>
    
            <BoxROI drawBoxes="1" box="4 0 0 5 1 0.05" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices"/>
            <Visual3DText text="StVenantKirchhoff" position="5 0 -0.5" scale="0.2" />
        </Node>
    
    
        <Node name="NeoHookean">
            <EulerImplicitIntegrationScheme name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="6 0 0"/>
    
            <MechanicalObject name="mechObj"/>
            <UniformMass totalMass="1.0"/>
    
            <Node name="tetras">
                <TetrahedronSetTopologyContainer name="Container"/>
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <Hexa2TetraTopologicalMapping name="default28" input="@../" output="@Container" swapping="true"/>
    
                <StandardTetrahedralFEMForceField name="FEM" ParameterSet="3448.2759 31034.483" materialName="NeoHookean"/>
            </Node>
    
            <BoxROI drawBoxes="1" box="6 0 0 7 1 0.05" name="box"/>
            <FixedProjectiveConstraint indices="@box.indices"/>
            <Visual3DText text="NeoHookean" position="7 0 -0.5" scale="0.2" />
        </Node>
    
    
        <Node name="MooneyRivlin">
            <EulerImplicitIntegrationScheme name="cg_odesolver" printLog="false" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="hexaGrid" min="0 0 0" max="1 1 2.7" n="3 3 8" p0="8 0 0"/>
    
            <MechanicalObject name="mechObj"/>
            <UniformMass totalMass="1.0"/>
    
            <Node name="tetras">
                <TetrahedronSetTopologyContainer name="Container"/>
                <TetrahedronSetTopologyModifier name="Modifier" />
                <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                <Hexa2TetraTopologicalMapping name="default28" input="@../" output="@Container" swapping="true"/>
    
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

       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.IntegrationScheme.Backward")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.SolidMechanics.FEM.HyperElastic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', pluginName="Sofa.Component.Visual")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showForceFields showBehaviorModels")

       corrotational = root.addChild('Corrotational')

       corrotational.addObject('EulerImplicitIntegrationScheme', name="cg_odesolver", printLog="false")
       corrotational.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       corrotational.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="0 0 0")
       corrotational.addObject('MechanicalObject', name="mechObj")
       corrotational.addObject('UniformMass', totalMass="1.0")
       corrotational.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="10000", poissonRatio="0.45", method="large")
       corrotational.addObject('BoxROI', drawBoxes="0", box="0 0 0 1 1 0.05", name="box")
       corrotational.addObject('FixedProjectiveConstraint', indices="@box.indices")
       corrotational.addObject('Visual3DText', text="Corrotational", position="1 0 -0.5", scale="0.2")

       arruda_boyce = root.addChild('ArrudaBoyce')

       arruda_boyce.addObject('EulerImplicitIntegrationScheme', name="cg_odesolver", printLog="false")
       arruda_boyce.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       arruda_boyce.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="2 0 0")
       arruda_boyce.addObject('MechanicalObject', name="mechObj")
       arruda_boyce.addObject('UniformMass', totalMass="1.0")

       tetras = ArrudaBoyce.addChild('tetras')

       tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", swapping="true")
       tetras.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483")

       arruda_boyce.addObject('BoxROI', drawBoxes="1", box="2 0 0 3 1 0.05", name="box")
       arruda_boyce.addObject('FixedProjectiveConstraint', indices="@box.indices")
       arruda_boyce.addObject('Visual3DText', text="ArrudaBoyce", position="3 0 -0.5", scale="0.2")

       st_venant_kirchhoff = root.addChild('StVenantKirchhoff')

       st_venant_kirchhoff.addObject('EulerImplicitIntegrationScheme', name="cg_odesolver", printLog="false")
       st_venant_kirchhoff.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       st_venant_kirchhoff.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="4 0 0")
       st_venant_kirchhoff.addObject('MechanicalObject', name="mechObj")
       st_venant_kirchhoff.addObject('UniformMass', totalMass="1.0")

       tetras = StVenantKirchhoff.addChild('tetras')

       tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", swapping="true")
       tetras.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483", materialName="StVenantKirchhoff")

       st_venant_kirchhoff.addObject('BoxROI', drawBoxes="1", box="4 0 0 5 1 0.05", name="box")
       st_venant_kirchhoff.addObject('FixedProjectiveConstraint', indices="@box.indices")
       st_venant_kirchhoff.addObject('Visual3DText', text="StVenantKirchhoff", position="5 0 -0.5", scale="0.2")

       neo_hookean = root.addChild('NeoHookean')

       neo_hookean.addObject('EulerImplicitIntegrationScheme', name="cg_odesolver", printLog="false")
       neo_hookean.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       neo_hookean.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="6 0 0")
       neo_hookean.addObject('MechanicalObject', name="mechObj")
       neo_hookean.addObject('UniformMass', totalMass="1.0")

       tetras = NeoHookean.addChild('tetras')

       tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", swapping="true")
       tetras.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="3448.2759 31034.483", materialName="NeoHookean")

       neo_hookean.addObject('BoxROI', drawBoxes="1", box="6 0 0 7 1 0.05", name="box")
       neo_hookean.addObject('FixedProjectiveConstraint', indices="@box.indices")
       neo_hookean.addObject('Visual3DText', text="NeoHookean", position="7 0 -0.5", scale="0.2")

       mooney_rivlin = root.addChild('MooneyRivlin')

       mooney_rivlin.addObject('EulerImplicitIntegrationScheme', name="cg_odesolver", printLog="false")
       mooney_rivlin.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       mooney_rivlin.addObject('RegularGridTopology', name="hexaGrid", min="0 0 0", max="1 1 2.7", n="3 3 8", p0="8 0 0")
       mooney_rivlin.addObject('MechanicalObject', name="mechObj")
       mooney_rivlin.addObject('UniformMass', totalMass="1.0")

       tetras = MooneyRivlin.addChild('tetras')

       tetras.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetras.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetras.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetras.addObject('Hexa2TetraTopologicalMapping', name="default28", input="@../", output="@Container", swapping="true")
       tetras.addObject('StandardTetrahedralFEMForceField', name="FEM", ParameterSet="5000 7000 10", materialName="MooneyRivlin")

       mooney_rivlin.addObject('BoxROI', drawBoxes="1", box="8 0 0 9 1 0.05", name="box")
       mooney_rivlin.addObject('FixedProjectiveConstraint', indices="@box.indices")
       mooney_rivlin.addObject('Visual3DText', text="MooneyRivlin", position="9 0 -0.5", scale="0.2")
    ```

