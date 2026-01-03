# SpiralIn

Qualified name: `manim.animation.creation.SpiralIn`

### *class* SpiralIn(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

Create the Mobject with sub-Mobjects flying in on spiral trajectories.

* **Parameters:**
  * **shapes** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The Mobject on which to be operated.
  * **scale_factor** (*float*) – The factor used for scaling the effect.
  * **fade_in_fraction** – Fractional duration of initial fade-in of sub-Mobjects as they fly inward.

### Examples

### Methods

| [`interpolate_mobject`](#manim.animation.creation.SpiralIn.interpolate_mobject)   | Interpolates the mobject of the `Animation` based on alpha value.   |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------|

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(shapes, scale_factor=8, fade_in_fraction=0.3, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **shapes** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **scale_factor** (*float*)
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
