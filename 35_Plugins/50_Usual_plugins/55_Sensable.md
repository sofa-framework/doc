Installing the Sensable Plugin
------------------------------

-   Download Geomagic drivers and SDK:  
    [OpenHaptics for **Windows** Developer Edition v3.4](https://3dsystems.teamplatform.com/pages/102774?t=r4nk8zvqwa91)  
    [OpenHaptics for **Linux** Developer Edition v3.4](https://3dsystems.teamplatform.com/pages/102863?t=fptvcy2zbkcc)
-   The OpenHaptics SDK comes with both the Phantom Drivers and the
    OpenHaptics libraries. First install the drivers, then the SDK.
-   Run the Phantom Test program that came with the SDK, and use it to
    check that the Omni is working. It is also recommended that you use
    it to calibrate your Omni.
-   In your Sofa CMake configuration, select **SOFA-PLUGIN\_SENSABLE**
    and configure. If you installed OpenHaptics in the default location,
    CMake should find all the libraries and directories automatically.

If CMake doesn't find them for you, it will return an error and you can
set them manually. The HD and HL libraries are found in
OpenHaptics/Academic/3.1/lib/"your system's subdirectories", while the
HDU library is found in OpenHaptics/Academic/3.1/utilities/lib/"your
system's subdirectories". Once all the variables are set, you can
**Configure**, **Generate** and **compile** as usual.

Using the Plugin
----------------

### Method 1

One method of using the Omni in a scene is to control a rigid object
directly with the Omni, and compute the force feedback based on the
penetration of that rigid object with any other object in the scene. The
Senable Plugin contains two important components. The **NewOmniDriver**
interfaces with the Omni device, getting the tool's location and sending
it the appropriate force feedback. The **EnslavementForceFeedback**
computes the force feedback values, based on the collision detection
that Sofa already does in a scene.

#### Example Scene 1 - Using the DistanceGrid Collision Model

In the examples directory of the Sensable Plugin, there are a number of
example scenes. We will examine **SimpleBox-DistanceGrid.scn**. This
scene has two main objects. A long curved tool is controlled by the
Omni, and a simple box serves as something for us to feel. Taking a look
at the scene in more detail, we see our collision pipeline:

```xml
<CollisionPipeline name="pipeline" depth="6" />
<BruteForceBroadPhase/>
<BVHNarrowPhase/>
<MinProximityIntersection name="proximity" alarmDistance="0.8" contactDistance="0.5" />
<CollisionResponse name="response" response="PenalityContactForceField" />
```

This is what does the collision detection for the scene. Next, we see
our **NewOmniDriver**:

```xml
<NewOmniDriver name="Omni Driver"  listening="true" tags="Omni" forceScale="0.5" scale="500"  permanent="true" />
```

We will discuss all the attributes in more detail later, but the
important one to note now is the **tags** attribute. The NewOmniDriver
needs to find the MechanicalObject that it will control, and the
ForceFeedback that will calculate the feedback for it. It will do this
by looking for the components that have the same tag as in, in this case
**Omni**. Next we see the **Instrument** node. First we see the
MechanicalObject:

```xml
<MechanicalObject template="Rigid3d" name="instrumentState" tags="Omni"  />
```

Here, the template type is important. The NewOmniDriver is looking for a
MechanicalObject with the template **Rigid**. Also, we see that it has
the matching tag, so that the NewOmniDriver knows that this is the
MechanicalObject that it should be controlling. The UniformMass object
simply gives the MechanicalObject some mass. In the **VisualModel**
node, the **OglModel** loads the mesh that is used to visualize the
instrument.

```xml
<OglModel template="Vec3d" name="InstrumentVisualModel"  fileMesh="data/mesh/dental_instrument.obj" scale3d="10 10 10" translation="-2.12256 1.32361 35.5" rotation="180 0 150" material="Default Diffuse 1 1 0.2 0.2 1 Ambient 1 0.2 0.04 0.04 1 Specular 0 1 0.2 0.2 1 Emissive 0 1 0.2 0.2 1 Shininess 0 45" />
```

Note the translation and rotation attributes. We will come back to them
later. The material attribute just gives the instrument a different look
than the box. The **RigidMapping** connects the MechanicalObject we saw
earlier with the OglModel. This keeps the visualization of the
instrument in sync with the movement of the Omni. In the **Collision
Model** node, there are a number of important details.

```xml
<MechanicalObject template="Vec3d" name="Particle" position="0 0 0" />
<Point name="ParticleModel" contactStiffness="2" />
<RigidMapping template="Rigid3d,Vec3d" name="MM->CM mapping"  object1="instrumentState"  object2="Particles" />
<EnslavementForceFeedback name="forcefeedback" tags="Omni" collisionModel1="@ParticleModel" collisionModel2="" relativeStiffness="4" attractionDistance="0.3" normalsPointOut="false"/>
```

First, we see the MechanicalObject named **Particle**, and the attribute
**position** with the value "0 0 0". Here we are making defining a
single point that will be used for our collisions. This point represents
the tip of the Omni. We place it at "0 0 0" because this lines it up
with the Omni properly. We then give our particle a Point collision
model. The **RigidMapping**, like the earlier one, keeps are particle in
sync with the movement of the Omni. The visual model is also in sync
with the motion, and we want to tip of the instrument to correspond with
our particle, so that the tip of the instrument is where the collision
occurs. That is what the translation and rotation attribute in
**InstrumentVisualModel** are for. They line the visual model of the
tool up with the particle. We put the translation in the visual model
instead of in the particle so that the tip lines up with the movement
and rotation of the Omni. The **EnslavementForceFeedback** listens for
any contact that our Particle Model makes with any other model in the
scene, then calculates the force feedback for the Omni accordingly. We
will look into all the attributes in detail later, but for now notice
that again the tag attribute matches that of the NewOmniDriver. The
**Box** node also has a visual model and a collision model. In this
case, the same mesh is used in both models. Here, the **DistanceGrid**
is the collision model for the box.


#### Example Scene 2 - Using the Triangle Collision Model

The example scene **SimpleBox-TriangleModel.scn** sets up the same scene
as SimpleBox-DistanceGrid.scn, but using a different collision model
type. There are two key differences in this example:

-   The DistanceGrid component is replaced by

    ```xml
    <Triangle />
    ```

-   In the component **MinProximityIntersection** has the the attribute
    **useSurfaceNormals** set to true

The useSurfaceNormals attribute tells the MinProximityIntersection to
use normals from the Triangle collision model when creating the
collision information, which is then used by the
EnslavementForceFeedback to correctly compute the force feedback.


### Method 2

Another way to set up the scene is to indirectly control a rigid object,
by attaching it to the position of the Omni using a spring.

#### Example 3 Using a Spring

The example scene **SimpleBox-Method2.scn** sets up the same type of
scene as the above examples, but using a spring to link the rigid body
and the Omni instead of directly controlling it. The Collision Pipeline
is slightly different:

```xml
<CollisionPipeline depth="8" />
<BruteForceDetection name="N2" />
<LocalMinDistance name="Proximity" alarmDistance="0.6" contactDistance="0.3" />
<RuleBasedContactManager name="Response" response="FrictionContactConstraint"
                            rules="1 * FrictionContact?mu=0.01
                            " />
<DefaultVisualManagerLoop />
```

We first create the representation of the Omni's actual position. In
contains the NewOmniDriver. Just like in Method 1, we use the **tags**
attribute to match up the NewOmniDriver, the mechanical object, and the
ForceFeedback (which will show up later).

```xml
<Node name="OmniObject">
    <Node name="RigidLayer">
        <MechanicalObject name="ToolRealPosition" tags="Omni" template="Rigid" />
        <NewOmniDriver name="omniDriver1" tags="Omni" scale="300" permanent="true" listening="true"/>
        <Node name="Tool1">
            <MechanicalObject template="Rigid" name="RealPosition"/>
            <SubsetMapping indices="0"/>
        </Node>
    </Node>
</Node>
```

Then we create our actual tool that will interact with the scene. First
we need solvers to allow for collision detection:

```xml
<Node name="Tool">
    <EulerImplicit />
    <CGLinearSolver />
```

Next we create our rigid object:

```xml
<MechanicalObject name="ms" template="Rigid"/>
<UniformMass totalMass="0.1" />
```

And we provide a ForceFeedback component to calculate the force feedback
to the Omni:

```xml
<LCPForceFeedback activate="true" tags="Omni" forceCoef="0.001" />
```

Next we create the Collision Model, and map it to the rigid model we
created above:

```xml
<Node name="ToolCollision">
    <MechanicalObject name="CM" position="0 0 0"/>
    <Point bothSide="true" group="1" />
    <RigidMapping />
</Node>
```

Now we need a Visual Model, also mapped to the rigid model we create
above:

```xml
<Node name="ToolVisual">
    <OglModel template="ExtVec3f" name="VisualModel" fileMesh="data/mesh/dental_instrument.obj" scale3d="10 10 10" translation="-2.12256 1.32361 35.5" rotation="180 0 150" />
    <RigidMapping template="Mapping<Rigid,ExtVec3f>" name="MM->VM mapping" object1="ms" object2="VisualModel" />
</Node>
```

Finally, we add the components to link the tool we created with the
representation of the Omni's position:

```xml
    <RestShapeSpringsForceField template="Rigid" stiffness="1000000" angularStiffness="200000000" external_rest_shape="../OmniObject/RigidLayer/Tool1/RealPosition" />
    <UncoupledConstraintCorrection compliance="0.001   0.00003 0 0   0.00003 0   0.00003" />
</Node>
```

The rest of the scene contains the box, which is created just as it was
in the other scenes.

NewOmniDriver Attributes
------------------------

-   **listening** - When true, the NewOmniDriver will listen to the
    ForceFeedback for the computation of the feedback.
-   **tags** - The NewOmniDriver will look for a MechanicalObject with
    template Rigid with a matching tag, and a ForceFeedback with a
    matching tag.
-   **forceScale** - scales the force feedback given to the Omni. This
    attribute will involve a balance in your scene. If it is too high,
    you will feel a lot of oscillations and vibrations. Too low and you
    will be able to push through your surfaces easily.
-   **scale** - scales the motion from the Omni. This changes how much
    motion on the physical Omni it takes to move the tool in the scene.
-   **permanent** - True if the force feedback will be
    applied permanently.
-   **alignOmniWithCamera** - True if the object controlled by the Omni,
    and the direction of motion from the Omni, should remain lined up
    with the camera. This means that as you change the camera's view,
    moving the Omni arm up will always make your object move up in
    the view. By default, the scene's default Camera is used, but if you
    wish to specify a camera, you can do so by matching the camera's
    tags with the NewOmniDriver's tags. See Example scene
    CameraAlignment.scn and SpecifyingCamera.scn.

EnslavementForceFeedback Attributes
-----------------------------------

-   **tags** - should correspond with the tags attribute in the
    NewOmniDriver
-   **collisionModel1** - The collision model that the Omni controls.
    The EnslavementForceFeedback will then gather the collision
    information for every collision this model has in the scene
-   **collisionModel2** - If you are only interested in the collision
    between collisionModel1 and one other collision model in the scene,
    you can specify that other model here. The EnslavementForceFeedback
    will then only gather the collision information for collisions
    involving both models. **Note:** if you do not want to specify
    another model, it is important that you specify the attribute as
    **collisionModel2=""**.
-   **relativeStiffness** - To reduce oscillations when contact is made
    with a surface, the force applied when the instrument is found to be
    inside the other object is higher than when it is outside. The ratio
    of these forces is specified by the relativeStiffness. This value
    will also involve a balance in your scene. If it is too high, you
    will feel a lot of oscillations and vibrations. Too low and you will
    be able to push through your surfaces easily.
-   **attractionDistance** - To reduce oscillation when contact is made
    with a surface, as the instrument gets very close to making contact,
    it is slightly attracted to the contact point. Once it reaches the
    contact point, the force feedback will push away from the object, to
    prevent the instrument from entering. The distance from contact at
    which this attraction starts is given with attractionDistance.
-   **normalsPointOut** - In order for the force feedback to be applied
    in the appropriate direction, the EnslavementForceField must know if
    the normals of the other objects in the scene point towards the
    inside of the object or towards the outside. If they point towards
    the outside, normalsPointOut should be true, and false in the
    normals point towards the inside. Note: All the objects (other than
    the once being controlled by the Omni) need to have their normals
    pointing in the same direction.
-   **contactScale** - This scales the strength of the force feedback
    depending on the size of the objects in your scene. Larger objects
    will require a larger contactScale in order for the force feedback
    to be felt.

Scenes at different scales
--------------------------

The forces computed in your scene will vary depending on the scale of
the objects in your scene. For example, the box in SimpleBox.scn is
10x10x10, while the box in SimpleBoxLarge.scn is scaled to be 10 times
bigger than that. At larger and smaller scales, a number of your
attributes will need to become larger and smaller as well. The
attributes that are sensitive to scale are:

-   MinProximityIntersection: alarmDistance
-   MinProximityIntersection: contactDistance
-   NewOmniDriver: scale
-   EnslavementForceFeedback: attractionDistance
-   EnslavementForceFeedback: contactScale

Look at the differences between these attributes in SimpleBox.scn and
SimpleBoxLarge.scn to learn more.

Scenes with translated objects
------------------------------

One of the downsides of the **DistanceGrid** collision models is that it
doesn't allow the **EnslavementForceFeedback** to correctly compute the
force feedback on an mesh that has been translated in the scene. There
are two ways to deal with this:

-   Use software such as
    [Blender](http://www.blender.org/ "http://www.blender.org/"){.external
    .text} to create a new mesh that has the translation built into the
    mesh file. See example scene **TwoTeeth-DistanceGrid.scn**
-   Use the **Triangle** collision model instead of the DistanceGrid.
    See example scene **TwoTeeth-TriangleModel.scn**

Rotating the scene
------------------

By default, when you rotate a scene with the NewOmniDriver, the tool
being controlled by the Omni follows this rotation. In this way, no
matter how you are viewing the scene, moving the Omni arm up will move
the tool up in the view. This behavior can be turned off by setting the
attribute **alignOmniWithCamera** to false. See the example scene
**CameraAlignment.scn**. The tool aligns to the view of a specific
camera. Usually, a scene won't have a camera specified, and the
NewOmniDriver will align the tool to the default view. If you do have a
camera specified, it will align with that camera. If you have more than
one camera specified, you can specify the camera that the tool will be
aligned to by setting the **tags** attribute to match the tags of the
NewOmniDriver. See the example scene **SpecifyingCamera.scn**.
