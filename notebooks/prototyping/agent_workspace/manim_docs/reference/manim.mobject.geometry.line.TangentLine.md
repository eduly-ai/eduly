# TangentLine

Qualified name: `manim.mobject.geometry.line.TangentLine`

### *class* TangentLine(vmob, alpha, length=1, d_alpha=1e-06, \*\*kwargs)

Bases: [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)

Constructs a line tangent to a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) at a specific point.

* **Parameters:**
  * **vmob** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The VMobject on which the tangent line is drawn.
  * **alpha** (*float*) – How far along the shape that the line will be constructed. range: 0-1.
  * **length** (*float*) – Length of the tangent line.
  * **d_alpha** (*float*) – The `dx` value
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)

#### SEE ALSO
[`point_from_proportion()`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion)

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

#### \_original_\_init_\_(vmob, alpha, length=1, d_alpha=1e-06, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vmob** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
  * **alpha** (*float*)
  * **length** (*float*)
  * **d_alpha** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None
