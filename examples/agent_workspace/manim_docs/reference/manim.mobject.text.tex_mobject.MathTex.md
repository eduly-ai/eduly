# MathTex

Qualified name: `manim.mobject.text.tex\_mobject.MathTex`

### *class* MathTex(\*tex_strings, arg_separator=' ', substrings_to_isolate=None, tex_to_color_map=None, tex_environment='align\*', \*\*kwargs)

Bases: [`SingleStringMathTex`](manim.mobject.text.tex_mobject.SingleStringMathTex.md#manim.mobject.text.tex_mobject.SingleStringMathTex)

A string compiled with LaTeX in math mode.

### Examples

### Tests

Check that creating a [`MathTex`](#manim.mobject.text.tex_mobject.MathTex) works:

```default
>>> MathTex('a^2 + b^2 = c^2') 
MathTex('a^2 + b^2 = c^2')
```

Check that double brace group splitting works correctly:

```default
>>> t1 = MathTex('{{ a }} + {{ b }} = {{ c }}') 
>>> len(t1.submobjects) 
5
>>> t2 = MathTex(r"\frac{1}{a+b\sqrt{2}}") 
>>> len(t2.submobjects) 
1
```

### Methods

| `get_part_by_tex`                                                                  |                                        |
|------------------------------------------------------------------------------------|----------------------------------------|
| `get_parts_by_tex`                                                                 |                                        |
| `index_of_part`                                                                    |                                        |
| `index_of_part_by_tex`                                                             |                                        |
| `set_color_by_tex`                                                                 |                                        |
| `set_color_by_tex_to_color_map`                                                    |                                        |
| [`set_opacity_by_tex`](#manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex) | Sets the opacity of the tex specified. |
| `sort_alphabetically`                                                              |                                        |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.               |
|-----------------------|------------------------------------------------------------------------|
| `animation_overrides` |                                                                        |
| `color`               |                                                                        |
| `depth`               | The depth of the mobject.                                              |
| `fill_color`          | If there are multiple colors (for gradient) this returns the first one |
| `font_size`           | The font size of the tex mobject.                                      |
| `hash_seed`           | A unique hash representing the result of the generated mobject points. |
| `height`              | The height of the mobject.                                             |
| `n_points_per_curve`  |                                                                        |
| `sheen_factor`        |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |
* **Parameters:**
  * **tex_strings** (*str*)
  * **arg_separator** (*str*)
  * **substrings_to_isolate** (*Iterable* *[**str* *]*  *|* *None*)
  * **tex_to_color_map** (*dict* *[**str* *,* [*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*  *|* *None*)
  * **tex_environment** (*str* *|* *None*)
  * **kwargs** (*Any*)

#### \_break_up_by_substrings()

Reorganize existing submobjects one layer
deeper based on the structure of tex_strings (as a list
of tex_strings)

* **Return type:**
  *Self*

#### \_original_\_init_\_(\*tex_strings, arg_separator=' ', substrings_to_isolate=None, tex_to_color_map=None, tex_environment='align\*', \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **tex_strings** (*str*)
  * **arg_separator** (*str*)
  * **substrings_to_isolate** (*Iterable* *[**str* *]*  *|* *None*)
  * **tex_to_color_map** (*dict* *[**str* *,* [*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*  *|* *None*)
  * **tex_environment** (*str* *|* *None*)
  * **kwargs** (*Any*)

#### set_opacity_by_tex(tex, opacity=0.5, remaining_opacity=None, \*\*kwargs)

Sets the opacity of the tex specified. If ‘remaining_opacity’ is specified,
then the remaining tex will be set to that opacity.

* **Parameters:**
  * **tex** (*str*) – The tex to set the opacity of.
  * **opacity** (*float*) – Default 0.5. The opacity to set the tex to
  * **remaining_opacity** (*float* *|* *None*) – Default None. The opacity to set the remaining tex to.
    If None, then the remaining tex will not be changed
  * **kwargs** (*Any*)
* **Return type:**
  *Self*
