# VectorScene

Qualified name: `manim.scene.vector\_space\_scene.VectorScene`

### *class* VectorScene(basis_vector_stroke_width=6.0, \*\*kwargs)

Bases: [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene)

### Methods

| [`add_axes`](#manim.scene.vector_space_scene.VectorScene.add_axes)                                 | Adds a pair of Axes to the Scene.                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`add_plane`](#manim.scene.vector_space_scene.VectorScene.add_plane)                               | Adds a NumberPlane object to the background.                                                                                                                                                           |
| [`add_vector`](#manim.scene.vector_space_scene.VectorScene.add_vector)                             | Returns the Vector after adding it to the Plane.                                                                                                                                                       |
| [`coords_to_vector`](#manim.scene.vector_space_scene.VectorScene.coords_to_vector)                 | This method writes the vector as a column matrix (henceforth called the label), takes the values in it one by one, and form the corresponding lines that make up the x and y components of the vector. |
| [`get_basis_vector_labels`](#manim.scene.vector_space_scene.VectorScene.get_basis_vector_labels)   | Returns naming labels for the basis vectors.                                                                                                                                                           |
| [`get_basis_vectors`](#manim.scene.vector_space_scene.VectorScene.get_basis_vectors)               | Returns a VGroup of the Basis Vectors (1,0) and (0,1)                                                                                                                                                  |
| [`get_vector`](#manim.scene.vector_space_scene.VectorScene.get_vector)                             | Returns an arrow on the Plane given an input numerical vector.                                                                                                                                         |
| [`get_vector_label`](#manim.scene.vector_space_scene.VectorScene.get_vector_label)                 | Returns naming labels for the passed vector.                                                                                                                                                           |
| [`label_vector`](#manim.scene.vector_space_scene.VectorScene.label_vector)                         | Shortcut method for creating, and animating the addition of a label for the vector.                                                                                                                    |
| [`lock_in_faded_grid`](#manim.scene.vector_space_scene.VectorScene.lock_in_faded_grid)             | This method freezes the NumberPlane and Axes that were already in the background, and adds new, manipulatable ones to the foreground.                                                                  |
| `position_x_coordinate`                                                                            |                                                                                                                                                                                                        |
| `position_y_coordinate`                                                                            |                                                                                                                                                                                                        |
| [`show_ghost_movement`](#manim.scene.vector_space_scene.VectorScene.show_ghost_movement)           | This method plays an animation that partially shows the entire plane moving in the direction of a particular vector.                                                                                   |
| [`vector_to_coords`](#manim.scene.vector_space_scene.VectorScene.vector_to_coords)                 | This method displays vector as a Vector() based vector, and then shows the corresponding lines that make up the x and y components of the vector.                                                      |
| [`write_vector_coordinates`](#manim.scene.vector_space_scene.VectorScene.write_vector_coordinates) | Returns a column matrix indicating the vector coordinates, after writing them to the screen.                                                                                                           |

### Attributes

| `camera`   |                                        |
|------------|----------------------------------------|
| `time`     | The time since the start of the scene. |
* **Parameters:**
  * **basis_vector_stroke_width** (*float*)
  * **kwargs** (*Any*)

#### add_axes(animate=False, color=ManimColor('#FFFFFF'))

Adds a pair of Axes to the Scene.

* **Parameters:**
  * **animate** (*bool*) – Whether or not to animate the addition of the axes through Create.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*) – The color of the axes. Defaults to WHITE.
* **Return type:**
  [Axes](manim.mobject.graphing.coordinate_systems.Axes.md#manim.mobject.graphing.coordinate_systems.Axes)

#### add_plane(animate=False, \*\*kwargs)

Adds a NumberPlane object to the background.

* **Parameters:**
  * **animate** (*bool*) – Whether or not to animate the addition of the plane via Create.
  * **\*\*kwargs** (*Any*) – Any valid keyword arguments accepted by NumberPlane.
* **Returns:**
  The NumberPlane object.
* **Return type:**
  [NumberPlane](manim.mobject.graphing.coordinate_systems.NumberPlane.md#manim.mobject.graphing.coordinate_systems.NumberPlane)

#### add_vector(vector, color=ManimColor('#FFFF00'), animate=True, \*\*kwargs)

Returns the Vector after adding it to the Plane.

* **Parameters:**
  * **vector** ([*Arrow*](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow) *|* [*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – It can be a pre-made graphical vector, or the
    coordinates of one.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*) – The string of the hex color of the vector.
    This is only taken into consideration if
    ‘vector’ is not an Arrow. Defaults to YELLOW.
  * **animate** (*bool*) – Whether or not to animate the addition of the vector
    by using GrowArrow
  * **\*\*kwargs** (*Any*) – Any valid keyword argument of Arrow.
    These are only considered if vector is not
    an Arrow.
* **Returns:**
  The arrow representing the vector.
* **Return type:**
  [Arrow](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow)

#### coords_to_vector(vector, coords_start=array([2., 2., 0.]), clean_up=True)

This method writes the vector as a column matrix (henceforth called the label),
takes the values in it one by one, and form the corresponding
lines that make up the x and y components of the vector. Then, an
Vector() based vector is created between the lines on the Screen.

* **Parameters:**
  * **vector** ([*Vector2DLike*](manim.typing.md#manim.typing.Vector2DLike)) – The vector to show.
  * **coords_start** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The starting point of the location of
    the label of the vector that shows it
    numerically.
    Defaults to 2 \* RIGHT + 2 \* UP or (2,2)
  * **clean_up** (*bool*) – Whether or not to remove whatever
    this method did after it’s done.
* **Return type:**
  None

#### get_basis_vector_labels(\*\*kwargs)

Returns naming labels for the basis vectors.

* **Parameters:**
  **\*\*kwargs** (*Any*) – 

  Any valid keyword arguments of get_vector_label:
  : vector,
    label (str,MathTex)
    at_tip (bool=False),
    direction (str=”left”),
    rotate (bool),
    color (str),
    label_scale_factor=VECTOR_LABEL_SCALE_FACTOR (int, float),
* **Return type:**
  [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

#### get_basis_vectors(i_hat_color=ManimColor('#83C167'), j_hat_color=ManimColor('#FC6255'))

Returns a VGroup of the Basis Vectors (1,0) and (0,1)

* **Parameters:**
  * **i_hat_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*) – The hex colour to use for the basis vector in the x direction
  * **j_hat_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*) – The hex colour to use for the basis vector in the y direction
* **Returns:**
  VGroup of the Vector Mobjects representing the basis vectors.
* **Return type:**
  [VGroup](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

#### get_vector(numerical_vector, \*\*kwargs)

Returns an arrow on the Plane given an input numerical vector.

* **Parameters:**
  * **numerical_vector** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The Vector to plot.
  * **\*\*kwargs** (*Any*) – Any valid keyword argument of Arrow.
* **Returns:**
  The Arrow representing the Vector.
* **Return type:**
  [Arrow](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow)

#### get_vector_label(vector, label, at_tip=False, direction='left', rotate=False, color=None, label_scale_factor=0.8)

Returns naming labels for the passed vector.

* **Parameters:**
  * **vector** ([*Vector*](manim.mobject.geometry.line.Vector.md#manim.mobject.geometry.line.Vector)) – Vector Object for which to get the label.
  * **at_tip** (*bool*) – Whether or not to place the label at the tip of the vector.
  * **direction** (*str*) – If the label should be on the “left” or right of the vector.
  * **rotate** (*bool*) – Whether or not to rotate it to align it with the vector.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – The color to give the label.
  * **label_scale_factor** (*float*) – How much to scale the label by.
  * **label** ([*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* *str*)
* **Returns:**
  The MathTex of the label.
* **Return type:**
  [MathTex](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex)

#### label_vector(vector, label, animate=True, \*\*kwargs)

Shortcut method for creating, and animating the addition of
a label for the vector.

* **Parameters:**
  * **vector** ([*Vector*](manim.mobject.geometry.line.Vector.md#manim.mobject.geometry.line.Vector)) – The vector for which the label must be added.
  * **label** ([*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* *str*) – The MathTex/string of the label.
  * **animate** (*bool*) – Whether or not to animate the labelling w/ Write
  * **\*\*kwargs** (*Any*) – Any valid keyword argument of get_vector_label
* **Returns:**
  The MathTex of the label.
* **Return type:**
  [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex)

#### lock_in_faded_grid(dimness=0.7, axes_dimness=0.5)

This method freezes the NumberPlane and Axes that were already
in the background, and adds new, manipulatable ones to the foreground.

* **Parameters:**
  * **dimness** (*float*) – The required dimness of the NumberPlane
  * **axes_dimness** (*float*) – The required dimness of the Axes.
* **Return type:**
  None

#### show_ghost_movement(vector)

This method plays an animation that partially shows the entire plane moving
in the direction of a particular vector. This is useful when you wish to
convey the idea of mentally moving the entire plane in a direction, without
actually moving the plane.

* **Parameters:**
  **vector** ([*Arrow*](manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow) *|* [*Vector2DLike*](manim.typing.md#manim.typing.Vector2DLike) *|* [*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The vector which indicates the direction of movement.
* **Return type:**
  None

#### vector_to_coords(vector, integer_labels=True, clean_up=True)

This method displays vector as a Vector() based vector, and then shows
the corresponding lines that make up the x and y components of the vector.
Then, a column matrix (henceforth called the label) is created near the
head of the Vector.

* **Parameters:**
  * **vector** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The vector to show.
  * **integer_labels** (*bool*) – Whether or not to round the value displayed.
    in the vector’s label to the nearest integer
  * **clean_up** (*bool*) – Whether or not to remove whatever
    this method did after it’s done.
* **Return type:**
  tuple[[*Matrix*](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix), [*Line*](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line), [*Line*](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)]

#### write_vector_coordinates(vector, \*\*kwargs)

Returns a column matrix indicating the vector coordinates,
after writing them to the screen.

* **Parameters:**
  * **vector** ([*Vector*](manim.mobject.geometry.line.Vector.md#manim.mobject.geometry.line.Vector)) – The arrow representing the vector.
  * **\*\*kwargs** (*Any*) – Any valid keyword arguments of [`coordinate_label()`](manim.mobject.geometry.line.Vector.md#manim.mobject.geometry.line.Vector.coordinate_label):
* **Returns:**
  The column matrix representing the vector.
* **Return type:**
  [`Matrix`](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix)
