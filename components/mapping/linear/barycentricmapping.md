<!-- generate_doc -->
# BarycentricMapping

Mapping using barycentric coordinates of the child with respect to cells of its parent.
Mapping using barycentric coordinates of the child with respect to cells of its parent.


## Vec3d,Rigid3d

Templates:

- Vec3d,Rigid3d

__Target__: Sofa.Component.Mapping.Linear

__namespace__: sofa::component::mapping::linear

__parents__:

- CRTPLinearMapping

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
list of the subsets the object belongs to
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
		<td>useRestPosition</td>
		<td>
Use the rest position of the input and output models to initialize the mapping
		</td>
		<td>0</td>
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
|output|Output object to map|State&lt;Rigid3d&gt;|
|mapper|Internal mapper created depending on the type of topology|TopologyBarycentricMapper&lt;Vec3d,Rigid3d&gt;|
|input_topology|Input topology container (usually the surrounding domain).|BaseMeshTopology|
|output_topology|Output topology container (usually the immersed domain).|BaseMeshTopology|

<!-- generate_doc -->
## Vec3d,Vec3d

Templates:

- Vec3d,Vec3d

__Target__: Sofa.Component.Mapping.Linear

__namespace__: sofa::component::mapping::linear

__parents__:

- CRTPLinearMapping

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
list of the subsets the object belongs to
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
		<td>useRestPosition</td>
		<td>
Use the rest position of the input and output models to initialize the mapping
		</td>
		<td>0</td>
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
|output|Output object to map|State&lt;Vec3d&gt;|
|mapper|Internal mapper created depending on the type of topology|TopologyBarycentricMapper&lt;Vec3d,Vec3d&gt;|
|input_topology|Input topology container (usually the surrounding domain).|BaseMeshTopology|
|output_topology|Output topology container (usually the immersed domain).|BaseMeshTopology|

## Examples 

