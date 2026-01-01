# GrowFromPoint

Qualified name: `manim.animation.growing.GrowFromPoint`

### *class* GrowFromPoint(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Introduce an [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) by growing it from a point.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to be introduced.
  * **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The point from which the mobject grows.
  * **point_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.
  * **kwargs** (*Any*)

### Examples

### Methods

| `create_starting_mobject`   |    |
|-----------------------------|----|
| `create_target`             |    |

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, point, point_color=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **point_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **kwargs** (*Any*)
