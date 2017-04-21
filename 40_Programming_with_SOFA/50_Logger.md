# SOFA Logging


## Main classes 

All the following classes are in the namespace *sofa::core::objectmodel::helper::logging*.

Source files are located in *SofaKernel/framework/sofa/helper/logging/* 

### Message

A *Message* object encapsulates everything about an output message:

* source file and line number from where the message was emitted
* message type (info, deprecated, warning, error, fatal)
* message class (dev, runtime)
* sender name (std::string) 
* sender extra information 
* text (std::string) with the actual content of the message

Messages text description can also contain markdown syntax to improve their rendering when used in a graphical application. Supported syntax
include emphasizing with `''`, `url's []()`, `double space` for new line.  

### MessageHandler (abstract class)

A *MessageHandler* object is in charge of processing and actually 'doing something' of the emitted messages. This can be displaying the message in the console, logging them into file, logging them into a GUI, ...., whatever you can imagine. For example: some unit-tests use a specific *MessageHandler* to catch error messages.

Available [MessageHandler](#MessageHandler) classes:

* FileMessageHandler writes textual representation of the messages in a file. 
* ClangMessageHandler writes a clang-syntax textual representation of the message in the console (for integration with IDE). 
* ConsoleMessageHandler writes a formatted representation of the message in the console. 
* ExceptionMessageHandler throw an exception for each message. 
* SilentMessageHandler  do nothing. 
* CountingMessageHandler counts the number of messages per message type (advice, info, deprecated, warning, error, fatal)
* LogginMessageHandler logs all the messages in a single message queue. 
* PerComponentLoggingMessageHandler logs the message in the component that emits them. 
* RoutingMessageHandler routes the messages to different handlers according to an user provided function.

### MessageFormatter (abstract class)

A *MessageFormatter* object has only one purpose, which is translate a *Message* object to a *std::ostream*.

Available *MessageFormatter* classes:

* DefaultStyleMessageFormatter
* ClangStyleMessageFormatter
* RichConsoleStyleMessageFormatter that convert messages into a good looking rendering for the console.

### MessageDispatcher (static class)

The *MessageDispatcher* is in charge of sending messages to every [MessageHandler](#MessageHandler) registered.

By default, only a *ConsoleMessageHandler* is registered.

## Macros and typical use

The macros are not in a namespace, for ease of use. 

There are 2 macros categories:

* **runtime macros** to emmit messages in every context.
* **developper's macros** to emmit messages only targetted to developpers (people willing to dive into the sofa source code)

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

If you are in a component (an object inheriting from 'Base') you should use
```
msg_warning() << "Previously used GUI not registered. Using default GUI.";
or
msg_warning(this) << "Previously used GUI not registered. Using default GUI.";
```

You can also send a message binded to a different component as in:
```
msg_warning(otherComponent) << "Previously used GUI not registered. Using default GUI.";
```

Finally if you are not in a sofa component you can specify the emitter's name with a string. 
```
msg_warning("GUIManager") << "Previously used GUI not registered. Using default GUI.";
```

If your message is for developper you can use the dmsg_info, dmsg_deprecated, dmsg_warning,... function. 
These messages are removed on end-user application and can be more specific and less well written as the one
that targets users. A very simple to guide the use of the dmsg_* API is to ask yourself if fixing the message needs to have the sourcode understand the message. 

## How are handled the messages in Sofa Component
Component have a 'printLog' data field that controls whether or not the msg_info() are emitted on the component side. An user that don't want the component to emit info messages have to set the 'printLog' to false. There is no equivalent way to prevent warning/error/fatal message to be emitted. The reason is that they are important in indicating the state of the sofa component and other componant may use them to validate that the componant is in a valid state. 

The fact that the warning/error and fatal message are always emitted by the component does not means the have to be showed to the user. If needed a third party application can implement its own message handler discarding (on demand) instead of printing 
these messages. 

## Message and unit-testing
Messages plays an important role in Sofa as they are the principal way to convey informations on the 
component state. Message are part of the behavior of a component and should be tested accordingly. 

For that there is two dedicated class in the file *applications/plugins/SofaTest/TestMessageHandler.h*

Using these class you can test that a component has emitted a message (as it should in the tested conditin) or the contrary, 
that a component emitted a message while it was not supposed to. 

```cpp
TEST_F(MyComponent, testAValidUsageThatShouldnotSendMessage)
{
	MessageAsTestFailure warning(Message::Warning);
	MessageAsTestFailure error(Message::Error);
	
	this->doSomething("validFile.obj") ;
}

``` 

Or
```cpp
TEST_F(MyComponent, testAnInvalidUsageThatShouldnotSendMessage)
{
	MessageAsTestFailure warning(Message::Warning);
	ExpectMessage error(Message::Error);
	
	this->doSomething("invalidFile.obj") ; 
}

``` 

When the condition is not respected this produce a test failure. 

## Customization
If you implement a specific [MessageHandler](#MessageHandler) and regiter it in the [MessageDispatcher](#MessageDispatcher), you will be able to receive every single message from the whole SOFA executable. 

Since you will receive [Message](#Message) objects, every useful informations will be available: source code location, type, class, sender, and obviously the message itself.


