# Circle

Qualified name: `manim.mobject.geometry.arc.Circle`

### *class* Circle(radius=None, color=ManimColor('#FC6255'), \*\*kwargs)

Bases: [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc)

A circle.

* **Parameters:**
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the shape.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc)
  * **radius** (*float* *|* *None*)

### Examples

### Methods

| [`from_three_points`](#manim.mobject.geometry.arc.Circle.from_three_points)   | Returns a circle passing through the specified three points.   |
|-------------------------------------------------------------------------------|----------------------------------------------------------------|
| [`point_at_angle`](#manim.mobject.geometry.arc.Circle.point_at_angle)         | Returns the position of a point on the circle.                 |
| [`surround`](#manim.mobject.geometry.arc.Circle.surround)                     | Modifies a circle so that it surrounds a given mobject.        |

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

#### \_original_\_init_\_(radius=None, color=ManimColor('#FC6255'), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **radius** (*float* *|* *None*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **kwargs** (*Any*)
* **Return type:**
  None

#### *static* from_three_points(p1, p2, p3, \*\*kwargs)

Returns a circle passing through the specified
three points.

### Example

* **Parameters:**
  * **p1** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **p2** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **p3** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **kwargs** (*Any*)
* **Return type:**
  [*Circle*](#manim.mobject.geometry.arc.Circle)

#### point_at_angle(angle)

Returns the position of a point on the circle.

* **Parameters:**
  **angle** (*float*) – The angle of the point along the circle in radians.
* **Returns:**
  The location of the point along the circle’s circumference.
* **Return type:**
  `numpy.ndarray`

### Examples

#### surround(mobject, dim_to_match=0, stretch=False, buffer_factor=1.2)

Modifies a circle so that it surrounds a given mobject.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject that the circle will be surrounding.
  * **dim_to_match** (*int*)
  * **buffer_factor** (*float*) – Scales the circle with respect to the mobject. A buffer_factor < 1 makes the circle smaller than the mobject.
  * **stretch** (*bool*) – Stretches the circle to fit more tightly around the mobject. Note: Does not work with `Line`
* **Return type:**
  Self

### Examples
