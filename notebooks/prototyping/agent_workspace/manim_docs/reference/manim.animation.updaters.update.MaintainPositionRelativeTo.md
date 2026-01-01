# MaintainPositionRelativeTo

Qualified name: `manim.animation.updaters.update.MaintainPositionRelativeTo`

### *class* MaintainPositionRelativeTo(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

### Methods

| [`interpolate_mobject`](#manim.animation.updaters.update.MaintainPositionRelativeTo.interpolate_mobject)   | Interpolates the mobject of the `Animation` based on alpha value.   |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|

### Attributes

| `run_time`   |    |
|--------------|----|
* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **tracked_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **kwargs** (*Any*)

#### \_original_\_init_\_(mobject, tracked_mobject, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **tracked_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
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
