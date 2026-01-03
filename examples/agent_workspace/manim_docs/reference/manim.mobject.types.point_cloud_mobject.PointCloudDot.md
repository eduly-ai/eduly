# PointCloudDot

Qualified name: `manim.mobject.types.point\_cloud\_mobject.PointCloudDot`

### *class* PointCloudDot(center=array([0., 0., 0.]), radius=2.0, stroke_width=2, density=10, color=ManimColor('#FFFF00'), \*\*kwargs)

Bases: [`Mobject1D`](manim.mobject.types.point_cloud_mobject.Mobject1D.md#manim.mobject.types.point_cloud_mobject.Mobject1D)

A disc made of a cloud of dots.

### Examples

### Methods

| [`generate_points`](#manim.mobject.types.point_cloud_mobject.PointCloudDot.generate_points)   | Initializes `points` and therefore the shape.   |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------|
| `init_points`                                                                                 |                                                 |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.   |
|-----------------------|------------------------------------------------------------|
| `animation_overrides` |                                                            |
| `depth`               | The depth of the mobject.                                  |
| `height`              | The height of the mobject.                                 |
| `width`               | The width of the mobject.                                  |
* **Parameters:**
  * **center** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **radius** (*float*)
  * **stroke_width** (*int*)
  * **density** (*int*)
  * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor))
  * **kwargs** (*Any*)

#### \_original_\_init_\_(center=array([0., 0., 0.]), radius=2.0, stroke_width=2, density=10, color=ManimColor('#FFFF00'), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **center** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **radius** (*float*)
  * **stroke_width** (*int*)
  * **density** (*int*)
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
