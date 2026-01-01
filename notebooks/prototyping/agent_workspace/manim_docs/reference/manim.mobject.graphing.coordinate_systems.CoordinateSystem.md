# CoordinateSystem

Qualified name: `manim.mobject.graphing.coordinate\_systems.CoordinateSystem`

### *class* CoordinateSystem(x_range=None, y_range=None, x_length=None, y_length=None, dimension=2)

Bases: `object`

Abstract base class for Axes and NumberPlane.

### Examples

### Methods

| [`add_coordinates`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.add_coordinates)                         | Adds labels to the axes.                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`angle_of_tangent`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.angle_of_tangent)                       | Returns the angle to the x-axis of the tangent to the plotted curve at a particular x-value.                                                                        |
| [`c2p`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.c2p)                                                 | Abbreviation for `coords_to_point()`                                                                                                                                |
| `coords_to_point`                                                                                                        |                                                                                                                                                                     |
| [`get_T_label`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_T_label)                                 | Creates a labelled triangle marker with a vertical line from the x-axis to a curve at a given x-value.                                                              |
| [`get_area`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_area)                                       | Returns a [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon) representing the area under the graph passed.             |
| `get_axes`                                                                                                               |                                                                                                                                                                     |
| `get_axis`                                                                                                               |                                                                                                                                                                     |
| `get_axis_labels`                                                                                                        |                                                                                                                                                                     |
| [`get_graph_label`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_graph_label)                         | Creates a properly positioned label for the passed graph, with an optional dot.                                                                                     |
| [`get_horizontal_line`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_horizontal_line)                 | A horizontal line from the y-axis to a given point in the scene.                                                                                                    |
| [`get_line_from_axis_to_point`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_line_from_axis_to_point) | Returns a straight line from a given axis to a point in the scene.                                                                                                  |
| [`get_lines_to_point`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_lines_to_point)                   | Generate both horizontal and vertical lines from the axis to a point.                                                                                               |
| [`get_origin`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_origin)                                   | Gets the origin of [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.md#manim.mobject.graphing.coordinate_systems.Axes).                                      |
| [`get_riemann_rectangles`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_riemann_rectangles)           | Generates a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) of the Riemann Rectangles for a given curve. |
| [`get_secant_slope_group`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_secant_slope_group)           | Creates two lines representing dx and df, the labels for dx and df, and                                                                                             |
| [`get_vertical_line`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_vertical_line)                     | A vertical line from the x-axis to a given point in the scene.                                                                                                      |
| [`get_vertical_lines_to_graph`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_vertical_lines_to_graph) | Obtains multiple lines from the x-axis to the curve.                                                                                                                |
| `get_x_axis`                                                                                                             |                                                                                                                                                                     |
| [`get_x_axis_label`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label)                       | Generate an x-axis label.                                                                                                                                           |
| `get_x_unit_size`                                                                                                        |                                                                                                                                                                     |
| `get_y_axis`                                                                                                             |                                                                                                                                                                     |
| [`get_y_axis_label`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_y_axis_label)                       | Generate a y-axis label.                                                                                                                                            |
| `get_y_unit_size`                                                                                                        |                                                                                                                                                                     |
| `get_z_axis`                                                                                                             |                                                                                                                                                                     |
| [`i2gc`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.i2gc)                                               | Alias for [`input_to_graph_coords()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.input_to_graph_coords).                                           |
| [`i2gp`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.i2gp)                                               | Alias for [`input_to_graph_point()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.input_to_graph_point).                                             |
| [`input_to_graph_coords`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.input_to_graph_coords)             | Returns a tuple of the axis relative coordinates of the point on the graph based on the x-value given.                                                              |
| [`input_to_graph_point`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.input_to_graph_point)               | Returns the coordinates of the point on a `graph` corresponding to an `x` value.                                                                                    |
| [`p2c`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.p2c)                                                 | Abbreviation for `point_to_coords()`                                                                                                                                |
| [`plot`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot)                                               | Generates a curve based on a function.                                                                                                                              |
| [`plot_antiderivative_graph`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_antiderivative_graph)     | Plots an antiderivative graph.                                                                                                                                      |
| [`plot_derivative_graph`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_derivative_graph)             | Returns the curve of the derivative of the passed graph.                                                                                                            |
| [`plot_implicit_curve`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_implicit_curve)                 | Creates the curves of an implicit function.                                                                                                                         |
| [`plot_parametric_curve`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_parametric_curve)             | A parametric curve.                                                                                                                                                 |
| [`plot_polar_graph`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_polar_graph)                       | A polar graph.                                                                                                                                                      |
| [`plot_surface`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_surface)                               | Generates a surface based on a function.                                                                                                                            |
| `point_to_coords`                                                                                                        |                                                                                                                                                                     |
| [`point_to_polar`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.point_to_polar)                           | Gets polar coordinates from a point.                                                                                                                                |
| [`polar_to_point`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.polar_to_point)                           | Gets a point from polar coordinates.                                                                                                                                |
| [`pr2pt`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.pr2pt)                                             | Abbreviation for [`polar_to_point()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.polar_to_point)                                                   |
| [`pt2pr`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.pt2pr)                                             | Abbreviation for [`point_to_polar()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.point_to_polar)                                                   |
| [`slope_of_tangent`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.slope_of_tangent)                       | Returns the slope of the tangent to the plotted curve at a particular x-value.                                                                                      |
* **Parameters:**
  * **x_range** (*Sequence* *[**float* *]*  *|* *None*)
  * **y_range** (*Sequence* *[**float* *]*  *|* *None*)
  * **x_length** (*float* *|* *None*)
  * **y_length** (*float* *|* *None*)
  * **dimension** (*int*)

