# MappingCamera

Qualified name: `manim.camera.mapping\_camera.MappingCamera`

### *class* MappingCamera(mapping_func=<function MappingCamera.<lambda>>, min_num_curves=50, allow_object_intrusion=False, \*\*kwargs)

Bases: [`Camera`](manim.camera.camera.Camera.md#manim.camera.camera.Camera)

* **Parameters:**
  * **mapping_func** (*callable*) – Function to map 3D points to new 3D points (identity by default).
  * **min_num_curves** (*int*) – Minimum number of curves for VMobjects to avoid visual glitches.
  * **allow_object_intrusion** (*bool*) – If True, modifies original mobjects; else works on copies.
  * **kwargs** (*dict*) – Additional arguments passed to Camera base class.

### Methods

| [`capture_mobjects`](#manim.camera.mapping_camera.MappingCamera.capture_mobjects)   | Capture mobjects for rendering after applying the spatial mapping.   |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| `points_to_pixel_coords`                                                            |                                                                      |

### Attributes

| `background_color`   |    |
|----------------------|----|
| `background_opacity` |    |

#### capture_mobjects(mobjects, \*\*kwargs)

Capture mobjects for rendering after applying the spatial mapping.

Copies mobjects unless intrusion is allowed, and ensures
vector objects have enough curves for smooth distortion.
