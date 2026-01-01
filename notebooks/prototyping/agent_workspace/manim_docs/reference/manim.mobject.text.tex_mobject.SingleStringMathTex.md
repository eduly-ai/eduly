# SingleStringMathTex

Qualified name: `manim.mobject.text.tex\_mobject.SingleStringMathTex`

### *class* SingleStringMathTex(tex_string, stroke_width=0, should_center=True, height=None, organize_left_to_right=False, tex_environment='align\*', tex_template=None, font_size=48, color=None, \*\*kwargs)

Bases: [`SVGMobject`](manim.mobject.svg.svg_mobject.SVGMobject.md#manim.mobject.svg.svg_mobject.SVGMobject)

Elementary building block for rendering text with LaTeX.

### Tests

Check that creating a [`SingleStringMathTex`](#manim.mobject.text.tex_mobject.SingleStringMathTex) object works:

```default
>>> SingleStringMathTex('Test') 
SingleStringMathTex('Test')
```

### Methods

| `get_tex_string`                                                                 |                         |
|----------------------------------------------------------------------------------|-------------------------|
| [`init_colors`](#manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors) | Initializes the colors. |

### Attributes

| `animate`                                                                    | Used to animate the application of any method of `self`.               |
|------------------------------------------------------------------------------|------------------------------------------------------------------------|
| `animation_overrides`                                                        |                                                                        |
| `color`                                                                      |                                                                        |
| `depth`                                                                      | The depth of the mobject.                                              |
| `fill_color`                                                                 | If there are multiple colors (for gradient) this returns the first one |
| [`font_size`](#manim.mobject.text.tex_mobject.SingleStringMathTex.font_size) | The font size of the tex mobject.                                      |
| `hash_seed`                                                                  | A unique hash representing the result of the generated mobject points. |
| `height`                                                                     | The height of the mobject.                                             |
| `n_points_per_curve`                                                         |                                                                        |
| `sheen_factor`                                                               |                                                                        |
| `stroke_color`                                                               |                                                                        |
| `width`                                                                      | The width of the mobject.                                              |
* **Parameters:**
  * **tex_string** (*str*)
  * **stroke_width** (*float*)
  * **should_center** (*bool*)
  * **height** (*float* *|* *None*)
  * **organize_left_to_right** (*bool*)
  * **tex_environment** (*str* *|* *None*)
  * **tex_template** ([*TexTemplate*](manim.utils.tex.TexTemplate.md#manim.utils.tex.TexTemplate) *|* *None*)
  * **font_size** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(tex_string, stroke_width=0, should_center=True, height=None, organize_left_to_right=False, tex_environment='align\*', tex_template=None, font_size=48, color=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **tex_string** (*str*)
  * **stroke_width** (*float*)
  * **should_center** (*bool*)
  * **height** (*float* *|* *None*)
  * **organize_left_to_right** (*bool*)
  * **tex_environment** (*str* *|* *None*)
  * **tex_template** ([*TexTemplate*](manim.utils.tex.TexTemplate.md#manim.utils.tex.TexTemplate) *|* *None*)
  * **font_size** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **kwargs** (*Any*)

#### \_remove_stray_braces(tex)

Makes [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) resilient to unmatched braces.

This is important when the braces in the TeX code are spread over
multiple arguments as in, e.g., `MathTex(r"e^{i", r"\tau} = 1")`.

* **Parameters:**
  **tex** (*str*)
* **Return type:**
  str

#### *property* font_size *: float*

The font size of the tex mobject.

#### init_colors(propagate_colors=True)

Initializes the colors.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Parameters:**
  **propagate_colors** (*bool*)
* **Return type:**
  *Self*
