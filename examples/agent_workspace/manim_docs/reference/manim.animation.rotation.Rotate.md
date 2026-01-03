# Rotate

Qualified name: `manim.animation.rotation.Rotate`

### *class* Rotate(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Animation that rotates a Mobject.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to be rotated.
  * **angle** (*float*) – The rotation angle.
  * **axis** (*np.ndarray*) – The rotation axis as a numpy vector.
  * **about_point** (*Sequence* *[**float* *]*  *|* *None*) – The rotation center.
  * **about_edge** (*Sequence* *[**float* *]*  *|* *None*) – If `about_point` is `None`, this argument specifies
    the direction of the bounding box point to be taken as
    the rotation center.
  * **kwargs** (*Any*)

### Examples

#### SEE ALSO
[`Rotating`](manim.animation.rotation.Rotating.md#manim.animation.rotation.Rotating), [`rotate()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.rotate)

### Methods

| `create_target`   |    |
|-------------------|----|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(mobject, angle=3.141592653589793, axis=array([0., 0., 1.]), about_point=None, about_edge=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **angle** (*float*)
  * **axis** (*np.ndarray*)
  * **about_point** (*Sequence* *[**float* *]*  *|* *None*)
  * **about_edge** (*Sequence* *[**float* *]*  *|* *None*)
  * **kwargs** (*Any*)
* **Return type:**
  None
