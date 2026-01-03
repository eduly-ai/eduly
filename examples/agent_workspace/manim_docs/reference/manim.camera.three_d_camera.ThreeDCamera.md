# ThreeDCamera

Qualified name: `manim.camera.three\_d\_camera.ThreeDCamera`

### *class* ThreeDCamera(focal_distance=20.0, shading_factor=0.2, default_distance=5.0, light_source_start_point=array([-7., -9., 10.]), should_apply_shading=True, exponential_projection=False, phi=0, theta=-1.5707963267948966, gamma=0, zoom=1, \*\*kwargs)

Bases: [`Camera`](manim.camera.camera.Camera.md#manim.camera.camera.Camera)

Initializes the ThreeDCamera

* **Parameters:**
  * **\*kwargs** (*Any*) – Any keyword argument of Camera.
  * **focal_distance** (*float*)
  * **shading_factor** (*float*)
  * **default_distance** (*float*)
  * **light_source_start_point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **should_apply_shading** (*bool*)
  * **exponential_projection** (*bool*)
  * **phi** (*float*)
  * **theta** (*float*)
  * **gamma** (*float*)
  * **zoom** (*float*)
  * **\*kwargs**

### Methods

| [`add_fixed_in_frame_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects)             | This method allows the mobject to have a fixed position, even when the camera moves around.                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`add_fixed_orientation_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects)       | This method allows the mobject to have a fixed orientation, even when the camera moves around.                                                                                                                |
| [`capture_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.capture_mobjects)                                   | Capture mobjects by printing them on `pixel_array`.                                                                                                                                                           |
| [`generate_rotation_matrix`](#manim.camera.three_d_camera.ThreeDCamera.generate_rotation_matrix)                   | Generates a rotation matrix based off the current position of the camera.                                                                                                                                     |
| [`get_fill_rgbas`](#manim.camera.three_d_camera.ThreeDCamera.get_fill_rgbas)                                       | Returns the RGBA array of the fill of the passed VMobject                                                                                                                                                     |
| [`get_focal_distance`](#manim.camera.three_d_camera.ThreeDCamera.get_focal_distance)                               | Returns focal_distance of the Camera.                                                                                                                                                                         |
| [`get_gamma`](#manim.camera.three_d_camera.ThreeDCamera.get_gamma)                                                 | Returns the rotation of the camera about the vector from the ORIGIN to the Camera.                                                                                                                            |
| [`get_mobjects_to_display`](#manim.camera.three_d_camera.ThreeDCamera.get_mobjects_to_display)                     | Used to get the list of mobjects to display with the camera.                                                                                                                                                  |
| [`get_phi`](#manim.camera.three_d_camera.ThreeDCamera.get_phi)                                                     | Returns the Polar angle (the angle off Z_AXIS) phi.                                                                                                                                                           |
| [`get_rotation_matrix`](#manim.camera.three_d_camera.ThreeDCamera.get_rotation_matrix)                             | Returns the matrix corresponding to the current position of the camera.                                                                                                                                       |
| [`get_stroke_rgbas`](#manim.camera.three_d_camera.ThreeDCamera.get_stroke_rgbas)                                   | Gets the RGBA array for the stroke of the passed VMobject.                                                                                                                                                    |
| [`get_theta`](#manim.camera.three_d_camera.ThreeDCamera.get_theta)                                                 | Returns the Azimuthal i.e the angle that spins the camera around the Z_AXIS.                                                                                                                                  |
| [`get_value_trackers`](#manim.camera.three_d_camera.ThreeDCamera.get_value_trackers)                               | A list of [`ValueTrackers`](manim.mobject.value_tracker.ValueTracker.md#manim.mobject.value_tracker.ValueTracker) of phi, theta, focal_distance, gamma and zoom.                                              |
| [`get_zoom`](#manim.camera.three_d_camera.ThreeDCamera.get_zoom)                                                   | Returns the zoom amount of the camera.                                                                                                                                                                        |
| `modified_rgbas`                                                                                                   |                                                                                                                                                                                                               |
| [`project_point`](#manim.camera.three_d_camera.ThreeDCamera.project_point)                                         | Applies the current rotation_matrix as a projection matrix to the passed point.                                                                                                                               |
| [`project_points`](#manim.camera.three_d_camera.ThreeDCamera.project_points)                                       | Applies the current rotation_matrix as a projection matrix to the passed array of points.                                                                                                                     |
| [`remove_fixed_in_frame_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.remove_fixed_in_frame_mobjects)       | If a mobject was fixed in frame by passing it through [`add_fixed_in_frame_mobjects()`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects), then this undoes that fixing.                 |
| [`remove_fixed_orientation_mobjects`](#manim.camera.three_d_camera.ThreeDCamera.remove_fixed_orientation_mobjects) | If a mobject was fixed in its orientation by passing it through [`add_fixed_orientation_mobjects()`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects), then this undoes that fixing. |
| [`reset_rotation_matrix`](#manim.camera.three_d_camera.ThreeDCamera.reset_rotation_matrix)                         | Sets the value of self.rotation_matrix to the matrix corresponding to the current position of the camera                                                                                                      |
| [`set_focal_distance`](#manim.camera.three_d_camera.ThreeDCamera.set_focal_distance)                               | Sets the focal_distance of the Camera.                                                                                                                                                                        |
| [`set_gamma`](#manim.camera.three_d_camera.ThreeDCamera.set_gamma)                                                 | Sets the angle of rotation of the camera about the vector from the ORIGIN to the Camera.                                                                                                                      |
| [`set_phi`](#manim.camera.three_d_camera.ThreeDCamera.set_phi)                                                     | Sets the polar angle i.e the angle between Z_AXIS and Camera through ORIGIN in radians.                                                                                                                       |
| [`set_theta`](#manim.camera.three_d_camera.ThreeDCamera.set_theta)                                                 | Sets the azimuthal angle i.e the angle that spins the camera around Z_AXIS in radians.                                                                                                                        |
| [`set_zoom`](#manim.camera.three_d_camera.ThreeDCamera.set_zoom)                                                   | Sets the zoom amount of the camera.                                                                                                                                                                           |
| `transform_points_pre_display`                                                                                     |                                                                                                                                                                                                               |

### Attributes

| `background_color`   |    |
|----------------------|----|
| `background_opacity` |    |
| `frame_center`       |    |

#### add_fixed_in_frame_mobjects(\*mobjects)

This method allows the mobject to have a fixed position,
even when the camera moves around.
E.G If it was passed through this method, at the top of the frame, it
will continue to be displayed at the top of the frame.

Highly useful when displaying Titles or formulae or the like.

* **Parameters:**
  **\*\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to fix in frame.
* **Return type:**
  None

#### add_fixed_orientation_mobjects(\*mobjects, use_static_center_func=False, center_func=None)

This method allows the mobject to have a fixed orientation,
even when the camera moves around.
E.G If it was passed through this method, facing the camera, it
will continue to face the camera even as the camera moves.
Highly useful when adding labels to graphs and the like.

* **Parameters:**
  * **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject whose orientation must be fixed.
  * **use_static_center_func** (*bool*) – Whether or not to use the function that takes the mobject’s
    center as centerpoint, by default False
  * **center_func** (*Callable* *[* *[* *]* *,* [*Point3D*](manim.typing.md#manim.typing.Point3D) *]*  *|* *None*) – The function which returns the centerpoint
    with respect to which the mobject will be oriented, by default None
* **Return type:**
  None

#### capture_mobjects(mobjects, \*\*kwargs)

Capture mobjects by printing them on `pixel_array`.

This is the essential function that converts the contents of a Scene
into an array, which is then converted to an image or video.

* **Parameters:**
  * **mobjects** (*Iterable* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – Mobjects to capture.
  * **kwargs** (*Any*) – Keyword arguments to be passed to [`get_mobjects_to_display()`](#manim.camera.three_d_camera.ThreeDCamera.get_mobjects_to_display).
* **Return type:**
  None

### Notes

For a list of classes that can currently be rendered, see `display_funcs()`.

#### generate_rotation_matrix()

Generates a rotation matrix based off the current position of the camera.

* **Returns:**
  The matrix corresponding to the current position of the camera.
* **Return type:**
  np.array

#### get_fill_rgbas(vmobject)

Returns the RGBA array of the fill of the passed VMobject

* **Parameters:**
  **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The VMobject
* **Returns:**
  The RGBA Array of the fill of the VMobject
* **Return type:**
  np.array

#### get_focal_distance()

Returns focal_distance of the Camera.

* **Returns:**
  The focal_distance of the Camera in MUnits.
* **Return type:**
  float

#### get_gamma()

Returns the rotation of the camera about the vector from the ORIGIN to the Camera.

* **Returns:**
  The angle of rotation of the camera about the vector
  from the ORIGIN to the Camera in radians
* **Return type:**
  float

#### get_mobjects_to_display(\*args, \*\*kwargs)

Used to get the list of mobjects to display
with the camera.

* **Parameters:**
  * **mobjects** – The Mobjects
  * **include_submobjects** – Whether or not to include the submobjects of mobjects, by default True
  * **excluded_mobjects** – Any mobjects to exclude, by default None
  * **args** (*Any*)
  * **kwargs** (*Any*)
* **Returns:**
  list of mobjects
* **Return type:**
  list

#### get_phi()

Returns the Polar angle (the angle off Z_AXIS) phi.

* **Returns:**
  The Polar angle in radians.
* **Return type:**
  float

#### get_rotation_matrix()

Returns the matrix corresponding to the current position of the camera.

* **Returns:**
  The matrix corresponding to the current position of the camera.
* **Return type:**
  np.array

#### get_stroke_rgbas(vmobject, background=False)

Gets the RGBA array for the stroke of the passed
VMobject.

* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The VMobject
  * **background** (*bool*) – Whether or not to consider the background when getting the stroke
    RGBAs, by default False
* **Returns:**
  The RGBA array of the stroke.
* **Return type:**
  np.ndarray

#### get_theta()

Returns the Azimuthal i.e the angle that spins the camera around the Z_AXIS.

* **Returns:**
  The Azimuthal angle in radians.
* **Return type:**
  float

#### get_value_trackers()

A list of [`ValueTrackers`](manim.mobject.value_tracker.ValueTracker.md#manim.mobject.value_tracker.ValueTracker) of phi, theta, focal_distance,
gamma and zoom.

* **Returns:**
  list of ValueTracker objects
* **Return type:**
  list

#### get_zoom()

Returns the zoom amount of the camera.

* **Returns:**
  The zoom amount of the camera.
* **Return type:**
  float

#### project_point(point)

Applies the current rotation_matrix as a projection
matrix to the passed point.

* **Parameters:**
  **point** ([*Point3D*](manim.typing.md#manim.typing.Point3D)) – The point to project.
* **Returns:**
  The point after projection.
* **Return type:**
  np.array

#### project_points(points)

Applies the current rotation_matrix as a projection
matrix to the passed array of points.

* **Parameters:**
  **points** ([*Point3D_Array*](manim.typing.md#manim.typing.Point3D_Array)) – The list of points to project.
* **Returns:**
  The points after projecting.
* **Return type:**
  np.array

#### remove_fixed_in_frame_mobjects(\*mobjects)

If a mobject was fixed in frame by passing it through
[`add_fixed_in_frame_mobjects()`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_in_frame_mobjects), then this undoes that fixing.
The Mobject will no longer be fixed in frame.

* **Parameters:**
  **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects which need not be fixed in frame any longer.
* **Return type:**
  None

#### remove_fixed_orientation_mobjects(\*mobjects)

If a mobject was fixed in its orientation by passing it through
[`add_fixed_orientation_mobjects()`](#manim.camera.three_d_camera.ThreeDCamera.add_fixed_orientation_mobjects), then this undoes that fixing.
The Mobject will no longer have a fixed orientation.

* **Parameters:**
  **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects whose orientation need not be fixed any longer.
* **Return type:**
  None

#### reset_rotation_matrix()

Sets the value of self.rotation_matrix to
the matrix corresponding to the current position of the camera

* **Return type:**
  None

#### set_focal_distance(value)

Sets the focal_distance of the Camera.

* **Parameters:**
  **value** (*float*) – The focal_distance of the Camera.
* **Return type:**
  None

#### set_gamma(value)

Sets the angle of rotation of the camera about the vector from the ORIGIN to the Camera.

* **Parameters:**
  **value** (*float*) – The new angle of rotation of the camera.
* **Return type:**
  None

#### set_phi(value)

Sets the polar angle i.e the angle between Z_AXIS and Camera through ORIGIN in radians.

* **Parameters:**
  **value** (*float*) – The new value of the polar angle in radians.
* **Return type:**
  None

#### set_theta(value)

Sets the azimuthal angle i.e the angle that spins the camera around Z_AXIS in radians.

* **Parameters:**
  **value** (*float*) – The new value of the azimuthal angle in radians.
* **Return type:**
  None

#### set_zoom(value)

Sets the zoom amount of the camera.

* **Parameters:**
  **value** (*float*) – The zoom amount of the camera.
* **Return type:**
  None
