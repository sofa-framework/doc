Adding Lights
-------------

One white global light illuminates the scene by default. This can be
changed through a light manager object and a certain number of lights
(limited by OpenGL). The first step is to add the object called
LightManager, preferably at the top of the scene file.

```xml
<LightManager />
```

After that, we can add 3 different kinds of lights :

-   a positional light (parameters : color, position) ;

    ```xml
    <PositionalLight name="light2" color="0 1 0" attenuation="0.1" position="0.5 -0.7 2" />
    ```

-   a directional light (parameters : color, direction) ;

    ```xml
    <DirectionalLight name="light2" color="0 0 1" direction="1 1 0" />
    ```

-   a spotlight (parameters : color, position, direction, cut off,
    exponent, attenuation)

    ```xml
     <SpotLight name="light1" color="1 0 0" position="0.5 0.7 2" cutoff="25" exponent="1" />
    ```

#### Example

-   example/Component/visualmodel/LightManager.scn


