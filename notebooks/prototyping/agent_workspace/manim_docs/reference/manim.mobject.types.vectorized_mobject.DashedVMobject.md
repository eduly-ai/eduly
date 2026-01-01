# DashedVMobject

Qualified name: `manim.mobject.types.vectorized\_mobject.DashedVMobject`

### *class* DashedVMobject(vmobject, num_dashes=15, dashed_ratio=0.5, dash_offset=0, color=ManimColor('#FFFFFF'), equal_lengths=True, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) composed of dashes instead of lines.

* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The object that will get dashed
  * **num_dashes** (*int*) – Number of dashes to add.
  * **dashed_ratio** (*float*) – Ratio of dash to empty space.
  * **dash_offset** (*float*) – Shifts the starting point of dashes along the
    path. Value 1 shifts by one full dash length.
  * **equal_lengths** (*bool*) – If `True`, dashes will be (approximately) equally long.
    If `False`, dashes will be split evenly in the curve’s
    input t variable (legacy behavior).
  * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor))

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

#### \_original_\_init_\_(vmobject, num_dashes=15, dashed_ratio=0.5, dash_offset=0, color=ManimColor('#FFFFFF'), equal_lengths=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
  * **num_dashes** (*int*)
  * **dashed_ratio** (*float*)
  * **dash_offset** (*float*)
  * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor))
  * **equal_lengths** (*bool*)
* **Return type:**
  None
