# VectorField

Qualified name: `manim.mobject.vector\_field.VectorField`

### *class* VectorField(func, color=None, color_scheme=None, min_color_scheme_value=0, max_color_scheme_value=2, colors=[ManimColor('#236B8E'), ManimColor('#83C167'), ManimColor('#FFFF00'), ManimColor('#FC6255')], \*\*kwargs)

Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

A vector field.

Vector fields are based on a function defining a vector at every position.
This class does by default not include any visible elements but provides
methods to move other [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) s along the vector field.

* **Parameters:**
  * **func** (*Callable* *[* *[*[*Point3D*](manim.typing.md#manim.typing.Point3D) *]* *,* [*Vector3D*](manim.typing.md#manim.typing.Vector3D) *]*) – The function defining the rate of change at every position of the VectorField.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – The color of the vector field. If set, position-specific coloring is disabled.
  * **color_scheme** (*Callable* *[* *[*[*Vector3D*](manim.typing.md#manim.typing.Vector3D) *]* *,* *float* *]*  *|* *None*) – A function mapping a vector to a single value. This value gives the position in the color gradient defined using min_color_scheme_value, max_color_scheme_value and colors.
  * **min_color_scheme_value** (*float*) – The value of the color_scheme function to be mapped to the first color in colors. Lower values also result in the first color of the gradient.
  * **max_color_scheme_value** (*float*) – The value of the color_scheme function to be mapped to the last color in colors. Higher values also result in the last color of the gradient.
  * **colors** (*Sequence* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*) – The colors defining the color gradient of the vector field.
  * **kwargs** – Additional arguments to be passed to the [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) constructor

### Methods

| [`fit_to_coordinate_system`](#manim.mobject.vector_field.VectorField.fit_to_coordinate_system)                           | Scale the vector field to fit a coordinate system.                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [`get_colored_background_image`](#manim.mobject.vector_field.VectorField.get_colored_background_image)                   | Generate an image that displays the vector field.                                                                                               |
| [`get_nudge_updater`](#manim.mobject.vector_field.VectorField.get_nudge_updater)                                         | Get an update function to move a [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) along the vector field.            |
| [`get_vectorized_rgba_gradient_function`](#manim.mobject.vector_field.VectorField.get_vectorized_rgba_gradient_function) | Generates a gradient of rgbas as a numpy array                                                                                                  |
| [`nudge`](#manim.mobject.vector_field.VectorField.nudge)                                                                 | Nudge a [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) along the vector field.                                     |
| [`nudge_submobjects`](#manim.mobject.vector_field.VectorField.nudge_submobjects)                                         | Apply a nudge along the vector field to all submobjects.                                                                                        |
| [`scale_func`](#manim.mobject.vector_field.VectorField.scale_func)                                                       | Scale a vector field function.                                                                                                                  |
| [`shift_func`](#manim.mobject.vector_field.VectorField.shift_func)                                                       | Shift a vector field function.                                                                                                                  |
| [`start_submobject_movement`](#manim.mobject.vector_field.VectorField.start_submobject_movement)                         | Start continuously moving all submobjects along the vector field.                                                                               |
| [`stop_submobject_movement`](#manim.mobject.vector_field.VectorField.stop_submobject_movement)                           | Stops the continuous movement started using [`start_submobject_movement()`](#manim.mobject.vector_field.VectorField.start_submobject_movement). |

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

#### \_original_\_init_\_(func, color=None, color_scheme=None, min_color_scheme_value=0, max_color_scheme_value=2, colors=[ManimColor('#236B8E'), ManimColor('#83C167'), ManimColor('#FFFF00'), ManimColor('#FC6255')], \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **func** (*Callable* *[* *[*[*Point3D*](manim.typing.md#manim.typing.Point3D) *]* *,* [*Vector3D*](manim.typing.md#manim.typing.Vector3D) *]*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **color_scheme** (*Callable* *[* *[*[*Vector3D*](manim.typing.md#manim.typing.Vector3D) *]* *,* *float* *]*  *|* *None*)
  * **min_color_scheme_value** (*float*)
  * **max_color_scheme_value** (*float*)
  * **colors** (*Sequence* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*)

#### fit_to_coordinate_system(coordinate_system)

Scale the vector field to fit a coordinate system.

This method is useful when the vector field is defined in a coordinate system
different from the one used to display the vector field.

This method can only be used once because it transforms the origin of each vector.

* **Parameters:**
  **coordinate_system** ([*CoordinateSystem*](manim.mobject.graphing.coordinate_systems.CoordinateSystem.md#manim.mobject.graphing.coordinate_systems.CoordinateSystem)) – The coordinate system to fit the vector field to.

#### get_colored_background_image(sampling_rate=5)

Generate an image that displays the vector field.

The color at each position is calculated by passing the positing through a
series of steps:
Calculate the vector field function at that position, map that vector to a
single value using self.color_scheme and finally generate a color from
that value using the color gradient.

* **Parameters:**
  **sampling_rate** (*int*) – The stepsize at which pixels get included in the image. Lower values give
  more accurate results, but may take a long time to compute.
* **Returns:**
  The vector field image.
* **Return type:**
  Image.Imgae

#### get_nudge_updater(speed=1, pointwise=False)

Get an update function to move a [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) along the vector field.

When used with [`add_updater()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.add_updater), the mobject will move along the vector field, where its speed is determined by the magnitude of the vector field.

* **Parameters:**
  * **speed** (*float*) – At speed=1 the distance a mobject moves per second is equal to the magnitude of the vector field along its path. The speed value scales the speed of such a mobject.
  * **pointwise** (*bool*) – Whether to move the mobject along the vector field. See [`nudge()`](#manim.mobject.vector_field.VectorField.nudge) for details.
* **Returns:**
  The update function.
* **Return type:**
  Callable[[[Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject), float], [Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)]

#### get_vectorized_rgba_gradient_function(start, end, colors)

Generates a gradient of rgbas as a numpy array

* **Parameters:**
  * **start** (*float*) – start value used for inverse interpolation at [`inverse_interpolate()`](manim.utils.bezier.md#manim.utils.bezier.inverse_interpolate)
  * **end** (*float*) – end value used for inverse interpolation at [`inverse_interpolate()`](manim.utils.bezier.md#manim.utils.bezier.inverse_interpolate)
  * **colors** (*Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*) – list of colors to generate the gradient
* **Return type:**
  function to generate the gradients as numpy arrays representing rgba values

#### nudge(mob, dt=1, substeps=1, pointwise=False)

Nudge a [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) along the vector field.

* **Parameters:**
  * **mob** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to move along the vector field
  * **dt** (*float*) – A scalar to the amount the mobject is moved along the vector field.
    The actual distance is based on the magnitude of the vector field.
  * **substeps** (*int*) – The amount of steps the whole nudge is divided into. Higher values
    give more accurate approximations.
  * **pointwise** (*bool*) – Whether to move the mobject along the vector field. If False the
    vector field takes effect on the center of the given
    [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject). If True the vector field takes effect on the
    points of the individual points of the [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject),
    potentially distorting it.
* **Returns:**
  This vector field.
* **Return type:**
  [VectorField](#manim.mobject.vector_field.VectorField)

### Examples

#### nudge_submobjects(dt=1, substeps=1, pointwise=False)

Apply a nudge along the vector field to all submobjects.

* **Parameters:**
  * **dt** (*float*) – A scalar to the amount the mobject is moved along the vector field.
    The actual distance is based on the magnitude of the vector field.
  * **substeps** (*int*) – The amount of steps the whole nudge is divided into. Higher values
    give more accurate approximations.
  * **pointwise** (*bool*) – Whether to move the mobject along the vector field. See [`nudge()`](#manim.mobject.vector_field.VectorField.nudge) for details.
* **Returns:**
  This vector field.
* **Return type:**
  [VectorField](#manim.mobject.vector_field.VectorField)

#### *static* scale_func(func, scalar)

Scale a vector field function.

* **Parameters:**
  * **func** (*Callable* *[* *[**ndarray* *]* *,* *ndarray* *]*) – The function defining a vector field.
  * **scalar** (*float*) – The scalar to be applied to the vector field.
* **Return type:**
  *Callable*[[*ndarray*], *ndarray*]

### Examples

* **Returns:**
  The scaled vector field function.
* **Return type:**
  Callable[[np.ndarray], np.ndarray]
* **Parameters:**
  * **func** (*Callable* *[* *[**ndarray* *]* *,* *ndarray* *]*)
  * **scalar** (*float*)

#### *static* shift_func(func, shift_vector)

Shift a vector field function.

* **Parameters:**
  * **func** (*Callable* *[* *[**ndarray* *]* *,* *ndarray* *]*) – The function defining a vector field.
  * **shift_vector** (*ndarray*) – The shift to be applied to the vector field.
* **Returns:**
  The shifted vector field function.
* **Return type:**
  Callable[[np.ndarray], np.ndarray]

#### start_submobject_movement(speed=1, pointwise=False)

Start continuously moving all submobjects along the vector field.

Calling this method multiple times will result in removing the previous updater created by this method.

* **Parameters:**
  * **speed** (*float*) – The speed at which to move the submobjects. See [`get_nudge_updater()`](#manim.mobject.vector_field.VectorField.get_nudge_updater) for details.
  * **pointwise** (*bool*) – Whether to move the mobject along the vector field. See [`nudge()`](#manim.mobject.vector_field.VectorField.nudge) for details.
* **Returns:**
  This vector field.
* **Return type:**
  [VectorField](#manim.mobject.vector_field.VectorField)

#### stop_submobject_movement()

Stops the continuous movement started using [`start_submobject_movement()`](#manim.mobject.vector_field.VectorField.start_submobject_movement).

* **Returns:**
  This vector field.
* **Return type:**
  [VectorField](#manim.mobject.vector_field.VectorField)
