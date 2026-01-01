# Wait

Qualified name: `manim.animation.animation.Wait`

### *class* Wait(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

A “no operation” animation.

* **Parameters:**
  * **run_time** (*float*) – The amount of time that should pass.
  * **stop_condition** (*Callable* *[* *[* *]* *,* *bool* *]*  *|* *None*) – A function without positional arguments that evaluates to a boolean.
    The function is evaluated after every new frame has been rendered.
    Playing the animation stops after the return value is truthy, or
    after the specified `run_time` has passed.
  * **frozen_frame** (*bool* *|* *None*) – Controls whether or not the wait animation is static, i.e., corresponds
    to a frozen frame. If `False` is passed, the render loop still
    progresses through the animation as usual and (among other things)
    continues to call updater functions. If `None` (the default value),
    the [`Scene.play()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.play) call tries to determine whether the Wait call
    can be static or not itself via `Scene.should_mobjects_update()`.
  * **kwargs** – Keyword arguments to be passed to the parent class, [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation).
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)

### Methods

| [`begin`](#manim.animation.animation.Wait.begin)                             | Begin the animation.                                                                                      |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`clean_up_from_scene`](#manim.animation.animation.Wait.clean_up_from_scene) | Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation. |
| [`finish`](#manim.animation.animation.Wait.finish)                           | Finish the animation.                                                                                     |
| [`interpolate`](#manim.animation.animation.Wait.interpolate)                 | Set the animation progress.                                                                               |
| [`update_mobjects`](#manim.animation.animation.Wait.update_mobjects)         | Updates things like starting_mobject, and (for Transforms) target_mobject.                                |

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(run_time=1, stop_condition=None, frozen_frame=None, rate_func=<function linear>, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **run_time** (*float*)
  * **stop_condition** (*Callable* *[* *[* *]* *,* *bool* *]*  *|* *None*)
  * **frozen_frame** (*bool* *|* *None*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)

#### begin()

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

* **Return type:**
  None

#### clean_up_from_scene(scene)

Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation.

This includes to [`remove()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.remove) the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) if the animation is a remover.

* **Parameters:**
  **scene** ([*Scene*](manim.scene.scene.Scene.md#manim.scene.scene.Scene)) – The scene the animation should be cleaned up from.
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
