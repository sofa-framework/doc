CUDA Compilation
----------------

#### Linux

To use CUDA in SOFA under Linux, you need to follow these steps:

-   Get the required files from
    [NVIDIA](https://developer.nvidia.com/cuda-downloads "http://www.nvidia.com/content/cuda/cuda-downloads.html") by specifying your operating system, distribution, architecture, version and desired installer type
-   Set the environment variables CUDA\_HOME to the location of cuda,
    for example: export CUDA\_HOME="/usr/local/cuda"
-   Add cuda to your path: export PATH=\${CUDA\_HOME}/bin:\${PATH}
-   In CMake, turn on the **SOFA-PLUGIN\_SOFACUDA** option, and
    reconfigure
    -   New options relating to Cuda will appear, some with the prefix
        "SOFA-CUDA" and some with the prefix "CUDA". The SOFA-CUDA
        options include:
        -   **SOFA-CUDA\_DOUBLE**: Option to activate double-precision
            support in CUDA (requires GT200+ GPU and -arch sm\_13 flag)
        -   **SOFA-CUDA\_PRECISE**: Option to use IEEE 754-compliant
            floating point operations
        -   **SOFA-CUDA\_DOUBLE\_PRECISE**: Option to get
            double-precision for sqrt/div (requires compute
            capability &gt;= 2 and CUDA\_VERSION &gt; 3.0) (with
            SOFA\_GPU\_CUDA\_PRECISE and SOFA\_GPU\_CUDA\_DOUBLE you get
            IEEE 754-compliant floating point operations for addition
            and multiplication only
        -   **SOFA-CUDA\_CUBLAS**: Option to activate cublas support in
            CUDA (requires SOFA\_GPU\_CUDA\_DOUBLE)
        -   **SOFA-CUDA\_CUDPP**: Option to activate CUDPP
            (for RadixSort)
        -   **SOFA-CUDA\_THRUST**: Option to activate THRUST
            (for RadixSort) Note: THRUST is included in CUDA SDK 4.0+,
            it is recommended to use it if available
    -   If you want to use some of the more advanced features of Cuda,
        such as atomics for floats, you should can set the
        CUDA\_NVCC\_FLAGS option to --ptxas-options=-v -arch sm\_12,
        changing sm\_12 to whatever Compute Capabilities you graphics
        card supports. See
        ([link](https://developer.nvidia.com/cuda-gpus)) for a table of
        Compute Capabilities.
-   Configure, Generate, and compile

#### Windows

To use CUDA in SOFA under Windows, you need to follow these steps:

-   Get the required installer from
    [NVIDIA](https://developer.nvidia.com/cuda-downloads) by specifying your operating system, architecture, version and desired installer type.
-   Check that the path to Cuda has been added to your system path. (for
    example, `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.5\bin`)
    -   Right click the My Computer icon on the desktop
    -   Select Properties
    -   Select Advanced System Settings from the left hand panel
    -   Select the Adcanced tab
    -   Press Environment Variables...
    -   Under System Variables, scroll until you find Path
    -   If the above path is not part of the Path variable, add a
        semicolon after the last path in the list, and add the
        above path.
-   In CMake, turn on the **PLUGIN\_SOFACUDA** option, and
    reconfigure
    -   New options relating to Cuda will appear, some with the prefix
        "SOFA-CUDA" and some with the prefix "CUDA". The SOFA-CUDA
        options include:
        -   **SOFA-CUDA\_DOUBLE**: Option to activate double-precision
            support in CUDA (requires GT200+ GPU and -arch sm\_13 flag)
        -   The appropriate Cuda driver for your system
        -   **SOFA-CUDA\_PRECISE**: Option to use IEEE 754-compliant
            floating point operations
        -   **SOFA-CUDA\_DOUBLE\_PRECISE**: Option to get
            double-precision for sqrt/div (requires compute
            capability &gt;= 2 and CUDA\_VERSION &gt; 3.0) (with
            SOFA\_GPU\_CUDA\_PRECISE and SOFA\_GPU\_CUDA\_DOUBLE you get
            IEEE 754-compliant floating point operations for addition
            and multiplication only
        -   **SOFA-CUDA\_CUBLAS**: Option to activate cublas support in
            CUDA (requires SOFA\_GPU\_CUDA\_DOUBLE)
        -   **SOFA-CUDA\_CUDPP**: Option to activate CUDPP
            (for RadixSort)
        -   **SOFA-CUDA\_THRUST**: Option to activate THRUST
            (for RadixSort) Note: THRUST is included in CUDA SDK 4.0+,
            it is recommended to use it if available
    -   If you want to use some of the more advanced features of Cuda,
        such as atomics for floats, you can set the
        CUDA\_NVCC\_FLAGS option to --ptxas-options=-v -arch sm\_12,
        changing sm\_12 to whatever Compute Capabilities you graphics
        card supports. See
        ([link](https://developer.nvidia.com/cuda-gpus)) for a table of
        Compute Capabilities.
-   Configure, Generate, and compile

 

SofaCUDA
--------

SofaCUDA is a plugin that provides a number of Sofa components that have
been implemented using CUDA, which allows
the graphics card to be used for multithreaded programming. This can
significantly improve the performance of your scene when working with
large meshes. To include this plugin, first follow the compilation
instructions define above.

#### CUDA scene file

To begin using the Cuda components, you need to change the template of
the Mechanical Object in your scene. Consider the following scene:

```xml
<Node name="root" dt="0.04" showBehaviorModels="0" showCollisionModels="0" showMappings="0" showForceFields="1">
  <Node name="M1">
    <MeshVTKLoader name="volume" filename="mesh/raptorTetra_19409.vtu" onlyAttachedPoints="false" />
    <EulerImplicit rayleighMass="0.01" rayleighStiffness="0.01" />
    <CGLinearSolver iterations="25" tolerance="1e-6" threshold="1e-20"/>
    <MeshTopology src="@volume" />
    <MechanicalObject template="Vec3f" />
    <UniformMass vertexMass="0.01" />
    <BoxROI name="box0" box="-2.2 -1 -10 2.2  10  10" drawBoxes="1" />
    <BoxROI name="box1" box="-2.2 -1  -1 2.2 2.5 1.5" drawBoxes="1" />
    <IndexValueMapper name="ind_box0"                                      indices="@box0.tetrahedronIndices" value="100000" />
    <IndexValueMapper name="ind_box1" inputValues="@ind_box0.outputValues" indices="@box1.tetrahedronIndices" value="1000000" />
    <TetrahedronFEMForceField name="FEM" youngModulus="@ind_box1.outputValues" poissonRatio="0.4" listening="true" />
    <BoxROI name="box3" box="-2.2 -0.3 -9.2    2.2 0.110668 2.88584" drawBoxes="1" drawSize="2" />
    <FixedProjectiveConstraint indices="@box3.indices" />
    <BoxROI name="boxF" box="-2.2 -1 6.88 2.2  10  10" drawBoxes="true" />
    <ConstantForceField points="@boxF.indices" force="7.5 -6.63 -15" arrowSizeCoef="0.1" />
    <PlaneForceField normal="0 1 0" d="-0.2" stiffness="100"  draw="1" drawSize="20" />
  </Node>
</Node>
```

To use the Cuda components that are available for this scene, there are
two steps: Add:

```xml
<RequiredPlugin name="CUDA computing" pluginName="SofaCUDA" />
```

near the top of the scene. This indicates that the SofaCUDA plugin is
needed, and will automatically load the plugin if it is not already
loaded in the Plugin Manager. Change the MechanicalObject template from
Vec3f to CudaVec3f. This will cause all of the components which have
been implemented in Cuda to use that implementation, rather than the
standard cpu implementation. In this scene, this includes components
such as BoxROI, TetrahedronFEMForceField and UniformMass. This leaves us
with the scene:

```xml
<Node name="root" dt="0.04" showBehaviorModels="0" showCollisionModels="0" showMappings="0" showForceFields="1">
    <RequiredPlugin name="CUDA computing" pluginName="SofaCUDA" />
    <Node name="M1">
        <MeshVTKLoader name="volume" filename="mesh/raptorTetra_19409.vtu" onlyAttachedPoints="false" />
        <EulerImplicit rayleighMass="0.01" rayleighStiffness="0.01" />
        <CGLinearSolver iterations="25" tolerance="1e-6" threshold="1e-20"/>
        <MeshTopology src="@volume" />
        <MechanicalObject template="CudaVec3f" />
        <UniformMass vertexMass="0.01" />
        <BoxROI name="box0" box="-2.2 -1 -10 2.2  10  10" drawBoxes="1" />
        <BoxROI name="box1" box="-2.2 -1  -1 2.2 2.5 1.5" drawBoxes="1" />
        <IndexValueMapper name="ind_box0"                                      indices="@box0.tetrahedronIndices" value="100000" />
        <IndexValueMapper name="ind_box1" inputValues="@ind_box0.outputValues" indices="@box1.tetrahedronIndices" value="1000000" />
        <TetrahedronFEMForceField name="FEM" youngModulus="@ind_box1.outputValues" poissonRatio="0.4" listening="true" />
        <BoxROI name="box3" box="-2.2 -0.3 -9.2    2.2 0.110668 2.88584" drawBoxes="1" drawSize="2" />
        <FixedProjectiveConstraint indices="@box3.indices" />
        <BoxROI name="boxF" box="-2.2 -1 6.88 2.2  10  10" drawBoxes="true" />
        <ConstantForceField points="@boxF.indices" force="7.5 -6.63 -15" arrowSizeCoef="0.1" />
        <PlaneForceField normal="0 1 0" d="-0.2" stiffness="100"  draw="1" drawSize="20" />
    </Node>
</Node>
```

#### CUDA coding

How to access a data from the MechanicalState and use it in CUDA: n CUDA
code, you cannot use the usual Accessor as for CPU coding. To access and
use a vector from the MechanicalState inside your kernel, two steps are
required: Reading access First, you need to access the vector:

``` cpp
const VecCoord& myPositions = this->getMState()->read(core::VecCoordId:: position())->getValue();
```

Then, to send the recovered vector to your kernel, you need to give as
argument:

``` cpp
myPositions.deviceRead();
```

Writing-Reading access In a similar way, you need to write it as
follows:

``` cpp
VecCoord& myPositions = *(this->getMState()->write(core::VecCoordId:: position()).beginEdit());
myPositions.deviceWrite();
```
