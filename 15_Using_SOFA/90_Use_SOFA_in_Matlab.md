This was done for Ubuntu.

Launch Matlab preloading libraries that SOFA uses
-------------------------------------------------
In command line, write:

```
LD_PRELOAD=”/usr/lib/x86_64-linux-gnu/libstdc++.so.6:/usr/lib/x86_64-linux-gnu/libQt5OpenGLusr/lib/x86_64-linux-gnu/libQt5Widgets.so.5:/usr/lib/x86_64-linux-gnu/libQt5Gui.so.5:/usr/lib/x86_64-linux-gnu/libQt5Core.so.5″ matlab
```

From a Matlab script launch sofa
--------------------------------
In Matlab, define:

```
pathToSofaScene = fullfile(PATH_TO_SOFA_SCENES, ‘sofaScene.scn’)
[status, result] = system([‘PATH_TO_SOFA_BIN/runSofa -g batch -n 10’ pathToSofaScene]);
```

It reads in result the SOFA terminal output.


__Note__: Matlab plots, and other Qt related functions (write png images) will be a bit broken
