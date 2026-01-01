# LaggedStart

Qualified name: `manim.animation.composition.LaggedStart`

### *class* LaggedStart(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`AnimationGroup`](manim.animation.composition.AnimationGroup.md#manim.animation.composition.AnimationGroup)

Adjusts the timing of a series of [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) according to `lag_ratio`.

* **Parameters:**
  * **animations** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation)) – Sequence of [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) objects to be played.
  * **lag_ratio** (*float*) – 

    Defines the delay after which the animation is applied to submobjects. A lag_ratio of
    `n.nn` means the next animation will play when `nnn%` of the current animation has played.
    Defaults to 0.05, meaning that the next animation will begin when 5% of the current
    animation has played.

    This does not influence the total runtime of the animation. Instead the runtime
    of individual animations is adjusted so that the complete animation has the defined
    run time.
  * **kwargs** (*Any*)

### Examples

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(\*animations, lag_ratio=0.05, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **animations** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
  * **lag_ratio** (*float*)
  * **kwargs** (*Any*)
