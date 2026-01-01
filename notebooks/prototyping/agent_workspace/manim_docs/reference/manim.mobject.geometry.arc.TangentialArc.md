# TangentialArc

Qualified name: `manim.mobject.geometry.arc.TangentialArc`

### *class* TangentialArc(line1, line2, radius, corner=(1, 1), \*\*kwargs)

Bases: [`ArcBetweenPoints`](manim.mobject.geometry.arc.ArcBetweenPoints.md#manim.mobject.geometry.arc.ArcBetweenPoints)

Construct an arc that is tangent to two intersecting lines.
You can choose any of the 4 possible corner arcs via the corner tuple.
corner = (s1, s2) where each si is ±1 to control direction along each line.

> Example
> class TangentialArcExample(Scene):
> : def construct(self):
>   : line1 = DashedLine(start=3 \* LEFT, end=3 \* RIGHT)
>     line1.rotate(angle=31 \* DEGREES, about_point=ORIGIN)
>     line2 = DashedLine(start=3 \* UP, end=3 \* DOWN)
>     line2.rotate(angle=12 \* DEGREES, about_point=ORIGIN)
>     <br/>
>     arc = TangentialArc(line1, line2, radius=2.25, corner=(1, 1), color=TEAL)
>     self.add(arc, line1, line2)

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
* **Parameters:**
  * **line1** ([*Line*](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line))
  * **line2** ([*Line*](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line))
  * **radius** (*float*)
  * **corner** (*Any*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(line1, line2, radius, corner=(1, 1), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **line1** ([*Line*](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line))
  * **line2** ([*Line*](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line))
  * **radius** (*float*)
  * **corner** (*Any*)
  * **kwargs** (*Any*)
