# Camera

Qualified name: `manim.camera.camera.Camera`

### *class* Camera(background_image=None, frame_center=array([0., 0., 0.]), image_mode='RGBA', n_channels=4, pixel_array_dtype='uint8', cairo_line_width_multiple=0.01, use_z_index=True, background=None, pixel_height=None, pixel_width=None, frame_height=None, frame_width=None, frame_rate=None, background_color=None, background_opacity=None, \*\*kwargs)

Bases: `object`

Base camera class.

This is the object which takes care of what exactly is displayed
on screen at any given moment.

* **Parameters:**
  * **background_image** (*str* *|* *None*) – The path to an image that should be the background image.
    If not set, the background is filled with `self.background_color`
  * **background** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray) *|* *None*) – What `background` is set to. By default, `None`.
  * **pixel_height** (*int* *|* *None*) – The height of the scene in pixels.
  * **pixel_width** (*int* *|* *None*) – The width of the scene in pixels.
  * **kwargs** (*Any*) – Additional arguments (`background_color`, `background_opacity`)
    to be set.
  * **frame_center** ([*Point3D*](manim.typing.md#manim.typing.Point3D))
  * **image_mode** (*str*)
  * **n_channels** (*int*)
  * **pixel_array_dtype** (*str*)
  * **cairo_line_width_multiple** (*float*)
  * **use_z_index** (*bool*)
  * **frame_height** (*float* *|* *None*)
  * **frame_width** (*float* *|* *None*)
  * **frame_rate** (*float* *|* *None*)
  * **background_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **background_opacity** (*float* *|* *None*)

### Methods

| [`adjust_out_of_range_points`](#manim.camera.camera.Camera.adjust_out_of_range_points)                                               | If any of the points in the passed array are out of the viable range, they are adjusted suitably.                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`adjusted_thickness`](#manim.camera.camera.Camera.adjusted_thickness)                                                               | Computes the adjusted stroke width for a zoomed camera.                                                                                                                              |
| [`apply_fill`](#manim.camera.camera.Camera.apply_fill)                                                                               | Fills the cairo context                                                                                                                                                              |
| [`apply_stroke`](#manim.camera.camera.Camera.apply_stroke)                                                                           | Applies a stroke to the VMobject in the cairo context.                                                                                                                               |
| [`cache_cairo_context`](#manim.camera.camera.Camera.cache_cairo_context)                                                             | Caches the passed Pixel array into a Cairo Context                                                                                                                                   |
| [`capture_mobject`](#manim.camera.camera.Camera.capture_mobject)                                                                     | Capture mobjects by storing it in `pixel_array`.                                                                                                                                     |
| [`capture_mobjects`](#manim.camera.camera.Camera.capture_mobjects)                                                                   | Capture mobjects by printing them on `pixel_array`.                                                                                                                                  |
| [`convert_pixel_array`](#manim.camera.camera.Camera.convert_pixel_array)                                                             | Converts a pixel array from values that have floats in then to proper RGB values.                                                                                                    |
| [`display_image_mobject`](#manim.camera.camera.Camera.display_image_mobject)                                                         | Displays an ImageMobject by changing the pixel_array suitably.                                                                                                                       |
| [`display_multiple_background_colored_vmobjects`](#manim.camera.camera.Camera.display_multiple_background_colored_vmobjects)         | Displays multiple vmobjects that have the same color as the background.                                                                                                              |
| [`display_multiple_image_mobjects`](#manim.camera.camera.Camera.display_multiple_image_mobjects)                                     | Displays multiple image mobjects by modifying the passed pixel_array.                                                                                                                |
| [`display_multiple_non_background_colored_vmobjects`](#manim.camera.camera.Camera.display_multiple_non_background_colored_vmobjects) | Displays multiple VMobjects in the cairo context, as long as they don't have background colors.                                                                                      |
| [`display_multiple_point_cloud_mobjects`](#manim.camera.camera.Camera.display_multiple_point_cloud_mobjects)                         | Displays multiple PMobjects by modifying the passed pixel array.                                                                                                                     |
| [`display_multiple_vectorized_mobjects`](#manim.camera.camera.Camera.display_multiple_vectorized_mobjects)                           | Displays multiple VMobjects in the pixel_array                                                                                                                                       |
| [`display_point_cloud`](#manim.camera.camera.Camera.display_point_cloud)                                                             | Displays a PMobject by modifying the pixel array suitably.                                                                                                                           |
| [`display_vectorized`](#manim.camera.camera.Camera.display_vectorized)                                                               | Displays a VMobject in the cairo context                                                                                                                                             |
| [`get_background_colored_vmobject_displayer`](#manim.camera.camera.Camera.get_background_colored_vmobject_displayer)                 | Returns the background_colored_vmobject_displayer if it exists or makes one and returns it if not.                                                                                   |
| [`get_cached_cairo_context`](#manim.camera.camera.Camera.get_cached_cairo_context)                                                   | Returns the cached cairo context of the passed pixel array if it exists, and None if it doesn't.                                                                                     |
| [`get_cairo_context`](#manim.camera.camera.Camera.get_cairo_context)                                                                 | Returns the cairo context for a pixel array after caching it to self.pixel_array_to_cairo_context If that array has already been cached, it returns the cached version instead.      |
| [`get_coords_of_all_pixels`](#manim.camera.camera.Camera.get_coords_of_all_pixels)                                                   | Returns the cartesian coordinates of each pixel.                                                                                                                                     |
| [`get_fill_rgbas`](#manim.camera.camera.Camera.get_fill_rgbas)                                                                       | Returns the RGBA array of the fill of the passed VMobject                                                                                                                            |
| [`get_image`](#manim.camera.camera.Camera.get_image)                                                                                 | Returns an image from the passed pixel array, or from the current frame if the passed pixel array is none.                                                                           |
| [`get_mobjects_to_display`](#manim.camera.camera.Camera.get_mobjects_to_display)                                                     | Used to get the list of mobjects to display with the camera.                                                                                                                         |
| [`get_stroke_rgbas`](#manim.camera.camera.Camera.get_stroke_rgbas)                                                                   | Gets the RGBA array for the stroke of the passed VMobject.                                                                                                                           |
| [`get_thickening_nudges`](#manim.camera.camera.Camera.get_thickening_nudges)                                                         | Determine a list of vectors used to nudge two-dimensional pixel coordinates.                                                                                                         |
| [`init_background`](#manim.camera.camera.Camera.init_background)                                                                     | Initialize the background.                                                                                                                                                           |
| [`is_in_frame`](#manim.camera.camera.Camera.is_in_frame)                                                                             | Checks whether the passed mobject is in frame or not.                                                                                                                                |
| [`make_background_from_func`](#manim.camera.camera.Camera.make_background_from_func)                                                 | Makes a pixel array for the background by using coords_to_colors_func to determine each pixel's color.                                                                               |
| [`on_screen_pixels`](#manim.camera.camera.Camera.on_screen_pixels)                                                                   | Returns array of pixels that are on the screen from a given array of pixel_coordinates                                                                                               |
| [`overlay_PIL_image`](#manim.camera.camera.Camera.overlay_PIL_image)                                                                 | Overlays a PIL image on the passed pixel array.                                                                                                                                      |
| [`overlay_rgba_array`](#manim.camera.camera.Camera.overlay_rgba_array)                                                               | Overlays an RGBA array on top of the given Pixel array.                                                                                                                              |
| `points_to_pixel_coords`                                                                                                             |                                                                                                                                                                                      |
| [`reset`](#manim.camera.camera.Camera.reset)                                                                                         | Resets the camera's pixel array to that of the background                                                                                                                            |
| [`reset_pixel_shape`](#manim.camera.camera.Camera.reset_pixel_shape)                                                                 | This method resets the height and width of a single pixel to the passed new_height and new_width.                                                                                    |
| [`resize_frame_shape`](#manim.camera.camera.Camera.resize_frame_shape)                                                               | Changes frame_shape to match the aspect ratio of the pixels, where fixed_dimension determines whether frame_height or frame_width remains fixed while the other changes accordingly. |
| [`set_background`](#manim.camera.camera.Camera.set_background)                                                                       | Sets the background to the passed pixel_array after converting to valid RGB values.                                                                                                  |
| [`set_background_from_func`](#manim.camera.camera.Camera.set_background_from_func)                                                   | Sets the background to a pixel array using coords_to_colors_func to determine each pixel's color.                                                                                    |
| [`set_cairo_context_color`](#manim.camera.camera.Camera.set_cairo_context_color)                                                     | Sets the color of the cairo context                                                                                                                                                  |
| [`set_cairo_context_path`](#manim.camera.camera.Camera.set_cairo_context_path)                                                       | Sets a path for the cairo context with the vmobject passed                                                                                                                           |
| `set_frame_to_background`                                                                                                            |                                                                                                                                                                                      |
| [`set_pixel_array`](#manim.camera.camera.Camera.set_pixel_array)                                                                     | Sets the pixel array of the camera to the passed pixel array.                                                                                                                        |
| [`thickened_coordinates`](#manim.camera.camera.Camera.thickened_coordinates)                                                         | Returns thickened coordinates for a passed array of pixel coords and a thickness to thicken by.                                                                                      |
| `transform_points_pre_display`                                                                                                       |                                                                                                                                                                                      |
| [`type_or_raise`](#manim.camera.camera.Camera.type_or_raise)                                                                         | Return the type of mobject, if it is a type that can be rendered.                                                                                                                    |

### Attributes

| `background_color`   |    |
|----------------------|----|
| `background_opacity` |    |

#### adjust_out_of_range_points(points)

If any of the points in the passed array are out of
the viable range, they are adjusted suitably.

* **Parameters:**
  **points** (*ndarray*) – The points to adjust
* **Returns:**
  The adjusted points.
* **Return type:**
  np.array

#### adjusted_thickness(thickness)

Computes the adjusted stroke width for a zoomed camera.

* **Parameters:**
  **thickness** (*float*) – The stroke width of a mobject.
* **Returns:**
  The adjusted stroke width that reflects zooming in with
  the camera.
* **Return type:**
  float

#### apply_fill(ctx, vmobject)

Fills the cairo context

* **Parameters:**
  * **ctx** (*Context*) – The cairo context
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The VMobject
* **Returns:**
  The camera object.
* **Return type:**
  [Camera](#manim.camera.camera.Camera)

#### apply_stroke(ctx, vmobject, background=False)

Applies a stroke to the VMobject in the cairo context.

* **Parameters:**
  * **ctx** (*Context*) – The cairo context
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The VMobject
  * **background** (*bool*) – Whether or not to consider the background when applying this
    stroke width, by default False
* **Returns:**
  The camera object with the stroke applied.
* **Return type:**
  [Camera](#manim.camera.camera.Camera)

#### cache_cairo_context(pixel_array, ctx)

Caches the passed Pixel array into a Cairo Context

* **Parameters:**
  * **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray)) – The pixel array to cache
  * **ctx** (*Context*) – The context to cache it into.
* **Return type:**
  None

#### capture_mobject(mobject, \*\*kwargs)

Capture mobjects by storing it in `pixel_array`.

This is a single-mobject version of [`capture_mobjects()`](#manim.camera.camera.Camera.capture_mobjects).

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – Mobject to capture.
  * **kwargs** (*Any*) – Keyword arguments to be passed to [`get_mobjects_to_display()`](#manim.camera.camera.Camera.get_mobjects_to_display).
* **Return type:**
  None

#### capture_mobjects(mobjects, \*\*kwargs)

Capture mobjects by printing them on `pixel_array`.

This is the essential function that converts the contents of a Scene
into an array, which is then converted to an image or video.

* **Parameters:**
  * **mobjects** (*Iterable* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – Mobjects to capture.
  * **kwargs** (*Any*) – Keyword arguments to be passed to [`get_mobjects_to_display()`](#manim.camera.camera.Camera.get_mobjects_to_display).
* **Return type:**
  None

### Notes

For a list of classes that can currently be rendered, see `display_funcs()`.

#### convert_pixel_array(pixel_array, convert_from_floats=False)

Converts a pixel array from values that have floats in then
to proper RGB values.

* **Parameters:**
  * **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray) *|* *list* *|* *tuple*) – Pixel array to convert.
  * **convert_from_floats** (*bool*) – Whether or not to convert float values to ints, by default False
* **Returns:**
  The new, converted pixel array.
* **Return type:**
  np.array

#### display_image_mobject(image_mobject, pixel_array)

Displays an ImageMobject by changing the pixel_array suitably.

* **Parameters:**
  * **image_mobject** ([*AbstractImageMobject*](manim.mobject.types.image_mobject.AbstractImageMobject.md#manim.mobject.types.image_mobject.AbstractImageMobject)) – The imageMobject to display
  * **pixel_array** (*np.ndarray*) – The Pixel array to put the imagemobject in.
* **Return type:**
  None

#### display_multiple_background_colored_vmobjects(cvmobjects, pixel_array)

Displays multiple vmobjects that have the same color as the background.

* **Parameters:**
  * **cvmobjects** (*Iterable* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*) – List of Colored VMobjects
  * **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray)) – The pixel array.
* **Returns:**
  The camera object.
* **Return type:**
  [Camera](#manim.camera.camera.Camera)

#### display_multiple_image_mobjects(image_mobjects, pixel_array)

Displays multiple image mobjects by modifying the passed pixel_array.

* **Parameters:**
  * **image_mobjects** (*Iterable* *[*[*AbstractImageMobject*](manim.mobject.types.image_mobject.AbstractImageMobject.md#manim.mobject.types.image_mobject.AbstractImageMobject) *]*) – list of ImageMobjects
  * **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray)) – The pixel array to modify.
* **Return type:**
  None

#### display_multiple_non_background_colored_vmobjects(vmobjects, pixel_array)

Displays multiple VMobjects in the cairo context, as long as they don’t have
background colors.

* **Parameters:**
  * **vmobjects** (*Iterable* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*) – list of the VMobjects
  * **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray)) – The Pixel array to add the VMobjects to.
* **Return type:**
  None

#### display_multiple_point_cloud_mobjects(pmobjects, pixel_array)

Displays multiple PMobjects by modifying the passed pixel array.

* **Parameters:**
  * **pmobjects** (*Iterable* *[*[*PMobject*](manim.mobject.types.point_cloud_mobject.PMobject.md#manim.mobject.types.point_cloud_mobject.PMobject) *]*) – List of PMobjects
  * **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray)) – The pixel array to modify.
* **Return type:**
  None

#### display_multiple_vectorized_mobjects(vmobjects, pixel_array)

Displays multiple VMobjects in the pixel_array

* **Parameters:**
  * **vmobjects** (*list* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*) – list of VMobjects to display
  * **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray)) – The pixel array
* **Return type:**
  None

#### display_point_cloud(pmobject, points, rgbas, thickness, pixel_array)

Displays a PMobject by modifying the pixel array suitably.

TODO: Write a description for the rgbas argument.

* **Parameters:**
  * **pmobject** ([*PMobject*](manim.mobject.types.point_cloud_mobject.PMobject.md#manim.mobject.types.point_cloud_mobject.PMobject)) – Point Cloud Mobject
  * **points** ([*Point3D_Array*](manim.typing.md#manim.typing.Point3D_Array)) – The points to display in the point cloud mobject
  * **rgbas** ([*FloatRGBA_Array*](manim.typing.md#manim.typing.FloatRGBA_Array))
  * **thickness** (*float*) – The thickness of each point of the PMobject
  * **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray)) – The pixel array to modify.
* **Return type:**
  None

#### display_vectorized(vmobject, ctx)

Displays a VMobject in the cairo context

* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The Vectorized Mobject to display
  * **ctx** (*Context*) – The cairo context to use.
* **Returns:**
  The camera object
* **Return type:**
  [Camera](#manim.camera.camera.Camera)

#### get_background_colored_vmobject_displayer()

Returns the background_colored_vmobject_displayer
if it exists or makes one and returns it if not.

* **Returns:**
  Object that displays VMobjects that have the same color
  as the background.
* **Return type:**
  [BackgroundColoredVMobjectDisplayer](manim.camera.camera.BackgroundColoredVMobjectDisplayer.md#manim.camera.camera.BackgroundColoredVMobjectDisplayer)

#### get_cached_cairo_context(pixel_array)

Returns the cached cairo context of the passed
pixel array if it exists, and None if it doesn’t.

* **Parameters:**
  **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray)) – The pixel array to check.
* **Returns:**
  The cached cairo context.
* **Return type:**
  cairo.Context

#### get_cairo_context(pixel_array)

Returns the cairo context for a pixel array after
caching it to self.pixel_array_to_cairo_context
If that array has already been cached, it returns the
cached version instead.

* **Parameters:**
  **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray)) – The Pixel array to get the cairo context of.
* **Returns:**
  The cairo context of the pixel array.
* **Return type:**
  cairo.Context

#### get_coords_of_all_pixels()

Returns the cartesian coordinates of each pixel.

* **Returns:**
  The array of cartesian coordinates.
* **Return type:**
  np.ndarray

#### get_fill_rgbas(vmobject)

Returns the RGBA array of the fill of the passed VMobject

* **Parameters:**
  **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The VMobject
* **Returns:**
  The RGBA Array of the fill of the VMobject
* **Return type:**
  np.array

#### get_image(pixel_array=None)

Returns an image from the passed
pixel array, or from the current frame
if the passed pixel array is none.

* **Parameters:**
  **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray) *|* *list* *|* *tuple* *|* *None*) – The pixel array from which to get an image, by default None
* **Returns:**
  The PIL image of the array.
* **Return type:**
  PIL.Image.Image

#### get_mobjects_to_display(mobjects, include_submobjects=True, excluded_mobjects=None)

Used to get the list of mobjects to display
with the camera.

* **Parameters:**
  * **mobjects** (*Iterable* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The Mobjects
  * **include_submobjects** (*bool*) – Whether or not to include the submobjects of mobjects, by default True
  * **excluded_mobjects** (*list* *|* *None*) – Any mobjects to exclude, by default None
* **Returns:**
  list of mobjects
* **Return type:**
  list

#### get_stroke_rgbas(vmobject, background=False)

Gets the RGBA array for the stroke of the passed
VMobject.

* **Parameters:**
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The VMobject
  * **background** (*bool*) – Whether or not to consider the background when getting the stroke
    RGBAs, by default False
* **Returns:**
  The RGBA array of the stroke.
* **Return type:**
  np.ndarray

#### get_thickening_nudges(thickness)

Determine a list of vectors used to nudge
two-dimensional pixel coordinates.

* **Parameters:**
  **thickness** (*float*)
* **Return type:**
  np.array

#### init_background()

Initialize the background.
If self.background_image is the path of an image
the image is set as background; else, the default
background color fills the background.

* **Return type:**
  None

#### is_in_frame(mobject)

Checks whether the passed mobject is in
frame or not.

* **Parameters:**
  **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject for which the checking needs to be done.
* **Returns:**
  True if in frame, False otherwise.
* **Return type:**
  bool

#### make_background_from_func(coords_to_colors_func)

Makes a pixel array for the background by using coords_to_colors_func to determine each pixel’s color. Each input
pixel’s color. Each input to coords_to_colors_func is an (x, y) pair in space (in ordinary space coordinates; not
pixel coordinates), and each output is expected to be an RGBA array of 4 floats.

* **Parameters:**
  **coords_to_colors_func** (*Callable* *[* *[**ndarray* *]* *,* *ndarray* *]*) – The function whose input is an (x,y) pair of coordinates and
  whose return values must be the colors for that point
* **Returns:**
  The pixel array which can then be passed to set_background.
* **Return type:**
  np.array

#### on_screen_pixels(pixel_coords)

Returns array of pixels that are on the screen from a given
array of pixel_coordinates

* **Parameters:**
  **pixel_coords** (*ndarray*) – The pixel coords to check.
* **Returns:**
  The pixel coords on screen.
* **Return type:**
  np.array

#### overlay_PIL_image(pixel_array, image)

Overlays a PIL image on the passed pixel array.

* **Parameters:**
  * **pixel_array** (*ndarray*) – The Pixel array
  * **image** ( *<module 'PIL.Image' from '/Users/nbilla/Documents/GitHub/nivibilla/eduly/manim/.venv/lib/python3.12/site-packages/PIL/Image.py'>*) – The Image to overlay.
* **Return type:**
  None

#### overlay_rgba_array(pixel_array, new_array)

Overlays an RGBA array on top of the given Pixel array.

* **Parameters:**
  * **pixel_array** (*ndarray*) – The original pixel array to modify.
  * **new_array** (*ndarray*) – The new pixel array to overlay.
* **Return type:**
  None

#### reset()

Resets the camera’s pixel array
to that of the background

* **Returns:**
  The camera object after setting the pixel array.
* **Return type:**
  [Camera](#manim.camera.camera.Camera)

#### reset_pixel_shape(new_height, new_width)

This method resets the height and width
of a single pixel to the passed new_height and new_width.

* **Parameters:**
  * **new_height** (*float*) – The new height of the entire scene in pixels
  * **new_width** (*float*) – The new width of the entire scene in pixels
* **Return type:**
  None

#### resize_frame_shape(fixed_dimension=0)

Changes frame_shape to match the aspect ratio
of the pixels, where fixed_dimension determines
whether frame_height or frame_width
remains fixed while the other changes accordingly.

* **Parameters:**
  **fixed_dimension** (*int*) – If 0, height is scaled with respect to width
  else, width is scaled with respect to height.
* **Return type:**
  None

#### set_background(pixel_array, convert_from_floats=False)

Sets the background to the passed pixel_array after converting
to valid RGB values.

* **Parameters:**
  * **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray) *|* *list* *|* *tuple*) – The pixel array to set the background to.
  * **convert_from_floats** (*bool*) – Whether or not to convert floats values to proper RGB valid ones, by default False
* **Return type:**
  None

#### set_background_from_func(coords_to_colors_func)

Sets the background to a pixel array using coords_to_colors_func to determine each pixel’s color. Each input
pixel’s color. Each input to coords_to_colors_func is an (x, y) pair in space (in ordinary space coordinates; not
pixel coordinates), and each output is expected to be an RGBA array of 4 floats.

* **Parameters:**
  **coords_to_colors_func** (*Callable* *[* *[**ndarray* *]* *,* *ndarray* *]*) – The function whose input is an (x,y) pair of coordinates and
  whose return values must be the colors for that point
* **Return type:**
  None

#### set_cairo_context_color(ctx, rgbas, vmobject)

Sets the color of the cairo context

* **Parameters:**
  * **ctx** (*Context*) – The cairo context
  * **rgbas** ([*FloatRGBALike_Array*](manim.typing.md#manim.typing.FloatRGBALike_Array)) – The RGBA array with which to color the context.
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The VMobject with which to set the color.
* **Returns:**
  The camera object
* **Return type:**
  [Camera](#manim.camera.camera.Camera)

#### set_cairo_context_path(ctx, vmobject)

Sets a path for the cairo context with the vmobject passed

* **Parameters:**
  * **ctx** (*Context*) – The cairo context
  * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The VMobject
* **Returns:**
  Camera object after setting cairo_context_path
* **Return type:**
  [Camera](#manim.camera.camera.Camera)

#### set_pixel_array(pixel_array, convert_from_floats=False)

Sets the pixel array of the camera to the passed pixel array.

* **Parameters:**
  * **pixel_array** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray) *|* *list* *|* *tuple*) – The pixel array to convert and then set as the camera’s pixel array.
  * **convert_from_floats** (*bool*) – Whether or not to convert float values to proper RGB values, by default False
* **Return type:**
  None

#### thickened_coordinates(pixel_coords, thickness)

Returns thickened coordinates for a passed array of pixel coords and
a thickness to thicken by.

* **Parameters:**
  * **pixel_coords** (*ndarray*) – Pixel coordinates
  * **thickness** (*float*) – Thickness
* **Returns:**
  Array of thickened pixel coords.
* **Return type:**
  np.array

#### type_or_raise(mobject)

Return the type of mobject, if it is a type that can be rendered.

If mobject is an instance of a class that inherits from a class that
can be rendered, return the super class.  For example, an instance of a
Square is also an instance of VMobject, and these can be rendered.
Therefore, type_or_raise(Square()) returns True.

* **Parameters:**
  **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The object to take the type of.
* **Return type:**
  type[[VMobject](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)] | type[[PMobject](manim.mobject.types.point_cloud_mobject.PMobject.md#manim.mobject.types.point_cloud_mobject.PMobject)] | type[[AbstractImageMobject](manim.mobject.types.image_mobject.AbstractImageMobject.md#manim.mobject.types.image_mobject.AbstractImageMobject)] | type[[Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)]

### Notes

For a list of classes that can currently be rendered, see `display_funcs()`.

* **Returns:**
  The type of mobjects, if it can be rendered.
* **Return type:**
  Type[[`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)]
* **Raises:**
  **TypeError** – When mobject is not an instance of a class that can be rendered.
* **Parameters:**
  **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
