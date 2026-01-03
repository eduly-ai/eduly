# TracedPath

Qualified name: `manim.animation.changing.TracedPath`

### *class* TracedPath(traced_point_func, stroke_width=2, stroke_color=ManimColor('#FFFFFF'), dissipating_time=None, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

Traces the path of a point returned by a function call.

* **Parameters:**
  * **traced_point_func** (*Callable*) – The function to be traced.
  * **stroke_width** (*float*) – The width of the trace.
  * **stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – The color of the trace.
  * **dissipating_time** (*float* *|* *None*) – The time taken for the path to dissipate. Default set to `None`
    which disables dissipation.
  * **kwargs** (*Any*)

### Examples

### Methods

| `update_path`   |    |
|-----------------|----|

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

#### \_original_\_init_\_(traced_point_func, stroke_width=2, stroke_color=ManimColor('#FFFFFF'), dissipating_time=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **traced_point_func** (*Callable*)
  * **stroke_width** (*float*)
  * **stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **dissipating_time** (*float* *|* *None*)
  * **kwargs** (*Any*)
* **Return type:**
  None
