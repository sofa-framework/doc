# Deprecation macros

## The 2 base macros

**Do not use them directly in your code**, see "how to use them" below.

`SOFA_ATTRIBUTE_DEPRECATED(deprecateDate, removeDate, toFixMsg)`
To be used to trigger a deprecation warning. It is a simple `[[deprecated]]` interface.
Warns that something
&nbsp;&nbsp;&nbsp; - is DEPRECATED (so still usable) since `deprecateDate`
&nbsp;&nbsp;&nbsp; - will be removed on `removeDate`
and gives the toFixMsg instructions to fix the deprecation warning.
    
`SOFA_ATTRIBUTE_DISABLED(deprecateDate, disableDate, toFixMsg)`
To be used jointly with `= delete` to trigger an error. It is a flavored `[[deprecated]]` interface.
Warns that something  
&nbsp;&nbsp;&nbsp; - is DISABLED (so not usable anymore) since `disabledDate`
&nbsp;&nbsp;&nbsp; - was firstly deprecated on `deprecateDate`
and gives the toFixMsg instructions to fix the compilation error.


## How to use them

Create a new deprecation macro specifying the deprecation topic you are tackling.
This way, you won't have dates everywhere in your code.

## Example

### Deprecate

I want to rename something that will break my API. 
To ease the transition for my users, I will propose a deprecation period with a fine message by using a deprecation macro.
Latest release is v20.06, next release (currently under development) is v20.12, after that will come the v21.06.

In my config.h.in
```cpp
#define SOFA_ATTRIBUTE_DEPRECATED__MYDEPRECATIONTOPIC() \
    SOFA_ATTRIBUTE_DEPRECATED( \
        "v20.12 (PR#12345)", "v21.06", \
        "XXX must be renamed into YYY.")
```

In my code
```cpp
SOFA_ATTRIBUTE_DEPRECATED__MYDEPRECATIONTOPIC()
void myDeprecatedMethod();
```

Anyone using myDeprecatedMethod will get this **warning**: 
```text
warning: 'myDeprecatedMethod' is deprecated: It is still usable but has been DEPRECATED since v20.12 (PR#12345). You have until v21.06 to fix your code. XXX must be renamed into YYY.
```

### Disable

Now forward in time ...
Latest release is v20.12, next release (currently under development) is v21.06, after that will come the v21.12.
It is time to stop the deprecation period. To provide a clear message to my users, I will not just remove my deprecated method but I will disable it with `= delete` and use a deprecation macro.

In my config.h.in
```cpp
#define SOFA_ATTRIBUTE_DISABLED__MYDEPRECATIONTOPIC() \
    SOFA_ATTRIBUTE_DISABLED( \
        "v20.12 (PR#12345)", "v21.06 (PR#45678)", \
        "XXX must be renamed into YYY.")
```

In my code
```cpp
SOFA_ATTRIBUTE_DISABLED__MYDEPRECATIONTOPIC()
void myDeprecatedMethod() = delete;
```

Anyone using myDeprecatedMethod will get an **error** right after this warning: 
```text
warning: 'myDeprecatedMethod' is deprecated: It is not usable anymore because it has been DISABLED since v21.06 (PR#45678) after being deprecated on v20.12 (PR#12345). XXX must be renamed into YYY.
```


