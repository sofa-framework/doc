<!-- generate_doc -->
# SPHFluidSurfaceMapping

Mapping the surface of a Smooth Particle Hydrodynamics model.


## Vec3d,Vec3d

Templates:

- Vec3d,Vec3d

__Target__: SofaSphFluid

__namespace__: sofa::component::mapping

__parents__:

- Mapping
- MeshTopology

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
		<td>filename</td>
		<td>
Filename of the mesh
		</td>
		<td></td>
	</tr>
	<tr>
		<td>position</td>
		<td>
List of point positions
		</td>
		<td></td>
	</tr>
	<tr>
		<td>edges</td>
		<td>
List of edge indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>triangles</td>
		<td>
List of triangle indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>quads</td>
		<td>
List of quad indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>tetrahedra</td>
		<td>
List of tetrahedron indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>hexahedra</td>
		<td>
List of hexahedron indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>uv</td>
		<td>
List of uv coordinates
		</td>
		<td></td>
	</tr>
	<tr>
		<td>computeAllBuffers</td>
		<td>
Option to compute all crossed topology buffers at init. False by default
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>step</td>
		<td>
Step
		</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Radius
		</td>
		<td>2</td>
	</tr>
	<tr>
		<td>isoValue</td>
		<td>
Iso Value
		</td>
		<td>0.5</td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>drawEdges</td>
		<td>
if true, draw the topology Edges
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTriangles</td>
		<td>
if true, draw the topology Triangles
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawQuads</td>
		<td>
if true, draw the topology Quads
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawTetrahedra</td>
		<td>
if true, draw the topology Tetrahedra
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>drawHexahedra</td>
		<td>
if true, draw the topology hexahedra
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

## Examples 

SPHFluidSurfaceMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node dt="0.01" gravity="0 -10 0">
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.MechanicalLoad"/> <!-- Needed to use components [PlaneForceField] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="SofaSphFluid"/> <!-- Needed to use components [SPHFluidForceField SPHFluidSurfaceMapping SpatialGridContainer] -->
    
        <VisualStyle displayFlags="hideBehaviorModels showForceFields hideCollisionModels" />
        <DefaultAnimationLoop/>    
        <Node name="SPHSurfaceMapping">
            <EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
            
            <RegularGridTopology nx="5" ny="40" nz="5" xmin="-1.5" xmax="0" ymin="-3" ymax="12" zmin="-1.5" zmax="0" drawEdges="0"/>
            <MechanicalObject name="MModel" />
            <UniformMass name="M1" vertexMass="1" />
            <SpatialGridContainer cellWidth="0.75"/>
            <SPHFluidForceField radius="0.745" density="15" kernelType="1" viscosityType="2" viscosity="10" pressure="1500" surfaceTension="-1000" printLog="0" />
            
            <PlaneForceField normal="1 0 0" d="-4" showPlane="1"/>
            <PlaneForceField normal="-1 0 0" d="-14" showPlane="1"/>
            <PlaneForceField normal="0.3 1 0" d="-4" showPlane="1"/>
            <PlaneForceField normal="0 0 1" d="-4" showPlane="1"/>
            <PlaneForceField normal="0 0 -1" d="-4" showPlane="1"/>
            
            <Node id="Visual">
                <OglModel name="VModel" color="blue" />
                <SPHFluidSurfaceMapping name="MarchingCube" input="@../MModel" output="@VModel" isoValue="0.5" radius="0.75" step="0.25" />
            </Node>
        </Node>
        
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       node = root_node.addChild('node', dt="0.01", gravity="0 -10 0")

       node.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       node.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       node.addObject('RequiredPlugin', name="Sofa.Component.MechanicalLoad")
       node.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       node.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       node.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       node.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       node.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       node.addObject('RequiredPlugin', name="SofaSphFluid")
       node.addObject('VisualStyle', displayFlags="hideBehaviorModels showForceFields hideCollisionModels")
       node.addObject('DefaultAnimationLoop', )

       sph_surface_mapping = node.addChild('SPHSurfaceMapping')

       sph_surface_mapping.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       sph_surface_mapping.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       sph_surface_mapping.addObject('RegularGridTopology', nx="5", ny="40", nz="5", xmin="-1.5", xmax="0", ymin="-3", ymax="12", zmin="-1.5", zmax="0", drawEdges="0")
       sph_surface_mapping.addObject('MechanicalObject', name="MModel")
       sph_surface_mapping.addObject('UniformMass', name="M1", vertexMass="1")
       sph_surface_mapping.addObject('SpatialGridContainer', cellWidth="0.75")
       sph_surface_mapping.addObject('SPHFluidForceField', radius="0.745", density="15", kernelType="1", viscosityType="2", viscosity="10", pressure="1500", surfaceTension="-1000", printLog="0")
       sph_surface_mapping.addObject('PlaneForceField', normal="1 0 0", d="-4", showPlane="1")
       sph_surface_mapping.addObject('PlaneForceField', normal="-1 0 0", d="-14", showPlane="1")
       sph_surface_mapping.addObject('PlaneForceField', normal="0.3 1 0", d="-4", showPlane="1")
       sph_surface_mapping.addObject('PlaneForceField', normal="0 0 1", d="-4", showPlane="1")
       sph_surface_mapping.addObject('PlaneForceField', normal="0 0 -1", d="-4", showPlane="1")

       node = SPHSurfaceMapping.addChild('node', id="Visual")

       node.addObject('OglModel', name="VModel", color="blue")
       node.addObject('SPHFluidSurfaceMapping', name="MarchingCube", input="@../MModel", output="@VModel", isoValue="0.5", radius="0.75", step="0.25")
    ```

