# text_mobject

Mobjects used for displaying (non-LaTeX) text.

#### NOTE
Just as you can use [`Tex`](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) and [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) (from the module [`tex_mobject`](manim.mobject.text.tex_mobject.md#module-manim.mobject.text.tex_mobject))
to insert LaTeX to your videos, you can use [`Text`](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) to to add normal text.

#### IMPORTANT
See the corresponding tutorial [Text Without LaTeX](../guides/using_text.md#using-text-objects), especially for information about fonts.

The simplest way to add text to your animations is to use the [`Text`](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) class. It uses the Pango library to render text.
With Pango, you are also able to render non-English alphabets like 你好 or  こんにちは or 안녕하세요 or مرحبا بالعالم.

### Examples

### Classes

| [`MarkupText`](manim.mobject.text.text_mobject.MarkupText.md#manim.mobject.text.text_mobject.MarkupText)   | Display (non-LaTeX) text rendered using [Pango](https://pango.org/).   |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [`Paragraph`](manim.mobject.text.text_mobject.Paragraph.md#manim.mobject.text.text_mobject.Paragraph)      | Display a paragraph of text.                                           |
| [`Text`](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text)                     |                                                                        |

### Functions

### register_font(font_file)

Temporarily add a font file to Pango’s search path.

This searches for the font_file at various places. The order it searches it described below.

1. Absolute path.
2. In `assets/fonts` folder.
3. In `font/` folder.
4. In the same directory.

* **Parameters:**
  **font_file** (*str* *|* *Path*) – The font file to add.
* **Return type:**
  *Iterator*[None]

### Examples

Use `with register_font(...)` to add a font file to search
path.

```python
with register_font("path/to/font_file.ttf"):
    a = Text("Hello", font="Custom Font Name")
```

* **Raises:**
  * **FileNotFoundError:** – If the font doesn’t exists.
  * **AttributeError:** – If this method is used on macOS.
  * **.. important ::** – This method is available for macOS for `ManimPango>=v0.2.3`. Using this
        method with previous releases will raise an `AttributeError` on macOS.
* **Parameters:**
  **font_file** (*str* *|* *Path*)
* **Return type:**
  *Iterator*[None]

### remove_invisible_chars(mobject)

Function to remove unwanted invisible characters from some mobjects.

* **Parameters:**
  **mobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – Any SVGMobject from which we want to remove unwanted invisible characters.
* **Returns:**
  The SVGMobject without unwanted invisible characters.
* **Return type:**
  [`SVGMobject`](manim.mobject.svg.svg_mobject.SVGMobject.md#manim.mobject.svg.svg_mobject.SVGMobject)
