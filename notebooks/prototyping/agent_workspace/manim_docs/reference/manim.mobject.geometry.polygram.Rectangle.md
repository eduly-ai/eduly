# Rectangle

Qualified name: `manim.mobject.geometry.polygram.Rectangle`

### *class* Rectangle(color=ManimColor('#FFFFFF'), height=2.0, width=4.0, grid_xstep=None, grid_ystep=None, mark_paths_closed=True, close_new_points=True, \*\*kwargs)

Bases: [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon)

A quadrilateral with two sets of parallel sides.

* **Parameters:**
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the rectangle.
  * **height** (*float*) – The vertical height of the rectangle.
  * **width** (*float*) – The horizontal width of the rectangle.
  * **grid_xstep** (*float* *|* *None*) – Space between vertical grid lines.
  * **grid_ystep** (*float* *|* *None*) – Space between horizontal grid lines.
  * **mark_paths_closed** (*bool*) – No purpose.
  * **close_new_points** (*bool*) – No purpose.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon)

### Examples

### Methods

### Attributes

| `animate`             | Used to animate the application of any method of `self`.               |
|-----------------------|------------------------------------------------------------------------|
| `animation_overrides` |                                                                        |
| `color`               |                                                                        |
| `depth`               | The depth of the mobject.                                              |
| `fill_color`          | If there are multiple colors (for gradient) this returns the first one |
| `height`              | The height of the mobject.                                             |
| `n_points_per_curve`  |                                                                        |
| `sheen_factor`        |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |

#### \_original_\_init_\_(color=ManimColor('#FFFFFF'), height=2.0, width=4.0, grid_xstep=None, grid_ystep=None, mark_paths_closed=True, close_new_points=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **height** (*float*)
  * **width** (*float*)
  * **grid_xstep** (*float* *|* *None*)
  * **grid_ystep** (*float* *|* *None*)
  * **mark_paths_closed** (*bool*)
  * **close_new_points** (*bool*)
  * **kwargs** (*Any*)
