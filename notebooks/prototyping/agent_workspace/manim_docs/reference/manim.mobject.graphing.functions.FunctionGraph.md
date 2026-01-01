# FunctionGraph

Qualified name: `manim.mobject.graphing.functions.FunctionGraph`

### *class* FunctionGraph(function, x_range=None, color=ManimColor('#FFFF00'), \*\*kwargs)

Bases: [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)

A [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction) that spans the length of the scene by default.

### Examples

### Methods

| `get_function`            |    |
|---------------------------|----|
| `get_point_from_function` |    |

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
  * **function** (*Callable* *[* *[**float* *]* *,* *Any* *]*)
  * **x_range** (*tuple* *[**float* *,* *float* *]*  *|* *tuple* *[**float* *,* *float* *,* *float* *]*  *|* *None*)
  * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor))
  * **kwargs** (*Any*)

#### \_original_\_init_\_(function, x_range=None, color=ManimColor('#FFFF00'), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **function** (*Callable* *[* *[**float* *]* *,* *Any* *]*)
  * **x_range** (*tuple* *[**float* *,* *float* *]*  *|* *tuple* *[**float* *,* *float* *,* *float* *]*  *|* *None*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **kwargs** (*Any*)
* **Return type:**
  None
