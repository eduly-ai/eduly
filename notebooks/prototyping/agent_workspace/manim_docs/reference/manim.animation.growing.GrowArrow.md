# GrowArrow

Qualified name: `manim.animation.growing.GrowArrow`

### *class* GrowArrow(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`GrowFromPoint`](manim.animation.growing.GrowFromPoint.md#manim.animation.growing.GrowFromPoint)

Introduce an [`Arrow`](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow) by growing it from its start toward its tip.

* **Parameters:**
  * **arrow** ([*Arrow*](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow)) – The arrow to be introduced.
  * **point_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – Initial color of the arrow before growing to its full size. Leave empty to match arrow’s color.
  * **kwargs** (*Any*)

### Examples

### Methods

| `create_starting_mobject`   |    |
|-----------------------------|----|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(arrow, point_color=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **arrow** ([*Arrow*](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow))
  * **point_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **kwargs** (*Any*)
