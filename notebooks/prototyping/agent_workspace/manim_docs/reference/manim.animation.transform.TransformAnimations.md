# TransformAnimations

Qualified name: `manim.animation.transform.TransformAnimations`

### *class* TransformAnimations(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

### Methods

| [`interpolate`](#manim.animation.transform.TransformAnimations.interpolate)   | Set the animation progress.   |
|-------------------------------------------------------------------------------|-------------------------------|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |
* **Parameters:**
  * **start_anim** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
  * **end_anim** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
  * **rate_func** (*Callable*)

#### \_original_\_init_\_(start_anim, end_anim, rate_func=<function squish_rate_func.<locals>.result>, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **start_anim** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
  * **end_anim** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
  * **rate_func** (*Callable*)
* **Return type:**
  None

#### interpolate(alpha)

Set the animation progress.

This method gets called for every frame during an animation.

* **Parameters:**
  **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
  the end.
* **Return type:**
  None
