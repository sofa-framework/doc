---
title: VisualStyle
---

Customize what to render on screen
----------------------------------

#### Description

**VisualStyle** component controls the *DisplayFlags* state embedded in
the **VisualParams** for the current subgraph. It merges the
**DisplayFlags** conveyed by the **VisualParams** with its own
DisplayFlags. Example Taken from
[*examples/Component/Visual/VisualStyle.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/Visual/VisualStyle.scn)



\[caption id="attachment\_1566" align="aligncenter"
width="533"\][![Resulting View from the previous XML
scene](https://www.sofa-framework.org/wp-content/uploads/2014/11/VisualStyle.jpg){.size-full
.wp-image-1566 width="533"
height="400"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/VisualStyle.jpg)
Resulting View from the previous XML scene\[/caption\]

#### XML Usage

```xml
<VisualStyle displayFlags="showBehavior showVisual" />
```

allowed values for displayFlags data are a combination of the following:

```xml
showAll, hideAll,
  showVisual, hideVisual,
   showVisualModels, hideVisualModels,
  showBehavior, hideBehavior,
    showBehaviorModels, hideBehaviorModels,
    showForceFields, hideForceFields,
    showInteractionForceFields, hideInteractionForceFields
  showMapping, hideMapping
    showMappings, hideMappings
    showMechanicalMappings, hideMechanicalMappings
  showCollision, hideCollision
     showCollisionModels, hideCollisionModels
     showBoundingCollisionModels, hideBoundingCollisionModels
showOptions hideOptions
  showNormals hideNormals
  showWireframe hideWireframe
```

#### C++ Usage

In C++, to set the visual style in a node, you have to create a
VisualStyle component, attach it to the node, create and tune a
!DisplayFlags object and set the !VisualStyle with it, as shown in the
following example:

```
  VisualStyle::SPtr visualStyle = New();
  root->addObject(visualStyle);
  VisualStyle::DisplayFlags displayFlags;
  displayFlags.setShowAll();
  visualStyle->displayFlags.setValue(displayFlags);
```

You can also use method component::visualmodel::addVisualStyle(
simulation::Node::SPtr ) to insert a VisualStyle component at the given
node and return a WriteAccessor on the display flags:

```
addVisualStyle(root)->setShowVisual().setShowBehavior().setShowMapping(false);
```
<!-- automatically generated doc START -->
__Target__: `Sofa.Component.Visual`

__namespace__: `#!c++ sofa::component::visual`

__parents__: 

- `#!c++ VisualModel`

__categories__: 

- VisualModel

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
		<td>enable</td>
		<td>
Display the object or not
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>displayFlags</td>
		<td>
Display Flags
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



## Examples

Component/Visual/VisualStyle.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 -9.81 0" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [SphereCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader SphereLoader] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedralCorotationalFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <!-- Using the VisualStyle choose your visual options! -->
        <!-- ACTIVATE: showVisual showBehavior showForceFields showInteractionForceFields showCollision showCollisionModels showWireFrame -->
        <!-- DE-ACTIVATE: hideVisual hideBehavior hideForceFields hideInteractionForceFields hideCollision hideCollisionModels hideWireFrame -->
        <VisualStyle displayFlags="showVisual showCollisionModels" />
        <DefaultAnimationLoop/>
        
        <Node name="Liver" >
            <MeshGmshLoader name="meshLoader" filename="mesh/liver.msh" />
            <TetrahedronSetTopologyContainer name="topo" src="@meshLoader" />
            <MechanicalObject name="dofs" src="@meshLoader" />
            <TetrahedronSetGeometryAlgorithms name="GeomAlgo" />
            <DiagonalMass name="computed using mass density" massDensity="1" />
            <TetrahedralCorotationalFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3" youngModulus="3000" computeGlobalMatrix="0" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64" />
            <Node name="WireframeVisu" >
                <VisualStyle displayFlags="showVisual showWireframe" />
                <MeshOBJLoader name="meshLoader_1" filename="mesh/liver-smooth.obj" handleSeams="1" />
                <OglModel name="VisualModel" src="@meshLoader_1" />
                <BarycentricMapping name="visual mapping" input="@../dofs" output="@VisualModel" />
            </Node>
            <Node name="Sphere" >
                <VisualStyle displayFlags="hideBehavior showCollision showWireframe" />
    	    <SphereLoader filename="mesh/liver.sph" />
                <MechanicalObject name="spheres" position="@[-1].position" />
                <SphereCollisionModel name="CollisionModel" listRadius="@[-2].listRadius" />
                <BarycentricMapping name="sphere mapping" input="@../dofs" output="@spheres" />
            </Node>
            
            
            <Node name="TranslatedSurface" gravity="0 -9.81 0">
    <!--             default rendering should be flat rendered and not wireframed -->
                <MeshOBJLoader name="meshLoader_0" filename="mesh/liver.obj" translation="5 0 0" handleSeams="1" />
                <OglModel src="@meshLoader_0" />
            </Node>
            
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="0 -9.81 0", dt="0.02")
        root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        root.addObject('VisualStyle', displayFlags="showVisual showCollisionModels")
        root.addObject('DefaultAnimationLoop')

        Liver = root.addChild('Liver')
        Liver.addObject('MeshGmshLoader', name="meshLoader", filename="mesh/liver.msh")
        Liver.addObject('TetrahedronSetTopologyContainer', name="topo", src="@meshLoader")
        Liver.addObject('MechanicalObject', name="dofs", src="@meshLoader")
        Liver.addObject('TetrahedronSetGeometryAlgorithms', name="GeomAlgo")
        Liver.addObject('DiagonalMass', name="computed using mass density", massDensity="1")
        Liver.addObject('TetrahedralCorotationalFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="3000", computeGlobalMatrix="0")
        Liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

        WireframeVisu = Liver.addChild('WireframeVisu')
        WireframeVisu.addObject('VisualStyle', displayFlags="showVisual showWireframe")
        WireframeVisu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/liver-smooth.obj", handleSeams="1")
        WireframeVisu.addObject('OglModel', name="VisualModel", src="@meshLoader_1")
        WireframeVisu.addObject('BarycentricMapping', name="visual mapping", input="@../dofs", output="@VisualModel")

        Sphere = Liver.addChild('Sphere')
        Sphere.addObject('VisualStyle', displayFlags="hideBehavior showCollision showWireframe")
        Sphere.addObject('SphereLoader', filename="mesh/liver.sph")
        Sphere.addObject('MechanicalObject', name="spheres", position="@[-1].position")
        Sphere.addObject('SphereCollisionModel', name="CollisionModel", listRadius="@[-2].listRadius")
        Sphere.addObject('BarycentricMapping', name="sphere mapping", input="@../dofs", output="@spheres")

        TranslatedSurface = Liver.addChild('TranslatedSurface', gravity="0 -9.81 0")
        TranslatedSurface.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/liver.obj", translation="5 0 0", handleSeams="1")
        TranslatedSurface.addObject('OglModel', src="@meshLoader_0")
    ```


<!-- automatically generated doc END -->
