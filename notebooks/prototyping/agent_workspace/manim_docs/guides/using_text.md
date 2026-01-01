# Rendering Text and Formulas

There are two different ways by which you can render **Text** in videos:

1. Using Pango ([`text_mobject`](../reference/manim.mobject.text.text_mobject.md#module-manim.mobject.text.text_mobject))
2. Using LaTeX ([`tex_mobject`](../reference/manim.mobject.text.tex_mobject.md#module-manim.mobject.text.tex_mobject))

If you want to render simple text, you should use either [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) or
[`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.md#manim.mobject.text.text_mobject.MarkupText), or one of its derivatives like [`Paragraph`](../reference/manim.mobject.text.text_mobject.Paragraph.md#manim.mobject.text.text_mobject.Paragraph).
See [Text Without LaTeX](#using-text-objects) for more information.

LaTeX should be used when you need mathematical typesetting. See
[Text With LaTeX](#rendering-with-latex) for more information.

<a id="using-text-objects"></a>

## Text Without LaTeX

The simplest way to add text to your animations is to use the [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text)
class. It uses the [Pango library](https://pango.org) to render text. With Pango, you can also
render non-English alphabets like 你好 or  こんにちは or 안녕하세요 or
مرحبا بالعالم.

Here is a simple *Hello World* animation.

You can also use [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.md#manim.mobject.text.text_mobject.MarkupText) which allows the use of PangoMarkup
(see the documentation of [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.md#manim.mobject.text.text_mobject.MarkupText) for details) to render text.
For example:

### Working with [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text)

This section explains the properties of [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) and how can it be used
in your animations.

#### Using Fonts

You can set a different font using `font`.

#### NOTE
The font used must be installed in your system, and Pango should know
about it. You can get a list of fonts using `manimpango.list_fonts()`.

```pycon
>>> import manimpango
>>> manimpango.list_fonts()
[...]
```

#### Setting Slant and Weight

Slant is the style of the Text, and it can be `NORMAL` (the default),
`ITALIC` or `OBLIQUE`. Usually, for many fonts both `ITALIC` and
`OBLIQUE` look similar, but `ITALIC` uses **Roman Style**, whereas
`OBLIQUE` uses **Italic Style**.

Weight specifies the boldness of a font. You can see a list of weights in
`manimpango.Weight`.

<a id="using-colors"></a>

#### Using Colors

You can set the color of the text using `color`:

You can use utilities like `t2c` for coloring specific characters.
This may be problematic if your text contains ligatures
as explained in [Iterating Text](#iterating-text).

`t2c` accepts two types of dictionaries,

* The keys can contain indices like `[2:-1]` or `[4:8]`,
  this works similar to how [slicing](https://realpython.com/python-strings/#string-slicing)
  works in Python. The values should be the color of the Text from `Color`.
* The keys contain words or characters which should be colored separately
  and the values should be the color from `Color`:

If you want to avoid problems when using colors (due to ligatures), consider using
`MarkupText`.

#### Using Gradients

You can add a gradient using `gradient`. The value must
be an iterable of any length:

You can also use `t2g` for gradients with specific
characters of the text. It shares a similar syntax to [the
interface for colors](#using-colors):

#### Setting Line Spacing

You can set the line spacing using `line_spacing`:

<a id="disable-ligatures"></a>

#### Disabling Ligatures

By disabling ligatures you would get a one-to-one mapping between characters and
submobjects. This fixes the issues with coloring text.

#### WARNING
Be aware that using this method with text that heavily depends on
ligatures (Arabic text) may yield unexpected results.

You can disable ligatures by passing `disable_ligatures` to
`Text`. For example:

<a id="iterating-text"></a>

#### Iterating [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text)

Text objects behave like [`VGroups`](../reference/manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup). Therefore, you can slice and index
the text.

For example, you can set each letter to different color by iterating it.

#### WARNING
Please note that [Ligature](https://en.wikipedia.org/wiki/Ligature_(writing)) can cause problems here. If you need a
one-to-one mapping of characters to submobjects you should pass
the `disable_ligatures` parameter to [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text).
See [Disabling Ligatures](#disable-ligatures).

### Working with [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.md#manim.mobject.text.text_mobject.MarkupText)

MarkupText is similar to [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text), the only difference between them is
that this accepts and processes PangoMarkup (which is similar to
html), instead of just rendering plain text.

Consult the documentation of [`MarkupText`](../reference/manim.mobject.text.text_mobject.MarkupText.md#manim.mobject.text.text_mobject.MarkupText) for more details
and further references about PangoMarkup.

<a id="rendering-with-latex"></a>

## Text With LaTeX

Just as you can use [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) to add text to your videos, you can
use [`Tex`](../reference/manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) to insert LaTeX.

For example,

#### NOTE
Note that we are using a raw string (`r'...'`) instead of a regular string (`'...'`).
This is because TeX code uses a lot of special characters - like `\` for example - that
have special meaning within a regular python string. An alternative would have been to
write `\\` to escape the backslash: `Tex('\\LaTeX')`.

### Working with [`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex)

Everything passed to [`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) is in math mode by default. To be more precise,
[`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) is processed within an `align*` environment. You can achieve a
similar effect with [`Tex`](../reference/manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) by enclosing your formula with `$` symbols:
`$\xrightarrow{x^6y^8}$`:

### LaTeX commands and keyword arguments

We can use any standard LaTeX commands in the AMS maths packages. Such
as the `mathtt` math-text type or the `looparrowright` arrow.

On the Manim side, the [`Tex`](../reference/manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) class also accepts attributes to
change the appearance of the output. This is very similar to the
[`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) class. For example, the `color` keyword changes the
color of the TeX mobject.

### Extra LaTeX Packages

Some commands require special packages to be loaded into the TeX template.
For example, to use the `mathscr` script, we need to add the `mathrsfs`
package. Since this package isn’t loaded into Manim’s tex template by default,
we have to add it manually.

### Substrings and parts

The TeX mobject can accept multiple strings as arguments. Afterwards you can
refer to the individual parts either by their index (like `tex[1]`), or by
selecting parts of the tex code. In this example, we set the color
of the `\bigstar` using `set_color_by_tex()`:

Note that `set_color_by_tex()` colors the entire substring containing
the Tex, not just the specific symbol or Tex expression. Consider the following example:

As you can see, this colors the entire equation yellow, contrary to what
may be expected. To color only `x` yellow, we have to do the following:

By setting `substrings_to_isolate` to `x`, we split up the
[`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) into substrings automatically and isolate the `x` components
into individual substrings. Only then can `set_color_by_tex()` be used
to achieve the desired result.

Note that Manim also supports a custom syntax that allows splitting
a TeX string into substrings easily: simply enclose parts of your formula
that you want to isolate with double braces. In the string
`MathTex(r"{{ a^2 }} + {{ b^2 }} = {{ c^2 }}")`, the rendered mobject
will consist of the substrings `a^2`, `+`, `b^2`, `=`, and `c^2`.
This makes transformations between similar text fragments easy
to write using [`TransformMatchingTex`](../reference/manim.animation.transform_matching_parts.TransformMatchingTex.md#manim.animation.transform_matching_parts.TransformMatchingTex).

### Using `index_labels` to work with complicated strings

You might sometimes be working with a very complicated [`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) mobject
that makes it difficult to work with its individual components. This is
where the debugging function [`index_labels()`](../reference/manim.utils.debug.md#manim.utils.debug.index_labels) is very useful.

The method shows the index of a mobject’s submobjects, allowing you
to easily find the components of the mobject you would like to change.

### LaTeX Maths Fonts - The Template Library

Changing fonts in LaTeX when typesetting mathematical formulae is
trickier than regular text. It requires changing the template that is used
to compile the TeX. Manim comes with a collection of [`TexFontTemplates`](../reference/manim.utils.tex_templates.TexFontTemplates.md#manim.utils.tex_templates.TexFontTemplates)
ready for you to use. These templates will all work in math mode:

Manim also has a [`TexTemplateLibrary`](../reference/manim.utils.tex_templates.TexTemplateLibrary.md#manim.utils.tex_templates.TexTemplateLibrary) containing the TeX
templates used by 3Blue1Brown. One example is the ctex template,
used for typesetting Chinese script. For this to work, the ctex LaTeX package
must be installed on your system. Furthermore, if you are only
typesetting Text, you probably do not need [`Tex`](../reference/manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) at all, and
should use [`Text`](../reference/manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) instead.

### Aligning formulae

[`MathTex`](../reference/manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) mobject is typeset in the LaTeX  `align*`
environment. This means you can use the `&` alignment character
when typesetting multiline formulae:
