# Unwrite

Qualified name: `manim.animation.creation.Unwrite`

### *class* Unwrite(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Write`](manim.animation.creation.Write.md#manim.animation.creation.Write)

Simulate erasing by hand a [`Text`](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) or a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).

* **Parameters:**
  * **reverse** (*bool*) – Set True to have the animation start erasing from the last submobject first.
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)

### Examples

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(vmobject, rate_func=<function linear>, reverse=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **reverse** (*bool*)
* **Return type:**
  None
