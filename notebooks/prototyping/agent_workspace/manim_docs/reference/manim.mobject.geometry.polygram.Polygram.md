# Polygram

Qualified name: `manim.mobject.geometry.polygram.Polygram`

### *class* Polygram(\*vertex_groups, color=ManimColor('#58C4DD'), \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A generalized [`Polygon`](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon), allowing for disconnected sets of edges.

* **Parameters:**
  * **vertex_groups** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array)) – 

    The groups of vertices making up the [`Polygram`](#manim.mobject.geometry.polygram.Polygram).

    The first vertex in each group is repeated to close the shape.
    Each point must be 3-dimensional: `[x,y,z]`
  * **color** ([*manim.utils.color.core.ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)) – The color of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram).
  * **kwargs** (*Any*) – Forwarded to the parent constructor.

### Examples

### Methods

| [`get_vertex_groups`](#manim.mobject.geometry.polygram.Polygram.get_vertex_groups)   | Gets the vertex groups of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram).   |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [`get_vertices`](#manim.mobject.geometry.polygram.Polygram.get_vertices)             | Gets the vertices of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram).        |
| [`round_corners`](#manim.mobject.geometry.polygram.Polygram.round_corners)           | Rounds off the corners of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram).   |

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

#### \_original_\_init_\_(\*vertex_groups, color=ManimColor('#58C4DD'), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vertex_groups** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array))
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **kwargs** (*Any*)

#### get_vertex_groups()

Gets the vertex groups of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram).

* **Returns:**
  The list of vertex groups of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram).
* **Return type:**
  list[[Point3D_Array](manim.typing.md#manim.typing.Point3D_Array)]

### Examples

```default
>>> poly = Polygram([ORIGIN, RIGHT, UP, LEFT + UP], [LEFT, LEFT + UP, 2 * LEFT])
>>> groups = poly.get_vertex_groups()
>>> len(groups)
2
>>> groups[0]
array([[ 0.,  0.,  0.],
       [ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [-1.,  1.,  0.]])
>>> groups[1]
array([[-1.,  0.,  0.],
       [-1.,  1.,  0.],
       [-2.,  0.,  0.]])
```

#### get_vertices()

Gets the vertices of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram).

* **Returns:**
  The vertices of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram).
* **Return type:**
  `numpy.ndarray`

### Examples

```default
>>> sq = Square()
>>> sq.get_vertices()
array([[ 1.,  1.,  0.],
       [-1.,  1.,  0.],
       [-1., -1.,  0.],
       [ 1., -1.,  0.]])
```

#### round_corners(radius=0.5, evenly_distribute_anchors=False, components_per_rounded_corner=2)

Rounds off the corners of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram).

* **Parameters:**
  * **radius** (*float* *|* *list* *[**float* *]*) – The curvature of the corners of the [`Polygram`](#manim.mobject.geometry.polygram.Polygram).
  * **evenly_distribute_anchors** (*bool*) – Break long line segments into proportionally-sized segments.
  * **components_per_rounded_corner** (*int*) – The number of points used to represent the rounded corner curve.
* **Return type:**
  Self

#### SEE ALSO
`RoundedRectangle`

#### NOTE
If radius is supplied as a single value, then the same radius
will be applied to all corners.  If radius is a list, then the
individual values will be applied sequentially, with the first
corner receiving radius[0], the second corner receiving
radius[1], etc.  The radius list will be repeated as necessary.

The components_per_rounded_corner value is provided so that the
fidelity of the rounded corner may be fine-tuned as needed.  2 is
an appropriate value for most shapes, however a larger value may be
need if the rounded corner is particularly large.  2 is the minimum
number allowed, representing the start and end of the curve.  3 will
result in a start, middle, and end point, meaning 2 curves will be
generated.

The option to evenly_distribute_anchors is provided so that the
line segments (the part part of each line remaining after rounding
off the corners) can be subdivided to a density similar to that of
the average density of the rounded corners.  This may be desirable
in situations in which an even distribution of curves is desired
for use in later transformation animations.  Be aware, though, that
enabling this option can result in an an object containing
significantly more points than the original, especially when the
rounded corner curves are small.

### Examples