BarycentricMapping_meshtopology.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 -10 0" dt="0.01">
    
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [LinearSolverConstraintCorrection] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [FixedLagrangianConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetTopologyContainer] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        </Node>
    
        <DefaultAnimationLoop computeBoundingBox="false" />
        <MeshOBJLoader name="meshLoader" triangulate="true" filename="mesh/raptor_35kp.obj" />
    
        <Node name="data">
            <SparseGridTopology n="10 5 10" name="topology" fileTopology="@../meshLoader.filename" />
            <MechanicalObject name="DOFs" template="Vec3" />
        </Node>
    
        <Node name="raptor">
            <EulerImplicitSolver rayleighStiffness="0.2" rayleighMass="0.2" />
            <SparseLDLSolver template="CompressedRowSparseMatrixd"/>
            <MeshTopology hexahedra="@../data/topology.hexahedra" />
            <MechanicalObject name="DOFs" template="Vec3" position="@../data/DOFs.position"/>
            <UniformMass totalMass="1.005"/>
            <TetrahedronFEMForceField name="FEM" youngModulus="500" poissonRatio='0.3' />
    
            <BoxROI name='ROI1' box='-5 -1 -3  5 1 3' drawBoxes='true'/>
            <FixedProjectiveConstraint indices="@ROI1.indices" />
    
            <Node name="Collision">
                <MechanicalObject name="collisMecha" src="@../../meshLoader" />
                <TriangleSetTopologyContainer src="@../../meshLoader" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <BarycentricMapping />
            </Node>
    
            <Node name="Visualization">
                <OglModel name="VisualModel1" src="@../../meshLoader" useNormals="0" />
                <TriangleSetTopologyContainer src="@../../meshLoader" />
                <BarycentricMapping />
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -10 0", dt="0.01")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")

       root.addObject('DefaultAnimationLoop', computeBoundingBox="false")
       root.addObject('MeshOBJLoader', name="meshLoader", triangulate="true", filename="mesh/raptor_35kp.obj")

       data = root.addChild('data')

       data.addObject('SparseGridTopology', n="10 5 10", name="topology", fileTopology="@../meshLoader.filename")
       data.addObject('MechanicalObject', name="DOFs", template="Vec3")

       raptor = root.addChild('raptor')

       raptor.addObject('EulerImplicitSolver', rayleighStiffness="0.2", rayleighMass="0.2")
       raptor.addObject('SparseLDLSolver', template="CompressedRowSparseMatrixd")
       raptor.addObject('MeshTopology', hexahedra="@../data/topology.hexahedra")
       raptor.addObject('MechanicalObject', name="DOFs", template="Vec3", position="@../data/DOFs.position")
       raptor.addObject('UniformMass', totalMass="1.005")
       raptor.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.3")
       raptor.addObject('BoxROI', name="ROI1", box="-5 -1 -3  5 1 3", drawBoxes="true")
       raptor.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")

       collision = raptor.addChild('Collision')

       collision.addObject('MechanicalObject', name="collisMecha", src="@../../meshLoader")
       collision.addObject('TriangleSetTopologyContainer', src="@../../meshLoader")
       collision.addObject('TriangleCollisionModel', )
       collision.addObject('LineCollisionModel', )
       collision.addObject('PointCollisionModel', )
       collision.addObject('BarycentricMapping', )

       visualization = raptor.addChild('Visualization')

       visualization.addObject('OglModel', name="VisualModel1", src="@../../meshLoader", useNormals="0")
       visualization.addObject('TriangleSetTopologyContainer', src="@../../meshLoader")
       visualization.addObject('BarycentricMapping', )
    ```

BarycentricMapping_sparsegrid.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 -10 0" dt="0.01">
    
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [LinearSolverConstraintCorrection] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [FixedLagrangianConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetTopologyContainer] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        </Node>
    
        <DefaultAnimationLoop computeBoundingBox="false" />
        <MeshOBJLoader name="meshLoader" triangulate="true" filename="mesh/raptor_35kp.obj" />
    
        <Node name="raptor">
            <EulerImplicitSolver rayleighStiffness="0.2" rayleighMass="0.2" />
            <SparseLDLSolver template="CompressedRowSparseMatrixd"/>
            <SparseGridTopology n="10 5 10" name="topology" fileTopology="@../meshLoader.filename" />
            <MechanicalObject name="DOFs" template="Vec3" position="@../data/DOFs.position"/>
            <UniformMass totalMass="1.005"/>
            <TetrahedronFEMForceField name="FEM" youngModulus="500" poissonRatio='0.3' />
    
            <BoxROI name='ROI1' box='-5 -1 -3  5 1 3' drawBoxes='true'/>
            <FixedProjectiveConstraint indices="@ROI1.indices" />
    
              <Node name="Collision">
                <MechanicalObject name="collisMecha" src="@../../meshLoader" />
                <TriangleSetTopologyContainer src="@../../meshLoader" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <BarycentricMapping />
            </Node>
    
            <Node name="Visualization">
                <OglModel name="VisualModel1" src="@../../meshLoader" useNormals="0" />
                <TriangleSetTopologyContainer src="@../../meshLoader" />
                <BarycentricMapping />
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -10 0", dt="0.01")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")

       root.addObject('DefaultAnimationLoop', computeBoundingBox="false")
       root.addObject('MeshOBJLoader', name="meshLoader", triangulate="true", filename="mesh/raptor_35kp.obj")

       raptor = root.addChild('raptor')

       raptor.addObject('EulerImplicitSolver', rayleighStiffness="0.2", rayleighMass="0.2")
       raptor.addObject('SparseLDLSolver', template="CompressedRowSparseMatrixd")
       raptor.addObject('SparseGridTopology', n="10 5 10", name="topology", fileTopology="@../meshLoader.filename")
       raptor.addObject('MechanicalObject', name="DOFs", template="Vec3", position="@../data/DOFs.position")
       raptor.addObject('UniformMass', totalMass="1.005")
       raptor.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.3")
       raptor.addObject('BoxROI', name="ROI1", box="-5 -1 -3  5 1 3", drawBoxes="true")
       raptor.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")

       collision = raptor.addChild('Collision')

       collision.addObject('MechanicalObject', name="collisMecha", src="@../../meshLoader")
       collision.addObject('TriangleSetTopologyContainer', src="@../../meshLoader")
       collision.addObject('TriangleCollisionModel', )
       collision.addObject('LineCollisionModel', )
       collision.addObject('PointCollisionModel', )
       collision.addObject('BarycentricMapping', )

       visualization = raptor.addChild('Visualization')

       visualization.addObject('OglModel', name="VisualModel1", src="@../../meshLoader", useNormals="0")
       visualization.addObject('TriangleSetTopologyContainer', src="@../../meshLoader")
       visualization.addObject('BarycentricMapping', )
    ```

