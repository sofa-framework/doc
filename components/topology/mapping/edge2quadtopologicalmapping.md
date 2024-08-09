<!-- generate_doc -->
# Edge2QuadTopologicalMapping

Special case of mapping where EdgeSetTopology is converted to QuadSetTopology.


__Target__: Sofa.Component.Topology.Mapping

__namespace__: sofa::component::topology::mapping

__parents__:

- TopologicalMapping

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
		<td>nbPointsOnEachCircle</td>
		<td>
Discretization of created circles
		</td>
		<td></td>
	</tr>
	<tr>
		<td>radius</td>
		<td>
Radius of created circles in yz plan
		</td>
		<td>1</td>
	</tr>
	<tr>
		<td>radiusFocal</td>
		<td>
If greater than 0., radius in focal axis of created ellipses
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>focalAxis</td>
		<td>
In case of ellipses
		</td>
		<td>0 0 1</td>
	</tr>
	<tr>
		<td>edgeList</td>
		<td>
list of input edges for the topological mapping: by default, all considered
		</td>
		<td></td>
	</tr>
	<tr>
		<td>flipNormals</td>
		<td>
Flip Normal ? (Inverse point order when creating quad)
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
|input|Input topology to map|BaseMeshTopology|
|output|Output topology to map|BaseMeshTopology|
|toQuadContainer|Output container storing Quads|QuadSetTopologyContainer|
|toQuadModifier|Output modifier handling Quads|QuadSetTopologyModifier|

## Examples 

Edge2QuadTopologicalMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.01" showBoundingTree="0" gravity="0 -9 0">
        <Node name="RequiredPlugins">
            <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
            <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
            <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
            <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
            <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
            <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [TubularMapping] -->
            <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
            <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
            <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [BeamFEMForceField] -->
            <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [QuadSetGeometryAlgorithms QuadSetTopologyContainer QuadSetTopologyModifier] -->
            <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [RegularGridTopology] -->
            <RequiredPlugin name="Sofa.Component.Topology.Mapping"/> <!-- Needed to use components [Edge2QuadTopologicalMapping] -->
            <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        </Node>
    
        <DefaultAnimationLoop />
        <CollisionPipeline />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.5" contactDistance="0.02"/>
    
       	<Node name="Beam">
            <EulerImplicitSolver  rayleighStiffness="0.1" rayleighMass="0.1" />
            <CGLinearSolver iterations="125" tolerance="1e-16" threshold="1e-16" />
    
            <RegularGridTopology name="MeshLines" nx="100" ny="1" nz="1" xmax="100" xmin="0" ymin="0" ymax="0" zmax="0" zmin="0"/>
    		<MechanicalObject template="Rigid3" name="BeamDof" />
    		<FixedProjectiveConstraint name="fix" indices="0" />
            <UniformMass totalMass="0.1" />
            <BeamFEMForceField name="BeamFEM" radius="1.0" youngModulus="1000" poissonRatio="0.45" />
            
            
            <Node name="VisuBeam" activated="true">
    			<OglModel template="Vec3" name="SurfDof" color="0.7 0.7 0.7" />
    			<QuadSetTopologyContainer  name="Container" />
    			<QuadSetTopologyModifier   name="Modifier" />
                <QuadSetGeometryAlgorithms name="GeomAlgo"  template="Vec3" drawQuads="1"/>
    			<Edge2QuadTopologicalMapping nbPointsOnEachCircle="10" radius="2" input="@../MeshLines" output="@Container" flipNormals="true"/>
                <TubularMapping nbPointsOnEachCircle="10" radius="2" input="@../BeamDof" output="@SurfDof" />
                
    		</Node>
    	</Node>  
    </Node>
    

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.01", showBoundingTree="0", gravity="0 -9 0")

       required_plugins = root.addChild('RequiredPlugins')

       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       required_plugins.addObject('RequiredPlugin', name="Sofa.Component.Topology.Mapping")
       required_plugins.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")

       root.addObject('DefaultAnimationLoop', )
       root.addObject('CollisionPipeline', )
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.5", contactDistance="0.02")

       beam = root.addChild('Beam')

       beam.addObject('EulerImplicitSolver', rayleighStiffness="0.1", rayleighMass="0.1")
       beam.addObject('CGLinearSolver', iterations="125", tolerance="1e-16", threshold="1e-16")
       beam.addObject('RegularGridTopology', name="MeshLines", nx="100", ny="1", nz="1", xmax="100", xmin="0", ymin="0", ymax="0", zmax="0", zmin="0")
       beam.addObject('MechanicalObject', template="Rigid3", name="BeamDof")
       beam.addObject('FixedProjectiveConstraint', name="fix", indices="0")
       beam.addObject('UniformMass', totalMass="0.1")
       beam.addObject('BeamFEMForceField', name="BeamFEM", radius="1.0", youngModulus="1000", poissonRatio="0.45")

       visu_beam = Beam.addChild('VisuBeam', activated="true")

       visu_beam.addObject('OglModel', template="Vec3", name="SurfDof", color="0.7 0.7 0.7")
       visu_beam.addObject('QuadSetTopologyContainer', name="Container")
       visu_beam.addObject('QuadSetTopologyModifier', name="Modifier")
       visu_beam.addObject('QuadSetGeometryAlgorithms', name="GeomAlgo", template="Vec3", drawQuads="1")
       visu_beam.addObject('Edge2QuadTopologicalMapping', nbPointsOnEachCircle="10", radius="2", input="@../MeshLines", output="@Container", flipNormals="true")
       visu_beam.addObject('TubularMapping', nbPointsOnEachCircle="10", radius="2", input="@../BeamDof", output="@SurfDof")
    ```

