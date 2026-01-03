# LabeledDot

Qualified name: `manim.mobject.geometry.arc.LabeledDot`

### *class* LabeledDot(label, radius=None, buff=0.1, \*\*kwargs)

Bases: [`Dot`](manim.mobject.geometry.arc.Dot.md#manim.mobject.geometry.arc.Dot)

A [`Dot`](manim.mobject.geometry.arc.Dot.md#manim.mobject.geometry.arc.Dot) containing a label in its center.

* **Parameters:**
  * **label** (*str* *|* [*SingleStringMathTex*](manim.mobject.text.tex_mobject.SingleStringMathTex.md#manim.mobject.text.tex_mobject.SingleStringMathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex)) – The label of the [`Dot`](manim.mobject.geometry.arc.Dot.md#manim.mobject.geometry.arc.Dot). This is rendered as [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex)
    by default (i.e., when passing a `str`), but other classes
    representing rendered strings like [`Text`](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) or [`Tex`](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex)
    can be passed as well.
  * **radius** (*float* *|* *None*) – The radius of the [`Dot`](manim.mobject.geometry.arc.Dot.md#manim.mobject.geometry.arc.Dot). If provided, the `buff` is ignored.
    If `None` (the default), the radius is calculated based on the size
    of the `label` and the `buff`.
  * **buff** (*float*)
  * **kwargs** (*Any*)

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

#### \_original_\_init_\_(label, radius=None, buff=0.1, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **label** (*str* *|* [*SingleStringMathTex*](manim.mobject.text.tex_mobject.SingleStringMathTex.md#manim.mobject.text.tex_mobject.SingleStringMathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex))
  * **radius** (*float* *|* *None*)
  * **buff** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None
