# DashedLine

Qualified name: `manim.mobject.geometry.line.DashedLine`

### *class* DashedLine(\*args, dash_length=0.05, dashed_ratio=0.5, \*\*kwargs)

Bases: [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)

A dashed [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line).

* **Parameters:**
  * **args** (*Any*) – Arguments to be passed to [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)
  * **dash_length** (*float*) – The length of each individual dash of the line.
  * **dashed_ratio** (*float*) – The ratio of dash space to empty space. Range of 0-1.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)

#### SEE ALSO
[`DashedVMobject`](manim.mobject.types.vectorized_mobject.DashedVMobject.md#manim.mobject.types.vectorized_mobject.DashedVMobject)

### Examples

### Methods

| [`get_end`](#manim.mobject.geometry.line.DashedLine.get_end)                   | Returns the end point of the line.     |
|--------------------------------------------------------------------------------|----------------------------------------|
| [`get_first_handle`](#manim.mobject.geometry.line.DashedLine.get_first_handle) | Returns the point of the first handle. |
| [`get_last_handle`](#manim.mobject.geometry.line.DashedLine.get_last_handle)   | Returns the point of the last handle.  |
| [`get_start`](#manim.mobject.geometry.line.DashedLine.get_start)               | Returns the start point of the line.   |

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

#### \_calculate_num_dashes()

Returns the number of dashes in the dashed line.

### Examples

```default
>>> DashedLine()._calculate_num_dashes()
20
```

* **Return type:**
  int

#### \_original_\_init_\_(\*args, dash_length=0.05, dashed_ratio=0.5, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **args** (*Any*)
  * **dash_length** (*float*)
  * **dashed_ratio** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### get_end()

Returns the end point of the line.

### Examples

```default
>>> DashedLine().get_end()
array([1., 0., 0.])
```

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_first_handle()

Returns the point of the first handle.

### Examples

```default
>>> DashedLine().get_first_handle()
array([-0.98333333,  0.        ,  0.        ])
```

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_last_handle()

Returns the point of the last handle.

### Examples

```default
>>> DashedLine().get_last_handle()
array([0.98333333, 0.        , 0.        ])
```

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_start()

Returns the start point of the line.

### Examples

```default
>>> DashedLine().get_start()
array([-1.,  0.,  0.])
```

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)
