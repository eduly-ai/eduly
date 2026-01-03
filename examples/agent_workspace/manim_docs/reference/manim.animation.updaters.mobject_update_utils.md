# mobject_update_utils

Utility functions for continuous animation of mobjects.

### Functions

### always(method, \*args, \*\*kwargs)

* **Parameters:**
  **method** (*Callable*)
* **Return type:**
  [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### always_redraw(func)

Redraw the mobject constructed by a function every frame.

This function returns a mobject with an attached updater that
continuously regenerates the mobject according to the
specified function.

* **Parameters:**
  **func** (*Callable* *[* *[* *]* *,* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – A function without (required) input arguments that returns
  a mobject.
* **Return type:**
  [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### Examples

### always_rotate(mobject, rate=0.3490658503988659, \*\*kwargs)

A mobject which is continuously rotated at a certain rate.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to be rotated.
  * **rate** (*float*) – The angle which the mobject is rotated by
    over one second.
  * **kwags** – Further arguments to be passed to [`Mobject.rotate()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.rotate).
* **Return type:**
  [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### Examples

### always_shift(mobject, direction=array([1., 0., 0.]), rate=0.1)

A mobject which is continuously shifted along some direction
at a certain rate.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to shift.
  * **direction** (*ndarray* *[**float64* *]*) – The direction to shift. The vector is normalized, the specified magnitude
    is not relevant.
  * **rate** (*float*) – Length in Manim units which the mobject travels in one
    second along the specified direction.
* **Return type:**
  [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### Examples

### assert_is_mobject_method(method)

* **Parameters:**
  **method** (*Callable*)
* **Return type:**
  None

### cycle_animation(animation, \*\*kwargs)

* **Parameters:**
  **animation** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
* **Return type:**
  [Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### f_always(method, \*arg_generators, \*\*kwargs)

More functional version of always, where instead
of taking in args, it takes in functions which output
the relevant arguments.

* **Parameters:**
  **method** (*Callable* *[* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]* *,* *None* *]*)
* **Return type:**
  [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### turn_animation_into_updater(animation, cycle=False, delay=0, \*\*kwargs)

Add an updater to the animation’s mobject which applies
the interpolation and update functions of the animation

If cycle is True, this repeats over and over.  Otherwise,
the updater will be popped upon completion

The `delay` parameter is the delay (in seconds) before the animation starts..

### Examples

* **Parameters:**
  * **animation** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
  * **cycle** (*bool*)
  * **delay** (*float*)
* **Return type:**
  [Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)
