# ShowIncreasingSubsets

Qualified name: `manim.animation.creation.ShowIncreasingSubsets`

### *class* ShowIncreasingSubsets(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

Show one submobject at a time, leaving all previous ones displayed on screen.

### Examples

### Methods

| [`interpolate_mobject`](#manim.animation.creation.ShowIncreasingSubsets.interpolate_mobject)   | Interpolates the mobject of the `Animation` based on alpha value.   |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| `update_submobject_list`                                                                       |                                                                     |

### Attributes

| `run_time`   |    |
|--------------|----|
* **Parameters:**
  * **group** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **suspend_mobject_updating** (*bool*)
  * **int_func** (*Callable* *[* *[**np.ndarray* *]* *,* *np.ndarray* *]*)

#### \_original_\_init_\_(group, suspend_mobject_updating=False, int_func=<ufunc 'floor'>, reverse_rate_function=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **group** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **suspend_mobject_updating** (*bool*)
  * **int_func** (*Callable* *[* *[**ndarray* *]* *,* *ndarray* *]*)
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
