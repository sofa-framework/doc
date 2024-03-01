Topology
========

In computer science, most of the computations require a discretization in space of the considered simulation domain. This discretization therefore implies to define the domain as a collection of subsets. Regarding the Finite Element Method (FEM), the domain is divided into small elements. These elements and their connectedness establish the topology. The topology can be used for the computation, the visualization, the collision, etc. It is therefore a transversal aspect of the simulation.
<img src="https://www.sofa-framework.org/wp-content/uploads/2016/08/redHeart-alpha.png" style="width: 40%;float:right;"/>

We consider meshes that are cellular complexes made of k-simplices (triangulations, tetrahedralisation) or k-cubes (quad or hexahedron meshes). These meshes are the most commonly used in real-time surgery simulation and can be hierarchically decomposed into k-cells, edges being 1-cells, triangles and quads being 2-cells, tetrahedron and hexahedron being 3-cells. To take advantage of this feature, the different mesh topologies are structured as a family tree where children topologies are made of their parent topology.

Loading a topology
------------------

### MeshLoaders

When simulating the physics of an object, its topology must therefore be loaded. To do so, many loaders are available in SOFA depending on the format of the loaded file. Among others:

* obj = [_MeshOBJLoader_](https://www.sofa-framework.org/community/doc/components/loaders/meshobjloader/)
* vtk = [_MeshVTKLoader_](https://www.sofa-framework.org/community/doc/components/loaders/meshvtkloader/)
* stl = [_MeshSTLLoader_](https://www.sofa-framework.org/community/doc/components/loaders/meshstlloader/)
* off = [_MeshOffLoader_](https://www.sofa-framework.org/community/doc/components/loaders/meshoffloader/)
* gmsh = [_MeshGmshLoader_](https://www.sofa-framework.org/community/doc/components/loaders/meshgmshloader)

All MeshLoaders share a common API, especially several available data:

* _**filename**_: corresponding to the path and filename of the file you are aiming at loading. This data is **required**.
* _**flipNormals**_: to flip the mesh normals
* _**triangulate**_: to divide all polygons into triangles
* _**createSubelements**_: to divide all n-D elements into their (n-1)-D boundary elements (e.g. tetrahedra to triangles)
* _**onlyAttachedPoints**_: to keep only points attached to elements of the mesh

Additional data (*translation*, *rotation* and *scale3d*) are available but it rather advised to use a [TransformEngine](https://www.sofa-framework.org/community/doc/components/engines/transformengine/) to apply a transformation to your geometry.

All MeshLoaders propose several data as output (for the most used):
* _**position**_: vector of vertices of the mesh loaded
* _**edges**_: vector of edges of the mesh loaded
* _**triangles**_: vector of triangles of the mesh loaded
* _**quads**_: vector of quads of the mesh loaded
* _**polygons**_: vector of polygons of the mesh loaded
* _**tetrahedra**_: vector of tetrahedra of the mesh loaded
* _**hexahedra**_: vector of  hexahedra of the mesh loaded
* _**normals**_: vector of the normals per vertex



<div style="text-align:center;width:90%;margin: 0 5% 0;">
<img src="https://www.sofa-framework.org/wp-content/uploads/2016/08/Topology-types.png" style="width: 80%;"/>
Fig. 1 - Elements of topology available in SOFA
</div>

### TopologyContainers

As shown in Fig. 1, these loaders will load the different elements of the topology (if any), namely: the points, edges, triangles, quads, hexas and tetras. These elements need to be saved into a _TopologyContainer_. This container stores all the topological information in vectors. It indicates how vertices are connected to each other by edges, triangles or any type of mesh element and implements all the related functions (e.g. _getTetrahedraAroundVertex()_, _getTriangleIndex()_). There is one container per topological element:

* _PointSetTopologyContainer_
* _EdgeSetTopologyContainer_
* _TriangleSetTopologyContainer_
* _QuadSetTopologyContainer_
* _TetrahedronSetTopologyContainer_
* _HexahedronSetTopologyContainer_


If the topology is uploaded from an .obj file with a topology involving tetrahedra, it would be written as:
```xml
<MeshObjLoader name="ObjLoader" filename="path_to_my_mesh.obj" />
<MechanicalObject name="StateVectors" src="@ObjLoader" />
<TetrahedronSetTopologyContainer name="TetraTopologyContainer" src="@meshLoader" />
```

Thus, the loader give the tetrahedral information to the _TopologyContainer_. From this information, the rest of the topology can be recovered, namely the triangles (faces), edges and points.

Example: _examples/Demos/liver.scn_


**_Algorithms on the geometry_**

Once loaded, one may want to perform computations based on the geometry. _SetGeometryAlgorithms_ classes are already available in SOFA to access geometrical algorithms (e.g. _computeTriangleArea()_, _isPointInTetrahedron()_). The _SetGeometryAlgorithms_ include all geometrical functions specific to the topological elements and also implement the visualization options for this topology (e.g. showing point indices, drawing triangles). One class is implemented per topological element. Thus, it exists:

* _PointSetGeometryAlgorithms_
* _EdgeSetGeometryAlgorithms_
* _TriangleSetGeometryAlgorithms_
* _QuadSetGeometryAlgorithms_
* _TetrahedronSetGeometryAlgorithms_
* _HexahedronSetGeometryAlgorithms_


In the XML scene, we have:

```xml
<MeshObjLoader name="ObjLoader" filename="path_to_my_mesh.obj" />
<MechanicalObject name="StateVectors" src="@ObjLoader" />
<TetrahedronSetTopologyContainer name="TetraTopologyContainer" src="@meshLoader" />
<TetrahedronSetGeometryAlgorithms name="TetraAlgorithms" template="Vec3d" drawTetrahedra="1"/>
```


**_Inheritance_**

When a topology is loaded in a node of the graph, the child nodes will automatically inherit from the parent's topology.


Topological changes
-------------------

In some simulations, the topology may evolve. Elements could be removed, added or separated: this is dynamic topological changes. Some components in SOFA do support such topological changes. In a scene with a dynamic topology, two components are compulsory:

* _SetTopologyModifier_: defines all the basic operations (add or remove tetrahedra) and their process
* _SetTopologyAlgorithms_: defines more specific algorithms (e.g. _subDivideTetrahedronsWithPlane()_, _InciseAlongEdge()_, etc.)

The XLM scene looks like:

```xml
<MeshObjLoader name="ObjLoader" filename="path_to_my_mesh.obj" />
<MechanicalObject name="StateVectors" src="@ObjLoader" />
<TetrahedronSetTopologyContainer name="TetraTopologyContainer" src="@meshLoader" />
<TetrahedronSetTopologyModifier   name="Modifier" />
<TetrahedronSetTopologyAlgorithms name="TopoAlgo"   template="Vec3d" />
<TetrahedronSetGeometryAlgorithms name="TetraAlgorithms" template="Vec3d" />
```

Then, the nature of the topological changes can either:

* be scheduled using a specific component: the TopologicalChangeProcessor (many examples are available in the folder _examples/Component/Topology/Container/Dynamic/_)
* or be developed for a specific need, e.g. simulating of cutting when a contact is detected. A class managing the topological change can be implemented using all functions implemented in the class _SetTopologyModifier_. Functions implementing standard removal or adding of elements are available in these modifiers. The class _TopologicalChangeManager_ is a good example.



Topological mappings
--------------------

**_Multi-model representation_**

One of the significant strength of SOFA is to allow several representation of a same object. For instance, an object can have a coarse triangular representation for the collision, a tetrahedral representation of the mechanics and a very detailed quad surface for the visualization. However, this means that these different representations must be linked one to another. This is the role of the [mappings](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/mappings/). When you run a simulation with such several representations, it assumes to load the different topologies in the scene.


**_From a topology to another_**

It is possible to define a mesh topology from another mesh topology using the same degrees of freedom. Again, the [mappings](https://www.sofa-framework.org/community/doc/main-principles/multi-model-representation/mappings/) make it possible. Mappings can be used either to go from one topology to a lower one in the topological hierarchy (from tetrahedra to triangles), or to split elements (quads into triangles). As usual mappings, forces applied on the slave topology are propagated onto the master one. Both topologies will therefore be assigned to the same _MechanicalObject_. The existing _TopologicalMappings_ are:

* _Hexa2TetraTopologicalMapping_
* _Hexa2QuadTopologicalMapping_
* _Quad2TriangleTopologicalMapping_
* _Tetra2TriangleTopologicalMapping_
* _Triangle2EdgeTopologicalMapping_


**_Topological subset_**

Finally, SOFA allows to select a subset of the topology using a _SubsetTopologicalMapping_. A part of the topology in the parent node can thus be selected to be used in a child node.




All examples are available in the folder _examples/Component/Topology/Mapping/_.
