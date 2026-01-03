# ComplexValueTracker

Qualified name: `manim.mobject.value\_tracker.ComplexValueTracker`

### *class* ComplexValueTracker(value=0, \*\*kwargs)

Bases: [`ValueTracker`](manim.mobject.value_tracker.ValueTracker.md#manim.mobject.value_tracker.ValueTracker)

Tracks a complex-valued parameter.

The value is internally stored as a points array [a, b, 0]. This can be accessed directly
to represent the value geometrically, see the usage example.
When the value is set through `animate`, the value will take a straight path from the
source point to the destination point.

### Examples

### Methods

| [`get_value`](#manim.mobject.value_tracker.ComplexValueTracker.get_value)   | Get the current value of this ComplexValueTracker as a complex number.   |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [`set_value`](#manim.mobject.value_tracker.ComplexValueTracker.set_value)   | Sets a new complex value to the ComplexValueTracker.                     |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.   |
|-----------------------|------------------------------------------------------------|
| `animation_overrides` |                                                            |
| `depth`               | The depth of the mobject.                                  |
| `height`              | The height of the mobject.                                 |
| `width`               | The width of the mobject.                                  |
* **Parameters:**
  * **value** (*float*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(value=0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **value** (*float*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### get_value()

Get the current value of this ComplexValueTracker as a complex number.

* **Return type:**
  complex

#### set_value(value)

Sets a new complex value to the ComplexValueTracker.

* **Parameters:**
  **value** (*complex* *|* *float*)
* **Return type:**
  Self