#### \_get_axis_label(label, axis, edge, direction, buff=0.1)

Gets the label for an axis.

* **Parameters:**
  * **label** (*float* *|* *str* *|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The label. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) for `str` and `float` inputs.
  * **axis** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The axis to which the label will be added.
  * **edge** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The edge of the axes to which the label will be added. `RIGHT` adds to the right side of the axis
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – Allows for further positioning of the label.
  * **buff** (*float*) – The distance of the label from the line.
* **Returns:**
  The positioned label along the given axis.
* **Return type:**
  [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

#### add_coordinates(\*axes_numbers, \*\*kwargs)

Adds labels to the axes. Use `Axes.coordinate_labels` to
access the coordinates after creation.

* **Parameters:**
  * **axes_numbers** (*Iterable* *[**float* *]*  *|* *None* *|* *dict* *[**float* *,* *str* *|* *float* *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The numbers to be added to the axes. Use `None` to represent an axis with default labels.
  * **kwargs** (*Any*)
* **Return type:**
  *Self*

### Examples

```python
ax = ThreeDAxes()
x_labels = range(-4, 5)
z_labels = range(-4, 4, 2)
ax.add_coordinates(
    x_labels, None, z_labels
)  # default y labels, custom x & z labels
ax.add_coordinates(x_labels)  # only x labels
```

You can also specifically control the position and value of the labels using a dict.

```python
ax = Axes(x_range=[0, 7])
x_pos = [x for x in range(1, 8)]

# strings are automatically converted into a Tex mobject.
x_vals = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
x_dict = dict(zip(x_pos, x_vals))
ax.add_coordinates(x_dict)
```

#### angle_of_tangent(x, graph, dx=1e-08)

Returns the angle to the x-axis of the tangent
to the plotted curve at a particular x-value.

* **Parameters:**
  * **x** (*float*) – The x-value at which the tangent must touch the curve.
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)) – The [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction) for which to calculate the tangent.
  * **dx** (*float*) – The change in x used to determine the angle of the tangent to the curve.
* **Returns:**
  The angle of the tangent to the curve.
* **Return type:**
  `float`

### Examples

```python
ax = Axes()
curve = ax.plot(lambda x: x**2)
ax.angle_of_tangent(x=3, graph=curve)
# 1.4056476493802699
```

#### c2p(\*coords)

Abbreviation for `coords_to_point()`

* **Parameters:**
  **coords** (*float* *|* *Sequence* *[**float* *]*  *|* *Sequence* *[**Sequence* *[**float* *]* *]*  *|* *ndarray*)
* **Return type:**
  *ndarray*

#### get_T_label(x_val, graph, label=None, label_color=None, triangle_size=0.25, triangle_color=ManimColor('#FFFFFF'), line_func=<class 'manim.mobject.geometry.line.Line'>, line_color=ManimColor('#FFFF00'))

Creates a labelled triangle marker with a vertical line from the x-axis
to a curve at a given x-value.

* **Parameters:**
  * **x_val** (*float*) – The position along the curve at which the label, line and triangle will be constructed.
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)) – The [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction) for which to construct the label.
  * **label** (*float* *|* *str* *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *None*) – The label of the vertical line and triangle.
  * **label_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – The color of the label.
  * **triangle_size** (*float*) – The size of the triangle.
  * **triangle_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – The color of the triangle.
  * **line_func** (*type* *[*[*Line*](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line) *]*) – The function used to construct the vertical line.
  * **line_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the vertical line.
