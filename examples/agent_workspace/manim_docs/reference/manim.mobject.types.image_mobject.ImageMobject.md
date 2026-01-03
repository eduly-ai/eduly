# ImageMobject

Qualified name: `manim.mobject.types.image\_mobject.ImageMobject`

### *class* ImageMobject(filename_or_array, scale_to_resolution=1080, invert=False, image_mode='RGBA', \*\*kwargs)

Bases: [`AbstractImageMobject`](manim.mobject.types.image_mobject.AbstractImageMobject.md#manim.mobject.types.image_mobject.AbstractImageMobject)

Displays an Image from a numpy array or a file.

* **Parameters:**
  * **scale_to_resolution** (*int*) – At this resolution the image is placed pixel by pixel onto the screen, so it
    will look the sharpest and best.
    This is a custom parameter of ImageMobject so that rendering a scene with
    e.g. the `--quality low` or `--quality medium` flag for faster rendering
    won’t effect the position of the image on the screen.
  * **filename_or_array** ([*StrPath*](manim.typing.md#manim.typing.StrPath) *|* *npt.NDArray*)
  * **invert** (*bool*)
  * **image_mode** (*str*)
  * **kwargs** (*Any*)

### Example

Changing interpolation style:

### Methods

| [`fade`](#manim.mobject.types.image_mobject.ImageMobject.fade)                           | Sets the image's opacity using a 1 - alpha relationship.                                                                   |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [`get_pixel_array`](#manim.mobject.types.image_mobject.ImageMobject.get_pixel_array)     | A simple getter method.                                                                                                    |
| `get_style`                                                                              |                                                                                                                            |
| [`interpolate_color`](#manim.mobject.types.image_mobject.ImageMobject.interpolate_color) | Interpolates the array of pixel color values from one ImageMobject into an array of equal size in the target ImageMobject. |
| [`set_color`](#manim.mobject.types.image_mobject.ImageMobject.set_color)                 | Condition is function which takes in one arguments, (x, y, z).                                                             |
| [`set_opacity`](#manim.mobject.types.image_mobject.ImageMobject.set_opacity)             | Sets the image's opacity.                                                                                                  |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.   |
|-----------------------|------------------------------------------------------------|
| `animation_overrides` |                                                            |
| `depth`               | The depth of the mobject.                                  |
| `height`              | The height of the mobject.                                 |
| `width`               | The width of the mobject.                                  |

#### \_original_\_init_\_(filename_or_array, scale_to_resolution=1080, invert=False, image_mode='RGBA', \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **filename_or_array** ([*StrPath*](manim.typing.md#manim.typing.StrPath) *|* *npt.NDArray*)
  * **scale_to_resolution** (*int*)
  * **invert** (*bool*)
  * **image_mode** (*str*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### fade(darkness=0.5, family=True)

Sets the image’s opacity using a 1 - alpha relationship.

* **Parameters:**
  * **darkness** (*float*) – The alpha value of the object, 1 being transparent and 0 being
    opaque.
  * **family** (*bool*) – Whether the submobjects of the ImageMobject should be affected.
* **Return type:**
  Self

#### get_pixel_array()

A simple getter method.

#### interpolate_color(mobject1, mobject2, alpha)

Interpolates the array of pixel color values from one ImageMobject
into an array of equal size in the target ImageMobject.

* **Parameters:**
  * **mobject1** ([*ImageMobject*](#manim.mobject.types.image_mobject.ImageMobject)) – The ImageMobject to transform from.
  * **mobject2** ([*ImageMobject*](#manim.mobject.types.image_mobject.ImageMobject)) – The ImageMobject to transform into.
  * **alpha** (*float*) – Used to track the lerp relationship. Not opacity related.
* **Return type:**
  None

#### set_color(color, alpha=None, family=True)

Condition is function which takes in one arguments, (x, y, z).
Here it just recurses to submobjects, but in subclasses this
should be further implemented based on the the inner workings
of color

#### set_opacity(alpha)

Sets the image’s opacity.

* **Parameters:**
  **alpha** (*float*) – The alpha value of the object, 1 being opaque and 0 being
  transparent.
* **Return type:**
  Self
