# Star

Qualified name: `manim.mobject.geometry.polygram.Star`

### *class* Star(n=5, \*, outer_radius=1, inner_radius=None, density=2, start_angle=1.5707963267948966, \*\*kwargs)

Bases: [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon)

A regular polygram without the intersecting lines.

* **Parameters:**
  * **n** (*int*) – How many points on the [`Star`](#manim.mobject.geometry.polygram.Star).
  * **outer_radius** (*float*) – The radius of the circle that the outer vertices are placed on.
  * **inner_radius** (*float* *|* *None*) – 

    The radius of the circle that the inner vertices are placed on.

    If unspecified, the inner radius will be
    calculated such that the edges of the [`Star`](#manim.mobject.geometry.polygram.Star)
    perfectly follow the edges of its [`RegularPolygram`](manim.mobject.geometry.polygram.RegularPolygram.md#manim.mobject.geometry.polygram.RegularPolygram)
    counterpart.
  * **density** (*int*) – 

    The density of the [`Star`](#manim.mobject.geometry.polygram.Star). Only used if
    `inner_radius` is unspecified.

    See [`RegularPolygram`](manim.mobject.geometry.polygram.RegularPolygram.md#manim.mobject.geometry.polygram.RegularPolygram) for more information.
  * **start_angle** (*float* *|* *None*) – The angle the vertices start at; the rotation of
    the [`Star`](#manim.mobject.geometry.polygram.Star).
  * **kwargs** (*Any*) – Forwardeds to the parent constructor.
* **Raises:**
  **ValueError** – If `inner_radius` is unspecified and `density`
      is not in the range `[1, n/2)`.

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

#### \_original_\_init_\_(n=5, \*, outer_radius=1, inner_radius=None, density=2, start_angle=1.5707963267948966, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **n** (*int*)
  * **outer_radius** (*float*)
  * **inner_radius** (*float* *|* *None*)
  * **density** (*int*)
  * **start_angle** (*float* *|* *None*)
  * **kwargs** (*Any*)
* **Return type:**
  None
