# ImageMobjectFromCamera

Qualified name: `manim.mobject.types.image\_mobject.ImageMobjectFromCamera`

### *class* ImageMobjectFromCamera(camera, default_display_frame_config=None, \*\*kwargs)

Bases: [`AbstractImageMobject`](manim.mobject.types.image_mobject.AbstractImageMobject.md#manim.mobject.types.image_mobject.AbstractImageMobject)

### Methods

| `add_display_frame`   |    |
|-----------------------|----|
| `get_pixel_array`     |    |
| `interpolate_color`   |    |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.   |
|-----------------------|------------------------------------------------------------|
| `animation_overrides` |                                                            |
| `depth`               | The depth of the mobject.                                  |
| `height`              | The height of the mobject.                                 |
| `width`               | The width of the mobject.                                  |
* **Parameters:**
  * **camera** ([*MovingCamera*](manim.camera.moving_camera.MovingCamera.md#manim.camera.moving_camera.MovingCamera))
  * **default_display_frame_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(camera, default_display_frame_config=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **camera** ([*MovingCamera*](manim.camera.moving_camera.MovingCamera.md#manim.camera.moving_camera.MovingCamera))
  * **default_display_frame_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **kwargs** (*Any*)
* **Return type:**
  None
