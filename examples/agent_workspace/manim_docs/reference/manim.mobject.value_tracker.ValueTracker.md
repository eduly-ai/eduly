# ValueTracker

Qualified name: `manim.mobject.value\_tracker.ValueTracker`

### *class* ValueTracker(value=0, \*\*kwargs)

Bases: [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

A mobject that can be used for tracking (real-valued) parameters.
Useful for animating parameter changes.

Not meant to be displayed.  Instead the position encodes some
number, often one which another animation or continual_animation
uses for its update function, and by treating it as a mobject it can
still be animated and manipulated just like anything else.

This value changes continuously when animated using the `animate` syntax.

### Examples

#### NOTE
You can also link ValueTrackers to updaters. In this case, you have to make sure that the
ValueTracker is added to the scene by `add`

### Methods

| [`get_value`](#manim.mobject.value_tracker.ValueTracker.get_value)             | Get the current value of this ValueTracker.                           |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [`increment_value`](#manim.mobject.value_tracker.ValueTracker.increment_value) | Increments (adds) a scalar value to the ValueTracker.                 |
| [`interpolate`](#manim.mobject.value_tracker.ValueTracker.interpolate)         | Turns `self` into an interpolation between `mobject1` and `mobject2`. |
| [`set_value`](#manim.mobject.value_tracker.ValueTracker.set_value)             | Sets a new scalar value to the ValueTracker.                          |

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

Get the current value of this ValueTracker.

* **Return type:**
  float

#### increment_value(d_value)

Increments (adds) a scalar value to the ValueTracker.

* **Parameters:**
  **d_value** (*float*)
* **Return type:**
  Self

#### interpolate(mobject1, mobject2, alpha, path_func=<function interpolate>)

Turns `self` into an interpolation between `mobject1` and `mobject2`.

* **Parameters:**
  * **mobject1** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **mobject2** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **alpha** (*float*)
  * **path_func** ([*PathFuncType*](manim.typing.md#manim.typing.PathFuncType))
* **Return type:**
  Self

#### set_value(value)

Sets a new scalar value to the ValueTracker.

* **Parameters:**
  **value** (*float*)
* **Return type:**
  Self
