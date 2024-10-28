<!-- generate_doc -->
# DistanceFromTargetMapping

Mapping point positions to distances from target points.


## Rigid3d,Vec1d

Templates:

- Rigid3d,Vec1d

__Target__: Sofa.Component.Mapping.NonLinear

__namespace__: sofa::component::mapping::nonlinear

__parents__:

- BaseNonLinearMapping

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
		<td>geometricStiffness</td>
		<td>
Method used to compute the geometric stiffness:
-None: geometric stiffness is not computed
-Exact: the exact geometric stiffness is computed
-Stabilized: the exact geometric stiffness is approximated in order to improve stability
		</td>
		<td>Stabilized</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the parent points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>targetPositions</td>
		<td>
Positions to compute the distances from
		</td>
		<td></td>
	</tr>
	<tr>
		<td>restLengths</td>
		<td>
Rest lengths of the connections
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showObjectScale</td>
		<td>
Scale for object display
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showColor</td>
		<td>
Color for object display.
		</td>
		<td>1 1 0 1</td>
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
|output|Output object to map|State&lt;Vec1d&gt;|

<!-- generate_doc -->
## Vec1d,Vec1d

Templates:

- Vec1d,Vec1d

__Target__: Sofa.Component.Mapping.NonLinear

__namespace__: sofa::component::mapping::nonlinear

__parents__:

- BaseNonLinearMapping

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
		<td>geometricStiffness</td>
		<td>
Method used to compute the geometric stiffness:
-None: geometric stiffness is not computed
-Exact: the exact geometric stiffness is computed
-Stabilized: the exact geometric stiffness is approximated in order to improve stability
		</td>
		<td>Stabilized</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the parent points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>targetPositions</td>
		<td>
Positions to compute the distances from
		</td>
		<td></td>
	</tr>
	<tr>
		<td>restLengths</td>
		<td>
Rest lengths of the connections
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showObjectScale</td>
		<td>
Scale for object display
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showColor</td>
		<td>
Color for object display.
		</td>
		<td>1 1 0 1</td>
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

<!-- generate_doc -->
## Vec3d,Vec1d

Templates:

- Vec3d,Vec1d

__Target__: Sofa.Component.Mapping.NonLinear

__namespace__: sofa::component::mapping::nonlinear

__parents__:

- BaseNonLinearMapping

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
		<td>geometricStiffness</td>
		<td>
Method used to compute the geometric stiffness:
-None: geometric stiffness is not computed
-Exact: the exact geometric stiffness is computed
-Stabilized: the exact geometric stiffness is approximated in order to improve stability
		</td>
		<td>Stabilized</td>
	</tr>
	<tr>
		<td>indices</td>
		<td>
Indices of the parent points
		</td>
		<td></td>
	</tr>
	<tr>
		<td>targetPositions</td>
		<td>
Positions to compute the distances from
		</td>
		<td></td>
	</tr>
	<tr>
		<td>restLengths</td>
		<td>
Rest lengths of the connections
		</td>
		<td></td>
	</tr>
	<tr>
		<td colspan="3">Visualization</td>
	</tr>
	<tr>
		<td>showObjectScale</td>
		<td>
Scale for object display
		</td>
		<td>0</td>
	</tr>
	<tr>
		<td>showColor</td>
		<td>
Color for object display.
		</td>
		<td>1 1 0 1</td>
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

## Examples 

DistanceFromTargetMapping.scn

