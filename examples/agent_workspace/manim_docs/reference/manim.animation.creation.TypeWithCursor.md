# TypeWithCursor

Qualified name: `manim.animation.creation.TypeWithCursor`

### *class* TypeWithCursor(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`AddTextLetterByLetter`](manim.animation.creation.AddTextLetterByLetter.md#manim.animation.creation.AddTextLetterByLetter)

Similar to [`AddTextLetterByLetter`](manim.animation.creation.AddTextLetterByLetter.md#manim.animation.creation.AddTextLetterByLetter) , but with an additional cursor mobject at the end.

* **Parameters:**
  * **time_per_char** (*float*) – Frequency of appearance of the letters.
  * **cursor** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) shown after the last added letter.
  * **buff** (*float*) – Controls how far away the cursor is to the right of the last added letter.
  * **keep_cursor_y** (*bool*) – If `True`, the cursor’s y-coordinate is set to the center of the `Text` and remains the same throughout the animation. Otherwise, it is set to the center of the last added letter.
  * **leave_cursor_on** (*bool*) – Whether to show the cursor after the animation.
  * **tip::** ( *..*) – This is currently only possible for class:~.Text and not for class:~.MathTex.
  * **text** ([*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text))

### Examples

### Methods

| [`begin`](#manim.animation.creation.TypeWithCursor.begin)                             | Begin the animation.                                                                                      |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`clean_up_from_scene`](#manim.animation.creation.TypeWithCursor.clean_up_from_scene) | Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation. |
| [`finish`](#manim.animation.creation.TypeWithCursor.finish)                           | Finish the animation.                                                                                     |
| `update_submobject_list`                                                              |                                                                                                           |

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(text, cursor, buff=0.1, keep_cursor_y=True, leave_cursor_on=True, time_per_char=0.1, reverse_rate_function=False, introducer=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **text** ([*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text))
  * **cursor** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **buff** (*float*)
  * **keep_cursor_y** (*bool*)
  * **leave_cursor_on** (*bool*)
  * **time_per_char** (*float*)
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

#### finish()

Finish the animation.

This method gets called when the animation is over.

* **Return type:**
  None
