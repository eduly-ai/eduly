# MarkupText

Qualified name: `manim.mobject.text.text\_mobject.MarkupText`

### *class* MarkupText(text, fill_opacity=1, stroke_width=0, color=None, font_size=48, line_spacing=-1, font='', slant='NORMAL', weight='NORMAL', justify=False, gradient=None, tab_width=4, height=None, width=None, should_center=True, disable_ligatures=False, warn_missing_font=True, \*\*kwargs)

Bases: [`SVGMobject`](manim.mobject.svg.svg_mobject.SVGMobject.md#manim.mobject.svg.svg_mobject.SVGMobject)

Display (non-LaTeX) text rendered using [Pango](https://pango.org/).

Text objects behave like a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)-like iterable of all characters
in the given text. In particular, slicing is possible.

**What is PangoMarkup?**

PangoMarkup is a small markup language like html and it helps you avoid using
“range of characters” while coloring or styling a piece a Text. You can use
this language with [`MarkupText`](#manim.mobject.text.text_mobject.MarkupText).

A simple example of a marked-up string might be:

```default
<span foreground="blue" size="x-large">Blue text</span> is <i>cool</i>!"
```

and it can be used with [`MarkupText`](#manim.mobject.text.text_mobject.MarkupText) as

A more elaborate example would be:

PangoMarkup can also contain XML features such as numeric character
entities such as `&#169;` for © can be used too.

The most general markup tag is `<span>`, then there are some
convenience tags.

Here is a list of supported tags:

- `<b>bold</b>`, `<i>italic</i>` and `<b><i>bold+italic</i></b>`
- `<u>underline</u>` and `<s>strike through</s>`
- `<tt>typewriter font</tt>`
- `<big>bigger font</big>` and `<small>smaller font</small>`
- `<sup>superscript</sup>` and `<sub>subscript</sub>`
- `<span underline="double" underline_color="green">double underline</span>`
- `<span underline="error">error underline</span>`
- `<span overline="single" overline_color="green">overline</span>`
- `<span strikethrough="true" strikethrough_color="red">strikethrough</span>`
- `<span font_family="sans">temporary change of font</span>`
- `<span foreground="red">temporary change of color</span>`
- `<span fgcolor="red">temporary change of color</span>`
- `<gradient from="YELLOW" to="RED">temporary gradient</gradient>`

For `<span>` markup, colors can be specified either as
hex triples like `#aabbcc` or as named CSS colors like
`AliceBlue`.
The `<gradient>` tag is handled by Manim rather than
Pango, and supports hex triplets or Manim constants like
`RED` or `RED_A`.
If you want to use Manim constants like `RED_A` together
with `<span>`, you will need to use Python’s f-String
syntax as follows:

```default
MarkupText(f'<span foreground="{RED_A}">here you go</span>')
```

If your text contains ligatures, the [`MarkupText`](#manim.mobject.text.text_mobject.MarkupText) class may
incorrectly determine the first and last letter when creating the
gradient. This is due to the fact that `fl` are two separate characters,
but might be set as one single glyph - a ligature. If your language
does not depend on ligatures, consider setting `disable_ligatures`
to `True`. If you must use ligatures, the `gradient` tag supports an optional
attribute `offset` which can be used to compensate for that error.

For example:

- `<gradient from="RED" to="YELLOW" offset="1">example</gradient>` to *start* the gradient one letter earlier
- `<gradient from="RED" to="YELLOW" offset=",1">example</gradient>` to *end* the gradient one letter earlier
- `<gradient from="RED" to="YELLOW" offset="2,1">example</gradient>` to *start* the gradient two letters earlier and *end* it one letter earlier

Specifying a second offset may be necessary if the text to be colored does
itself contain ligatures. The same can happen when using HTML entities for
special chars.

When using `underline`, `overline` or `strikethrough` together with
`<gradient>` tags, you will also need to use the offset, because
underlines are additional paths in the final `SVGMobject`.
Check out the following example.

Escaping of special characters: `>` **should** be written as `&gt;`
whereas `<` and `&` *must* be written as `&lt;` and
`&amp;`.

You can find more information about Pango markup formatting at the
corresponding documentation page:
[Pango Markup](https://docs.gtk.org/Pango/pango_markup.html).
Please be aware that not all features are supported by this class and that
the `<gradient>` tag mentioned above is not supported by Pango.

* **Parameters:**
  * **text** (*str*) – The text that needs to be created as mobject.
  * **fill_opacity** (*float*) – The fill opacity, with 1 meaning opaque and 0 meaning transparent.
  * **stroke_width** (*float*) – Stroke width.
  * **font_size** (*float*) – Font size.
  * **line_spacing** (*float*) – Line spacing.
  * **font** (*str*) – Global font setting for the entire text. Local overrides are possible.
  * **slant** (*str*) – Global slant setting, e.g. NORMAL or ITALIC. Local overrides are possible.
  * **weight** (*str*) – Global weight setting, e.g. NORMAL or BOLD. Local overrides are possible.
  * **gradient** (*Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*  *|* *None*) – Global gradient setting. Local overrides are possible.
  * **warn_missing_font** (*bool*) – If True (default), Manim will issue a warning if the font does not exist in the
    (case-sensitive) list of fonts returned from manimpango.list_fonts().
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **justify** (*bool*)
  * **tab_width** (*int*)
  * **height** (*int* *|* *None*)
  * **width** (*int* *|* *None*)
  * **should_center** (*bool*)
  * **disable_ligatures** (*bool*)
  * **kwargs** (*Any*)
* **Returns:**
  The text displayed in form of a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)-like mobject.
* **Return type:**
  [`MarkupText`](#manim.mobject.text.text_mobject.MarkupText)

### Examples

As [`MarkupText`](#manim.mobject.text.text_mobject.MarkupText) uses Pango to render text, rendering non-English
characters is easily possible:

You can justify the text by passing `justify` parameter.

### Tests

Check that the creation of [`MarkupText`](#manim.mobject.text.text_mobject.MarkupText) works:

```default
>>> MarkupText('The horse does not eat cucumber salad.')
MarkupText('The horse does not eat cucumber salad.')
```

### Methods

| `font_list`   |    |
|---------------|----|

### Attributes

| `animate`             | Used to animate the application of any method of `self`.               |
|-----------------------|------------------------------------------------------------------------|
| `animation_overrides` |                                                                        |
| `color`               |                                                                        |
| `depth`               | The depth of the mobject.                                              |
| `fill_color`          | If there are multiple colors (for gradient) this returns the first one |
| `font_size`           |                                                                        |
| `hash_seed`           | A unique hash representing the result of the generated mobject points. |
| `height`              | The height of the mobject.                                             |
| `n_points_per_curve`  |                                                                        |
| `sheen_factor`        |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |

#### \_count_real_chars(s)

Counts characters that will be displayed.

This is needed for partial coloring or gradients, because space
counts to the text’s len, but has no corresponding character.

* **Parameters:**
  **s** (*str*)
* **Return type:**
  int

#### \_extract_color_tags()

Used to determine which parts (if any) of the string should be formatted
with a custom color.

Removes the `<color>` tag, as it is not part of Pango’s markup and would cause an error.

Note: Using the `<color>` tags is deprecated. As soon as the legacy syntax is gone, this function
will be removed.

* **Return type:**
  list[dict[str, *Any*]]

#### \_extract_gradient_tags()

Used to determine which parts (if any) of the string should be formatted
with a gradient.

Removes the `<gradient>` tag, as it is not part of Pango’s markup and would cause an error.

* **Return type:**
  list[dict[str, *Any*]]

#### \_original_\_init_\_(text, fill_opacity=1, stroke_width=0, color=None, font_size=48, line_spacing=-1, font='', slant='NORMAL', weight='NORMAL', justify=False, gradient=None, tab_width=4, height=None, width=None, should_center=True, disable_ligatures=False, warn_missing_font=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **text** (*str*)
  * **fill_opacity** (*float*)
  * **stroke_width** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **font_size** (*float*)
  * **line_spacing** (*float*)
  * **font** (*str*)
  * **slant** (*str*)
  * **weight** (*str*)
  * **justify** (*bool*)
  * **gradient** (*Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*  *|* *None*)
  * **tab_width** (*int*)
  * **height** (*int* *|* *None*)
  * **width** (*int* *|* *None*)
  * **should_center** (*bool*)
  * **disable_ligatures** (*bool*)
  * **warn_missing_font** (*bool*)
  * **kwargs** (*Any*)

#### \_parse_color(col)

Parse color given in `<color>` or `<gradient>` tags.

* **Parameters:**
  **col** (*str*)
* **Return type:**
  str

#### \_text2hash(color)

Generates `sha256` hash for file name.

* **Parameters:**
  **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
* **Return type:**
  str

#### \_text2svg(color)

Convert the text to SVG using Pango.

* **Parameters:**
  **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
* **Return type:**
  str
