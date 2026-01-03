# Point

Qualified name: `manim.mobject.types.point\_cloud\_mobject.Point`

### *class* Point(location=array([0., 0., 0.]), color=ManimColor('#000000'), \*\*kwargs)

Bases: [`PMobject`](manim.mobject.types.point_cloud_mobject.PMobject.md#manim.mobject.types.point_cloud_mobject.PMobject)

A mobject representing a point.

### Examples

### Methods

| [`generate_points`](#manim.mobject.types.point_cloud_mobject.Point.generate_points)   | Initializes `points` and therefore the shape.   |
|---------------------------------------------------------------------------------------|-------------------------------------------------|
| `init_points`                                                                         |                                                 |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.   |
|-----------------------|------------------------------------------------------------|
| `animation_overrides` |                                                            |
| `depth`               | The depth of the mobject.                                  |
| `height`              | The height of the mobject.                                 |
| `width`               | The width of the mobject.                                  |
* **Parameters:**
  * **location** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor))
  * **kwargs** (*Any*)

#### \_original_\_init_\_(location=array([0., 0., 0.]), color=ManimColor('#000000'), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **location** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor))
  * **kwargs** (*Any*)
* **Return type:**
  None

#### generate_points()

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  None
