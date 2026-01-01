# MethodWithArgs

Qualified name: `manim.data\_structures.MethodWithArgs`

### *class* MethodWithArgs(method, args, kwargs)

Bases: `object`

Object containing a [`method`](#manim.data_structures.MethodWithArgs.method) which is intended to be called later
with the positional arguments [`args`](#manim.data_structures.MethodWithArgs.args) and the keyword arguments
[`kwargs`](#manim.data_structures.MethodWithArgs.kwargs).

* **Parameters:**
  * **method** (*MethodType*)
  * **args** (*Iterable* *[**Any* *]*)
  * **kwargs** (*dict* *[**str* *,* *Any* *]*)

#### method

A callable representing a method of some class.

* **Type:**
  MethodType

#### args

Positional arguments for [`method`](#manim.data_structures.MethodWithArgs.method).

* **Type:**
  Iterable[Any]

#### kwargs

Keyword arguments for [`method`](#manim.data_structures.MethodWithArgs.method).

* **Type:**
  dict[str, Any]

### Methods

### Attributes

| [`method`](#manim.data_structures.MethodWithArgs.method)   |    |
|------------------------------------------------------------|----|
| [`args`](#manim.data_structures.MethodWithArgs.args)       |    |
| [`kwargs`](#manim.data_structures.MethodWithArgs.kwargs)   |    |