* **Returns:**
  A [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) of the label, triangle and vertical line mobjects.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_area(graph, x_range=None, color=(ManimColor('#58C4DD'), ManimColor('#83C167')), opacity=0.3, bounded_graph=None, \*\*kwargs)

Returns a [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon) representing the area under the graph passed.

* **Parameters:**
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)) – The graph/curve for which the area needs to be gotten.
  * **x_range** (*tuple* *[**float* *,* *float* *]*  *|* *None*) – The range of the minimum and maximum x-values of the area. `x_range = [x_min, x_max]`.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*) – The color of the area. Creates a gradient if a list of colors is provided.
  * **opacity** (*float*) – The opacity of the area.
  * **bounded_graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction) *|* *None*) – If a secondary `graph` is specified, encloses the area between the two curves.
  * **kwargs** (*Any*) – Additional parameters passed to [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon).
* **Returns:**
  The [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon) representing the area.
* **Return type:**
  [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon)
* **Raises:**
  **ValueError** – When x_ranges do not match (either area x_range, graph’s x_range or bounded_graph’s x_range).

### Examples

#### get_graph_label(graph, label='f(x)', x_val=None, direction=array([1., 0., 0.]), buff=0.25, color=None, dot=False, dot_config=None)

Creates a properly positioned label for the passed graph, with an optional dot.

