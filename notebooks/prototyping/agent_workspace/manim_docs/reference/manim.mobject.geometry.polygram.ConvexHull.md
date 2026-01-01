# ConvexHull

Qualified name: `manim.mobject.geometry.polygram.ConvexHull`

### *class* ConvexHull(\*points, tolerance=1e-05, \*\*kwargs)

Bases: [`Polygram`](manim.mobject.geometry.polygram.Polygram.md#manim.mobject.geometry.polygram.Polygram)

Constructs a convex hull for a set of points in no particular order.

* **Parameters:**
  * **points** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The points to consider.
  * **tolerance** (*float*) – The tolerance used by quickhull.
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
  * **points** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **tolerance** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None
