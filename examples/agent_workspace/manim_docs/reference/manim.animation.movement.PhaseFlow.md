# PhaseFlow

Qualified name: `manim.animation.movement.PhaseFlow`

### *class* PhaseFlow(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

### Methods

| [`interpolate_mobject`](#manim.animation.movement.PhaseFlow.interpolate_mobject)   | Interpolates the mobject of the `Animation` based on alpha value.   |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------|

### Attributes

| `run_time`   |    |
|--------------|----|
* **Parameters:**
  * **function** (*Callable* *[* *[**np.ndarray* *]* *,* *np.ndarray* *]*)
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **virtual_time** (*float*)
  * **suspend_mobject_updating** (*bool*)
  * **rate_func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
  * **kwargs** (*Any*)

#### \_original_\_init_\_(function, mobject, virtual_time=1, suspend_mobject_updating=False, rate_func=<function linear>, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **function** (*Callable* *[* *[**np.ndarray* *]* *,* *np.ndarray* *]*)
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **virtual_time** (*float*)
  * **suspend_mobject_updating** (*bool*)
  * **rate_func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
  * **kwargs** (*Any*)

#### interpolate_mobject(alpha)

Interpolates the mobject of the `Animation` based on alpha value.

* **Parameters:**
  **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
  is completed. For example, alpha-values of 0, 0.5, and 1 correspond
  to the animation being completed 0%, 50%, and 100%, respectively.
* **Return type:**
  None
