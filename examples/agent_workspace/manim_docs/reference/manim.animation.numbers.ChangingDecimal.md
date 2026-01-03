# ChangingDecimal

Qualified name: `manim.animation.numbers.ChangingDecimal`

### *class* ChangingDecimal(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

Animate a [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) to values specified by a user-supplied function.

* **Parameters:**
  * **decimal_mob** ([*DecimalNumber*](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber)) – The [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) instance to animate.
  * **number_update_func** (*Callable* *[* *[**float* *]* *,* *float* *]*) – A function that returns the number to display at each point in the animation.
  * **suspend_mobject_updating** (*bool*) – If `True`, the mobject is not updated outside this animation.
  * **kwargs** (*Any*)
* **Raises:**
  **TypeError** – If `decimal_mob` is not an instance of [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber).

### Examples

### Methods

| `check_validity_of_input`                                                             |                                                                   |
|---------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [`interpolate_mobject`](#manim.animation.numbers.ChangingDecimal.interpolate_mobject) | Interpolates the mobject of the `Animation` based on alpha value. |

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(decimal_mob, number_update_func, suspend_mobject_updating=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **decimal_mob** ([*DecimalNumber*](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber))
  * **number_update_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
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
