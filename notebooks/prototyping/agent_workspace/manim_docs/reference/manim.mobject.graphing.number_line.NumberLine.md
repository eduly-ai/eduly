# NumberLine

Qualified name: `manim.mobject.graphing.number\_line.NumberLine`

### *class* NumberLine(x_range=None, length=None, unit_size=1, include_ticks=True, tick_size=0.1, numbers_with_elongated_ticks=None, longer_tick_multiple=2, exclude_origin_tick=False, rotation=0, stroke_width=2.0, include_tip=False, tip_width=0.35, tip_height=0.35, tip_shape=None, include_numbers=False, font_size=36, label_direction=array([ 0., -1., 0.]), label_constructor=<class 'manim.mobject.text.tex_mobject.MathTex'>, scaling=<manim.mobject.graphing.scale.LinearBase object>, line_to_number_buff=0.25, decimal_number_config=None, numbers_to_exclude=None, numbers_to_include=None, \*\*kwargs)

Bases: [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)

Creates a number line with tick marks.

* **Parameters:**
  * **x_range** (*Sequence* *[**float* *]*  *|* *None*) – The `[x_min, x_max, x_step]` values to create the line.
  * **length** (*float* *|* *None*) – The length of the number line.
  * **unit_size** (*float*) – The distance between each tick of the line. Overwritten by `length`, if specified.
  * **include_ticks** (*bool*) – Whether to include ticks on the number line.
  * **tick_size** (*float*) – The length of each tick mark.
  * **numbers_with_elongated_ticks** (*Iterable* *[**float* *]*  *|* *None*) – An iterable of specific values with elongated ticks.
  * **longer_tick_multiple** (*int*) – Influences how many times larger elongated ticks are than regular ticks (2 = 2x).
  * **rotation** (*float*) – The angle (in radians) at which the line is rotated.
  * **stroke_width** (*float*) – The thickness of the line.
  * **include_tip** (*bool*) – Whether to add a tip to the end of the line.
  * **tip_width** (*float*) – The width of the tip.
  * **tip_height** (*float*) – The height of the tip.
  * **tip_shape** (*type* *[*[*ArrowTip*](manim.mobject.geometry.tips.ArrowTip.md#manim.mobject.geometry.tips.ArrowTip) *]*  *|* *None*) – The mobject class used to construct the tip, or `None` (the
    default) for the default arrow tip. Passed classes have to inherit
    from [`ArrowTip`](manim.mobject.geometry.tips.ArrowTip.md#manim.mobject.geometry.tips.ArrowTip).
  * **include_numbers** (*bool*) – Whether to add numbers to the tick marks. The number of decimal places is determined
    by the step size, this default can be overridden by `decimal_number_config`.
  * **scaling** ( *\_ScaleBase*) – The way the `x_range` is value is scaled, i.e. [`LogBase`](manim.mobject.graphing.scale.LogBase.md#manim.mobject.graphing.scale.LogBase) for a logarithmic numberline. Defaults to [`LinearBase`](manim.mobject.graphing.scale.LinearBase.md#manim.mobject.graphing.scale.LinearBase).
  * **font_size** (*float*) – The size of the label mobjects. Defaults to 36.
  * **label_direction** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The specific position to which label mobjects are added on the line.
  * **label_constructor** (*type* *[*[*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *]*) – Determines the mobject class that will be used to construct the labels of the number line.
  * **line_to_number_buff** (*float*) – The distance between the line and the label mobject.
  * **decimal_number_config** (*dict* *|* *None*) – Arguments that can be passed to [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) to influence number mobjects.
  * **numbers_to_exclude** (*Iterable* *[**float* *]*  *|* *None*) – An explicit iterable of numbers to not be added to the number line.
  * **numbers_to_include** (*Iterable* *[**float* *]*  *|* *None*) – An explicit iterable of numbers to add to the number line
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line).
  * **exclude_origin_tick** (*bool*)

#### NOTE
Number ranges that include both negative and positive values will be generated
from the 0 point, and may not include a tick at the min / max
values as the tick locations are dependent on the step size.

### Examples

### Methods

| [`add_labels`](#manim.mobject.graphing.number_line.NumberLine.add_labels)                 | Adds specifically positioned labels to the [`NumberLine`](#manim.mobject.graphing.number_line.NumberLine) using a `dict`.                                                          |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`add_numbers`](#manim.mobject.graphing.number_line.NumberLine.add_numbers)               | Adds [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) mobjects representing their position at each tick of the number line. |
| [`add_ticks`](#manim.mobject.graphing.number_line.NumberLine.add_ticks)                   | Adds ticks to the number line.                                                                                                                                                     |
| `get_labels`                                                                              |                                                                                                                                                                                    |
| [`get_number_mobject`](#manim.mobject.graphing.number_line.NumberLine.get_number_mobject) | Generates a positioned [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) mobject generated according to `label_constructor`. |
| `get_number_mobjects`                                                                     |                                                                                                                                                                                    |
| [`get_tick`](#manim.mobject.graphing.number_line.NumberLine.get_tick)                     | Generates a tick and positions it along the number line.                                                                                                                           |
| `get_tick_marks`                                                                          |                                                                                                                                                                                    |
| [`get_tick_range`](#manim.mobject.graphing.number_line.NumberLine.get_tick_range)         | Generates the range of values on which labels are plotted based on the `x_range` attribute of the number line.                                                                     |
| `get_unit_size`                                                                           |                                                                                                                                                                                    |
| `get_unit_vector`                                                                         |                                                                                                                                                                                    |
| [`n2p`](#manim.mobject.graphing.number_line.NumberLine.n2p)                               | Abbreviation for [`number_to_point()`](#manim.mobject.graphing.number_line.NumberLine.number_to_point).                                                                            |
| [`number_to_point`](#manim.mobject.graphing.number_line.NumberLine.number_to_point)       | Accepts a value along the number line and returns a point with respect to the scene.                                                                                               |
| [`p2n`](#manim.mobject.graphing.number_line.NumberLine.p2n)                               | Abbreviation for [`point_to_number()`](#manim.mobject.graphing.number_line.NumberLine.point_to_number).                                                                            |
| [`point_to_number`](#manim.mobject.graphing.number_line.NumberLine.point_to_number)       | Accepts a point with respect to the scene and returns a float along the number line.                                                                                               |
| `rotate_about_number`                                                                     |                                                                                                                                                                                    |
| `rotate_about_zero`                                                                       |                                                                                                                                                                                    |

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

#### \_create_label_tex(label_tex, label_constructor=None, \*\*kwargs)

Checks if the label is a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject), otherwise, creates a
label by passing `label_tex` to `label_constructor`.

* **Parameters:**
  * **label_tex** (*str* *|* *float* *|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The label for which a mobject should be created. If the label already
    is a mobject, no new mobject is created.
  * **label_constructor** (*Callable* *|* *None*) – Optional. A class or function returning a mobject when
    passing `label_tex` as an argument. If `None` is passed
    (the default), the label constructor from the `label_constructor`
    attribute is used.
  * **kwargs** (*Any*)
* **Returns:**
  The label.
* **Return type:**
  [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

#### \_original_\_init_\_(x_range=None, length=None, unit_size=1, include_ticks=True, tick_size=0.1, numbers_with_elongated_ticks=None, longer_tick_multiple=2, exclude_origin_tick=False, rotation=0, stroke_width=2.0, include_tip=False, tip_width=0.35, tip_height=0.35, tip_shape=None, include_numbers=False, font_size=36, label_direction=array([ 0., -1., 0.]), label_constructor=<class 'manim.mobject.text.tex_mobject.MathTex'>, scaling=<manim.mobject.graphing.scale.LinearBase object>, line_to_number_buff=0.25, decimal_number_config=None, numbers_to_exclude=None, numbers_to_include=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **x_range** (*Sequence* *[**float* *]*  *|* *None*)
  * **length** (*float* *|* *None*)
  * **unit_size** (*float*)
  * **include_ticks** (*bool*)
  * **tick_size** (*float*)
  * **numbers_with_elongated_ticks** (*Iterable* *[**float* *]*  *|* *None*)
  * **longer_tick_multiple** (*int*)
  * **exclude_origin_tick** (*bool*)
  * **rotation** (*float*)
  * **stroke_width** (*float*)
  * **include_tip** (*bool*)
  * **tip_width** (*float*)
  * **tip_height** (*float*)
  * **tip_shape** (*type* *[*[*ArrowTip*](manim.mobject.geometry.tips.ArrowTip.md#manim.mobject.geometry.tips.ArrowTip) *]*  *|* *None*)
  * **include_numbers** (*bool*)
  * **font_size** (*float*)
  * **label_direction** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **label_constructor** (*type* *[*[*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *]*)
  * **scaling** ( *\_ScaleBase*)
  * **line_to_number_buff** (*float*)
  * **decimal_number_config** (*dict* *|* *None*)
  * **numbers_to_exclude** (*Iterable* *[**float* *]*  *|* *None*)
  * **numbers_to_include** (*Iterable* *[**float* *]*  *|* *None*)
  * **kwargs** (*Any*)

#### add_labels(dict_values, direction=None, buff=None, font_size=None, label_constructor=None)

Adds specifically positioned labels to the [`NumberLine`](#manim.mobject.graphing.number_line.NumberLine) using a `dict`.
The labels can be accessed after creation via `self.labels`.

* **Parameters:**
  * **dict_values** (*dict* *[**float* *,* *str* *|* *float* *|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*) – A dictionary consisting of the position along the number line and the mobject to be added:
    `{1: Tex("Monday"), 3: Tex("Tuesday")}`. `label_constructor` will be used
    to construct the labels if the value is not a mobject (`str` or `float`).
  * **direction** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*) – Determines the direction at which the label is positioned next to the line.
  * **buff** (*float* *|* *None*) – The distance of the label from the line.
  * **font_size** (*float* *|* *None*) – The font size of the mobject to be positioned.
  * **label_constructor** (*type* *[*[*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *]*  *|* *None*) – The [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) class that will be used to construct the label.
    Defaults to the `label_constructor` attribute of the number line
    if not specified.
* **Raises:**
  **AttributeError** – If the label does not have a `font_size` attribute, an `AttributeError` is raised.
* **Return type:**
  Self

#### add_numbers(x_values=None, excluding=None, font_size=None, label_constructor=None, \*\*kwargs)

Adds [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) mobjects representing their position
at each tick of the number line. The numbers can be accessed after creation
via `self.numbers`.

* **Parameters:**
  * **x_values** (*Iterable* *[**float* *]*  *|* *None*) – An iterable of the values used to position and create the labels.
    Defaults to the output produced by [`get_tick_range()`](#manim.mobject.graphing.number_line.NumberLine.get_tick_range)
  * **excluding** (*Iterable* *[**float* *]*  *|* *None*) – A list of values to exclude from `x_values`.
  * **font_size** (*float* *|* *None*) – The font size of the labels. Defaults to the `font_size` attribute
    of the number line.
  * **label_constructor** (*type* *[*[*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *]*  *|* *None*) – The [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) class that will be used to construct the label.
    Defaults to the `label_constructor` attribute of the number line
    if not specified.
  * **kwargs** (*Any*)
* **Return type:**
  Self

#### add_ticks()

Adds ticks to the number line. Ticks can be accessed after creation
via `self.ticks`.

* **Return type:**
  None

#### get_number_mobject(x, direction=None, buff=None, font_size=None, label_constructor=None, \*\*number_config)

Generates a positioned [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) mobject
generated according to `label_constructor`.

* **Parameters:**
  * **x** (*float*) – The x-value at which the mobject should be positioned.
  * **direction** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D) *|* *None*) – Determines the direction at which the label is positioned next to the line.
  * **buff** (*float* *|* *None*) – The distance of the label from the line.
  * **font_size** (*float* *|* *None*) – The font size of the label mobject.
  * **label_constructor** (*type* *[*[*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *]*  *|* *None*) – The [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) class that will be used to construct the label.
    Defaults to the `label_constructor` attribute of the number line
    if not specified.
  * **number_config** (*dict* *[**str* *,* *Any* *]*)
* **Returns:**
  The positioned mobject.
* **Return type:**
  [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber)

#### get_tick(x, size=None)

Generates a tick and positions it along the number line.

* **Parameters:**
  * **x** (*float*) – The position of the tick.
  * **size** (*float* *|* *None*) – The factor by which the tick is scaled.
* **Returns:**
  A positioned tick.
* **Return type:**
  [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)

#### get_tick_range()

Generates the range of values on which labels are plotted based on the
`x_range` attribute of the number line.

* **Returns:**
  A numpy array of floats represnting values along the number line.
* **Return type:**
  np.ndarray

#### n2p(number)

Abbreviation for [`number_to_point()`](#manim.mobject.graphing.number_line.NumberLine.number_to_point).

* **Parameters:**
  **number** (*float* *|* *ndarray*)
* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### number_to_point(number)

Accepts a value along the number line and returns a point with
respect to the scene.
Equivalent to NumberLine @ number

* **Parameters:**
  **number** (*float* *|* *ndarray*) – The value to be transformed into a coordinate. Or a list of values.
* **Returns:**
  A point with respect to the scene’s coordinate system. Or a list of points.
* **Return type:**
  np.ndarray

### Examples

```pycon
>>> from manim import NumberLine
>>> number_line = NumberLine()
>>> number_line.number_to_point(0)
array([0., 0., 0.])
>>> number_line.number_to_point(1)
array([1., 0., 0.])
>>> number_line @ 1
array([1., 0., 0.])
>>> number_line.number_to_point([1, 2, 3])
array([[1., 0., 0.],
       [2., 0., 0.],
       [3., 0., 0.]])
```

#### p2n(point)

Abbreviation for [`point_to_number()`](#manim.mobject.graphing.number_line.NumberLine.point_to_number).

* **Parameters:**
  **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
* **Return type:**
  float

#### point_to_number(point)

Accepts a point with respect to the scene and returns
a float along the number line.

* **Parameters:**
  **point** (*Sequence* *[**float* *]*) – A sequence of values consisting of `(x_coord, y_coord, z_coord)`.
* **Returns:**
  A float representing a value along the number line.
* **Return type:**
  float

### Examples

```pycon
>>> from manim import NumberLine
>>> number_line = NumberLine()
>>> number_line.point_to_number((0, 0, 0))
np.float64(0.0)
>>> number_line.point_to_number((1, 0, 0))
np.float64(1.0)
>>> number_line.point_to_number([[0.5, 0, 0], [1, 0, 0], [1.5, 0, 0]])
array([0.5, 1. , 1.5])
```
