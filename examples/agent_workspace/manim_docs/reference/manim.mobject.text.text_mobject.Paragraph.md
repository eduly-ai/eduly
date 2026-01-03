# Paragraph

Qualified name: `manim.mobject.text.text\_mobject.Paragraph`

### *class* Paragraph(\*text, line_spacing=-1, alignment=None, \*\*kwargs)

Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

Display a paragraph of text.

For a given [`Paragraph`](#manim.mobject.text.text_mobject.Paragraph) `par`, the attribute `par.chars` is a
[`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) containing all the lines. In this context, every line is
constructed as a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) of characters contained in the line.

* **Parameters:**
  * **line_spacing** (*float*) – Represents the spacing between lines. Defaults to -1, which means auto.
  * **alignment** (*str* *|* *None*) – Defines the alignment of paragraph. Defaults to None. Possible values are “left”, “right” or “center”.
  * **text** (*str*)
  * **kwargs** (*Any*)

### Examples

Normal usage:

```default
paragraph = Paragraph(
    "this is a awesome",
    "paragraph",
    "With \nNewlines",
    "\tWith Tabs",
    "  With Spaces",
    "With Alignments",
    "center",
    "left",
    "right",
)
```

Remove unwanted invisible characters:

```default
self.play(Transform(remove_invisible_chars(paragraph.chars[0:2]),
                    remove_invisible_chars(paragraph.chars[3][0:3]))
```

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

#### \_change_alignment_for_a_line(alignment, line_no)

Function to change one line’s alignment to a specific value.

* **Parameters:**
  * **alignment** (*str*) – Defines the alignment of paragraph. Possible values are “left”, “right”, “center”.
  * **line_no** (*int*) – Defines the line number for which we want to set given alignment.
* **Return type:**
  None

#### \_gen_chars(lines_str_list)

Function to convert a list of plain strings to a VGroup of VGroups of chars.

* **Parameters:**
  **lines_str_list** (*list*) – List of plain text strings.
* **Returns:**
  The generated 2d-VGroup of chars.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

#### \_original_\_init_\_(\*text, line_spacing=-1, alignment=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **text** (*str*)
  * **line_spacing** (*float*)
  * **alignment** (*str* *|* *None*)
  * **kwargs** (*Any*)

#### \_set_all_lines_alignments(alignment)

Function to set all line’s alignment to a specific value.

* **Parameters:**
  **alignment** (*str*) – Defines the alignment of paragraph. Possible values are “left”, “right”, “center”.
* **Return type:**
  [*Paragraph*](#manim.mobject.text.text_mobject.Paragraph)

#### \_set_all_lines_to_initial_positions()

Set all lines to their initial positions.

* **Return type:**
  [*Paragraph*](#manim.mobject.text.text_mobject.Paragraph)

#### \_set_line_alignment(alignment, line_no)

Function to set one line’s alignment to a specific value.

* **Parameters:**
  * **alignment** (*str*) – Defines the alignment of paragraph. Possible values are “left”, “right”, “center”.
  * **line_no** (*int*) – Defines the line number for which we want to set given alignment.
* **Return type:**
  [*Paragraph*](#manim.mobject.text.text_mobject.Paragraph)

#### \_set_line_to_initial_position(line_no)

Function to set one line to initial positions.

* **Parameters:**
  **line_no** (*int*) – Defines the line number for which we want to set given alignment.
* **Return type:**
  [*Paragraph*](#manim.mobject.text.text_mobject.Paragraph)
