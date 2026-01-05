<!-- generate_doc -->
# VisualPointCloud

Render a point cloud.


## Rigid3d

Templates:

- Rigid3d

__Target__: Sofa.Component.Visual

__namespace__: sofa::component::visual

__parents__:

- VisualModel

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
		<td>enable</td>
		<td>
Display the object or not
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
The position of the points to display
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pointSize</td>
		<td>
The size of the points and frames
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>sphereRadius</td>
		<td>
The radius list of the spheres
		</td>
		<td></td>
	</tr>
	<tr>
		<td>color</td>
		<td>
The color of the points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>indicesScale</td>
		<td>
The scale of the indices
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>indicesColor</td>
		<td>
The color of the indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawMode</td>
		<td>
The draw mode:
- Point: Coordinates are displayed with points
- Sphere: Coordinates are displayed using spheres
- Frame: Coordinates are displayed using oriented frames
		</td>
		<td></td>
	</tr>
	<tr>
		<td>showIndices</td>
		<td>
Show the indices of the points
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

<!-- generate_doc -->
## Vec3d

Templates:

- Vec3d

__Target__: Sofa.Component.Visual

__namespace__: sofa::component::visual

__parents__:

- VisualModel

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
		<td>enable</td>
		<td>
Display the object or not
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>position</td>
		<td>
The position of the points to display
		</td>
		<td></td>
	</tr>
	<tr>
		<td>pointSize</td>
		<td>
The size of the points and frames
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>sphereRadius</td>
		<td>
The radius list of the spheres
		</td>
		<td></td>
	</tr>
	<tr>
		<td>color</td>
		<td>
The color of the points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>indicesScale</td>
		<td>
The scale of the indices
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>indicesColor</td>
		<td>
The color of the indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawMode</td>
		<td>
The draw mode:
- Point: Coordinates are displayed with points
- Sphere: Coordinates are displayed using spheres
		</td>
		<td></td>
	</tr>
	<tr>
		<td>showIndices</td>
		<td>
Show the indices of the points
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

## Examples 

VisualPointCloud.scn

