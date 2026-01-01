# AnimatedBoundary

Qualified name: `manim.animation.changing.AnimatedBoundary`

### *class* AnimatedBoundary(vmobject, colors=[ManimColor('#29ABCA'), ManimColor('#9CDCEB'), ManimColor('#236B8E'), ManimColor('#736357')], max_stroke_width=3, cycle_rate=0.5, back_and_forth=True, draw_rate_func=<function smooth>, fade_rate_func=<function smooth>, \*\*kwargs)

Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

Boundary of a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) with animated color change.

### Examples

### Methods

| `full_family_become_partial`   |    |
|--------------------------------|----|
| `update_boundary_copies`       |    |

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
* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
  * **colors** (*Sequence* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*)
  * **max_stroke_width** (*float*)
  * **cycle_rate** (*float*)
  * **back_and_forth** (*bool*)
  * **draw_rate_func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
  * **fade_rate_func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
  * **kwargs** (*Any*)

#### \_original_\_init_\_(vmobject, colors=[ManimColor('#29ABCA'), ManimColor('#9CDCEB'), ManimColor('#236B8E'), ManimColor('#736357')], max_stroke_width=3, cycle_rate=0.5, back_and_forth=True, draw_rate_func=<function smooth>, fade_rate_func=<function smooth>, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
  * **colors** (*Sequence* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*)
  * **max_stroke_width** (*float*)
  * **cycle_rate** (*float*)
  * **back_and_forth** (*bool*)
  * **draw_rate_func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
  * **fade_rate_func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
  * **kwargs** (*Any*)
