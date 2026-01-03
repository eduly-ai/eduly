# Arc

Qualified name: `manim.mobject.geometry.arc.Arc`

### *class* Arc(radius=1.0, start_angle=0, angle=1.5707963267948966, num_components=9, arc_center=array([0., 0., 0.]), \*\*kwargs)

Bases: [`TipableVMobject`](manim.mobject.geometry.arc.TipableVMobject.md#manim.mobject.geometry.arc.TipableVMobject)

A circular arc.

### Examples

A simple arc of angle Pi.

### Methods

| [`generate_points`](#manim.mobject.geometry.arc.Arc.generate_points)   | Initializes `points` and therefore the shape.                                      |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [`get_arc_center`](#manim.mobject.geometry.arc.Arc.get_arc_center)     | Looks at the normals to the first two anchors, and finds their intersection points |
| `init_points`                                                          |                                                                                    |
| `move_arc_center_to`                                                   |                                                                                    |
| `stop_angle`                                                           |                                                                                    |

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
* **Parameters:**
  * **radius** (*float* *|* *None*)
  * **start_angle** (*float*)
  * **angle** (*float*)
  * **num_components** (*int*)
  * **arc_center** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **kwargs** (*Any*)

#### \_original_\_init_\_(radius=1.0, start_angle=0, angle=1.5707963267948966, num_components=9, arc_center=array([0., 0., 0.]), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **radius** (*float* *|* *None*)
  * **start_angle** (*float*)
  * **angle** (*float*)
  * **num_components** (*int*)
  * **arc_center** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **kwargs** (*Any*)

#### generate_points()

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  None

#### get_arc_center(warning=True)

Looks at the normals to the first two
anchors, and finds their intersection points

* **Parameters:**
  **warning** (*bool*)
* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)
