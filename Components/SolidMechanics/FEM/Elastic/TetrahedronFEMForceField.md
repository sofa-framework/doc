---
title: TetrahedronFEMForceField
---

TetrahedronFEMForceField
========================

This component belongs to the category of [ForceField](https://www.sofa-framework.org/community/doc/simulation-principles/multi-model-representation/forcefield/). The page is still incomplete, but give us a bit of time to work on it!

Description of the component ...

What it is made for, what it does



Sequence diagram
----------------


Data  
----



Usage
-----

How to use it, what **required** component, case

In which case it works, in which case it doesn't

Limitations

Example
-------

This component is used as follows in XML format:

``` xml
<TetrahedronFEMForceField data_field="X" />
```

or using SofaPython3:

``` python
node.addObject('TetrahedronFEMForceField', data_field='X')
```

With a description of each data

An example scene involving a TetrahedronFEMForceField is available in [*examples/Component/SolidMechanics/FEM/TetrahedronFEMForceField.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/SolidMechanics/FEM/TetrahedronFEMForceField.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.SolidMechanics.FEM.Elastic`

__namespace__: `#!c++ sofa::component::solidmechanics::fem::elastic`

__parents__: 

- `#!c++ ForceField`
- `#!c++ BaseObject`

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
"small", "large" (by QR), "polar" or "svd" displacements
</td>
		<td>large</td>
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
		<td></td>
	</tr>
	<tr>
		<td>localStiffnessFactor</td>
		<td>
Allow specification of different stiffness per element. If there are N element and M values are specified, the youngModulus factor for element i would be localStiffnessFactor[i*M/N]
</td>
		<td></td>
	</tr>
	<tr>
		<td>updateStiffnessMatrix</td>
		<td>

</td>
		<td>0</td>
	</tr>
	<tr>
		<td>computeGlobalMatrix</td>
		<td>

</td>
		<td>0</td>
	</tr>
	<tr>
		<td>plasticMaxThreshold</td>
		<td>
Plastic Max Threshold (2-norm of the strain)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>plasticYieldThreshold</td>
		<td>
Plastic Yield Threshold (2-norm of the strain)
</td>
		<td>0.0001</td>
	</tr>
	<tr>
		<td>plasticCreep</td>
		<td>
Plastic Creep Factor * dt [0,1]. Warning this factor depends on dt.
</td>
		<td>0.9</td>
	</tr>
	<tr>
		<td>gatherPt</td>
		<td>
number of dof accumulated per threads during the gather operation (Only use in GPU version)
</td>
		<td></td>
	</tr>
	<tr>
		<td>gatherBsize</td>
		<td>
number of dof accumulated per threads during the gather operation (Only use in GPU version)
</td>
		<td></td>
	</tr>
	<tr>
		<td>computeVonMisesStress</td>
		<td>
compute and display von Mises stress: 0: no computations, 1: using corotational strain, 2: using full Green strain. Set listening=1
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>vonMisesPerElement</td>
		<td>
von Mises Stress per element
</td>
		<td></td>
	</tr>
	<tr>
		<td>vonMisesPerNode</td>
		<td>
von Mises Stress per node
</td>
		<td></td>
	</tr>
	<tr>
		<td>vonMisesStressColors</td>
		<td>
Vector of colors describing the VonMises stress
</td>
		<td></td>
	</tr>
	<tr>
		<td>updateStiffness</td>
		<td>
udpate structures (precomputed in init) using stiffness parameters in each iteration (set listening=1)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawHeterogeneousTetra</td>
		<td>
Draw Heterogeneous Tetra in different color
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showStressColorMap</td>
		<td>
Color map used to show stress values
</td>
		<td>Blue to Red</td>
	</tr>
	<tr>
		<td>showStressAlpha</td>
		<td>
Alpha for vonMises visualisation
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>showVonMisesStressPerNode</td>
		<td>
draw points showing vonMises stress interpolated in nodes
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showVonMisesStressPerNodeColorMap</td>
		<td>
draw elements showing vonMises stress interpolated in nodes
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showVonMisesStressPerElement</td>
		<td>
draw triangles showing vonMises stress interpolated in elements
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showElementGapScale</td>
		<td>
draw gap between elements (when showWireFrame is disabled) [0,1]: 0: no gap, 1: no element
</td>
		<td>0.333</td>
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
|topology|link to the tetrahedron topology container|



## Examples

Component/SolidMechanics/FEM/TetrahedronFEMForceField_Chain.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
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
    
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase name="N2" />
        <BVHNarrowPhase />
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <DefaultAnimationLoop/>
        
        <Node name="ChainFEM">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_3" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="gray" />
            </Node>
            <Node name="TorusFEM_LARGE">
                <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="2.5" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="large" />
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
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
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
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase', name="N2")
        root.addObject('BVHNarrowPhase')
        root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
        root.addObject('DefaultAnimationLoop')

        ChainFEM = root.addChild('ChainFEM')

        TorusFixed = ChainFEM.addChild('TorusFixed')
        TorusFixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
        TorusFixed.addObject('MeshTopology', src="@loader")
        TorusFixed.addObject('MechanicalObject', src="@loader")
        TorusFixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
        TorusFixed.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus2.obj", handleSeams="1")
        TorusFixed.addObject('OglModel', name="Visual", src="@meshLoader_3", color="gray")

        TorusFEM_LARGE = ChainFEM.addChild('TorusFEM_LARGE')
        TorusFEM_LARGE.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        TorusFEM_LARGE.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        TorusFEM_LARGE.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
        TorusFEM_LARGE.addObject('MeshTopology', src="@loader")
        TorusFEM_LARGE.addObject('MechanicalObject', src="@loader", dx="2.5")
        TorusFEM_LARGE.addObject('UniformMass', totalMass="5")
        TorusFEM_LARGE.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large")

        Visu = TorusFEM_LARGE.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="red", dx="2.5")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = TorusFEM_LARGE.addChild('Surf2')
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
        TorusFEM_SVD.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
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

Component/SolidMechanics/FEM/TetrahedronFEMForceField_plasticity.scn

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
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <VisualStyle displayFlags="showForceFields" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <NewProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <DefaultAnimationLoop/>
    
        <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
        <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
        <Node name="Plastic1">
            <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" rotation="90 0 0" />
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader"  />
            <UniformMass totalMass="5" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="large" plasticYieldThreshold="0.01" plasticMaxThreshold="0.025" plasticCreep="1"/>
            <PlaneForceField normal="0 1 0" d="-3" stiffness="100000" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_2" filename="mesh/torus.obj" rotation="90 0 0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" color="red"/>
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf2">
                <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" rotation="90 0 0"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader"  />
                <TriangleCollisionModel />
                <BarycentricMapping />
            </Node>
        </Node>
    
    
        <Node name="Plastic2">
            <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" rotation="90 0 0" translation="-6 0 0"/>
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader"  />
            <UniformMass totalMass="5" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="large" plasticYieldThreshold="0.005" plasticMaxThreshold="0.5" plasticCreep="1"/>
            <PlaneForceField normal="0 1 0" d="-3" stiffness="100000" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" rotation="90 0 0" translation="-6 0 0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_0" color="blue"/>
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf2">
                <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" rotation="90 0 0" translation="-6 0 0"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader"  />
                <TriangleCollisionModel />
                <BarycentricMapping />
            </Node>
        </Node>
    
    
        <Node name="Plastic3">
            <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" rotation="90 0 0" translation="-12 0 0"/>
            <MeshTopology src="@loader" />
            <MechanicalObject src="@loader"  />
            <UniformMass totalMass="5" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="large" plasticYieldThreshold="0.005" plasticMaxThreshold="0.5" plasticCreep=".1"/>
            <PlaneForceField normal="0 1 0" d="-3" stiffness="100000" />
            <Node name="Visu">
                <MeshOBJLoader name="meshLoader_3" filename="mesh/torus.obj" rotation="90 0 0" translation="-12 0 0" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_3" color="yellow"/>
                <BarycentricMapping input="@.." output="@Visual" />
            </Node>
            <Node name="Surf2">
                <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" rotation="90 0 0" translation="-12 0 0"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader"  />
                <TriangleCollisionModel />
                <BarycentricMapping />
            </Node>
        </Node>
    
        <Node name="Elastic">
        <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" rotation="90 0 0" translation="6 0 0" />
        <MeshTopology src="@loader" />
        <MechanicalObject src="@loader"  />
        <UniformMass totalMass="5" />
        <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false" method="large" />
        <PlaneForceField normal="0 1 0" d="-3" stiffness="100000" />
        <Node name="Visu">
        <MeshOBJLoader name="meshLoader_1" filename="mesh/torus.obj" rotation="90 0 0" translation="6 0 0" handleSeams="1" />
        <OglModel name="Visual" src="@meshLoader_1" color="green"/>
        <BarycentricMapping input="@.." output="@Visual" />
        </Node>
            <Node name="Surf2">
                <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" rotation="90 0 0" translation="6 0 0"/>
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader"  />
                <TriangleCollisionModel />
                <BarycentricMapping />
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
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showForceFields")
        root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
        root.addObject('BruteForceBroadPhase')
        root.addObject('BVHNarrowPhase')
        root.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
        root.addObject('DefaultAnimationLoop')
        root.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        root.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")

        Plastic1 = root.addChild('Plastic1')
        Plastic1.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", rotation="90 0 0")
        Plastic1.addObject('MeshTopology', src="@loader")
        Plastic1.addObject('MechanicalObject', src="@loader")
        Plastic1.addObject('UniformMass', totalMass="5")
        Plastic1.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large", plasticYieldThreshold="0.01", plasticMaxThreshold="0.025", plasticCreep="1")
        Plastic1.addObject('PlaneForceField', normal="0 1 0", d="-3", stiffness="100000")

        Visu = Plastic1.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus.obj", rotation="90 0 0", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_2", color="red")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = Plastic1.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj", rotation="90 0 0")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        Plastic2 = root.addChild('Plastic2')
        Plastic2.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", rotation="90 0 0", translation="-6 0 0")
        Plastic2.addObject('MeshTopology', src="@loader")
        Plastic2.addObject('MechanicalObject', src="@loader")
        Plastic2.addObject('UniformMass', totalMass="5")
        Plastic2.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large", plasticYieldThreshold="0.005", plasticMaxThreshold="0.5", plasticCreep="1")
        Plastic2.addObject('PlaneForceField', normal="0 1 0", d="-3", stiffness="100000")

        Visu = Plastic2.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", rotation="90 0 0", translation="-6 0 0", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_0", color="blue")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = Plastic2.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj", rotation="90 0 0", translation="-6 0 0")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        Plastic3 = root.addChild('Plastic3')
        Plastic3.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", rotation="90 0 0", translation="-12 0 0")
        Plastic3.addObject('MeshTopology', src="@loader")
        Plastic3.addObject('MechanicalObject', src="@loader")
        Plastic3.addObject('UniformMass', totalMass="5")
        Plastic3.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large", plasticYieldThreshold="0.005", plasticMaxThreshold="0.5", plasticCreep=".1")
        Plastic3.addObject('PlaneForceField', normal="0 1 0", d="-3", stiffness="100000")

        Visu = Plastic3.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus.obj", rotation="90 0 0", translation="-12 0 0", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="yellow")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = Plastic3.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj", rotation="90 0 0", translation="-12 0 0")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')

        Elastic = root.addChild('Elastic')
        Elastic.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh", rotation="90 0 0", translation="6 0 0")
        Elastic.addObject('MeshTopology', src="@loader")
        Elastic.addObject('MechanicalObject', src="@loader")
        Elastic.addObject('UniformMass', totalMass="5")
        Elastic.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large")
        Elastic.addObject('PlaneForceField', normal="0 1 0", d="-3", stiffness="100000")

        Visu = Elastic.addChild('Visu')
        Visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus.obj", rotation="90 0 0", translation="6 0 0", handleSeams="1")
        Visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="green")
        Visu.addObject('BarycentricMapping', input="@..", output="@Visual")

        Surf2 = Elastic.addChild('Surf2')
        Surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj", rotation="90 0 0", translation="6 0 0")
        Surf2.addObject('MeshTopology', src="@loader")
        Surf2.addObject('MechanicalObject', src="@loader")
        Surf2.addObject('TriangleCollisionModel')
        Surf2.addObject('BarycentricMapping')
    ```

Component/SolidMechanics/FEM/TetrahedronFEMForceField_assemble.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
        <DefaultAnimationLoop/>
        
        <Node name="BeamFEM_SMALL">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9"/>
            
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" />
            
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
            
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="true"
            method="small" computeVonMisesStress="2" showVonMisesStressPerElement="true"/>
            
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
        
        <Node name="BeamFEM_LARGE">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="11 0 0"/>
            
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
            
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="true"
            method="large" computeVonMisesStress="1" showVonMisesStressPerElement="true"/>
            
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 -9 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")
        root.addObject('DefaultAnimationLoop')

        BeamFEM_SMALL = root.addChild('BeamFEM_SMALL')
        BeamFEM_SMALL.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        BeamFEM_SMALL.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        BeamFEM_SMALL.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
        BeamFEM_SMALL.addObject('MechanicalObject', template="Vec3")
        BeamFEM_SMALL.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
        BeamFEM_SMALL.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        BeamFEM_SMALL.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        BeamFEM_SMALL.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
        BeamFEM_SMALL.addObject('DiagonalMass', massDensity="0.2")
        BeamFEM_SMALL.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="true", method="small", computeVonMisesStress="2", showVonMisesStressPerElement="true")
        BeamFEM_SMALL.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
        BeamFEM_SMALL.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

        BeamFEM_LARGE = root.addChild('BeamFEM_LARGE')
        BeamFEM_LARGE.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        BeamFEM_LARGE.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        BeamFEM_LARGE.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
        BeamFEM_LARGE.addObject('MechanicalObject', template="Vec3", translation="11 0 0")
        BeamFEM_LARGE.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
        BeamFEM_LARGE.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        BeamFEM_LARGE.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        BeamFEM_LARGE.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
        BeamFEM_LARGE.addObject('DiagonalMass', massDensity="0.2")
        BeamFEM_LARGE.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="true", method="large", computeVonMisesStress="1", showVonMisesStressPerElement="true")
        BeamFEM_LARGE.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
        BeamFEM_LARGE.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
    ```

