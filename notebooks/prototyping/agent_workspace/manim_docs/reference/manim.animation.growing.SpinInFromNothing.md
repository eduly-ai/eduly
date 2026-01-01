# SpinInFromNothing

Qualified name: `manim.animation.growing.SpinInFromNothing`

### *class* SpinInFromNothing(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`GrowFromCenter`](manim.animation.growing.GrowFromCenter.md#manim.animation.growing.GrowFromCenter)

Introduce an [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) spinning and growing it from its center.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to be introduced.
  * **angle** (*float*) – The amount of spinning before mobject reaches its full size. E.g. 2\*PI means
    that the object will do one full spin before being fully introduced.
  * **point_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.
  * **kwargs** (*Any*)

### Examples

### Methods

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, angle=1.5707963267948966, point_color=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **angle** (*float*)
  * **point_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **kwargs** (*Any*)