* **Parameters:**
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)) – The curve.
  * **label** (*float* *|* *str* *|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The label for the function’s curve. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) for `str` and `float` inputs.
  * **x_val** (*float* *|* *None*) – The x_value along the curve that positions the label.
  * **direction** (*Sequence* *[**float* *]*) – The cartesian position, relative to the curve that the label will be at –> `LEFT`, `RIGHT`.
  * **buff** (*float*) – The distance between the curve and the label.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – The color of the label. Defaults to the color of the curve.
  * **dot** (*bool*) – Whether to add a dot at the point on the graph.
  * **dot_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – Additional parameters to be passed to [`Dot`](manim.mobject.geometry.arc.Dot.md#manim.mobject.geometry.arc.Dot).
* **Returns:**
  The positioned label and [`Dot`](manim.mobject.geometry.arc.Dot.md#manim.mobject.geometry.arc.Dot), if applicable.
* **Return type:**
  `Mobject`

### Examples

#### get_horizontal_line(point, \*\*kwargs)

A horizontal line from the y-axis to a given point in the scene.

* **Parameters:**
  * **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The point to which the horizontal line will be drawn.
  * **kwargs** (*Any*) – Additional parameters to be passed to [`get_line_from_axis_to_point`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_line_from_axis_to_point).
* **Returns:**
  A horizontal line from the y-axis to the point.
* **Return type:**
  `Line`

### Examples

#### get_line_from_axis_to_point(index: int, point: [Point3DLike](manim.typing.md#manim.typing.Point3DLike), line_config: dict | None = None, color: [ParsableManimColor](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) | None = None, stroke_width: float = 2) → [DashedLine](manim.mobject.geometry.line.DashedLine.md#manim.mobject.geometry.line.DashedLine)

#### get_line_from_axis_to_point(index: int, point: [Point3DLike](manim.typing.md#manim.typing.Point3DLike), line_func: type[[LineType](manim.mobject.graphing.coordinate_systems.md#manim.mobject.graphing.coordinate_systems.LineType)], line_config: dict | None = None, color: [ParsableManimColor](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) | None = None, stroke_width: float = 2) → [LineType](manim.mobject.graphing.coordinate_systems.md#manim.mobject.graphing.coordinate_systems.LineType)

Returns a straight line from a given axis to a point in the scene.

* **Parameters:**
  * **index** – Specifies the axis from which to draw the line. 0 = x_axis, 1 = y_axis
  * **point** – The point to which the line will be drawn.
  * **line_func** – The function of the [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line) mobject used to construct the line.
  * **line_config** – Optional arguments to passed to `line_func`.
  * **color** – The color of the line.
  * **stroke_width** – The stroke width of the line.
* **Returns:**
  The line from an axis to a point.
* **Return type:**
  [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)

#### SEE ALSO
[`get_vertical_line()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_vertical_line)
[`get_horizontal_line()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_horizontal_line)

#### get_lines_to_point(point, \*\*kwargs)

Generate both horizontal and vertical lines from the axis to a point.

* **Parameters:**
  * **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – A point on the scene.
  * **kwargs** (*Any*) – Additional parameters to be passed to [`get_line_from_axis_to_point()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_line_from_axis_to_point)
* **Returns:**
  A [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) of the horizontal and vertical lines.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

#### SEE ALSO
[`get_vertical_line()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_vertical_line)
[`get_horizontal_line()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_horizontal_line)

### Examples

#### get_origin()

Gets the origin of [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.md#manim.mobject.graphing.coordinate_systems.Axes).

* **Returns:**
  The center point.
* **Return type:**
  np.ndarray

#### get_riemann_rectangles(graph, x_range=None, dx=0.1, input_sample_type='left', stroke_width=1, stroke_color=ManimColor('#000000'), fill_opacity=1, color=(ManimColor('#58C4DD'), ManimColor('#83C167')), show_signed_area=True, bounded_graph=None, blend=False, width_scale_factor=1.001)

Generates a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) of the Riemann Rectangles for a given curve.

* **Parameters:**
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)) – The graph whose area will be approximated by Riemann rectangles.
  * **x_range** (*Sequence* *[**float* *]*  *|* *None*) – The minimum and maximum x-values of the rectangles. `x_range = [x_min, x_max]`.
  * **dx** (*float*) – The change in x-value that separates each rectangle.
  * **input_sample_type** (*str*) – Can be any of `"left"`, `"right"` or `"center"`. Refers to where
    the sample point for the height of each Riemann Rectangle
    will be inside the segments of the partition.
  * **stroke_width** (*float*) – The stroke_width of the border of the rectangles.
  * **stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the border of the rectangle.
  * **fill_opacity** (*float*) – The opacity of the rectangles.
  * **color** (*Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*  *|* [*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The colors of the rectangles. Creates a balanced gradient if multiple colors are passed.
  * **show_signed_area** (*bool*) – Indicates negative area when the curve dips below the x-axis by inverting its color.
  * **blend** (*bool*) – Sets the `stroke_color` to `fill_color`, blending the rectangles without clear separation.
  * **bounded_graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction) *|* *None*) – If a secondary graph is specified, encloses the area between the two curves.
  * **width_scale_factor** (*float*) – The factor by which the width of the rectangles is scaled.
* **Returns:**
  A [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) containing the Riemann Rectangles.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_secant_slope_group(x, graph, dx=None, dx_line_color=ManimColor('#FFFF00'), dy_line_color=None, dx_label=None, dy_label=None, include_secant_line=True, secant_line_color=ManimColor('#83C167'), secant_line_length=10)

Creates two lines representing dx and df, the labels for dx and df, and
: the secant to the curve at a particular x-value.

* **Parameters:**
  * **x** (*float*) – The x-value at which the secant intersects the graph for the first time.
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)) – The curve for which the secant will be found.
  * **dx** (*float* *|* *None*) – The change in x after which the secant exits.
  * **dx_line_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the line that indicates the change in x.
  * **dy_line_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – The color of the line that indicates the change in y. Defaults to the color of `graph`.
  * **dx_label** (*float* *|* *str* *|* *None*) – The label for the dx line. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) for `str` and `float` inputs.
  * **dy_label** (*float* *|* *str* *|* *None*) – The label for the dy line. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) for `str` and `float` inputs.
  * **include_secant_line** (*bool*) – Whether to include the secant line in the graph,
    or just the df/dx lines and labels.
  * **secant_line_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the secant line.
  * **secant_line_length** (*float*) – The length of the secant line.
* **Returns:**
  A group containing the elements: dx_line, df_line, and
  if applicable also `dx_label`, `df_label`, secant_line.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_vertical_line(point, \*\*kwargs)

A vertical line from the x-axis to a given point in the scene.

* **Parameters:**
  * **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The point to which the vertical line will be drawn.
  * **kwargs** (*Any*) – Additional parameters to be passed to [`get_line_from_axis_to_point`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_line_from_axis_to_point).
* **Returns:**
  A vertical line from the x-axis to the point.
* **Return type:**
  `Line`

### Examples

#### get_vertical_lines_to_graph(graph, x_range=None, num_lines=20, \*\*kwargs)

Obtains multiple lines from the x-axis to the curve.

* **Parameters:**
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)) – The graph along which the lines are placed.
  * **x_range** (*Sequence* *[**float* *]*  *|* *None*) – A list containing the lower and and upper bounds of the lines: `x_range = [x_min, x_max]`.
  * **num_lines** (*int*) – The number of evenly spaced lines.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`get_vertical_line()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_vertical_line).
* **Returns:**
  The [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) of the evenly spaced lines.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_x_axis_label(label, edge=array([1., 1., 0.]), direction=array([1., 1., 0.]), buff=0.1, \*\*kwargs)

Generate an x-axis label.

* **Parameters:**
  * **label** (*float* *|* *str* *|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The label. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) for `str` and `float` inputs.
  * **edge** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D)) – The edge of the x-axis to which the label will be added, by default `UR`.
  * **direction** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D)) – Allows for further positioning of the label from an edge, by default `UR`.
  * **buff** (*float*) – The distance of the label from the line.
  * **kwargs** (*Any*)
