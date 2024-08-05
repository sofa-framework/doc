---
title: MeshGmshLoader
---

MeshGmshLoader
==============

This component belongs to the category of the [MeshLoaders](https://www.sofa-framework.org/community/doc/simulation-principles/topology/#meshloaders).

The MeshGmshLoader loads a mesh from a file under the format \*.msh. Such a mesh file can be either surface or volumetric meshes. The \*.msh meshes can be generated using software like [Gmsh](https://gmsh.info/).
To be noted, an interesting [project couples SOFA and Gmsh in python](https://github.com/sescaida/gmsh-sofa_tutorial) for applications such as parametric design or design optimization.

Usage
-----

**No pre-requisite** in your scene to use a MeshLoader.


Example
-------

This component is used as follows in XML format:

``` xml
<MeshGmshLoader name="GmshLoader" filename="mesh/square3.msh" createSubelements="true" flipNormals="0" />
```

or using SofaPython3:

``` python
node.addObject('MeshGmshLoader', name="ObjLoader", filename="mesh/square3.msh", createSubelements="true", flipNormals="0")
```

An example scene involving a MeshGmshLoader is available in [*examples/Component/IO/Mesh/MeshGmshLoader.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Component/IO/Mesh/MeshGmshLoader.scn)<!-- automatically generated doc START -->
__Target__: `Sofa.Component.IO.Mesh`

__namespace__: `#!c++ sofa::component::io::mesh`

__parents__: 

- `#!c++ MeshLoader`

__categories__: 

- Loader

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
		<td>filename</td>
		<td>
Filename of the object
</td>
		<td></td>
	</tr>
	<tr>
		<td>flipNormals</td>
		<td>
Flip Normals
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>triangulate</td>
		<td>
Divide all polygons into triangles
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>createSubelements</td>
		<td>
Divide all n-D elements into their (n-1)-D boundary elements (e.g. tetrahedra to triangles)
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>onlyAttachedPoints</td>
		<td>
Only keep points attached to elements of the mesh
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>translation</td>
		<td>
Translation of the DOFs
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>rotation</td>
		<td>
Rotation of the DOFs
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>scale3d</td>
		<td>
Scale of the DOFs in 3 dimensions
</td>
		<td>1 1 1</td>
	</tr>
	<tr>
		<td>transformation</td>
		<td>
4x4 Homogeneous matrix to transform the DOFs (when present replace any)
</td>
		<td>[1 0 0 0,0 1 0 0,0 0 1 0,0 0 0 1]</td>
	</tr>
	<tr>
		<td colspan="3">Groups</td>
	</tr>
	<tr>
		<td>edgesGroups</td>
		<td>
Groups of Edges
</td>
		<td></td>
	</tr>
	<tr>
		<td>trianglesGroups</td>
		<td>
Groups of Triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>quadsGroups</td>
		<td>
Groups of Quads
</td>
		<td></td>
	</tr>
	<tr>
		<td>polygonsGroups</td>
		<td>
Groups of Polygons
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedraGroups</td>
		<td>
Groups of Tetrahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedraGroups</td>
		<td>
Groups of Hexahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>pentahedraGroups</td>
		<td>
Groups of Pentahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>pyramidsGroups</td>
		<td>
Groups of Pyramids
</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Vectors</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Vertices of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>polylines</td>
		<td>
Polylines of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
Edges of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
Triangles of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
Quads of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>polygons</td>
		<td>
Polygons of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderEdgePositions</td>
		<td>
High order edge points of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderTrianglePositions</td>
		<td>
High order triangle points of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderQuadPositions</td>
		<td>
High order quad points of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
Tetrahedra of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
Hexahedra of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>pentahedra</td>
		<td>
Pentahedra of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderTetrahedronPositions</td>
		<td>
High order tetrahedron points of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>highOrderHexahedronPositions</td>
		<td>
High order hexahedron points of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>pyramids</td>
		<td>
Pyramids of the mesh loaded
</td>
		<td></td>
	</tr>
	<tr>
		<td>normals</td>
		<td>
Normals of the mesh loaded
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

Component/IO/Mesh/MeshGmshLoader.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <!-- For more details see: https://wiki.sofa-framework.org/tdev/wiki/Notes/NewLoaderArchitecture -->
    <Node name="Root" gravity="0 -9.81 0" dt="0.05">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField TriangularFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [TriangularBendingSprings] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual showBehaviorModels showForceFields showCollision showMapping" />
        <CollisionPipeline name="DefaultCollisionPipeline" verbose="0" draw="0" depth="6" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="gmsh file">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="GmshLoader" filename="mesh/square3.msh" createSubelements="true" flipNormals="0" />
            <MechanicalObject name="dofs" scale="10" src="@GmshLoader" />
            <TriangleSetTopologyContainer name="topo" src="@GmshLoader" />
            <TriangleSetTopologyModifier name="modif" />
            <TriangleSetGeometryAlgorithms name="triGeo" drawEdges="1" />
            <DiagonalMass massDensity="0.15" />
            <FixedProjectiveConstraint indices="0 1" />
            <TriangularFEMForceField name="FEM" youngModulus="100" poissonRatio="0.3" method="large" />
            <TriangularBendingSprings name="FEM-Bend" stiffness="300" damping="1.0" />
            <TriangleCollisionModel />
            <Node>
                <OglModel src="@../GmshLoader" name="VisualModel" color="blue" />
                <IdentityMapping name="mapping" input="@.." output="@VisualModel" />
            </Node>
        </Node>
        <Node name="gmsh file v4">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            <MeshGmshLoader name="GmshLoaderv4" filename="mesh/msh4_cube.msh" createSubelements="true" flipNormals="0" />
            <MechanicalObject name="dofs" scale="10" src="@GmshLoaderv4" />
            <TetrahedronSetTopologyContainer name="topo" src="@GmshLoaderv4" />
            <TetrahedronSetTopologyModifier name="modif" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="tetraGeo" />
            <DiagonalMass massDensity="0.2" />
            <FixedProjectiveConstraint indices="0 1" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" method="large" />
            <TriangleCollisionModel />
            <Node>
                <OglModel src="@../GmshLoaderv4" name="VisualModel" color="blue" />
                <IdentityMapping name="mapping" input="@.." output="@VisualModel" />
            </Node>
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        Root = rootNode.addChild('Root', gravity="0 -9.81 0", dt="0.05")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        Root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        Root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        Root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        Root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        Root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
        Root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        Root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        Root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
        Root.addObject('DefaultAnimationLoop')
        Root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showForceFields showCollision showMapping")
        Root.addObject('CollisionPipeline', name="DefaultCollisionPipeline", verbose="0", draw="0", depth="6")
        Root.addObject('BruteForceBroadPhase')
        Root.addObject('BVHNarrowPhase')
        Root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
        Root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

        gmsh file = Root.addChild('gmsh file')
        gmsh file.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        gmsh file.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        gmsh file.addObject('MeshGmshLoader', name="GmshLoader", filename="mesh/square3.msh", createSubelements="true", flipNormals="0")
        gmsh file.addObject('MechanicalObject', name="dofs", scale="10", src="@GmshLoader")
        gmsh file.addObject('TriangleSetTopologyContainer', name="topo", src="@GmshLoader")
        gmsh file.addObject('TriangleSetTopologyModifier', name="modif")
        gmsh file.addObject('TriangleSetGeometryAlgorithms', name="triGeo", drawEdges="1")
        gmsh file.addObject('DiagonalMass', massDensity="0.15")
        gmsh file.addObject('FixedProjectiveConstraint', indices="0 1")
        gmsh file.addObject('TriangularFEMForceField', name="FEM", youngModulus="100", poissonRatio="0.3", method="large")
        gmsh file.addObject('TriangularBendingSprings', name="FEM-Bend", stiffness="300", damping="1.0")
        gmsh file.addObject('TriangleCollisionModel')

        gmsh file = gmsh file.addChild('gmsh file')
        gmsh file.addObject('OglModel', src="@../GmshLoader", name="VisualModel", color="blue")
        gmsh file.addObject('IdentityMapping', name="mapping", input="@..", output="@VisualModel")

        gmsh file v4 = Root.addChild('gmsh file v4')
        gmsh file v4.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
        gmsh file v4.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        gmsh file v4.addObject('MeshGmshLoader', name="GmshLoaderv4", filename="mesh/msh4_cube.msh", createSubelements="true", flipNormals="0")
        gmsh file v4.addObject('MechanicalObject', name="dofs", scale="10", src="@GmshLoaderv4")
        gmsh file v4.addObject('TetrahedronSetTopologyContainer', name="topo", src="@GmshLoaderv4")
        gmsh file v4.addObject('TetrahedronSetTopologyModifier', name="modif")
        gmsh file v4.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="tetraGeo")
        gmsh file v4.addObject('DiagonalMass', massDensity="0.2")
        gmsh file v4.addObject('FixedProjectiveConstraint', indices="0 1")
        gmsh file v4.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", method="large")
        gmsh file v4.addObject('TriangleCollisionModel')

        gmsh file v4 = gmsh file v4.addChild('gmsh file v4')
        gmsh file v4.addObject('OglModel', src="@../GmshLoaderv4", name="VisualModel", color="blue")
        gmsh file v4.addObject('IdentityMapping', name="mapping", input="@..", output="@VisualModel")
    ```


<!-- automatically generated doc END -->
