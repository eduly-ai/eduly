# Code

Qualified name: `manim.mobject.text.code\_mobject.Code`

### *class* Code(code_file=None, code_string=None, language=None, formatter_style='vim', tab_width=4, add_line_numbers=True, line_numbers_from=1, background='rectangle', background_config=None, paragraph_config=None)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A highlighted source code listing.

### Examples

Normal usage:

```default
listing = Code(
    "helloworldcpp.cpp",
    tab_width=4,
    formatter_style="emacs",
    background="window",
    language="cpp",
    background_config={"stroke_color": WHITE},
    paragraph_config={"font": "Noto Sans Mono"},
)
```

We can also render code passed as a string. As the automatic language
detection can be a bit flaky, it is recommended to specify the language
explicitly:

* **Parameters:**
  * **code_file** ([*StrPath*](manim.typing.md#manim.typing.StrPath) *|* *None*) – The path to the code file to display.
  * **code_string** (*str* *|* *None*) – Alternatively, the code string to display.
  * **language** (*str* *|* *None*) – The programming language of the code. If not specified, it will be
    guessed from the file extension or the code itself.
  * **formatter_style** (*str*) – The style to use for the code highlighting. Defaults to `"vim"`.
    A list of all available styles can be obtained by calling
    [`Code.get_styles_list()`](#manim.mobject.text.code_mobject.Code.get_styles_list).
  * **tab_width** (*int*) – The width of a tab character in spaces. Defaults to 4.
  * **add_line_numbers** (*bool*) – Whether to display line numbers. Defaults to `True`.
  * **line_numbers_from** (*int*) – The first line number to display. Defaults to 1.
  * **background** (*Literal* *[* *'rectangle'* *,*  *'window'* *]*) – The type of background to use. Can be either `"rectangle"` (the
    default) or `"window"`.
  * **background_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – Keyword arguments passed to the background constructor. Default
    settings are stored in the class attribute
    `default_background_config` (which can also be modified
    directly).
  * **paragraph_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – Keyword arguments passed to the constructor of the
    [`Paragraph`](manim.mobject.text.text_mobject.Paragraph.md#manim.mobject.text.text_mobject.Paragraph) objects holding the code, and the line
    numbers. Default settings are stored in the class attribute
    `default_paragraph_config` (which can also be modified
    directly).

### Methods

| [`get_styles_list`](#manim.mobject.text.code_mobject.Code.get_styles_list)   | Get the list of all available formatter styles.   |
|------------------------------------------------------------------------------|---------------------------------------------------|

### Attributes

| `animate`                   | Used to animate the application of any method of `self`.               |
|-----------------------------|------------------------------------------------------------------------|
| `animation_overrides`       |                                                                        |
| `color`                     |                                                                        |
| `default_background_config` |                                                                        |
| `default_paragraph_config`  |                                                                        |
| `depth`                     | The depth of the mobject.                                              |
| `fill_color`                | If there are multiple colors (for gradient) this returns the first one |
| `height`                    | The height of the mobject.                                             |
| `n_points_per_curve`        |                                                                        |
| `sheen_factor`              |                                                                        |
| `stroke_color`              |                                                                        |
| `width`                     | The width of the mobject.                                              |
| `code`                      |                                                                        |

#### \_original_\_init_\_(code_file=None, code_string=None, language=None, formatter_style='vim', tab_width=4, add_line_numbers=True, line_numbers_from=1, background='rectangle', background_config=None, paragraph_config=None)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **code_file** ([*StrPath*](manim.typing.md#manim.typing.StrPath) *|* *None*)
  * **code_string** (*str* *|* *None*)
  * **language** (*str* *|* *None*)
  * **formatter_style** (*str*)
  * **tab_width** (*int*)
  * **add_line_numbers** (*bool*)
  * **line_numbers_from** (*int*)
  * **background** (*Literal* *[* *'rectangle'* *,*  *'window'* *]*)
  * **background_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **paragraph_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)

#### *classmethod* get_styles_list()

Get the list of all available formatter styles.

* **Return type:**
  list[str]
