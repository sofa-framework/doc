<!-- generate_doc -->
# VolumeMapping

Mapping each tetrahedron in a topology to a scalar value representing its volume


## Vec3d,Vec1d

Templates:

- Vec3d,Vec1d

__Target__: Sofa.Component.Mapping.NonLinear

__namespace__: sofa::component::mapping::nonlinear

__parents__:

- Mapping

### Data

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
		<td>mapForces</td>
		<td>
Are forces mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapConstraints</td>
		<td>
Are constraints mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMasses</td>
		<td>
Are masses mapped ?
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>mapMatrices</td>
		<td>
Are matrix explicit mapped?
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>applyRestPosition</td>
		<td>
set to true to apply this mapping to restPosition at init
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>geometricStiffness</td>
		<td>
Method used to compute the geometric stiffness:
-None: geometric stiffness is not computed
-Exact: the exact geometric stiffness is computed
-Stabilized: the exact geometric stiffness is approximated in order to improve stability
		</td>
		<td>Stabilized</td>
	</tr>

</tbody>
</table>

### Links


| Name | Description | Destination type name |
| ---- | ----------- | --------------------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|BaseContext|
|slaves|Sub-objects used internally by this object|BaseObject|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|BaseObject|
|input|Input object to map|State&lt;Vec3d&gt;|
|output|Output object to map|State&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|

## Examples 

VolumeMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" gravity="0 -9.81 0" dt="0.02">
    
        <CollisionPipeline name="CollisionPipeline" verbose="0"/>
        <DefaultAnimationLoop/>
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse name="collision response" response="PenalityContactForceField"/>
        <DiscreteIntersection/>
    
        <MeshOBJLoader name="LiverSurface" filename="mesh/liver-smooth.obj"/>
    
        <Node name="Liver" gravity="0 -9.81 0">
            <EulerImplicitSolver name="cg_odesolver" rayleighStiffness="0.1" rayleighMass="0.1"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixMat3x3d"/>
            <MeshGmshLoader name="meshLoader" filename="mesh/liver.msh"/>
            <TetrahedronSetTopologyContainer name="topo" src="@meshLoader"/>
            <MechanicalObject name="dofs" src="@meshLoader"/>
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo"/>
            <DiagonalMass name="computed using mass density" massDensity="1"/>
            <TetrahedralCorotationalFEMForceField template="Vec3" name="FEM" method="large" poissonRatio="0.3"
                                                  youngModulus="3000" computeGlobalMatrix="0"/>
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="3 39 64"/>
            <Node name="constraintSpace">
                <MechanicalObject template="Vec1" name="volumeDoFs"/>
                <VolumeMapping name="volumeMapping" topology="@../topo" geometricStiffness="Exact" applyRestPosition="true"/>
                <RestShapeSpringsForceField template="Vec1" stiffness="15000"/>
            </Node>
            <Node name="Visu" tags="Visual" gravity="0 -9.81 0">
                <OglModel name="VisualModel" src="@../../LiverSurface"/>
                <BarycentricMapping name="visual mapping" input="@../dofs" output="@VisualModel"/>
            </Node>
            <Node name="Surf" gravity="0 -9.81 0">
                <SphereLoader filename="mesh/liver.sph"/>
                <MechanicalObject name="spheres" position="@[-1].position"/>
                <SphereCollisionModel name="CollisionModel" listRadius="@[-2].listRadius"/>
                <BarycentricMapping name="sphere mapping" input="@../dofs" output="@spheres"/>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.02")

       root.addObject('CollisionPipeline', name="CollisionPipeline", verbose="0")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', name="collision response", response="PenalityContactForceField")
       root.addObject('DiscreteIntersection', )
       root.addObject('MeshOBJLoader', name="LiverSurface", filename="mesh/liver-smooth.obj")

       liver = root.addChild('Liver', gravity="0 -9.81 0")

       liver.addObject('EulerImplicitSolver', name="cg_odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       liver.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixMat3x3d")
       liver.addObject('MeshGmshLoader', name="meshLoader", filename="mesh/liver.msh")
       liver.addObject('TetrahedronSetTopologyContainer', name="topo", src="@meshLoader")
       liver.addObject('MechanicalObject', name="dofs", src="@meshLoader")
       liver.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       liver.addObject('DiagonalMass', name="computed using mass density", massDensity="1")
       liver.addObject('TetrahedralCorotationalFEMForceField', template="Vec3", name="FEM", method="large", poissonRatio="0.3", youngModulus="3000", computeGlobalMatrix="0")
       liver.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="3 39 64")

       constraint_space = Liver.addChild('constraintSpace')

       constraint_space.addObject('MechanicalObject', template="Vec1", name="volumeDoFs")
       constraint_space.addObject('VolumeMapping', name="volumeMapping", topology="@../topo", geometricStiffness="Exact", applyRestPosition="true")
       constraint_space.addObject('RestShapeSpringsForceField', template="Vec1", stiffness="15000")

       visu = Liver.addChild('Visu', tags="Visual", gravity="0 -9.81 0")

       visu.addObject('OglModel', name="VisualModel", src="@../../LiverSurface")
       visu.addObject('BarycentricMapping', name="visual mapping", input="@../dofs", output="@VisualModel")

       surf = Liver.addChild('Surf', gravity="0 -9.81 0")

       surf.addObject('SphereLoader', filename="mesh/liver.sph")
       surf.addObject('MechanicalObject', name="spheres", position="@[-1].position")
       surf.addObject('SphereCollisionModel', name="CollisionModel", listRadius="@[-2].listRadius")
       surf.addObject('BarycentricMapping', name="sphere mapping", input="@../dofs", output="@spheres")
    ```

