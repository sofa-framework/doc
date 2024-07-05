# GenerateCylinder

Generate a Cylindrical Tetrahedral Mesh


__Templates__:

- `#!c++ Vec3d`

__Target__: `Sofa.Component.Engine.Generate`

__namespace__: `#!c++ sofa::component::engine::generate`

__parents__: 

- `#!c++ DataEngine`

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
		<td>BezierTriangleDegree</td>
		<td>
order of Bezier triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>BezierTetrahedronDegree</td>
		<td>
order of Bezier tetrahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>openSurface</td>
		<td>
if the cylinder is open at its 2 ends
</td>
		<td>1</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
input cylinder radius
</td>
		<td>0.2</td>
	</tr>
	<tr>
		<td>height</td>
		<td>
input cylinder height
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>origin</td>
		<td>
cylinder origin point
</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>resCircumferential</td>
		<td>
Resolution in the circumferential direction
</td>
		<td>6</td>
	</tr>
	<tr>
		<td>resRadial</td>
		<td>
Resolution in the radial direction
</td>
		<td>3</td>
	</tr>
	<tr>
		<td>resHeight</td>
		<td>
Resolution in the height direction
</td>
		<td>5</td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>output_TetrahedraPosition</td>
		<td>
output array of 3d points of tetrahedra mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>output_TrianglesPosition</td>
		<td>
output array of 3d points of triangle mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
output mesh tetrahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
output triangular mesh
</td>
		<td></td>
	</tr>
	<tr>
		<td>BezierTriangleWeights</td>
		<td>
weights of rational Bezier triangles
</td>
		<td></td>
	</tr>
	<tr>
		<td>isBezierTriangleRational</td>
		<td>
booleans indicating if each Bezier triangle is rational or integral
</td>
		<td></td>
	</tr>
	<tr>
		<td>BezierTetrahedronWeights</td>
		<td>
weights of rational Bezier tetrahedra
</td>
		<td></td>
	</tr>
	<tr>
		<td>isBezierTetrahedronRational</td>
		<td>
booleans indicating if each Bezier tetrahedron is rational or integral
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

Component/Engine/Generate/GenerateCylinder.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="1" showBoundingTree="0" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedPlaneProjectiveConstraint FixedProjectiveConstraint LineProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [GenerateCylinder] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [TrianglePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [FastTetrahedralCorotationalForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer] -->
    
        <DefaultAnimationLoop/>
        <GenerateCylinder template="Vec3" name="Cylinder" radius="0.2" height="1" resHeight="7" resCircumferential="7" resRadial="3" />
        <Node name="Tetra" >
            <CGLinearSolver iterations="3000" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" /> 
            <EulerImplicitSolver name="default12" rayleighStiffness="0.01"  rayleighMass="0.1" />
            <TetrahedronSetTopologyContainer name="Container" tetrahedra="@../Cylinder.tetrahedra" position="@../Cylinder.output_position" createTriangleArray="1" />
            <TetrahedronSetGeometryAlgorithms  drawEdges="1"/>
            <MechanicalObject name="dofs" showObject="1"/>
            <MeshMatrixMass name="mass" lumping="1" printMass="0" massDensity="1" />
            <BoxROI box="-0.01 -0.01 -0.01 0.01 0.01 0.01" drawBoxes="1" name="fixedPoint"  />
            <FixedProjectiveConstraint indices="@fixedPoint.indices" />
            <FixedPlaneProjectiveConstraint direction="0 0 1" dmin="-0.01" dmax="0.01"  />
            <BoxROI box="-0.2 -0.2 0.99 0.2 0.2 1.01" drawBoxes="1" name="pressurePlane"  />
            <LineProjectiveConstraint direction="1 0 0" origin="0 0 0" indices="15"  />
            <TrianglePressureForceField  showForces="1"  triangleList="@pressurePlane.triangleIndices" pressure="0.01 0 -0.04" />
            <FastTetrahedralCorotationalForceField poissonRatio="0.45" youngModulus="1" method="polar" /> 
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="1", showBoundingTree="0", gravity="0 0 0")
        root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
        root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
        root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
        root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
        root.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
        root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
        root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
        root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
        root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
        root.addObject('DefaultAnimationLoop')
        root.addObject('GenerateCylinder', template="Vec3", name="Cylinder", radius="0.2", height="1", resHeight="7", resCircumferential="7", resRadial="3")

        Tetra = root.addChild('Tetra')
        Tetra.addObject('CGLinearSolver', iterations="3000", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        Tetra.addObject('EulerImplicitSolver', name="default12", rayleighStiffness="0.01", rayleighMass="0.1")
        Tetra.addObject('TetrahedronSetTopologyContainer', name="Container", tetrahedra="@../Cylinder.tetrahedra", position="@../Cylinder.output_position", createTriangleArray="1")
        Tetra.addObject('TetrahedronSetGeometryAlgorithms', drawEdges="1")
        Tetra.addObject('MechanicalObject', name="dofs", showObject="1")
        Tetra.addObject('MeshMatrixMass', name="mass", lumping="1", printMass="0", massDensity="1")
        Tetra.addObject('BoxROI', box="-0.01 -0.01 -0.01 0.01 0.01 0.01", drawBoxes="1", name="fixedPoint")
        Tetra.addObject('FixedProjectiveConstraint', indices="@fixedPoint.indices")
        Tetra.addObject('FixedPlaneProjectiveConstraint', direction="0 0 1", dmin="-0.01", dmax="0.01")
        Tetra.addObject('BoxROI', box="-0.2 -0.2 0.99 0.2 0.2 1.01", drawBoxes="1", name="pressurePlane")
        Tetra.addObject('LineProjectiveConstraint', direction="1 0 0", origin="0 0 0", indices="15")
        Tetra.addObject('TrianglePressureForceField', showForces="1", triangleList="@pressurePlane.triangleIndices", pressure="0.01 0 -0.04")
        Tetra.addObject('FastTetrahedralCorotationalForceField', poissonRatio="0.45", youngModulus="1", method="polar")
    ```