Component/SolidMechanics/FEM/TetrahedronFEMForceField.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" dt="0.01" gravity="0 -9 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showForceFields" />
    
        <Node name="BeamFEM_SMALL">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9"/>
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" />
    
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false"
                                      method="small" computeVonMisesStress="2" showVonMisesStressPerElement="true"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
    
        <Node name="BeamFEM_LARGE">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="11 0 0"/>
    
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false"
                                      method="large" computeVonMisesStress="1" showVonMisesStressPerElement="true"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
        <Node name="BeamFEM_POLAR">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="22 0 0"/>
    
            <TetrahedronSetTopologyContainer name="Tetra_topo" />
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false"
                                      method="polar" computeVonMisesStress="1" showVonMisesStressPerElement="true"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
        <Node name="BeamFEM_SVD">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    
            <RegularGridTopology name="grid" min="-5 -5 0" max="5 5 40" n="5 5 20"/>
            <MechanicalObject template="Vec3" translation="33 0 0"/>
    
            <TetrahedronSetTopologyContainer name="Tetra_topo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <Hexa2TetraTopologicalMapping input="@grid" output="@Tetra_topo" />
    
            <DiagonalMass massDensity="0.2" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.4" computeGlobalMatrix="false"
                                      method="svd" computeVonMisesStress="1" showVonMisesStressPerElement="true"/>
    
            <BoxROI template="Vec3" name="box_roi" box="-6 -6 -1 50 6 0.1" drawBoxes="1" />
            <FixedProjectiveConstraint template="Vec3" indices="@box_roi.indices" />
        </Node>
    
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 -9 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('DefaultAnimationLoop')
        root.addObject('VisualStyle', displayFlags="showBehaviorModels showForceFields")

        BeamFEM_SMALL = root.addChild('BeamFEM_SMALL')
        BeamFEM_SMALL.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        BeamFEM_SMALL.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        BeamFEM_SMALL.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
        BeamFEM_SMALL.addObject('MechanicalObject', template="Vec3")
        BeamFEM_SMALL.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
        BeamFEM_SMALL.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        BeamFEM_SMALL.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        BeamFEM_SMALL.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
        BeamFEM_SMALL.addObject('DiagonalMass', massDensity="0.2")
        BeamFEM_SMALL.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="small", computeVonMisesStress="2", showVonMisesStressPerElement="true")
        BeamFEM_SMALL.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
        BeamFEM_SMALL.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

        BeamFEM_LARGE = root.addChild('BeamFEM_LARGE')
        BeamFEM_LARGE.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        BeamFEM_LARGE.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        BeamFEM_LARGE.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
        BeamFEM_LARGE.addObject('MechanicalObject', template="Vec3", translation="11 0 0")
        BeamFEM_LARGE.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
        BeamFEM_LARGE.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        BeamFEM_LARGE.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        BeamFEM_LARGE.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
        BeamFEM_LARGE.addObject('DiagonalMass', massDensity="0.2")
        BeamFEM_LARGE.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="large", computeVonMisesStress="1", showVonMisesStressPerElement="true")
        BeamFEM_LARGE.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
        BeamFEM_LARGE.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

        BeamFEM_POLAR = root.addChild('BeamFEM_POLAR')
        BeamFEM_POLAR.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        BeamFEM_POLAR.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        BeamFEM_POLAR.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
        BeamFEM_POLAR.addObject('MechanicalObject', template="Vec3", translation="22 0 0")
        BeamFEM_POLAR.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
        BeamFEM_POLAR.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        BeamFEM_POLAR.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        BeamFEM_POLAR.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
        BeamFEM_POLAR.addObject('DiagonalMass', massDensity="0.2")
        BeamFEM_POLAR.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="polar", computeVonMisesStress="1", showVonMisesStressPerElement="true")
        BeamFEM_POLAR.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
        BeamFEM_POLAR.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")

        BeamFEM_SVD = root.addChild('BeamFEM_SVD')
        BeamFEM_SVD.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        BeamFEM_SVD.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        BeamFEM_SVD.addObject('RegularGridTopology', name="grid", min="-5 -5 0", max="5 5 40", n="5 5 20")
        BeamFEM_SVD.addObject('MechanicalObject', template="Vec3", translation="33 0 0")
        BeamFEM_SVD.addObject('TetrahedronSetTopologyContainer', name="Tetra_topo")
        BeamFEM_SVD.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        BeamFEM_SVD.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        BeamFEM_SVD.addObject('Hexa2TetraTopologicalMapping', input="@grid", output="@Tetra_topo")
        BeamFEM_SVD.addObject('DiagonalMass', massDensity="0.2")
        BeamFEM_SVD.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.4", computeGlobalMatrix="false", method="svd", computeVonMisesStress="1", showVonMisesStressPerElement="true")
        BeamFEM_SVD.addObject('BoxROI', template="Vec3", name="box_roi", box="-6 -6 -1 50 6 0.1", drawBoxes="1")
        BeamFEM_SVD.addObject('FixedProjectiveConstraint', template="Vec3", indices="@box_roi.indices")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/TetrahedronFEMForceField_beam10x10x40_cpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 0" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
      
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
       
        <Node name="TetrahedronFEMForceField-CPU-red">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="20" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="Vec3"/>
    
            <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
    
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <TetrahedronFEMForceField template="Vec3" name="FEM" computeGlobalMatrix="false" method="large" poissonRatio="0.3" youngModulus="2000" />
            
            <Node name="surface">
                <TriangleSetTopologyContainer name="Container" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
                <Node name="Visu">
                    <OglModel name="Visual" color="red" />
                    <IdentityMapping input="@../../Volume" output="@Visual" />
                </Node>
            </Node>
        </Node>   
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9 0", dt="0.01")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
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

        TetrahedronFEMForceField-CPU-red = root.addChild('TetrahedronFEMForceField-CPU-red')
        TetrahedronFEMForceField-CPU-red.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        TetrahedronFEMForceField-CPU-red.addObject('CGLinearSolver', iterations="20", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
        TetrahedronFEMForceField-CPU-red.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="Vec3")
        TetrahedronFEMForceField-CPU-red.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
        TetrahedronFEMForceField-CPU-red.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        TetrahedronFEMForceField-CPU-red.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        TetrahedronFEMForceField-CPU-red.addObject('DiagonalMass', totalMass="50.0")
        TetrahedronFEMForceField-CPU-red.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        TetrahedronFEMForceField-CPU-red.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        TetrahedronFEMForceField-CPU-red.addObject('TetrahedronFEMForceField', template="Vec3", name="FEM", computeGlobalMatrix="false", method="large", poissonRatio="0.3", youngModulus="2000")

        surface = TetrahedronFEMForceField-CPU-red.addChild('surface')
        surface.addObject('TriangleSetTopologyContainer', name="Container")
        surface.addObject('TriangleSetTopologyModifier', name="Modifier")
        surface.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        surface.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")

        Visu = surface.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="red")
        Visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/TetrahedronFEMForceField_beam10x10x40_gpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 0" dt="0.01">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaCUDA"/> <!-- Needed to use components [BoxROI DiagonalMass FixedProjectiveConstraint IdentityMapping MechanicalObject TetrahedronFEMForceField TetrahedronSetGeometryAlgorithms TriangleSetGeometryAlgorithms] -->
        
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
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="20" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="CudaVec3f"/>
    
            <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" template="CudaVec3f" />
    
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <TetrahedronFEMForceField template="CudaVec3f" name="FEM" computeGlobalMatrix="false" method="large" poissonRatio="0.3" youngModulus="2000" />
            
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

        root = rootNode.addChild('root', gravity="0 -9 0", dt="0.01")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
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
        TetrahedronFEMForceField-GPU-Green.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        TetrahedronFEMForceField-GPU-Green.addObject('CGLinearSolver', iterations="20", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
        TetrahedronFEMForceField-GPU-Green.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="CudaVec3f")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo", template="CudaVec3f")
        TetrahedronFEMForceField-GPU-Green.addObject('DiagonalMass', totalMass="50.0")
        TetrahedronFEMForceField-GPU-Green.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        TetrahedronFEMForceField-GPU-Green.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronFEMForceField', template="CudaVec3f", name="FEM", computeGlobalMatrix="false", method="large", poissonRatio="0.3", youngModulus="2000")

        surface = TetrahedronFEMForceField-GPU-Green.addChild('surface')
        surface.addObject('TriangleSetTopologyContainer', name="Container")
        surface.addObject('TriangleSetTopologyModifier', name="Modifier")
        surface.addObject('TriangleSetGeometryAlgorithms', template="CudaVec3f", name="GeomAlgo")
        surface.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")

        Visu = surface.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="green")
        Visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")
    ```

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/TetrahedronFEMForceField_beam16x16x76_gpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 0" dt="0.04">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaCUDA"/> <!-- Needed to use components [BoxROI DiagonalMass FixedProjectiveConstraint IdentityMapping MechanicalObject PlaneForceField TetrahedronFEMForceField TetrahedronSetGeometryAlgorithms TriangleSetGeometryAlgorithms] -->
      
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
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="10" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="CudaVec3f"/>
    
            <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" template="CudaVec3f" />
    
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <TetrahedronFEMForceField template="CudaVec3f" name="FEM" computeGlobalMatrix="false" method="large" poissonRatio="0.3" youngModulus="1000" />
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

        root = rootNode.addChild('root', gravity="0 -9 0", dt="0.04")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
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
        TetrahedronFEMForceField-GPU-Green.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        TetrahedronFEMForceField-GPU-Green.addObject('CGLinearSolver', iterations="10", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
        TetrahedronFEMForceField-GPU-Green.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="CudaVec3f")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo", template="CudaVec3f")
        TetrahedronFEMForceField-GPU-Green.addObject('DiagonalMass', totalMass="50.0")
        TetrahedronFEMForceField-GPU-Green.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        TetrahedronFEMForceField-GPU-Green.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        TetrahedronFEMForceField-GPU-Green.addObject('TetrahedronFEMForceField', template="CudaVec3f", name="FEM", computeGlobalMatrix="false", method="large", poissonRatio="0.3", youngModulus="1000")
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

SofaCUDA/share/sofa/examples/SofaCUDA/benchmarks/TetrahedronFEMForceField_beam16x16x76_cpu.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9 0" dt="0.04">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [DiscreteIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
      
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
       
        <Node name="TetrahedronFEMForceField-CPU-red">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="10" name="linear solver" tolerance="1.0e-6" threshold="1.0e-6" />
            
            <MechanicalObject position="@../Beam/grid.position" name="Volume" template="Vec3"/>
    
            <TetrahedronSetTopologyContainer name="Container" src="@../Beam/BeamTopo"/>
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" template="Vec3" />
    
            <DiagonalMass totalMass="50.0" />
            <BoxROI name="ROI1" box="-0.1 5 -3 0.1 11 3" drawBoxes="1" />
            
            <FixedProjectiveConstraint indices="@ROI1.indices" />
            <TetrahedronFEMForceField template="Vec3" name="FEM" computeGlobalMatrix="false" method="large" poissonRatio="0.3" youngModulus="1000" />
    		<PlaneForceField normal="0 1 0" d="2" stiffness="10000"  showPlane="1" />
            
            <Node name="surface">
                <TriangleSetTopologyContainer name="Container" />
                <TriangleSetTopologyModifier name="Modifier" />
                <TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
                
                <Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" />
                <Node name="Visu">
                    <OglModel name="Visual" color="red" />
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

        root = rootNode.addChild('root', gravity="0 -9 0", dt="0.04")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
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

        TetrahedronFEMForceField-CPU-red = root.addChild('TetrahedronFEMForceField-CPU-red')
        TetrahedronFEMForceField-CPU-red.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
        TetrahedronFEMForceField-CPU-red.addObject('CGLinearSolver', iterations="10", name="linear solver", tolerance="1.0e-6", threshold="1.0e-6")
        TetrahedronFEMForceField-CPU-red.addObject('MechanicalObject', position="@../Beam/grid.position", name="Volume", template="Vec3")
        TetrahedronFEMForceField-CPU-red.addObject('TetrahedronSetTopologyContainer', name="Container", src="@../Beam/BeamTopo")
        TetrahedronFEMForceField-CPU-red.addObject('TetrahedronSetTopologyModifier', name="Modifier")
        TetrahedronFEMForceField-CPU-red.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo", template="Vec3")
        TetrahedronFEMForceField-CPU-red.addObject('DiagonalMass', totalMass="50.0")
        TetrahedronFEMForceField-CPU-red.addObject('BoxROI', name="ROI1", box="-0.1 5 -3 0.1 11 3", drawBoxes="1")
        TetrahedronFEMForceField-CPU-red.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")
        TetrahedronFEMForceField-CPU-red.addObject('TetrahedronFEMForceField', template="Vec3", name="FEM", computeGlobalMatrix="false", method="large", poissonRatio="0.3", youngModulus="1000")
        TetrahedronFEMForceField-CPU-red.addObject('PlaneForceField', normal="0 1 0", d="2", stiffness="10000", showPlane="1")

        surface = TetrahedronFEMForceField-CPU-red.addChild('surface')
        surface.addObject('TriangleSetTopologyContainer', name="Container")
        surface.addObject('TriangleSetTopologyModifier', name="Modifier")
        surface.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
        surface.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container")

        Visu = surface.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="red")
        Visu.addObject('IdentityMapping', input="@../../Volume", output="@Visual")

        Floor = root.addChild('Floor')
        Floor.addObject('RegularGridTopology', nx="4", ny="1", nz="4", xmin="-10", xmax="30", ymin="1.9", ymax="1.9", zmin="-20", zmax="20")
        Floor.addObject('MechanicalObject')

        Visu = Floor.addChild('Visu')
        Visu.addObject('OglModel', name="Visual", color="white")
        Visu.addObject('IdentityMapping', input="@..", output="@Visual")
    ```


<!-- automatically generated doc END -->
