# Arrow3D

Qualified name: `manim.mobject.three\_d.three\_dimensions.Arrow3D`

### *class* Arrow3D(start=array([-1., 0., 0.]), end=array([1., 0., 0.]), thickness=0.02, height=0.3, base_radius=0.08, color=ManimColor('#FFFFFF'), resolution=24, \*\*kwargs)

Bases: [`Line3D`](manim.mobject.three_d.three_dimensions.Line3D.md#manim.mobject.three_d.three_dimensions.Line3D)

An arrow made out of a cylindrical line and a conical tip.

* **Parameters:**
  * **start** (*np.ndarray*) – The start position of the arrow.
  * **end** (*np.ndarray*) – The end position of the arrow.
  * **thickness** (*float*) – The thickness of the arrow.
  * **height** (*float*) – The height of the conical tip.
  * **base_radius** (*float*) – The base radius of the conical tip.
  * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)) – The color of the arrow.
  * **resolution** (*int* *|* *Sequence* *[**int* *]*) – The resolution of the arrow line.

### Examples

### Methods

| [`get_end`](#manim.mobject.three_d.three_dimensions.Arrow3D.get_end)   | Returns the ending point of the [`Line3D`](manim.mobject.three_d.three_dimensions.Line3D.md#manim.mobject.three_d.three_dimensions.Line3D).   |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|

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

#### \_original_\_init_\_(start=array([-1., 0., 0.]), end=array([1., 0., 0.]), thickness=0.02, height=0.3, base_radius=0.08, color=ManimColor('#FFFFFF'), resolution=24, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **start** (*ndarray*)
  * **end** (*ndarray*)
  * **thickness** (*float*)
  * **height** (*float*)
  * **base_radius** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **resolution** (*int* *|* *Sequence* *[**int* *]*)
* **Return type:**
  None

#### get_end()

Returns the ending point of the [`Line3D`](manim.mobject.three_d.three_dimensions.Line3D.md#manim.mobject.three_d.three_dimensions.Line3D).

* **Returns:**
  **end** – Ending point of the [`Line3D`](manim.mobject.three_d.three_dimensions.Line3D.md#manim.mobject.three_d.three_dimensions.Line3D).
* **Return type:**
  `numpy.array`
