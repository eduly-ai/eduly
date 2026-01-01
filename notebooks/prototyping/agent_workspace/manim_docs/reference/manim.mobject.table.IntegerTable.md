# IntegerTable

Qualified name: `manim.mobject.table.IntegerTable`

### *class* IntegerTable(table, element_to_mobject=<class 'manim.mobject.text.numbers.Integer'>, \*\*kwargs)

Bases: [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table)

A specialized [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table) mobject for use with [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer).

### Examples

Special case of [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table) with element_to_mobject set to [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer).
Will round if there are decimal entries in the table.

* **Parameters:**
  * **table** (*Iterable* *[**Iterable* *[**float* *|* *str* *]* *]*) – A 2d array or list of lists. Content of the table has to be valid input
    for [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer).
  * **element_to_mobject** (*Callable* *[* *[**float* *|* *str* *]* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*) – The [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) class applied to the table entries. Set as [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer).
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

#### \_original_\_init_\_(table, element_to_mobject=<class 'manim.mobject.text.numbers.Integer'>, \*\*kwargs)

Special case of [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table) with element_to_mobject set to [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer).
Will round if there are decimal entries in the table.

* **Parameters:**
  * **table** (*Iterable* *[**Iterable* *[**float* *|* *str* *]* *]*) – A 2d array or list of lists. Content of the table has to be valid input
    for [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer).
  * **element_to_mobject** (*Callable* *[* *[**float* *|* *str* *]* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*) – The [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) class applied to the table entries. Set as [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer).
  * **kwargs** – Additional arguments to be passed to [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table).
