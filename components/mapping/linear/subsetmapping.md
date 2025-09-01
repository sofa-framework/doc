<!-- generate_doc -->
# SubsetMapping

Compute a subset of input DOFs.


## Rigid3d,Rigid3d

Templates:

- Rigid3d,Rigid3d

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
		<td>indices</td>
		<td>
list of input indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>first</td>
		<td>
first index (use if indices are sequential)
		</td>
		<td>4294967295</td>
	</tr>
	<tr>
		<td>last</td>
		<td>
last index (use if indices are sequential)
		</td>
		<td>4294967295</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
search radius to find corresponding points in case no indices are given
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>handleTopologyChange</td>
		<td>
Enable support of topological changes for indices (disable if it is linked from SubsetTopologicalMapping::pointD2S)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>ignoreNotFound</td>
		<td>
True to ignore points that are not found in the input model, they will be treated as fixed points
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>resizeToModel</td>
		<td>
True to resize the output MechanicalState to match the size of indices
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
|input|Input object to map|State&lt;Rigid3d&gt;|
|output|Output object to map|State&lt;Rigid3d&gt;|
|topology|link to the topology container|BaseMeshTopology|

<!-- generate_doc -->
## Vec1d,Vec1d

Templates:

- Vec1d,Vec1d

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
		<td>indices</td>
		<td>
list of input indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>first</td>
		<td>
first index (use if indices are sequential)
		</td>
		<td>4294967295</td>
	</tr>
	<tr>
		<td>last</td>
		<td>
last index (use if indices are sequential)
		</td>
		<td>4294967295</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
search radius to find corresponding points in case no indices are given
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>handleTopologyChange</td>
		<td>
Enable support of topological changes for indices (disable if it is linked from SubsetTopologicalMapping::pointD2S)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>ignoreNotFound</td>
		<td>
True to ignore points that are not found in the input model, they will be treated as fixed points
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>resizeToModel</td>
		<td>
True to resize the output MechanicalState to match the size of indices
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
|input|Input object to map|State&lt;Vec1d&gt;|
|output|Output object to map|State&lt;Vec1d&gt;|
|topology|link to the topology container|BaseMeshTopology|

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
		<td>indices</td>
		<td>
list of input indices
		</td>
		<td></td>
	</tr>
	<tr>
		<td>first</td>
		<td>
first index (use if indices are sequential)
		</td>
		<td>4294967295</td>
	</tr>
	<tr>
		<td>last</td>
		<td>
last index (use if indices are sequential)
		</td>
		<td>4294967295</td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
search radius to find corresponding points in case no indices are given
		</td>
		<td>1e-05</td>
	</tr>
	<tr>
		<td>handleTopologyChange</td>
		<td>
Enable support of topological changes for indices (disable if it is linked from SubsetTopologicalMapping::pointD2S)
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>ignoreNotFound</td>
		<td>
True to ignore points that are not found in the input model, they will be treated as fixed points
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>resizeToModel</td>
		<td>
True to resize the output MechanicalState to match the size of indices
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
|topology|link to the topology container|BaseMeshTopology|

## Examples 

SubsetMapping.scn

