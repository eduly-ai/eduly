# ShowPartial

Qualified name: `manim.animation.creation.ShowPartial`

### *class* ShowPartial(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

Abstract class for Animations that show the VMobject partially.

* **Raises:**
  **TypeError** – If `mobject` is not an instance of [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).
* **Parameters:**
  **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *OpenGLVMobject* *|* *OpenGLSurface* *|* *None*)

#### SEE ALSO
[`Create`](manim.animation.creation.Create.md#manim.animation.creation.Create), [`ShowPassingFlash`](manim.animation.indication.ShowPassingFlash.md#manim.animation.indication.ShowPassingFlash)

### Methods

| `interpolate_submobject`   |    |
|----------------------------|----|

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(mobject, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *OpenGLVMobject* *|* *OpenGLSurface* *|* *None*)
