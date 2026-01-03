# mobject

Base classes for objects that can be displayed.

### Type Aliases

### *class* TimeBasedUpdater

```default
Callable[['Mobject', float], object]
```

### *class* NonTimeBasedUpdater

```default
Callable[['Mobject'], object]
```

### *class* Updater

```default
[`NonTimeBasedUpdater`](#manim.mobject.mobject.NonTimeBasedUpdater) | [`TimeBasedUpdater`](#manim.mobject.mobject.TimeBasedUpdater)
```

### Classes

| [`Group`](manim.mobject.mobject.Group.md#manim.mobject.mobject.Group)       | Groups together multiple [`Mobjects`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).   |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) | Mathematical Object: base class for objects that can be displayed on screen.                             |

### Functions

### override_animate(method)

Decorator for overriding method animations.

This allows to specify a method (returning an [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
which is called when the decorated method is used with the `.animate` syntax
for animating the application of a method.

#### SEE ALSO
[`animate`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.animate)

#### NOTE
Overridden methods cannot be combined with normal or other overridden
methods using method chaining with the `.animate` syntax.

### Examples

* **Return type:**
  *LambdaType*
