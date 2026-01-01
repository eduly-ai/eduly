# ScreenRectangle

Qualified name: `manim.mobject.frame.ScreenRectangle`

### *class* ScreenRectangle(aspect_ratio=1.7777777777777777, height=4, \*\*kwargs)

Bases: [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.md#manim.mobject.geometry.polygram.Rectangle)

### Methods

### Attributes

| `animate`                                                           | Used to animate the application of any method of `self`.               |
|---------------------------------------------------------------------|------------------------------------------------------------------------|
| `animation_overrides`                                               |                                                                        |
| [`aspect_ratio`](#manim.mobject.frame.ScreenRectangle.aspect_ratio) | The aspect ratio.                                                      |
| `color`                                                             |                                                                        |
| `depth`                                                             | The depth of the mobject.                                              |
| `fill_color`                                                        | If there are multiple colors (for gradient) this returns the first one |
| `height`                                                            | The height of the mobject.                                             |
| `n_points_per_curve`                                                |                                                                        |
| `sheen_factor`                                                      |                                                                        |
| `stroke_color`                                                      |                                                                        |
| `width`                                                             | The width of the mobject.                                              |
* **Parameters:**
  * **aspect_ratio** (*float*)
  * **height** (*float*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(aspect_ratio=1.7777777777777777, height=4, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **aspect_ratio** (*float*)
  * **height** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### *property* aspect_ratio *: float*

The aspect ratio.

When set, the width is stretched to accommodate
the new aspect ratio.
