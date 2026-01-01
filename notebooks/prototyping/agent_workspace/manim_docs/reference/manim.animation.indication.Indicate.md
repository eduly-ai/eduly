# Indicate

Qualified name: `manim.animation.indication.Indicate`

### *class* Indicate(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Indicate a Mobject by temporarily resizing and recoloring it.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to indicate.
  * **scale_factor** (*float*) – The factor by which the mobject will be temporally scaled
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The color the mobject temporally takes.
  * **rate_func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction)) – The function defining the animation progress at every point in time.
  * **kwargs** (*Any*) – Additional arguments to be passed to the [`Succession`](manim.animation.composition.Succession.md#manim.animation.composition.Succession) constructor

### Examples

### Methods

| `create_target`   |    |
|-------------------|----|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, scale_factor=1.2, color=ManimColor('#FFFF00'), rate_func=<function there_and_back>, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **scale_factor** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **rate_func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
  * **kwargs** (*Any*)
