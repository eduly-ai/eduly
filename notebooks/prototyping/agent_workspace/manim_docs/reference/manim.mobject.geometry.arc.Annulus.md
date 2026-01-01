# Annulus

Qualified name: `manim.mobject.geometry.arc.Annulus`

### *class* Annulus(inner_radius=1, outer_radius=2, fill_opacity=1, stroke_width=0, color=ManimColor('#FFFFFF'), mark_paths_closed=False, \*\*kwargs)

Bases: [`Circle`](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle)

Region between two concentric [`Circles`](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle).

* **Parameters:**
  * **inner_radius** (*float*) – The radius of the inner [`Circle`](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle).
  * **outer_radius** (*float*) – The radius of the outer [`Circle`](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle).
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Annulus`](#manim.mobject.geometry.arc.Annulus)
  * **fill_opacity** (*float*)
  * **stroke_width** (*float*)
  * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor))
  * **mark_paths_closed** (*bool*)

### Examples

### Methods

| [`generate_points`](#manim.mobject.geometry.arc.Annulus.generate_points)   | Initializes `points` and therefore the shape.   |
|----------------------------------------------------------------------------|-------------------------------------------------|
| `init_points`                                                              |                                                 |

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

#### \_original_\_init_\_(inner_radius=1, outer_radius=2, fill_opacity=1, stroke_width=0, color=ManimColor('#FFFFFF'), mark_paths_closed=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **inner_radius** (*float*)
  * **outer_radius** (*float*)
  * **fill_opacity** (*float*)
  * **stroke_width** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **mark_paths_closed** (*bool*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### generate_points()

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  None
