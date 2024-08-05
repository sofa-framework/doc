---
title: Pause the animation
---

Pause the Animation
-------------------

Sometimes, you would like the animation to be paused without pressing
any button but from the **Simulation** itself. For example if solver
does not converge, you might want to stop the animation so you can look
at it carefully, or because the interesting part is over. This is now
possible, using a **PauseAnimation** component. This component has a
method *pause()* that tells the Simulation it should paused using
*setPaused()* a write accessor on the Simulation field paused. The
RealGUI step() we check the state of the Simulation to know if we should
stop the Animation, pressing back the Animate button.

#### PauseAnimationOnEvent

**PauseAnimationOnEvent** is derived from **PauseAnimation** and handles
*PauseEvent* event. When it receives this event, it calls the *pause()*
method. Add the following component on your scene description:

```xml
listening="true"
```

Then launch the PauseEvent where you want to in your code. For example,
when your solver does not succeed to converge, or when the simulated end
time has been reached... (To learn how to launch a visitor).

#### Quick component hierarchy overview

\[caption id="attachment\_1551" align="aligncenter"
width="350"\][![PauseAnimation
architecture](https://www.sofa-framework.org/wp-content/uploads/2014/11/350px-PauseAnimation1.png){.size-full
.wp-image-1551 width="350"
height="239"}](https://www.sofa-framework.org/wp-content/uploads/2014/11/350px-PauseAnimation1.png)
PauseAnimation architecture\[/caption\]
