# Scene

Qualified name: `manim.scene.scene.Scene`

### *class* Scene(renderer=None, camera_class=<class 'manim.camera.camera.Camera'>, always_update_mobjects=False, random_seed=None, skip_animations=False)

Bases: `object`

A Scene is the canvas of your animation.

The primary role of [`Scene`](#manim.scene.scene.Scene) is to provide the user with tools to manage
mobjects and animations.  Generally speaking, a manim script consists of a class
that derives from [`Scene`](#manim.scene.scene.Scene) whose [`Scene.construct()`](#manim.scene.scene.Scene.construct) method is overridden
by the user’s code.

Mobjects are displayed on screen by calling [`Scene.add()`](#manim.scene.scene.Scene.add) and removed from
screen by calling [`Scene.remove()`](#manim.scene.scene.Scene.remove).  All mobjects currently on screen are kept
in `Scene.mobjects`.  Animations are played by calling [`Scene.play()`](#manim.scene.scene.Scene.play).

A [`Scene`](#manim.scene.scene.Scene) is rendered internally by calling [`Scene.render()`](#manim.scene.scene.Scene.render).  This in
turn calls [`Scene.setup()`](#manim.scene.scene.Scene.setup), [`Scene.construct()`](#manim.scene.scene.Scene.construct), and
[`Scene.tear_down()`](#manim.scene.scene.Scene.tear_down), in that order.

It is not recommended to override the `__init__` method in user Scenes.  For code
that should be ran before a Scene is rendered, use [`Scene.setup()`](#manim.scene.scene.Scene.setup) instead.

### Examples

Override the [`Scene.construct()`](#manim.scene.scene.Scene.construct) method with your code.

```python
class MyScene(Scene):
    def construct(self):
        self.play(Write(Text("Hello World!")))
```

### Methods

| [`add`](#manim.scene.scene.Scene.add)                                                             | Mobjects will be displayed, from background to foreground in the order with which they are added.                                                             |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`add_foreground_mobject`](#manim.scene.scene.Scene.add_foreground_mobject)                       | Adds a single mobject to the foreground, and internally to the list foreground_mobjects, and mobjects.                                                        |
| [`add_foreground_mobjects`](#manim.scene.scene.Scene.add_foreground_mobjects)                     | Adds mobjects to the foreground, and internally to the list foreground_mobjects, and mobjects.                                                                |
| `add_mobjects_from_animations`                                                                    |                                                                                                                                                               |
| [`add_sound`](#manim.scene.scene.Scene.add_sound)                                                 | This method is used to add a sound to the animation.                                                                                                          |
| [`add_subcaption`](#manim.scene.scene.Scene.add_subcaption)                                       | Adds an entry in the corresponding subcaption file at the current time stamp.                                                                                 |
| [`add_updater`](#manim.scene.scene.Scene.add_updater)                                             | Add an update function to the scene.                                                                                                                          |
| [`begin_animations`](#manim.scene.scene.Scene.begin_animations)                                   | Start the animations of the scene.                                                                                                                            |
| [`bring_to_back`](#manim.scene.scene.Scene.bring_to_back)                                         | Removes the mobject from the scene and adds them to the back of the scene.                                                                                    |
| [`bring_to_front`](#manim.scene.scene.Scene.bring_to_front)                                       | Adds the passed mobjects to the scene again, pushing them to he front of the scene.                                                                           |
| `check_interactive_embed_is_valid`                                                                |                                                                                                                                                               |
| [`clear`](#manim.scene.scene.Scene.clear)                                                         | Removes all mobjects present in self.mobjects and self.foreground_mobjects from the scene.                                                                    |
| [`compile_animation_data`](#manim.scene.scene.Scene.compile_animation_data)                       | Given a list of animations, compile the corresponding static and moving mobjects, and gather the animation durations.                                         |
| [`compile_animations`](#manim.scene.scene.Scene.compile_animations)                               | Creates \_MethodAnimations from any \_AnimationBuilders and updates animation kwargs with kwargs passed to play().                                            |
| [`construct`](#manim.scene.scene.Scene.construct)                                                 | Add content to the Scene.                                                                                                                                     |
| `embed`                                                                                           |                                                                                                                                                               |
| [`get_attrs`](#manim.scene.scene.Scene.get_attrs)                                                 | Gets attributes of a scene given the attribute's identifier/name.                                                                                             |
| [`get_mobject_family_members`](#manim.scene.scene.Scene.get_mobject_family_members)               | Returns list of family-members of all mobjects in scene.                                                                                                      |
| `get_moving_and_static_mobjects`                                                                  |                                                                                                                                                               |
| [`get_moving_mobjects`](#manim.scene.scene.Scene.get_moving_mobjects)                             | Gets all moving mobjects in the passed animation(s).                                                                                                          |
| [`get_restructured_mobject_list`](#manim.scene.scene.Scene.get_restructured_mobject_list)         | Given a list of mobjects and a list of mobjects to be removed, this filters out the removable mobjects from the list of mobjects.                             |
| [`get_run_time`](#manim.scene.scene.Scene.get_run_time)                                           | Gets the total run time for a list of animations.                                                                                                             |
| [`get_time_progression`](#manim.scene.scene.Scene.get_time_progression)                           | You will hardly use this when making your own animations.                                                                                                     |
| [`get_top_level_mobjects`](#manim.scene.scene.Scene.get_top_level_mobjects)                       | Returns all mobjects which are not submobjects.                                                                                                               |
| `interact`                                                                                        |                                                                                                                                                               |
| [`interactive_embed`](#manim.scene.scene.Scene.interactive_embed)                                 | Like embed(), but allows for screen interaction.                                                                                                              |
| [`is_current_animation_frozen_frame`](#manim.scene.scene.Scene.is_current_animation_frozen_frame) | Returns whether the current animation produces a static frame (generally a Wait).                                                                             |
| `mouse_drag_orbit_controls`                                                                       |                                                                                                                                                               |
| `mouse_scroll_orbit_controls`                                                                     |                                                                                                                                                               |
| [`next_section`](#manim.scene.scene.Scene.next_section)                                           | Create separation here; the last section gets finished and a new one gets created.                                                                            |
| `on_key_press`                                                                                    |                                                                                                                                                               |
| `on_key_release`                                                                                  |                                                                                                                                                               |
| `on_mouse_drag`                                                                                   |                                                                                                                                                               |
| `on_mouse_motion`                                                                                 |                                                                                                                                                               |
| `on_mouse_press`                                                                                  |                                                                                                                                                               |
| `on_mouse_scroll`                                                                                 |                                                                                                                                                               |
| [`pause`](#manim.scene.scene.Scene.pause)                                                         | Pauses the scene (i.e., displays a frozen frame).                                                                                                             |
| [`play`](#manim.scene.scene.Scene.play)                                                           | Plays an animation in this scene.                                                                                                                             |
| [`play_internal`](#manim.scene.scene.Scene.play_internal)                                         | This method is used to prep the animations for rendering, apply the arguments and parameters required to them, render them, and write them to the video file. |
| [`remove`](#manim.scene.scene.Scene.remove)                                                       | Removes mobjects in the passed list of mobjects from the scene and the foreground, by removing them from "mobjects" and "foreground_mobjects"                 |
| [`remove_foreground_mobject`](#manim.scene.scene.Scene.remove_foreground_mobject)                 | Removes a single mobject from the foreground, and internally from the list foreground_mobjects.                                                               |
| [`remove_foreground_mobjects`](#manim.scene.scene.Scene.remove_foreground_mobjects)               | Removes mobjects from the foreground, and internally from the list foreground_mobjects.                                                                       |
| [`remove_updater`](#manim.scene.scene.Scene.remove_updater)                                       | Remove an update function from the scene.                                                                                                                     |
| [`render`](#manim.scene.scene.Scene.render)                                                       | Renders this Scene.                                                                                                                                           |
| [`replace`](#manim.scene.scene.Scene.replace)                                                     | Replace one mobject in the scene with another, preserving draw order.                                                                                         |
| [`restructure_mobjects`](#manim.scene.scene.Scene.restructure_mobjects)                           | tl:wr                                                                                                                                                         |
| `set_key_function`                                                                                |                                                                                                                                                               |
| [`setup`](#manim.scene.scene.Scene.setup)                                                         | This is meant to be implemented by any scenes which are commonly subclassed, and have some common setup involved before the construct method is called.       |
| [`should_update_mobjects`](#manim.scene.scene.Scene.should_update_mobjects)                       | Returns True if the mobjects of this scene should be updated.                                                                                                 |
| [`tear_down`](#manim.scene.scene.Scene.tear_down)                                                 | This is meant to be implemented by any scenes which are commonly subclassed, and have some common method to be invoked before the scene ends.                 |
| `update_meshes`                                                                                   |                                                                                                                                                               |
| [`update_mobjects`](#manim.scene.scene.Scene.update_mobjects)                                     | Begins updating all mobjects in the Scene.                                                                                                                    |
| [`update_self`](#manim.scene.scene.Scene.update_self)                                             | Run all scene updater functions.                                                                                                                              |
| `update_to_time`                                                                                  |                                                                                                                                                               |
| `validate_run_time`                                                                               |                                                                                                                                                               |
| [`wait`](#manim.scene.scene.Scene.wait)                                                           | Plays a "no operation" animation.                                                                                                                             |
| [`wait_until`](#manim.scene.scene.Scene.wait_until)                                               | Wait until a condition is satisfied, up to a given maximum duration.                                                                                          |

### Attributes

| `camera`                                |                                        |
|-----------------------------------------|----------------------------------------|
| [`time`](#manim.scene.scene.Scene.time) | The time since the start of the scene. |
* **Parameters:**
  * **renderer** (*CairoRenderer* *|* *OpenGLRenderer* *|* *None*)
  * **camera_class** (*type* *[*[*Camera*](manim.camera.camera.Camera.md#manim.camera.camera.Camera) *]*)
  * **always_update_mobjects** (*bool*)
  * **random_seed** (*int* *|* *None*)
  * **skip_animations** (*bool*)

#### \_get_animation_time_progression(animations, duration)

You will hardly use this when making your own animations.
This method is for Manim’s internal use.

Uses `get_time_progression()` to obtain a
CommandLine ProgressBar whose `fill_time` is
dependent on the qualities of the passed Animation,

* **Parameters:**
  * **animations** (*list* *[*[*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – The list of animations to get
    the time progression for.
  * **duration** (*float*) – duration of wait time
* **Returns:**
  The CommandLine Progress Bar.
* **Return type:**
  time_progression

#### add(\*mobjects)

Mobjects will be displayed, from background to
foreground in the order with which they are added.

* **Parameters:**
  **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *OpenGLMobject*) – Mobjects to add.
* **Returns:**
  The same scene after adding the Mobjects in.
* **Return type:**
  [Scene](#manim.scene.scene.Scene)

#### add_foreground_mobject(mobject)

Adds a single mobject to the foreground, and internally to the list
foreground_mobjects, and mobjects.

* **Parameters:**
  **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The Mobject to add to the foreground.
* **Returns:**
  The Scene, with the foreground mobject added.
* **Return type:**
  [Scene](#manim.scene.scene.Scene)

#### add_foreground_mobjects(\*mobjects)

Adds mobjects to the foreground, and internally to the list
foreground_mobjects, and mobjects.

* **Parameters:**
  **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The Mobjects to add to the foreground.
* **Returns:**
  The Scene, with the foreground mobjects added.
* **Return type:**
  [Scene](#manim.scene.scene.Scene)

#### add_sound(sound_file, time_offset=0, gain=None, \*\*kwargs)

This method is used to add a sound to the animation.

* **Parameters:**
  * **sound_file** (*str*) – The path to the sound file.
  * **time_offset** (*float*) – The offset in the sound file after which
    the sound can be played.
  * **gain** (*float* *|* *None*) – Amplification of the sound.
  * **kwargs** (*Any*)
* **Return type:**
  None

### Examples

Download the resource for the previous example [here](https://github.com/ManimCommunity/manim/blob/main/docs/source/_static/click.wav) .

#### add_subcaption(content, duration=1, offset=0)

Adds an entry in the corresponding subcaption file
at the current time stamp.

The current time stamp is obtained from `Scene.time`.

* **Parameters:**
  * **content** (*str*) – The subcaption content.
  * **duration** (*float*) – The duration (in seconds) for which the subcaption is shown.
  * **offset** (*float*) – This offset (in seconds) is added to the starting time stamp
    of the subcaption.
* **Return type:**
  None

### Examples

This example illustrates both possibilities for adding
subcaptions to Manimations:

```default
class SubcaptionExample(Scene):
    def construct(self):
        square = Square()
        circle = Circle()

        # first option: via the add_subcaption method
        self.add_subcaption("Hello square!", duration=1)
        self.play(Create(square))

        # second option: within the call to Scene.play
        self.play(
            Transform(square, circle), subcaption="The square transforms."
        )
```

#### add_updater(func)

Add an update function to the scene.

The scene updater functions are run every frame,
and they are the last type of updaters to run.

#### WARNING
When using the Cairo renderer, scene updaters that
modify mobjects are not detected in the same way
that mobject updaters are. To be more concrete,
a mobject only modified via a scene updater will
not necessarily be added to the list of *moving
mobjects* and thus might not be updated every frame.

TL;DR: Use mobject updaters to update mobjects.

* **Parameters:**
  **func** (*Callable* *[* *[**float* *]* *,* *None* *]*) – The updater function. It takes a float, which is the
  time difference since the last update (usually equal
  to the frame rate).
* **Return type:**
  None

#### SEE ALSO
[`Scene.remove_updater()`](#manim.scene.scene.Scene.remove_updater), [`Scene.update_self()`](#manim.scene.scene.Scene.update_self)

#### begin_animations()

Start the animations of the scene.

* **Return type:**
  None

#### bring_to_back(\*mobjects)

Removes the mobject from the scene and
adds them to the back of the scene.

* **Parameters:**
  **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject(s) to push to the back of the scene.
* **Returns:**
  The Scene, with the mobjects pushed to the back
  of the scene.
* **Return type:**
  [Scene](#manim.scene.scene.Scene)

#### bring_to_front(\*mobjects)

Adds the passed mobjects to the scene again,
pushing them to he front of the scene.

* **Parameters:**
  **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject(s) to bring to the front of the scene.
* **Returns:**
  The Scene, with the mobjects brought to the front
  of the scene.
* **Return type:**
  [Scene](#manim.scene.scene.Scene)

#### clear()

Removes all mobjects present in self.mobjects
and self.foreground_mobjects from the scene.

* **Returns:**
  The Scene, with all of its mobjects in
  self.mobjects and self.foreground_mobjects
  removed.
* **Return type:**
  [Scene](#manim.scene.scene.Scene)

#### compile_animation_data(\*animations, \*\*play_kwargs)

Given a list of animations, compile the corresponding
static and moving mobjects, and gather the animation durations.

This also begins the animations.

* **Parameters:**
  * **animations** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|*  *\_AnimationBuilder*) – Animation or mobject with mobject method and params
  * **play_kwargs** (*Any*) – Named parameters affecting what was passed in `animations`,
    e.g. `run_time`, `lag_ratio` and so on.
* **Returns:**
  None if there is nothing to play, or self otherwise.
* **Return type:**
  self, None

#### compile_animations(\*args, \*\*kwargs)

Creates \_MethodAnimations from any \_AnimationBuilders and updates animation
kwargs with kwargs passed to play().

* **Parameters:**
  * **\*args** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|*  *\_AnimationBuilder*) – Animations to be played.
  * **\*\*kwargs** (*Any*) – Configuration for the call to play().
* **Returns:**
  Animations to be played.
* **Return type:**
  Tuple[`Animation`]

#### construct()

Add content to the Scene.

From within [`Scene.construct()`](#manim.scene.scene.Scene.construct), display mobjects on screen by calling
[`Scene.add()`](#manim.scene.scene.Scene.add) and remove them from screen by calling [`Scene.remove()`](#manim.scene.scene.Scene.remove).
All mobjects currently on screen are kept in `Scene.mobjects`.  Play
animations by calling [`Scene.play()`](#manim.scene.scene.Scene.play).

### Notes

Initialization code should go in [`Scene.setup()`](#manim.scene.scene.Scene.setup).  Termination code should
go in [`Scene.tear_down()`](#manim.scene.scene.Scene.tear_down).

### Examples

A typical manim script includes a class derived from [`Scene`](#manim.scene.scene.Scene) with an
overridden [`Scene.construct()`](#manim.scene.scene.Scene.construct) method:

```python
class MyScene(Scene):
    def construct(self):
        self.play(Write(Text("Hello World!")))
```

#### SEE ALSO
[`Scene.setup()`](#manim.scene.scene.Scene.setup), [`Scene.render()`](#manim.scene.scene.Scene.render), [`Scene.tear_down()`](#manim.scene.scene.Scene.tear_down)

* **Return type:**
  None

#### get_attrs(\*keys)

Gets attributes of a scene given the attribute’s identifier/name.

* **Parameters:**
  **\*keys** (*str*) – Name(s) of the argument(s) to return the attribute of.
* **Returns:**
  List of attributes of the passed identifiers.
* **Return type:**
  list

#### get_mobject_family_members()

Returns list of family-members of all mobjects in scene.
If a Circle() and a VGroup(Rectangle(),Triangle()) were added,
it returns not only the Circle(), Rectangle() and Triangle(), but
also the VGroup() object.

* **Returns:**
  List of mobject family members.
* **Return type:**
  list

#### get_moving_mobjects(\*animations)

Gets all moving mobjects in the passed animation(s).

* **Parameters:**
  **\*animations** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation)) – The animations to check for moving mobjects.
* **Returns:**
  The list of mobjects that could be moving in
  the Animation(s)
* **Return type:**
  list

#### get_restructured_mobject_list(mobjects, to_remove)

Given a list of mobjects and a list of mobjects to be removed, this
filters out the removable mobjects from the list of mobjects.

* **Parameters:**
  * **mobjects** (*Iterable* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The Mobjects to check.
  * **to_remove** (*Iterable* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The list of mobjects to remove.
* **Returns:**
  The list of mobjects with the mobjects to remove removed.
* **Return type:**
  list

#### get_run_time(animations)

Gets the total run time for a list of animations.

* **Parameters:**
  **animations** (*list* *[*[*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – A list of the animations whose total
  `run_time` is to be calculated.
* **Returns:**
  The total `run_time` of all of the animations in the list.
* **Return type:**
  float

#### get_time_progression(run_time, description, n_iterations=None, override_skip_animations=False)

You will hardly use this when making your own animations.
This method is for Manim’s internal use.

Returns a CommandLine ProgressBar whose `fill_time`
is dependent on the `run_time` of an animation,
the iterations to perform in that animation
and a bool saying whether or not to consider
the skipped animations.

* **Parameters:**
  * **run_time** (*float*) – The `run_time` of the animation.
  * **n_iterations** (*int* *|* *None*) – The number of iterations in the animation.
  * **override_skip_animations** (*bool*) – Whether or not to show skipped animations in the progress bar.
  * **description** (*str*)
* **Returns:**
  The CommandLine Progress Bar.
* **Return type:**
  time_progression

#### get_top_level_mobjects()

Returns all mobjects which are not submobjects.

* **Returns:**
  List of top level mobjects.
* **Return type:**
  list

#### interactive_embed()

Like embed(), but allows for screen interaction.

* **Return type:**
  None

#### is_current_animation_frozen_frame()

Returns whether the current animation produces a static frame (generally a Wait).

* **Return type:**
  bool

#### next_section(name='unnamed', section_type=DefaultSectionType.NORMAL, skip_animations=False)

Create separation here; the last section gets finished and a new one gets created.
`skip_animations` skips the rendering of all animations in this section.
Refer to [the documentation](../tutorials/output_and_config.md) on how to use sections.

* **Parameters:**
  * **name** (*str*)
  * **section_type** (*str*)
  * **skip_animations** (*bool*)
* **Return type:**
  None

#### pause(duration=1.0)

Pauses the scene (i.e., displays a frozen frame).

This is an alias for [`wait()`](#manim.scene.scene.Scene.wait) with `frozen_frame`
set to `True`.

* **Parameters:**
  **duration** (*float*) – The duration of the pause.
* **Return type:**
  None

#### SEE ALSO
[`wait()`](#manim.scene.scene.Scene.wait), [`Wait`](manim.animation.animation.Wait.md#manim.animation.animation.Wait)

#### play(\*args, subcaption=None, subcaption_duration=None, subcaption_offset=0, \*\*kwargs)

Plays an animation in this scene.

* **Parameters:**
  * **args** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *|* [*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|*  *\_AnimationBuilder*) – Animations to be played.
  * **subcaption** (*str* *|* *None*) – The content of the external subcaption that should
    be added during the animation.
  * **subcaption_duration** (*float* *|* *None*) – The duration for which the specified subcaption is
    added. If `None` (the default), the run time of the
    animation is taken.
  * **subcaption_offset** (*float*) – An offset (in seconds) for the start time of the
    added subcaption.
  * **kwargs** (*Any*) – All other keywords are passed to the renderer.
* **Return type:**
  None

#### play_internal(skip_rendering=False)

This method is used to prep the animations for rendering,
apply the arguments and parameters required to them,
render them, and write them to the video file.

* **Parameters:**
  **skip_rendering** (*bool*) – Whether the rendering should be skipped, by default False
* **Return type:**
  None

#### remove(\*mobjects)

Removes mobjects in the passed list of mobjects
from the scene and the foreground, by removing them
from “mobjects” and “foreground_mobjects”

* **Parameters:**
  **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to remove.
* **Return type:**
  Self

#### remove_foreground_mobject(mobject)

Removes a single mobject from the foreground, and internally from the list
foreground_mobjects.

* **Parameters:**
  **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to remove from the foreground.
* **Returns:**
  The Scene, with the foreground mobject removed.
* **Return type:**
  [Scene](#manim.scene.scene.Scene)

#### remove_foreground_mobjects(\*to_remove)

Removes mobjects from the foreground, and internally from the list
foreground_mobjects.

* **Parameters:**
  **\*to_remove** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject(s) to remove from the foreground.
* **Returns:**
  The Scene, with the foreground mobjects removed.
* **Return type:**
  [Scene](#manim.scene.scene.Scene)

#### remove_updater(func)

Remove an update function from the scene.

* **Parameters:**
  **func** (*Callable* *[* *[**float* *]* *,* *None* *]*) – The updater function to be removed.
* **Return type:**
  None

#### SEE ALSO
[`Scene.add_updater()`](#manim.scene.scene.Scene.add_updater), [`Scene.update_self()`](#manim.scene.scene.Scene.update_self)

#### render(preview=False)

Renders this Scene.

* **Parameters:**
  **preview** (*bool*) – If true, opens scene in a file viewer.
* **Return type:**
  bool

#### replace(old_mobject, new_mobject)

Replace one mobject in the scene with another, preserving draw order.

If `old_mobject` is a submobject of some other Mobject (e.g. a
[`Group`](manim.mobject.mobject.Group.md#manim.mobject.mobject.Group)), the new_mobject will replace it inside the group,
without otherwise changing the parent mobject.

* **Parameters:**
  * **old_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to be replaced. Must be present in the scene.
  * **new_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – A mobject which must not already be in the scene.
* **Return type:**
  None

#### restructure_mobjects(to_remove, mobject_list_name='mobjects', extract_families=True)

tl:wr
: If your scene has a Group(), and you removed a mobject from the Group,
  this dissolves the group and puts the rest of the mobjects directly
  in self.mobjects or self.foreground_mobjects.

In cases where the scene contains a group, e.g. Group(m1, m2, m3), but one
of its submobjects is removed, e.g. scene.remove(m1), the list of mobjects
will be edited to contain other submobjects, but not m1, e.g. it will now
insert m2 and m3 to where the group once was.

* **Parameters:**
  * **to_remove** (*Sequence* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The Mobject to remove.
  * **mobject_list_name** (*str*) – The list of mobjects (“mobjects”, “foreground_mobjects” etc) to remove from.
  * **extract_families** (*bool*) – Whether the mobject’s families should be recursively extracted.
* **Returns:**
  The Scene mobject with restructured Mobjects.
* **Return type:**
  [Scene](#manim.scene.scene.Scene)

#### setup()

This is meant to be implemented by any scenes which
are commonly subclassed, and have some common setup
involved before the construct method is called.

* **Return type:**
  None

#### should_update_mobjects()

Returns True if the mobjects of this scene should be updated.

In particular, this checks whether

- the `always_update_mobjects` attribute of [`Scene`](#manim.scene.scene.Scene)
  is set to `True`,
- the [`Scene`](#manim.scene.scene.Scene) itself has time-based updaters attached,
- any mobject in this [`Scene`](#manim.scene.scene.Scene) has time-based updaters attached.

This is only called when a single Wait animation is played.

* **Return type:**
  bool

#### tear_down()

This is meant to be implemented by any scenes which
are commonly subclassed, and have some common method
to be invoked before the scene ends.

* **Return type:**
  None

#### *property* time *: float*

The time since the start of the scene.

#### update_mobjects(dt)

Begins updating all mobjects in the Scene.

* **Parameters:**
  **dt** (*float*) – Change in time between updates. Defaults (mostly) to 1/frames_per_second
* **Return type:**
  None

#### update_self(dt)

Run all scene updater functions.

Among all types of update functions (mobject updaters, mesh updaters,
scene updaters), scene update functions are called last.

* **Parameters:**
  **dt** (*float*) – Scene time since last update.
* **Return type:**
  None

#### SEE ALSO
[`Scene.add_updater()`](#manim.scene.scene.Scene.add_updater), [`Scene.remove_updater()`](#manim.scene.scene.Scene.remove_updater)

#### wait(duration=1.0, stop_condition=None, frozen_frame=None)

Plays a “no operation” animation.

* **Parameters:**
  * **duration** (*float*) – The run time of the animation.
  * **stop_condition** (*Callable* *[* *[* *]* *,* *bool* *]*  *|* *None*) – A function without positional arguments that is evaluated every time
    a frame is rendered. The animation only stops when the return value
    of the function is truthy, or when the time specified in `duration`
    passes.
  * **frozen_frame** (*bool* *|* *None*) – If True, updater functions are not evaluated, and the animation outputs
    a frozen frame. If False, updater functions are called and frames
    are rendered as usual. If None (the default), the scene tries to
    determine whether or not the frame is frozen on its own.
* **Return type:**
  None

#### SEE ALSO
[`Wait`](manim.animation.animation.Wait.md#manim.animation.animation.Wait), `should_mobjects_update()`

#### wait_until(stop_condition, max_time=60)

Wait until a condition is satisfied, up to a given maximum duration.

* **Parameters:**
  * **stop_condition** (*Callable* *[* *[* *]* *,* *bool* *]*) – A function with no arguments that determines whether or not the
    scene should keep waiting.
  * **max_time** (*float*) – The maximum wait time in seconds.
* **Return type:**
  None
