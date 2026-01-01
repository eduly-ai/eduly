# ApplyMethod

Qualified name: `manim.animation.transform.ApplyMethod`

### *class* ApplyMethod(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Animates a mobject by applying a method.

Note that only the method needs to be passed to this animation,
it is not required to pass the corresponding mobject. Furthermore,
this animation class only works if the method returns the modified
mobject.

* **Parameters:**
  * **method** (*Callable*) – The method that will be applied in the animation.
  * **args** – Any positional arguments to be passed when applying the method.
  * **kwargs** – Any keyword arguments passed to [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform).

### Methods

| `check_validity_of_input`   |    |
|-----------------------------|----|
| `create_target`             |    |

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(method, \*args, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  **method** (*Callable*)
* **Return type:**
  None
