# Variable

Qualified name: `manim.mobject.text.numbers.Variable`

### *class* Variable(var, label, var_type=<class 'manim.mobject.text.numbers.DecimalNumber'>, num_decimal_places=2, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A class for displaying text that shows “label = value” with
the value continuously updated from a [`ValueTracker`](manim.mobject.value_tracker.ValueTracker.md#manim.mobject.value_tracker.ValueTracker).

* **Parameters:**
  * **var** (*float*) – The initial value you need to keep track of and display.
  * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) *|* [*SingleStringMathTex*](manim.mobject.text.tex_mobject.SingleStringMathTex.md#manim.mobject.text.tex_mobject.SingleStringMathTex)) – The label for your variable. Raw strings are convertex to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) objects.
  * **var_type** (*type* *[*[*DecimalNumber*](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) *|* [*Integer*](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer) *]*) – The class used for displaying the number. Defaults to [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber).
  * **num_decimal_places** (*int*) – The number of decimal places to display in your variable. Defaults to 2.
    If var_type is an [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer), this parameter is ignored.
  * **kwargs** (*Any*) – Other arguments to be passed to ~.Mobject.

#### label

The label for your variable, for example `x = ...`.

* **Type:**
  Union[`str`, [`Tex`](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex), [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex), [`Text`](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text), [`SingleStringMathTex`](manim.mobject.text.tex_mobject.SingleStringMathTex.md#manim.mobject.text.tex_mobject.SingleStringMathTex)]

#### tracker

Useful in updating the value of your variable on-screen.

* **Type:**
  [`ValueTracker`](manim.mobject.value_tracker.ValueTracker.md#manim.mobject.value_tracker.ValueTracker)

#### value

The tex for the value of your variable.

* **Type:**
  Union[[`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber), [`Integer`](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer)]

### Examples

Normal usage:

```default
# DecimalNumber type
var = 0.5
on_screen_var = Variable(var, Text("var"), num_decimal_places=3)
# Integer type
int_var = 0
on_screen_int_var = Variable(int_var, Text("int_var"), var_type=Integer)
# Using math mode for the label
on_screen_int_var = Variable(int_var, "{a}_{i}", var_type=Integer)
```

### Methods

### Attributes

| `animate`             | Used to animate the application of any method of `self`.               |
|-----------------------|------------------------------------------------------------------------|
| `animation_overrides` |                                                                        |
| `color`               |                                                                        |
| `depth`               | The depth of the mobject.                                              |
| `fill_color`          | If there are multiple colors (for gradient) this returns the first one |
| `height`              | The height of the mobject.                                             |
| `n_points_per_curve`  |                                                                        |
| `sheen_factor`        |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |

#### \_original_\_init_\_(var, label, var_type=<class 'manim.mobject.text.numbers.DecimalNumber'>, num_decimal_places=2, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **var** (*float*)
  * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) *|* [*SingleStringMathTex*](manim.mobject.text.tex_mobject.SingleStringMathTex.md#manim.mobject.text.tex_mobject.SingleStringMathTex))
  * **var_type** (*type* *[*[*DecimalNumber*](manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) *|* [*Integer*](manim.mobject.text.numbers.Integer.md#manim.mobject.text.numbers.Integer) *]*)
  * **num_decimal_places** (*int*)
  * **kwargs** (*Any*)
