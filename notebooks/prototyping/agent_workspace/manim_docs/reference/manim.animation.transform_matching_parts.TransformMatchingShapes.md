# TransformMatchingShapes

Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingShapes`

### *class* TransformMatchingShapes(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`TransformMatchingAbstractBase`](manim.animation.transform_matching_parts.TransformMatchingAbstractBase.md#manim.animation.transform_matching_parts.TransformMatchingAbstractBase)

An animation trying to transform groups by matching the shape
of their submobjects.

Two submobjects match if the hash of their point coordinates after
normalization (i.e., after translation to the origin, fixing the submobject
height at 1 unit, and rounding the coordinates to three decimal places)
matches.

#### SEE ALSO
[`TransformMatchingAbstractBase`](manim.animation.transform_matching_parts.TransformMatchingAbstractBase.md#manim.animation.transform_matching_parts.TransformMatchingAbstractBase)

### Examples

### Methods

| `get_mobject_key`   |    |
|---------------------|----|
| `get_mobject_parts` |    |

### Attributes

| `run_time`   |    |
|--------------|----|
* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **transform_mismatches** (*bool*)
  * **fade_transform_mismatches** (*bool*)
  * **key_map** (*dict* *|* *None*)

#### \_original_\_init_\_(mobject, target_mobject, transform_mismatches=False, fade_transform_mismatches=False, key_map=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **target_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **transform_mismatches** (*bool*)
  * **fade_transform_mismatches** (*bool*)
  * **key_map** (*dict* *|* *None*)
