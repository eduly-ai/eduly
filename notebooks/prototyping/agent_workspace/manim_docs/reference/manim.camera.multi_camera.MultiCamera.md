# MultiCamera

Qualified name: `manim.camera.multi\_camera.MultiCamera`

### *class* MultiCamera(image_mobjects_from_cameras=None, allow_cameras_to_capture_their_own_display=False, \*\*kwargs)

Bases: [`MovingCamera`](manim.camera.moving_camera.MovingCamera.md#manim.camera.moving_camera.MovingCamera)

Camera Object that allows for multiple perspectives.

Initialises the MultiCamera

* **Parameters:**
  * **image_mobjects_from_cameras** (*Iterable* *[*[*ImageMobjectFromCamera*](manim.mobject.types.image_mobject.ImageMobjectFromCamera.md#manim.mobject.types.image_mobject.ImageMobjectFromCamera) *]*  *|* *None*)
  * **kwargs** (*Any*) – Any valid keyword arguments of MovingCamera.
  * **allow_cameras_to_capture_their_own_display** (*bool*)

### Methods

| [`add_image_mobject_from_camera`](#manim.camera.multi_camera.MultiCamera.add_image_mobject_from_camera)       | Adds an ImageMobject that's been obtained from the camera into the list `self.image_mobject_from_cameras`              |
|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [`capture_mobjects`](#manim.camera.multi_camera.MultiCamera.capture_mobjects)                                 | Capture mobjects by printing them on `pixel_array`.                                                                    |
| [`get_mobjects_indicating_movement`](#manim.camera.multi_camera.MultiCamera.get_mobjects_indicating_movement) | Returns all mobjects whose movement implies that the camera should think of all other mobjects on the screen as moving |
| [`reset`](#manim.camera.multi_camera.MultiCamera.reset)                                                       | Resets the MultiCamera.                                                                                                |
| [`update_sub_cameras`](#manim.camera.multi_camera.MultiCamera.update_sub_cameras)                             | Reshape sub_camera pixel_arrays                                                                                        |

### Attributes

| `background_color`   |                                                                |
|----------------------|----------------------------------------------------------------|
| `background_opacity` |                                                                |
| `frame_center`       | Returns the centerpoint of the frame in cartesian coordinates. |
| `frame_height`       | Returns the height of the frame.                               |
| `frame_width`        | Returns the width of the frame                                 |

#### add_image_mobject_from_camera(image_mobject_from_camera)

Adds an ImageMobject that’s been obtained from the camera
into the list `self.image_mobject_from_cameras`

* **Parameters:**
  **image_mobject_from_camera** ([*ImageMobjectFromCamera*](manim.mobject.types.image_mobject.ImageMobjectFromCamera.md#manim.mobject.types.image_mobject.ImageMobjectFromCamera)) – The ImageMobject to add to self.image_mobject_from_cameras
* **Return type:**
  None

#### capture_mobjects(mobjects, \*\*kwargs)

Capture mobjects by printing them on `pixel_array`.

This is the essential function that converts the contents of a Scene
into an array, which is then converted to an image or video.

* **Parameters:**
  * **mobjects** (*Iterable* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – Mobjects to capture.
  * **kwargs** (*Any*) – Keyword arguments to be passed to `get_mobjects_to_display()`.
* **Return type:**
  None

### Notes

For a list of classes that can currently be rendered, see `display_funcs()`.

#### get_mobjects_indicating_movement()

Returns all mobjects whose movement implies that the camera
should think of all other mobjects on the screen as moving

* **Return type:**
  list

#### reset()

Resets the MultiCamera.

* **Returns:**
  The reset MultiCamera
* **Return type:**
  [MultiCamera](#manim.camera.multi_camera.MultiCamera)

#### update_sub_cameras()

Reshape sub_camera pixel_arrays

* **Return type:**
  None
