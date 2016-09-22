# SOFA Logging


## Main classes 

All the following classes are in the namespace *sofa::core::objectmodel::helper::logging*.

Source files are located in *SofaKernel/framework/sofa/helper/logging/* 

### Message

A *Message* object encapsulates everything about an output message:

* source file and line number from where the message was emitted
* message type (info, deprecated, warning, fatal)
* message class (dev, runtime)
* sender name (std::string) 

### MessageHandler (abstract class)

A *MessageHandler* object is in charge of doing things wich every emitted messages. This can be console ouput, file logging, whatever you can imagine. For example: some unit-tests use a specific *MessageHandler* to catch error messages.

Available [MessageHandler](#MessageHandler) classes:

* ClangMessageHandler
* ConsoleMessageHandler
* ExceptionMessageHandler
* SilentMessageHandler

### MessageFormatter (abstract class)

A *MessageFormatter* object has only one purpose, which is translate a *Message* object to a *std::ostream*.

Available *MessageFormatter* classes:

* DefaultStyleMessageFormatter
* ClangStyleMessageFormatter

### MessageDispatcher (static class)

The *MessageDispatcher* is in charge of sending messages to every [MessageHandler](#MessageHandler) registered.

By default, only a *ConsoleMessageHandler* is registered.

## Macros and typical use

The macros are not in a namespace, for ease of use. 

There are 2 macros categories:

* **runtime macros** to emmit messages in every context.
* **debug macros** 

Typically, to output a message you can use one of these macros, depending of the criticality level:

* msg_info
* msg_deprecated
* msg_warning
* msg_error
* msg_fatal

Just include *Messaging.h* and you can use these macros like any output stream:

```
#include <sofa/helper/logging/Messaging.h>
```

```
msg_warning("GUIManager") << "WARNING(SofaGUI): Previously used GUI not registered. Using default GUI.";
```

## Customization

If you implement a specific [MessageHandler](#MessageHandler) and regiter it in the [MessageDispatcher](#MessageDispatcher), you will be able to receive every single message from the whole SOFA executable. 

Since you will receive [Message](#Message) objects, every useful informations will be available: source code location, type, class, sender, and obviously the message itself.

### example: unit-testing

Take a look at the file *applications/plugins/SofaTest/TestMessageHandler.h*

This is a typical example of a specific use of message handling, not to report anything but only to **detect** errors by error messages emission:

```cpp
/// each ERROR and FATAL message raises a gtest error
class SOFA_TestPlugin_API TestMessageHandler : public MessageHandler
{
public:

    /// raises a gtest error as soon as message is an error
    /// iff the handler is active (see setActive)
    virtual void process(Message &m)
    {
        if( active && m.type()>=Message::Error )
            ADD_FAILURE() << std::endl;
    }
```
