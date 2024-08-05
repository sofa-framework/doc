# ParallelBruteForceBroadPhase

Collision detection using extensive pair-wise tests performed in parallel


__Target__: `MultiThreading`

__namespace__: `#!c++ multithreading::component::collision::detection::algorithm`

__parents__: 

- `#!c++ BruteForceBroadPhase`

__categories__: 

- CollisionAlgorithm

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
		<td>box</td>
		<td>
if not empty, objects that do not intersect this bounding-box will be ignored
</td>
		<td></td>
	</tr>
	<tr>
		<td>nbThreads</td>
		<td>
If not yet initialized, the main task scheduler is initialized with this number of threads. 0 corresponds to the number of available cores on the CPU. -n (minus) corresponds to the number of available cores on the CPU minus the provided number.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>taskSchedulerType</td>
		<td>
Type of task scheduler to use.
</td>
		<td>_default</td>
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

MultiThreading/share/sofa/examples/MultiThreading/ParallelBruteForceBroadPhase.scn

=== "XML"

    ```xml
    <?xml version="1.0" ?>
    
    <!--
    ParallelBruteForceBroadPhase is interesting when there are many objects potentially in collision.
    This scene has 72 cubes and a floor.
    Each cube has a TriangleCollisionModel, a LineCollisionModel and a PointCollisionModel.
    The floor has only a TriangleCollisionModel.
    It results in n = 72*3 + 1 = 217 collision models.
    It makes n*(n-1)/2 = 23436 pairs of collision models to test.
    On a CPU with 6 cores, each core tests 3906 pairs of collision models.
    -->
    
    
    <Node name="root" dt="0.01" gravity="0 -9.81 0">
        <Node name="pluginList" />
        </Node>
    
    
        <VisualStyle displayFlags="showBehavior showCollisionModels" />
        <OglSceneFrame/>
    
        <!-- Basic Components to perform the collision detection -->
        <FreeMotionAnimationLoop name="FreeMotionAnimationLoop" parallelODESolving="true" />
        <CollisionPipeline name="CollisionPipeline" />
    
        <ParallelBruteForceBroadPhase/>
        <ParallelBVHNarrowPhase/>
    
    <!--    <BruteForceBroadPhase/>-->
    <!--    <BVHNarrowPhase/>-->
    
        <NewProximityIntersection name="Proximity" alarmDistance="0.2" contactDistance="0.09" angleCone="0.0" />
        <CollisionResponse name="Response" response="FrictionContactConstraint" />
        <LCPConstraintSolver maxIt="1000" tolerance="0.001"/>
        <!-- Using a rigid cube using collision triangles, lines and points  -->
    
        <Node name="grid0">
    
            <OglLabel label="72 cubes" selectContrastingColor="true"/>
            <Node name="Cube0">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.74819886067333 0.13000773132313 0.93028979372712" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube1">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="4.3804729733991 0.77457089385696 0.27803373722268" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube2">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.8670557578407 0.72764094440622 0.57778551223585" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube3">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.52166113561097 5.0046672055054 0.10088881528978" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube4">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="3.9450474625663 5.2738956775395 0.89534907690033" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube5">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.305407303062 4.5237374729587 0.39064753911954" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube6">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.071737911119935 9.523777224833 0.58510420731507" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube7">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="4.0065867209372 9.9413022501121 0.37843590061107" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube8">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.2205059766865 9.1447510035451 0.6489813419287" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube9">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.45521484057196 13.636816443939 0.34713000261557" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube10">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="3.7994200369806 13.985573250561 0.064533073019485" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube11">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.7237247050385 13.884293768268 0.63587171194883" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube12">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.93478864614609 18.345891356164 0.70599745712522" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube13">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="4.321946673478 18.265142549884 0.52448542440519" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube14">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.2815712151497 18.894561551928 0.31266520419748" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube15">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.3549315493344 23.275718517963 0.24514779459925" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube16">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="3.5063231964625 23.236317592085 0.37010838993364" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube17">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.9298104769223 23.441940895255 0.67634991681033" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube18">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.95332908441933 0.36214441310714 3.8638965107332" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube19">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="3.8713179339521 0.72825660031673 4.4170562354462" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube20">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.3623172698367 0.42303866540223 4.2916329795456" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube21">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.41599076540023 5.011850300949 4.0764630770201" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube22">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="4.1831578415274 4.5458585773808 3.657553949001" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube23">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.3023503712855 5.2596857597864 4.4541927831965" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube24">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.76817353431516 9.4053872043292 3.9015833886348" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube25">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="4.2292593758224 9.1146520563004 3.6763078310417" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube26">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.0779307592092 9.5021445925823 3.5487861833762" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube27">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.95456032825381 14.079579005753 3.9779275546213" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube28">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="3.523460344888 14.072634430869 3.847393618127" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube29">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.147231008926 14.275786010444 4.385838838241" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube30">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.033113344587904 18.947797390142 3.5628156732129" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube31">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="4.1209282542676 18.712580375705 4.1972367044991" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube32">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.4567343417819 18.837116944528 3.9945605623045" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube33">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.45280707555488 22.736685181612 3.6824013070121" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube34">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="4.2000142329838 22.655285063272 4.4546194779475" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube35">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.2545063110322 23.301119732578 3.7903861488637" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube36">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.15341132886401 0.16820048083002 7.5094929363157" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube37">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="3.8576176000562 0.53452356138012 7.1683901088165" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube38">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.0715503013095 0.51248217444517 7.0173420589498" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube39">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.25969415216692 5.333801087846 7.2361134994943" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube40">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="4.0694888157628 5.1161159149446 7.6208188285217" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube41">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.5960498701763 4.9855055615704 7.3799518441688" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube42">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.76430473093144 9.6086890309158 7.0650074975868" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube43">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="3.8057373828747 9.1482642410082 7.4258274763943" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube44">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.5454184466719 9.4156656071617 7.6357635323125" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube45">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.27177981393029 13.737715651392 7.6596358635741" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube46">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="4.3768386486344 14.108665051688 7.9202950656974" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube47">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.6850976271951 13.885693371941 7.6036874165776" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube48">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.73397222474868 18.105128143497 7.5915422609968" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube49">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="3.5186291742225 18.128789600045 7.3756774833313" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube50">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.1199427680671 18.613336643955 7.5970546564074" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube51">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.87562178442051 23.386319402552 7.7875950596238" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube52">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="4.0230774183399 22.973699588549 7.3888650198415" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube53">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.1893345374564 23.204612573006 7.9542482183102" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube54">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.70143965198725 0.46208797370181 11.339157561231" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube55">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="3.5612233099813 0.76873835118894 10.7542899946" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube56">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.8808409226503 0.47441122283899 10.761158771935" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube57">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.20105870682795 5.2240685013701 11.228900610343" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube58">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="3.7781574303648 5.1834110597537 11.499482400249" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube59">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.378450799444 4.6493099369804 10.858263911846" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube60">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.5189850952099 9.8197980647999 10.900365949795" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube61">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="4.4804301839231 9.4211909856746 10.967158918952" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube62">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.7952008055501 9.8081736153961 11.096402088458" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube63">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.79275295687502 14.464405236284 10.748098089475" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube64">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="3.6885991167224 13.893336361457 10.928832660163" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube65">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.2408640437018 14.334363525191 11.055393364539" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube66">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.71346587348425 18.499748504488 11.371397064939" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube67">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="3.5899672480719 18.040807920527 10.888626934676" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube68">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.2406462054889 18.491647830928 10.765999238596" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube69">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="0.18580314292843 22.549640740757 10.934388120861" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube70">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="4.1552629799839 23.388142889779 11.26025542466" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
            <Node name="Cube71">
                <EulerImplicitSolver name="EulerImplicit"  rayleighStiffness="0.1" rayleighMass="0.1" />
                <CGLinearSolver name="CG Solver" iterations="25" tolerance="1e-5" threshold="1e-5"/>
                <MechanicalObject name="Cube_RigidDOF" template="Rigid3d" translation="7.1060958626243 22.531728374321 11.242810407068" />
                <UniformMass name="UniformMass" totalMass="10.0" />
                <UncoupledConstraintCorrection />
                <OBBCollisionModel/>
            </Node>
    
    
        </Node>
    
        <Node name="Floor">
            <MeshTopology name="Topology Floor" filename="mesh/floor.obj" />
            <MechanicalObject name="Floor Particles" scale3d="0.3 1 0.5" rotation="10 0 0"/>
            <!-- Collision Models -->
            <TriangleCollisionModel name="Floor Triangle For Collision" moving="0" simulated="0" />
        </Node>
    </Node>
    ```

