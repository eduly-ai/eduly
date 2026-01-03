# ManimColor

Qualified name: `manim.utils.color.core.ManimColor`

### *class* ManimColor(value, alpha=1.0)

Bases: `object`

Internal representation of a color.

The [`ManimColor`](#manim.utils.color.core.ManimColor) class is the main class for the representation of a color.
Its internal representation is an array of 4 floats corresponding to a `[r,g,b,a]`
value where `r,g,b,a` can be between 0.0 and 1.0.

This is done in order to reduce the amount of color inconsistencies by constantly
casting between integers and floats which introduces errors.

The class can accept any value of type [`ParsableManimColor`](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) i.e.

`ManimColor, int, str, RGB_Tuple_Int, RGB_Tuple_Float, RGBA_Tuple_Int, RGBA_Tuple_Float, RGB_Array_Int,
RGB_Array_Float, RGBA_Array_Int, RGBA_Array_Float`

[`ManimColor`](#manim.utils.color.core.ManimColor) itself only accepts singular values and will directly interpret
them into a single color if possible. Be careful when passing strings to
[`ManimColor`](#manim.utils.color.core.ManimColor): it can create a big overhead for the color processing.

If you want to parse a list of colors, use the [`parse()`](#manim.utils.color.core.ManimColor.parse) method, which assumes
that you’re going to pass a list of colors so that arrays will not be interpreted as
a single color.

#### WARNING
If you pass an array of numbers to [`parse()`](#manim.utils.color.core.ManimColor.parse), it will interpret the
`r,g,b,a` numbers in that array as colors: Instead of the expected
singular color, you will get an array with 4 colors.

For conversion behaviors, see the `_internal` functions for further documentation.

You can create a [`ManimColor`](#manim.utils.color.core.ManimColor) instance via its classmethods. See the
respective methods for more info.

```python
mycolor = ManimColor.from_rgb((0, 1, 0.4, 0.5))
myothercolor = ManimColor.from_rgb((153, 255, 255))
```

You can also convert between different color spaces:

```python
mycolor_hex = mycolor.to_hex()
myoriginalcolor = ManimColor.from_hex(mycolor_hex).to_hsv()
```

* **Parameters:**
  * **value** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – Some representation of a color (e.g., a string or
    a suitable tuple). The default `None` is `BLACK`.
  * **alpha** (*float*) – The opacity of the color. By default, colors are
    fully opaque (value 1.0).

### Methods

| [`contrasting`](#manim.utils.color.core.ManimColor.contrasting)                       | Return one of two colors, light or dark (by default white or black), that contrasts with the current color (depending on its luminance).                                   |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`darker`](#manim.utils.color.core.ManimColor.darker)                                 | Return a new color that is darker than the current color, i.e. interpolated with `BLACK`.                                                                                  |
| [`from_hex`](#manim.utils.color.core.ManimColor.from_hex)                             | Create a [`ManimColor`](#manim.utils.color.core.ManimColor) from a hex string.                                                                                             |
| [`from_hsl`](#manim.utils.color.core.ManimColor.from_hsl)                             | Create a [`ManimColor`](#manim.utils.color.core.ManimColor) from an HSL array.                                                                                             |
| [`from_hsv`](#manim.utils.color.core.ManimColor.from_hsv)                             | Create a [`ManimColor`](#manim.utils.color.core.ManimColor) from an HSV array.                                                                                             |
| [`from_rgb`](#manim.utils.color.core.ManimColor.from_rgb)                             | Create a ManimColor from an RGB array.                                                                                                                                     |
| [`from_rgba`](#manim.utils.color.core.ManimColor.from_rgba)                           | Create a ManimColor from an RGBA Array.                                                                                                                                    |
| [`gradient`](#manim.utils.color.core.ManimColor.gradient)                             | This method is currently not implemented.                                                                                                                                  |
| [`interpolate`](#manim.utils.color.core.ManimColor.interpolate)                       | Interpolate between the current and the given [`ManimColor`](#manim.utils.color.core.ManimColor), and return the result.                                                   |
| [`into`](#manim.utils.color.core.ManimColor.into)                                     | Convert the current color into a different colorspace given by `class_type`, without changing the [`_internal_value`](#manim.utils.color.core.ManimColor._internal_value). |
| [`invert`](#manim.utils.color.core.ManimColor.invert)                                 | Return a new, linearly inverted version of this [`ManimColor`](#manim.utils.color.core.ManimColor) (no inplace changes).                                                   |
| [`lighter`](#manim.utils.color.core.ManimColor.lighter)                               | Return a new color that is lighter than the current color, i.e. interpolated with `WHITE`.                                                                                 |
| [`opacity`](#manim.utils.color.core.ManimColor.opacity)                               | Create a new [`ManimColor`](#manim.utils.color.core.ManimColor) with the given opacity and the same color values as before.                                                |
| [`parse`](#manim.utils.color.core.ManimColor.parse)                                   | Parse one color as a [`ManimColor`](#manim.utils.color.core.ManimColor) or a sequence of colors as a list of [`ManimColor`](#manim.utils.color.core.ManimColor)'s.         |
| [`to_hex`](#manim.utils.color.core.ManimColor.to_hex)                                 | Convert the [`ManimColor`](#manim.utils.color.core.ManimColor) to a hexadecimal representation of the color.                                                               |
| [`to_hsl`](#manim.utils.color.core.ManimColor.to_hsl)                                 | Convert the [`ManimColor`](#manim.utils.color.core.ManimColor) to an HSL array.                                                                                            |
| [`to_hsv`](#manim.utils.color.core.ManimColor.to_hsv)                                 | Convert the [`ManimColor`](#manim.utils.color.core.ManimColor) to an HSV array.                                                                                            |
| [`to_int_rgb`](#manim.utils.color.core.ManimColor.to_int_rgb)                         | Convert the current [`ManimColor`](#manim.utils.color.core.ManimColor) into an RGB array of integers.                                                                      |
| [`to_int_rgba`](#manim.utils.color.core.ManimColor.to_int_rgba)                       | Convert the current ManimColor into an RGBA array of integers.                                                                                                             |
| [`to_int_rgba_with_alpha`](#manim.utils.color.core.ManimColor.to_int_rgba_with_alpha) | Convert the current [`ManimColor`](#manim.utils.color.core.ManimColor) into an RGBA array of integers.                                                                     |
| [`to_integer`](#manim.utils.color.core.ManimColor.to_integer)                         | Convert the current [`ManimColor`](#manim.utils.color.core.ManimColor) into an integer.                                                                                    |
| [`to_rgb`](#manim.utils.color.core.ManimColor.to_rgb)                                 | Convert the current [`ManimColor`](#manim.utils.color.core.ManimColor) into an RGB array of floats.                                                                        |
| [`to_rgba`](#manim.utils.color.core.ManimColor.to_rgba)                               | Convert the current [`ManimColor`](#manim.utils.color.core.ManimColor) into an RGBA array of floats.                                                                       |
| [`to_rgba_with_alpha`](#manim.utils.color.core.ManimColor.to_rgba_with_alpha)         | Convert the current [`ManimColor`](#manim.utils.color.core.ManimColor) into an RGBA array of floats.                                                                       |

#### *classmethod* \_construct_from_space(\_space)

This function is used as a proxy for constructing a color with an internal
value. This can be used by subclasses to hook into the construction of new
objects using the internal value format.

* **Parameters:**
  **\_space** (*ndarray* *[**tuple* *[**int* *,*  *...* *]* *,* *dtype* *[*[*ManimFloat*](manim.typing.md#manim.typing.ManimFloat) *]* *]*  *|* *tuple* *[**float* *,* *float* *,* *float* *]*  *|* *tuple* *[**float* *,* *float* *,* *float* *,* *float* *]*)
* **Return type:**
  *Self*

#### *classmethod* \_from_internal(value)

This method is intended to be overwritten by custom color space classes
which are subtypes of [`ManimColor`](#manim.utils.color.core.ManimColor).

The method constructs a new object of the given class by transforming the value
in the internal format `[r,g,b,a]` into a format which the constructor of the
custom class can understand. Look at [`HSV`](manim.utils.color.core.HSV.md#manim.utils.color.core.HSV) for an example.

* **Parameters:**
  **value** ([*ManimColorInternal*](manim.typing.md#manim.typing.ManimColorInternal))
* **Return type:**
  *Self*

#### *static* \_internal_from_hex_string(hex_, alpha)

Internal function for converting a hex string into the internal representation
of a [`ManimColor`](#manim.utils.color.core.ManimColor).

#### WARNING
This does not accept any prefixes like # or similar in front of the hex string.
This is just intended for the raw hex part.

*For internal use only*

* **Parameters:**
  * **hex** – Hex string to be parsed.
  * **alpha** (*float*) – Alpha value used for the color, if the color is only 3 bytes long. Otherwise,
    if the color is 4 bytes long, this parameter will not be used.
  * **hex_** (*str*)
* **Returns:**
  Internal color representation
* **Return type:**
  [ManimColorInternal](manim.typing.md#manim.typing.ManimColorInternal)

#### *static* \_internal_from_int_rgb(rgb, alpha=1.0)

Internal function for converting an RGB tuple of integers into the internal
representation of a [`ManimColor`](#manim.utils.color.core.ManimColor).

*For internal use only*

* **Parameters:**
  * **rgb** ([*IntRGBLike*](manim.typing.md#manim.typing.IntRGBLike)) – Integer RGB tuple to be parsed
  * **alpha** (*float*) – Optional alpha value. Default is 1.0.
* **Returns:**
  Internal color representation.
* **Return type:**
  [ManimColorInternal](manim.typing.md#manim.typing.ManimColorInternal)

#### *static* \_internal_from_int_rgba(rgba)

Internal function for converting an RGBA tuple of integers into the internal
representation of a [`ManimColor`](#manim.utils.color.core.ManimColor).

*For internal use only*

* **Parameters:**
  **rgba** ([*IntRGBALike*](manim.typing.md#manim.typing.IntRGBALike)) – Int RGBA tuple to be parsed.
* **Returns:**
  Internal color representation.
* **Return type:**
  [ManimColorInternal](manim.typing.md#manim.typing.ManimColorInternal)

#### *static* \_internal_from_rgb(rgb, alpha=1.0)

Internal function for converting a rgb tuple of floats into the internal
representation of a [`ManimColor`](#manim.utils.color.core.ManimColor).

*For internal use only*

* **Parameters:**
  * **rgb** ([*FloatRGBLike*](manim.typing.md#manim.typing.FloatRGBLike)) – Float RGB tuple to be parsed.
  * **alpha** (*float*) – Optional alpha value. Default is 1.0.
* **Returns:**
  Internal color representation.
* **Return type:**
  [ManimColorInternal](manim.typing.md#manim.typing.ManimColorInternal)

#### *static* \_internal_from_rgba(rgba)

Internal function for converting an RGBA tuple of floats into the internal
representation of a [`ManimColor`](#manim.utils.color.core.ManimColor).

*For internal use only*

* **Parameters:**
  **rgba** ([*FloatRGBALike*](manim.typing.md#manim.typing.FloatRGBALike)) – Int RGBA tuple to be parsed.
* **Returns:**
  Internal color representation.
* **Return type:**
  [ManimColorInternal](manim.typing.md#manim.typing.ManimColorInternal)

#### *static* \_internal_from_string(name, alpha)

Internal function for converting a string into the internal representation of
a [`ManimColor`](#manim.utils.color.core.ManimColor). This is not used for hex strings: please refer to
`_internal_from_hex()` for this functionality.

*For internal use only*

* **Parameters:**
  * **name** (*str*) – The color name to be parsed into a color. Refer to the different color
    modules in the documentation page to find the corresponding color names.
  * **alpha** (*float*)
* **Returns:**
  Internal color representation.
* **Return type:**
  [ManimColorInternal](manim.typing.md#manim.typing.ManimColorInternal)
* **Raises:**
  **ValueError** – If the color name is not present in Manim.

#### *property* \_internal_space *: ndarray[tuple[int, ...], dtype[[ManimFloat](manim.typing.md#manim.typing.ManimFloat)]]*

This is a readonly property which is a custom representation for color space
operations. It is used for operators and can be used when implementing a custom
color space.

#### *property* \_internal_value *: [ManimColorInternal](manim.typing.md#manim.typing.ManimColorInternal)*

Return the internal value of the current Manim color `[r,g,b,a]` float
array.

* **Returns:**
  Internal color representation.
* **Return type:**
  [ManimColorInternal](manim.typing.md#manim.typing.ManimColorInternal)

#### contrasting(threshold=0.5, light=None, dark=None)

Return one of two colors, light or dark (by default white or black),
that contrasts with the current color (depending on its luminance).
This is typically used to set text in a contrasting color that ensures
it is readable against a background of the current color.

* **Parameters:**
  * **threshold** (*float*) – The luminance threshold which dictates whether the current color is
    considered light or dark (and thus whether to return the dark or
    light color, respectively). Default is 0.5.
  * **light** (*Self* *|* *None*) – The light color to return if the current color is considered dark.
    Default is `None`: in this case, pure `WHITE` will be returned.
  * **dark** (*Self* *|* *None*) – The dark color to return if the current color is considered light,
    Default is `None`: in this case, pure `BLACK` will be returned.
* **Returns:**
  The contrasting [`ManimColor`](#manim.utils.color.core.ManimColor).
* **Return type:**
  [ManimColor](#manim.utils.color.core.ManimColor)

#### darker(blend=0.2)

Return a new color that is darker than the current color, i.e.
interpolated with `BLACK`. The opacity is unchanged.

* **Parameters:**
  **blend** (*float*) – The blend ratio for the interpolation, from 0.0 (the current color
  unchanged) to 1.0 (pure black). Default is 0.2, which results in a
  slightly darker color.
* **Returns:**
  The darker [`ManimColor`](#manim.utils.color.core.ManimColor).
* **Return type:**
  [ManimColor](#manim.utils.color.core.ManimColor)

#### SEE ALSO
[`lighter()`](#manim.utils.color.core.ManimColor.lighter)

#### *classmethod* from_hex(hex_str, alpha=1.0)

Create a [`ManimColor`](#manim.utils.color.core.ManimColor) from a hex string.

* **Parameters:**
  * **hex_str** (*str*) – The hex string to be converted.  The allowed prefixes for this string are
    `#` and `0x`. Currently, this method only supports 6 nibbles, i.e. only
    strings in the format `#XXXXXX` or `0xXXXXXX`.
  * **alpha** (*float*) – Alpha value to be used for the hex string. Default is 1.0.
* **Returns:**
  The [`ManimColor`](#manim.utils.color.core.ManimColor) represented by the hex string.
* **Return type:**
  [ManimColor](#manim.utils.color.core.ManimColor)

#### *classmethod* from_hsl(hsl, alpha=1.0)

Create a [`ManimColor`](#manim.utils.color.core.ManimColor) from an HSL array.

* **Parameters:**
  * **hsl** ([*FloatHSLLike*](manim.typing.md#manim.typing.FloatHSLLike)) – Any iterable containing 3 floats from 0.0 to 1.0.
  * **alpha** (*float*) – The alpha value to be used. Default is 1.0.
* **Returns:**
  The [`ManimColor`](#manim.utils.color.core.ManimColor) with the corresponding RGB values to the given HSL
  array.
* **Return type:**
  [ManimColor](#manim.utils.color.core.ManimColor)

#### *classmethod* from_hsv(hsv, alpha=1.0)

Create a [`ManimColor`](#manim.utils.color.core.ManimColor) from an HSV array.

* **Parameters:**
  * **hsv** ([*FloatHSVLike*](manim.typing.md#manim.typing.FloatHSVLike)) – Any iterable containing 3 floats from 0.0 to 1.0.
  * **alpha** (*float*) – The alpha value to be used. Default is 1.0.
* **Returns:**
  The [`ManimColor`](#manim.utils.color.core.ManimColor) with the corresponding RGB values to the given HSV
  array.
* **Return type:**
  [ManimColor](#manim.utils.color.core.ManimColor)

#### *classmethod* from_rgb(rgb, alpha=1.0)

Create a ManimColor from an RGB array. Automagically decides which type it
is: `int` or `float`.

#### WARNING
Please make sure that your elements are not floats if you want integers. A
`5.0` will result in the input being interpreted as if it was an RGB float
array with the value `5.0` and not the integer `5`.

* **Parameters:**
  * **rgb** ([*FloatRGBLike*](manim.typing.md#manim.typing.FloatRGBLike) *|* [*IntRGBLike*](manim.typing.md#manim.typing.IntRGBLike)) – Any iterable of 3 floats or 3 integers.
  * **alpha** (*float*) – Alpha value to be used in the color. Default is 1.0.
* **Returns:**
  The [`ManimColor`](#manim.utils.color.core.ManimColor) which corresponds to the given `rgb`.
* **Return type:**
  [ManimColor](#manim.utils.color.core.ManimColor)

#### *classmethod* from_rgba(rgba)

Create a ManimColor from an RGBA Array. Automagically decides which type it
is: `int` or `float`.

#### WARNING
Please make sure that your elements are not floats if you want integers. A
`5.0` will result in the input being interpreted as if it was a float RGB
array with the float `5.0` and not the integer `5`.

* **Parameters:**
  **rgba** ([*FloatRGBALike*](manim.typing.md#manim.typing.FloatRGBALike) *|* [*IntRGBALike*](manim.typing.md#manim.typing.IntRGBALike)) – Any iterable of 4 floats or 4 integers.
* **Returns:**
  The [`ManimColor`](#manim.utils.color.core.ManimColor) corresponding to the given `rgba`.
* **Return type:**
  [ManimColor](#manim.utils.color.core.ManimColor)

#### *static* gradient(colors, length)

This method is currently not implemented. Refer to [`color_gradient()`](manim.utils.color.core.md#manim.utils.color.core.color_gradient) for
a working implementation for now.

* **Parameters:**
  * **colors** (*list* *[*[*ManimColor*](#manim.utils.color.core.ManimColor) *]*)
  * **length** (*int*)
* **Return type:**
  [*ManimColor*](#manim.utils.color.core.ManimColor) | list[[*ManimColor*](#manim.utils.color.core.ManimColor)]

#### interpolate(other, alpha)

Interpolate between the current and the given [`ManimColor`](#manim.utils.color.core.ManimColor), and return
the result.

* **Parameters:**
  * **other** (*Self*) – The other [`ManimColor`](#manim.utils.color.core.ManimColor) to be used for interpolation.
  * **alpha** (*float*) – A point on the line in RGBA colorspace connecting the two colors, i.e. the
    interpolation point. 0.0 corresponds to the current [`ManimColor`](#manim.utils.color.core.ManimColor) and
    1.0 corresponds to the other [`ManimColor`](#manim.utils.color.core.ManimColor).
* **Returns:**
  The interpolated [`ManimColor`](#manim.utils.color.core.ManimColor).
* **Return type:**
  [ManimColor](#manim.utils.color.core.ManimColor)

#### into(class_type)

Convert the current color into a different colorspace given by `class_type`,
without changing the [`_internal_value`](#manim.utils.color.core.ManimColor._internal_value).

* **Parameters:**
  **class_type** (*type* *[*[*ManimColorT*](manim.utils.color.core.md#manim.utils.color.core.ManimColorT) *]*) – The class that is used for conversion. It must be a subclass of
  [`ManimColor`](#manim.utils.color.core.ManimColor) which respects the specification HSV, RGBA, …
* **Returns:**
  A new color object of type `class_type` and the same
  [`_internal_value`](#manim.utils.color.core.ManimColor._internal_value) as the original color.
* **Return type:**
  [ManimColorT](manim.utils.color.core.md#manim.utils.color.core.ManimColorT)

#### invert(with_alpha=False)

Return a new, linearly inverted version of this [`ManimColor`](#manim.utils.color.core.ManimColor) (no
inplace changes).

* **Parameters:**
  **with_alpha** (*bool*) – 

  If `True`, the alpha value will be inverted too. Default is `False`.

  #### NOTE
  Setting `with_alpha=True` can result in unintended behavior where
  objects are not displayed because their new alpha value is suddenly 0 or
  very low.
* **Returns:**
  The linearly inverted [`ManimColor`](#manim.utils.color.core.ManimColor).
* **Return type:**
  [ManimColor](#manim.utils.color.core.ManimColor)

#### lighter(blend=0.2)

Return a new color that is lighter than the current color, i.e.
interpolated with `WHITE`. The opacity is unchanged.

* **Parameters:**
  **blend** (*float*) – The blend ratio for the interpolation, from 0.0 (the current color
  unchanged) to 1.0 (pure white). Default is 0.2, which results in a
  slightly lighter color.
* **Returns:**
  The lighter [`ManimColor`](#manim.utils.color.core.ManimColor).
* **Return type:**
  [ManimColor](#manim.utils.color.core.ManimColor)

#### SEE ALSO
[`darker()`](#manim.utils.color.core.ManimColor.darker)

#### opacity(opacity)

Create a new [`ManimColor`](#manim.utils.color.core.ManimColor) with the given opacity and the same color
values as before.

* **Parameters:**
  **opacity** (*float*) – The new opacity value to be used.
* **Returns:**
  The new [`ManimColor`](#manim.utils.color.core.ManimColor) with the same color values and the new opacity.
* **Return type:**
  [ManimColor](#manim.utils.color.core.ManimColor)

#### *classmethod* parse(color: [ParsableManimColor](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) | None, alpha: float = 1.0) → Self

#### *classmethod* parse(color: Sequence[[ParsableManimColor](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)], alpha: float = 1.0) → list[Self]

Parse one color as a [`ManimColor`](#manim.utils.color.core.ManimColor) or a sequence of colors as a list of
[`ManimColor`](#manim.utils.color.core.ManimColor)’s.

* **Parameters:**
  * **color** – The color or list of colors to parse. Note that this function can not accept
    tuples: it will assume that you mean `Sequence[ParsableManimColor]` and will
    return a `list[ManimColor]`.
  * **alpha** – The alpha (opacity) value to use for the passed color(s).
* **Returns:**
  Either a list of colors or a singular color, depending on the input.
* **Return type:**
  [ManimColor](#manim.utils.color.core.ManimColor) | list[[ManimColor](#manim.utils.color.core.ManimColor)]

#### to_hex(with_alpha=False)

Convert the [`ManimColor`](#manim.utils.color.core.ManimColor) to a hexadecimal representation of the color.

* **Parameters:**
  **with_alpha** (*bool*) – If `True`, append 2 extra characters to the hex string which represent the
  alpha value of the color between 0 and 255. Default is `False`.
* **Returns:**
  A hex string starting with a `#`, with either 6 or 8 nibbles depending on
  the `with_alpha` parameter. By default, it has 6 nibbles, i.e. `#XXXXXX`.
* **Return type:**
  str

#### to_hsl()

Convert the [`ManimColor`](#manim.utils.color.core.ManimColor) to an HSL array.

#### NOTE
Be careful: this returns an array in the form `[h, s, l]`, where the
elements are floats. This might be confusing, because RGB can also be an array
of floats. You might want to annotate the usage of this function in your code
by typing your HSL array variables as `HSL_Array_Float` in order to
differentiate them from RGB arrays.

* **Returns:**
  An HSL array of 3 floats from 0.0 to 1.0.
* **Return type:**
  HSL_Array_Float

#### to_hsv()

Convert the [`ManimColor`](#manim.utils.color.core.ManimColor) to an HSV array.

#### NOTE
Be careful: this returns an array in the form `[h, s, v]`, where the
elements are floats. This might be confusing, because RGB can also be an array
of floats. You might want to annotate the usage of this function in your code
by typing your HSV array variables as `HSV_Array_Float` in order to
differentiate them from RGB arrays.

* **Returns:**
  An HSV array of 3 floats from 0.0 to 1.0.
* **Return type:**
  HSV_Array_Float

#### to_int_rgb()

Convert the current [`ManimColor`](#manim.utils.color.core.ManimColor) into an RGB array of integers.

* **Returns:**
  RGB array of 3 integers from 0 to 255.
* **Return type:**
  RGB_Array_Int

#### to_int_rgba()

Convert the current ManimColor into an RGBA array of integers.

* **Returns:**
  RGBA array of 4 integers from 0 to 255.
* **Return type:**
  RGBA_Array_Int

#### to_int_rgba_with_alpha(alpha)

Convert the current [`ManimColor`](#manim.utils.color.core.ManimColor) into an RGBA array of integers. This
is similar to [`to_int_rgba()`](#manim.utils.color.core.ManimColor.to_int_rgba), but you can change the alpha value.

* **Parameters:**
  **alpha** (*float*) – Alpha value to be used for the return value. Pass a float between 0.0 and
  1.0: it will automatically be scaled to an integer between 0 and 255.
* **Returns:**
  RGBA array of 4 integers from 0 to 255.
* **Return type:**
  RGBA_Array_Int

#### to_integer()

Convert the current [`ManimColor`](#manim.utils.color.core.ManimColor) into an integer.

#### WARNING
This will return only the RGB part of the color.

* **Returns:**
  Integer representation of the color.
* **Return type:**
  int

#### to_rgb()

Convert the current [`ManimColor`](#manim.utils.color.core.ManimColor) into an RGB array of floats.

* **Returns:**
  RGB array of 3 floats from 0.0 to 1.0.
* **Return type:**
  RGB_Array_Float

#### to_rgba()

Convert the current [`ManimColor`](#manim.utils.color.core.ManimColor) into an RGBA array of floats.

* **Returns:**
  RGBA array of 4 floats from 0.0 to 1.0.
* **Return type:**
  RGBA_Array_Float

#### to_rgba_with_alpha(alpha)

Convert the current [`ManimColor`](#manim.utils.color.core.ManimColor) into an RGBA array of floats. This is
similar to [`to_rgba()`](#manim.utils.color.core.ManimColor.to_rgba), but you can change the alpha value.

* **Parameters:**
  **alpha** (*float*) – Alpha value to be used in the return value.
* **Returns:**
  RGBA array of 4 floats from 0.0 to 1.0.
* **Return type:**
  RGBA_Array_Float
