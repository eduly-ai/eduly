# ApplyMatrix

Qualified name: `manim.animation.transform.ApplyMatrix`

### *class* ApplyMatrix(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`ApplyPointwiseFunction`](manim.animation.transform.ApplyPointwiseFunction.md#manim.animation.transform.ApplyPointwiseFunction)

Applies a matrix transform to an mobject.

* **Parameters:**
  * **matrix** (*np.ndarray*) – The transformation matrix.
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject).
  * **about_point** (*np.ndarray*) – The origin point for the transform. Defaults to `ORIGIN`.
  * **kwargs** – Further keyword arguments that are passed to [`ApplyPointwiseFunction`](manim.animation.transform.ApplyPointwiseFunction.md#manim.animation.transform.ApplyPointwiseFunction).

### Examples

### Methods

| `initialize_matrix`   |    |
|-----------------------|----|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(matrix, mobject, about_point=array([0., 0., 0.]), \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **matrix** (*ndarray*)
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **about_point** (*ndarray*)
* **Return type:**
  None
