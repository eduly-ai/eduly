# Arrow

Qualified name: `manim.mobject.geometry.line.Arrow`

### *class* Arrow(\*args, stroke_width=6, buff=0.25, max_tip_length_to_length_ratio=0.25, max_stroke_width_to_length_ratio=5, \*\*kwargs)

Bases: [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)

An arrow.

* **Parameters:**
  * **args** (*Any*) – Arguments to be passed to [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line).
  * **stroke_width** (*float*) – The thickness of the arrow. Influenced by `max_stroke_width_to_length_ratio`.
  * **buff** (*float*) – The distance of the arrow from its start and end points.
  * **max_tip_length_to_length_ratio** (*float*) – `tip_length` scales with the length of the arrow. Increasing this ratio raises the max value of `tip_length`.
  * **max_stroke_width_to_length_ratio** (*float*) – `stroke_width` scales with the length of the arrow. Increasing this ratio ratios the max value of `stroke_width`.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line).

#### SEE ALSO
`ArrowTip`
`CurvedArrow`

### Examples

### Methods

| [`get_default_tip_length`](#manim.mobject.geometry.line.Arrow.get_default_tip_length)   | Returns the default tip_length of the arrow.                    |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| [`get_normal_vector`](#manim.mobject.geometry.line.Arrow.get_normal_vector)             | Returns the normal of a vector.                                 |
| [`reset_normal_vector`](#manim.mobject.geometry.line.Arrow.reset_normal_vector)         | Resets the normal of a vector                                   |
| [`scale`](#manim.mobject.geometry.line.Arrow.scale)                                     | Scale an arrow, but keep stroke width and arrow tip size fixed. |

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

#### \_original_\_init_\_(\*args, stroke_width=6, buff=0.25, max_tip_length_to_length_ratio=0.25, max_stroke_width_to_length_ratio=5, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **args** (*Any*)
  * **stroke_width** (*float*)
  * **buff** (*float*)
  * **max_tip_length_to_length_ratio** (*float*)
  * **max_stroke_width_to_length_ratio** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### \_set_stroke_width_from_length()

Sets stroke width based on length.

* **Return type:**
  Self

#### get_default_tip_length()

Returns the default tip_length of the arrow.

### Examples

```default
>>> Arrow().get_default_tip_length()
0.35
```

* **Return type:**
  float

#### get_normal_vector()

Returns the normal of a vector.

### Examples

```default
>>> np.round(Arrow().get_normal_vector()) + 0. # add 0. to avoid negative 0 in output
array([ 0.,  0., -1.])
```

* **Return type:**
  [*Vector3D*](manim.typing.md#manim.typing.Vector3D)

#### reset_normal_vector()

Resets the normal of a vector

* **Return type:**
  Self

#### scale(factor, scale_tips=False, \*\*kwargs)

Scale an arrow, but keep stroke width and arrow tip size fixed.

#### SEE ALSO
[`scale()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.scale)

### Examples

```default
>>> arrow = Arrow(np.array([-1, -1, 0]), np.array([1, 1, 0]), buff=0)
>>> scaled_arrow = arrow.scale(2)
>>> np.round(scaled_arrow.get_start_and_end(), 8) + 0
array([[-2., -2.,  0.],
       [ 2.,  2.,  0.]])
>>> arrow.tip.length == scaled_arrow.tip.length
True
```

Manually scaling the object using the default method
[`scale()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.scale) does not have the same properties:

```default
>>> new_arrow = Arrow(np.array([-1, -1, 0]), np.array([1, 1, 0]), buff=0)
>>> another_scaled_arrow = VMobject.scale(new_arrow, 2)
>>> another_scaled_arrow.tip.length == arrow.tip.length
False
```

* **Parameters:**
  * **factor** (*float*)
  * **scale_tips** (*bool*)
  * **kwargs** (*Any*)
* **Return type:**
  Self
