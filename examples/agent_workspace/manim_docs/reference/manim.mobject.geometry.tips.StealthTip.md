# StealthTip

Qualified name: `manim.mobject.geometry.tips.StealthTip`

### *class* StealthTip(fill_opacity=1, stroke_width=3, length=0.175, start_angle=3.141592653589793, \*\*kwargs)

Bases: [`ArrowTip`](manim.mobject.geometry.tips.ArrowTip.md#manim.mobject.geometry.tips.ArrowTip)

‘Stealth’ fighter / kite arrow shape.

Naming is inspired by the corresponding
[TikZ arrow shape](https://tikz.dev/tikz-arrows#sec-16.3).

### Methods

### Attributes

| `animate`                                                  | Used to animate the application of any method of `self`.               |
|------------------------------------------------------------|------------------------------------------------------------------------|
| `animation_overrides`                                      |                                                                        |
| `base`                                                     | The base point of the arrow tip.                                       |
| `color`                                                    |                                                                        |
| `depth`                                                    | The depth of the mobject.                                              |
| `fill_color`                                               | If there are multiple colors (for gradient) this returns the first one |
| `height`                                                   | The height of the mobject.                                             |
| [`length`](#manim.mobject.geometry.tips.StealthTip.length) | The length of the arrow tip.                                           |
| `n_points_per_curve`                                       |                                                                        |
| `sheen_factor`                                             |                                                                        |
| `stroke_color`                                             |                                                                        |
| `tip_angle`                                                | The angle of the arrow tip.                                            |
| `tip_point`                                                | The tip point of the arrow tip.                                        |
| `vector`                                                   | The vector pointing from the base point to the tip point.              |
| `width`                                                    | The width of the mobject.                                              |
* **Parameters:**
  * **fill_opacity** (*float*)
  * **stroke_width** (*float*)
  * **length** (*float*)
  * **start_angle** (*float*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(fill_opacity=1, stroke_width=3, length=0.175, start_angle=3.141592653589793, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **fill_opacity** (*float*)
  * **stroke_width** (*float*)
  * **length** (*float*)
  * **start_angle** (*float*)
  * **kwargs** (*Any*)

#### *property* length *: float*

The length of the arrow tip.

In this case, the length is computed as the height of
the triangle encompassing the stealth tip (otherwise,
the tip is scaled too large).
