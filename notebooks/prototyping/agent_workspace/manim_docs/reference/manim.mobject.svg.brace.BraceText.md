# BraceText

Qualified name: `manim.mobject.svg.brace.BraceText`

### *class* BraceText(obj, text, label_constructor=<class 'manim.mobject.text.text_mobject.Text'>, \*\*kwargs)

Bases: [`BraceLabel`](manim.mobject.svg.brace.BraceLabel.md#manim.mobject.svg.brace.BraceLabel)

Create a brace with a text label attached.

* **Parameters:**
  * **obj** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject adjacent to which the brace is placed.
  * **text** (*str*) – The label text.
  * **brace_direction** – The direction of the brace. By default `DOWN`.
  * **label_constructor** (*type* *[*[*SingleStringMathTex*](manim.mobject.text.tex_mobject.SingleStringMathTex.md#manim.mobject.text.tex_mobject.SingleStringMathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) *]*) – A class or function used to construct a mobject representing
    the label. By default [`Text`](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text).
  * **font_size** – The font size of the label, passed to the `label_constructor`.
  * **buff** – The buffer between the mobject and the brace.
  * **brace_config** – Arguments to be passed to [`Brace`](manim.mobject.svg.brace.Brace.md#manim.mobject.svg.brace.Brace).
  * **kwargs** (*Any*) – Additional arguments to be passed to [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).

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

#### \_original_\_init_\_(obj, text, label_constructor=<class 'manim.mobject.text.text_mobject.Text'>, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **obj** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **text** (*str*)
  * **label_constructor** (*type* *[*[*SingleStringMathTex*](manim.mobject.text.tex_mobject.SingleStringMathTex.md#manim.mobject.text.tex_mobject.SingleStringMathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) *]*)
  * **kwargs** (*Any*)
