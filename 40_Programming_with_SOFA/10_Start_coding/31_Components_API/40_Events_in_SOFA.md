Recovering the events from the keyboard or the mouse can be very useful
for interactive simulation (ex: controlling surgical instruments) There
is already implemented in SOFA a very easy way to access these so-called
events during the simulation. To access the event within a SOFA
component, you need:

-   **handleEvent()** function: you need to define the inherited
    function handleEvent. A nice example is available in the component:
    BaseController.cpp (see at line 71).
-   **f\_listening** parameter: activate the boolean f\_listening by the
    function handleEvent in order to listen to the events. This boolean
    is not activated by default.The best way to activate it is to
    specify it in the scene file that while writing "listening=1". You
    can otherwise "hard" code it in your C++ component as
    follow "myComponent.f\_listening.setValue(true)".

Now, you will be able to recover the events and therefore to interact
with your simulation. Have fun !

If you still don't receive events, it may be possible than you will need to press Ctrl key.

Mouse or Keyboard Events
------------------------

``` cpp
template< class DataTypes>
void myComponent< datatypes >::handleEvent(core::objectmodel::Event *event)
{
    // Key pressed event
    if(KeypressedEvent* ev = dynamic_cast< keypressedevent *>(event))
    {
        switch(ev->getKey())
        {
            // The key M is pressed
            case 'M':
            case 'm':
            {
            ....
            }
        }
    }


    // Mouse Events
    if(MouseEvent* ev = dynamic_cast< mouseevent *>(event))
    {
        switch(ev->getState())
        {
            // The left key of the mouse is pressed
            case MouseEvent::LeftPressed:
            {
            ....
            }
        }
    }
}
```

Specific integration events
---------------------------

In the same way than for Mouse or Keyboard events, you can detect
specific events during the time integration. These events are managed
and sent by the AnimationLoop you are using. The most common events are:

-   BeginAnimationStep: start of a time step
-   EndAnimationStep: end of a time step
-   CollisionBeginEvent: start of the collision phase
-   CollisionEndEvent: end of the collision phase

``` cpp
template< class DataTypes>
void myComponent< datatypes >::handleEvent(core::objectmodel::Event *event)
{
    // Begin of the animation step
    if (dynamic_cast< sofa::simulation::AnimateBeginEvent *>(event))
    {
            ...
    }


    // End of the animation step
    if (dynamic_cast< sofa::simulation::AnimateEndEvent *>(event))
    {
            ...
    }
}
```
