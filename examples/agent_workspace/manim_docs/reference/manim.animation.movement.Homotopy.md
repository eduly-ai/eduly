# Homotopy

Qualified name: `manim.animation.movement.Homotopy`

### *class* Homotopy(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

A Homotopy.

This is an animation transforming the points of a mobject according
to the specified transformation function. With the parameter $t$
moving from 0 to 1 throughout the animation and $(x, y, z)$
describing the coordinates of the point of a mobject,
the function passed to the `homotopy` keyword argument should
transform the tuple $(x, y, z, t)$ to $(x', y', z')$,
the coordinates the original point is transformed to at time $t$.

* **Parameters:**
  * **homotopy** (*Callable* *[* *[**float* *,* *float* *,* *float* *,* *float* *]* *,* *tuple* *[**float* *,* *float* *,* *float* *]* *]*) – A function mapping $(x, y, z, t)$ to $(x', y', z')$.
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject transformed under the given homotopy.
  * **run_time** (*float*) – The run time of the animation.
  * **apply_function_kwargs** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – Keyword arguments propagated to `Mobject.apply_function()`.
  * **kwargs** (*Any*) – Further keyword arguments passed to the parent class.

### Examples

### Methods

| `function_at_time_t`     |    |
|--------------------------|----|
| `interpolate_submobject` |    |

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(homotopy, mobject, run_time=3, apply_function_kwargs=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **homotopy** (*Callable* *[* *[**float* *,* *float* *,* *float* *,* *float* *]* *,* *tuple* *[**float* *,* *float* *,* *float* *]* *]*)
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **run_time** (*float*)
  * **apply_function_kwargs** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **kwargs** (*Any*)