BarycentricMapping_topologycontainer.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 -10 0" dt="0.01">
    
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [LinearSolverConstraintCorrection] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Model"/> <!-- Needed to use components [FixedLagrangianConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [SparseLDLSolver] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TriangleSetTopologyContainer] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        </Node>
    
        <DefaultAnimationLoop computeBoundingBox="false" />
        <MeshOBJLoader name="meshLoader" triangulate="true" filename="mesh/raptor_35kp.obj" />
    
        <Node name="data">
            <SparseGridTopology n="10 5 10" name="topology" fileTopology="@../meshLoader.filename" />
            <MechanicalObject name="DOFs" template="Vec3" />
        </Node>
    
        <Node name="raptor">
            <EulerImplicitSolver rayleighStiffness="0.2" rayleighMass="0.2" />
            <SparseLDLSolver template="CompressedRowSparseMatrixd"/>
            <HexahedronSetTopologyContainer hexahedra="@../data/topology.hexahedra" />
            <MechanicalObject name="DOFs" template="Vec3" position="@../data/DOFs.position"/>
            <UniformMass totalMass="1.005"/>
            <TetrahedronFEMForceField name="FEM" youngModulus="500" poissonRatio='0.3' />
    
            <BoxROI name='ROI1' box='-5 -1 -3  5 1 3' drawBoxes='true'/>
            <FixedProjectiveConstraint indices="@ROI1.indices" />
    
            <Node name="Collision">
                <MechanicalObject name="collisMecha" src="@../../meshLoader" />
                <TriangleSetTopologyContainer src="@../../meshLoader" />
                <TriangleCollisionModel />
                <LineCollisionModel />
                <PointCollisionModel />
                <BarycentricMapping />
            </Node>
    
            <Node name="Visualization">
                <OglModel name="VisualModel1" src="@../../meshLoader" useNormals="0" />
                <TriangleSetTopologyContainer src="@../../meshLoader" />
                <BarycentricMapping />
            </Node>
        </Node>
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -10 0", dt="0.01")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Model")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")

       root.addObject('DefaultAnimationLoop', computeBoundingBox="false")
       root.addObject('MeshOBJLoader', name="meshLoader", triangulate="true", filename="mesh/raptor_35kp.obj")

       data = root.addChild('data')

       data.addObject('SparseGridTopology', n="10 5 10", name="topology", fileTopology="@../meshLoader.filename")
       data.addObject('MechanicalObject', name="DOFs", template="Vec3")

       raptor = root.addChild('raptor')

       raptor.addObject('EulerImplicitSolver', rayleighStiffness="0.2", rayleighMass="0.2")
       raptor.addObject('SparseLDLSolver', template="CompressedRowSparseMatrixd")
       raptor.addObject('HexahedronSetTopologyContainer', hexahedra="@../data/topology.hexahedra")
       raptor.addObject('MechanicalObject', name="DOFs", template="Vec3", position="@../data/DOFs.position")
       raptor.addObject('UniformMass', totalMass="1.005")
       raptor.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="500", poissonRatio="0.3")
       raptor.addObject('BoxROI', name="ROI1", box="-5 -1 -3  5 1 3", drawBoxes="true")
       raptor.addObject('FixedProjectiveConstraint', indices="@ROI1.indices")

       collision = raptor.addChild('Collision')

       collision.addObject('MechanicalObject', name="collisMecha", src="@../../meshLoader")
       collision.addObject('TriangleSetTopologyContainer', src="@../../meshLoader")
       collision.addObject('TriangleCollisionModel', )
       collision.addObject('LineCollisionModel', )
       collision.addObject('PointCollisionModel', )
       collision.addObject('BarycentricMapping', )

       visualization = raptor.addChild('Visualization')

       visualization.addObject('OglModel', name="VisualModel1", src="@../../meshLoader", useNormals="0")
       visualization.addObject('TriangleSetTopologyContainer', src="@../../meshLoader")
       visualization.addObject('BarycentricMapping', )
    ```

BarycentricMappingTrussBeam.scn

=== "XML"

    ```xml
    <Node name="root" dt="0.01" showBoundingTree="0" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping IdentityMapping TubularMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [ConstantForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [BeamFEMForceField TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [QuadSetTopologyContainer QuadSetTopologyModifier TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Edge2QuadTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <VisualStyle displayFlags="showVisual showBehaviorModels showCollisionModels" />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <LocalMinDistance name="Proximity" alarmDistance="0.5" contactDistance="0.05" />
        <CollisionResponse response="PenalityContactForceField" />
        <DefaultAnimationLoop/>
        
        <!-- A deformable square mesh -->
        <Node name="Truss" activated="true" gravity="0 0 0">
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="125" tolerance="1e-16" threshold="1e-16" />
            <MeshGmshLoader name="meshLoader0" filename="mesh/truss_tetra.msh" />
            <TetrahedronSetTopologyContainer name="Container" src="@meshLoader0" />
            <TetrahedronSetTopologyModifier name="Modifier" />
            <TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo" />
            <MechanicalObject template="Vec3" name="TrussMO" />
            <UniformMass totalMass="0.05" />
            <BoxConstraint box="-0.001 -0.001 -0.001 0.001 0.011 0.011" />
            <TetrahedronFEMForceField name="FEM" youngModulus="300000" poissonRatio="0.45" method="large" />
            <BoxROI box="0.099 -0.001 -0.001 0.11 0.011 0.011"/>
            <ConstantForceField forces="0 -0.1 0" />
    
            <Node name="Triangle">
                <TriangleSetTopologyContainer name="Container"/>
                <TriangleSetTopologyModifier />
                <Tetra2TriangleTopologicalMapping input="@/Truss/Container" output="@Container" />
                <TriangleCollisionModel />
                <Node name="TriangleVisual">
                    <OglModel template="Vec3" name="Visual" material="Default Diffuse 1 1 0 0 1 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45" />
                    <IdentityMapping template="Vec3,Vec3" name="default12" input="@.." output="@Visual" />
                </Node>
            </Node>
            <Node name="Beam">
                <MechanicalObject template="Rigid3" name="BeamMO" position="0 0 0  0 0 0 1  0.02 0 0  0 0 0 1  0.04 0 0  0 0 0 1   0.06 0 0  0 0 0 1  0.08 0 0  0 0 0 1   0.1 0 0  0 0 0 1" />
                <MeshTopology name="BeamMesh" lines="0 1 1 2 2 3 3 4 4 5" />
                <FixedProjectiveConstraint name="BeamFixedProjectiveConstraint" indices="0" />
                <UniformMass vertexMass="0.001 0.001 [0.0001 0 0 0 0.0001 0 0 0 0.0001]" />
                <BeamFEMForceField name="BeamFEM" radius="0.005" youngModulus="3000000000" poissonRatio="0.45" />
                <ConstantForceField indices="5" forces="0 0 0 -10 0 0" />
                <BarycentricMapping isMechanical="true" input="@TrussMO" output="@BeamMO" />
                <Node name="VisuThread">
                    <QuadSetTopologyContainer name="Container"/>
                    <QuadSetTopologyModifier />
                    <Edge2QuadTopologicalMapping nbPointsOnEachCircle="10" radius="0.005" input="@BeamMesh" output="@Container" />
                    <MechanicalObject name="Quads" />
                    <TubularMapping nbPointsOnEachCircle="10" radius="0.005" input="@BeamMO" output="@Quads" />
                    <Node name="VisuOgl">
                        <OglModel name="Visual" color="0.5 0.5 1.0" />
                        <IdentityMapping input="@Quads" output="@Visual" />
                    </Node>
                </Node>
            </Node>
        </Node>
    </Node>
    

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", showBoundingTree="0", gravity="0 0 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels showCollisionModels")
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('LocalMinDistance', name="Proximity", alarmDistance="0.5", contactDistance="0.05")
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('DefaultAnimationLoop', )

       truss = root.addChild('Truss', activated="true", gravity="0 0 0")

       truss.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       truss.addObject('CGLinearSolver', iterations="125", tolerance="1e-16", threshold="1e-16")
       truss.addObject('MeshGmshLoader', name="meshLoader0", filename="mesh/truss_tetra.msh")
       truss.addObject('TetrahedronSetTopologyContainer', name="Container", src="@meshLoader0")
       truss.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       truss.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       truss.addObject('MechanicalObject', template="Vec3", name="TrussMO")
       truss.addObject('UniformMass', totalMass="0.05")
       truss.addObject('BoxConstraint', box="-0.001 -0.001 -0.001 0.001 0.011 0.011")
       truss.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="300000", poissonRatio="0.45", method="large")
       truss.addObject('BoxROI', box="0.099 -0.001 -0.001 0.11 0.011 0.011")
       truss.addObject('ConstantForceField', forces="0 -0.1 0")

       triangle = Truss.addChild('Triangle')

       triangle.addObject('TriangleSetTopologyContainer', name="Container")
       triangle.addObject('TriangleSetTopologyModifier', )
       triangle.addObject('Tetra2TriangleTopologicalMapping', input="@/Truss/Container", output="@Container")
       triangle.addObject('TriangleCollisionModel', )

       triangle_visual = Triangle.addChild('TriangleVisual')

       triangle_visual.addObject('OglModel', template="Vec3", name="Visual", material="Default Diffuse 1 1 0 0 1 Ambient 1 0.2 0 0 1 Specular 0 1 0 0 1 Emissive 0 1 0 0 1 Shininess 0 45")
       triangle_visual.addObject('IdentityMapping', template="Vec3,Vec3", name="default12", input="@..", output="@Visual")

       beam = Truss.addChild('Beam')

       beam.addObject('MechanicalObject', template="Rigid3", name="BeamMO", position="0 0 0  0 0 0 1  0.02 0 0  0 0 0 1  0.04 0 0  0 0 0 1   0.06 0 0  0 0 0 1  0.08 0 0  0 0 0 1   0.1 0 0  0 0 0 1")
       beam.addObject('MeshTopology', name="BeamMesh", lines="0 1 1 2 2 3 3 4 4 5")
       beam.addObject('FixedProjectiveConstraint', name="BeamFixedProjectiveConstraint", indices="0")
       beam.addObject('UniformMass', vertexMass="0.001 0.001 [0.0001 0 0 0 0.0001 0 0 0 0.0001]")
       beam.addObject('BeamFEMForceField', name="BeamFEM", radius="0.005", youngModulus="3000000000", poissonRatio="0.45")
       beam.addObject('ConstantForceField', indices="5", forces="0 0 0 -10 0 0")
       beam.addObject('BarycentricMapping', isMechanical="true", input="@TrussMO", output="@BeamMO")

       visu_thread = Beam.addChild('VisuThread')

       visu_thread.addObject('QuadSetTopologyContainer', name="Container")
       visu_thread.addObject('QuadSetTopologyModifier', )
       visu_thread.addObject('Edge2QuadTopologicalMapping', nbPointsOnEachCircle="10", radius="0.005", input="@BeamMesh", output="@Container")
       visu_thread.addObject('MechanicalObject', name="Quads")
       visu_thread.addObject('TubularMapping', nbPointsOnEachCircle="10", radius="0.005", input="@BeamMO", output="@Quads")

       visu_ogl = VisuThread.addChild('VisuOgl')

       visu_ogl.addObject('OglModel', name="Visual", color="0.5 0.5 1.0")
       visu_ogl.addObject('IdentityMapping', input="@Quads", output="@Visual")
    ```

BarycentricMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.02">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [RigidMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [MeshSpringForceField RegularGridSpringForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showBehaviorModels showMappings" />
        <CollisionPipeline depth="6" verbose="0" draw="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <MinProximityIntersection name="Proximity" alarmDistance="0.3" contactDistance="0.2" />
        <CollisionResponse name="Response" response="PenalityContactForceField" />
        <Node name="Chain">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_19" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_19" color="gray" />
            </Node>
            <Node name="TorusFEM">
                <EulerImplicitSolver rayleighStiffness="0.01"  rayleighMass="0.1" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="2.5" />
                <UniformMass vertexMass="0.1" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_3" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_3" color="red" dx="2.5" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="2.5" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusSpring">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="5" />
                <UniformMass totalMass="5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="400" tetrasDamping="4" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_8" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_8" dx="5" color="green" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="5" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFFD">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject dx="7.5" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="2" nz="5" xmin="-2.5" xmax="2.5" ymin="-0.5" ymax="0.5" zmin="-2" zmax="2" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_13" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_13" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusRigid">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject template="Rigid3" dx="10" />
                <UniformMass filename="BehaviorModels/torus2.rigid" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_17" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_17" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
        </Node>
        <Node name="ChainFEM">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dz="6" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_21" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_21" color="gray" dz="6" />
            </Node>
            <Node name="TorusFEM1">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="2.5" dz="6" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_23" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_23" color="red" dx="2.5" dz="6" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="2.5" dz="6" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM2">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="5" dz="6" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_1" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_1" color="red" dx="5" dz="6" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="5" dz="6" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM3">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="7.5" dz="6" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_6" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_6" color="red" dx="7.5" dz="6" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="7.5" dz="6" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFEM4">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="10" dz="6" />
                <UniformMass totalMass="5" />
                <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.3" computeGlobalMatrix="false" method="polar" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_10" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_10" color="red" dx="10" dz="6" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="10" dz="6" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
        </Node>
        <Node name="ChainSpring">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dz="12" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_14" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_14" dz="12" color="gray" />
            </Node>
            <Node name="TorusSpring1">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="2.5" dz="12" />
                <UniformMass totalMass="5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="400" tetrasDamping="4" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_18" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_18" dx="2.5" dz="12" color="green" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="2.5" dz="12" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusSpring2">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="5" dz="12" />
                <UniformMass totalMass="5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="400" tetrasDamping="4" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_22" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_22" dx="5" dz="12" color="green" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="5" dz="12" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusSpring3">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="7.5" dz="12" />
                <UniformMass totalMass="5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="400" tetrasDamping="4" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_0" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_0" dx="7.5" dz="12" color="green" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="7.5" dz="12" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusSpring4">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MeshGmshLoader name="loader" filename="mesh/torus2_low_res.msh" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dx="10" dz="12" />
                <UniformMass totalMass="5" />
                <MeshSpringForceField name="Springs" tetrasStiffness="400" tetrasDamping="4" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_5" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_5" dx="10" dz="12" color="green" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" dx="10" dz="12" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
        </Node>
        <Node name="ChainFFD">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dz="18" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_9" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_9" dz="18" color="gray" />
            </Node>
            <Node name="TorusFFD1">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject dx="2.5" dz="18" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="2" nz="5" xmin="-2.5" xmax="2.5" ymin="-0.5" ymax="0.5" zmin="-2" zmax="2" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_11" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_11" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFFD2">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject dx="5" dz="18" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="5" nz="2" xmin="-2.5" xmax="2.5" ymin="-2" ymax="2" zmin="-0.5" zmax="0.5" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_15" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_15" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFFD3">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject dx="7.5" dz="18" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="2" nz="5" xmin="-2.5" xmax="2.5" ymin="-0.5" ymax="0.5" zmin="-2" zmax="2" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_20" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_20" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
            <Node name="TorusFFD4">
                <EulerImplicitSolver rayleighStiffness="0.01" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject dx="10" dz="18" />
                <UniformMass totalMass="5" />
                <RegularGridTopology nx="6" ny="5" nz="2" xmin="-2.5" xmax="2.5" ymin="-2" ymax="2" zmin="-0.5" zmax="0.5" />
                <RegularGridSpringForceField name="Springs" stiffness="200" damping="2" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_24" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_24" color="yellow" />
                    <BarycentricMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <BarycentricMapping />
                </Node>
            </Node>
        </Node>
        <Node name="ChainRigid">
            <Node name="TorusFixed">
                <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                <MeshTopology src="@loader" />
                <MechanicalObject src="@loader" dz="24" />
                <TriangleCollisionModel simulated="0" moving="0" />
                <LineCollisionModel simulated="0" moving="0" />
                <PointCollisionModel simulated="0" moving="0" />
                <MeshOBJLoader name="meshLoader_2" filename="mesh/torus2.obj" handleSeams="1" />
                <OglModel name="Visual" src="@meshLoader_2" dz="24" color="gray" />
            </Node>
            <Node name="TorusRigid1">
                <EulerImplicitSolver rayleighStiffness="0" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject template="Rigid3" dx="2.5" dz="24" />
                <UniformMass filename="BehaviorModels/torus.rigid" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_4" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_4" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
            <Node name="TorusRigid2">
                <EulerImplicitSolver rayleighStiffness="0" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject template="Rigid3" dx="5" dz="24" />
                <UniformMass filename="BehaviorModels/torus2.rigid" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_7" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_7" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
            <Node name="TorusRigid3">
                <EulerImplicitSolver rayleighStiffness="0" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject template="Rigid3" dx="7.5" dz="24" />
                <UniformMass filename="BehaviorModels/torus.rigid" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_12" filename="mesh/torus.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_12" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
            <Node name="TorusRigid4">
                <EulerImplicitSolver rayleighStiffness="0" />
                <CGLinearSolver iterations="100" threshold="0.00000001" tolerance="1e-5"/>
                <MechanicalObject template="Rigid3" dx="10" dz="24" />
                <UniformMass filename="BehaviorModels/torus2.rigid" />
                <Node name="Visu">
                    <MeshOBJLoader name="meshLoader_16" filename="mesh/torus2.obj" handleSeams="1" />
                    <OglModel name="Visual" src="@meshLoader_16" color="gray" />
                    <RigidMapping input="@.." output="@Visual" />
                </Node>
                <Node name="Surf2">
                    <MeshOBJLoader name="loader" filename="mesh/torus2_for_collision.obj" />
                    <MeshTopology src="@loader" />
                    <MechanicalObject src="@loader" />
                    <TriangleCollisionModel />
                    <LineCollisionModel />
                    <PointCollisionModel />
                    <RigidMapping />
                </Node>
            </Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.02")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showBehaviorModels showMappings")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.3", contactDistance="0.2")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")

       chain = root.addChild('Chain')

       torus_fixed = Chain.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('LineCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('PointCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_19", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_19", color="gray")

       torus_fem = Chain.addChild('TorusFEM')

       torus_fem.addObject('EulerImplicitSolver', rayleighStiffness="0.01", rayleighMass="0.1")
       torus_fem.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_fem.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
       torus_fem.addObject('MeshTopology', src="@loader")
       torus_fem.addObject('MechanicalObject', src="@loader", dx="2.5")
       torus_fem.addObject('UniformMass', vertexMass="0.1")
       torus_fem.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", computeGlobalMatrix="false", method="polar")

       visu = TorusFEM.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_3", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_3", color="red", dx="2.5")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="2.5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_spring = Chain.addChild('TorusSpring')

       torus_spring.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_spring.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_spring.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
       torus_spring.addObject('MeshTopology', src="@loader")
       torus_spring.addObject('MechanicalObject', src="@loader", dx="5")
       torus_spring.addObject('UniformMass', totalMass="5")
       torus_spring.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="4")

       visu = TorusSpring.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_8", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_8", dx="5", color="green")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusSpring.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="5")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_ffd = Chain.addChild('TorusFFD')

       torus_ffd.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_ffd.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_ffd.addObject('MechanicalObject', dx="7.5")
       torus_ffd.addObject('UniformMass', totalMass="5")
       torus_ffd.addObject('RegularGridTopology', nx="6", ny="2", nz="5", xmin="-2.5", xmax="2.5", ymin="-0.5", ymax="0.5", zmin="-2", zmax="2")
       torus_ffd.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

       visu = TorusFFD.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_13", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_13", color="yellow")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFFD.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_rigid = Chain.addChild('TorusRigid')

       torus_rigid.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_rigid.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_rigid.addObject('MechanicalObject', template="Rigid3", dx="10")
       torus_rigid.addObject('UniformMass', filename="BehaviorModels/torus2.rigid")

       visu = TorusRigid.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_17", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_17", color="gray")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = TorusRigid.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('RigidMapping', )

       chain_fem = root.addChild('ChainFEM')

       torus_fixed = ChainFEM.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader", dz="6")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('LineCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('PointCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_21", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_21", color="gray", dz="6")

       torus_fem1 = ChainFEM.addChild('TorusFEM1')

       torus_fem1.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_fem1.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_fem1.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
       torus_fem1.addObject('MeshTopology', src="@loader")
       torus_fem1.addObject('MechanicalObject', src="@loader", dx="2.5", dz="6")
       torus_fem1.addObject('UniformMass', totalMass="5")
       torus_fem1.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", computeGlobalMatrix="false", method="polar")

       visu = TorusFEM1.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_23", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_23", color="red", dx="2.5", dz="6")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM1.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="2.5", dz="6")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_fem2 = ChainFEM.addChild('TorusFEM2')

       torus_fem2.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_fem2.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_fem2.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
       torus_fem2.addObject('MeshTopology', src="@loader")
       torus_fem2.addObject('MechanicalObject', src="@loader", dx="5", dz="6")
       torus_fem2.addObject('UniformMass', totalMass="5")
       torus_fem2.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", computeGlobalMatrix="false", method="polar")

       visu = TorusFEM2.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_1", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_1", color="red", dx="5", dz="6")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM2.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="5", dz="6")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_fem3 = ChainFEM.addChild('TorusFEM3')

       torus_fem3.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_fem3.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_fem3.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
       torus_fem3.addObject('MeshTopology', src="@loader")
       torus_fem3.addObject('MechanicalObject', src="@loader", dx="7.5", dz="6")
       torus_fem3.addObject('UniformMass', totalMass="5")
       torus_fem3.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", computeGlobalMatrix="false", method="polar")

       visu = TorusFEM3.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_6", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_6", color="red", dx="7.5", dz="6")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM3.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="7.5", dz="6")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_fem4 = ChainFEM.addChild('TorusFEM4')

       torus_fem4.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_fem4.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_fem4.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
       torus_fem4.addObject('MeshTopology', src="@loader")
       torus_fem4.addObject('MechanicalObject', src="@loader", dx="10", dz="6")
       torus_fem4.addObject('UniformMass', totalMass="5")
       torus_fem4.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.3", computeGlobalMatrix="false", method="polar")

       visu = TorusFEM4.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_10", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_10", color="red", dx="10", dz="6")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFEM4.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="10", dz="6")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       chain_spring = root.addChild('ChainSpring')

       torus_fixed = ChainSpring.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader", dz="12")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('LineCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('PointCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_14", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_14", dz="12", color="gray")

       torus_spring1 = ChainSpring.addChild('TorusSpring1')

       torus_spring1.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_spring1.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_spring1.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
       torus_spring1.addObject('MeshTopology', src="@loader")
       torus_spring1.addObject('MechanicalObject', src="@loader", dx="2.5", dz="12")
       torus_spring1.addObject('UniformMass', totalMass="5")
       torus_spring1.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="4")

       visu = TorusSpring1.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_18", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_18", dx="2.5", dz="12", color="green")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusSpring1.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="2.5", dz="12")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_spring2 = ChainSpring.addChild('TorusSpring2')

       torus_spring2.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_spring2.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_spring2.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
       torus_spring2.addObject('MeshTopology', src="@loader")
       torus_spring2.addObject('MechanicalObject', src="@loader", dx="5", dz="12")
       torus_spring2.addObject('UniformMass', totalMass="5")
       torus_spring2.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="4")

       visu = TorusSpring2.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_22", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_22", dx="5", dz="12", color="green")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusSpring2.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="5", dz="12")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_spring3 = ChainSpring.addChild('TorusSpring3')

       torus_spring3.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_spring3.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_spring3.addObject('MeshGmshLoader', name="loader", filename="mesh/torus_low_res.msh")
       torus_spring3.addObject('MeshTopology', src="@loader")
       torus_spring3.addObject('MechanicalObject', src="@loader", dx="7.5", dz="12")
       torus_spring3.addObject('UniformMass', totalMass="5")
       torus_spring3.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="4")

       visu = TorusSpring3.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_0", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_0", dx="7.5", dz="12", color="green")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusSpring3.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="7.5", dz="12")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_spring4 = ChainSpring.addChild('TorusSpring4')

       torus_spring4.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_spring4.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_spring4.addObject('MeshGmshLoader', name="loader", filename="mesh/torus2_low_res.msh")
       torus_spring4.addObject('MeshTopology', src="@loader")
       torus_spring4.addObject('MechanicalObject', src="@loader", dx="10", dz="12")
       torus_spring4.addObject('UniformMass', totalMass="5")
       torus_spring4.addObject('MeshSpringForceField', name="Springs", tetrasStiffness="400", tetrasDamping="4")

       visu = TorusSpring4.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_5", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_5", dx="10", dz="12", color="green")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusSpring4.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader", dx="10", dz="12")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       chain_ffd = root.addChild('ChainFFD')

       torus_fixed = ChainFFD.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader", dz="18")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('LineCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('PointCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_9", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_9", dz="18", color="gray")

       torus_ffd1 = ChainFFD.addChild('TorusFFD1')

       torus_ffd1.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_ffd1.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_ffd1.addObject('MechanicalObject', dx="2.5", dz="18")
       torus_ffd1.addObject('UniformMass', totalMass="5")
       torus_ffd1.addObject('RegularGridTopology', nx="6", ny="2", nz="5", xmin="-2.5", xmax="2.5", ymin="-0.5", ymax="0.5", zmin="-2", zmax="2")
       torus_ffd1.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

       visu = TorusFFD1.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_11", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_11", color="yellow")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFFD1.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_ffd2 = ChainFFD.addChild('TorusFFD2')

       torus_ffd2.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_ffd2.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_ffd2.addObject('MechanicalObject', dx="5", dz="18")
       torus_ffd2.addObject('UniformMass', totalMass="5")
       torus_ffd2.addObject('RegularGridTopology', nx="6", ny="5", nz="2", xmin="-2.5", xmax="2.5", ymin="-2", ymax="2", zmin="-0.5", zmax="0.5")
       torus_ffd2.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

       visu = TorusFFD2.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_15", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_15", color="yellow")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFFD2.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_ffd3 = ChainFFD.addChild('TorusFFD3')

       torus_ffd3.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_ffd3.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_ffd3.addObject('MechanicalObject', dx="7.5", dz="18")
       torus_ffd3.addObject('UniformMass', totalMass="5")
       torus_ffd3.addObject('RegularGridTopology', nx="6", ny="2", nz="5", xmin="-2.5", xmax="2.5", ymin="-0.5", ymax="0.5", zmin="-2", zmax="2")
       torus_ffd3.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

       visu = TorusFFD3.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_20", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_20", color="yellow")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFFD3.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       torus_ffd4 = ChainFFD.addChild('TorusFFD4')

       torus_ffd4.addObject('EulerImplicitSolver', rayleighStiffness="0.01")
       torus_ffd4.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_ffd4.addObject('MechanicalObject', dx="10", dz="18")
       torus_ffd4.addObject('UniformMass', totalMass="5")
       torus_ffd4.addObject('RegularGridTopology', nx="6", ny="5", nz="2", xmin="-2.5", xmax="2.5", ymin="-2", ymax="2", zmin="-0.5", zmax="0.5")
       torus_ffd4.addObject('RegularGridSpringForceField', name="Springs", stiffness="200", damping="2")

       visu = TorusFFD4.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_24", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_24", color="yellow")
       visu.addObject('BarycentricMapping', input="@..", output="@Visual")

       surf2 = TorusFFD4.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('BarycentricMapping', )

       chain_rigid = root.addChild('ChainRigid')

       torus_fixed = ChainRigid.addChild('TorusFixed')

       torus_fixed.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       torus_fixed.addObject('MeshTopology', src="@loader")
       torus_fixed.addObject('MechanicalObject', src="@loader", dz="24")
       torus_fixed.addObject('TriangleCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('LineCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('PointCollisionModel', simulated="0", moving="0")
       torus_fixed.addObject('MeshOBJLoader', name="meshLoader_2", filename="mesh/torus2.obj", handleSeams="1")
       torus_fixed.addObject('OglModel', name="Visual", src="@meshLoader_2", dz="24", color="gray")

       torus_rigid1 = ChainRigid.addChild('TorusRigid1')

       torus_rigid1.addObject('EulerImplicitSolver', rayleighStiffness="0")
       torus_rigid1.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_rigid1.addObject('MechanicalObject', template="Rigid3", dx="2.5", dz="24")
       torus_rigid1.addObject('UniformMass', filename="BehaviorModels/torus.rigid")

       visu = TorusRigid1.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_4", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_4", color="gray")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = TorusRigid1.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('RigidMapping', )

       torus_rigid2 = ChainRigid.addChild('TorusRigid2')

       torus_rigid2.addObject('EulerImplicitSolver', rayleighStiffness="0")
       torus_rigid2.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_rigid2.addObject('MechanicalObject', template="Rigid3", dx="5", dz="24")
       torus_rigid2.addObject('UniformMass', filename="BehaviorModels/torus2.rigid")

       visu = TorusRigid2.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_7", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_7", color="gray")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = TorusRigid2.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('RigidMapping', )

       torus_rigid3 = ChainRigid.addChild('TorusRigid3')

       torus_rigid3.addObject('EulerImplicitSolver', rayleighStiffness="0")
       torus_rigid3.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_rigid3.addObject('MechanicalObject', template="Rigid3", dx="7.5", dz="24")
       torus_rigid3.addObject('UniformMass', filename="BehaviorModels/torus.rigid")

       visu = TorusRigid3.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_12", filename="mesh/torus.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_12", color="gray")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = TorusRigid3.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('RigidMapping', )

       torus_rigid4 = ChainRigid.addChild('TorusRigid4')

       torus_rigid4.addObject('EulerImplicitSolver', rayleighStiffness="0")
       torus_rigid4.addObject('CGLinearSolver', iterations="100", threshold="0.00000001", tolerance="1e-5")
       torus_rigid4.addObject('MechanicalObject', template="Rigid3", dx="10", dz="24")
       torus_rigid4.addObject('UniformMass', filename="BehaviorModels/torus2.rigid")

       visu = TorusRigid4.addChild('Visu')

       visu.addObject('MeshOBJLoader', name="meshLoader_16", filename="mesh/torus2.obj", handleSeams="1")
       visu.addObject('OglModel', name="Visual", src="@meshLoader_16", color="gray")
       visu.addObject('RigidMapping', input="@..", output="@Visual")

       surf2 = TorusRigid4.addChild('Surf2')

       surf2.addObject('MeshOBJLoader', name="loader", filename="mesh/torus2_for_collision.obj")
       surf2.addObject('MeshTopology', src="@loader")
       surf2.addObject('MechanicalObject', src="@loader")
       surf2.addObject('TriangleCollisionModel', )
       surf2.addObject('LineCollisionModel', )
       surf2.addObject('PointCollisionModel', )
       surf2.addObject('RigidMapping', )
    ```

