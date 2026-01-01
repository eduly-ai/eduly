# MovingCameraScene

Qualified name: `manim.scene.moving\_camera\_scene.MovingCameraScene`

### *class* MovingCameraScene(camera_class=<class 'manim.camera.moving_camera.MovingCamera'>, \*\*kwargs)

Bases: [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene)

This is a Scene, with special configurations and properties that
make it suitable for cases where the camera must be moved around.

Note: Examples are included in the moving_camera_scene module
documentation, see below in the ‘see also’ section.

#### SEE ALSO
[`moving_camera_scene`](manim.scene.moving_camera_scene.md#module-manim.scene.moving_camera_scene)
[`MovingCamera`](manim.camera.moving_camera.MovingCamera.md#manim.camera.moving_camera.MovingCamera)

### Methods

| [`get_moving_mobjects`](#manim.scene.moving_camera_scene.MovingCameraScene.get_moving_mobjects)   | This method returns a list of all of the Mobjects in the Scene that are moving, that are also in the animations passed.   |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|

### Attributes

| `camera`   |                                        |
|------------|----------------------------------------|
| `time`     | The time since the start of the scene. |
* **Parameters:**
  * **camera_class** (*type* *[*[*Camera*](manim.camera.camera.Camera.md#manim.camera.camera.Camera) *]*)
  * **kwargs** (*Any*)

#### get_moving_mobjects(\*animations)

This method returns a list of all of the Mobjects in the Scene that
are moving, that are also in the animations passed.

* **Parameters:**
  **\*animations** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation)) – The Animations whose mobjects will be checked.
* **Return type:**
  list[[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)]
