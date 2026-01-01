# Line

Qualified name: `manim.mobject.geometry.line.Line`

### *class* Line(start=array([-1., 0., 0.]), end=array([1., 0., 0.]), buff=0, path_arc=0, \*\*kwargs)

Bases: [`TipableVMobject`](manim.mobject.geometry.arc.TipableVMobject.md#manim.mobject.geometry.arc.TipableVMobject)

A straight or curved line segment between two points or mobjects.

* **Parameters:**
  * **start** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The starting point or Mobject of the line.
  * **end** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The ending point or Mobject of the line.
  * **buff** (*float*) – The distance to shorten the line from both ends.
  * **path_arc** (*float*) – If nonzero, the line will be curved into an arc with this angle (in radians).
  * **kwargs** (*Any*) – Additional arguments to be passed to `TipableVMobject`

### Examples

### Methods

| [`generate_points`](#manim.mobject.geometry.line.Line.generate_points)           | Initializes `points` and therefore the shape.                  |
|----------------------------------------------------------------------------------|----------------------------------------------------------------|
| `get_angle`                                                                      |                                                                |
| [`get_projection`](#manim.mobject.geometry.line.Line.get_projection)             | Returns the projection of a point onto a line.                 |
| `get_slope`                                                                      |                                                                |
| `get_unit_vector`                                                                |                                                                |
| `get_vector`                                                                     |                                                                |
| `init_points`                                                                    |                                                                |
| [`put_start_and_end_on`](#manim.mobject.geometry.line.Line.put_start_and_end_on) | Sets starts and end coordinates of a line.                     |
| `set_angle`                                                                      |                                                                |
| `set_length`                                                                     |                                                                |
| `set_path_arc`                                                                   |                                                                |
| [`set_points_by_ends`](#manim.mobject.geometry.line.Line.set_points_by_ends)     | Sets the points of the line based on its start and end points. |

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

#### \_original_\_init_\_(start=array([-1., 0., 0.]), end=array([1., 0., 0.]), buff=0, path_arc=0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **start** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **end** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **buff** (*float*)
  * **path_arc** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### \_pointify(mob_or_point, direction=None)

Transforms a mobject into its corresponding point. Does nothing if a point is passed.

`direction` determines the location of the point along its bounding box in that direction.

* **Parameters:**
  * **mob_or_point** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* [*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The mobject or point.
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike) *|* *None*) – The direction.
* **Return type:**
  [Point3D](manim.typing.md#manim.typing.Point3D)

#### generate_points()

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  None

#### get_projection(point)

Returns the projection of a point onto a line.

* **Parameters:**
  **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The point to which the line is projected.
* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### put_start_and_end_on(start, end)

Sets starts and end coordinates of a line.

### Examples

* **Parameters:**
  * **start** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **end** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
* **Return type:**
  Self

#### set_points_by_ends(start, end, buff=0, path_arc=0)

Sets the points of the line based on its start and end points.
Unlike [`put_start_and_end_on()`](#manim.mobject.geometry.line.Line.put_start_and_end_on), this method respects self.buff and
Mobject bounding boxes.

* **Parameters:**
  * **start** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The start point or Mobject of the line.
  * **end** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The end point or Mobject of the line.
  * **buff** (*float*) – The empty space between the start and end of the line, by default 0.
  * **path_arc** (*float*) – The angle of a circle spanned by this arc, by default 0 which is a straight line.
* **Return type:**
  None
