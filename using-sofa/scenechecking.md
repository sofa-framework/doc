---
title: SceneChecking
---

# Scene Checking

When the `runSofa` application loads a scene, it performs several verification checks. These checks help ensure the scene follows implicit design rules. If any issues are detected during the verification process, warning messages are displayed in the console.

Using a SOFA built from sources, you can activate or de-activate these checks using the CMake flag `APPLICATION_SCENECHECKING`

| Name | Description |
| ---- | ----------- |
| SceneCheckCollisionResponse | Check that the appropriate components are in the scene to compute the desired collision response |
| SceneCheckDeprecatedComponents | Check there is not deprecated components in the scenegraph |
| SceneCheckDuplicatedName | Check there is not duplicated name in the scenegraph |
| SceneCheckEmptyNodeName | Check if a Node has an empty name. |
| SceneCheckMapping | Check if the mappings and states inside a Node are consistent regarding the visitor logic. |
| SceneCheckMissingRequiredPlugin | Check for each component provided by a plugin that the corresponding <RequiredPlugin> directive is present in the scene |
| SceneCheckUsingAlias | Check if a Component has been created using an Alias. |
