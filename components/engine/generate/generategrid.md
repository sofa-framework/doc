<!-- generate_doc -->
# GenerateGrid

Generate a Grid Tetrahedral or Hexahedral Mesh


Templates:

- Vec2d
- Vec3d

__Target__: Sofa.Component.Engine.Generate

__namespace__: sofa::component::engine::generate

__parents__:

- DataEngine

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
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>output_position</td>
		<td>
output array of 3d points
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
		<td>quads</td>
		<td>
output mesh quads
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
output mesh triangles
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
output mesh hexahedra
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>min</td>
		<td>
the 3 coordinates of the minimum corner
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>max</td>
		<td>
the 3 coordinates of the maximum corner
		</td>
		<td>0 0 0</td>
	</tr>
	<tr>
		<td>resolution</td>
		<td>
the number of cubes in the x,y,z directions. If resolution in the z direction is  0 then a 2D grid is generated
		</td>
		<td>3 3 3</td>
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

GenerateGrid.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="1" showBoundingTree="0" gravity="0 0 0">
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedPlaneProjectiveConstraint FixedProjectiveConstraint LineProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [GenerateGrid] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [MeshMatrixMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [QuadPressureForceField TrianglePressureForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [FastTetrahedralCorotationalForceField HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [HexahedronSetGeometryAlgorithms HexahedronSetTopologyContainer TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer] -->
        <DefaultAnimationLoop/>
    
        <GenerateGrid template="Vec3" name="Slab" max="0.5 1.5 1" resolution="5 3 4" />
        <Node name="Tetra">
            <CGLinearSolver iterations="3000" name="linear solver" tolerance="1.0e-12" threshold="1.0e-12" /> 
            <EulerImplicitSolver name="default12" rayleighStiffness="0.01"  rayleighMass="0.1" />
            <TetrahedronSetTopologyContainer name="Container1" tetrahedra="@../Slab.tetrahedra" position="@../Slab.output_position" createTriangleArray="1"/>
            <TetrahedronSetGeometryAlgorithms  drawTriangles="1"/>
            <MechanicalObject name="dofs" showObject="1"/>
            <MeshMatrixMass name="mass" lumping="1" printMass="0" massDensity="1" />	
            <BoxROI box="-0.01 -0.01 -0.01 0.01 0.01 0.01" drawBoxes="1" name="fixedPoint"  />
            <FixedProjectiveConstraint indices="@fixedPoint.indices" />
            <FixedPlaneProjectiveConstraint direction="0 0 1" dmin="-0.01" dmax="0.01"  />
            <BoxROI box="-5.2 -5.2 7.49 5.2 5.2 7.51" drawBoxes="1" name="pressurePlane"  />
            <LineProjectiveConstraint direction="1 0 0" origin="0 0 0" indices="4"  />
            <TrianglePressureForceField  showForces="1"  triangleList="@pressurePlane.triangleIndices" pressure="0.00 0 -0.04" />
            <FastTetrahedralCorotationalForceField poissonRatio="0.45" youngModulus="1" method="polar" /> 
        </Node>
        <Node name="Hexa">
            <CGLinearSolver iterations="3000" name="linear solver" tolerance="1.0e-12" threshold="1.0e-12" /> 
            <EulerImplicitSolver name="default12" rayleighStiffness="0.01" />
            <HexahedronSetTopologyContainer name="Container1" hexahedra="@../Slab.hexahedra" position="@../Slab.output_position" createQuadArray="1"/>
            <HexahedronSetGeometryAlgorithms  drawQuads="1"/>
            <MechanicalObject name="dofs" translation="5 0 0" showObject="1"/>
            <MeshMatrixMass name="mass" lumping="1" printMass="0" massDensity="1" />	
            <BoxROI box="-4.99 -0.01 -0.01 5.01 0.01 0.01" drawBoxes="1" name="fixedPointHexa"  />
            <FixedProjectiveConstraint indices="@fixedPointHexa.indices" />
            <FixedPlaneProjectiveConstraint direction="0 0 1" dmin="-0.01" dmax="0.01"  />
            <BoxROI box="-0.2 -5.2 7.49 10.2 5.2 7.51" drawBoxes="1" name="pressurePlaneQuad"  />
            <LineProjectiveConstraint direction="1 0 0" origin="0 0 0" indices="4"  />
            <QuadPressureForceField  showForces="1"  quadList="@pressurePlaneQuad.quadIndices" pressure="0.00 0 -0.04" />
            <HexahedronFEMForceField poissonRatio="0.45" youngModulus="1" method="polar" /> 
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="1", showBoundingTree="0", gravity="0 0 0")

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
       root.addObject('DefaultAnimationLoop', )
       root.addObject('GenerateGrid', template="Vec3", name="Slab", max="0.5 1.5 1", resolution="5 3 4")

       tetra = root.addChild('Tetra')

       tetra.addObject('CGLinearSolver', iterations="3000", name="linear solver", tolerance="1.0e-12", threshold="1.0e-12")
       tetra.addObject('EulerImplicitSolver', name="default12", rayleighStiffness="0.01", rayleighMass="0.1")
       tetra.addObject('TetrahedronSetTopologyContainer', name="Container1", tetrahedra="@../Slab.tetrahedra", position="@../Slab.output_position", createTriangleArray="1")
       tetra.addObject('TetrahedronSetGeometryAlgorithms', drawTriangles="1")
       tetra.addObject('MechanicalObject', name="dofs", showObject="1")
       tetra.addObject('MeshMatrixMass', name="mass", lumping="1", printMass="0", massDensity="1")
       tetra.addObject('BoxROI', box="-0.01 -0.01 -0.01 0.01 0.01 0.01", drawBoxes="1", name="fixedPoint")
       tetra.addObject('FixedProjectiveConstraint', indices="@fixedPoint.indices")
       tetra.addObject('FixedPlaneProjectiveConstraint', direction="0 0 1", dmin="-0.01", dmax="0.01")
       tetra.addObject('BoxROI', box="-5.2 -5.2 7.49 5.2 5.2 7.51", drawBoxes="1", name="pressurePlane")
       tetra.addObject('LineProjectiveConstraint', direction="1 0 0", origin="0 0 0", indices="4")
       tetra.addObject('TrianglePressureForceField', showForces="1", triangleList="@pressurePlane.triangleIndices", pressure="0.00 0 -0.04")
       tetra.addObject('FastTetrahedralCorotationalForceField', poissonRatio="0.45", youngModulus="1", method="polar")

       hexa = root.addChild('Hexa')

       hexa.addObject('CGLinearSolver', iterations="3000", name="linear solver", tolerance="1.0e-12", threshold="1.0e-12")
       hexa.addObject('EulerImplicitSolver', name="default12", rayleighStiffness="0.01")
       hexa.addObject('HexahedronSetTopologyContainer', name="Container1", hexahedra="@../Slab.hexahedra", position="@../Slab.output_position", createQuadArray="1")
       hexa.addObject('HexahedronSetGeometryAlgorithms', drawQuads="1")
       hexa.addObject('MechanicalObject', name="dofs", translation="5 0 0", showObject="1")
       hexa.addObject('MeshMatrixMass', name="mass", lumping="1", printMass="0", massDensity="1")
       hexa.addObject('BoxROI', box="-4.99 -0.01 -0.01 5.01 0.01 0.01", drawBoxes="1", name="fixedPointHexa")
       hexa.addObject('FixedProjectiveConstraint', indices="@fixedPointHexa.indices")
       hexa.addObject('FixedPlaneProjectiveConstraint', direction="0 0 1", dmin="-0.01", dmax="0.01")
       hexa.addObject('BoxROI', box="-0.2 -5.2 7.49 10.2 5.2 7.51", drawBoxes="1", name="pressurePlaneQuad")
       hexa.addObject('LineProjectiveConstraint', direction="1 0 0", origin="0 0 0", indices="4")
       hexa.addObject('QuadPressureForceField', showForces="1", quadList="@pressurePlaneQuad.quadIndices", pressure="0.00 0 -0.04")
       hexa.addObject('HexahedronFEMForceField', poissonRatio="0.45", youngModulus="1", method="polar")
    ```