=== "XML"

    ```xml
    <!-- Mechanical SubsetMapping Group Basic Example -->
    <Node name="root" dt="0.01" gravity="0 -9.6 0">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [LocalMinDistance] -->
        <RequiredPlugin name="Sofa.Component.Collision.Geometry"/> <!-- Needed to use components [LineCollisionModel PointCollisionModel TriangleCollisionModel] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [IdentityMapping SubsetMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [TetrahedronSetGeometryAlgorithms TetrahedronSetTopologyContainer TetrahedronSetTopologyModifier TriangleSetGeometryAlgorithms TriangleSetTopologyContainer TriangleSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
        <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Hexa2TetraTopologicalMapping Tetra2TriangleTopologicalMapping] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
    
    
        <VisualStyle displayFlags="hideBehaviorModels hideCollisionModels hideBoundingCollisionModels hideForceFields showInteractionForceFields hideWireframe" />
        <CollisionPipeline depth="6" verbose="0" draw="0"/>
    	<BruteForceBroadPhase/>
        <BVHNarrowPhase/>
    	<LocalMinDistance name="Proximity"  alarmDistance="0.006" contactDistance="0.001" coneFactor="0.3" angleCone="0.01" filterIntersection="true"/>
    	<CollisionResponse name="Response" response="PenalityContactForceField"/>
    	<DefaultAnimationLoop/>
    
    	<Node name="sutureSoftCubes">
    		<EulerImplicitSolver name="TissueSolver" printLog="false" rayleighStiffness="0.3" rayleighMass="0.2"/>
    		<CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    		<MechanicalObject template="Vec3"/>
    		<UniformMass vertexMass="0.001"/>
    		<RegularGridTopology name="grid"
    				nx="10" ny="4" nz="10"
    				xmin="-0.05" xmax="0.05"
    				ymin="0.0" ymax="0.03"
    				zmin="-0.05" zmax="0.05"
    		/>
    		<!--<TetrahedronFEMForceField name="FEM" youngModulus="1e3" poissonRatio="0.4" computeGlobalMatrix="false" method="large"/>-->
    		<BoxROI name="box_roi" box="-0.06 -0.001 -0.06 0.06 0.001 0.06   -0.052 -0.001 -0.06 -0.048 0.011 0.06    0.048 -0.001 -0.06 0.052 0.011 0.06" />
    		<FixedProjectiveConstraint indices="@box_roi.indices" />
    
    		<Node name="subCube1">
    			<MechanicalObject template="Vec3"/>
    			<RegularGridTopology name="grid"
    				nx="5" ny="2" nz="10"
    				xmin="-0.05" xmax="-0.00555555555555555555555"
    				ymin="0.02" ymax="0.03"
    				zmin="-0.05" zmax="0.05"
    			/>
    			<HexahedronFEMForceField name="FEM" youngModulus="3e5" poissonRatio="0.4" method="large"/>
    			<SubsetMapping />
    			<Node name="Tetra1">
    				<TetrahedronSetTopologyContainer name="Container"/>
    				<TetrahedronSetTopologyModifier name="Modifier"/>
    				<TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo"/>
    				<Hexa2TetraTopologicalMapping input="@../grid" output="@Container"/>
    				<Node name="Visu1">
    					<TriangleSetTopologyContainer name="Container"/>
    					<TriangleSetTopologyModifier name="Modifier"/>
    					<TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo"/>
    					<Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" flipNormals="1" />
    <!-- 					<OglModel name="Visual" filename="mesh/suture.obj" putOnlyTexCoords="true"  dx="-0.055" material="texture Ambient 1 0.2 0.2 0.2 0.0 Diffuse 1 1.0 0.8 0.7 1.0 Specular 1 0.1 0.1 0.1 1.0 Emissive 0 0.15 0.05 0.05 0.0 Shininess 1 20" />
    					<OglShadowShader/>
    					<OglShaderDefineMacro id="USE_TEXTURE" />
    					<OglTexture2D id="colorTexture" texture2DFilename="textures/skin2.png" textureUnit="1" repeat="true" />
    					<BarycentricMapping input="@../.." output="@Visual"/>
    -->
    					<OglModel name="Visual1" color="0.3 1 0.3 1"/>
    					<IdentityMapping input="@../.." output="@Visual1"/>
    
    					<TriangleCollisionModel group="2" name="cube1_collis_tri"/>
    					<LineCollisionModel group="2"  name="cube1_collis_line"/>
    					<PointCollisionModel group="2" name="cube2_collis_point"/>
    				</Node>
    			</Node>
    		</Node>
    
    		<Node name="subCube2">
    			<MechanicalObject template="Vec3"/>
    			<RegularGridTopology name="grid"
    				nx="5" ny="2" nz="10"
    				xmin="0.00555555555555555555555" xmax="0.05"
    				ymin="0.02" ymax="0.03"
    				zmin="-0.05" zmax="0.05"
    			/>
    			<HexahedronFEMForceField name="FEM" youngModulus="3e5" poissonRatio="0.4" method="large"/>
    			<SubsetMapping />
    			<Node name="Tetra2">
    				<TetrahedronSetTopologyContainer name="Container"/>
    				<TetrahedronSetTopologyModifier name="Modifier"/>
    				<TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo"/>
    				<Hexa2TetraTopologicalMapping input="@../grid" output="@Container"/>
    				<Node name="Visu2">
    					<TriangleSetTopologyContainer name="Container"/>
    					<TriangleSetTopologyModifier name="Modifier"/>
    					<TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo"/>
    					<Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" flipNormals="1" />
    <!-- 					<OglModel name="Visual" filename="mesh/suture.obj" putOnlyTexCoords="true"  dx="0.00" material="texture Ambient 1 0.2 0.2 0.2 0.0 Diffuse 1 1.0 0.8 0.7 1.0 Specular 1 0.1 0.1 0.1 1.0 Emissive 0 0.15 0.05 0.05 0.0 Shininess 1 20" />
    					<OglShadowShader/>
    					<OglShaderDefineMacro id="USE_TEXTURE" />
    					<OglTexture2D id="colorTexture" texture2DFilename="textures/skin2.png" textureUnit="1" repeat="true" />
    					<BarycentricMapping input="@../.." output="@Visual"/>
     -->
    					<OglModel name="Visual2" color="0.3 0.3 1 1"/>
    					<IdentityMapping input="@../.." output="@Visual2"/>
    
    					<TriangleCollisionModel group="3" name="cube2_collis_tri"/>
    					<LineCollisionModel group="3"  name="cube2_collis_line"/>
    					<PointCollisionModel group="3" name="cube2_collis_point"/>
    				</Node>
    			</Node>
    		</Node>
    
    		<Node name="subCube3">
    			<MechanicalObject template="Vec3"/>
    			<RegularGridTopology name="grid"
    				nx="10" ny="3" nz="10"
    				xmin="-0.05" xmax="0.05"
    				ymin="0.0" ymax="0.02"
    				zmin="-0.05" zmax="0.05"
    			/>
    			<HexahedronFEMForceField name="FEM" youngModulus="2e3" poissonRatio="0.4" method="large"/>
    			<SubsetMapping />
    			<Node name="Tetra3">
    				<TetrahedronSetTopologyContainer name="Container"/>
    				<TetrahedronSetTopologyModifier name="Modifier"/>
    				<TetrahedronSetGeometryAlgorithms template="Vec3" name="GeomAlgo"/>
    				<Hexa2TetraTopologicalMapping input="@../grid" output="@Container"/>
    				<Node name="Visu3">
    					<TriangleSetTopologyContainer name="Container"/>
    					<TriangleSetTopologyModifier name="Modifier"/>
    					<TriangleSetGeometryAlgorithms template="Vec3" name="GeomAlgo"/>
    					<Tetra2TriangleTopologicalMapping input="@../Container" output="@Container" flipNormals="1" />
    					<OglModel name="Visual3" color="1 0.3 0.1 1"/>
    					<IdentityMapping input="@../.." output="@Visual3"/>
    				</Node>
    			</Node>
    		</Node>
    	</Node>
    
    
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", gravity="0 -9.6 0")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Geometry")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('VisualStyle', displayFlags="hideBehaviorModels hideCollisionModels hideBoundingCollisionModels hideForceFields showInteractionForceFields hideWireframe")
       root.addObject('CollisionPipeline', depth="6", verbose="0", draw="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('LocalMinDistance', name="Proximity", alarmDistance="0.006", contactDistance="0.001", coneFactor="0.3", angleCone="0.01", filterIntersection="true")
       root.addObject('CollisionResponse', name="Response", response="PenalityContactForceField")
       root.addObject('DefaultAnimationLoop', )

       suture_soft_cubes = root.addChild('sutureSoftCubes')

       suture_soft_cubes.addObject('EulerImplicitSolver', name="TissueSolver", printLog="false", rayleighStiffness="0.3", rayleighMass="0.2")
       suture_soft_cubes.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       suture_soft_cubes.addObject('MechanicalObject', template="Vec3")
       suture_soft_cubes.addObject('UniformMass', vertexMass="0.001")
       suture_soft_cubes.addObject('RegularGridTopology', name="grid", nx="10", ny="4", nz="10", xmin="-0.05", xmax="0.05", ymin="0.0", ymax="0.03", zmin="-0.05", zmax="0.05")
       suture_soft_cubes.addObject('BoxROI', name="box_roi", box="-0.06 -0.001 -0.06 0.06 0.001 0.06   -0.052 -0.001 -0.06 -0.048 0.011 0.06    0.048 -0.001 -0.06 0.052 0.011 0.06")
       suture_soft_cubes.addObject('FixedProjectiveConstraint', indices="@box_roi.indices")

       sub_cube1 = sutureSoftCubes.addChild('subCube1')

       sub_cube1.addObject('MechanicalObject', template="Vec3")
       sub_cube1.addObject('RegularGridTopology', name="grid", nx="5", ny="2", nz="10", xmin="-0.05", xmax="-0.00555555555555555555555", ymin="0.02", ymax="0.03", zmin="-0.05", zmax="0.05")
       sub_cube1.addObject('HexahedronFEMForceField', name="FEM", youngModulus="3e5", poissonRatio="0.4", method="large")
       sub_cube1.addObject('SubsetMapping', )

       tetra1 = subCube1.addChild('Tetra1')

       tetra1.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetra1.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetra1.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetra1.addObject('Hexa2TetraTopologicalMapping', input="@../grid", output="@Container")

       visu1 = Tetra1.addChild('Visu1')

       visu1.addObject('TriangleSetTopologyContainer', name="Container")
       visu1.addObject('TriangleSetTopologyModifier', name="Modifier")
       visu1.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       visu1.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container", flipNormals="1")
       visu1.addObject('OglModel', name="Visual1", color="0.3 1 0.3 1")
       visu1.addObject('IdentityMapping', input="@../..", output="@Visual1")
       visu1.addObject('TriangleCollisionModel', group="2", name="cube1_collis_tri")
       visu1.addObject('LineCollisionModel', group="2", name="cube1_collis_line")
       visu1.addObject('PointCollisionModel', group="2", name="cube2_collis_point")

       sub_cube2 = sutureSoftCubes.addChild('subCube2')

       sub_cube2.addObject('MechanicalObject', template="Vec3")
       sub_cube2.addObject('RegularGridTopology', name="grid", nx="5", ny="2", nz="10", xmin="0.00555555555555555555555", xmax="0.05", ymin="0.02", ymax="0.03", zmin="-0.05", zmax="0.05")
       sub_cube2.addObject('HexahedronFEMForceField', name="FEM", youngModulus="3e5", poissonRatio="0.4", method="large")
       sub_cube2.addObject('SubsetMapping', )

       tetra2 = subCube2.addChild('Tetra2')

       tetra2.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetra2.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetra2.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetra2.addObject('Hexa2TetraTopologicalMapping', input="@../grid", output="@Container")

       visu2 = Tetra2.addChild('Visu2')

       visu2.addObject('TriangleSetTopologyContainer', name="Container")
       visu2.addObject('TriangleSetTopologyModifier', name="Modifier")
       visu2.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       visu2.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container", flipNormals="1")
       visu2.addObject('OglModel', name="Visual2", color="0.3 0.3 1 1")
       visu2.addObject('IdentityMapping', input="@../..", output="@Visual2")
       visu2.addObject('TriangleCollisionModel', group="3", name="cube2_collis_tri")
       visu2.addObject('LineCollisionModel', group="3", name="cube2_collis_line")
       visu2.addObject('PointCollisionModel', group="3", name="cube2_collis_point")

       sub_cube3 = sutureSoftCubes.addChild('subCube3')

       sub_cube3.addObject('MechanicalObject', template="Vec3")
       sub_cube3.addObject('RegularGridTopology', name="grid", nx="10", ny="3", nz="10", xmin="-0.05", xmax="0.05", ymin="0.0", ymax="0.02", zmin="-0.05", zmax="0.05")
       sub_cube3.addObject('HexahedronFEMForceField', name="FEM", youngModulus="2e3", poissonRatio="0.4", method="large")
       sub_cube3.addObject('SubsetMapping', )

       tetra3 = subCube3.addChild('Tetra3')

       tetra3.addObject('TetrahedronSetTopologyContainer', name="Container")
       tetra3.addObject('TetrahedronSetTopologyModifier', name="Modifier")
       tetra3.addObject('TetrahedronSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       tetra3.addObject('Hexa2TetraTopologicalMapping', input="@../grid", output="@Container")

       visu3 = Tetra3.addChild('Visu3')

       visu3.addObject('TriangleSetTopologyContainer', name="Container")
       visu3.addObject('TriangleSetTopologyModifier', name="Modifier")
       visu3.addObject('TriangleSetGeometryAlgorithms', template="Vec3", name="GeomAlgo")
       visu3.addObject('Tetra2TriangleTopologicalMapping', input="@../Container", output="@Container", flipNormals="1")
       visu3.addObject('OglModel', name="Visual3", color="1 0.3 0.1 1")
       visu3.addObject('IdentityMapping', input="@../..", output="@Visual3")
    ```

