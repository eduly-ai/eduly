# Brace

Qualified name: `manim.mobject.svg.brace.Brace`

### *class* Brace(mobject, direction=array([0., -1., 0.]), buff=0.2, sharpness=2, stroke_width=0, fill_opacity=1.0, background_stroke_width=0, background_stroke_color=ManimColor('#000000'), \*\*kwargs)

Bases: [`VMobjectFromSVGPath`](manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.md#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath)

Takes a mobject and draws a brace adjacent to it.

Passing a direction vector determines the direction from which the
brace is drawn. By default it is drawn from below.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject adjacent to which the brace is placed.
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The direction from which the brace faces the mobject.
  * **buff** (*float*)
  * **sharpness** (*float*)
  * **stroke_width** (*float*)
  * **fill_opacity** (*float*)
  * **background_stroke_width** (*float*)
  * **background_stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **kwargs** (*Any*)

#### SEE ALSO
[`BraceBetweenPoints`](manim.mobject.svg.brace.BraceBetweenPoints.md#manim.mobject.svg.brace.BraceBetweenPoints)

### Examples

### Methods

| [`get_direction`](#manim.mobject.svg.brace.Brace.get_direction)   | Returns the direction from the center to the brace tip.   |
|-------------------------------------------------------------------|-----------------------------------------------------------|
| [`get_tex`](#manim.mobject.svg.brace.Brace.get_tex)               | Places the tex at the brace tip.                          |
| [`get_text`](#manim.mobject.svg.brace.Brace.get_text)             | Places the text at the brace tip.                         |
| [`get_tip`](#manim.mobject.svg.brace.Brace.get_tip)               | Returns the point at the brace tip.                       |
| [`put_at_tip`](#manim.mobject.svg.brace.Brace.put_at_tip)         | Puts the given mobject at the brace tip.                  |

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

#### \_original_\_init_\_(mobject, direction=array([0., -1., 0.]), buff=0.2, sharpness=2, stroke_width=0, fill_opacity=1.0, background_stroke_width=0, background_stroke_color=ManimColor('#000000'), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **buff** (*float*)
  * **sharpness** (*float*)
  * **stroke_width** (*float*)
  * **fill_opacity** (*float*)
  * **background_stroke_width** (*float*)
  * **background_stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **kwargs** (*Any*)

#### get_direction()

Returns the direction from the center to the brace tip.

* **Return type:**
  [*Vector3D*](manim.typing.md#manim.typing.Vector3D)

#### get_tex(\*tex, \*\*kwargs)

Places the tex at the brace tip.

* **Parameters:**
  * **tex** (*str*) – The tex to be placed at the brace tip.
  * **kwargs** (*Any*) – Any further keyword arguments are passed to [`put_at_tip()`](#manim.mobject.svg.brace.Brace.put_at_tip) which
    is used to position the tex at the brace tip.
* **Return type:**
  [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex)

#### get_text(\*text, \*\*kwargs)

Places the text at the brace tip.

* **Parameters:**
  * **text** (*str*) – The text to be placed at the brace tip.
  * **kwargs** (*Any*) – Any additional keyword arguments are passed to [`put_at_tip()`](#manim.mobject.svg.brace.Brace.put_at_tip) which
    is used to position the text at the brace tip.
* **Return type:**
  [`Tex`](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex)

#### get_tip()

Returns the point at the brace tip.

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### put_at_tip(mob, use_next_to=True, \*\*kwargs)

Puts the given mobject at the brace tip.

* **Parameters:**
  * **mob** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to be placed at the tip.
  * **use_next_to** (*bool*) – If true, then `next_to()` is used to place the mobject at the
    tip.
  * **kwargs** (*Any*) – Any additional keyword arguments are passed to `next_to()` which
    is used to put the mobject next to the brace tip.
* **Return type:**
  *Self*
