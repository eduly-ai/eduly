# UpdateFromAlphaFunc

Qualified name: `manim.animation.updaters.update.UpdateFromAlphaFunc`

### *class* UpdateFromAlphaFunc(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`UpdateFromFunc`](manim.animation.updaters.update.UpdateFromFunc.md#manim.animation.updaters.update.UpdateFromFunc)

### Methods

| [`interpolate_mobject`](#manim.animation.updaters.update.UpdateFromAlphaFunc.interpolate_mobject)   | Interpolates the mobject of the `Animation` based on alpha value.   |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|

### Attributes

| `run_time`   |    |
|--------------|----|
* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **update_function** (*Callable* *[* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]* *,* *Any* *]*)
  * **suspend_mobject_updating** (*bool*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(mobject, update_function, suspend_mobject_updating=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **update_function** (*Callable* *[* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]* *,* *Any* *]*)
  * **suspend_mobject_updating** (*bool*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### interpolate_mobject(alpha)

Interpolates the mobject of the `Animation` based on alpha value.

* **Parameters:**
  **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
  is completed. For example, alpha-values of 0, 0.5, and 1 correspond
  to the animation being completed 0%, 50%, and 100%, respectively.
* **Return type:**
  None
