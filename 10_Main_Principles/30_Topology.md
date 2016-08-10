<img src="https://www.sofa-framework.org/wp-content/uploads/2016/08/redHeart-alpha.png" style="width: 30%;float:right;"/>
In computer science, most of the computations require a discretization in space of the considered simulation domain. This discretization therefore implies to define the domain as a collection of subsets. Regarding the Finite Element Method (FEM), the domain is divided into small elements. These elements and their connectedness establish the topology. The topology can be used for the computation, the visualization, the collision, etc. It is therefore a transversal aspect of the simulation.



Loading a topology
------------------

When simulating the physics of an object, its topology must therefore be loaded. To do so, many loaders are available in SOFA depending on the format of the loaded file. Among others:

* obj = MeshObjLoader
* vtk = MeshVTKLoader
* stl = MeshSTLLoader
* off = MeshVTKLoader
* gmsh = MeshGmshLoader

More information about the loaders can be found on the [associated page](https://www.sofa-framework.org/community/doc/using-sofa/basic-components/loaders/).

<div style="text-align:center;width:50%;margin: 0 25% 0;">
<img src="https://www.sofa-framework.org/wp-content/uploads/2016/08/Topology-types.png" style="width: 90%;"/>
Fig. 1 - Elements of topology available in SOFA
</div>

**_Generic loading_**

As shown in Fig. 1, these loaders will load the different elements of the topology (if any), namely: the points, edges, triangles, quads, hexas and tetras. These elements need to be saved into a "Mesh" container. This container gathers all topological elements and stores all the information in vectors. If the topology is uploaded from an .obj file, the generic xml writing is:
```xml
    <MeshObjLoader name="ObjLoader" filename="path_to_my_mesh.obj" />
    <MechanicalObject name="StateVectors" src="@ObjLoader" />
    <Mesh name="TopologyContainer" src="@ObjLoader" />
```

Example: _examples/Components/topology/MeshTopology.scn_



**_Specific loading_**

However, if the targeted topology involves tetrahedra, it is possible to load it in a more explicit way:
```xml
    <MeshObjLoader name="ObjLoader" filename="path_to_my_mesh.obj" />
    <MechanicalObject name="StateVectors" src="@ObjLoader" />
    <TetrahedronSetTopologyContainer name="TetraTopologyContainer" src="@meshLoader" />
```

Thus, the loader give the tetrahedral information to the _TopologyContainer_. From this information, the rest of the topology can be recovered, namely the triangles (faces), edges and points.

Example: _examples/Demos/liver.scn_


**_Algorithms on the geometry_**

Once loaded, one may want to perform computations based on the geometry (e.g. _computeTriangleArea()_, _isPointInTetrahedron()_). _SetGeometryAlgorithms_ classes are already available in SOFA to access geometrical algorithms. One class is implemented per topological element. It allows for instance to know whether a specific position is (or not) within a tetrahedron, or to select all tetrahedra around one point. Thus, it exists:

* PointSetGeometryAlgorithms
* EdgeSetGeometryAlgorithms
* TriangleSetGeometryAlgorithms
* QuadSetGeometryAlgorithms
* TetrahedronSetGeometryAlgorithms
* HexahedronSetGeometryAlgorithms

The resulting xml file is:

```xml
    <MeshObjLoader name="ObjLoader" filename="path_to_my_mesh.obj" />
    <MechanicalObject name="StateVectors" src="@ObjLoader" />
    <TetrahedronSetTopologyContainer name="TetraTopologyContainer" src="@meshLoader" />
    <TetrahedronSetGeometryAlgorithms name="TetraAlgorithms" template="Vec3d" />
```


**_Inheritance_**

When a topology is loaded in a node of the graph, the child nodes will automatically inherit from the parent's topology.



Topological changes
-------------------

In some simulations, the topology may evolve. Elements could be removed, added or separated: this is dynamic topological changes. Some components in SOFA do support such topological changes. In a scene with a dynamic topology, two components are compulsory:

* a _SetTopologyModifier_: defines all the basic operations (add or remove tetrahedra) and their process
* and a _SetTopologyAlgorithms_: defines more specific algorithms (e.g. _subDivideTetrahedronsWithPlane()_, _InciseAlongEdge()_, etc.)

The The xml scene looks like:

```xml
    <MeshObjLoader name="ObjLoader" filename="path_to_my_mesh.obj" />
    <MechanicalObject name="StateVectors" src="@ObjLoader" />
    <TetrahedronSetTopologyContainer name="TetraTopologyContainer" src="@meshLoader" />
    <TetrahedronSetTopologyModifier   name="Modifier" />
    <TetrahedronSetTopologyAlgorithms name="TopoAlgo"   template="Vec3d" />
    <TetrahedronSetGeometryAlgorithms name="TetraAlgorithms" template="Vec3d" />

```

Then, the nature of the topological changes can either:

* be scheduled using a specific component: the TopologicalChangeProcessor (many examples are available in the folder _examples/Components/topology/TopologicalModifiers/_)
* or be developped for a specific need, e.g. simulating of cutting when a contact is detected. A class managing the topological change can be implemented using all functions implemented in the class _SetTopologyModifier_. Functions implementing standard removal or adding of elements are available in these modifiers. The class _TopologicalChangeManager_ is a good example.



Topology & Mappings
-------------------

**_Multi-model representation_**

One of the significant strength of SOFA is to allow several representation of a same object. For instance, an object can have a coarse triangular representation for the collision, a tetrahedral representation of the mechanics and a very detailed quad surface for the visualization. However, this means that these different representations must be linked one to another. This is the role of the [mappings](https://www.sofa-framework.org/community/doc/main-principles/mapping-mechanism/). When you run a simulation with such several representations, it assumes to load the different topologies in the scene.


**_From a topology to another_**

It is possible to go from one topological representation to another. Again, the [mappings](https://www.sofa-framework.org/community/doc/main-principles/mapping-mechanism/) make it possible. If one of the simulation node is modeling hexahedra, you can compute another model based on the same geometry with tetrahedra (based on the subdivision of hexahedra). The existing _TopologicalMappings_ are:

* Hexa2TetraTopologicalMapping
* Hexa2QuadTopologicalMapping
* Quad2TriangleTopologicalMapping
* Tetra2TriangleTopologicalMapping
* Triangle2EdgeTopologicalMapping


Finally, SOFA allows to select a subset of the topology using a _SubsetTopologicalMapping_. A part of the topology in the parent node can thus be selected to be used in a child node.

All examples are available in the folder _examples/Components/topology/_.