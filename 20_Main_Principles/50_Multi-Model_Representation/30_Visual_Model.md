Visualization
=============

To visualize an object in SOFA, the main component to use is the _OglModel_. Using OpenGL, this class will display the topology of its context. To display a mesh loaded with any MeshLoader, all you need to do is to connect the OglModel with the MeshLoader by writing (in case if an XML scene):

```xml
<MeshObjLoader name="myLoader" filename="" />
<OglModel name="MyOGLVisualization" src="@myLoader" />
```

You can also specify some Data like _color_ or _scale_.