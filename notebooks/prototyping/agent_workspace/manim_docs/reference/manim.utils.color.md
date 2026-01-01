# color

Utilities for working with colors and predefined color constants.

## Color data structure

| [`core`](manim.utils.color.core.md#module-manim.utils.color.core)   | Manim's (internal) color data structure and some utilities for color conversion.   |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------|

## Predefined colors

There are several predefined colors available in Manim:

- The colors listed in [`color.manim_colors`](manim.utils.color.manim_colors.md#module-manim.utils.color.manim_colors) are loaded into
  Manim’s global name space.
- The colors in [`color.AS2700`](manim.utils.color.AS2700.md#module-manim.utils.color.AS2700), [`color.BS381`](manim.utils.color.BS381.md#module-manim.utils.color.BS381),
  [`color.DVIPSNAMES`](manim.utils.color.DVIPSNAMES.md#module-manim.utils.color.DVIPSNAMES), [`color.SVGNAMES`](manim.utils.color.SVGNAMES.md#module-manim.utils.color.SVGNAMES), [`color.X11`](manim.utils.color.X11.md#module-manim.utils.color.X11) and
  [`color.XKCD`](manim.utils.color.XKCD.md#module-manim.utils.color.XKCD) need to be accessed via their module (which are available
  in Manim’s global name space), or imported separately. For example:
  ```pycon
  >>> from manim import XKCD
  >>> XKCD.AVOCADO
  ManimColor('#90B134')
  ```

  Or, alternatively:
  ```pycon
  >>> from manim.utils.color.XKCD import AVOCADO
  >>> AVOCADO
  ManimColor('#90B134')
  ```

The following modules contain the predefined color constants:

| [`manim_colors`](manim.utils.color.manim_colors.md#module-manim.utils.color.manim_colors)   | Colors included in the global name space.   |
|---------------------------------------------------------------------------------------------|---------------------------------------------|
| [`AS2700`](manim.utils.color.AS2700.md#module-manim.utils.color.AS2700)                     | Australian Color Standard                   |
| [`BS381`](manim.utils.color.BS381.md#module-manim.utils.color.BS381)                        | British Color Standard                      |
| [`DVIPSNAMES`](manim.utils.color.DVIPSNAMES.md#module-manim.utils.color.DVIPSNAMES)         | dvips Colors                                |
| [`SVGNAMES`](manim.utils.color.SVGNAMES.md#module-manim.utils.color.SVGNAMES)               | SVG 1.1 Colors                              |
| [`XKCD`](manim.utils.color.XKCD.md#module-manim.utils.color.XKCD)                           | Colors from the XKCD Color Name Survey      |
| [`X11`](manim.utils.color.X11.md#module-manim.utils.color.X11)                              | X11 Colors                                  |
