# UntypeWithCursor

Qualified name: `manim.animation.creation.UntypeWithCursor`

### *class* UntypeWithCursor(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`TypeWithCursor`](manim.animation.creation.TypeWithCursor.md#manim.animation.creation.TypeWithCursor)

Similar to [`RemoveTextLetterByLetter`](manim.animation.creation.RemoveTextLetterByLetter.md#manim.animation.creation.RemoveTextLetterByLetter) , but with an additional cursor mobject at the end.

* **Parameters:**
  * **time_per_char** (*float*) – Frequency of appearance of the letters.
  * **cursor** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *None*) – [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) shown after the last added letter.
  * **buff** – Controls how far away the cursor is to the right of the last added letter.
  * **keep_cursor_y** – If `True`, the cursor’s y-coordinate is set to the center of the `Text` and remains the same throughout the animation. Otherwise, it is set to the center of the last added letter.
  * **leave_cursor_on** – Whether to show the cursor after the animation.
  * **tip::** ( *..*) – This is currently only possible for class:~.Text and not for class:~.MathTex.
  * **text** ([*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text))

### Examples

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(text, cursor=None, time_per_char=0.1, reverse_rate_function=True, introducer=False, remover=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **text** ([*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text))
  * **cursor** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *None*)
  * **time_per_char** (*float*)
* **Return type:**
  None
