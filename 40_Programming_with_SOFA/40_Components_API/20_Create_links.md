A 'Link' allow you to access a sofa component from another one anywhere
in the simulation graph. In your scene creation file, it usually appear
as : input=@../component. In this page we explain how to use it. In your
.h, declare your link :

``` cpp
//Where it comes from (usually you do not need to include it, it is already included)
#include <sofa/core/objectmodel/Link.h>
//Use a typedef to make it readable
typedef sofa::core::objectmodel::SingleLink< FROM_CLASS, TO_CLASS, LINK_FLAG> MyLink;
MyLink mylink;
```

In your constructor use :

``` cpp
MyConstructor::MyConstructor():mylink(initLink('name', 'help')){}
```

The list of flags you can use is available in the [Sofa
API](https://www.sofa-framework.org/api/SOFA/index.html "SOFA API") at
[this specific
place.](https://www.sofa-framework.org/api/SOFA/classsofa_1_1core_1_1objectmodel_1_1_base_link.html#a5e9e323c0eca40c08a8020da6631c1bd "SofaAPIBaseLink")
Here is a link to [the BaseLink
API](https://www.sofa-framework.org/api/SOFA/_base_link_8h.html). Here
is an example from
[mapping.h](https://www.sofa-framework.org/api/SOFA/_mapping_8h_source.html).
See the Mapping.inl for implementation also.
