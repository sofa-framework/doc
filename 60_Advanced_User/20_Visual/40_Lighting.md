Adding Lights
-------------

One white global light illuminates the scene by default. This can be
changed through a light manager object and a certain number of lights
(limited by OpenGL). The first step is to add the object called
LightManager, preferably at the top of the scene file.

```xml
```

After that, we can add 3 different kinds of lights :

-   a positional light (parameters : color, position) ;

    ```xml
    ```

-   a directional light (parameters : color, direction) ;

    ```xml
    ```

-   a spotlight (parameters : color, position, direction, cut off,
    exponent, attenuation)

    ```xml
    ```

<!-- -->


