In computer science, most of the computations require a discretization in space of the considered simulation domain. This discretization therefore implies to define the domain as a collection of subsets. Regarding the Finite Element Method (FEM), the domain is divided into small elements. These elements and their connectedness establish the topology. The topology can be used for the computation, the visualization, the collision, etc. It is therefore a transversal aspect of the simulation.

Loading a topology
__________________

When simulating the physics of an object, its topology must therefore be loaded. To do so, many loaders are available in SOFA depending on the format of the loaded file.



loaders : generic / specific
container : generic / specific
inherited



Topological changes
___________________

not every component in SOFA does support topological changes
functions are available to handle topological changes in the code



Last remarks
____________

topo different for different representation --> mapping



<TriangleSetTopologyContainer  name="Container" src="@Loader"/>
<TriangleSetTopologyModifier   name="Modifier" />
<TriangleSetTopologyAlgorithms name="TopoAlgo"   template="Vec3d" />
<TriangleSetGeometryAlgorithms name="GeomAlgo"   template="Vec3d" />


<TetrahedronSetTopologyContainer  name="Container" src="@Loader"/>
<TetrahedronSetTopologyModifier   name="Modifier" />
<TetrahedronSetTopologyAlgorithms name="TopoAlgo"   template="Vec3d" />
<TetrahedronSetGeometryAlgorithms name="GeomAlgo"   template="Vec3d" />