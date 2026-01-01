# Table

Qualified name: `manim.mobject.table.Table`

### *class* Table(table, row_labels=None, col_labels=None, top_left_entry=None, v_buff=0.8, h_buff=1.3, include_outer_lines=False, add_background_rectangles_to_entries=False, entries_background_color=ManimColor('#000000'), include_background_rectangle=False, background_rectangle_color=ManimColor('#000000'), element_to_mobject=<class 'manim.mobject.text.text_mobject.Paragraph'>, element_to_mobject_config={}, arrange_in_grid_config={}, line_config={}, \*\*kwargs)

Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

A mobject that displays a table on the screen.

* **Parameters:**
  * **table** (*Iterable* *[**Iterable* *[**float* *|* *str* *|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *]*) – A 2D array or list of lists. Content of the table has to be a valid input
    for the callable set in `element_to_mobject`.
  * **row_labels** (*Iterable* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*  *|* *None*) – List of [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) representing the labels of each row.
  * **col_labels** (*Iterable* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*  *|* *None*) – List of [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) representing the labels of each column.
  * **top_left_entry** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *None*) – The top-left entry of the table, can only be specified if row and
    column labels are given.
  * **v_buff** (*float*) – Vertical buffer passed to [`arrange_in_grid()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.arrange_in_grid), by default 0.8.
  * **h_buff** (*float*) – Horizontal buffer passed to [`arrange_in_grid()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.arrange_in_grid), by default 1.3.
  * **include_outer_lines** (*bool*) – `True` if the table should include outer lines, by default False.
  * **add_background_rectangles_to_entries** (*bool*) – `True` if background rectangles should be added to entries, by default `False`.
  * **entries_background_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – Background color of entries if `add_background_rectangles_to_entries` is `True`.
  * **include_background_rectangle** (*bool*) – `True` if the table should have a background rectangle, by default `False`.
  * **background_rectangle_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – Background color of table if `include_background_rectangle` is `True`.
  * **element_to_mobject** (*Callable* *[* *[**float* *|* *str* *|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*) – The [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) class applied to the table entries. by default [`Paragraph`](manim.mobject.text.text_mobject.Paragraph.md#manim.mobject.text.text_mobject.Paragraph). For common choices, see [`text_mobject`](manim.mobject.text.text_mobject.md#module-manim.mobject.text.text_mobject)/[`tex_mobject`](manim.mobject.text.tex_mobject.md#module-manim.mobject.text.tex_mobject).
  * **element_to_mobject_config** (*dict*) – Custom configuration passed to `element_to_mobject`, by default {}.
  * **arrange_in_grid_config** (*dict*) – Dict passed to [`arrange_in_grid()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.arrange_in_grid), customizes the arrangement of the table.
  * **line_config** (*dict*) – Dict passed to [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line), customizes the lines of the table.
  * **kwargs** – Additional arguments to be passed to [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup).

### Examples

### Methods

| [`add_background_to_entries`](#manim.mobject.table.Table.add_background_to_entries)   | Adds a black [`BackgroundRectangle`](manim.mobject.geometry.shape_matchers.BackgroundRectangle.md#manim.mobject.geometry.shape_matchers.BackgroundRectangle) to each entry of the table.                                                                    |
|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`add_highlighted_cell`](#manim.mobject.table.Table.add_highlighted_cell)             | Highlights one cell at a specific position on the table by adding a [`BackgroundRectangle`](manim.mobject.geometry.shape_matchers.BackgroundRectangle.md#manim.mobject.geometry.shape_matchers.BackgroundRectangle).                                        |
| [`create`](#manim.mobject.table.Table.create)                                         | Customized create-type function for tables.                                                                                                                                                                                                                 |
| [`get_cell`](#manim.mobject.table.Table.get_cell)                                     | Returns one specific cell as a rectangular [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon) without the entry.                                                                                               |
| [`get_col_labels`](#manim.mobject.table.Table.get_col_labels)                         | Return the column labels of the table.                                                                                                                                                                                                                      |
| [`get_columns`](#manim.mobject.table.Table.get_columns)                               | Return columns of the table as a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) of [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup).  |
| [`get_entries`](#manim.mobject.table.Table.get_entries)                               | Return the individual entries of the table (including labels) or one specific entry if the parameter, `pos`,  is set.                                                                                                                                       |
| [`get_entries_without_labels`](#manim.mobject.table.Table.get_entries_without_labels) | Return the individual entries of the table (without labels) or one specific entry if the parameter, `pos`, is set.                                                                                                                                          |
| [`get_highlighted_cell`](#manim.mobject.table.Table.get_highlighted_cell)             | Returns a [`BackgroundRectangle`](manim.mobject.geometry.shape_matchers.BackgroundRectangle.md#manim.mobject.geometry.shape_matchers.BackgroundRectangle) of the cell at the given position.                                                                |
| [`get_horizontal_lines`](#manim.mobject.table.Table.get_horizontal_lines)             | Return the horizontal lines of the table.                                                                                                                                                                                                                   |
| [`get_labels`](#manim.mobject.table.Table.get_labels)                                 | Returns the labels of the table.                                                                                                                                                                                                                            |
| [`get_row_labels`](#manim.mobject.table.Table.get_row_labels)                         | Return the row labels of the table.                                                                                                                                                                                                                         |
| [`get_rows`](#manim.mobject.table.Table.get_rows)                                     | Return the rows of the table as a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) of [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup). |
| [`get_vertical_lines`](#manim.mobject.table.Table.get_vertical_lines)                 | Return the vertical lines of the table.                                                                                                                                                                                                                     |
| [`scale`](#manim.mobject.table.Table.scale)                                           | Scale the size by a factor.                                                                                                                                                                                                                                 |
| [`set_column_colors`](#manim.mobject.table.Table.set_column_colors)                   | Set individual colors for each column of the table.                                                                                                                                                                                                         |
| [`set_row_colors`](#manim.mobject.table.Table.set_row_colors)                         | Set individual colors for each row of the table.                                                                                                                                                                                                            |

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

#### \_add_horizontal_lines()

Adds the horizontal lines to the table.

* **Return type:**
  [*Table*](#manim.mobject.table.Table)

#### \_add_labels(mob_table)

Adds labels to an in a grid arranged [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup).

* **Parameters:**
  **mob_table** ([*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)) – An in a grid organized class:~.VGroup.
* **Returns:**
  Returns the `mob_table` with added labels.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

#### \_add_vertical_lines()

Adds the vertical lines to the table

* **Return type:**
  [*Table*](#manim.mobject.table.Table)

#### \_organize_mob_table(table)

Arranges the [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) of `table` in a grid.

* **Parameters:**
  **table** (*Iterable* *[**Iterable* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *]*) – A 2D iterable object with [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) entries.
* **Returns:**
  The [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) of the `table` in a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) already
  arranged in a table-like grid.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

#### \_original_\_init_\_(table, row_labels=None, col_labels=None, top_left_entry=None, v_buff=0.8, h_buff=1.3, include_outer_lines=False, add_background_rectangles_to_entries=False, entries_background_color=ManimColor('#000000'), include_background_rectangle=False, background_rectangle_color=ManimColor('#000000'), element_to_mobject=<class 'manim.mobject.text.text_mobject.Paragraph'>, element_to_mobject_config={}, arrange_in_grid_config={}, line_config={}, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **table** (*Iterable* *[**Iterable* *[**float* *|* *str* *|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *]*)
  * **row_labels** (*Iterable* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*  *|* *None*)
  * **col_labels** (*Iterable* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*  *|* *None*)
  * **top_left_entry** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *None*)
  * **v_buff** (*float*)
  * **h_buff** (*float*)
  * **include_outer_lines** (*bool*)
  * **add_background_rectangles_to_entries** (*bool*)
  * **entries_background_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **include_background_rectangle** (*bool*)
  * **background_rectangle_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **element_to_mobject** (*Callable* *[* *[**float* *|* *str* *|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*)
  * **element_to_mobject_config** (*dict*)
  * **arrange_in_grid_config** (*dict*)
  * **line_config** (*dict*)

#### \_table_to_mob_table(table)

Initializes the entries of `table` as [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).

* **Parameters:**
  **table** (*Iterable* *[**Iterable* *[**float* *|* *str* *|* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *]*) – A 2D array or list of lists. Content of the table has to be a valid input
  for the callable set in `element_to_mobject`.
* **Returns:**
  List of [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) from the entries of `table`.
* **Return type:**
  List

#### add_background_to_entries(color=ManimColor('#000000'))

Adds a black [`BackgroundRectangle`](manim.mobject.geometry.shape_matchers.BackgroundRectangle.md#manim.mobject.geometry.shape_matchers.BackgroundRectangle) to each entry of the table.

* **Parameters:**
  **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
* **Return type:**
  [*Table*](#manim.mobject.table.Table)

#### add_highlighted_cell(pos=(1, 1), color=ManimColor('#FFFF00'), \*\*kwargs)

Highlights one cell at a specific position on the table by adding a [`BackgroundRectangle`](manim.mobject.geometry.shape_matchers.BackgroundRectangle.md#manim.mobject.geometry.shape_matchers.BackgroundRectangle).

* **Parameters:**
  * **pos** (*Sequence* *[**int* *]*) – The position of a specific entry on the table. `(1,1)` being the top left entry
    of the table.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color used to highlight the cell.
  * **kwargs** – Additional arguments to be passed to [`BackgroundRectangle`](manim.mobject.geometry.shape_matchers.BackgroundRectangle.md#manim.mobject.geometry.shape_matchers.BackgroundRectangle).
* **Return type:**
  [*Table*](#manim.mobject.table.Table)

### Examples

#### create(lag_ratio=1, line_animation=<class 'manim.animation.creation.Create'>, label_animation=<class 'manim.animation.creation.Write'>, element_animation=<class 'manim.animation.creation.Create'>, entry_animation=<class 'manim.animation.fading.FadeIn'>, \*\*kwargs)

Customized create-type function for tables.

* **Parameters:**
  * **lag_ratio** (*float*) – The lag ratio of the animation.
  * **line_animation** (*Callable* *[* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) *]* *,* [*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – The animation style of the table lines, see [`creation`](manim.animation.creation.md#module-manim.animation.creation) for examples.
  * **label_animation** (*Callable* *[* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) *]* *,* [*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – The animation style of the table labels, see [`creation`](manim.animation.creation.md#module-manim.animation.creation) for examples.
  * **element_animation** (*Callable* *[* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) *]* *,* [*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – The animation style of the table elements, see [`creation`](manim.animation.creation.md#module-manim.animation.creation) for examples.
  * **entry_animation** (*Callable* *[* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) *]* *,* [*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – The entry animation of the table background, see [`creation`](manim.animation.creation.md#module-manim.animation.creation) for examples.
  * **kwargs** – Further arguments passed to the creation animations.
* **Returns:**
  AnimationGroup containing creation of the lines and of the elements.
* **Return type:**
  [`AnimationGroup`](manim.animation.composition.AnimationGroup.md#manim.animation.composition.AnimationGroup)

### Examples

#### get_cell(pos=(1, 1), \*\*kwargs)

Returns one specific cell as a rectangular [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon) without the entry.

* **Parameters:**
  * **pos** (*Sequence* *[**int* *]*) – The position of a specific entry on the table. `(1,1)` being the top left entry
    of the table.
  * **kwargs** – Additional arguments to be passed to [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon).
* **Returns:**
  Polygon mimicking one specific cell of the Table.
* **Return type:**
  [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon)

### Examples

#### get_col_labels()

Return the column labels of the table.

* **Returns:**
  VGroup containing the column labels of the table.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_columns()

Return columns of the table as a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) of [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup).

* **Returns:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) containing each column in a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup).
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_entries(pos=None)

Return the individual entries of the table (including labels) or one specific entry
if the parameter, `pos`,  is set.

* **Parameters:**
  **pos** (*Sequence* *[**int* *]*  *|* *None*) – The position of a specific entry on the table. `(1,1)` being the top left entry
  of the table.
* **Returns:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) containing all entries of the table (including labels)
  or the [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) at the given position if `pos` is set.
* **Return type:**
  Union[[`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject), [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)]

### Examples

#### get_entries_without_labels(pos=None)

Return the individual entries of the table (without labels) or one specific entry
if the parameter, `pos`, is set.

* **Parameters:**
  **pos** (*Sequence* *[**int* *]*  *|* *None*) – The position of a specific entry on the table. `(1,1)` being the top left entry
  of the table (without labels).
* **Returns:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) containing all entries of the table (without labels)
  or the [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) at the given position if `pos` is set.
* **Return type:**
  Union[[`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject), [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)]

### Examples

#### get_highlighted_cell(pos=(1, 1), color=ManimColor('#FFFF00'), \*\*kwargs)

Returns a [`BackgroundRectangle`](manim.mobject.geometry.shape_matchers.BackgroundRectangle.md#manim.mobject.geometry.shape_matchers.BackgroundRectangle) of the cell at the given position.

* **Parameters:**
  * **pos** (*Sequence* *[**int* *]*) – The position of a specific entry on the table. `(1,1)` being the top left entry
    of the table.
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color used to highlight the cell.
  * **kwargs** – Additional arguments to be passed to [`BackgroundRectangle`](manim.mobject.geometry.shape_matchers.BackgroundRectangle.md#manim.mobject.geometry.shape_matchers.BackgroundRectangle).
* **Return type:**
  [*BackgroundRectangle*](manim.mobject.geometry.shape_matchers.BackgroundRectangle.md#manim.mobject.geometry.shape_matchers.BackgroundRectangle)

### Examples

#### get_horizontal_lines()

Return the horizontal lines of the table.

* **Returns:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) containing all the horizontal lines of the table.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_labels()

Returns the labels of the table.

* **Returns:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) containing all the labels of the table.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_row_labels()

Return the row labels of the table.

* **Returns:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) containing the row labels of the table.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_rows()

Return the rows of the table as a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) of [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup).

* **Returns:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) containing each row in a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup).
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_vertical_lines()

Return the vertical lines of the table.

* **Returns:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) containing all the vertical lines of the table.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### scale(scale_factor, \*\*kwargs)

Scale the size by a factor.

Default behavior is to scale about the center of the vmobject.

* **Parameters:**
  * **scale_factor** (*float*) – The scaling factor $\alpha$. If $0 < |\alpha| < 1$, the mobject
    will shrink, and for $|\alpha| > 1$ it will grow. Furthermore,
    if $\alpha < 0$, the mobject is also flipped.
  * **scale_stroke** – Boolean determining if the object’s outline is scaled when the object is scaled.
    If enabled, and object with 2px outline is scaled by a factor of .5, it will have an outline of 1px.
  * **kwargs** – Additional keyword arguments passed to
    [`scale()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.scale).
* **Returns:**
  `self`
* **Return type:**
  `VMobject`

### Examples

#### SEE ALSO
`move_to()`

#### set_column_colors(\*colors)

Set individual colors for each column of the table.

* **Parameters:**
  **colors** (*Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*) – An iterable of colors; each color corresponds to a column.
* **Return type:**
  [*Table*](#manim.mobject.table.Table)

### Examples

#### set_row_colors(\*colors)

Set individual colors for each row of the table.

* **Parameters:**
  **colors** (*Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*) – An iterable of colors; each color corresponds to a row.
* **Return type:**
  [*Table*](#manim.mobject.table.Table)

### Examples
