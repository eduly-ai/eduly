# Text

Qualified name: `manim.mobject.text.text\_mobject.Text`

### *class* Text(text, fill_opacity=1.0, stroke_width=0, color=None, font_size=48, line_spacing=-1, font='', slant='NORMAL', weight='NORMAL', t2c=None, t2f=None, t2g=None, t2s=None, t2w=None, gradient=None, tab_width=4, warn_missing_font=True, height=None, width=None, should_center=True, disable_ligatures=False, use_svg_cache=False, \*\*kwargs)

Bases: [`SVGMobject`](manim.mobject.svg.svg_mobject.SVGMobject.md#manim.mobject.svg.svg_mobject.SVGMobject)

Display (non-LaTeX) text rendered using [Pango](https://pango.org/).

Text objects behave like a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)-like iterable of all characters
in the given text. In particular, slicing is possible.

* **Parameters:**
  * **text** (*str*) – The text that needs to be created as a mobject.
  * **font** (*str*) – The font family to be used to render the text. This is either a system font or
    one loaded with register_font(). Note that font family names may be different
    across operating systems.
  * **warn_missing_font** (*bool*) – If True (default), Manim will issue a warning if the font does not exist in the
    (case-sensitive) list of fonts returned from manimpango.list_fonts().
  * **fill_opacity** (*float*)
  * **stroke_width** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **font_size** (*float*)
  * **line_spacing** (*float*)
  * **slant** (*str*)
  * **weight** (*str*)
  * **t2c** (*dict* *[**str* *,* *str* *]*  *|* *None*)
  * **t2f** (*dict* *[**str* *,* *str* *]*  *|* *None*)
  * **t2g** (*dict* *[**str* *,* *Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]* *]*  *|* *None*)
  * **t2s** (*dict* *[**str* *,* *str* *]*  *|* *None*)
  * **t2w** (*dict* *[**str* *,* *str* *]*  *|* *None*)
  * **gradient** (*Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*  *|* *None*)
  * **tab_width** (*int*)
  * **height** (*float* *|* *None*)
  * **width** (*float* *|* *None*)
  * **should_center** (*bool*)
  * **disable_ligatures** (*bool*)
  * **use_svg_cache** (*bool*)
  * **kwargs** (*Any*)
* **Returns:**
  The mobject-like [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup).
* **Return type:**
  [`Text`](#manim.mobject.text.text_mobject.Text)

### Examples

As [`Text`](#manim.mobject.text.text_mobject.Text) uses Pango to render text, rendering non-English
characters is easily possible:

### Tests

Check that the creation of [`Text`](#manim.mobject.text.text_mobject.Text) works:

```default
>>> Text('The horse does not eat cucumber salad.')
Text('The horse does not eat cucumber salad.')
```

### Methods

| `font_list`                                                        |                         |
|--------------------------------------------------------------------|-------------------------|
| [`init_colors`](#manim.mobject.text.text_mobject.Text.init_colors) | Initializes the colors. |

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

#### \_find_indexes(word, text)

Finds the indexes of `text` in `word`.

* **Parameters:**
  * **word** (*str*)
  * **text** (*str*)
* **Return type:**
  list[tuple[int, int]]

#### \_original_\_init_\_(text, fill_opacity=1.0, stroke_width=0, color=None, font_size=48, line_spacing=-1, font='', slant='NORMAL', weight='NORMAL', t2c=None, t2f=None, t2g=None, t2s=None, t2w=None, gradient=None, tab_width=4, warn_missing_font=True, height=None, width=None, should_center=True, disable_ligatures=False, use_svg_cache=False, \*\*kwargs)

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
  * **t2c** (*dict* *[**str* *,* *str* *]*  *|* *None*)
  * **t2f** (*dict* *[**str* *,* *str* *]*  *|* *None*)
  * **t2g** (*dict* *[**str* *,* *Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]* *]*  *|* *None*)
  * **t2s** (*dict* *[**str* *,* *str* *]*  *|* *None*)
  * **t2w** (*dict* *[**str* *,* *str* *]*  *|* *None*)
  * **gradient** (*Iterable* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*  *|* *None*)
  * **tab_width** (*int*)
  * **warn_missing_font** (*bool*)
  * **height** (*float* *|* *None*)
  * **width** (*float* *|* *None*)
  * **should_center** (*bool*)
  * **disable_ligatures** (*bool*)
  * **use_svg_cache** (*bool*)
  * **kwargs** (*Any*)

#### \_text2hash(color)

Generates `sha256` hash for file name.

* **Parameters:**
  **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
* **Return type:**
  str

#### \_text2settings(color)

Converts the texts and styles to a setting for parsing.

* **Parameters:**
  **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
* **Return type:**
  list[*TextSetting*]

#### \_text2svg(color)

Convert the text to SVG using Pango.

* **Parameters:**
  **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
* **Return type:**
  str

#### init_colors(propagate_colors=True)

Initializes the colors.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Parameters:**
  **propagate_colors** (*bool*)
* **Return type:**
  Self
