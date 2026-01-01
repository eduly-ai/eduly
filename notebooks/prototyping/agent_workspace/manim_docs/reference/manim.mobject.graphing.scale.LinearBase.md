# LinearBase

Qualified name: `manim.mobject.graphing.scale.LinearBase`

### *class* LinearBase(scale_factor=1.0)

Bases: `_ScaleBase`

The default scaling class.

* **Parameters:**
  **scale_factor** (*float*) – The slope of the linear function, by default 1.0

### Methods

| [`function`](#manim.mobject.graphing.scale.LinearBase.function)                 | Multiplies the value by the scale factor.   |
|---------------------------------------------------------------------------------|---------------------------------------------|
| [`inverse_function`](#manim.mobject.graphing.scale.LinearBase.inverse_function) | Inverse of function.                        |

#### function(value)

Multiplies the value by the scale factor.

* **Parameters:**
  **value** (*float*) – Value to be multiplied by the scale factor.
* **Return type:**
  float

#### inverse_function(value)

Inverse of function. Divides the value by the scale factor.

* **Parameters:**
  **value** (*float*) – value to be divided by the scale factor.
* **Return type:**
  float
