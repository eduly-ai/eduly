# ArrowTip

Qualified name: `manim.mobject.geometry.tips.ArrowTip`

### *class* ArrowTip(\*args, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

Base class for arrow tips.

#### SEE ALSO
[`ArrowTriangleTip`](manim.mobject.geometry.tips.ArrowTriangleTip.md#manim.mobject.geometry.tips.ArrowTriangleTip)
[`ArrowTriangleFilledTip`](manim.mobject.geometry.tips.ArrowTriangleFilledTip.md#manim.mobject.geometry.tips.ArrowTriangleFilledTip)
[`ArrowCircleTip`](manim.mobject.geometry.tips.ArrowCircleTip.md#manim.mobject.geometry.tips.ArrowCircleTip)
[`ArrowCircleFilledTip`](manim.mobject.geometry.tips.ArrowCircleFilledTip.md#manim.mobject.geometry.tips.ArrowCircleFilledTip)
[`ArrowSquareTip`](manim.mobject.geometry.tips.ArrowSquareTip.md#manim.mobject.geometry.tips.ArrowSquareTip)
[`ArrowSquareFilledTip`](manim.mobject.geometry.tips.ArrowSquareFilledTip.md#manim.mobject.geometry.tips.ArrowSquareFilledTip)
[`StealthTip`](manim.mobject.geometry.tips.StealthTip.md#manim.mobject.geometry.tips.StealthTip)

### Examples

Cannot be used directly, only intended for inheritance:

```default
>>> tip = ArrowTip()
Traceback (most recent call last):
...
NotImplementedError: Has to be implemented in inheriting subclasses.
```

Instead, use one of the pre-defined ones, or make
a custom one like this:

Using a class inherited from [`ArrowTip`](#manim.mobject.geometry.tips.ArrowTip) to get a non-filled
tip is a shorthand to manually specifying the arrow tip style as follows:

```default
>>> arrow = Arrow(np.array([0, 0, 0]), np.array([1, 1, 0]),
...               tip_style={'fill_opacity': 0, 'stroke_width': 3})
```

The following example illustrates the usage of all of the predefined
arrow tips.

### Methods

### Attributes

| `animate`                                                      | Used to animate the application of any method of `self`.               |
|----------------------------------------------------------------|------------------------------------------------------------------------|
| `animation_overrides`                                          |                                                                        |
| [`base`](#manim.mobject.geometry.tips.ArrowTip.base)           | The base point of the arrow tip.                                       |
| `color`                                                        |                                                                        |
| `depth`                                                        | The depth of the mobject.                                              |
| `fill_color`                                                   | If there are multiple colors (for gradient) this returns the first one |
| `height`                                                       | The height of the mobject.                                             |
| [`length`](#manim.mobject.geometry.tips.ArrowTip.length)       | The length of the arrow tip.                                           |
| `n_points_per_curve`                                           |                                                                        |
| `sheen_factor`                                                 |                                                                        |
| `stroke_color`                                                 |                                                                        |
| [`tip_angle`](#manim.mobject.geometry.tips.ArrowTip.tip_angle) | The angle of the arrow tip.                                            |
| [`tip_point`](#manim.mobject.geometry.tips.ArrowTip.tip_point) | The tip point of the arrow tip.                                        |
| [`vector`](#manim.mobject.geometry.tips.ArrowTip.vector)       | The vector pointing from the base point to the tip point.              |
| `width`                                                        | The width of the mobject.                                              |
* **Parameters:**
  * **args** (*Any*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(\*args, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **args** (*Any*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### *property* base *: [Point3D](manim.typing.md#manim.typing.Point3D)*

The base point of the arrow tip.

This is the point connecting to the arrow line.

### Examples

```default
>>> from manim import Arrow
>>> arrow = Arrow(np.array([0, 0, 0]), np.array([2, 0, 0]), buff=0)
>>> arrow.tip.base.round(2) + 0.  # add 0. to avoid negative 0 in output
array([1.65, 0.  , 0.  ])
```

#### *property* length *: float*

The length of the arrow tip.

### Examples

```default
>>> from manim import Arrow
>>> arrow = Arrow(np.array([0, 0, 0]), np.array([1, 2, 0]))
>>> round(arrow.tip.length, 3)
0.35
```

#### *property* tip_angle *: float*

The angle of the arrow tip.

### Examples

```default
>>> from manim import Arrow
>>> arrow = Arrow(np.array([0, 0, 0]), np.array([1, 1, 0]), buff=0)
>>> bool(round(arrow.tip.tip_angle, 5) == round(PI/4, 5))
True
```

#### *property* tip_point *: [Point3D](manim.typing.md#manim.typing.Point3D)*

The tip point of the arrow tip.

### Examples

```default
>>> from manim import Arrow
>>> arrow = Arrow(np.array([0, 0, 0]), np.array([2, 0, 0]), buff=0)
>>> arrow.tip.tip_point.round(2) + 0.
array([2., 0., 0.])
```

#### *property* vector *: [Vector3D](manim.typing.md#manim.typing.Vector3D)*

The vector pointing from the base point to the tip point.

### Examples

```default
>>> from manim import Arrow
>>> arrow = Arrow(np.array([0, 0, 0]), np.array([2, 2, 0]), buff=0)
>>> arrow.tip.vector.round(2) + 0.
array([0.25, 0.25, 0.  ])
```
