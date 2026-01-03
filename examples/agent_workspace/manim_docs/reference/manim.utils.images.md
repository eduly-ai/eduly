# images

Image manipulation utilities.

### Functions

### change_to_rgba_array(image, dtype='uint8')

Converts an RGB array into RGBA with the alpha value opacity maxed.

* **Parameters:**
  * **image** ([*RGBPixelArray*](manim.typing.md#manim.typing.RGBPixelArray))
  * **dtype** (*str*)
* **Return type:**
  [*RGBAPixelArray*](manim.typing.md#manim.typing.RGBAPixelArray)

### drag_pixels(frames)

* **Parameters:**
  **frames** (*Sequence* *[*[*PixelArray*](manim.typing.md#manim.typing.PixelArray) *]*)
* **Return type:**
  list[np.ndarray]

### get_full_raster_image_path(image_file_name)

* **Parameters:**
  **image_file_name** (*str* *|* *PurePath*)
* **Return type:**
  *Path*

### get_full_vector_image_path(image_file_name)

* **Parameters:**
  **image_file_name** (*str* *|* *PurePath*)
* **Return type:**
  *Path*

### invert_image(image)

* **Parameters:**
  **image** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray))
* **Return type:**
  <module ‘PIL.Image’ from ‘/Users/nbilla/Documents/GitHub/nivibilla/eduly/manim/.venv/lib/python3.12/site-packages/PIL/Image.py’>
