# OldMultiCamera

Qualified name: `manim.camera.mapping\_camera.OldMultiCamera`

### *class* OldMultiCamera(\*cameras_with_start_positions, \*\*kwargs)

Bases: [`Camera`](manim.camera.camera.Camera.md#manim.camera.camera.Camera)

* **Parameters:**
  **cameras_with_start_positions** (*tuple*) – Tuples of (Camera, (start_y, start_x)) indicating camera and
  its pixel offset on the final frame.

### Methods

| [`capture_mobjects`](#manim.camera.mapping_camera.OldMultiCamera.capture_mobjects)   | Capture mobjects by printing them on `pixel_array`.                                 |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [`init_background`](#manim.camera.mapping_camera.OldMultiCamera.init_background)     | Initialize the background.                                                          |
| [`set_background`](#manim.camera.mapping_camera.OldMultiCamera.set_background)       | Sets the background to the passed pixel_array after converting to valid RGB values. |
| [`set_pixel_array`](#manim.camera.mapping_camera.OldMultiCamera.set_pixel_array)     | Sets the pixel array of the camera to the passed pixel array.                       |

### Attributes

| `background_color`   |    |
|----------------------|----|
| `background_opacity` |    |

#### capture_mobjects(mobjects, \*\*kwargs)

Capture mobjects by printing them on `pixel_array`.

This is the essential function that converts the contents of a Scene
into an array, which is then converted to an image or video.

* **Parameters:**
  * **mobjects** – Mobjects to capture.
  * **kwargs** – Keyword arguments to be passed to `get_mobjects_to_display()`.

### Notes

For a list of classes that can currently be rendered, see `display_funcs()`.

#### init_background()

Initialize the background.
If self.background_image is the path of an image
the image is set as background; else, the default
background color fills the background.

#### set_background(pixel_array, \*\*kwargs)

Sets the background to the passed pixel_array after converting
to valid RGB values.

* **Parameters:**
  * **pixel_array** – The pixel array to set the background to.
  * **convert_from_floats** – Whether or not to convert floats values to proper RGB valid ones, by default False

#### set_pixel_array(pixel_array, \*\*kwargs)

Sets the pixel array of the camera to the passed pixel array.

* **Parameters:**
  * **pixel_array** – The pixel array to convert and then set as the camera’s pixel array.
  * **convert_from_floats** – Whether or not to convert float values to proper RGB values, by default False
