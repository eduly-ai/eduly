# LaggedStartMap

Qualified name: `manim.animation.composition.LaggedStartMap`

### *class* LaggedStartMap(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`LaggedStart`](manim.animation.composition.LaggedStart.md#manim.animation.composition.LaggedStart)

Plays a series of [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) while mapping a function to submobjects.

* **Parameters:**
  * **AnimationClass** – [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) to apply to mobject.
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) whose submobjects the animation, and optionally the function,
    are to be applied.
  * **arg_creator** (*Callable* *[* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]* *,* *Iterable* *[**Any* *]* *]*  *|* *None*) – Function which will be applied to [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).
  * **run_time** (*float*) – The duration of the animation in seconds.
  * **animation_class** (*type* *[*[*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*)
  * **kwargs** (*Any*)

### Examples

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(animation_class, mobject, arg_creator=None, run_time=2, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **animation_class** (*type* *[*[*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*)
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **arg_creator** (*Callable* *[* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]* *,* *Iterable* *[**Any* *]* *]*  *|* *None*)
  * **run_time** (*float*)
  * **kwargs** (*Any*)
