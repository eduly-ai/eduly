# MoveToTarget

Qualified name: `manim.animation.transform.MoveToTarget`

### *class* MoveToTarget(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform)

Transforms a mobject to the mobject stored in its `target` attribute.

After calling the `generate_target()` method, the `target`
attribute of the mobject is populated with a copy of it. After modifying the attribute,
playing the [`MoveToTarget`](#manim.animation.transform.MoveToTarget) animation transforms the original mobject
into the modified one stored in the `target` attribute.

### Examples

### Methods

| `check_validity_of_input`   |    |
|-----------------------------|----|

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |
* **Parameters:**
  **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))

#### \_original_\_init_\_(mobject, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
* **Return type:**
  None
