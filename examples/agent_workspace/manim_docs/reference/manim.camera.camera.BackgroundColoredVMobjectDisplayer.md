# BackgroundColoredVMobjectDisplayer

Qualified name: `manim.camera.camera.BackgroundColoredVMobjectDisplayer`

### *class* BackgroundColoredVMobjectDisplayer(camera)

Bases: `object`

Auxiliary class that handles displaying vectorized mobjects with
a set background image.

* **Parameters:**
  **camera** ([*Camera*](manim.camera.camera.Camera.md#manim.camera.camera.Camera)) – Camera object to use.

### Methods

| [`display`](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.display)                                                   | Displays the colored VMobjects.                               |
|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| [`get_background_array`](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.get_background_array)                         | Gets the background array that has the passed file_name.      |
| `reset_pixel_array`                                                                                                            |                                                               |
| [`resize_background_array`](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array)                   | Resizes the pixel array representing the background.          |
| [`resize_background_array_to_match`](#manim.camera.camera.BackgroundColoredVMobjectDisplayer.resize_background_array_to_match) | Resizes the background array to match the passed pixel array. |

#### display(\*cvmobjects)

Displays the colored VMobjects.

* **Parameters:**
  **\*cvmobjects** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The VMobjects
* **Returns:**
  The pixel array with the cvmobjects displayed.
* **Return type:**
  np.array

#### get_background_array(image)

Gets the background array that has the passed file_name.

* **Parameters:**
  **image** (*Image* *|* *Path* *|* *str*) – The background image or its file name.
* **Returns:**
  The pixel array of the image.
* **Return type:**
  np.ndarray

#### resize_background_array(background_array, new_width, new_height, mode='RGBA')

Resizes the pixel array representing the background.

* **Parameters:**
  * **background_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray)) – The pixel
  * **new_width** (*float*) – The new width of the background
  * **new_height** (*float*) – The new height of the background
  * **mode** (*str*) – The PIL image mode, by default “RGBA”
* **Returns:**
  The numpy pixel array of the resized background.
* **Return type:**
  np.array

#### resize_background_array_to_match(background_array, pixel_array)

Resizes the background array to match the passed pixel array.

* **Parameters:**
  * **background_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray)) – The prospective pixel array.
  * **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray)) – The pixel array whose width and height should be matched.
* **Returns:**
  The resized background array.
* **Return type:**
  np.array
