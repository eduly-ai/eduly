# Transform

Qualified name: `manim.animation.transform.Transform`

### *class* Transform(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

A Transform transforms a Mobject into a target Mobject.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *None*) – The [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) to be transformed. It will be mutated to become the `target_mobject`.
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *None*) – The target of the transformation.
  * **path_func** (*Callable* *|* *None*) – A function defining the path that the points of the `mobject` are being moved
    along until they match the points of the `target_mobject`, see [`utils.paths`](manim.utils.paths.md#module-manim.utils.paths).
  * **path_arc** (*float*) – The arc angle (in radians) that the points of `mobject` will follow to reach
    the points of the target if using a circular path arc, see `path_arc_centers`.
    See also [`manim.utils.paths.path_along_arc()`](manim.utils.paths.md#manim.utils.paths.path_along_arc).
  * **path_arc_axis** (*np.ndarray*) – The axis to rotate along if using a circular path arc, see `path_arc_centers`.
  * **path_arc_centers** (*np.ndarray*) – 

    The center of the circular arcs along which the points of `mobject` are
    moved by the transformation.

    If this is set and `path_func` is not set, then a `path_along_circles` path will be generated
    using the `path_arc` parameters and stored in `path_func`. If `path_func` is set, this and the
    other `path_arc` fields are set as attributes, but a `path_func` is not generated from it.
  * **replace_mobject_with_target_in_scene** (*bool*) – 

    Controls which mobject is replaced when the transformation is complete.

    If set to True, `mobject` will be removed from the scene and `target_mobject` will
    replace it. Otherwise, `target_mobject` is never added and `mobject` just takes its shape.

### Examples

#### SEE ALSO
[`ReplacementTransform`](manim.animation.transform.ReplacementTransform.md#manim.animation.transform.ReplacementTransform), [`interpolate()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.interpolate), [`align_data()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.align_data)

### Methods

| [`begin`](#manim.animation.transform.Transform.begin)                             | Begin the animation.                                                                                      |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`clean_up_from_scene`](#manim.animation.transform.Transform.clean_up_from_scene) | Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation. |
| `create_target`                                                                   |                                                                                                           |
| `get_all_families_zipped`                                                         |                                                                                                           |
| [`get_all_mobjects`](#manim.animation.transform.Transform.get_all_mobjects)       | Get all mobjects involved in the animation.                                                               |
| `interpolate_submobject`                                                          |                                                                                                           |

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, target_mobject=None, path_func=None, path_arc=0, path_arc_axis=array([0., 0., 1.]), path_arc_centers=None, replace_mobject_with_target_in_scene=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *None*)
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *None*)
  * **path_func** (*Callable* *|* *None*)
  * **path_arc** (*float*)
  * **path_arc_axis** (*ndarray*)
  * **path_arc_centers** (*ndarray*)
  * **replace_mobject_with_target_in_scene** (*bool*)
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

#### get_all_mobjects()

Get all mobjects involved in the animation.

Ordering must match the ordering of arguments to interpolate_submobject

* **Returns:**
  The sequence of mobjects.
* **Return type:**
  Sequence[[Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)]
