Collision Group Managers
========================

The collision group manager components are used in a [collision pipeline](https://www.sofa-framework.org/community/doc/using-sofa/components/collisions/pipelines/collisionpipeline).

The role of a collision group manager is to find and merge solvers for a contact, i.e. two different objects in collision, into groups.
The term 'group' refers to a group of integration components.
It includes an [ODE solver](https://www.sofa-framework.org/community/doc/using-sofa/simulation-principles/system-resolution/integration-scheme), its associated [linear solver](https://www.sofa-framework.org/community/doc/simulation-principles/system-resolution/linear-solver/) and the [constraint solver](https://www.sofa-framework.org/community/doc/using-sofa/simulation-principles/constraint/lagrange-constraint).
_DefaultCollisionGroupManager_ modifies the scene graph so that two objects in contact share the same node with a single integration algorithm.
In that case, the integration algorithm solves the ODE of the two objects simultaneously.

In [DefaultPipeline](https://www.sofa-framework.org/community/doc/using-sofa/components/collisions/pipelines/defaultpipeline), groups are created only for contacts between two non-static objects.

After creating the groups, _DefaultCollisionGroupManager_ is also in charge to create the contact responses. 

## Merging Two Integration Nodes

It is possible that two objects in contact are not solved with the same type of solver.
For example, _objectA_ can be solved with [EulerImplicitSolver](https://www.sofa-framework.org/community/doc/components/integrationschemes/eulerimplicitsolver/), and _objectB_ with [EulerExplicitSolver](https://www.sofa-framework.org/community/doc/components/integrationschemes/eulerexplicitsolver/).
In that case, some rules are pre-defined to select which one is kept.
The other one is removed.
Usually, the more stable or precise solver is prefered.
For example, [EulerImplicitSolver](https://www.sofa-framework.org/community/doc/components/integrationschemes/eulerimplicitsolver/), is prefered over [EulerExplicitSolver](https://www.sofa-framework.org/community/doc/components/integrationschemes/eulerexplicitsolver/).

In case both ODE solvers are of the same type, but still a different instance, pre-defined rules merge Data values of both ODE solvers.

Similar rules also exist for the linear solvers.
For example, if two conjugate gradient solvers are merged, the maximum number of iterations will be the highest value of both solvers.

Similarly, pre-defined rules merge Data values of two constraint solvers (only LCPConstraintSolver).

Interaction with Other Components
==============

A collision group manager is optional in a simulation scene.
A [collision pipeline](https://www.sofa-framework.org/community/doc/using-sofa/components/collisions/pipelines/collisionpipeline) uses it if one is defined in the scene.
It is usually a good practice to place the group manager near the [collision pipeline](https://www.sofa-framework.org/community/doc/using-sofa/components/collisions/pipelines/collisionpipeline), at the same level (not in a child node).

Implementation
==============

The following function must be called in the [collision pipeline](https://www.sofa-framework.org/community/doc/using-sofa/components/collisions/pipelines/collisionpipeline), once contacts have been detected:
```cpp
/// Create the integration groups
void CollisionGroupManager::createGroups(objectmodel::BaseContext* scene, const sofa::helper::vector<Contact::SPtr>& contacts)
```

Contacts are provided through the contact manager:
```cpp
const helper::vector<Contact::SPtr>& contacts = contactManager->getContacts();
```

Examples of Components
======================

The following components are collision group managers, and can be placed in a simulation scene:
- DefaultCollisionGroupManager (plugin SofaMiscCollision)

Inheritance Diagram
===================

<a href="https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1core_1_1collision_1_1_collision_group_manager.html">
<img src="https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1core_1_1collision_1_1_collision_group_manager__inherit__graph.png" title="NarrowPhaseDetection diagram class"/>
</a>

Read more on [SOFA API documentation](https://www.sofa-framework.org/api/master/sofa/html/classsofa_1_1core_1_1collision_1_1_collision_group_manager.html)