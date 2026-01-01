# ApplyWave

Qualified name: `manim.animation.indication.ApplyWave`

### *class* ApplyWave(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Homotopy`](manim.animation.movement.Homotopy.md#manim.animation.movement.Homotopy)

Send a wave through the Mobject distorting it temporarily.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to be distorted.
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The direction in which the wave nudges points of the shape
  * **amplitude** (*float*) – The distance points of the shape get shifted
  * **wave_func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction)) – The function defining the shape of one wave flank.
  * **time_width** (*float*) – The length of the wave relative to the width of the mobject.
  * **ripples** (*int*) – The number of ripples of the wave
  * **run_time** (*float*) – The duration of the animation.
  * **kwargs** (*Any*)

### Examples

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(mobject, direction=array([0., 1., 0.]), amplitude=0.2, wave_func=<function smooth>, time_width=1, ripples=1, run_time=2, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **amplitude** (*float*)
  * **wave_func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
  * **time_width** (*float*)
  * **ripples** (*int*)
  * **run_time** (*float*)
  * **kwargs** (*Any*)
