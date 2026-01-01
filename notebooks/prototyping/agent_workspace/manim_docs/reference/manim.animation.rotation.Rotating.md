# Rotating

Qualified name: `manim.animation.rotation.Rotating`

### *class* Rotating(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

Animation that rotates a Mobject.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to be rotated.
  * **angle** (*float*) – The rotation angle in radians. Predefined constants such as `DEGREES`
    can also be used to specify the angle in degrees.
  * **axis** (*np.ndarray*) – The rotation axis as a numpy vector.
  * **about_point** (*np.ndarray* *|* *None*) – The rotation center.
  * **about_edge** (*np.ndarray* *|* *None*) – If `about_point` is `None`, this argument specifies
    the direction of the bounding box point to be taken as
    the rotation center.
  * **run_time** (*float*) – The duration of the animation in seconds.
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*) – The function defining the animation progress based on the relative
    runtime (see [`rate_functions`](manim.utils.rate_functions.md#module-manim.utils.rate_functions)) .
  * **\*\*kwargs** (*Any*) – Additional keyword arguments passed to [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation).

### Examples

#### SEE ALSO
[`Rotate`](manim.animation.rotation.Rotate.md#manim.animation.rotation.Rotate), [`rotate()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.rotate)

### Methods

| [`interpolate_mobject`](#manim.animation.rotation.Rotating.interpolate_mobject)   | Interpolates the mobject of the `Animation` based on alpha value.   |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------|

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(mobject, angle=6.283185307179586, axis=array([0., 0., 1.]), about_point=None, about_edge=None, run_time=5, rate_func=<function linear>, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **angle** (*float*)
  * **axis** (*np.ndarray*)
  * **about_point** (*np.ndarray* *|* *None*)
  * **about_edge** (*np.ndarray* *|* *None*)
  * **run_time** (*float*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
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
