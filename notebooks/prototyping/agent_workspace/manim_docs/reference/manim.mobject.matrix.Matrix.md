# Matrix

Qualified name: `manim.mobject.matrix.Matrix`

### *class* Matrix(matrix, v_buff=0.8, h_buff=1.3, bracket_h_buff=0.25, bracket_v_buff=0.25, add_background_rectangles_to_entries=False, include_background_rectangle=False, element_to_mobject=<class 'manim.mobject.text.tex_mobject.MathTex'>, element_to_mobject_config={}, element_alignment_corner=array([ 1., -1., 0.]), left_bracket='[', right_bracket=']', stretch_brackets=True, bracket_config={}, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A mobject that displays a matrix on the screen.

* **Parameters:**
  * **matrix** (*Iterable*) – A numpy 2d array or list of lists.
  * **v_buff** (*float*) – Vertical distance between elements, by default 0.8.
  * **h_buff** (*float*) – Horizontal distance between elements, by default 1.3.
  * **bracket_h_buff** (*float*) – Distance of the brackets from the matrix, by default `MED_SMALL_BUFF`.
  * **bracket_v_buff** (*float*) – Height of the brackets, by default `MED_SMALL_BUFF`.
  * **add_background_rectangles_to_entries** (*bool*) – `True` if should add backgraound rectangles to entries, by default `False`.
  * **include_background_rectangle** (*bool*) – `True` if should include background rectangle, by default `False`.
  * **element_to_mobject** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*  *|* *Callable* *[* *...* *,* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The mobject class used to construct the elements, by default [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex).
  * **element_to_mobject_config** (*dict*) – Additional arguments to be passed to the constructor in `element_to_mobject`,
    by default `{}`.
  * **element_alignment_corner** (*Sequence* *[**float* *]*) – The corner to which elements are aligned, by default `DR`.
  * **left_bracket** (*str*) – The left bracket type, by default `"["`.
  * **right_bracket** (*str*) – The right bracket type, by default `"]"`.
  * **stretch_brackets** (*bool*) – `True` if should stretch the brackets to fit the height of matrix contents, by default `True`.
  * **bracket_config** (*dict*) – Additional arguments to be passed to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) when constructing
    the brackets.
  * **kwargs** (*Any*)

### Examples

The first example shows a variety of uses of this module while the second example
exlpains the use of the options add_background_rectangles_to_entries and
include_background_rectangle.

### Methods

| [`add_background_to_entries`](#manim.mobject.matrix.Matrix.add_background_to_entries)   | Add a black background rectangle to the matrix, see above for an example.   |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [`get_brackets`](#manim.mobject.matrix.Matrix.get_brackets)                             | Return the bracket mobjects.                                                |
| [`get_columns`](#manim.mobject.matrix.Matrix.get_columns)                               | Return columns of the matrix as VGroups.                                    |
| [`get_entries`](#manim.mobject.matrix.Matrix.get_entries)                               | Return the individual entries of the matrix.                                |
| [`get_mob_matrix`](#manim.mobject.matrix.Matrix.get_mob_matrix)                         | Return the underlying mob matrix mobjects.                                  |
| [`get_rows`](#manim.mobject.matrix.Matrix.get_rows)                                     | Return rows of the matrix as VGroups.                                       |
| [`set_column_colors`](#manim.mobject.matrix.Matrix.set_column_colors)                   | Set individual colors for each columns of the matrix.                       |
| [`set_row_colors`](#manim.mobject.matrix.Matrix.set_row_colors)                         | Set individual colors for each row of the matrix.                           |

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

#### \_add_brackets(left='[', right=']', \*\*kwargs)

Adds the brackets to the Matrix mobject.

See Latex document for various bracket types.

* **Parameters:**
  * **left** (*str*) – the left bracket, by default “[”
  * **right** (*str*) – the right bracket, by default “]”
  * **kwargs** (*Any*)
* **Returns:**
  The current matrix object (self).
* **Return type:**
  [`Matrix`](#manim.mobject.matrix.Matrix)

#### \_original_\_init_\_(matrix, v_buff=0.8, h_buff=1.3, bracket_h_buff=0.25, bracket_v_buff=0.25, add_background_rectangles_to_entries=False, include_background_rectangle=False, element_to_mobject=<class 'manim.mobject.text.tex_mobject.MathTex'>, element_to_mobject_config={}, element_alignment_corner=array([ 1., -1., 0.]), left_bracket='[', right_bracket=']', stretch_brackets=True, bracket_config={}, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **matrix** (*Iterable*)
  * **v_buff** (*float*)
  * **h_buff** (*float*)
  * **bracket_h_buff** (*float*)
  * **bracket_v_buff** (*float*)
  * **add_background_rectangles_to_entries** (*bool*)
  * **include_background_rectangle** (*bool*)
  * **element_to_mobject** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*  *|* *Callable* *[* *[* *...* *]* *,* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*)
  * **element_to_mobject_config** (*dict*)
  * **element_alignment_corner** (*Sequence* *[**float* *]*)
  * **left_bracket** (*str*)
  * **right_bracket** (*str*)
  * **stretch_brackets** (*bool*)
  * **bracket_config** (*dict*)
  * **kwargs** (*Any*)

#### add_background_to_entries()

Add a black background rectangle to the matrix,
see above for an example.

* **Returns:**
  The current matrix object (self).
* **Return type:**
  [`Matrix`](#manim.mobject.matrix.Matrix)

#### get_brackets()

Return the bracket mobjects.

* **Returns:**
  A VGroup containing the left and right bracket.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_columns()

Return columns of the matrix as VGroups.

* **Returns:**
  The VGroup contains a nested VGroup for each column of the matrix.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_entries()

Return the individual entries of the matrix.

* **Returns:**
  VGroup containing entries of the matrix.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### get_mob_matrix()

Return the underlying mob matrix mobjects.

* **Returns:**
  Each VGroup contains a row of the matrix.
* **Return type:**
  List[[`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)]

#### get_rows()

Return rows of the matrix as VGroups.

* **Returns:**
  The VGroup contains a nested VGroup for each row of the matrix.
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

#### set_column_colors(\*colors)

Set individual colors for each columns of the matrix.

* **Parameters:**
  **colors** (*str*) – The list of colors; each color specified corresponds to a column.
* **Returns:**
  The current matrix object (self).
* **Return type:**
  [`Matrix`](#manim.mobject.matrix.Matrix)

### Examples

#### set_row_colors(\*colors)

Set individual colors for each row of the matrix.

* **Parameters:**
  **colors** (*str*) – The list of colors; each color specified corresponds to a row.
* **Returns:**
  The current matrix object (self).
* **Return type:**
  [`Matrix`](#manim.mobject.matrix.Matrix)

### Examples
