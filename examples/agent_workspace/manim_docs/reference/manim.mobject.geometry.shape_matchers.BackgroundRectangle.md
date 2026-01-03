# BackgroundRectangle

Qualified name: `manim.mobject.geometry.shape\_matchers.BackgroundRectangle`

### *class* BackgroundRectangle(\*mobjects, color=None, stroke_width=0, stroke_opacity=0, fill_opacity=0.75, buff=0, \*\*kwargs)

Bases: [`SurroundingRectangle`](manim.mobject.geometry.shape_matchers.SurroundingRectangle.md#manim.mobject.geometry.shape_matchers.SurroundingRectangle)

A background rectangle. Its default color is the background color
of the scene.

### Examples

### Methods

| [`get_fill_color`](#manim.mobject.geometry.shape_matchers.BackgroundRectangle.get_fill_color)                     | If there are multiple colors (for gradient) this returns the first one                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`pointwise_become_partial`](#manim.mobject.geometry.shape_matchers.BackgroundRectangle.pointwise_become_partial) | Given a 2nd [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) `vmobject`, a lower bound `a` and an upper bound `b`, modify this [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)'s points to match the portion of the Bézier spline described by `vmobject.points` with the parameter `t` between `a` and `b`. |
| `set_style`                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                               |

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
  * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **stroke_width** (*float*)
  * **stroke_opacity** (*float*)
  * **fill_opacity** (*float*)
  * **buff** (*float* *|* *tuple* *[**float* *,* *float* *]*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(\*mobjects, color=None, stroke_width=0, stroke_opacity=0, fill_opacity=0.75, buff=0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **stroke_width** (*float*)
  * **stroke_opacity** (*float*)
  * **fill_opacity** (*float*)
  * **buff** (*float* *|* *tuple* *[**float* *,* *float* *]*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### get_fill_color()

If there are multiple colors (for gradient)
this returns the first one

* **Return type:**
  [*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)

#### pointwise_become_partial(mobject, a, b)

Given a 2nd [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) `vmobject`, a lower bound `a` and
an upper bound `b`, modify this [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)’s points to
match the portion of the Bézier spline described by `vmobject.points`
with the parameter `t` between `a` and `b`.

* **Parameters:**
  * **vmobject** – The [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) that will serve as a model.
  * **a** (*Any*) – The lower bound for `t`.
  * **b** (*float*) – The upper bound for `t`
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
* **Returns:**
  The [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) itself, after the transformation.
* **Return type:**
  [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)
* **Raises:**
  **TypeError** – If `vmobject` is not an instance of `VMobject`.