* **Returns:**
  The positioned label.
* **Return type:**
  [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### Examples

#### get_y_axis_label(label, edge=array([1., 1., 0.]), direction=array([1., 0.5, 0.]), buff=0.1, \*\*kwargs)

Generate a y-axis label.

* **Parameters:**
  * **label** (*float* *|* *str* *|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The label. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) for `str` and `float` inputs.
  * **edge** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D)) – The edge of the y-axis to which the label will be added, by default `UR`.
  * **direction** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D)) – Allows for further positioning of the label from an edge, by default `UR`
  * **buff** (*float*) – The distance of the label from the line.
  * **kwargs** (*Any*)
* **Returns:**
  The positioned label.
* **Return type:**
  [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### Examples

#### i2gc(x, graph)

Alias for [`input_to_graph_coords()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.input_to_graph_coords).

* **Parameters:**
  * **x** (*float*)
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction))
* **Return type:**
  tuple[float, float]

#### i2gp(x, graph)

Alias for [`input_to_graph_point()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.input_to_graph_point).

* **Parameters:**
  * **x** (*float*)
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction))
* **Return type:**
  *ndarray*

#### input_to_graph_coords(x, graph)

Returns a tuple of the axis relative coordinates of the point
on the graph based on the x-value given.

### Examples

```pycon
>>> from manim import Axes
>>> ax = Axes()
>>> parabola = ax.plot(lambda x: x**2)
>>> ax.input_to_graph_coords(x=3, graph=parabola)
(3, 9)
```

* **Parameters:**
  * **x** (*float*)
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction))
* **Return type:**
  tuple[float, float]

#### input_to_graph_point(x, graph)

Returns the coordinates of the point on a `graph` corresponding to an `x` value.

* **Parameters:**
  * **x** (*float*) – The x-value of a point on the `graph`.
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction) *|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction) on which the point lies.
* **Returns:**
  The coordinates of the point on the `graph` corresponding to the `x` value.
* **Return type:**
  `np.ndarray`
* **Raises:**
  **ValueError** – When the target x is not in the range of the line graph.

