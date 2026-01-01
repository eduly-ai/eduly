# animation

Animate mobjects.

### Classes

| [`Add`](manim.animation.animation.Add.md#manim.animation.animation.Add)                   | Add Mobjects to a scene, without animating them in any other way.   |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) | An animation.                                                       |
| [`Wait`](manim.animation.animation.Wait.md#manim.animation.animation.Wait)                | A "no operation" animation.                                         |

### Functions

### override_animation(animation_class)

Decorator used to mark methods as overrides for specific [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) types.

Should only be used to decorate methods of classes derived from [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).
`Animation` overrides get inherited to subclasses of the `Mobject` who defined
them. They don’t override subclasses of the `Animation` they override.

#### SEE ALSO
[`add_animation_override()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.add_animation_override)

* **Parameters:**
  **animation_class** (*type* *[*[*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – The animation to be overridden.
* **Returns:**
  The actual decorator. This marks the method as overriding an animation.
* **Return type:**
  Callable[[Callable], Callable]

### Examples

### prepare_animation(anim)

Returns either an unchanged animation, or the animation built
from a passed animation factory.

### Examples

```default
>>> from manim import Square, FadeIn
>>> s = Square()
>>> prepare_animation(FadeIn(s))
FadeIn(Square)
```

```default
>>> prepare_animation(s.animate.scale(2).rotate(42))
_MethodAnimation(Square)
```

```default
>>> prepare_animation(42)
Traceback (most recent call last):
...
TypeError: Object 42 cannot be converted to an animation
```

* **Parameters:**
  **anim** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *|*  *\_AnimationBuilder* *|*  *\_AnimationBuilder*)
* **Return type:**
  [*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation)
