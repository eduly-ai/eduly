# core

Manim’s (internal) color data structure and some utilities for color conversion.

This module contains the implementation of [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor), the data structure
internally used to represent colors.

The preferred way of using these colors is by importing their constants from Manim:

```pycon
>>> from manim import RED, GREEN, BLUE
>>> print(RED)
#FC6255
```

Note that this way uses the name of the colors in UPPERCASE.

#### NOTE
The colors with a `_C` suffix have an alias equal to the colorname without a
letter. For example, `GREEN = GREEN_C`.

## Custom Color Spaces

Hello, dear visitor. You seem to be interested in implementing a custom color class for
a color space we don’t currently support.

The current system is using a few indirections for ensuring a consistent behavior with
all other color types in Manim.

To implement a custom color space, you must subclass [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor) and implement
three important methods:

- [`_internal_value`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor._internal_value): a `@property` implemented on
  [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor) with the goal of keeping a consistent internal representation
  which can be referenced by other functions in [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor). This property acts
  as a proxy to whatever representation you need in your class.
  - The getter should always return a NumPy array in the format `[r,g,b,a]`, in
    accordance with the type `ManimColorInternal`.
  - The setter should always accept a value in the format `[r,g,b,a]` which can be
    converted to whatever attributes you need.
- [`_internal_space`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor._internal_space): a read-only `@property` implemented on
  [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor) with the goal of providing a useful representation which can be
  used by operators, interpolation and color transform functions.

  The only constraints on this value are:
  - It must be a NumPy array.
  - The last value must be the opacity in a range `0.0` to `1.0`.

  Additionally, your `__init__` must support this format as an initialization value
  without additional parameters to ensure correct functionality of all other methods in
  [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor).
- [`_from_internal()`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor._from_internal): a `@classmethod` which converts an
  `[r,g,b,a]` value into suitable parameters for your `__init__` method and calls
  the `cls` parameter.

### Type Aliases

### *class* ParsableManimColor

```default
ManimColor | int | str | [`IntRGBLike`](manim.typing.md#manim.typing.IntRGBLike) | [`FloatRGBLike`](manim.typing.md#manim.typing.FloatRGBLike) | [`IntRGBALike`](manim.typing.md#manim.typing.IntRGBALike) | [`FloatRGBALike`](manim.typing.md#manim.typing.FloatRGBALike)
```

[`ParsableManimColor`](#manim.utils.color.core.ParsableManimColor) represents all the types which can be parsed
to a [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor) in Manim.

### TypeVar’s

### *class* ManimColorT

```default
TypeVar('ManimColorT', bound=ManimColor)
```

### Classes

| [`HSV`](manim.utils.color.core.HSV.md#manim.utils.color.core.HSV)                                                    | HSV Color Space                     |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)                               | Internal representation of a color. |
| [`RGBA`](manim.utils.color.core.RGBA.md#manim.utils.color.core.RGBA)                                                 | RGBA Color Space                    |
| [`RandomColorGenerator`](manim.utils.color.core.RandomColorGenerator.md#manim.utils.color.core.RandomColorGenerator) |                                     |

### Functions

### average_color(\*colors)

Determine the average color between the given parameters.

#### NOTE
This operation does not consider the alphas (opacities) of the colors. The
generated color has an alpha or opacity of 1.0.

* **Returns:**
  The average color of the input.
* **Return type:**
  [ManimColor](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)
* **Parameters:**
  **colors** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor))

### color_gradient(reference_colors, length_of_output)

Create a list of colors interpolated between the input array of colors with a
specific number of colors.

* **Parameters:**
  * **reference_colors** (*Iterable* *[*[*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor) *]*) – The colors to be interpolated between or spread apart.
  * **length_of_output** (*int*) – The number of colors that the output should have, ideally more than the input.
* **Returns:**
  A list of interpolated [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)’s.
* **Return type:**
  list[[ManimColor](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)]

### color_to_int_rgb(color)

Helper function for use in functional style programming. Refer to
[`ManimColor.to_int_rgb()`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor.to_int_rgb).

* **Parameters:**
  **color** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor)) – A color to convert to an RGB integer array.
* **Returns:**
  The corresponding RGB integer array.
* **Return type:**
  RGB_Array_Int

### color_to_int_rgba(color, alpha=1.0)

Helper function for use in functional style programming. Refer to
[`ManimColor.to_int_rgba_with_alpha()`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor.to_int_rgba_with_alpha).

* **Parameters:**
  * **color** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor)) – A color to convert to an RGBA integer array.
  * **alpha** (*float*) – An alpha value between 0.0 and 1.0 to be used as opacity in the color. Default is
    1.0.
* **Returns:**
  The corresponding RGBA integer array.
* **Return type:**
  RGBA_Array_Int

### color_to_rgb(color)

Helper function for use in functional style programming.
Refer to [`ManimColor.to_rgb()`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor.to_rgb).

