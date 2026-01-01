# RemoveTextLetterByLetter

Qualified name: `manim.animation.creation.RemoveTextLetterByLetter`

### *class* RemoveTextLetterByLetter(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`AddTextLetterByLetter`](manim.animation.creation.AddTextLetterByLetter.md#manim.animation.creation.AddTextLetterByLetter)

Remove a [`Text`](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) letter by letter from the scene.

* **Parameters:**
  * **time_per_char** (*float*) – Frequency of appearance of the letters.
  * **tip::** ( *..*) – This is currently only possible for class:~.Text and not for class:~.MathTex
  * **text** ([*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text))
  * **suspend_mobject_updating** (*bool*)
  * **int_func** (*Callable* *[* *[**np.ndarray* *]* *,* *np.ndarray* *]*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **run_time** (*float* *|* *None*)

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(text, suspend_mobject_updating=False, int_func=<ufunc 'ceil'>, rate_func=<function linear>, time_per_char=0.1, run_time=None, reverse_rate_function=True, introducer=False, remover=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **text** ([*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text))
  * **suspend_mobject_updating** (*bool*)
  * **int_func** (*Callable* *[* *[**np.ndarray* *]* *,* *np.ndarray* *]*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **time_per_char** (*float*)
  * **run_time** (*float* *|* *None*)
* **Return type:**
  None
