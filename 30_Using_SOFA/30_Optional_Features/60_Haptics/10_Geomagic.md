Installing the OpenHaptics SDK
------------------------------

The Geomagic drivers and SDK can be directly downloaded from the 3DSystem website:

- [OpenHaptics for **Windows** Developer Edition v3.4](https://3dsystems.teamplatform.com/pages/102774?t=r4nk8zvqwa91)  
- [OpenHaptics for **Linux** Developer Edition v3.4](https://3dsystems.teamplatform.com/pages/102863?t=fptvcy2zbkcc)

Once the download is complete, follow the [installation guide](https://3dsystems.teamplatform.com/pages/102863?t=fptvcy2zbkcc#). The installation directory should be:

- `C:/OpenHaptics` for Windows
- `/opt/OpenHaptics/Developer/3.4-0/` for Linux

You can check the install by running the *Geomagic_Touch_Setup* and *Geomagic_Touch_Diagnostic* applications (located in `/opt/geomagic_touch_device_driver/` for Linux). To do so, your Geomagic device must now be connected. If you are using Ethernet connection, make sure the address assignement of the wired connection is set to "Link-Local Only" instead of "Automatic".


Compilation in SOFA
-------------------

Now in SOFA:

- activate the plugin in cmake-gui by setting the flag PLUGIN_GEOMGIC to true
- compile SOFA, which should trigger the compilation of the Geomagic plugin
- enjoy the power of the Geomagic haptic interfaces with SOFA and give a try to the example scene (examples/DemoGeomagic.scn)

And let us know about your Geomagic simulations!



Using the plugin in a simulation
--------------------------------

### Load the plugin

Like any other plugin in SOFA, you need to load it dynamically in your scene if you want to use classes defined in this plugin.
For the Geomagic plugin, to benefit from the GeomagicDriver, you need to add in your root node:

```xml
<RequiredPlugin name="Geomagic plugin" pluginName="Geomagic" />
```

### Add the GeomagicDriver

To interface the Geomagic device with the simulation, all you need is to add the GeomagicDriver class into your scene:
```xml
<GeomagicDriver name="GeomagicDevice" deviceName="Default Device" scale="1" drawDeviceFrame="1" positionBase="0 0 0"  orientationBase="0 0 0 1"/>
```

This class will recover the motion of the device and allow for communication with the simulation.

### Control an object in the scene

The use of the GeomagicDriver in a scene could be to control a rigid object in a simulation.
For install, let's control one rigid point with
```xml
<GeomagicDriver name="GeomagicDevice" deviceName="Default Device" scale="1" drawDeviceFrame="1" positionBase="0 0 0" orientationBase="0 0 0 1"/>
<MechanicalObject template="Rigid" name="GeomagicMO" position="@GeomagicDevice.positionDevice" />
```

Then, as in any SOFA simulation, you can map this rigid point to any other object (visual, mechanical or collision model).

### Get haptic feedback

Now, if you wan to control an object and get haptic feedback due to collision, the scene becomes more complicated.
You will need to set up the entire collision pipeline in order to solve the Linear Complementary Problem (LCP), thus finding its solutions: the Lagrange multipliers.

In the root node, the collision pipeline needs to be defined with:
```xml
<RequiredPlugin name="Geomagic plugin" pluginName="Geomagic" />
    
<CollisionPipeline name="pipeline" depth="6" verbose="0"/>
<BruteForceDetection name="detection" />
<CollisionResponse name="response" response="FrictionContact" />
<LocalMinDistance name="proximity" />
<FreeMotionAnimationLoop/>
<LCPConstraintSolver tolerance="0.001" maxIt="1000"/>
<GeomagicDriver name="GeomagicDevice" deviceName="Default Device" scale="1" drawDeviceFrame="1" positionBase="0 0 0" orientationBase="0 0 0 1" />
```

In the node describing your object on which you want to recover the force feedback, you need to add a LCPForceFeedback. This class computes the force applied on the object based on the constraint problem. During the simulation, the GeomagicDriver will look for a pointer to a LCPForceFeedback to get the force value to return to the haptic interface. The node therefore can be written:

```xml
<Node name="Instrument-1" >
    <EulerImplicitSolver name="ODE solver" rayleighStiffness="0.05" rayleighMass="1.0" />
    <CGLinearSolver name="linear solver" iterations="25" tolerance="1e-10" threshold="10e-10" /> 
    <MechanicalObject name="instrumentState" position="@PATH_TO_GEOMAGICDRIVER/GeomagicDevice.positionDevice" template="Rigid" />
    <UniformMass name="mass" totalmass="0.005" />
    <LCPForceFeedback activate="true" forceCoef="0.005"/> <!-- this class computes the force to return back -->
    <UncoupledConstraintCorrection/>

    <!-- This node is the collision model associated to our controlled object -->
    <Node name="CollisionModel" >
        <MeshObjLoader filename="MY_COLLISION_SURFACE_MODEL.obj"  name="loader"/>
        <Mesh src="@loader" name="InstrumentCollisionModel" />
        <MechanicalObject src="@loader" name="instrumentCollisionState"  />
        <Line name="instrument" />
        <Point name="instrument"  /> 
        <RigidMapping name="CollisionMapping" input="@instrumentState" output="@instrumentCollisionState" />
    </Node>
</Node>
```
