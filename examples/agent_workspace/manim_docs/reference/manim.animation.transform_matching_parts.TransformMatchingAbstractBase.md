# TransformMatchingAbstractBase

Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingAbstractBase`

### *class* TransformMatchingAbstractBase(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`AnimationGroup`](manim.animation.composition.AnimationGroup.md#manim.animation.composition.AnimationGroup)

Abstract base class for transformations that keep track of matching parts.

Subclasses have to implement the two static methods
`get_mobject_parts()` and
`get_mobject_key()`.

Basically, this transformation first maps all submobjects returned
by the `get_mobject_parts` method to certain keys by applying the
`get_mobject_key` method. Then, submobjects with matching keys
are transformed into each other.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The starting [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The target [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).
  * **transform_mismatches** (*bool*) – Controls whether submobjects without a matching key are transformed
    into each other by using [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform). Default: `False`.
  * **fade_transform_mismatches** (*bool*) – Controls whether submobjects without a matching key are transformed
    into each other by using [`FadeTransform`](manim.animation.transform.FadeTransform.md#manim.animation.transform.FadeTransform). Default: `False`.
  * **key_map** (*dict* *|* *None*) – Optional. A dictionary mapping keys belonging to some of the starting mobject’s
    submobjects (i.e., the return values of the `get_mobject_key` method)
    to some keys belonging to the target mobject’s submobjects that should
    be transformed although the keys don’t match.
  * **kwargs** – All further keyword arguments are passed to the submobject transformations.

#### NOTE
If neither `transform_mismatches` nor `fade_transform_mismatches`
are set to `True`, submobjects without matching keys in the starting
mobject are faded out in the direction of the unmatched submobjects in
the target mobject, and unmatched submobjects in the target mobject
are faded in from the direction of the unmatched submobjects in the
start mobject.

### Methods

| [`clean_up_from_scene`](#manim.animation.transform_matching_parts.TransformMatchingAbstractBase.clean_up_from_scene)   | Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation.   |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `get_mobject_key`                                                                                                      |                                                                                                             |
| `get_mobject_parts`                                                                                                    |                                                                                                             |
| `get_shape_map`                                                                                                        |                                                                                                             |

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(mobject, target_mobject, transform_mismatches=False, fade_transform_mismatches=False, key_map=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **transform_mismatches** (*bool*)
  * **fade_transform_mismatches** (*bool*)
  * **key_map** (*dict* *|* *None*)

#### clean_up_from_scene(scene)

Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation.

This includes to [`remove()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.remove) the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) if the animation is a remover.

* **Parameters:**
  **scene** ([*Scene*](manim.scene.scene.Scene.md#manim.scene.scene.Scene)) – The scene the animation should be cleaned up from.
* **Return type:**
  None