=== "XML"

    ```xml
    <Node name="root" gravity="0 -9.81 0" dt="0.01">
    
        <Node name="plugins">
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [BTDLinearSolver,EigenSimplicialLDLT] -->
            <RequiredPlugin name="Sofa.Component.LinearSystem"/> <!-- Needed to use components [ConstantSparsityPatternSystem] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [BeamFEMForceField,HexahedronFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Constant"/> <!-- Needed to use components [MeshTopology] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [LineAxis,VisualGrid,VisualPointCloud,VisualStyle] -->
        </Node>
    
        <DefaultAnimationLoop parallelODESolving="true"/>
        <DefaultVisualManagerLoop name="visualLoop"/>
        <VisualStyle displayFlags="showVisual" />
        <VisualGrid name="grid"/>
        <LineAxis size="@grid.size"/>
    
        <Node name="3d_point">
            <EulerImplicitSolver name="odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <ConstantSparsityPatternSystem template="CompressedRowSparseMatrixd" name="A"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixd"/>
            <MechanicalObject name="DoFs" template="Vec3" />
            <UniformMass name="mass" totalMass="320" />
            <RegularGridTopology name="grid" nx="4" ny="4" nz="10" xmin="-5" xmax="-3" ymin="2" ymax="5" zmin="0" zmax="9" />
            <BoxROI name="box" box="-6 1 -0.0001  -2 6 0.0001"/>
            <FixedProjectiveConstraint indices="@box.indices" />
            <HexahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" method="large" />
    
            <VisualPointCloud position="@DoFs.position" pointSize="10" drawMode="Point" color="navy"/>
        </Node>
    
        <Node name="3d_sphere">
            <EulerImplicitSolver name="odesolver" rayleighStiffness="0.1" rayleighMass="0.1" />
            <ConstantSparsityPatternSystem template="CompressedRowSparseMatrixd" name="A"/>
            <EigenSimplicialLDLT template="CompressedRowSparseMatrixd"/>
            <MechanicalObject name="DoFs" template="Vec3" />
            <UniformMass name="mass" totalMass="320" />
            <RegularGridTopology name="grid" nx="4" ny="4" nz="10" xmin="-5" xmax="-3" ymin="-5" ymax="-2" zmin="0" zmax="9" />
            <BoxROI name="box" box="-6 -6 -0.0001  -2 -1 0.0001"/>
            <FixedProjectiveConstraint indices="@box.indices" />
            <HexahedronFEMForceField name="FEM" youngModulus="4000" poissonRatio="0.3" method="large" />
    
            <VisualPointCloud position="@DoFs.position" drawMode="Sphere" sphereRadius="0.1" color="lime"/>
        </Node>
    
        <Node name="rigid3">
            <EulerImplicitSolver rayleighStiffness="0" printLog="false" rayleighMass="0.1"/>
            <BTDLinearSolver template="BTDMatrix6d"/>
    
            <MechanicalObject template="Rigid3" name="DoFs" position="0 0 1 0 0 0 1  1 0 1 0 0 0 1  2 0 1 0 0 0 1  3 0 1 0 0 0 1" />
            <MeshTopology name="lines" lines="0 1 1 2 2 3" />
            <FixedProjectiveConstraint name="FixedProjectiveConstraint" indices="0" />
            <UniformMass totalMass="4" />
            <BeamFEMForceField name="FEM" radius="0.05" radiusInner="0" youngModulus="20000000" poissonRatio="0.49"/>
    
            <VisualPointCloud position="@DoFs.position" pointSize="1" template="Rigid3" drawMode="Frame"/>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.01")

       plugins = root.addChild('plugins')

       plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSystem")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Constant")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       plugins.addObject('RequiredPlugin', name="Sofa.Component.Visual")

       root.addObject('DefaultAnimationLoop', parallelODESolving="true")
       root.addObject('DefaultVisualManagerLoop', name="visualLoop")
       root.addObject('VisualStyle', displayFlags="showVisual")
       root.addObject('VisualGrid', name="grid")
       root.addObject('LineAxis', size="@grid.size")

       3d_point = root.addChild('3d_point')

       3d_point.addObject('EulerImplicitSolver', name="odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       3d_point.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrixd", name="A")
       3d_point.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixd")
       3d_point.addObject('MechanicalObject', name="DoFs", template="Vec3")
       3d_point.addObject('UniformMass', name="mass", totalMass="320")
       3d_point.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="10", xmin="-5", xmax="-3", ymin="2", ymax="5", zmin="0", zmax="9")
       3d_point.addObject('BoxROI', name="box", box="-6 1 -0.0001  -2 6 0.0001")
       3d_point.addObject('FixedProjectiveConstraint', indices="@box.indices")
       3d_point.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")
       3d_point.addObject('VisualPointCloud', position="@DoFs.position", pointSize="10", drawMode="Point", color="navy")

       3d_sphere = root.addChild('3d_sphere')

       3d_sphere.addObject('EulerImplicitSolver', name="odesolver", rayleighStiffness="0.1", rayleighMass="0.1")
       3d_sphere.addObject('ConstantSparsityPatternSystem', template="CompressedRowSparseMatrixd", name="A")
       3d_sphere.addObject('EigenSimplicialLDLT', template="CompressedRowSparseMatrixd")
       3d_sphere.addObject('MechanicalObject', name="DoFs", template="Vec3")
       3d_sphere.addObject('UniformMass', name="mass", totalMass="320")
       3d_sphere.addObject('RegularGridTopology', name="grid", nx="4", ny="4", nz="10", xmin="-5", xmax="-3", ymin="-5", ymax="-2", zmin="0", zmax="9")
       3d_sphere.addObject('BoxROI', name="box", box="-6 -6 -0.0001  -2 -1 0.0001")
       3d_sphere.addObject('FixedProjectiveConstraint', indices="@box.indices")
       3d_sphere.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000", poissonRatio="0.3", method="large")
       3d_sphere.addObject('VisualPointCloud', position="@DoFs.position", drawMode="Sphere", sphereRadius="0.1", color="lime")

       rigid3 = root.addChild('rigid3')

       rigid3.addObject('EulerImplicitSolver', rayleighStiffness="0", printLog="false", rayleighMass="0.1")
       rigid3.addObject('BTDLinearSolver', template="BTDMatrix6d")
       rigid3.addObject('MechanicalObject', template="Rigid3", name="DoFs", position="0 0 1 0 0 0 1  1 0 1 0 0 0 1  2 0 1 0 0 0 1  3 0 1 0 0 0 1")
       rigid3.addObject('MeshTopology', name="lines", lines="0 1 1 2 2 3")
       rigid3.addObject('FixedProjectiveConstraint', name="FixedProjectiveConstraint", indices="0")
       rigid3.addObject('UniformMass', totalMass="4")
       rigid3.addObject('BeamFEMForceField', name="FEM", radius="0.05", radiusInner="0", youngModulus="20000000", poissonRatio="0.49")
       rigid3.addObject('VisualPointCloud', position="@DoFs.position", pointSize="1", template="Rigid3", drawMode="Frame")
    ```