### Examples

#### p2c(point)

Abbreviation for `point_to_coords()`

* **Parameters:**
  **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
* **Return type:**
  list[[*ManimFloat*](manim.typing.md#manim.typing.ManimFloat)]

#### plot(function, x_range=None, use_vectorized=False, colorscale=None, colorscale_axis=1, \*\*kwargs)

Generates a curve based on a function.

* **Parameters:**
  * **function** (*Callable* *[* *[**float* *]* *,* *float* *]*) – The function used to construct the [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction).
  * **x_range** (*Sequence* *[**float* *]*  *|* *None*) – The range of the curve along the axes. `x_range = [x_min, x_max, x_step]`.
  * **use_vectorized** (*bool*) – Whether to pass in the generated t value array to the function. Only use this if your function supports it.
    Output should be a numpy array of shape `[y_0, y_1, ...]`
  * **colorscale** (*Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*  *|* *Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *,* *float* *]*  *|* *None*) – Colors of the function. Optional parameter used when coloring a function by values. Passing a list of colors
    and a colorscale_axis will color the function by y-value. Passing a list of tuples in the form `(color, pivot)`
    allows user-defined pivots where the color transitions.
  * **colorscale_axis** (*int*) – Defines the axis on which the colorscale is applied (0 = x, 1 = y), default is y-axis (1).
  * **kwargs** (*Any*) – Additional parameters to be passed to [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction).
* **Returns:**
  The plotted curve.
* **Return type:**
  [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)

#### WARNING
This method may not produce accurate graphs since Manim currently relies on interpolation between
evenly-spaced samples of the curve, instead of intelligent plotting.
See the example below for some solutions to this problem.

### Examples

#### plot_antiderivative_graph(graph, y_intercept=0, samples=50, use_vectorized=False, \*\*kwargs)

Plots an antiderivative graph.

* **Parameters:**
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)) – The graph for which the antiderivative will be found.
  * **y_intercept** (*float*) – The y-value at which the graph intercepts the y-axis.
  * **samples** (*int*) – The number of points to take the area under the graph.
  * **use_vectorized** (*bool*) – Whether to use the vectorized version of the antiderivative. This means
    to pass in the generated t value array to the function. Only use this if your function supports it.
    Output should be a numpy array of shape `[y_0, y_1, ...]`
  * **kwargs** (*Any*) – Any valid keyword argument of [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction).
* **Returns:**
  The curve of the antiderivative.
* **Return type:**
  [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)

#### NOTE
This graph is plotted from the values of area under the reference graph.
The result might not be ideal if the reference graph contains uncalculatable
areas from x=0.

### Examples

#### plot_derivative_graph(graph, color=ManimColor('#83C167'), \*\*kwargs)

Returns the curve of the derivative of the passed graph.

* **Parameters:**
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)) – The graph for which the derivative will be found.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the derivative curve.
  * **kwargs** (*Any*) – Any valid keyword argument of [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction).
* **Returns:**
  The curve of the derivative.
* **Return type:**
  [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)

### Examples

#### plot_implicit_curve(func, min_depth=5, max_quads=1500, \*\*kwargs)

Creates the curves of an implicit function.

* **Parameters:**
  * **func** (*Callable* *[* *[**float* *,* *float* *]* *,* *float* *]*) – The function to graph, in the form of f(x, y) = 0.
  * **min_depth** (*int*) – The minimum depth of the function to calculate.
  * **max_quads** (*int*) – The maximum number of quads to use.
  * **kwargs** (*Any*) – Additional parameters to pass into `ImplicitFunction`.
