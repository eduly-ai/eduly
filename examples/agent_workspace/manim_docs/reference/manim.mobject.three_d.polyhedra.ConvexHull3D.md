# ConvexHull3D

Qualified name: `manim.mobject.three\_d.polyhedra.ConvexHull3D`

### *class* ConvexHull3D(\*points, tolerance=1e-05, \*\*kwargs)

Bases: [`Polyhedron`](manim.mobject.three_d.polyhedra.Polyhedron.md#manim.mobject.three_d.polyhedra.Polyhedron)

A convex hull for a set of points

* **Parameters:**
  * **points** ([*Point3D*](manim.typing.md#manim.typing.Point3D)) – The points to consider.
  * **tolerance** (*float*) – The tolerance used for quickhull.
  * **kwargs** (*Any*) – Forwarded to the parent constructor.

### Examples

### Methods

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

#### \_original_\_init_\_(\*points, tolerance=1e-05, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **points** ([*Point3D*](manim.typing.md#manim.typing.Point3D))
  * **tolerance** (*float*)
  * **kwargs** (*Any*)
