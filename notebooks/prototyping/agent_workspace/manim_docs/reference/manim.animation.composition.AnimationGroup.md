# AnimationGroup

Qualified name: `manim.animation.composition.AnimationGroup`

### *class* AnimationGroup(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

Plays a group or series of [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation).

* **Parameters:**
  * **animations** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *|* *Iterable* *[*[*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – Sequence of [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation) objects to be played.
  * **group** ([*Group*](manim.mobject.mobject.Group.md#manim.mobject.mobject.Group) *|* [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) *|* *OpenGLGroup* *|* *OpenGLVGroup* *|* *None*) – A group of multiple [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).
  * **run_time** (*float* *|* *None*) – The duration of the animation in seconds.
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*) – The function defining the animation progress based on the relative
    runtime (see [`rate_functions`](manim.utils.rate_functions.md#module-manim.utils.rate_functions)) .
  * **lag_ratio** (*float*) – 

    Defines the delay after which the animation is applied to submobjects. A lag_ratio of
    `n.nn` means the next animation will play when `nnn%` of the current animation has played.
    Defaults to 0.0, meaning that all animations will be played together.

    This does not influence the total runtime of the animation. Instead the runtime
    of individual animations is adjusted so that the complete animation has the defined
    run time.
  * **kwargs** (*Any*)

### Methods

| [`begin`](#manim.animation.composition.AnimationGroup.begin)                                                 | Begin the animation.                                                                                      |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`build_animations_with_timings`](#manim.animation.composition.AnimationGroup.build_animations_with_timings) | Creates a list of triplets of the form (anim, start_time, end_time).                                      |
| [`clean_up_from_scene`](#manim.animation.composition.AnimationGroup.clean_up_from_scene)                     | Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation. |
| [`finish`](#manim.animation.composition.AnimationGroup.finish)                                               | Finish the animation.                                                                                     |
| [`get_all_mobjects`](#manim.animation.composition.AnimationGroup.get_all_mobjects)                           | Get all mobjects involved in the animation.                                                               |
| [`init_run_time`](#manim.animation.composition.AnimationGroup.init_run_time)                                 | Calculates the run time of the animation, if different from `run_time`.                                   |
| [`interpolate`](#manim.animation.composition.AnimationGroup.interpolate)                                     | Set the animation progress.                                                                               |
| [`update_mobjects`](#manim.animation.composition.AnimationGroup.update_mobjects)                             | Updates things like starting_mobject, and (for Transforms) target_mobject.                                |

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(\*animations, group=None, run_time=None, rate_func=<function linear>, lag_ratio=0, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **animations** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *|* *Iterable* *[*[*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*)
  * **group** ([*Group*](manim.mobject.mobject.Group.md#manim.mobject.mobject.Group) *|* [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) *|* *OpenGLGroup* *|* *OpenGLVGroup* *|* *None*)
  * **run_time** (*float* *|* *None*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **lag_ratio** (*float*)
  * **kwargs** (*Any*)

#### \_setup_scene(scene)

Setup up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) before starting the animation.

This includes to [`add()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.add) the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) if the animation is an introducer.

* **Parameters:**
  **scene** ([*Scene*](manim.scene.scene.Scene.md#manim.scene.scene.Scene)) – The scene the animation should be cleaned up from.
* **Return type:**
  None

#### begin()

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

* **Return type:**
  None

#### build_animations_with_timings()

Creates a list of triplets of the form (anim, start_time, end_time).

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

#### get_all_mobjects()

Get all mobjects involved in the animation.

Ordering must match the ordering of arguments to interpolate_submobject

* **Returns:**
  The sequence of mobjects.
* **Return type:**
  Sequence[[Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)]

#### init_run_time(run_time)

Calculates the run time of the animation, if different from `run_time`.

* **Parameters:**
  **run_time** (*float* *|* *None*) – The duration of the animation in seconds.
* **Returns:**
  The duration of the animation in seconds.
* **Return type:**
  run_time

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
