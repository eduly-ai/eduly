# LabeledLine

Qualified name: `manim.mobject.geometry.labeled.LabeledLine`

### *class* LabeledLine(label, label_position=0.5, label_config=None, box_config=None, frame_config=None, \*args, \*\*kwargs)

Bases: [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)

Constructs a line containing a label box somewhere along its length.

* **Parameters:**
  * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text)) – Label that will be displayed on the line.
  * **label_position** (*float*) – A ratio in the range [0-1] to indicate the position of the label with respect to the length of the line. Default value is 0.5.
  * **label_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – A dictionary containing the configuration for the label.
    This is only applied if `label` is of type `str`.
  * **box_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – A dictionary containing the configuration for the background box.
  * **frame_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – 

    A dictionary containing the configuration for the frame.

    #### SEE ALSO
    [`LabeledArrow`](manim.mobject.geometry.labeled.LabeledArrow.md#manim.mobject.geometry.labeled.LabeledArrow)
  * **args** (*Any*)
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

#### \_original_\_init_\_(label, label_position=0.5, label_config=None, box_config=None, frame_config=None, \*args, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text))
  * **label_position** (*float*)
  * **label_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **box_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **frame_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **args** (*Any*)
  * **kwargs** (*Any*)
* **Return type:**
  None
