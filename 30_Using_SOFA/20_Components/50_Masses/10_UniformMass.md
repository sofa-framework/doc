UniformMass  
===========


The UniformMass is a mass contributing to



Description of the component

What it is made for, what it does



Data  
----
**vertexMass**
**totalMass**


Usage
-----

How to use it, what **required** component, case

mstate

In which case it works, in which case it doesn't

Limitations



Example
-------

This component is used as follows in XML format:

``` xml
<UniformMass totalMass="10" />
```

or using Python:

``` python
node.createObject('UniformMass', totalMass='10')
```

An example scene involving a UniformMass is available in [*examples/Components/mass/UniformMass.scn*](https://github.com/sofa-framework/sofa/blob/master/examples/Components/mass/UniformMass.scn)