<!-- generate_doc -->
# MergePoints

Merge 2 coordinate vectors.


Templates:

- Rigid2d
- Rigid3d
- Vec1d
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
		<td>noUpdate</td>
		<td>
do not update the output at each time step (false)
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td colspan="3">Inputs</td>
	</tr>
	<tr>
		<td>position1</td>
		<td>
position coordinates of the degrees of freedom of the first object
		</td>
		<td></td>
	</tr>
	<tr>
		<td>position2</td>
		<td>
Rest position coordinates of the degrees of freedom of the second object
		</td>
		<td></td>
	</tr>
	<tr>
		<td>mappingX2</td>
		<td>
Mapping of indices to inject position2 inside position1 vertex buffer
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Outputs</td>
	</tr>
	<tr>
		<td>indices1</td>
		<td>
Indices of the points of the first object
		</td>
		<td></td>
	</tr>
	<tr>
		<td>indices2</td>
		<td>
Indices of the points of the second object
		</td>
		<td></td>
	</tr>
	<tr>
		<td>points</td>
		<td>
position coordinates resulting from the merge
		</td>
		<td></td>
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

MergePoints.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    <Node name="root" dt="0.05" showBoundingTree="0" gravity="0 -9 1">
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Algorithm"/> <!-- Needed to use components [BVHNarrowPhase BruteForceBroadPhase CollisionPipeline] -->
        <RequiredPlugin name="Sofa.Component.Collision.Detection.Intersection"/> <!-- Needed to use components [MinProximityIntersection] -->
        <RequiredPlugin name="Sofa.Component.Collision.Response.Contact"/> <!-- Needed to use components [CollisionResponse] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Lagrangian.Correction"/> <!-- Needed to use components [UncoupledConstraintCorrection] -->
        <RequiredPlugin name="Sofa.Component.Constraint.Projective"/> <!-- Needed to use components [FixedProjectiveConstraint] -->
        <RequiredPlugin name="Sofa.Component.Engine.Generate"/> <!-- Needed to use components [MergePoints] -->
        <RequiredPlugin name="Sofa.Component.Engine.Select"/> <!-- Needed to use components [BoxROI SubsetTopology] -->
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [MeshOBJLoader] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Iterative"/> <!-- Needed to use components [CGLinearSolver] -->
        <RequiredPlugin name="Sofa.Component.Mapping.Linear"/> <!-- Needed to use components [BarycentricMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [UniformMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.FEM.Elastic"/> <!-- Needed to use components [HexahedronFEMForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [QuadSetGeometryAlgorithms QuadSetTopologyContainer QuadSetTopologyModifier] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Grid"/> <!-- Needed to use components [SparseGridRamificationTopology] -->
        <RequiredPlugin name="Sofa.Component.Visual"/> <!-- Needed to use components [VisualStyle] -->
        <RequiredPlugin name="Sofa.GL.Component.Rendering3D"/> <!-- Needed to use components [OglModel] -->
        <RequiredPlugin name="Sofa.GL.Component.Shader"/> <!-- Needed to use components [LightManager SpotLight] -->
        
        <DefaultAnimationLoop/>
        <VisualStyle displayFlags="showVisual showBehaviorModels" />
        <CollisionPipeline verbose="0" />
        <BruteForceBroadPhase/>
        <BVHNarrowPhase/>
        <CollisionResponse response="PenalityContactForceField" />
        <MinProximityIntersection name="Proximity" alarmDistance="0.8" contactDistance="0.5" />
        
        <LightManager />
        <SpotLight name="light1" color="1 1 1" position="0 80 25" direction="0 -1 -0.8" cutoff="30" exponent="1" />
        <SpotLight name="light2" color="1 1 1" position="0 40 100" direction="0 0 -1" cutoff="30" exponent="1" />
        
        <Node name="mesh">
    		<MeshOBJLoader name="meshLoader" filename="mesh/raptor_35kp.obj"/>  
    		<SubsetTopology template="Vec3" name="subset_head" box="-2 4 4 2 8 8" drawROI="1" src="@meshLoader" rest_position="@meshLoader.position" localIndices="1"/>
    		
    		<Node name="simu_head">
    			<EulerImplicitSolver name="cg_odesolver" printLog="false"  rayleighStiffness="0.1" rayleighMass="0.1" />
    			<CGLinearSolver iterations="25" name="linear solver" tolerance="1.0e-9" threshold="1.0e-9" />
    			<SparseGridRamificationTopology position="@../subset_head.pointsInROI" n="10 10 10" nbVirtualFinerLevels="0" finestConnectivity="0" />			
    			<MechanicalObject template="Vec3" name="mecaObj2"  />
    			<BoxConstraint box="-2 4 4 2 8 4.5" drawBoxes="0"/>
    			<UniformMass totalMass="50.0" />
                <HexahedronFEMForceField name="FEM" youngModulus="4000.0" poissonRatio="0.30" method="large" updateStiffnessMatrix="false" printLog="0" 
                drawing="1"/>            
                <UncoupledConstraintCorrection defaultCompliance="0.05"/>
                
                <Node name="Visu">	
    				<QuadSetTopologyContainer  name="Container" 
    					position="@../../subset_head.pointsInROI"
    					quads="@../../subset_head.quadsInROI"
    					 />
    				<QuadSetTopologyModifier   name="Modifier" />
    				<QuadSetGeometryAlgorithms name="GeomAlgo"   template="Vec3" drawEdges="0" />		                    
    				<MechanicalObject name="CollisModel" />
    				<BarycentricMapping input="@.." output="@CollisModel" />
    			</Node>  
    		</Node>
            
       		<MergePoints template="Vec3" name="merge_subsets" position1="@meshLoader.position"
    			position2="@simu_head/Visu/CollisModel.position" mappingX2="@subset_head.indices"/>
    
           <Node>
    			<OglModel name="Visual" position="@../merge_subsets.points" 
    				src="@../meshLoader" texturename="textures/snakeskin.png" scaleTex="20 20"/>
    		</Node>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', dt="0.05", showBoundingTree="0", gravity="0 -9 1")

       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Algorithm")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Detection.Intersection")
       root.addObject('RequiredPlugin', name="Sofa.Component.Collision.Response.Contact")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Lagrangian.Correction")
       root.addObject('RequiredPlugin', name="Sofa.Component.Constraint.Projective")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Generate")
       root.addObject('RequiredPlugin', name="Sofa.Component.Engine.Select")
       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Iterative")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.Linear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.FEM.Elastic")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Grid")
       root.addObject('RequiredPlugin', name="Sofa.Component.Visual")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Rendering3D")
       root.addObject('RequiredPlugin', name="Sofa.GL.Component.Shader")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('VisualStyle', displayFlags="showVisual showBehaviorModels")
       root.addObject('CollisionPipeline', verbose="0")
       root.addObject('BruteForceBroadPhase', )
       root.addObject('BVHNarrowPhase', )
       root.addObject('CollisionResponse', response="PenalityContactForceField")
       root.addObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
       root.addObject('LightManager', )
       root.addObject('SpotLight', name="light1", color="1 1 1", position="0 80 25", direction="0 -1 -0.8", cutoff="30", exponent="1")
       root.addObject('SpotLight', name="light2", color="1 1 1", position="0 40 100", direction="0 0 -1", cutoff="30", exponent="1")

       mesh = root.addChild('mesh')

       mesh.addObject('MeshOBJLoader', name="meshLoader", filename="mesh/raptor_35kp.obj")
       mesh.addObject('SubsetTopology', template="Vec3", name="subset_head", box="-2 4 4 2 8 8", drawROI="1", src="@meshLoader", rest_position="@meshLoader.position", localIndices="1")

       simu_head = mesh.addChild('simu_head')

       simu_head.addObject('EulerImplicitSolver', name="cg_odesolver", printLog="false", rayleighStiffness="0.1", rayleighMass="0.1")
       simu_head.addObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
       simu_head.addObject('SparseGridRamificationTopology', position="@../subset_head.pointsInROI", n="10 10 10", nbVirtualFinerLevels="0", finestConnectivity="0")
       simu_head.addObject('MechanicalObject', template="Vec3", name="mecaObj2")
       simu_head.addObject('BoxConstraint', box="-2 4 4 2 8 4.5", drawBoxes="0")
       simu_head.addObject('UniformMass', totalMass="50.0")
       simu_head.addObject('HexahedronFEMForceField', name="FEM", youngModulus="4000.0", poissonRatio="0.30", method="large", updateStiffnessMatrix="false", printLog="0", drawing="1")
       simu_head.addObject('UncoupledConstraintCorrection', defaultCompliance="0.05")

       visu = simu_head.addChild('Visu')

       visu.addObject('QuadSetTopologyContainer', name="Container", position="@../../subset_head.pointsInROI", quads="@../../subset_head.quadsInROI")
       visu.addObject('QuadSetTopologyModifier', name="Modifier")
       visu.addObject('QuadSetGeometryAlgorithms', name="GeomAlgo", template="Vec3", drawEdges="0")
       visu.addObject('MechanicalObject', name="CollisModel")
       visu.addObject('BarycentricMapping', input="@..", output="@CollisModel")

       mesh.addObject('MergePoints', template="Vec3", name="merge_subsets", position1="@meshLoader.position", position2="@simu_head/Visu/CollisModel.position", mappingX2="@subset_head.indices")

       node = mesh.addChild('node')

       node.addObject('OglModel', name="Visual", position="@../merge_subsets.points", src="@../meshLoader", texturename="textures/snakeskin.png", scaleTex="20 20")
    ```

