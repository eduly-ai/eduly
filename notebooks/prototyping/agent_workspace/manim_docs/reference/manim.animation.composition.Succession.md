# Succession

Qualified name: `manim.animation.composition.Succession`

### *class* Succession(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`AnimationGroup`](manim.animation.composition.AnimationGroup.md#manim.animation.composition.AnimationGroup)

Plays a series of animations in succession.

* **Parameters:**
  * **animations** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation)) – Sequence of [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) objects to be played.
  * **lag_ratio** (*float*) – 

    Defines the delay after which the animation is applied to submobjects. A lag_ratio of
    `n.nn` means the next animation will play when `nnn%` of the current animation has played.
    Defaults to 1.0, meaning that the next animation will begin when 100% of the current
    animation has played.

    This does not influence the total runtime of the animation. Instead the runtime
    of individual animations is adjusted so that the complete animation has the defined
    run time.
  * **kwargs** (*Any*)

### Examples

### Methods

| [`begin`](#manim.animation.composition.Succession.begin)                     | Begin the animation.                                                       |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [`finish`](#manim.animation.composition.Succession.finish)                   | Finish the animation.                                                      |
| [`interpolate`](#manim.animation.composition.Succession.interpolate)         | Set the animation progress.                                                |
| [`next_animation`](#manim.animation.composition.Succession.next_animation)   | Proceeds to the next animation.                                            |
| `update_active_animation`                                                    |                                                                            |
| [`update_mobjects`](#manim.animation.composition.Succession.update_mobjects) | Updates things like starting_mobject, and (for Transforms) target_mobject. |

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(\*animations, lag_ratio=1, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **animations** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation))
  * **lag_ratio** (*float*)
  * **kwargs** (*Any*)

#### \_setup_scene(scene)

Setup up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) before starting the animation.

This includes to [`add()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.add) the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) if the animation is an introducer.

* **Parameters:**
  **scene** ([*Scene*](manim.scene.scene.Scene.md#manim.scene.scene.Scene) *|* *None*) – The scene the animation should be cleaned up from.
* **Return type:**
  None

#### begin()

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

* **Return type:**
  None

#### finish()

Finish the animation.

This method gets called when the animation is over.

* **Return type:**
  None

#### interpolate(alpha)

Set the animation progress.

This method gets called for every frame during an animation.

* **Parameters:**
  **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
  the end.
* **Return type:**
  None

#### next_animation()

Proceeds to the next animation.

This method is called right when the active animation finishes.

* **Return type:**
  None

#### update_mobjects(dt)

Updates things like starting_mobject, and (for
Transforms) target_mobject.  Note, since typically
(always?) self.mobject will have its updating
suspended during the animation, this will do
nothing to self.mobject.

* **Parameters:**
  **dt** (*float*)
* **Return type:**
  None
