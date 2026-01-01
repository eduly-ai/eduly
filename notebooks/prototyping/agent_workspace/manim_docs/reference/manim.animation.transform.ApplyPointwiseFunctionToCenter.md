# ApplyPointwiseFunctionToCenter

Qualified name: `manim.animation.transform.ApplyPointwiseFunctionToCenter`

### *class* ApplyPointwiseFunctionToCenter(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`ApplyPointwiseFunction`](manim.animation.transform.ApplyPointwiseFunction.md#manim.animation.transform.ApplyPointwiseFunction)

### Methods

| [`begin`](#manim.animation.transform.ApplyPointwiseFunctionToCenter.begin)   | Begin the animation.   |
|------------------------------------------------------------------------------|------------------------|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |
* **Parameters:**
  * **function** (*types.MethodType*)
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))

#### \_original_\_init_\_(function, mobject, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **function** (*MethodType*)
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
* **Return type:**
  None

#### begin()

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

* **Return type:**
  None
