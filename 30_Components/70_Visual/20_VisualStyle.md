Customize what to render on screen
----------------------------------

#### Description

**VisualStyle** component controls the *DisplayFlags* state embedded in
the **VisualParams** for the current subgraph. It merges the
**DisplayFlags** conveyed by the **VisualParams** with its own
DisplayFlags. Example Taken from
*examples/Components/visualmodel/VisualStyle.scn*



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
