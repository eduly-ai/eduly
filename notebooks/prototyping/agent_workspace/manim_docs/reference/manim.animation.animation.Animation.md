# Animation

Qualified name: `manim.animation.animation.Animation`

### *class* Animation(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: `object`

An animation.

Animations have a fixed time span.

* **Parameters:**
  * **mobject** – The mobject to be animated. This is not required for all types of animations.
  * **lag_ratio** – 

    Defines the delay after which the animation is applied to submobjects. This lag
    is relative to the duration of the animation.

    This does not influence the total
    runtime of the animation. Instead the runtime of individual animations is
    adjusted so that the complete animation has the defined run time.
  * **run_time** – The duration of the animation in seconds.
  * **rate_func** – 

    The function defining the animation progress based on the relative runtime (see  [`rate_functions`](manim.utils.rate_functions.md#module-manim.utils.rate_functions)) .

    For example `rate_func(0.5)` is the proportion of the animation that is done
    after half of the animations run time.
  * **reverse_rate_function** – Reverses the rate function of the animation. Setting `reverse_rate_function`
    does not have any effect on `remover` or `introducer`. These need to be
    set explicitly if an introducer-animation should be turned into a remover one
    and vice versa.
  * **name** – The name of the animation. This gets displayed while rendering the animation.
    Defaults to <class-name>(<Mobject-name>).
  * **remover** – Whether the given mobject should be removed from the scene after this animation.
  * **suspend_mobject_updating** – Whether updaters of the mobject should be suspended during the animation.
* **Return type:**
  Self

#### NOTE
In the current implementation of this class, the specified rate function is applied
within [`Animation.interpolate_mobject()`](#manim.animation.animation.Animation.interpolate_mobject) call as part of the call to
`Animation.interpolate_submobject()`. For subclasses of [`Animation`](#manim.animation.animation.Animation)
that are implemented by overriding [`interpolate_mobject()`](#manim.animation.animation.Animation.interpolate_mobject), the rate function
has to be applied manually (e.g., by passing `self.rate_func(alpha)` instead
of just `alpha`).

### Examples

### Methods

| [`begin`](#manim.animation.animation.Animation.begin)                                           | Begin the animation.                                                                                      |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`clean_up_from_scene`](#manim.animation.animation.Animation.clean_up_from_scene)               | Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation. |
| [`copy`](#manim.animation.animation.Animation.copy)                                             | Create a copy of the animation.                                                                           |
| `create_starting_mobject`                                                                       |                                                                                                           |
| [`finish`](#manim.animation.animation.Animation.finish)                                         | Finish the animation.                                                                                     |
| `get_all_families_zipped`                                                                       |                                                                                                           |
| [`get_all_mobjects`](#manim.animation.animation.Animation.get_all_mobjects)                     | Get all mobjects involved in the animation.                                                               |
| [`get_all_mobjects_to_update`](#manim.animation.animation.Animation.get_all_mobjects_to_update) | Get all mobjects to be updated during the animation.                                                      |
| [`get_rate_func`](#manim.animation.animation.Animation.get_rate_func)                           | Get the rate function of the animation.                                                                   |
| [`get_run_time`](#manim.animation.animation.Animation.get_run_time)                             | Get the run time of the animation.                                                                        |
| [`get_sub_alpha`](#manim.animation.animation.Animation.get_sub_alpha)                           | Get the animation progress of any submobjects subanimation.                                               |
| [`interpolate`](#manim.animation.animation.Animation.interpolate)                               | Set the animation progress.                                                                               |
| [`interpolate_mobject`](#manim.animation.animation.Animation.interpolate_mobject)               | Interpolates the mobject of the [`Animation`](#manim.animation.animation.Animation) based on alpha value. |
| `interpolate_submobject`                                                                        |                                                                                                           |
| [`is_introducer`](#manim.animation.animation.Animation.is_introducer)                           | Test if the animation is an introducer.                                                                   |
| [`is_remover`](#manim.animation.animation.Animation.is_remover)                                 | Test if the animation is a remover.                                                                       |
| [`set_default`](#manim.animation.animation.Animation.set_default)                               | Sets the default values of keyword arguments.                                                             |
| [`set_name`](#manim.animation.animation.Animation.set_name)                                     | Set the name of the animation.                                                                            |
| [`set_rate_func`](#manim.animation.animation.Animation.set_rate_func)                           | Set the rate function of the animation.                                                                   |
| [`set_run_time`](#manim.animation.animation.Animation.set_run_time)                             | Set the run time of the animation.                                                                        |
| [`update_mobjects`](#manim.animation.animation.Animation.update_mobjects)                       | Updates things like starting_mobject, and (for Transforms) target_mobject.                                |

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(mobject, lag_ratio=0.0, run_time=1.0, rate_func=<function smooth>, reverse_rate_function=False, name=None, remover=False, suspend_mobject_updating=True, introducer=False, \*, \_on_finish=<function Animation.<lambda>>, use_override=True)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *OpenGLMobject* *|* *None*)
  * **lag_ratio** (*float*)
  * **run_time** (*float*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **reverse_rate_function** (*bool*)
  * **name** (*str*)
  * **remover** (*bool*)
  * **suspend_mobject_updating** (*bool*)
  * **introducer** (*bool*)
  * **\_on_finish** (*Callable* *[* *[* *]* *,* *None* *]*)
  * **use_override** (*bool*)
* **Return type:**
  None

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

#### clean_up_from_scene(scene)

Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation.

This includes to [`remove()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.remove) the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) if the animation is a remover.

* **Parameters:**
  **scene** ([*Scene*](manim.scene.scene.Scene.md#manim.scene.scene.Scene)) – The scene the animation should be cleaned up from.
* **Return type:**
  None

#### copy()

Create a copy of the animation.

* **Returns:**
  A copy of `self`
* **Return type:**
  [Animation](#manim.animation.animation.Animation)

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

#### get_all_mobjects_to_update()

Get all mobjects to be updated during the animation.

* **Returns:**
  The list of mobjects to be updated during the animation.
* **Return type:**
  List[[Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)]

#### get_rate_func()

Get the rate function of the animation.

* **Returns:**
  The rate function of the animation.
* **Return type:**
  Callable[[float], float]

#### get_run_time()

Get the run time of the animation.

* **Returns:**
  The time the animation takes in seconds.
* **Return type:**
  float

#### get_sub_alpha(alpha, index, num_submobjects)

Get the animation progress of any submobjects subanimation.

* **Parameters:**
  * **alpha** (*float*) – The overall animation progress
  * **index** (*int*) – The index of the subanimation.
  * **num_submobjects** (*int*) – The total count of subanimations.
* **Returns:**
  The progress of the subanimation.
* **Return type:**
  float

#### interpolate(alpha)

Set the animation progress.

This method gets called for every frame during an animation.

* **Parameters:**
  **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
  the end.
* **Return type:**
  None

#### interpolate_mobject(alpha)

Interpolates the mobject of the [`Animation`](#manim.animation.animation.Animation) based on alpha value.

* **Parameters:**
  **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
  is completed. For example, alpha-values of 0, 0.5, and 1 correspond
  to the animation being completed 0%, 50%, and 100%, respectively.
* **Return type:**
  None

#### is_introducer()

Test if the animation is an introducer.

* **Returns:**
  `True` if the animation is an introducer, `False` otherwise.
* **Return type:**
  bool

#### is_remover()

Test if the animation is a remover.

* **Returns:**
  `True` if the animation is a remover, `False` otherwise.
* **Return type:**
  bool

#### *classmethod* set_default(\*\*kwargs)

Sets the default values of keyword arguments.

If this method is called without any additional keyword
arguments, the original default values of the initialization
method of this class are restored.

* **Parameters:**
  **kwargs** – Passing any keyword argument will update the default
  values of the keyword arguments of the initialization
  function of this class.
* **Return type:**
  None

### Examples

#### set_name(name)

Set the name of the animation.

* **Parameters:**
  **name** (*str*) – The new name of the animation.
* **Returns:**
  `self`
* **Return type:**
  [Animation](#manim.animation.animation.Animation)

#### set_rate_func(rate_func)

Set the rate function of the animation.

* **Parameters:**
  **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*) – The new function defining the animation progress based on the
  relative runtime (see [`rate_functions`](manim.utils.rate_functions.md#module-manim.utils.rate_functions)).
* **Returns:**
  `self`
* **Return type:**
  [Animation](#manim.animation.animation.Animation)

#### set_run_time(run_time)

Set the run time of the animation.

* **Parameters:**
  * **run_time** (*float*) – The new time the animation should take in seconds.
  * **note::** ( *..*) – The run_time of an animation should not be changed while it is already
    running.
* **Returns:**
  `self`
* **Return type:**
  [Animation](#manim.animation.animation.Animation)

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
