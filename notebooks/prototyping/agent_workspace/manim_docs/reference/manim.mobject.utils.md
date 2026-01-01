# utils

Utilities for working with mobjects.

### Functions

### get_mobject_class()

Gets the base mobject class, depending on the currently active renderer.

#### NOTE
This method is intended to be used in the code base of Manim itself
or in plugins where code should work independent of the selected
renderer.

### Examples

The function has to be explicitly imported. We test that
the name of the returned class is one of the known mobject
base classes:

```default
>>> from manim.mobject.utils import get_mobject_class
>>> get_mobject_class().__name__ in ['Mobject', 'OpenGLMobject']
True
```

* **Return type:**
  type

### get_point_mobject_class()

Gets the point cloud mobject class, depending on the currently
active renderer.

#### NOTE
This method is intended to be used in the code base of Manim itself
or in plugins where code should work independent of the selected
renderer.

### Examples

The function has to be explicitly imported. We test that
the name of the returned class is one of the known mobject
base classes:

```default
>>> from manim.mobject.utils import get_point_mobject_class
>>> get_point_mobject_class().__name__ in ['PMobject', 'OpenGLPMobject']
True
```

* **Return type:**
  type

### get_vectorized_mobject_class()

Gets the vectorized mobject class, depending on the currently
active renderer.

#### NOTE
This method is intended to be used in the code base of Manim itself
or in plugins where code should work independent of the selected
renderer.

### Examples

The function has to be explicitly imported. We test that
the name of the returned class is one of the known mobject
base classes:

```default
>>> from manim.mobject.utils import get_vectorized_mobject_class
>>> get_vectorized_mobject_class().__name__ in ['VMobject', 'OpenGLVMobject']
True
```

* **Return type:**
  type