=== "XML"

    ```xml
    <?xml version="1.0"?>
    <Node name="root" gravity="0 -9.81 0" dt="0.01">
        <RequiredPlugin name="Sofa.Component.IO.Mesh"/> <!-- Needed to use components [StringMeshCreator] -->
        <RequiredPlugin name="Sofa.Component.LinearSolver.Direct"/> <!-- Needed to use components [EigenSimplicialLLT] -->
        <RequiredPlugin name="Sofa.Component.Mapping.NonLinear"/> <!-- Needed to use components [DistanceFromTargetMapping DistanceMapping] -->
        <RequiredPlugin name="Sofa.Component.Mass"/> <!-- Needed to use components [DiagonalMass] -->
        <RequiredPlugin name="Sofa.Component.ODESolver.Backward"/> <!-- Needed to use components [EulerImplicitSolver] -->
        <RequiredPlugin name="Sofa.Component.SolidMechanics.Spring"/> <!-- Needed to use components [RestShapeSpringsForceField] -->
        <RequiredPlugin name="Sofa.Component.StateContainer"/> <!-- Needed to use components [MechanicalObject] -->
        <RequiredPlugin name="Sofa.Component.Topology.Container.Dynamic"/> <!-- Needed to use components [EdgeSetGeometryAlgorithms EdgeSetTopologyContainer] -->
    
        <DefaultAnimationLoop/>
        <DefaultVisualManagerLoop/>
    
        <StringMeshCreator name="loader" resolution="20" scale3d="1 1 1" />
    
        <EulerImplicitSolver />
        <EigenSimplicialLLT />
    
        <EdgeSetTopologyContainer name="topology" position="@loader.position" edges="@loader.edges"/>
        <MechanicalObject name="dofs" template="Vec3" />
        <EdgeSetGeometryAlgorithms drawEdges="true" />
        <DiagonalMass name="mass" totalMass="1e-3"/>
        <Node name="attach">
            <MechanicalObject template="Vec1"/>
            <DistanceFromTargetMapping indices="0" targetPositions="0 0 0"/>
            <RestShapeSpringsForceField/>
        </Node>
        <Node name="extensionsNode" >
            <MechanicalObject template="Vec1"  name="extensionsDOF" />
            <DistanceMapping  name="distanceMapping" topology="@../topology"/>
            <RestShapeSpringsForceField/>
        </Node>
    </Node>

    ```

=== "Python"

    ```python
    def createScene(root_node):

       root = root_node.addChild('root', gravity="0 -9.81 0", dt="0.01")

       root.addObject('RequiredPlugin', name="Sofa.Component.IO.Mesh")
       root.addObject('RequiredPlugin', name="Sofa.Component.LinearSolver.Direct")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mapping.NonLinear")
       root.addObject('RequiredPlugin', name="Sofa.Component.Mass")
       root.addObject('RequiredPlugin', name="Sofa.Component.ODESolver.Backward")
       root.addObject('RequiredPlugin', name="Sofa.Component.SolidMechanics.Spring")
       root.addObject('RequiredPlugin', name="Sofa.Component.StateContainer")
       root.addObject('RequiredPlugin', name="Sofa.Component.Topology.Container.Dynamic")
       root.addObject('DefaultAnimationLoop', )
       root.addObject('DefaultVisualManagerLoop', )
       root.addObject('StringMeshCreator', name="loader", resolution="20", scale3d="1 1 1")
       root.addObject('EulerImplicitSolver', )
       root.addObject('EigenSimplicialLLT', )
       root.addObject('EdgeSetTopologyContainer', name="topology", position="@loader.position", edges="@loader.edges")
       root.addObject('MechanicalObject', name="dofs", template="Vec3")
       root.addObject('EdgeSetGeometryAlgorithms', drawEdges="true")
       root.addObject('DiagonalMass', name="mass", totalMass="1e-3")

       attach = root.addChild('attach')

       attach.addObject('MechanicalObject', template="Vec1")
       attach.addObject('DistanceFromTargetMapping', indices="0", targetPositions="0 0 0")
       attach.addObject('RestShapeSpringsForceField', )

       extensions_node = root.addChild('extensionsNode')

       extensions_node.addObject('MechanicalObject', template="Vec1", name="extensionsDOF")
       extensions_node.addObject('DistanceMapping', name="distanceMapping", topology="@../topology")
       extensions_node.addObject('RestShapeSpringsForceField', )
    ```

