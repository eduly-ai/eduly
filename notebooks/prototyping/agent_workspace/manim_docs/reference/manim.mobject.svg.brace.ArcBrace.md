# ArcBrace

Qualified name: `manim.mobject.svg.brace.ArcBrace`

### *class* ArcBrace(arc=None, direction=array([1., 0., 0.]), \*\*kwargs)

Bases: [`Brace`](manim.mobject.svg.brace.Brace.md#manim.mobject.svg.brace.Brace)

Creates a [`Brace`](manim.mobject.svg.brace.Brace.md#manim.mobject.svg.brace.Brace) that wraps around an [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc).

The direction parameter allows the brace to be applied
from outside or inside the arc.

#### WARNING
The [`ArcBrace`](#manim.mobject.svg.brace.ArcBrace) is smaller for arcs with smaller radii.

#### NOTE
The [`ArcBrace`](#manim.mobject.svg.brace.ArcBrace) is initially a vertical [`Brace`](manim.mobject.svg.brace.Brace.md#manim.mobject.svg.brace.Brace) defined by the
length of the [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc), but is scaled down to match the start and end
angles. An exponential function is then applied after it is shifted based on
the radius of the arc.

The scaling effect is not applied for arcs with radii smaller than 1 to prevent
over-scaling.

* **Parameters:**
  * **arc** ([*Arc*](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc) *|* *None*) – The [`Arc`](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc) that wraps around the [`Brace`](manim.mobject.svg.brace.Brace.md#manim.mobject.svg.brace.Brace) mobject.
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The direction from which the brace faces the arc.
    `LEFT` for inside the arc, and `RIGHT` for the outside.
  * **kwargs** (*Any*)

### Example

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

#### \_original_\_init_\_(arc=None, direction=array([1., 0., 0.]), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **arc** ([*Arc*](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc) *|* *None*)
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **kwargs** (*Any*)
