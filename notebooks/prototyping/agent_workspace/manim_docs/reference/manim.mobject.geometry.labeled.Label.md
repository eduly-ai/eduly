# Label

Qualified name: `manim.mobject.geometry.labeled.Label`

### *class* Label(label, label_config=None, box_config=None, frame_config=None, \*\*kwargs)

Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

A Label consisting of text surrounded by a frame.

* **Parameters:**
  * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text)) – Label that will be displayed.
  * **label_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – A dictionary containing the configuration for the label.
    This is only applied if `label` is of type `str`.
  * **box_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – A dictionary containing the configuration for the background box.
  * **frame_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – A dictionary containing the configuration for the frame.
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

#### \_original_\_init_\_(label, label_config=None, box_config=None, frame_config=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text))
  * **label_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **box_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **frame_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **kwargs** (*Any*)
* **Return type:**
  None
