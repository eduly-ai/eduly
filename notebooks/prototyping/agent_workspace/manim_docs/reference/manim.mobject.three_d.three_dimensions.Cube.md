# Cube

Qualified name: `manim.mobject.three\_d.three\_dimensions.Cube`

### *class* Cube(side_length=2, fill_opacity=0.75, fill_color=ManimColor('#58C4DD'), stroke_width=0, \*\*kwargs)

Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

A three-dimensional cube.

* **Parameters:**
  * **side_length** (*float*) – Length of each side of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube).
  * **fill_opacity** (*float*) – The opacity of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube), from 0 being fully transparent to 1 being
    fully opaque. Defaults to 0.75.
  * **fill_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube).
  * **stroke_width** (*float*) – The width of the stroke surrounding each face of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube).

### Examples

### Methods

| [`generate_points`](#manim.mobject.three_d.three_dimensions.Cube.generate_points)   | Creates the sides of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube).   |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| `init_points`                                                                       |                                                                                    |

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

#### \_original_\_init_\_(side_length=2, fill_opacity=0.75, fill_color=ManimColor('#58C4DD'), stroke_width=0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **side_length** (*float*)
  * **fill_opacity** (*float*)
  * **fill_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **stroke_width** (*float*)
* **Return type:**
  None

#### generate_points()

Creates the sides of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube).

* **Return type:**
  None
