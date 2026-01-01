# ArcPolygonFromArcs

Qualified name: `manim.mobject.geometry.arc.ArcPolygonFromArcs`

### *class* ArcPolygonFromArcs(\*arcs, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A generalized polygon allowing for points to be connected with arcs.

This version takes in pre-defined arcs to generate the arcpolygon and introduces
little new syntax. However unlike `Polygon` it can’t be created with points
directly.

For proper appearance the passed arcs should connect seamlessly:
`[a,b][b,c][c,a]`

If there are any gaps between the arcs, those will be filled in
with straight lines, which can be used deliberately for any straight
sections. Arcs can also be passed as straight lines such as an arc
initialized with `angle=0`.

* **Parameters:**
  * **arcs** ([*Arc*](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc) *|* [*ArcBetweenPoints*](manim.mobject.geometry.arc.ArcBetweenPoints.md#manim.mobject.geometry.arc.ArcBetweenPoints)) – These are the arcs from which the arcpolygon is assembled.
  * **kwargs** (*Any*) – Keyword arguments that are passed to the constructor of
    [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject). Affects how the ArcPolygon itself is drawn,
    but doesn’t affect passed arcs.

#### arcs

The arcs used to initialize the ArcPolygonFromArcs:

```default
>>> from manim import ArcPolygonFromArcs, Arc, ArcBetweenPoints
>>> ap = ArcPolygonFromArcs(Arc(), ArcBetweenPoints([1,0,0], [0,1,0]), Arc())
>>> ap.arcs
[Arc, ArcBetweenPoints, Arc]
```

#### NOTE
There is an alternative version ([`ArcPolygon`](manim.mobject.geometry.arc.ArcPolygon.md#manim.mobject.geometry.arc.ArcPolygon)) that can be instantiated
with points.

#### SEE ALSO
[`ArcPolygon`](manim.mobject.geometry.arc.ArcPolygon.md#manim.mobject.geometry.arc.ArcPolygon)

### Examples

One example of an arcpolygon is the Reuleaux triangle.
Instead of 3 straight lines connecting the outer points,
a Reuleaux triangle has 3 arcs connecting those points,
making a shape with constant width.

Passed arcs are stored as submobjects in the arcpolygon.
This means that the arcs are changed along with the arcpolygon,
for example when it’s shifted, and these arcs can be manipulated
after the arcpolygon has been initialized.

Also both the arcs contained in an [`ArcPolygonFromArcs`](#manim.mobject.geometry.arc.ArcPolygonFromArcs), as well as the
arcpolygon itself are drawn, which affects draw time in [`Create`](manim.animation.creation.Create.md#manim.animation.creation.Create)
for example. In most cases the arcs themselves don’t
need to be drawn, in which case they can be passed as invisible.

The arcpolygon itself can also be hidden so that instead only the contained
arcs are drawn. This can be used to easily debug arcs or to highlight them.

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

#### \_original_\_init_\_(\*arcs, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **arcs** ([*Arc*](manim.mobject.geometry.arc.Arc.md#manim.mobject.geometry.arc.Arc) *|* [*ArcBetweenPoints*](manim.mobject.geometry.arc.ArcBetweenPoints.md#manim.mobject.geometry.arc.ArcBetweenPoints))
  * **kwargs** (*Any*)
* **Return type:**
  None
