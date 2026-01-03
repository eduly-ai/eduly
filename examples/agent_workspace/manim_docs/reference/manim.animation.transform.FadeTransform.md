# FadeTransform

Qualified name: `manim.animation.transform.FadeTransform`

### *class* FadeTransform(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Fades one mobject into another.

* **Parameters:**
  * **mobject** – The starting [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).
  * **target_mobject** – The target [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).
  * **stretch** – Controls whether the target [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) is stretched during
    the animation. Default: `True`.
  * **dim_to_match** – If the target mobject is not stretched automatically, this allows
    to adjust the initial scale of the target [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) while
    it is shifted in. Setting this to 0, 1, and 2, respectively,
    matches the length of the target with the length of the starting
    [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) in x, y, and z direction, respectively.
  * **kwargs** – Further keyword arguments are passed to the parent class.

### Examples

### Methods

| [`begin`](#manim.animation.transform.FadeTransform.begin)                             | Initial setup for the animation.                                                                          |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`clean_up_from_scene`](#manim.animation.transform.FadeTransform.clean_up_from_scene) | Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation. |
| `get_all_families_zipped`                                                             |                                                                                                           |
| [`get_all_mobjects`](#manim.animation.transform.FadeTransform.get_all_mobjects)       | Get all mobjects involved in the animation.                                                               |
| [`ghost_to`](#manim.animation.transform.FadeTransform.ghost_to)                       | Replaces the source by the target and sets the opacity to 0.                                              |

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, target_mobject, stretch=True, dim_to_match=1, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

#### begin()

Initial setup for the animation.

The mobject to which this animation is bound is a group consisting of
both the starting and the ending mobject. At the start, the ending
mobject replaces the starting mobject (and is completely faded). In the
end, it is set to be the other way around.

#### clean_up_from_scene(scene)

Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation.

This includes to [`remove()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.remove) the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) if the animation is a remover.

* **Parameters:**
  **scene** – The scene the animation should be cleaned up from.

#### get_all_mobjects()

Get all mobjects involved in the animation.

Ordering must match the ordering of arguments to interpolate_submobject

* **Returns:**
  The sequence of mobjects.
* **Return type:**
  Sequence[[Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)]

#### ghost_to(source, target)

Replaces the source by the target and sets the opacity to 0.

If the provided target has no points, and thus a location of [0, 0, 0]
the source will simply fade out where it currently is.
