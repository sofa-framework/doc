## BeamLinearMapping_mt

This component inherits all the functionality from the BeamLinearMapping component and overrides three virtual functions that contain a `for` loop: `apply()`, `applyJ()` and `applyJT()`.
It adds only one data attribute, the granularity. This attribute sets the number of iterations of the `for` loop, corresponding to the number of points along the beam elements that must be assigned and executed for each task.
If this number is lower than the number of iterations the loop won't be parallelized, and the corresponding BeamLinearMapping function is called.
If this number is greater than the number of iterations of the loop the tasks are created, and each task executes the granularity value of iterations of the loop.
