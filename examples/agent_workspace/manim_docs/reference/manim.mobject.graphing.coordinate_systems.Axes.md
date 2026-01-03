# Axes

Qualified name: `manim.mobject.graphing.coordinate\_systems.Axes`

### *class* Axes(x_range=None, y_range=None, x_length=12, y_length=6, axis_config=None, x_axis_config=None, y_axis_config=None, tips=True, \*\*kwargs)

Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup), [`CoordinateSystem`](manim.mobject.graphing.coordinate_systems.CoordinateSystem.md#manim.mobject.graphing.coordinate_systems.CoordinateSystem)

Creates a set of axes.

* **Parameters:**
  * **x_range** (*Sequence* *[**float* *]*  *|* *None*) – The `(x_min, x_max, x_step)` values of the x-axis.
  * **y_range** (*Sequence* *[**float* *]*  *|* *None*) – The `(y_min, y_max, y_step)` values of the y-axis.
  * **x_length** (*float* *|* *None*) – The length of the x-axis.
  * **y_length** (*float* *|* *None*) – The length of the y-axis.
  * **axis_config** (*dict* *|* *None*) – Arguments to be passed to [`NumberLine`](manim.mobject.graphing.number_line.NumberLine.md#manim.mobject.graphing.number_line.NumberLine) that influences both axes.
  * **x_axis_config** (*dict* *|* *None*) – Arguments to be passed to [`NumberLine`](manim.mobject.graphing.number_line.NumberLine.md#manim.mobject.graphing.number_line.NumberLine) that influence the x-axis.
  * **y_axis_config** (*dict* *|* *None*) – Arguments to be passed to [`NumberLine`](manim.mobject.graphing.number_line.NumberLine.md#manim.mobject.graphing.number_line.NumberLine) that influence the y-axis.
  * **tips** (*bool*) – Whether or not to include the tips on both axes.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`CoordinateSystem`](manim.mobject.graphing.coordinate_systems.CoordinateSystem.md#manim.mobject.graphing.coordinate_systems.CoordinateSystem) and [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup).

### Examples

Styling arguments can be passed to the underlying [`NumberLine`](manim.mobject.graphing.number_line.NumberLine.md#manim.mobject.graphing.number_line.NumberLine)
mobjects that represent the axes:

### Methods

| [`coords_to_point`](#manim.mobject.graphing.coordinate_systems.Axes.coords_to_point)   | Accepts coordinates from the axes and returns a point with respect to the scene.     |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [`get_axes`](#manim.mobject.graphing.coordinate_systems.Axes.get_axes)                 | Gets the axes.                                                                       |
| [`get_axis_labels`](#manim.mobject.graphing.coordinate_systems.Axes.get_axis_labels)   | Defines labels for the x-axis and y-axis of the graph.                               |
| [`plot_line_graph`](#manim.mobject.graphing.coordinate_systems.Axes.plot_line_graph)   | Draws a line graph.                                                                  |
| [`point_to_coords`](#manim.mobject.graphing.coordinate_systems.Axes.point_to_coords)   | Accepts a point from the scene and returns its coordinates with respect to the axes. |

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

#### \_create_axis(range_terms, axis_config, length)

Creates an axis and dynamically adjusts its position depending on where 0 is located on the line.

* **Parameters:**
  * **range_terms** (*Sequence* *[**float* *]*) – The range of the the axis : `(x_min, x_max, x_step)`.
  * **axis_config** (*dict* *[**str* *,* *Any* *]*) – Additional parameters that are passed to [`NumberLine`](manim.mobject.graphing.number_line.NumberLine.md#manim.mobject.graphing.number_line.NumberLine).
  * **length** (*float*) – The length of the axis.
* **Returns:**
  Returns a number line based on `range_terms`.
* **Return type:**
  `NumberLine`

#### *static* \_origin_shift(axis_range)

Determines how to shift graph mobjects to compensate when 0 is not on the axis.

* **Parameters:**
  **axis_range** (*Sequence* *[**float* *]*) – The range of the axis : `(x_min, x_max, x_step)`.
* **Return type:**
  float

#### \_original_\_init_\_(x_range=None, y_range=None, x_length=12, y_length=6, axis_config=None, x_axis_config=None, y_axis_config=None, tips=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **x_range** (*Sequence* *[**float* *]*  *|* *None*)
  * **y_range** (*Sequence* *[**float* *]*  *|* *None*)
  * **x_length** (*float* *|* *None*)
  * **y_length** (*float* *|* *None*)
  * **axis_config** (*dict* *|* *None*)
  * **x_axis_config** (*dict* *|* *None*)
  * **y_axis_config** (*dict* *|* *None*)
  * **tips** (*bool*)
  * **kwargs** (*Any*)

#### *static* \_update_default_configs(default_configs, passed_configs)

Takes in two tuples of dicts and return modifies the first such that values from
`passed_configs` overwrite values in `default_configs`. If a key does not exist
in default_configs, it is added to the dict.

This method is useful for having defaults in a class and being able to overwrite
them with user-defined input.

* **Parameters:**
  * **default_configs** (*tuple* *[**dict* *[**Any* *,* *Any* *]* *]*) – The dict that will be updated.
  * **passed_configs** (*tuple* *[**dict* *[**Any* *,* *Any* *]* *]*) – The dict that will be used to update.
* **Return type:**
  None

### Examples

To create a tuple with one dictionary, add a comma after the element:

```python
self._update_default_configs(
    (dict_1,)(
        dict_2,
    )
)
```

#### coords_to_point(\*coords)

Accepts coordinates from the axes and returns a point with respect to the scene.
Equivalent to ax @ (coord1)

* **Parameters:**
  **coords** (*float* *|* *Sequence* *[**float* *]*  *|* *Sequence* *[**Sequence* *[**float* *]* *]*  *|* *ndarray*) – 

  The coordinates. Each coord is passed as a separate argument: `ax.coords_to_point(1, 2, 3)`.

  Also accepts a list of coordinates

  `ax.coords_to_point( [x_0, x_1, ...], [y_0, y_1, ...], ... )`

  `ax.coords_to_point( [[x_0, y_0, z_0], [x_1, y_1, z_1]] )`
* **Returns:**
  A point with respect to the scene’s coordinate system.
  The shape of the array will be similar to the shape of the input.
* **Return type:**
  np.ndarray

### Examples

```pycon
>>> from manim import Axes
>>> import numpy as np
>>> ax = Axes()
>>> np.around(ax.coords_to_point(1, 0, 0), 2)
array([0.86, 0.  , 0.  ])
>>> np.around(ax @ (1, 0, 0), 2)
array([0.86, 0.  , 0.  ])
>>> np.around(ax.coords_to_point([[0, 1], [1, 1], [1, 0]]), 2)
array([[0.  , 0.75, 0.  ],
       [0.86, 0.75, 0.  ],
       [0.86, 0.  , 0.  ]])
>>> np.around(
...     ax.coords_to_point([0, 1, 1], [1, 1, 0]), 2
... )  # Transposed version of the above
array([[0.  , 0.86, 0.86],
       [0.75, 0.75, 0.  ],
       [0.  , 0.  , 0.  ]])
```

#### get_axes()

Gets the axes.

* **Returns:**
  A pair of axes.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

#### get_axis_labels(x_label='x', y_label='y')

Defines labels for the x-axis and y-axis of the graph.

For increased control over the position of the labels,
use [`get_x_axis_label()`](manim.mobject.graphing.coordinate_systems.CoordinateSystem.md#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label) and
[`get_y_axis_label()`](manim.mobject.graphing.coordinate_systems.CoordinateSystem.md#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_y_axis_label).

* **Parameters:**
  * **x_label** (*float* *|* *str* *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The label for the x_axis. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) for `str` and `float` inputs.
  * **y_label** (*float* *|* *str* *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The label for the y_axis. Defaults to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) for `str` and `float` inputs.
* **Returns:**
  A [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) of the labels for the x_axis and y_axis.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

#### SEE ALSO
[`get_x_axis_label()`](manim.mobject.graphing.coordinate_systems.CoordinateSystem.md#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label)
[`get_y_axis_label()`](manim.mobject.graphing.coordinate_systems.CoordinateSystem.md#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_y_axis_label)

### Examples

#### plot_line_graph(x_values, y_values, z_values=None, line_color=ManimColor('#FFFF00'), add_vertex_dots=True, vertex_dot_radius=0.08, vertex_dot_style=None, \*\*kwargs)

Draws a line graph.

The graph connects the vertices formed from zipping
`x_values`, `y_values` and `z_values`. Also adds [`Dots`](manim.mobject.geometry.arc.Dot.md#manim.mobject.geometry.arc.Dot) at the
vertices if `add_vertex_dots` is set to `True`.

* **Parameters:**
  * **x_values** (*Iterable* *[**float* *]*) – Iterable of values along the x-axis.
  * **y_values** (*Iterable* *[**float* *]*) – Iterable of values along the y-axis.
  * **z_values** (*Iterable* *[**float* *]*  *|* *None*) – Iterable of values (zeros if z_values is None) along the z-axis.
  * **line_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – Color for the line graph.
  * **add_vertex_dots** (*bool*) – Whether or not to add [`Dot`](manim.mobject.geometry.arc.Dot.md#manim.mobject.geometry.arc.Dot) at each vertex.
  * **vertex_dot_radius** (*float*) – Radius for the [`Dot`](manim.mobject.geometry.arc.Dot.md#manim.mobject.geometry.arc.Dot) at each vertex.
  * **vertex_dot_style** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – Style arguments to be passed into [`Dot`](manim.mobject.geometry.arc.Dot.md#manim.mobject.geometry.arc.Dot) at each vertex.
  * **kwargs** (*Any*) – Additional arguments to be passed into [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).
* **Returns:**
  A VDict containing both the line and dots (if specified). The line can be accessed with: `line_graph["line_graph"]`.
  The dots can be accessed with: `line_graph["vertex_dots"]`.
* **Return type:**
  [`VDict`](manim.mobject.types.vectorized_mobject.VDict.md#manim.mobject.types.vectorized_mobject.VDict)

### Examples

#### point_to_coords(point)

Accepts a point from the scene and returns its coordinates with respect to the axes.

* **Parameters:**
  **point** (*Sequence* *[**float* *]*) – The point, i.e. `RIGHT` or `[0, 1, 0]`.
  Also accepts a list of points as `[RIGHT, [0, 1, 0]]`.
* **Returns:**
  The coordinates on the axes, i.e. `[4.0, 7.0]`.
  Or a list of coordinates if point is a list of points.
* **Return type:**
  np.ndarray[float]

### Examples

```pycon
>>> from manim import Axes, RIGHT
>>> import numpy as np
>>> ax = Axes(x_range=[0, 10, 2])
>>> np.around(ax.point_to_coords(RIGHT), 2)
array([5.83, 0.  ])
>>> np.around(ax.point_to_coords([[0, 0, 1], [1, 0, 0]]), 2)
array([[5.  , 0.  ],
       [5.83, 0.  ]])
```