* **Return type:**
  [*ImplicitFunction*](manim.mobject.graphing.functions.ImplicitFunction.md#manim.mobject.graphing.functions.ImplicitFunction)

### Examples

#### plot_parametric_curve(function, use_vectorized=False, \*\*kwargs)

A parametric curve.

* **Parameters:**
  * **function** (*Callable* *[* *[**float* *]* *,* *ndarray* *]*) – A parametric function mapping a number to a point in the
    coordinate system.
  * **use_vectorized** (*bool*) – Whether to pass in the generated t value array to the function. Only use this if your function supports it.
  * **kwargs** (*Any*) – Any further keyword arguments are passed to [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction).
* **Return type:**
  [*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)

### Example

#### plot_polar_graph(r_func, theta_range=None, \*\*kwargs)

A polar graph.

* **Parameters:**
  * **r_func** (*Callable* *[* *[**float* *]* *,* *float* *]*) – The function r of theta.
  * **theta_range** (*Sequence* *[**float* *]*  *|* *None*) – The range of theta as `theta_range = [theta_min, theta_max, theta_step]`.
  * **kwargs** (*Any*) – Additional parameters passed to [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction).
* **Return type:**
  [*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)

### Examples

#### plot_surface(function, u_range=None, v_range=None, colorscale=None, colorscale_axis=2, \*\*kwargs)

Generates a surface based on a function.

* **Parameters:**
  * **function** (*Callable* *[* *[**float* *]* *,* *float* *]*) – The function used to construct the [`Surface`](manim.mobject.three_d.three_dimensions.Surface.md#manim.mobject.three_d.three_dimensions.Surface).
  * **u_range** (*Sequence* *[**float* *]*  *|* *None*) – The range of the `u` variable: `(u_min, u_max)`.
  * **v_range** (*Sequence* *[**float* *]*  *|* *None*) – The range of the `v` variable: `(v_min, v_max)`.
  * **colorscale** (*Sequence* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*  *|* *Sequence* *[**tuple* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *,* *float* *]* *]*  *|* *None*) – Colors of the surface. Passing a list of colors will color the surface by z-value.
    Passing a list of tuples in the form `(color, pivot)` allows user-defined pivots
    where the color transitions.
  * **colorscale_axis** (*int*) – Defines the axis on which the colorscale is applied (0 = x, 1 = y, 2 = z), default
    is z-axis (2).
  * **kwargs** (*Any*) – Additional parameters to be passed to [`Surface`](manim.mobject.three_d.three_dimensions.Surface.md#manim.mobject.three_d.three_dimensions.Surface).
* **Returns:**
  The plotted surface.
* **Return type:**
  [`Surface`](manim.mobject.three_d.three_dimensions.Surface.md#manim.mobject.three_d.three_dimensions.Surface)

### Examples

#### point_to_polar(point)

Gets polar coordinates from a point.

* **Parameters:**
  **point** ([*Point2DLike*](manim.typing.md#manim.typing.Point2DLike)) – The point.
* **Returns:**
  The coordinate radius ($r$) and the coordinate azimuth ($\theta$).
* **Return type:**
  [Point2D](manim.typing.md#manim.typing.Point2D)

#### polar_to_point(radius, azimuth)

Gets a point from polar coordinates.

* **Parameters:**
  * **radius** (*float*) – The coordinate radius ($r$).
  * **azimuth** (*float*) – The coordinate azimuth ($\theta$).
* **Returns:**
  The point.
* **Return type:**
  numpy.ndarray

### Examples

#### pr2pt(radius, azimuth)

Abbreviation for [`polar_to_point()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.polar_to_point)

* **Parameters:**
  * **radius** (*float*)
  * **azimuth** (*float*)
* **Return type:**
  *ndarray*

#### pt2pr(point)

Abbreviation for [`point_to_polar()`](#manim.mobject.graphing.coordinate_systems.CoordinateSystem.point_to_polar)

* **Parameters:**
  **point** (*ndarray*)
* **Return type:**
  [*Point2D*](manim.typing.md#manim.typing.Point2D)

#### slope_of_tangent(x, graph, \*\*kwargs)

Returns the slope of the tangent to the plotted curve
at a particular x-value.

* **Parameters:**
  * **x** (*float*) – The x-value at which the tangent must touch the curve.
  * **graph** ([*ParametricFunction*](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction)) – The [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.md#manim.mobject.graphing.functions.ParametricFunction) for which to calculate the tangent.
  * **kwargs** (*Any*)
* **Returns:**
  The slope of the tangent with the x axis.
* **Return type:**
  `float`

### Examples

```python
ax = Axes()
curve = ax.plot(lambda x: x**2)
ax.slope_of_tangent(x=-2, graph=curve)
# -3.5000000259052038
```
