# ParametricFunction

Qualified name: `manim.mobject.graphing.functions.ParametricFunction`

### *class* ParametricFunction(function, t_range=(0, 1), scaling=<manim.mobject.graphing.scale.LinearBase object>, dt=1e-08, discontinuities=None, use_smoothing=True, use_vectorized=False, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A parametric curve.

* **Parameters:**
  * **function** (*Callable* *[* *[**float* *]* *,* [*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *]*) – The function to be plotted in the form of `(lambda t: (x(t), y(t), z(t)))`
  * **t_range** (*tuple* *[**float* *,* *float* *]*  *|* *tuple* *[**float* *,* *float* *,* *float* *]*) – Determines the length that the function spans in the form of (t_min, t_max, step=0.01). By default `[0, 1]`
  * **scaling** ( *\_ScaleBase*) – Scaling class applied to the points of the function. Default of [`LinearBase`](manim.mobject.graphing.scale.LinearBase.md#manim.mobject.graphing.scale.LinearBase).
  * **use_smoothing** (*bool*) – Whether to interpolate between the points of the function after they have been created.
    (Will have odd behaviour with a low number of points)
  * **use_vectorized** (*bool*) – Whether to pass in the generated t value array to the function as `[t_0, t_1, ...]`.
    Only use this if your function supports it. Output should be a numpy array
    of shape `[[x_0, x_1, ...], [y_0, y_1, ...], [z_0, z_1, ...]]` but `z` can
    also be 0 if the Axes is 2D
  * **discontinuities** (*Iterable* *[**float* *]*  *|* *None*) – Values of t at which the function experiences discontinuity.
  * **dt** (*float*) – The left and right tolerance for the discontinuities.
  * **kwargs** (*Any*)

### Examples

#### ATTENTION
If your function has discontinuities, you’ll have to specify the location
of the discontinuities manually. See the following example for guidance.

### Methods

| [`generate_points`](#manim.mobject.graphing.functions.ParametricFunction.generate_points)   | Initializes `points` and therefore the shape.   |
|---------------------------------------------------------------------------------------------|-------------------------------------------------|
| `get_function`                                                                              |                                                 |
| `get_point_from_function`                                                                   |                                                 |
| `init_points`                                                                               |                                                 |

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

#### \_original_\_init_\_(function, t_range=(0, 1), scaling=<manim.mobject.graphing.scale.LinearBase object>, dt=1e-08, discontinuities=None, use_smoothing=True, use_vectorized=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **function** (*Callable* *[* *[**float* *]* *,* [*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *]*)
  * **t_range** (*tuple* *[**float* *,* *float* *]*  *|* *tuple* *[**float* *,* *float* *,* *float* *]*)
  * **scaling** ( *\_ScaleBase*)
  * **dt** (*float*)
  * **discontinuities** (*Iterable* *[**float* *]*  *|* *None*)
  * **use_smoothing** (*bool*)
  * **use_vectorized** (*bool*)
  * **kwargs** (*Any*)

#### generate_points()

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  Self
