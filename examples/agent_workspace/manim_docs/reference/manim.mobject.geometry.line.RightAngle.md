# RightAngle

Qualified name: `manim.mobject.geometry.line.RightAngle`

### *class* RightAngle(line1, line2, length=None, \*\*kwargs)

Bases: [`Angle`](manim.mobject.geometry.line.Angle.md#manim.mobject.geometry.line.Angle)

An elbow-type mobject representing a right angle between two lines.

* **Parameters:**
  * **line1** ([*Line*](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)) – The first line.
  * **line2** ([*Line*](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)) – The second line.
  * **length** (*float* *|* *None*) – The length of the arms.
  * **\*\*kwargs** (*Any*) – Further keyword arguments that are passed to the constructor of [`Angle`](manim.mobject.geometry.line.Angle.md#manim.mobject.geometry.line.Angle).

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

#### \_original_\_init_\_(line1, line2, length=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **line1** ([*Line*](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line))
  * **line2** ([*Line*](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line))
  * **length** (*float* *|* *None*)
  * **kwargs** (*Any*)
* **Return type:**
  None
