# AbstractImageMobject

Qualified name: `manim.mobject.types.image\_mobject.AbstractImageMobject`

### *class* AbstractImageMobject(scale_to_resolution, pixel_array_dtype='uint8', resampling_algorithm=Resampling.BICUBIC, \*\*kwargs)

Bases: [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

Automatically filters out black pixels

* **Parameters:**
  * **scale_to_resolution** (*int*) – At this resolution the image is placed pixel by pixel onto the screen, so it
    will look the sharpest and best.
    This is a custom parameter of ImageMobject so that rendering a scene with
    e.g. the `--quality low` or `--quality medium` flag for faster rendering
    won’t effect the position of the image on the screen.
  * **pixel_array_dtype** (*str*)
  * **resampling_algorithm** (*Resampling*)
  * **kwargs** (*Any*)

### Methods

| `get_pixel_array`                                                                                              |                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| [`reset_points`](#manim.mobject.types.image_mobject.AbstractImageMobject.reset_points)                         | Sets `points` to be the four image corners.                    |
| [`set_color`](#manim.mobject.types.image_mobject.AbstractImageMobject.set_color)                               | Condition is function which takes in one arguments, (x, y, z). |
| [`set_resampling_algorithm`](#manim.mobject.types.image_mobject.AbstractImageMobject.set_resampling_algorithm) | Sets the interpolation method for upscaling the image.         |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.   |
|-----------------------|------------------------------------------------------------|
| `animation_overrides` |                                                            |
| `depth`               | The depth of the mobject.                                  |
| `height`              | The height of the mobject.                                 |
| `width`               | The width of the mobject.                                  |

#### \_original_\_init_\_(scale_to_resolution, pixel_array_dtype='uint8', resampling_algorithm=Resampling.BICUBIC, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **scale_to_resolution** (*int*)
  * **pixel_array_dtype** (*str*)
  * **resampling_algorithm** (*Resampling*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### reset_points()

Sets `points` to be the four image corners.

* **Return type:**
  None

#### set_color(color, alpha=None, family=True)

Condition is function which takes in one arguments, (x, y, z).
Here it just recurses to submobjects, but in subclasses this
should be further implemented based on the the inner workings
of color

#### set_resampling_algorithm(resampling_algorithm)

Sets the interpolation method for upscaling the image. By default the image is
interpolated using bicubic algorithm. This method lets you change it.
Interpolation is done internally using Pillow, and the function besides the
string constants describing the algorithm accepts the Pillow integer constants.

* **Parameters:**
  **resampling_algorithm** (*int*) – 

  An integer constant described in the Pillow library,
  or one from the RESAMPLING_ALGORITHMS global dictionary,
  under the following keys:
  * ’bicubic’ or ‘cubic’
  * ’nearest’ or ‘none’
  * ’box’
  * ’bilinear’ or ‘linear’
  * ’hamming’
  * ’lanczos’ or ‘antialias’
* **Return type:**
  Self
