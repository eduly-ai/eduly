# Write

Qualified name: `manim.animation.creation.Write`

### *class* Write(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`DrawBorderThenFill`](manim.animation.creation.DrawBorderThenFill.md#manim.animation.creation.DrawBorderThenFill)

Simulate hand-writing a [`Text`](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) or hand-drawing a [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).

### Examples

### Tests

Check that creating empty [`Write`](#manim.animation.creation.Write) animations works:

```default
>>> from manim import Write, Text
>>> Write(Text(''))
Write(Text(''))
```

### Methods

| [`begin`](#manim.animation.creation.Write.begin)   | Begin the animation.   |
|----------------------------------------------------|------------------------|
| [`finish`](#manim.animation.creation.Write.finish) | Finish the animation.  |
| `reverse_submobjects`                              |                        |

### Attributes

| `run_time`   |    |
|--------------|----|
* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *OpenGLVMobject*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **reverse** (*bool*)

#### \_original_\_init_\_(vmobject, rate_func=<function linear>, reverse=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *OpenGLVMobject*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **reverse** (*bool*)
* **Return type:**
  None

#### begin()

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

* **Return type:**
  None

#### finish()

Finish the animation.

This method gets called when the animation is over.

* **Return type:**
  None
