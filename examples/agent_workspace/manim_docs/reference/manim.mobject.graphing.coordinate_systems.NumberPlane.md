# NumberPlane

Qualified name: `manim.mobject.graphing.coordinate\_systems.NumberPlane`

### *class* NumberPlane(x_range=(-7.111111111111111, 7.111111111111111, 1), y_range=(-4.0, 4.0, 1), x_length=None, y_length=None, background_line_style=None, faded_line_style=None, faded_line_ratio=1, make_smooth_after_applying_functions=True, \*\*kwargs)

Bases: [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.md#manim.mobject.graphing.coordinate_systems.Axes)

Creates a cartesian plane with background lines.

* **Parameters:**
  * **x_range** (*Sequence* *[**float* *]*  *|* *None*) – The `[x_min, x_max, x_step]` values of the plane in the horizontal direction.
  * **y_range** (*Sequence* *[**float* *]*  *|* *None*) – The `[y_min, y_max, y_step]` values of the plane in the vertical direction.
  * **x_length** (*float* *|* *None*) – The width of the plane.
  * **y_length** (*float* *|* *None*) – The height of the plane.
  * **background_line_style** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – Arguments that influence the construction of the background lines of the plane.
  * **faded_line_style** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – Similar to `background_line_style`, affects the construction of the scene’s background lines.
  * **faded_line_ratio** (*int*) – Determines the number of boxes within the background lines: `2` = 4 boxes, `3` = 9 boxes.
  * **make_smooth_after_applying_functions** (*bool*) – Currently non-functional.
  * **kwargs** (*dict* *[**str* *,* *Any* *]*) – Additional arguments to be passed to [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.md#manim.mobject.graphing.coordinate_systems.Axes).

#### NOTE
If `x_length` or `y_length` are not defined, they are automatically calculated such that
one unit on each axis is one Manim unit long.

### Examples

### Methods

| `get_vector`                      |    |
|-----------------------------------|----|
| `prepare_for_nonlinear_transform` |    |

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

#### \_get_lines()

Generate all the lines, faded and not faded.
: Two sets of lines are generated: one parallel to the X-axis, and parallel to the Y-axis.

* **Returns:**
  The first (i.e the non faded lines) and second (i.e the faded lines) sets of lines, respectively.
* **Return type:**
  Tuple[[`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup), [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)]

#### \_get_lines_parallel_to_axis(axis_parallel_to, axis_perpendicular_to, freq, ratio_faded_lines)

Generate a set of lines parallel to an axis.

* **Parameters:**
  * **axis_parallel_to** ([*NumberLine*](manim.mobject.graphing.number_line.NumberLine.md#manim.mobject.graphing.number_line.NumberLine)) – The axis with which the lines will be parallel.
  * **axis_perpendicular_to** ([*NumberLine*](manim.mobject.graphing.number_line.NumberLine.md#manim.mobject.graphing.number_line.NumberLine)) – The axis with which the lines will be perpendicular.
  * **ratio_faded_lines** (*int*) – The ratio between the space between faded lines and the space between non-faded lines.
  * **freq** (*float*) – Frequency of non-faded lines (number of non-faded lines per graph unit).
* **Returns:**
  The first (i.e the non-faded lines parallel to axis_parallel_to) and second
  : (i.e the faded lines parallel to axis_parallel_to) sets of lines, respectively.
* **Return type:**
  Tuple[[`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup), [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)]

#### \_init_background_lines()

Will init all the lines of NumberPlanes (faded or not)

* **Return type:**
  None

#### \_original_\_init_\_(x_range=(-7.111111111111111, 7.111111111111111, 1), y_range=(-4.0, 4.0, 1), x_length=None, y_length=None, background_line_style=None, faded_line_style=None, faded_line_ratio=1, make_smooth_after_applying_functions=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **x_range** (*Sequence* *[**float* *]*  *|* *None*)
  * **y_range** (*Sequence* *[**float* *]*  *|* *None*)
  * **x_length** (*float* *|* *None*)
  * **y_length** (*float* *|* *None*)
  * **background_line_style** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **faded_line_style** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **faded_line_ratio** (*int*)
  * **make_smooth_after_applying_functions** (*bool*)
  * **kwargs** (*dict* *[**str* *,* *Any* *]*)
