# PolarPlane

Qualified name: `manim.mobject.graphing.coordinate\_systems.PolarPlane`

### *class* PolarPlane(radius_max=4.0, size=None, radius_step=1, azimuth_step=None, azimuth_units='PI radians', azimuth_compact_fraction=True, azimuth_offset=0, azimuth_direction='CCW', azimuth_label_buff=0.1, azimuth_label_font_size=24, radius_config=None, background_line_style=None, faded_line_style=None, faded_line_ratio=1, make_smooth_after_applying_functions=True, \*\*kwargs)

Bases: [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.md#manim.mobject.graphing.coordinate_systems.Axes)

Creates a polar plane with background lines.

* **Parameters:**
  * **azimuth_step** (*float* *|* *None*) – 

    The number of divisions in the azimuth (also known as the angular coordinate or polar angle). If `None` is specified then it will use the default
    specified by `azimuth_units`:
    - `"PI radians"` or `"TAU radians"`: 20
    - `"degrees"`: 36
    - `"gradians"`: 40
    - `None`: 1

    A non-integer value will result in a partial division at the end of the circle.
  * **size** (*float* *|* *None*) – The diameter of the plane.
  * **radius_step** (*float*) – The distance between faded radius lines.
  * **radius_max** (*float*) – The maximum value of the radius.
  * **azimuth_units** (*str*) – 

    Specifies a default labelling system for the azimuth. Choices are:
    - `"PI radians"`: Fractional labels in the interval $\left[0, 2\pi\right]$ with $\pi$ as a constant.
    - `"TAU radians"`: Fractional labels in the interval $\left[0, \tau\right]$ (where $\tau = 2\pi$) with $\tau$ as a constant.
    - `"degrees"`: Decimal labels in the interval $\left[0, 360\right]$ with a degree ($^{\circ}$) symbol.
    - `"gradians"`: Decimal labels in the interval $\left[0, 400\right]$ with a superscript “g” ($^{g}$).
    - `None`: Decimal labels in the interval $\left[0, 1\right]$.
  * **azimuth_compact_fraction** (*bool*) – If the `azimuth_units` choice has fractional labels, choose whether to
    combine the constant in a compact form $\tfrac{xu}{y}$ as opposed to
    $\tfrac{x}{y}u$, where $u$ is the constant.
  * **azimuth_offset** (*float*) – The angle offset of the azimuth, expressed in radians.
  * **azimuth_direction** (*str*) – 

    The direction of the azimuth.
    - `"CW"`: Clockwise.
    - `"CCW"`: Anti-clockwise.
  * **azimuth_label_buff** (*float*) – The buffer for the azimuth labels.
  * **azimuth_label_font_size** (*float*) – The font size of the azimuth labels.
  * **radius_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – The axis config for the radius.
  * **background_line_style** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **faded_line_style** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **faded_line_ratio** (*int*)
  * **make_smooth_after_applying_functions** (*bool*)
  * **kwargs** (*Any*)

### Examples

### Methods

| [`add_coordinates`](#manim.mobject.graphing.coordinate_systems.PolarPlane.add_coordinates)             | Adds the coordinates.           |
|--------------------------------------------------------------------------------------------------------|---------------------------------|
| [`get_axes`](#manim.mobject.graphing.coordinate_systems.PolarPlane.get_axes)                           | Gets the axes.                  |
| [`get_coordinate_labels`](#manim.mobject.graphing.coordinate_systems.PolarPlane.get_coordinate_labels) | Gets labels for the coordinates |
| `get_radian_label`                                                                                     |                                 |
| `get_vector`                                                                                           |                                 |
| `prepare_for_nonlinear_transform`                                                                      |                                 |

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

Generate all the lines and circles, faded and not faded.

* **Returns:**
  The first (i.e the non faded lines and circles) and second (i.e the faded lines and circles) sets of lines and circles, respectively.
* **Return type:**
  Tuple[[`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup), [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)]

#### \_init_background_lines()

Will init all the lines of NumberPlanes (faded or not)

* **Return type:**
  None

#### \_original_\_init_\_(radius_max=4.0, size=None, radius_step=1, azimuth_step=None, azimuth_units='PI radians', azimuth_compact_fraction=True, azimuth_offset=0, azimuth_direction='CCW', azimuth_label_buff=0.1, azimuth_label_font_size=24, radius_config=None, background_line_style=None, faded_line_style=None, faded_line_ratio=1, make_smooth_after_applying_functions=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **radius_max** (*float*)
  * **size** (*float* *|* *None*)
  * **radius_step** (*float*)
  * **azimuth_step** (*float* *|* *None*)
  * **azimuth_units** (*str*)
  * **azimuth_compact_fraction** (*bool*)
  * **azimuth_offset** (*float*)
  * **azimuth_direction** (*str*)
  * **azimuth_label_buff** (*float*)
  * **azimuth_label_font_size** (*float*)
  * **radius_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **background_line_style** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **faded_line_style** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **faded_line_ratio** (*int*)
  * **make_smooth_after_applying_functions** (*bool*)
  * **kwargs** (*Any*)

#### add_coordinates(r_values=None, a_values=None)

Adds the coordinates.

* **Parameters:**
  * **r_values** (*Iterable* *[**float* *]*  *|* *None*) – Iterable of values along the radius, by default None.
  * **a_values** (*Iterable* *[**float* *]*  *|* *None*) – Iterable of values along the azimuth, by default None.
* **Return type:**
  *Self*

#### get_axes()

Gets the axes.

* **Returns:**
  A pair of axes.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

#### get_coordinate_labels(r_values=None, a_values=None, \*\*kwargs)

Gets labels for the coordinates

* **Parameters:**
  * **r_values** (*Iterable* *[**float* *]*  *|* *None*) – Iterable of values along the radius, by default None.
  * **a_values** (*Iterable* *[**float* *]*  *|* *None*) – Iterable of values along the azimuth, by default None.
  * **kwargs** (*Any*)
* **Returns:**
  Labels for the radius and azimuth values.
* **Return type:**
  [VDict](manim.mobject.types.vectorized_mobject.VDict.md#manim.mobject.types.vectorized_mobject.VDict)
