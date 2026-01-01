# Wiggle

Qualified name: `manim.animation.indication.Wiggle`

### *class* Wiggle(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

Wiggle a Mobject.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to wiggle.
  * **scale_value** (*float*) – The factor by which the mobject will be temporarily scaled.
  * **rotation_angle** (*float*) – The wiggle angle.
  * **n_wiggles** (*int*) – The number of wiggles.
  * **scale_about_point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*) – The point about which the mobject gets scaled.
  * **rotate_about_point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*) – The point around which the mobject gets rotated.
  * **run_time** (*float*) – The duration of the animation
  * **kwargs** (*Any*)

### Examples

### Methods

| `get_rotate_about_point`   |    |
|----------------------------|----|
| `get_scale_about_point`    |    |
| `interpolate_submobject`   |    |

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(mobject, scale_value=1.1, rotation_angle=0.06283185307179587, n_wiggles=6, scale_about_point=None, rotate_about_point=None, run_time=2, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **scale_value** (*float*)
  * **rotation_angle** (*float*)
  * **n_wiggles** (*int*)
  * **scale_about_point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*)
  * **rotate_about_point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*)
  * **run_time** (*float*)
  * **kwargs** (*Any*)