* **Parameters:**
  **color** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor)) – A color to convert to an RGB float array.
* **Returns:**
  The corresponding RGB float array.
* **Return type:**
  RGB_Array_Float

### color_to_rgba(color, alpha=1.0)

Helper function for use in functional style programming. Refer to
[`ManimColor.to_rgba_with_alpha()`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor.to_rgba_with_alpha).

* **Parameters:**
  * **color** ([*ParsableManimColor*](#manim.utils.color.core.ParsableManimColor)) – A color to convert to an RGBA float array.
  * **alpha** (*float*) – An alpha value between 0.0 and 1.0 to be used as opacity in the color. Default is
    1.0.
* **Returns:**
  The corresponding RGBA float array.
* **Return type:**
  RGBA_Array_Float

### get_shaded_rgb(rgb, point, unit_normal_vect, light_source)

Add light or shadow to the `rgb` color of some surface which is located at a
given `point` in space and facing in the direction of `unit_normal_vect`,
depending on whether the surface is facing a `light_source` or away from it.

* **Parameters:**
  * **rgb** ([*FloatRGB*](manim.typing.md#manim.typing.FloatRGB)) – An RGB array of floats.
  * **point** ([*Point3D*](manim.typing.md#manim.typing.Point3D)) – The location of the colored surface.
  * **unit_normal_vect** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D)) – The direction in which the colored surface is facing.
  * **light_source** ([*Point3D*](manim.typing.md#manim.typing.Point3D)) – The location of a light source which might illuminate the surface.
* **Returns:**
  The color with added light or shadow, depending on the direction of the colored
  surface.
* **Return type:**
  RGB_Array_Float

### hex_to_rgb(hex_code)

Helper function for use in functional style programming. Refer to
[`ManimColor.to_rgb()`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor.to_rgb).

* **Parameters:**
  **hex_code** (*str*) – A hex string representing a color.
* **Returns:**
  An RGB array representing the color.
* **Return type:**
  RGB_Array_Float

### interpolate_color(color1, color2, alpha)

Standalone function to interpolate two ManimColors and get the result. Refer to
[`ManimColor.interpolate()`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor.interpolate).

* **Parameters:**
  * **color1** ([*ManimColorT*](#manim.utils.color.core.ManimColorT)) – The first [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor).
  * **color2** ([*ManimColorT*](#manim.utils.color.core.ManimColorT)) – The second [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor).
  * **alpha** (*float*) – The alpha value determining the point of interpolation between the colors.
* **Returns:**
  The interpolated ManimColor.
* **Return type:**
  [ManimColor](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)

### invert_color(color)

Helper function for use in functional style programming. Refer to
[`ManimColor.invert()`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor.invert)

* **Parameters:**
  **color** ([*ManimColorT*](#manim.utils.color.core.ManimColorT)) – The [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor) to invert.
* **Returns:**
  The linearly inverted [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor).
* **Return type:**
  [ManimColor](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)

### random_bright_color()

Return a random bright color: a random color averaged with `WHITE`.

#### WARNING
This operation is very expensive. Please keep in mind the performance loss.

* **Returns:**
  A random bright [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor).
* **Return type:**
  [ManimColor](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)

### random_color()

Return a random [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor).

* **Returns:**
  A random [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor).
* **Return type:**
  [ManimColor](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)

### rgb_to_color(rgb)

Helper function for use in functional style programming. Refer to
[`ManimColor.from_rgb()`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor.from_rgb).

* **Parameters:**
  **rgb** ([*FloatRGBLike*](manim.typing.md#manim.typing.FloatRGBLike) *|* [*IntRGBLike*](manim.typing.md#manim.typing.IntRGBLike)) – A 3 element iterable.
* **Returns:**
  A ManimColor with the corresponding value.
* **Return type:**
  [ManimColor](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)

### rgb_to_hex(rgb)

Helper function for use in functional style programming. Refer to
[`ManimColor.from_rgb()`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor.from_rgb) and [`ManimColor.to_hex()`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor.to_hex).

* **Parameters:**
  **rgb** ([*FloatRGBLike*](manim.typing.md#manim.typing.FloatRGBLike) *|* [*IntRGBLike*](manim.typing.md#manim.typing.IntRGBLike)) – A 3 element iterable.
* **Returns:**
  A hex representation of the color.
* **Return type:**
  str

### rgba_to_color(rgba)

Helper function for use in functional style programming. Refer to
[`ManimColor.from_rgba()`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor.from_rgba).

* **Parameters:**
  **rgba** ([*FloatRGBALike*](manim.typing.md#manim.typing.FloatRGBALike) *|* [*IntRGBALike*](manim.typing.md#manim.typing.IntRGBALike)) – A 4 element iterable.
* **Returns:**
  A ManimColor with the corresponding value
* **Return type:**
  [ManimColor](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)
