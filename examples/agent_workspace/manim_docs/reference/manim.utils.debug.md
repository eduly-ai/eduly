# debug

Debugging utilities.

### Functions

### index_labels(mobject, label_height=0.15, background_stroke_width=5, background_stroke_color=ManimColor('#000000'), \*\*kwargs)

Returns a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup) of [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer) mobjects
that shows the index of each submobject.

Useful for working with parts of complicated mobjects.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject that will have its submobjects labelled.
  * **label_height** (*float*) – The height of the labels, by default 0.15.
  * **background_stroke_width** (*float*) – The stroke width of the outline of the labels, by default 5.
  * **background_stroke_color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)) – The stroke color of the outline of labels.
  * **kwargs** (*Any*) – Additional parameters to be passed into the :class\`~.Integer\`
    mobjects used to construct the labels.
* **Return type:**
  [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

### Examples

### print_family(mobject, n_tabs=0)

For debugging purposes

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **n_tabs** (*int*)
* **Return type:**
  None
