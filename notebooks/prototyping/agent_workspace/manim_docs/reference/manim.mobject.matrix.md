# matrix

Mobjects representing matrices.

### Examples

### Classes

| [`DecimalMatrix`](manim.mobject.matrix.DecimalMatrix.md#manim.mobject.matrix.DecimalMatrix)   | A mobject that displays a matrix with decimal entries on the screen.   |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [`IntegerMatrix`](manim.mobject.matrix.IntegerMatrix.md#manim.mobject.matrix.IntegerMatrix)   | A mobject that displays a matrix with integer entries on the screen.   |
| [`Matrix`](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix)                        | A mobject that displays a matrix on the screen.                        |
| [`MobjectMatrix`](manim.mobject.matrix.MobjectMatrix.md#manim.mobject.matrix.MobjectMatrix)   | A mobject that displays a matrix of mobject entries on the screen.     |

### Functions

### get_det_text(matrix, determinant=None, background_rect=False, initial_scale_factor=2)

Helper function to create determinant.

* **Parameters:**
  * **matrix** ([*Matrix*](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix)) – The matrix whose determinant is to be created
  * **determinant** (*int* *|* *str* *|* *None*) – The value of the determinant of the matrix
  * **background_rect** (*bool*) – The background rectangle
  * **initial_scale_factor** (*float*) – The scale of the text det w.r.t the matrix
* **Returns:**
  A VGroup containing the determinant
* **Return type:**
  [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

### matrix_to_mobject(matrix)

* **Parameters:**
  **matrix** (*ndarray*)
* **Return type:**
  [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex)

### matrix_to_tex_string(matrix)

* **Parameters:**
  **matrix** (*ndarray*)
* **Return type:**
  str
