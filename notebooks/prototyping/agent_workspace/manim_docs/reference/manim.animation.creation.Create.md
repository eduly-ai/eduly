# Create

Qualified name: `manim.animation.creation.Create`

### *class* Create(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`ShowPartial`](manim.animation.creation.ShowPartial.md#manim.animation.creation.ShowPartial)

Incrementally show a VMobject.

* **Parameters:**
  * **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *OpenGLVMobject* *|* *OpenGLSurface*) – The VMobject to animate.
  * **lag_ratio** (*float*)
  * **introducer** (*bool*)
* **Raises:**
  **TypeError** – If `mobject` is not an instance of [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).

### Examples

#### SEE ALSO
[`ShowPassingFlash`](manim.animation.indication.ShowPassingFlash.md#manim.animation.indication.ShowPassingFlash)

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(mobject, lag_ratio=1.0, introducer=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *OpenGLVMobject* *|* *OpenGLSurface*)
  * **lag_ratio** (*float*)
  * **introducer** (*bool*)
* **Return type:**
  None
