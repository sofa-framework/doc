The Monitor Component
---------------------

A Sofa Component named Monitor (**sofa::component::misc::Monitor**) can
help you to visualize, to monitor or to export some properties.

#### Quick overview of Monitor possibilities

With this component, you can see the positions, trajectories,
velocities, forces of chosen particles directly in the GUI or save it
into files (readable with Gnuplot for example). You can get an idea of
what this component can make launching the
*Sofa/examples/Components/misc/Monitor.scn* scene.

#### Using the Monitor Component

To monitor properties you have to add a Monitor Component in your scene.
Here is a selection of a piece of code of one of the Monitor of the
example scene:

```xml
<Monitor template="Vec3d" name="velocities_8-16-24" listening="1" indices="8 16 24" showPositions="0" PositionsColor="1 1 0 1" showVelocities="1" VelocitiesColor="1 1 0 1" ForcesColor="1 1 0 1" showMinThreshold="0.01" TrajectoriesPrecision="0.1" TrajectoriesColor="1 1 0 1" sizeFactor="1" />
```

You can of course also add the component to your scene with the Modeler,
look for Monitor in the search form. Required : for the Monitor to work
you have to specify **listening="1"** or to set listening to true in the
GUI. You have to select the properties you want to monitor or display.

-   If you want to visualize positions, you have to select showPositions
    (either clicking the corresponding field in the Visualization tab in
    the component GUI or adding `showPositions="1"` in your scene
    description file).
-   Then you can choose the color to be applied to your position
    visualization with `PositionsColor` and if needed the size of the
    visualization with `sizeFactor`.
-   You have to select the dofs that you want to monitor using the
    classic indices field : `indices="8 16 24"`.
-   You can choose to export the positions of your dofs
    with ExportPositions. The positions will be exported to a file named
    following this rule : **your\_monitor\_component\_name+\_x.txt** in
    your **Sofa** directory.

  -------------- ------------------------- ------------------------ ------------------------------- --------------------------------------------------------------------------------------
                 Field                     XML                      example                         Default Comments
                 `indices`                 `""`                     `indices="0 2 4"`               *select the dofs to be monitored*
  Positions      `showPositions`           `false`                  `showPositions="true"`          *to monitor positions*
  Positions      `PositionsColor`          `(1.0, 1.0, 0.0, 1.0)`   `PositionsColor="1 1 0 1"`      *to visualize the positions as some yellow points*
  Positions      `ExportPositions`         `false`                  `ExportPositions="true"`        *positions will be exported to **\${component\_name}\_x.txt***
  Velocities     `showVelocities`          `false`                  `showVelocities="true"`         *to monitor velocities*
  Velocities     `VelocitiesColor`         `(1.0, 1.0, 0.0, 1.0)`   `VelocitiesColor="1 0 1 1"`     *to visualize the velocities as some purple arrows*
  Velocities     `ExportVelocities`        `false`                  `ExportVelocities="true"`       *velocities will be exported to **\${component\_name}\_v.txt***
  Forces         `showForces`              `false`                  `showForces="true"`             *to monitor forces*
  Forces         `ForcesColor`             `(1.0, 1.0, 0.0, 1.0)`   `ForcesColor="1 0 0 1"`         *to visualize the forces as some red arrows*
  Forces         `ExportForces`            `false`                  `ExportForces="true"`           *forces will be exported to **\${component\_name}\_f.txt***
  Trajectories   `showTrajectories`        `false`                  `showTrajectories="true"`       *to visualize the trajectories*
  Trajectories   `TrajectoriesColor`       `(1.0, 1.0, 0.0, 1.0)`   `TrajectoriesColor="1 0 1 1"`   *to get nice purple trajectories represented as lines*
  Trajectories   `TrajectoriesPrecision`   `1.0`                    `TrajectoriesPrecision="0.1"`   *to specify the timestep between two positions saving to reconstruct the trajectory*
                 `sizeFactor`              `1.0`                    `sizeFactor="true"`             *to change the size of the drawing (points, arrows or lines)*
                 `showMinThreshold`        `0.01`                   `showMinThreshold="0.01"`       *under this value, vectors are not represented*
  -------------- ------------------------- ------------------------ ------------------------------- --------------------------------------------------------------------------------------

