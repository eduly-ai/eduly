# MobjectTable

Qualified name: `manim.mobject.table.MobjectTable`

### *class* MobjectTable(table, element_to_mobject=<function MobjectTable.<lambda>>, \*\*kwargs)

Bases: [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table)

A specialized [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table) mobject for use with [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).

### Examples

Special case of [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table) with `element_to_mobject` set to an identity function.
Here, every item in `table` must already be of type [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).

* **Parameters:**
  * **table** (*Iterable* *[**Iterable* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *]*) – A 2D array or list of lists. Content of the table must be of type [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).
  * **element_to_mobject** (*Callable* *[* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*) – The [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) class applied to the table entries. Set as `lambda m : m` to return itself.
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

#### \_original_\_init_\_(table, element_to_mobject=<function MobjectTable.<lambda>>, \*\*kwargs)

Special case of [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table) with `element_to_mobject` set to an identity function.
Here, every item in `table` must already be of type [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).

* **Parameters:**
  * **table** (*Iterable* *[**Iterable* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *]*) – A 2D array or list of lists. Content of the table must be of type [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).
  * **element_to_mobject** (*Callable* *[* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*) – The [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) class applied to the table entries. Set as `lambda m : m` to return itself.
  * **kwargs** – Additional arguments to be passed to [`Table`](manim.mobject.table.Table.md#manim.mobject.table.Table).
