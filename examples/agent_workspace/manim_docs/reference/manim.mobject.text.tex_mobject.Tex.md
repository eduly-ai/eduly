# Tex

Qualified name: `manim.mobject.text.tex\_mobject.Tex`

### *class* Tex(\*tex_strings, arg_separator='', tex_environment='center', \*\*kwargs)

Bases: [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex)

A string compiled with LaTeX in normal mode.

The color can be set using
the `color` argument. Any parts of the `tex_string` that are colored by the
TeX commands `\color` or `\textcolor` will retain their original color.

### Tests

Check whether writing a LaTeX string works:

```default
>>> Tex('The horse does not eat cucumber salad.') 
Tex('The horse does not eat cucumber salad.')
```

### Methods

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
  * **tex_environment** (*str* *|* *None*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(\*tex_strings, arg_separator='', tex_environment='center', \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **tex_strings** (*str*)
  * **arg_separator** (*str*)
  * **tex_environment** (*str* *|* *None*)
  * **kwargs** (*Any*)
