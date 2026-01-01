# FocusOn

Qualified name: `manim.animation.indication.FocusOn`

### *class* FocusOn(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Shrink a spotlight to a position.

* **Parameters:**
  * **focus_point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The point at which to shrink the spotlight. If it is a `Mobject` its center will be used.
  * **opacity** (*float*) – The opacity of the spotlight.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the spotlight.
  * **run_time** (*float*) – The duration of the animation.
  * **kwargs** (*Any*)

### Examples

### Methods

| `create_target`   |    |
|-------------------|----|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(focus_point, opacity=0.2, color=ManimColor('#888888'), run_time=2, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **focus_point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **opacity** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **run_time** (*float*)
  * **kwargs** (*Any*)