#### Visualize the result
To read the resulting file, you can use ![Gnuplot](http://www.gnuplot.info/). In Gnuplot, you can for instance run the following command to render curves of your export file:
```batch
splot "monitor-displacement-faceNode_x.txt"
```

See more ![Gnuplot examples here](http://gnuplot.sourceforge.net/demo/surface1.html).



The ExtraMonitor Component, a Monitor extension
-----------------------------------------------

The ExtraMonitor component gives you the ability to use everything that
it is in Monitor with some Extra stuff. IIt has been written to allow to
compute, for example, the resultant of the forces of all the dofs of a
MechanicalObject, or the minimum displacement of a region...

#### Using ExtraMonitor

Include the ExtraMonitor in your scene. Here is an example of use :

```xml
<ExtraMonitor template="Vec3d" name="velocities_8-16-24" listening="1" indices="8 16 24" showPositions="0" PositionsColor="1 1 0 1" showVelocities="1" VelocitiesColor="1 1 0 1" ForcesColor="1 1 0 1" showMinThreshold="0.01" TrajectoriesPrecision="0.1" TrajectoriesColor="1 1 0 1" sizeFactor="1" ExportWcin="false" ExportWext="false" resultantF="true" />
```

-   With this xml code, we say we want to use an ExtraMonitor named
    'Socle' with every indices read in the indices field of the Engine
    named 'engineToto'. (We suppose 'engineToto' has been
    defined before).
-   Then we say we would like to export forces in a file but we set
    resultantF to true to precise we want to export the resultant of the
    dofs forces and not the forces of each of the dofs given in the
    indices set.
-   We also export positions but again we don't want every positions to
    be written down in the selected flag. We choose to export the
    minimum displacement and the maximum displacement of our set
    of particles. minCoord contains the number of the coordinate (0
    stands for x, 1 stands for y, 2 stands for z in a 3D) for which we
    want to get the displacement. The same for maxCoord. Defaults values
    are -1 which means we don't want to export the
    corresponding displacement.

#### Additions

ExtraMonitor does not add visualization possibilities but it adds export
possibilities.

  ----------- -------------- ------------------------ --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------
              Field          XML                      example               Default Comments
              `indices`      `""`                     `indices="0 2 4"`     *select the dofs to be monitored*
  Energy      `ExportWcin`   `false`                  `ExportWcin="true"`   *export kinetic energy computed by Mass in the context of the Monitor (need not indices to be set), exported to **\${component\_name}\_wcin.txt***
  Energy      `ExportWext`   `(1.0, 1.0, 0.0, 1.0)`   `ExportWext="true"`   *export potential energy computed by the Mass in the context of the Monitor (need not indices to be set), exported to **\${component\_name}\_wext.txt***
  Forces      `resultantF`   `false`                  `resultantF="true"`   *to export force resultant of the monitored dofs in a gnuplot file, **ExportForces** must be set to **true***
  Positions   `minCoord`     `-1`                     `minCoord="2"`        *gives the coordinate on which we want to monitor the minimum displacement of a set of dofs, **ExportPositions** must be set to **true***
  Positions   `maxCoord`     `-1`                     `maxCoord="1"`        *gives the coordinate on which we want to monitor the minimum displacement of a set of dofs, **ExportPositions** must be set to **true***
  Positions   `dispCoord`    `-1`                     `dispCoord="0"`       *gives the coordinate on which we want to export the displacement of the given dofs, **ExportPositions** must be set to **true***
  ----------- -------------- ------------------------ --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------


