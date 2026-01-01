# SpecialThreeDScene

Qualified name: `manim.scene.three\_d\_scene.SpecialThreeDScene`

### *class* SpecialThreeDScene(cut_axes_at_radius=True, camera_config={'exponential_projection': True, 'should_apply_shading': True}, three_d_axes_config={'axis_config': {'numbers_with_elongated_ticks': [0, 1, 2], 'stroke_width': 2, 'tick_frequency': 1, 'unit_size': 2}, 'num_axis_pieces': 1}, sphere_config={'radius': 2, 'resolution': (24, 48)}, default_angled_camera_position={'phi': 1.2217304763960306, 'theta': -1.9198621771937625}, low_quality_config={'camera_config': {'should_apply_shading': False}, 'sphere_config': {'resolution': (12, 24)}, 'three_d_axes_config': {'num_axis_pieces': 1}}, \*\*kwargs)

Bases: [`ThreeDScene`](manim.scene.three_d_scene.ThreeDScene.md#manim.scene.three_d_scene.ThreeDScene)

An extension of [`ThreeDScene`](manim.scene.three_d_scene.ThreeDScene.md#manim.scene.three_d_scene.ThreeDScene) with more settings.

It has some extra configuration for axes, spheres,
and an override for low quality rendering. Further key differences
are:

* The camera shades applicable 3DMobjects by default,
  except if rendering in low quality.
* Some default params for Spheres and Axes have been added.

### Methods

| [`get_axes`](#manim.scene.three_d_scene.SpecialThreeDScene.get_axes)                                             | Return a set of 3D axes.                                          |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [`get_default_camera_position`](#manim.scene.three_d_scene.SpecialThreeDScene.get_default_camera_position)       | Returns the default_angled_camera position.                       |
| [`get_sphere`](#manim.scene.three_d_scene.SpecialThreeDScene.get_sphere)                                         | Returns a sphere with the passed keyword arguments as properties. |
| [`set_camera_to_default_position`](#manim.scene.three_d_scene.SpecialThreeDScene.set_camera_to_default_position) | Sets the camera to its default position.                          |

### Attributes

| `camera`   |                                        |
|------------|----------------------------------------|
| `time`     | The time since the start of the scene. |

#### get_axes()

Return a set of 3D axes.

* **Returns:**
  A set of 3D axes.
* **Return type:**
  [`ThreeDAxes`](manim.mobject.graphing.coordinate_systems.ThreeDAxes.md#manim.mobject.graphing.coordinate_systems.ThreeDAxes)

#### get_default_camera_position()

Returns the default_angled_camera position.

* **Returns:**
  Dictionary of phi, theta, focal_distance, and gamma.
* **Return type:**
  dict

#### get_sphere(\*\*kwargs)

Returns a sphere with the passed keyword arguments as properties.

* **Parameters:**
  **\*\*kwargs** – Any valid parameter of [`Sphere`](manim.mobject.three_d.three_dimensions.Sphere.md#manim.mobject.three_d.three_dimensions.Sphere) or [`Surface`](manim.mobject.three_d.three_dimensions.Surface.md#manim.mobject.three_d.three_dimensions.Surface).
* **Returns:**
  The sphere object.
* **Return type:**
  [`Sphere`](manim.mobject.three_d.three_dimensions.Sphere.md#manim.mobject.three_d.three_dimensions.Sphere)

#### set_camera_to_default_position()

Sets the camera to its default position.
