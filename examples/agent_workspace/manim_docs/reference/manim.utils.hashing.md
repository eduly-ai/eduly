# hashing

Utilities for scene caching.

### Functions

### get_hash_from_play_call(scene_object, camera_object, animations_list, current_mobjects_list)

Take the list of animations and a list of mobjects and output their hashes. This is meant to be used for scene.play function.

* **Parameters:**
  * **scene_object** ([*Scene*](manim.scene.scene.Scene.md#manim.scene.scene.Scene)) – The scene object.
  * **camera_object** ([*Camera*](manim.camera.camera.Camera.md#manim.camera.camera.Camera) *|* *OpenGLCamera*) – The camera object used in the scene.
  * **animations_list** (*Iterable* *[*[*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – The list of animations.
  * **current_mobjects_list** (*Iterable* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The list of mobjects.
* **Returns:**
  A string concatenation of the respective hashes of camera_object, animations_list and current_mobjects_list, separated by \_.
* **Return type:**
  `str`

### get_json(obj)

Recursively serialize object to JSON using the `CustomEncoder` class.

* **Parameters:**
  **obj** (*Any*) – The dict to flatten
* **Returns:**
  The flattened object
* **Return type:**
  `str`
