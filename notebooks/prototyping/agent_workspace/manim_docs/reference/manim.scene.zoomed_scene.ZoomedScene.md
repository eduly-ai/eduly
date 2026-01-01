# ZoomedScene

Qualified name: `manim.scene.zoomed\_scene.ZoomedScene`

### *class* ZoomedScene(camera_class=<class 'manim.camera.multi_camera.MultiCamera'>, zoomed_display_height=3, zoomed_display_width=3, zoomed_display_center=None, zoomed_display_corner=array([1., 1., 0.]), zoomed_display_corner_buff=0.5, zoomed_camera_config={'background_opacity': 1, 'default_frame_stroke_width': 2}, zoomed_camera_image_mobject_config={}, zoomed_camera_frame_starting_position=array([0., 0., 0.]), zoom_factor=0.15, image_frame_stroke_width=3, zoom_activated=False, \*\*kwargs)

Bases: [`MovingCameraScene`](manim.scene.moving_camera_scene.MovingCameraScene.md#manim.scene.moving_camera_scene.MovingCameraScene)

This is a Scene with special configurations made for when
a particular part of the scene must be zoomed in on and displayed
separately.

### Methods

| [`activate_zooming`](#manim.scene.zoomed_scene.ZoomedScene.activate_zooming)                                         | This method is used to activate the zooming for the zoomed_camera.                                        |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`get_zoom_factor`](#manim.scene.zoomed_scene.ZoomedScene.get_zoom_factor)                                           | Returns the Zoom factor of the Zoomed camera.                                                             |
| [`get_zoom_in_animation`](#manim.scene.zoomed_scene.ZoomedScene.get_zoom_in_animation)                               | Returns the animation of camera zooming in.                                                               |
| [`get_zoomed_display_pop_out_animation`](#manim.scene.zoomed_scene.ZoomedScene.get_zoomed_display_pop_out_animation) | This is the animation of the popping out of the mini-display that shows the content of the zoomed camera. |
| [`setup`](#manim.scene.zoomed_scene.ZoomedScene.setup)                                                               | This method is used internally by Manim to setup the scene for proper use.                                |

### Attributes

| `camera`   |                                        |
|------------|----------------------------------------|
| `time`     | The time since the start of the scene. |
* **Parameters:**
  * **camera_class** (*type* *[*[*Camera*](manim.camera.camera.Camera.md#manim.camera.camera.Camera) *]*)
  * **zoomed_display_height** (*float*)
  * **zoomed_display_width** (*float*)
  * **zoomed_display_center** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*)
  * **zoomed_display_corner** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D))
  * **zoomed_display_corner_buff** (*float*)
  * **zoomed_camera_config** (*dict* *[**str* *,* *Any* *]*)
  * **zoomed_camera_image_mobject_config** (*dict* *[**str* *,* *Any* *]*)
  * **zoomed_camera_frame_starting_position** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **zoom_factor** (*float*)
  * **image_frame_stroke_width** (*float*)
  * **zoom_activated** (*bool*)
  * **kwargs** (*Any*)

#### activate_zooming(animate=False)

This method is used to activate the zooming for the zoomed_camera.

* **Parameters:**
  **animate** (*bool*) – Whether or not to animate the activation
  of the zoomed camera.
* **Return type:**
  None

#### get_zoom_factor()

Returns the Zoom factor of the Zoomed camera.

Defined as the ratio between the height of the zoomed camera and
the height of the zoomed mini display.

* **Returns:**
  The zoom factor.
* **Return type:**
  float

#### get_zoom_in_animation(run_time=2, \*\*kwargs)

Returns the animation of camera zooming in.

* **Parameters:**
  * **run_time** (*float*) – The run_time of the animation of the camera zooming in.
  * **\*\*kwargs** (*Any*) – Any valid keyword arguments of ApplyMethod()
* **Returns:**
  The animation of the camera zooming in.
* **Return type:**
  [ApplyMethod](manim.animation.transform.ApplyMethod.md#manim.animation.transform.ApplyMethod)

#### get_zoomed_display_pop_out_animation(\*\*kwargs)

This is the animation of the popping out of the mini-display that
shows the content of the zoomed camera.

* **Returns:**
  The Animation of the Zoomed Display popping out.
* **Return type:**
  [ApplyMethod](manim.animation.transform.ApplyMethod.md#manim.animation.transform.ApplyMethod)
* **Parameters:**
  **kwargs** (*Any*)

#### setup()

This method is used internally by Manim to
setup the scene for proper use.

* **Return type:**
  None
