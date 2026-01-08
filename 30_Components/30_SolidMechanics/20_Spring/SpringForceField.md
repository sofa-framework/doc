# SpringForceField

This component implements a physics-based spring force field for simulating elastic connections between particles or points. It's designed for modeling systems where objects are connected by springs (e.g., molecular dynamics, cloth simulation, soft tissue modeling).

## Overview
The `SpringForceField` component creates a physics-based spring system that:
- Applies Hooke's law forces proportional to displacement from rest length
- Includes viscous damping for energy dissipation
- Supports individual spring properties (stiffness, damping, rest length, activation state)
- Handles topological changes automatically
- Provides visualization options for debugging

## Physics Model
The component implements a linear spring model where each connection (spring) provides the force model:

$$
\mathbf{F} = k_s (l - l_0) \; \mathbf{u} + k_d (\mathbf{v} ·\mathbf{u}) \; \mathbf{u}
$$

where:
- `k_s` = Spring stiffness
- `l` = Current length
- `l_0` = Rest length
- `u` = Unit vector along spring
- `v` = Relative velocity
- `k_d` = Damping coefficient
