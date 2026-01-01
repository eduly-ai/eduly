# LogBase

Qualified name: `manim.mobject.graphing.scale.LogBase`

### *class* LogBase(base=10, custom_labels=True)

Bases: `_ScaleBase`

Scale for logarithmic graphs/functions.

* **Parameters:**
  * **base** (*float*) – The base of the log, by default 10.
  * **custom_labels** (*bool*) – For use with [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.md#manim.mobject.graphing.coordinate_systems.Axes):
    Whether or not to include `LaTeX` axis labels, by default True.

### Examples

```python
func = ParametricFunction(lambda x: x, scaling=LogBase(base=2))
```

### Methods

| [`function`](#manim.mobject.graphing.scale.LogBase.function)                   | Scales the value to fit it to a logarithmic scale.\`\`self.function(5)==10\*\*5\`\`                                                 |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [`get_custom_labels`](#manim.mobject.graphing.scale.LogBase.get_custom_labels) | Produces custom [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer) labels in the form of `10^2`. |
| [`inverse_function`](#manim.mobject.graphing.scale.LogBase.inverse_function)   | Inverse of `function`.                                                                                                              |

#### function(value)

Scales the value to fit it to a logarithmic scale.\`\`self.function(5)==10\*\*5\`\`

* **Parameters:**
  **value** (*float*)
* **Return type:**
  float

#### get_custom_labels(val_range, unit_decimal_places=0, \*\*base_config)

Produces custom [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer) labels in the form of `10^2`.

* **Parameters:**
  * **val_range** (*Iterable* *[**float* *]*) – The iterable of values used to create the labels. Determines the exponent.
  * **unit_decimal_places** (*int*) – The number of decimal places to include in the exponent
  * **base_config** (*Any*) – Additional arguments to be passed to [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer).
* **Return type:**
  list[[*Integer*](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer)]

#### inverse_function(value)

Inverse of `function`. The value must be greater than 0

* **Parameters:**
  **value** (*float*)
* **Return type:**
  float
