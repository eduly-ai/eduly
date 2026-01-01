# MathTable

Qualified name: `manim.mobject.table.MathTable`

### *class* MathTable(table, element_to_mobject=<class 'manim.mobject.text.tex_mobject.MathTex'>, \*\*kwargs)

Bases: [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table)

A specialized [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table) mobject for use with LaTeX.

### Examples

Special case of [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table) with element_to_mobject set to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex).
Every entry in table is set in a Latex align environment.

* **Parameters:**
  * **table** (*Iterable* *[**Iterable* *[**float* *|* *str* *]* *]*) – A 2d array or list of lists. Content of the table have to be valid input
    for [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex).
  * **element_to_mobject** (*Callable* *[* *[**float* *|* *str* *]* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*) – The [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) class applied to the table entries. Set as [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex).
  * **kwargs** – Additional arguments to be passed to [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table).

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

#### \_original_\_init_\_(table, element_to_mobject=<class 'manim.mobject.text.tex_mobject.MathTex'>, \*\*kwargs)

Special case of [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table) with element_to_mobject set to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex).
Every entry in table is set in a Latex align environment.

* **Parameters:**
  * **table** (*Iterable* *[**Iterable* *[**float* *|* *str* *]* *]*) – A 2d array or list of lists. Content of the table have to be valid input
    for [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex).
  * **element_to_mobject** (*Callable* *[* *[**float* *|* *str* *]* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*) – The [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) class applied to the table entries. Set as [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex).
  * **kwargs** – Additional arguments to be passed to [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table).
