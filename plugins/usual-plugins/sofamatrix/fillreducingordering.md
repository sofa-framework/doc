# FillReducingOrdering

Reorder the degrees of freedom to reduce fill-in


__Templates__:

- `#!c++ Vec3d`

__Target__: `SofaMatrix`

__namespace__: `#!c++ sofa::component::linearsolver`

__parents__: 

- `#!c++ DataEngine`

__categories__: 

- Engine

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
		<td>orderingMethod</td>
		<td>
Ordering method.
nestedDissection is the multilevel nested dissection algorithm implemented in the METIS library.
approximateMinimumDegree is the approximate minimum degree algorithm implemented in the Eigen library.
</td>
		<td>nestedDissection</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>permutation</td>
		<td>
Output vector of indices mapping the reordered vertices to the initial list
</td>
		<td></td>
	</tr>
	<tr>
		<td>invPermutation</td>
		<td>
Output vector of indices mapping the initial vertices to the reordered list
</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
Reordered position vector
</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
Reordered hexahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
Reordered tetrahedra
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
|mstate|Mechanical state to reorder|
|topology|Topology to reorder|



## Examples

SofaMatrix/share/sofa/examples/SofaMatrix/FillReducingOrdering.scn

=== "XML"

    ```xml
    <!--
    This scene introduces the usage of the component FillReducingOrdering.
    See its class description for more details.
    
    The scene compares two simulations in which only the vertices order differs:
    - The Node "NoReorder" simulates the initial mesh.
    - The Node "Reorder" simulates the reordered mesh.
    -->
    <Node name="root" gravity="-1.8 0 100" dt="0.001">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Transform"/> <!-- Needed to use components [MapIndices TransformEngine] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshGmshLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSparseLU] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [TetrahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering2D"/> <!-- Needed to use components [OglLabel] -->
        <RequiredPlugin name="SofaMatrix"/> <!-- Needed to use components [FillReducingOrdering GlobalSystemMatrixImage] -->
    
        <VisualStyle displayFlags="showForceFields hideVisualModels showBehaviorModels" />
    
        <Node name="Mesh">
    
            <MeshGmshLoader name="loader" filename="mesh/truthcylinder1.msh" />
            <TetrahedronSetTopologyContainer src="@loader" name="topologyContainer"/>
            <MechanicalObject name="dofs" src="@loader"/>
    
        </Node>
    
        <Node name="NoReorder" activated="true">
            <EulerImplicitSolver name="odeImplicitSolver" />
            <MatrixLinearSystem name="system"/>
            <EigenSparseLU name="solver" template="CompressedRowSparseMatrixd"/>
    
            <GlobalSystemMatrixImage linearSystem="@system"/>
    
            <TetrahedronSetTopologyContainer src="@../Mesh/loader" name="topologyContainer"/>
            <MechanicalObject name="dofs" src="@../Mesh/loader"/>
            <MeshMatrixMass totalMass="15" topology="@topologyContainer"/>
    
            <FixedProjectiveConstraint name="fix" indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.49" method="large" />
    
        </Node>
    
        <Node name="Reorder" activated="true">
            <EulerImplicitSolver name="odeImplicitSolver" />
            <MatrixLinearSystem name="system"/>
            <EigenSparseLU name="solver" template="CompressedRowSparseMatrixd"/>
    
            <GlobalSystemMatrixImage linearSystem="@system"/>
    
            <FillReducingOrdering name="reorder" mstate="@../Mesh/dofs" topology="@../Mesh/topologyContainer" orderingMethod="AMD"/>
            <TransformEngine name="transform" input_position="@reorder.position" translation="10 0 0"/>
    
            <TetrahedronSetTopologyContainer name="topologyContainer" tetrahedra="@reorder.tetrahedra" position="@transform.output_position"/>
            <TetrahedronSetGeometryAlgorithms name="geomAlgo"/>
    
            <MechanicalObject name="dofs" position="@transform.output_position"/>
            <MeshMatrixMass totalMass="15" topology="@topologyContainer"/>
    
            <MapIndices name="perm" template="int" in="@../NoReorder/fix.indices" indices="@reorder.permutation"/>
            <FixedProjectiveConstraint indices="@perm.out" />
            <TetrahedronFEMForceField name="FEM" youngModulus="1000" poissonRatio="0.49" method="large" />
    
        </Node>
    
        <OglLabel label="Nb non-zeroes:" fontsize="30"/>
        <OglLabel prefix="  Without reordering: " label="@NoReorder/solver.L_nnz" fontsize="20" y="70"/>
        <OglLabel prefix="  With reordering: " label="@Reorder/solver.L_nnz" fontsize="20" y="120"/>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', gravity="-1.8 0 100", dt="0.001")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Transform")
        root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
        root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering2D")
        root.addObject('RequiredPlugin', name="SofaMatrix")
        root.addObject('VisualStyle', displayFlags="showForceFields hideVisualModels showBehaviorModels")

        Mesh = root.addChild('Mesh')
        Mesh.addObject('MeshGmshLoader', name="loader", filename="mesh/truthcylinder1.msh")
        Mesh.addObject('TetrahedronSetTopologyContainer', src="@loader", name="topologyContainer")
        Mesh.addObject('MechanicalObject', name="dofs", src="@loader")

        NoReorder = root.addChild('NoReorder', activated="true")
        NoReorder.addObject('EulerImplicitSolver', name="odeImplicitSolver")
        NoReorder.addObject('MatrixLinearSystem', name="system")
        NoReorder.addObject('EigenSparseLU', name="solver", template="CompressedRowSparseMatrixd")
        NoReorder.addObject('GlobalSystemMatrixImage', linearSystem="@system")
        NoReorder.addObject('TetrahedronSetTopologyContainer', src="@../Mesh/loader", name="topologyContainer")
        NoReorder.addObject('MechanicalObject', name="dofs", src="@../Mesh/loader")
        NoReorder.addObject('MeshMatrixMass', totalMass="15", topology="@topologyContainer")
        NoReorder.addObject('FixedProjectiveConstraint', name="fix", indices="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 268 269 270 271 343 345")
        NoReorder.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.49", method="large")

        Reorder = root.addChild('Reorder', activated="true")
        Reorder.addObject('EulerImplicitSolver', name="odeImplicitSolver")
        Reorder.addObject('MatrixLinearSystem', name="system")
        Reorder.addObject('EigenSparseLU', name="solver", template="CompressedRowSparseMatrixd")
        Reorder.addObject('GlobalSystemMatrixImage', linearSystem="@system")
        Reorder.addObject('FillReducingOrdering', name="reorder", mstate="@../Mesh/dofs", topology="@../Mesh/topologyContainer", orderingMethod="AMD")
        Reorder.addObject('TransformEngine', name="transform", input_position="@reorder.position", translation="10 0 0")
        Reorder.addObject('TetrahedronSetTopologyContainer', name="topologyContainer", tetrahedra="@reorder.tetrahedra", position="@transform.output_position")
        Reorder.addObject('TetrahedronSetGeometryAlgorithms', name="geomAlgo")
        Reorder.addObject('MechanicalObject', name="dofs", position="@transform.output_position")
        Reorder.addObject('MeshMatrixMass', totalMass="15", topology="@topologyContainer")
        Reorder.addObject('MapIndices', name="perm", template="int", in="@../NoReorder/fix.indices", indices="@reorder.permutation")
        Reorder.addObject('FixedProjectiveConstraint', indices="@perm.out")
        Reorder.addObject('TetrahedronFEMForceField', name="FEM", youngModulus="1000", poissonRatio="0.49", method="large")
        root.addObject('OglLabel', label="Nb non-zeroes:", fontsize="30")
        root.addObject('OglLabel', prefix="  Without reordering: ", label="@NoReorder/solver.L_nnz", fontsize="20", y="70")
        root.addObject('OglLabel', prefix="  With reordering: ", label="@Reorder/solver.L_nnz", fontsize="20", y="120")
    ```

