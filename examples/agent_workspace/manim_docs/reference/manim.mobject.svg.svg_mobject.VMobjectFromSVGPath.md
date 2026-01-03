# VMobjectFromSVGPath

Qualified name: `manim.mobject.svg.svg\_mobject.VMobjectFromSVGPath`

### *class* VMobjectFromSVGPath(path_obj, long_lines=False, should_subdivide_sharp_curves=False, should_remove_null_curves=False, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A vectorized mobject representing an SVG path.

#### NOTE
The `long_lines`, `should_subdivide_sharp_curves`,
and `should_remove_null_curves` keyword arguments are
only respected with the OpenGL renderer.

* **Parameters:**
  * **path_obj** (*se.Path*) – A parsed SVG path object.
  * **long_lines** (*bool*) – Whether or not straight lines in the vectorized mobject
    are drawn in one or two segments.
  * **should_subdivide_sharp_curves** (*bool*) – Whether or not to subdivide subcurves further in case
    two segments meet at an angle that is sharper than a
    given threshold.
  * **should_remove_null_curves** (*bool*) – Whether or not to remove subcurves of length 0.
  * **kwargs** (*Any*) – Further keyword arguments are passed to the parent
    class.

### Methods

| [`generate_points`](#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.generate_points)   | Initializes `points` and therefore the shape.   |
|-------------------------------------------------------------------------------------------|-------------------------------------------------|
| `handle_commands`                                                                         |                                                 |
| `init_points`                                                                             |                                                 |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.               |
|-----------------------|------------------------------------------------------------------------|
| `animation_overrides` |                                                                        |
| `color`               |                                                                        |
| `depth`               | The depth of the mobject.                                              |
| `fill_color`          | If there are multiple colors (for gradient) this returns the first one |
| `height`              | The height of the mobject.                                             |
| `n_points_per_curve`  |                                                                        |
| `sheen_factor`        |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |

#### \_original_\_init_\_(path_obj, long_lines=False, should_subdivide_sharp_curves=False, should_remove_null_curves=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **path_obj** (*Path*)
  * **long_lines** (*bool*)
  * **should_subdivide_sharp_curves** (*bool*)
  * **should_remove_null_curves** (*bool*)
  * **kwargs** (*Any*)

#### generate_points()

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  None
