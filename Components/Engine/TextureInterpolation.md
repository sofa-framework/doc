---
title: TextureInterpolation
---

TextureInterpolation
====================

This component belongs to the category of [Engines](https://www.sofa-framework.org/community/doc/simulation-principles/engine/). This engine creates texture coordinate in 1D according to an input state vector. Coordinate can be interpolated either from min and max value of input states (default behavior) or on a manual define scale.

Input Data
----------

-   **input\_states**: input array of state values
-   **input\_coordinates**: input array of coordinates values (not mandatory)

Output Data
----------

-   **output\_coordinates**: output array of texture coordinates

Additional Parameter
-------------------

**For manual scale :**

-   **min\_value**: minimum value of state value for interpolation
-   **max\_value**: maximum value of state value for interpolation
-   **manual\_scale**: compute texture interpolation on manually scale defined above

Examples
--------

An example scene involving the TextureInterpolation engine is available in [*examples/Component/Engine/GL/TextureInterpolation.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Engine/GL/TextureInterpolation.scn)
<!-- automatically generated doc START -->
__Target__: `Sofa.GL.Component.Engine`

__namespace__: `#!c++ sofa::gl::component::engine`

__parents__: 

- `#!c++ DataEngine`

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
		<td>input_coordinates</td>
		<td>
input array of coordinates values.
</td>
		<td></td>
	</tr>
	<tr>
		<td>scalarField</td>
		<td>
To interpolate only the first dimension of input field (useful if this component need to be templated in higher dimension).
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>min_value</td>
		<td>
minimum value of state value for interpolation.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>max_value</td>
		<td>
maximum value of state value for interpolation.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>manual_scale</td>
		<td>
compute texture interpolation on manually scale defined above.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>vertexPloted</td>
		<td>
Vertex index of values display in graph for each iteration.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>graph</td>
		<td>
Vertex state value per iteration
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>input_states</td>
		<td>
input array of state values.
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>output_coordinates</td>
		<td>
output array of texture coordinates.
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawPotentiels</td>
		<td>
Debug: view state values.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showIndicesScale</td>
		<td>
Debug : scale of state values displayed.
</td>
		<td>0.0001</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



## Examples

Component/Engine/GL/TextureInterpolation.scn

=== "XML"

    ```xml
    <Node name="Root" gravity="0 0 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Engine"/> <!-- Needed to use components [TextureInterpolation] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual showBehaviorModels showForceFields showCollision showMapping" />
        <CollisionPipeline name="DefaultCollisionPipeline" verbose="0" draw="0" depth="6" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="MecaNode" gravity="0 0 0">
            <MeshGmshLoader name="loader" tags="meca" filename="mesh/square3.msh" />
            <MechanicalObject src="@loader" template="Vec3" name="mecaObj" tags="meca" scale="10" />
            <TriangleSetTopologyContainer src="@loader" name="topo" tags="meca" />
            <Node name="ElecNode" gravity="0 0 0">
                <EulerImplicitSolver name="euler" tags="elec"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" tags="elec" />
                <MechanicalObject template="Vec1" name="ElecObj" position="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 10 10 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0&#x0A;&#x09;&#x09;&#x09;&#x09;  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0" tags="elec" />
                <!-- Components used in heat diffusion, still in work in Sophia. the potentiel
    	evolve and interpolation is computed at the same time to display the diffusion. -->
                <!--   <TriangularDiffusionForceField template="Vec1" name="ffDiffusion" tags="elec"/>
                 <MeshMatrixMass template="Vec1" name="mass" tags="elec" />   -->
            </Node>
            <Node name="visu" gravity="0 0 0">
                <TextureInterpolation template="Vec1" name="EngineInterpolation" input_states="@../ElecNode/ElecObj.position" input_coordinates="@../mecaObj.position" min_value="0.0" max_value="10.0" manual_scale="1" drawPotentiels="1" />
                <OglModel template="Vec3" name="oglPotentiel" texcoords="@EngineInterpolation.output_coordinates" texturename="textures/heatColor.bmp" handleDynamicTopology="0" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        Root = rootNode.addChild('Root', gravity="0 0 0", dt="0.02")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        Root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        Root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        Root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        Root.addObject('RequiredPlugin', name="Sofa.GL.Component.Engine")
        Root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        Root.addObject('DefaultAnimationLoop')
        Root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showForceFields showCollision showMapping")
        Root.addObject('CollisionPipeline', name="DefaultCollisionPipeline", verbose="0", draw="0", depth="6")
        Root.addObject('BruteForceBroadPhase')
        Root.addObject('BVHNarrowPhase')
        Root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        Root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        MecaNode = Root.addChild('MecaNode', gravity="0 0 0")
        MecaNode.addObject('MeshGmshLoader', name="loader", tags="meca", filename="mesh/square3.msh")
        MecaNode.addObject('MechanicalObject', src="@loader", template="Vec3", name="mecaObj", tags="meca", scale="10")
        MecaNode.addObject('TriangleSetTopologyContainer', src="@loader", name="topo", tags="meca")

        ElecNode = MecaNode.addChild('ElecNode', gravity="0 0 0")
        ElecNode.addObject('EulerImplicitSolver', name="euler", tags="elec", rayleighStiffness="0.1", rayleighMass="0.1")
        ElecNode.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9", tags="elec")
        ElecNode.addObject('MechanicalObject', template="Vec1", name="ElecObj", position="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 10 10 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 100 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				  0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0", tags="elec")

        visu = MecaNode.addChild('visu', gravity="0 0 0")
        visu.addObject('TextureInterpolation', template="Vec1", name="EngineInterpolation", input_states="@../ElecNode/ElecObj.position", input_coordinates="@../mecaObj.position", min_value="0.0", max_value="10.0", manual_scale="1", drawPotentiels="1")
        visu.addObject('OglModel', template="Vec3", name="oglPotentiel", texcoords="@EngineInterpolation.output_coordinates", texturename="textures/heatColor.bmp", handleDynamicTopology="0")
    ```


<!-- automatically generated doc END -->
