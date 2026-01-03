# BraceBetweenPoints

Qualified name: `manim.mobject.svg.brace.BraceBetweenPoints`

### *class* BraceBetweenPoints(point_1, point_2, direction=array([0., 0., 0.]), \*\*kwargs)

Bases: [`Brace`](manim.mobject.svg.brace.Brace.md#manim.mobject.svg.brace.Brace)

Similar to Brace, but instead of taking a mobject it uses 2
points to place the brace.

A fitting direction for the brace is
computed, but it still can be manually overridden.
If the points go from left to right, the brace is drawn from below.
Swapping the points places the brace on the opposite side.

* **Parameters:**
  * **point_1** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The first point.
  * **point_2** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The second point.
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The direction from which the brace faces towards the points.
  * **kwargs** (*Any*)

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

#### \_original_\_init_\_(point_1, point_2, direction=array([0., 0., 0.]), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **point_1** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **point_2** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **kwargs** (*Any*)
