# MobjectMatrix

Qualified name: `manim.mobject.matrix.MobjectMatrix`

### *class* MobjectMatrix(matrix, element_to_mobject=<function MobjectMatrix.<lambda>>, \*\*kwargs)

Bases: [`Matrix`](manim.mobject.matrix.Matrix.md#manim.mobject.matrix.Matrix)

A mobject that displays a matrix of mobject entries on the screen.

### Examples

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
* **Parameters:**
  * **matrix** (*Iterable*)
  * **element_to_mobject** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*  *|* *Callable* *[* *...* *,* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(matrix, element_to_mobject=<function MobjectMatrix.<lambda>>, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **matrix** (*Iterable*)
  * **element_to_mobject** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*  *|* *Callable* *[* *[* *...* *]* *,* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*)
  * **kwargs** (*Any*)