=== "Python"

    ```python
    def createScene(rootNode):

        root = rootNode.addChild('root', dt="0.01", gravity="0 -9.81 0")

        pluginList = root.addChild('pluginList')
        rootNode.addObject('VisualStyle', displayFlags="showBehavior showCollisionModels")
        rootNode.addObject('OglSceneFrame')
        rootNode.addObject('FreeMotionAnimationLoop', name="FreeMotionAnimationLoop", parallelODESolving="true")
        rootNode.addObject('CollisionPipeline', name="CollisionPipeline")
        rootNode.addObject('ParallelBruteForceBroadPhase')
        rootNode.addObject('ParallelBVHNarrowPhase')
        rootNode.addObject('NewProximityIntersection', name="Proximity", alarmDistance="0.2", contactDistance="0.09", angleCone="0.0")
        rootNode.addObject('CollisionResponse', name="Response", response="FrictionContactConstraint")
        rootNode.addObject('LCPConstraintSolver', maxIt="1000", tolerance="0.001")

        grid0 = rootNode.addChild('grid0')
        grid0.addObject('OglLabel', label="72 cubes", selectContrastingColor="true")

        Cube0 = grid0.addChild('Cube0')
        Cube0.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube0.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube0.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.74819886067333 0.13000773132313 0.93028979372712")
        Cube0.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube0.addObject('UncoupledConstraintCorrection')
        Cube0.addObject('OBBCollisionModel')

        Cube1 = grid0.addChild('Cube1')
        Cube1.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube1.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube1.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="4.3804729733991 0.77457089385696 0.27803373722268")
        Cube1.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube1.addObject('UncoupledConstraintCorrection')
        Cube1.addObject('OBBCollisionModel')

        Cube2 = grid0.addChild('Cube2')
        Cube2.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube2.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube2.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.8670557578407 0.72764094440622 0.57778551223585")
        Cube2.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube2.addObject('UncoupledConstraintCorrection')
        Cube2.addObject('OBBCollisionModel')

        Cube3 = grid0.addChild('Cube3')
        Cube3.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube3.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube3.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.52166113561097 5.0046672055054 0.10088881528978")
        Cube3.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube3.addObject('UncoupledConstraintCorrection')
        Cube3.addObject('OBBCollisionModel')

        Cube4 = grid0.addChild('Cube4')
        Cube4.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube4.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube4.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="3.9450474625663 5.2738956775395 0.89534907690033")
        Cube4.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube4.addObject('UncoupledConstraintCorrection')
        Cube4.addObject('OBBCollisionModel')

        Cube5 = grid0.addChild('Cube5')
        Cube5.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube5.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube5.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.305407303062 4.5237374729587 0.39064753911954")
        Cube5.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube5.addObject('UncoupledConstraintCorrection')
        Cube5.addObject('OBBCollisionModel')

        Cube6 = grid0.addChild('Cube6')
        Cube6.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube6.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube6.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.071737911119935 9.523777224833 0.58510420731507")
        Cube6.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube6.addObject('UncoupledConstraintCorrection')
        Cube6.addObject('OBBCollisionModel')

        Cube7 = grid0.addChild('Cube7')
        Cube7.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube7.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube7.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="4.0065867209372 9.9413022501121 0.37843590061107")
        Cube7.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube7.addObject('UncoupledConstraintCorrection')
        Cube7.addObject('OBBCollisionModel')

        Cube8 = grid0.addChild('Cube8')
        Cube8.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube8.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube8.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.2205059766865 9.1447510035451 0.6489813419287")
        Cube8.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube8.addObject('UncoupledConstraintCorrection')
        Cube8.addObject('OBBCollisionModel')

        Cube9 = grid0.addChild('Cube9')
        Cube9.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube9.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube9.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.45521484057196 13.636816443939 0.34713000261557")
        Cube9.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube9.addObject('UncoupledConstraintCorrection')
        Cube9.addObject('OBBCollisionModel')

        Cube10 = grid0.addChild('Cube10')
        Cube10.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube10.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube10.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="3.7994200369806 13.985573250561 0.064533073019485")
        Cube10.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube10.addObject('UncoupledConstraintCorrection')
        Cube10.addObject('OBBCollisionModel')

        Cube11 = grid0.addChild('Cube11')
        Cube11.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube11.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube11.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.7237247050385 13.884293768268 0.63587171194883")
        Cube11.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube11.addObject('UncoupledConstraintCorrection')
        Cube11.addObject('OBBCollisionModel')

        Cube12 = grid0.addChild('Cube12')
        Cube12.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube12.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube12.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.93478864614609 18.345891356164 0.70599745712522")
        Cube12.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube12.addObject('UncoupledConstraintCorrection')
        Cube12.addObject('OBBCollisionModel')

        Cube13 = grid0.addChild('Cube13')
        Cube13.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube13.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube13.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="4.321946673478 18.265142549884 0.52448542440519")
        Cube13.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube13.addObject('UncoupledConstraintCorrection')
        Cube13.addObject('OBBCollisionModel')

        Cube14 = grid0.addChild('Cube14')
        Cube14.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube14.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube14.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.2815712151497 18.894561551928 0.31266520419748")
        Cube14.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube14.addObject('UncoupledConstraintCorrection')
        Cube14.addObject('OBBCollisionModel')

        Cube15 = grid0.addChild('Cube15')
        Cube15.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube15.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube15.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.3549315493344 23.275718517963 0.24514779459925")
        Cube15.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube15.addObject('UncoupledConstraintCorrection')
        Cube15.addObject('OBBCollisionModel')

        Cube16 = grid0.addChild('Cube16')
        Cube16.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube16.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube16.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="3.5063231964625 23.236317592085 0.37010838993364")
        Cube16.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube16.addObject('UncoupledConstraintCorrection')
        Cube16.addObject('OBBCollisionModel')

        Cube17 = grid0.addChild('Cube17')
        Cube17.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube17.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube17.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.9298104769223 23.441940895255 0.67634991681033")
        Cube17.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube17.addObject('UncoupledConstraintCorrection')
        Cube17.addObject('OBBCollisionModel')

        Cube18 = grid0.addChild('Cube18')
        Cube18.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube18.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube18.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.95332908441933 0.36214441310714 3.8638965107332")
        Cube18.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube18.addObject('UncoupledConstraintCorrection')
        Cube18.addObject('OBBCollisionModel')

        Cube19 = grid0.addChild('Cube19')
        Cube19.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube19.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube19.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="3.8713179339521 0.72825660031673 4.4170562354462")
        Cube19.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube19.addObject('UncoupledConstraintCorrection')
        Cube19.addObject('OBBCollisionModel')

        Cube20 = grid0.addChild('Cube20')
        Cube20.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube20.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube20.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.3623172698367 0.42303866540223 4.2916329795456")
        Cube20.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube20.addObject('UncoupledConstraintCorrection')
        Cube20.addObject('OBBCollisionModel')

        Cube21 = grid0.addChild('Cube21')
        Cube21.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube21.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube21.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.41599076540023 5.011850300949 4.0764630770201")
        Cube21.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube21.addObject('UncoupledConstraintCorrection')
        Cube21.addObject('OBBCollisionModel')

        Cube22 = grid0.addChild('Cube22')
        Cube22.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube22.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube22.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="4.1831578415274 4.5458585773808 3.657553949001")
        Cube22.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube22.addObject('UncoupledConstraintCorrection')
        Cube22.addObject('OBBCollisionModel')

        Cube23 = grid0.addChild('Cube23')
        Cube23.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube23.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube23.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.3023503712855 5.2596857597864 4.4541927831965")
        Cube23.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube23.addObject('UncoupledConstraintCorrection')
        Cube23.addObject('OBBCollisionModel')

        Cube24 = grid0.addChild('Cube24')
        Cube24.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube24.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube24.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.76817353431516 9.4053872043292 3.9015833886348")
        Cube24.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube24.addObject('UncoupledConstraintCorrection')
        Cube24.addObject('OBBCollisionModel')

        Cube25 = grid0.addChild('Cube25')
        Cube25.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube25.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube25.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="4.2292593758224 9.1146520563004 3.6763078310417")
        Cube25.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube25.addObject('UncoupledConstraintCorrection')
        Cube25.addObject('OBBCollisionModel')

        Cube26 = grid0.addChild('Cube26')
        Cube26.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube26.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube26.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.0779307592092 9.5021445925823 3.5487861833762")
        Cube26.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube26.addObject('UncoupledConstraintCorrection')
        Cube26.addObject('OBBCollisionModel')

        Cube27 = grid0.addChild('Cube27')
        Cube27.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube27.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube27.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.95456032825381 14.079579005753 3.9779275546213")
        Cube27.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube27.addObject('UncoupledConstraintCorrection')
        Cube27.addObject('OBBCollisionModel')

        Cube28 = grid0.addChild('Cube28')
        Cube28.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube28.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube28.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="3.523460344888 14.072634430869 3.847393618127")
        Cube28.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube28.addObject('UncoupledConstraintCorrection')
        Cube28.addObject('OBBCollisionModel')

        Cube29 = grid0.addChild('Cube29')
        Cube29.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube29.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube29.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.147231008926 14.275786010444 4.385838838241")
        Cube29.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube29.addObject('UncoupledConstraintCorrection')
        Cube29.addObject('OBBCollisionModel')

        Cube30 = grid0.addChild('Cube30')
        Cube30.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube30.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube30.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.033113344587904 18.947797390142 3.5628156732129")
        Cube30.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube30.addObject('UncoupledConstraintCorrection')
        Cube30.addObject('OBBCollisionModel')

        Cube31 = grid0.addChild('Cube31')
        Cube31.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube31.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube31.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="4.1209282542676 18.712580375705 4.1972367044991")
        Cube31.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube31.addObject('UncoupledConstraintCorrection')
        Cube31.addObject('OBBCollisionModel')

        Cube32 = grid0.addChild('Cube32')
        Cube32.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube32.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube32.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.4567343417819 18.837116944528 3.9945605623045")
        Cube32.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube32.addObject('UncoupledConstraintCorrection')
        Cube32.addObject('OBBCollisionModel')

        Cube33 = grid0.addChild('Cube33')
        Cube33.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube33.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube33.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.45280707555488 22.736685181612 3.6824013070121")
        Cube33.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube33.addObject('UncoupledConstraintCorrection')
        Cube33.addObject('OBBCollisionModel')

        Cube34 = grid0.addChild('Cube34')
        Cube34.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube34.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube34.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="4.2000142329838 22.655285063272 4.4546194779475")
        Cube34.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube34.addObject('UncoupledConstraintCorrection')
        Cube34.addObject('OBBCollisionModel')

        Cube35 = grid0.addChild('Cube35')
        Cube35.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube35.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube35.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.2545063110322 23.301119732578 3.7903861488637")
        Cube35.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube35.addObject('UncoupledConstraintCorrection')
        Cube35.addObject('OBBCollisionModel')

        Cube36 = grid0.addChild('Cube36')
        Cube36.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube36.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube36.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.15341132886401 0.16820048083002 7.5094929363157")
        Cube36.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube36.addObject('UncoupledConstraintCorrection')
        Cube36.addObject('OBBCollisionModel')

        Cube37 = grid0.addChild('Cube37')
        Cube37.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube37.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube37.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="3.8576176000562 0.53452356138012 7.1683901088165")
        Cube37.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube37.addObject('UncoupledConstraintCorrection')
        Cube37.addObject('OBBCollisionModel')

        Cube38 = grid0.addChild('Cube38')
        Cube38.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube38.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube38.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.0715503013095 0.51248217444517 7.0173420589498")
        Cube38.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube38.addObject('UncoupledConstraintCorrection')
        Cube38.addObject('OBBCollisionModel')

        Cube39 = grid0.addChild('Cube39')
        Cube39.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube39.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube39.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.25969415216692 5.333801087846 7.2361134994943")
        Cube39.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube39.addObject('UncoupledConstraintCorrection')
        Cube39.addObject('OBBCollisionModel')

        Cube40 = grid0.addChild('Cube40')
        Cube40.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube40.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube40.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="4.0694888157628 5.1161159149446 7.6208188285217")
        Cube40.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube40.addObject('UncoupledConstraintCorrection')
        Cube40.addObject('OBBCollisionModel')

        Cube41 = grid0.addChild('Cube41')
        Cube41.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube41.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube41.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.5960498701763 4.9855055615704 7.3799518441688")
        Cube41.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube41.addObject('UncoupledConstraintCorrection')
        Cube41.addObject('OBBCollisionModel')

        Cube42 = grid0.addChild('Cube42')
        Cube42.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube42.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube42.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.76430473093144 9.6086890309158 7.0650074975868")
        Cube42.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube42.addObject('UncoupledConstraintCorrection')
        Cube42.addObject('OBBCollisionModel')

        Cube43 = grid0.addChild('Cube43')
        Cube43.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube43.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube43.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="3.8057373828747 9.1482642410082 7.4258274763943")
        Cube43.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube43.addObject('UncoupledConstraintCorrection')
        Cube43.addObject('OBBCollisionModel')

        Cube44 = grid0.addChild('Cube44')
        Cube44.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube44.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube44.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.5454184466719 9.4156656071617 7.6357635323125")
        Cube44.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube44.addObject('UncoupledConstraintCorrection')
        Cube44.addObject('OBBCollisionModel')

        Cube45 = grid0.addChild('Cube45')
        Cube45.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube45.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube45.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.27177981393029 13.737715651392 7.6596358635741")
        Cube45.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube45.addObject('UncoupledConstraintCorrection')
        Cube45.addObject('OBBCollisionModel')

        Cube46 = grid0.addChild('Cube46')
        Cube46.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube46.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube46.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="4.3768386486344 14.108665051688 7.9202950656974")
        Cube46.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube46.addObject('UncoupledConstraintCorrection')
        Cube46.addObject('OBBCollisionModel')

        Cube47 = grid0.addChild('Cube47')
        Cube47.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube47.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube47.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.6850976271951 13.885693371941 7.6036874165776")
        Cube47.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube47.addObject('UncoupledConstraintCorrection')
        Cube47.addObject('OBBCollisionModel')

        Cube48 = grid0.addChild('Cube48')
        Cube48.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube48.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube48.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.73397222474868 18.105128143497 7.5915422609968")
        Cube48.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube48.addObject('UncoupledConstraintCorrection')
        Cube48.addObject('OBBCollisionModel')

        Cube49 = grid0.addChild('Cube49')
        Cube49.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube49.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube49.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="3.5186291742225 18.128789600045 7.3756774833313")
        Cube49.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube49.addObject('UncoupledConstraintCorrection')
        Cube49.addObject('OBBCollisionModel')

        Cube50 = grid0.addChild('Cube50')
        Cube50.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube50.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube50.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.1199427680671 18.613336643955 7.5970546564074")
        Cube50.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube50.addObject('UncoupledConstraintCorrection')
        Cube50.addObject('OBBCollisionModel')

        Cube51 = grid0.addChild('Cube51')
        Cube51.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube51.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube51.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.87562178442051 23.386319402552 7.7875950596238")
        Cube51.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube51.addObject('UncoupledConstraintCorrection')
        Cube51.addObject('OBBCollisionModel')

        Cube52 = grid0.addChild('Cube52')
        Cube52.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube52.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube52.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="4.0230774183399 22.973699588549 7.3888650198415")
        Cube52.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube52.addObject('UncoupledConstraintCorrection')
        Cube52.addObject('OBBCollisionModel')

        Cube53 = grid0.addChild('Cube53')
        Cube53.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube53.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube53.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.1893345374564 23.204612573006 7.9542482183102")
        Cube53.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube53.addObject('UncoupledConstraintCorrection')
        Cube53.addObject('OBBCollisionModel')

        Cube54 = grid0.addChild('Cube54')
        Cube54.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube54.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube54.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.70143965198725 0.46208797370181 11.339157561231")
        Cube54.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube54.addObject('UncoupledConstraintCorrection')
        Cube54.addObject('OBBCollisionModel')

        Cube55 = grid0.addChild('Cube55')
        Cube55.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube55.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube55.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="3.5612233099813 0.76873835118894 10.7542899946")
        Cube55.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube55.addObject('UncoupledConstraintCorrection')
        Cube55.addObject('OBBCollisionModel')

        Cube56 = grid0.addChild('Cube56')
        Cube56.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube56.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube56.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.8808409226503 0.47441122283899 10.761158771935")
        Cube56.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube56.addObject('UncoupledConstraintCorrection')
        Cube56.addObject('OBBCollisionModel')

        Cube57 = grid0.addChild('Cube57')
        Cube57.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube57.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube57.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.20105870682795 5.2240685013701 11.228900610343")
        Cube57.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube57.addObject('UncoupledConstraintCorrection')
        Cube57.addObject('OBBCollisionModel')

        Cube58 = grid0.addChild('Cube58')
        Cube58.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube58.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube58.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="3.7781574303648 5.1834110597537 11.499482400249")
        Cube58.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube58.addObject('UncoupledConstraintCorrection')
        Cube58.addObject('OBBCollisionModel')

        Cube59 = grid0.addChild('Cube59')
        Cube59.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube59.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube59.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.378450799444 4.6493099369804 10.858263911846")
        Cube59.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube59.addObject('UncoupledConstraintCorrection')
        Cube59.addObject('OBBCollisionModel')

        Cube60 = grid0.addChild('Cube60')
        Cube60.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube60.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube60.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.5189850952099 9.8197980647999 10.900365949795")
        Cube60.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube60.addObject('UncoupledConstraintCorrection')
        Cube60.addObject('OBBCollisionModel')

        Cube61 = grid0.addChild('Cube61')
        Cube61.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube61.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube61.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="4.4804301839231 9.4211909856746 10.967158918952")
        Cube61.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube61.addObject('UncoupledConstraintCorrection')
        Cube61.addObject('OBBCollisionModel')

        Cube62 = grid0.addChild('Cube62')
        Cube62.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube62.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube62.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.7952008055501 9.8081736153961 11.096402088458")
        Cube62.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube62.addObject('UncoupledConstraintCorrection')
        Cube62.addObject('OBBCollisionModel')

        Cube63 = grid0.addChild('Cube63')
        Cube63.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube63.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube63.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.79275295687502 14.464405236284 10.748098089475")
        Cube63.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube63.addObject('UncoupledConstraintCorrection')
        Cube63.addObject('OBBCollisionModel')

        Cube64 = grid0.addChild('Cube64')
        Cube64.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube64.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube64.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="3.6885991167224 13.893336361457 10.928832660163")
        Cube64.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube64.addObject('UncoupledConstraintCorrection')
        Cube64.addObject('OBBCollisionModel')

        Cube65 = grid0.addChild('Cube65')
        Cube65.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube65.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube65.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.2408640437018 14.334363525191 11.055393364539")
        Cube65.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube65.addObject('UncoupledConstraintCorrection')
        Cube65.addObject('OBBCollisionModel')

        Cube66 = grid0.addChild('Cube66')
        Cube66.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube66.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube66.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.71346587348425 18.499748504488 11.371397064939")
        Cube66.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube66.addObject('UncoupledConstraintCorrection')
        Cube66.addObject('OBBCollisionModel')

        Cube67 = grid0.addChild('Cube67')
        Cube67.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube67.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube67.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="3.5899672480719 18.040807920527 10.888626934676")
        Cube67.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube67.addObject('UncoupledConstraintCorrection')
        Cube67.addObject('OBBCollisionModel')

        Cube68 = grid0.addChild('Cube68')
        Cube68.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube68.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube68.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.2406462054889 18.491647830928 10.765999238596")
        Cube68.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube68.addObject('UncoupledConstraintCorrection')
        Cube68.addObject('OBBCollisionModel')

        Cube69 = grid0.addChild('Cube69')
        Cube69.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube69.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube69.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="0.18580314292843 22.549640740757 10.934388120861")
        Cube69.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube69.addObject('UncoupledConstraintCorrection')
        Cube69.addObject('OBBCollisionModel')

        Cube70 = grid0.addChild('Cube70')
        Cube70.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube70.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube70.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="4.1552629799839 23.388142889779 11.26025542466")
        Cube70.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube70.addObject('UncoupledConstraintCorrection')
        Cube70.addObject('OBBCollisionModel')

        Cube71 = grid0.addChild('Cube71')
        Cube71.addObject('EulerImplicitSolver', name="EulerImplicit", rayleighStiffness="0.1", rayleighMass="0.1")
        Cube71.addObject('CGLinearSolver', name="CG Solver", iterations="25", tolerance="1e-5", threshold="1e-5")
        Cube71.addObject('MechanicalObject', name="Cube_RigidDOF", template="Rigid3d", translation="7.1060958626243 22.531728374321 11.242810407068")
        Cube71.addObject('UniformMass', name="UniformMass", totalMass="10.0")
        Cube71.addObject('UncoupledConstraintCorrection')
        Cube71.addObject('OBBCollisionModel')

        Floor = rootNode.addChild('Floor')
        Floor.addObject('MeshTopology', name="Topology Floor", filename="mesh/floor.obj")
        Floor.addObject('MechanicalObject', name="Floor Particles", scale3d="0.3 1 0.5", rotation="10 0 0")
        Floor.addObject('TriangleCollisionModel', name="Floor Triangle For Collision", moving="0", simulated="0")
    ```

