The SofaCarving plugin provides basic functionality for removing
tetrahedra from a mesh. This can be used to simulate tissue destruction
in medical simulations. []()

Loading the Plugin
---------------------------------------------------

To load the SofaCarving plugin, select **SOFA-PLUGIN\_SOFACARVING** in
your Cmake configuration. Reconfigure, generate and build. []()

CarvingManager
-----------------------------------------------

The plugin provides one component, the CarvingManager. When added to a
scene, it automatically looks for a collision model that will act as
the tool from removing tetrahedra, and a surface model that will have
its tetrahedra removed by the tool. If your scene has many possible
collision or surface models, you can specify the ones that the
CarvingManager will use by giving those components the tags
**CarvingTool** and **CarvingSurface**. See the example scene
**SofaCarving/SimpleCarving.scn**.
