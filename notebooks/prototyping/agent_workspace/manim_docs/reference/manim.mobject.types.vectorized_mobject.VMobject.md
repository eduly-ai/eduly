# VMobject

Qualified name: `manim.mobject.types.vectorized\_mobject.VMobject`

### *class* VMobject(fill_color=None, fill_opacity=0.0, stroke_color=None, stroke_opacity=1.0, stroke_width=4, background_stroke_color=ManimColor('#000000'), background_stroke_opacity=1.0, background_stroke_width=0, sheen_factor=0.0, joint_type=None, sheen_direction=array([-1., 1., 0.]), close_new_points=False, pre_function_handle_to_anchor_scale_factor=0.01, make_smooth_after_applying_functions=False, background_image=None, shade_in_3d=False, tolerance_for_point_equality=1e-06, n_points_per_cubic_curve=4, cap_style=CapStyleType.AUTO, \*\*kwargs)

Bases: [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

A vectorized mobject.

* **Parameters:**
  * **background_stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – The purpose of background stroke is to have something
    that won’t overlap fill, e.g.  For text against some
    textured background.
  * **sheen_factor** (*float*) – When a color c is set, there will be a second color
    computed based on interpolating c to WHITE by with
    sheen_factor, and the display will gradient to this
    secondary color in the direction of sheen_direction.
  * **close_new_points** (*bool*) – Indicates that it will not be displayed, but
    that it should count in parent mobject’s path
  * **tolerance_for_point_equality** (*float*) – This is within a pixel
  * **joint_type** ([*LineJointType*](manim.constants.LineJointType.md#manim.constants.LineJointType) *|* *None*) – The line joint type used to connect the curve segments
    of this vectorized mobject. See [`LineJointType`](manim.constants.LineJointType.md#manim.constants.LineJointType)
    for options.
  * **fill_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **fill_opacity** (*float*)
  * **stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **stroke_opacity** (*float*)
  * **stroke_width** (*float*)
  * **background_stroke_opacity** (*float*)
  * **background_stroke_width** (*float*)
  * **sheen_direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **pre_function_handle_to_anchor_scale_factor** (*float*)
  * **make_smooth_after_applying_functions** (*bool*)
  * **background_image** (*Image* *|* *str* *|* *None*)
  * **shade_in_3d** (*bool*)
  * **n_points_per_cubic_curve** (*int*)
  * **cap_style** ([*CapStyleType*](manim.constants.CapStyleType.md#manim.constants.CapStyleType))
  * **kwargs** (*Any*)

### Methods

| `add_cubic_bezier_curve`                                                                                                      |                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`add_cubic_bezier_curve_to`](#manim.mobject.types.vectorized_mobject.VMobject.add_cubic_bezier_curve_to)                     | Add cubic bezier curve to the path.                                                                                                                                                                                                                                                                                                       |
| `add_cubic_bezier_curves`                                                                                                     |                                                                                                                                                                                                                                                                                                                                           |
| [`add_line_to`](#manim.mobject.types.vectorized_mobject.VMobject.add_line_to)                                                 | Add a straight line from the last point of VMobject to the given point.                                                                                                                                                                                                                                                                   |
| [`add_points_as_corners`](#manim.mobject.types.vectorized_mobject.VMobject.add_points_as_corners)                             | Append multiple straight lines at the end of `VMobject.points`, which connect the given `points` in order starting from the end of the current path.                                                                                                                                                                                      |
| [`add_quadratic_bezier_curve_to`](#manim.mobject.types.vectorized_mobject.VMobject.add_quadratic_bezier_curve_to)             | Add Quadratic bezier curve to the path.                                                                                                                                                                                                                                                                                                   |
| [`add_smooth_curve_to`](#manim.mobject.types.vectorized_mobject.VMobject.add_smooth_curve_to)                                 | Creates a smooth curve from given points and add it to the VMobject.                                                                                                                                                                                                                                                                      |
| `add_subpath`                                                                                                                 |                                                                                                                                                                                                                                                                                                                                           |
| [`align_points`](#manim.mobject.types.vectorized_mobject.VMobject.align_points)                                               | Adds points to self and vmobject so that they both have the same number of subpaths, with corresponding subpaths each containing the same number of points.                                                                                                                                                                               |
| `align_rgbas`                                                                                                                 |                                                                                                                                                                                                                                                                                                                                           |
| [`append_points`](#manim.mobject.types.vectorized_mobject.VMobject.append_points)                                             | Append the given `new_points` to the end of `VMobject.points`.                                                                                                                                                                                                                                                                            |
| `append_vectorized_mobject`                                                                                                   |                                                                                                                                                                                                                                                                                                                                           |
| `apply_function`                                                                                                              |                                                                                                                                                                                                                                                                                                                                           |
| [`change_anchor_mode`](#manim.mobject.types.vectorized_mobject.VMobject.change_anchor_mode)                                   | Changes the anchor mode of the bezier curves.                                                                                                                                                                                                                                                                                             |
| `clear_points`                                                                                                                |                                                                                                                                                                                                                                                                                                                                           |
| `close_path`                                                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
| `color_using_background_image`                                                                                                |                                                                                                                                                                                                                                                                                                                                           |
| `consider_points_equals`                                                                                                      |                                                                                                                                                                                                                                                                                                                                           |
| [`consider_points_equals_2d`](#manim.mobject.types.vectorized_mobject.VMobject.consider_points_equals_2d)                     | Determine if two points are close enough to be considered equal.                                                                                                                                                                                                                                                                          |
| `fade`                                                                                                                        |                                                                                                                                                                                                                                                                                                                                           |
| [`force_direction`](#manim.mobject.types.vectorized_mobject.VMobject.force_direction)                                         | Makes sure that points are either directed clockwise or counterclockwise.                                                                                                                                                                                                                                                                 |
| [`gen_cubic_bezier_tuples_from_points`](#manim.mobject.types.vectorized_mobject.VMobject.gen_cubic_bezier_tuples_from_points) | Returns the bezier tuples from an array of points.                                                                                                                                                                                                                                                                                        |
| `gen_subpaths_from_points_2d`                                                                                                 |                                                                                                                                                                                                                                                                                                                                           |
| [`generate_rgbas_array`](#manim.mobject.types.vectorized_mobject.VMobject.generate_rgbas_array)                               | First arg can be either a color, or a tuple/list of colors.                                                                                                                                                                                                                                                                               |
| [`get_anchors`](#manim.mobject.types.vectorized_mobject.VMobject.get_anchors)                                                 | Returns the anchors of the curves forming the VMobject.                                                                                                                                                                                                                                                                                   |
| [`get_anchors_and_handles`](#manim.mobject.types.vectorized_mobject.VMobject.get_anchors_and_handles)                         | Returns anchors1, handles1, handles2, anchors2, where (anchors1[i], handles1[i], handles2[i], anchors2[i]) will be four points defining a cubic bezier curve for any i in range(0, len(anchors1))                                                                                                                                         |
| [`get_arc_length`](#manim.mobject.types.vectorized_mobject.VMobject.get_arc_length)                                           | Return the approximated length of the whole curve.                                                                                                                                                                                                                                                                                        |
| `get_background_image`                                                                                                        |                                                                                                                                                                                                                                                                                                                                           |
| [`get_color`](#manim.mobject.types.vectorized_mobject.VMobject.get_color)                                                     | Returns the color of the [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)                                                                                                                                                                                                                                      |
| `get_cubic_bezier_tuples`                                                                                                     |                                                                                                                                                                                                                                                                                                                                           |
| `get_cubic_bezier_tuples_from_points`                                                                                         |                                                                                                                                                                                                                                                                                                                                           |
| [`get_curve_functions`](#manim.mobject.types.vectorized_mobject.VMobject.get_curve_functions)                                 | Gets the functions for the curves of the mobject.                                                                                                                                                                                                                                                                                         |
| [`get_curve_functions_with_lengths`](#manim.mobject.types.vectorized_mobject.VMobject.get_curve_functions_with_lengths)       | Gets the functions and lengths of the curves for the mobject.                                                                                                                                                                                                                                                                             |
| [`get_direction`](#manim.mobject.types.vectorized_mobject.VMobject.get_direction)                                             | Uses [`shoelace_direction()`](manim.utils.space_ops.md#manim.utils.space_ops.shoelace_direction) to calculate the direction.                                                                                                                                                                                                              |
| [`get_end_anchors`](#manim.mobject.types.vectorized_mobject.VMobject.get_end_anchors)                                         | Return the end anchors of the bezier curves.                                                                                                                                                                                                                                                                                              |
| [`get_fill_color`](#manim.mobject.types.vectorized_mobject.VMobject.get_fill_color)                                           | If there are multiple colors (for gradient) this returns the first one                                                                                                                                                                                                                                                                    |
| `get_fill_colors`                                                                                                             |                                                                                                                                                                                                                                                                                                                                           |
| `get_fill_opacities`                                                                                                          |                                                                                                                                                                                                                                                                                                                                           |
| [`get_fill_opacity`](#manim.mobject.types.vectorized_mobject.VMobject.get_fill_opacity)                                       | If there are multiple opacities, this returns the first                                                                                                                                                                                                                                                                                   |
| `get_fill_rgbas`                                                                                                              |                                                                                                                                                                                                                                                                                                                                           |
| `get_gradient_start_and_end_points`                                                                                           |                                                                                                                                                                                                                                                                                                                                           |
| `get_group_class`                                                                                                             |                                                                                                                                                                                                                                                                                                                                           |
| `get_last_point`                                                                                                              |                                                                                                                                                                                                                                                                                                                                           |
| [`get_mobject_type_class`](#manim.mobject.types.vectorized_mobject.VMobject.get_mobject_type_class)                           | Return the base class of this mobject type.                                                                                                                                                                                                                                                                                               |
| [`get_nth_curve_function`](#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_function)                           | Returns the expression of the nth curve.                                                                                                                                                                                                                                                                                                  |
| [`get_nth_curve_function_with_length`](#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_function_with_length)   | Returns the expression of the nth curve along with its (approximate) length.                                                                                                                                                                                                                                                              |
| [`get_nth_curve_length`](#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_length)                               | Returns the (approximate) length of the nth curve.                                                                                                                                                                                                                                                                                        |
| [`get_nth_curve_length_pieces`](#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_length_pieces)                 | Returns the array of short line lengths used for length approximation.                                                                                                                                                                                                                                                                    |
| [`get_nth_curve_points`](#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_points)                               | Returns the points defining the nth curve of the vmobject.                                                                                                                                                                                                                                                                                |
| [`get_num_curves`](#manim.mobject.types.vectorized_mobject.VMobject.get_num_curves)                                           | Returns the number of curves of the vmobject.                                                                                                                                                                                                                                                                                             |
| [`get_point_mobject`](#manim.mobject.types.vectorized_mobject.VMobject.get_point_mobject)                                     | The simplest [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) to be transformed to or from self.                                                                                                                                                                                                               |
| `get_points_defining_boundary`                                                                                                |                                                                                                                                                                                                                                                                                                                                           |
| `get_sheen_direction`                                                                                                         |                                                                                                                                                                                                                                                                                                                                           |
| `get_sheen_factor`                                                                                                            |                                                                                                                                                                                                                                                                                                                                           |
| [`get_start_anchors`](#manim.mobject.types.vectorized_mobject.VMobject.get_start_anchors)                                     | Returns the start anchors of the bezier curves.                                                                                                                                                                                                                                                                                           |
| `get_stroke_color`                                                                                                            |                                                                                                                                                                                                                                                                                                                                           |
| `get_stroke_colors`                                                                                                           |                                                                                                                                                                                                                                                                                                                                           |
| `get_stroke_opacities`                                                                                                        |                                                                                                                                                                                                                                                                                                                                           |
| `get_stroke_opacity`                                                                                                          |                                                                                                                                                                                                                                                                                                                                           |
| `get_stroke_rgbas`                                                                                                            |                                                                                                                                                                                                                                                                                                                                           |
| `get_stroke_width`                                                                                                            |                                                                                                                                                                                                                                                                                                                                           |
| `get_style`                                                                                                                   |                                                                                                                                                                                                                                                                                                                                           |
| [`get_subcurve`](#manim.mobject.types.vectorized_mobject.VMobject.get_subcurve)                                               | Returns the subcurve of the VMobject between the interval [a, b].                                                                                                                                                                                                                                                                         |
| [`get_subpaths`](#manim.mobject.types.vectorized_mobject.VMobject.get_subpaths)                                               | Returns subpaths formed by the curves of the VMobject.                                                                                                                                                                                                                                                                                    |
| `get_subpaths_from_points`                                                                                                    |                                                                                                                                                                                                                                                                                                                                           |
| `has_new_path_started`                                                                                                        |                                                                                                                                                                                                                                                                                                                                           |
| [`init_colors`](#manim.mobject.types.vectorized_mobject.VMobject.init_colors)                                                 | Initializes the colors.                                                                                                                                                                                                                                                                                                                   |
| [`insert_n_curves`](#manim.mobject.types.vectorized_mobject.VMobject.insert_n_curves)                                         | Inserts n curves to the bezier curves of the vmobject.                                                                                                                                                                                                                                                                                    |
| [`insert_n_curves_to_point_list`](#manim.mobject.types.vectorized_mobject.VMobject.insert_n_curves_to_point_list)             | Given an array of k points defining a bezier curves (anchors and handles), returns points defining exactly k + n bezier curves.                                                                                                                                                                                                           |
| `interpolate_color`                                                                                                           |                                                                                                                                                                                                                                                                                                                                           |
| `is_closed`                                                                                                                   |                                                                                                                                                                                                                                                                                                                                           |
| `make_jagged`                                                                                                                 |                                                                                                                                                                                                                                                                                                                                           |
| `make_smooth`                                                                                                                 |                                                                                                                                                                                                                                                                                                                                           |
| `match_background_image`                                                                                                      |                                                                                                                                                                                                                                                                                                                                           |
| `match_style`                                                                                                                 |                                                                                                                                                                                                                                                                                                                                           |
| [`point_from_proportion`](#manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion)                             | Gets the point at a proportion along the path of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).                                                                                                                                                                                                                      |
| [`pointwise_become_partial`](#manim.mobject.types.vectorized_mobject.VMobject.pointwise_become_partial)                       | Given a 2nd [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) `vmobject`, a lower bound `a` and an upper bound `b`, modify this [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)'s points to match the portion of the Bézier spline described by `vmobject.points` with the parameter `t` between `a` and `b`. |
| [`proportion_from_point`](#manim.mobject.types.vectorized_mobject.VMobject.proportion_from_point)                             | Returns the proportion along the path of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) a particular given point is at.                                                                                                                                                                                               |
| [`resize_points`](#manim.mobject.types.vectorized_mobject.VMobject.resize_points)                                             | Resize the array of anchor points and handles to have the specified size.                                                                                                                                                                                                                                                                 |
| [`reverse_direction`](#manim.mobject.types.vectorized_mobject.VMobject.reverse_direction)                                     | Reverts the point direction by inverting the point order.                                                                                                                                                                                                                                                                                 |
| [`rotate`](#manim.mobject.types.vectorized_mobject.VMobject.rotate)                                                           | Rotates the [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) around a specified axis and point.                                                                                                                                                                                                                |
| [`rotate_sheen_direction`](#manim.mobject.types.vectorized_mobject.VMobject.rotate_sheen_direction)                           | Rotates the direction of the applied sheen.                                                                                                                                                                                                                                                                                               |
| [`scale`](#manim.mobject.types.vectorized_mobject.VMobject.scale)                                                             | Scale the size by a factor.                                                                                                                                                                                                                                                                                                               |
| [`scale_handle_to_anchor_distances`](#manim.mobject.types.vectorized_mobject.VMobject.scale_handle_to_anchor_distances)       | If the distance between a given handle point H and its associated anchor point A is d, then it changes H to be a distances factor\*d away from A, but so that the line from A to H doesn't change.                                                                                                                                        |
| [`set_anchors_and_handles`](#manim.mobject.types.vectorized_mobject.VMobject.set_anchors_and_handles)                         | Given two sets of anchors and handles, process them to set them as anchors and handles of the VMobject.                                                                                                                                                                                                                                   |
| `set_background_stroke`                                                                                                       |                                                                                                                                                                                                                                                                                                                                           |
| [`set_cap_style`](#manim.mobject.types.vectorized_mobject.VMobject.set_cap_style)                                             | Sets the cap style of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).                                                                                                                                                                                                                                                 |
| [`set_color`](#manim.mobject.types.vectorized_mobject.VMobject.set_color)                                                     | Condition is function which takes in one arguments, (x, y, z).                                                                                                                                                                                                                                                                            |
| [`set_fill`](#manim.mobject.types.vectorized_mobject.VMobject.set_fill)                                                       | Set the fill color and fill opacity of a [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).                                                                                                                                                                                                                                  |
| `set_opacity`                                                                                                                 |                                                                                                                                                                                                                                                                                                                                           |
| `set_points`                                                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
| [`set_points_as_corners`](#manim.mobject.types.vectorized_mobject.VMobject.set_points_as_corners)                             | Given an array of points, set them as corners of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).                                                                                                                                                                                                                      |
| `set_points_smoothly`                                                                                                         |                                                                                                                                                                                                                                                                                                                                           |
| `set_shade_in_3d`                                                                                                             |                                                                                                                                                                                                                                                                                                                                           |
| [`set_sheen`](#manim.mobject.types.vectorized_mobject.VMobject.set_sheen)                                                     | Applies a color gradient from a direction.                                                                                                                                                                                                                                                                                                |
| [`set_sheen_direction`](#manim.mobject.types.vectorized_mobject.VMobject.set_sheen_direction)                                 | Sets the direction of the applied sheen.                                                                                                                                                                                                                                                                                                  |
| `set_stroke`                                                                                                                  |                                                                                                                                                                                                                                                                                                                                           |
| `set_style`                                                                                                                   |                                                                                                                                                                                                                                                                                                                                           |
| [`start_new_path`](#manim.mobject.types.vectorized_mobject.VMobject.start_new_path)                                           | Append a `point` to the `VMobject.points`, which will be the beginning of a new Bézier curve in the path given by the points.                                                                                                                                                                                                             |
| `update_rgbas_array`                                                                                                          |                                                                                                                                                                                                                                                                                                                                           |

### Attributes

| `animate`                                                                   | Used to animate the application of any method of `self`.               |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------|
| `animation_overrides`                                                       |                                                                        |
| `color`                                                                     |                                                                        |
| `depth`                                                                     | The depth of the mobject.                                              |
| [`fill_color`](#manim.mobject.types.vectorized_mobject.VMobject.fill_color) | If there are multiple colors (for gradient) this returns the first one |
| `height`                                                                    | The height of the mobject.                                             |
| `n_points_per_curve`                                                        |                                                                        |
| `sheen_factor`                                                              |                                                                        |
| `stroke_color`                                                              |                                                                        |
| `width`                                                                     | The width of the mobject.                                              |

#### \_assert_valid_submobjects(submobjects)

Check that all submobjects are actually instances of
`Mobject`, and that none of them is `self` (a
`Mobject` cannot contain itself).

This is an auxiliary function called when adding Mobjects to the
`submobjects` list.

This function is intended to be overridden by subclasses such as
[`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject), which should assert that only other VMobjects
may be added into it.

* **Parameters:**
  **submobjects** (*Iterable* *[*[*VMobject*](#manim.mobject.types.vectorized_mobject.VMobject) *]*) – The list containing values to validate.
* **Returns:**
  The Mobject itself.
* **Return type:**
  `Mobject`
* **Raises:**
  * **TypeError** – If any of the values in submobjects is not a `Mobject`.
  * **ValueError** – If there was an attempt to add a `Mobject` as its own
        submobject.

#### \_gen_subpaths_from_points(points, filter_func)

Given an array of points defining the bezier curves of the vmobject, return subpaths formed by these points.
Here, Two bezier curves form a path if at least two of their anchors are evaluated True by the relation defined by filter_func.

The algorithm every bezier tuple (anchors and handles) in `self.points` (by regrouping each n elements, where
n is the number of points per cubic curve)), and evaluate the relation between two anchors with filter_func.
NOTE : The filter_func takes an int n as parameter, and will evaluate the relation between points[n] and points[n - 1]. This should probably be changed so
the function takes two points as parameters.

* **Parameters:**
  * **points** ([*CubicBezierPath*](manim.typing.md#manim.typing.CubicBezierPath)) – points defining the bezier curve.
  * **filter_func** (*Callable* *[* *[**int* *]* *,* *bool* *]*) – Filter-func defining the relation.
* **Returns:**
  subpaths formed by the points.
* **Return type:**
  Iterable[[CubicSpline](manim.typing.md#manim.typing.CubicSpline)]

#### \_original_\_init_\_(fill_color=None, fill_opacity=0.0, stroke_color=None, stroke_opacity=1.0, stroke_width=4, background_stroke_color=ManimColor('#000000'), background_stroke_opacity=1.0, background_stroke_width=0, sheen_factor=0.0, joint_type=None, sheen_direction=array([-1., 1., 0.]), close_new_points=False, pre_function_handle_to_anchor_scale_factor=0.01, make_smooth_after_applying_functions=False, background_image=None, shade_in_3d=False, tolerance_for_point_equality=1e-06, n_points_per_cubic_curve=4, cap_style=CapStyleType.AUTO, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **fill_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **fill_opacity** (*float*)
  * **stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **stroke_opacity** (*float*)
  * **stroke_width** (*float*)
  * **background_stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **background_stroke_opacity** (*float*)
  * **background_stroke_width** (*float*)
  * **sheen_factor** (*float*)
  * **joint_type** ([*LineJointType*](manim.constants.LineJointType.md#manim.constants.LineJointType) *|* *None*)
  * **sheen_direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **close_new_points** (*bool*)
  * **pre_function_handle_to_anchor_scale_factor** (*float*)
  * **make_smooth_after_applying_functions** (*bool*)
  * **background_image** (*Image* *|* *str* *|* *None*)
  * **shade_in_3d** (*bool*)
  * **tolerance_for_point_equality** (*float*)
  * **n_points_per_cubic_curve** (*int*)
  * **cap_style** ([*CapStyleType*](manim.constants.CapStyleType.md#manim.constants.CapStyleType))
  * **kwargs** (*Any*)

#### add_cubic_bezier_curve_to(handle1, handle2, anchor)

Add cubic bezier curve to the path.

NOTE : the first anchor is not a parameter as by default the end of the last sub-path!

* **Parameters:**
  * **handle1** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – first handle
  * **handle2** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – second handle
  * **anchor** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – anchor
* **Returns:**
  `self`
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

#### add_line_to(point)

Add a straight line from the last point of VMobject to the given point.

* **Parameters:**
  **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The end of the straight line.
* **Returns:**
  `self`
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

#### add_points_as_corners(points)

Append multiple straight lines at the end of
`VMobject.points`, which connect the given `points` in order
starting from the end of the current path. These `points` would be
therefore the corners of the new polyline appended to the path.

* **Parameters:**
  **points** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array)) – An array of 3D points representing the corners of the polyline to
  append to `VMobject.points`.
* **Returns:**
  The VMobject itself, after appending the straight lines to its
  path.
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

#### add_quadratic_bezier_curve_to(handle, anchor)

Add Quadratic bezier curve to the path.

* **Returns:**
  `self`
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)
* **Parameters:**
  * **handle** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **anchor** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))

#### add_smooth_curve_to(\*points)

Creates a smooth curve from given points and add it to the VMobject. If two points are passed in, the first is interpreted
as a handle, the second as an anchor.

* **Parameters:**
  **points** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – Points (anchor and handle, or just anchor) to add a smooth curve from
* **Returns:**
  `self`
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)
* **Raises:**
  **ValueError** – If 0 or more than 2 points are given.

#### align_points(vmobject)

Adds points to self and vmobject so that they both have the same number of subpaths, with
corresponding subpaths each containing the same number of points.

Points are added either by subdividing curves evenly along the subpath, or by creating new subpaths consisting
of a single point repeated.

* **Parameters:**
  **vmobject** ([*VMobject*](#manim.mobject.types.vectorized_mobject.VMobject)) – The object to align points with.
* **Returns:**
  `self`
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

#### SEE ALSO
[`interpolate()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.interpolate), [`align_data()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.align_data)

#### append_points(new_points)

Append the given `new_points` to the end of
`VMobject.points`.

* **Parameters:**
  **new_points** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array)) – An array of 3D points to append.
* **Returns:**
  The VMobject itself, after appending `new_points`.
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

#### change_anchor_mode(mode)

Changes the anchor mode of the bezier curves. This will modify the handles.

There can be only two modes, “jagged”, and “smooth”.

* **Returns:**
  `self`
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)
* **Parameters:**
  **mode** (*Literal* *[* *'jagged'* *,*  *'smooth'* *]*)

#### consider_points_equals_2d(p0, p1)

Determine if two points are close enough to be considered equal.

This uses the algorithm from np.isclose(), but expanded here for the
2D point case. NumPy is overkill for such a small question.
:param p0: first point
:param p1: second point

* **Returns:**
  whether two points considered close.
* **Return type:**
  bool
* **Parameters:**
  * **p0** ([*Point2DLike*](manim.typing.md#manim.typing.Point2DLike))
  * **p1** ([*Point2DLike*](manim.typing.md#manim.typing.Point2DLike))

#### *property* fill_color *: [ManimColor](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)*

If there are multiple colors (for gradient)
this returns the first one

#### force_direction(target_direction)

Makes sure that points are either directed clockwise or
counterclockwise.

* **Parameters:**
  **target_direction** (*Literal* *[* *'CW'* *,*  *'CCW'* *]*) – Either `"CW"` or `"CCW"`.
* **Return type:**
  Self

#### gen_cubic_bezier_tuples_from_points(points)

Returns the bezier tuples from an array of points.

self.points is a list of the anchors and handles of the bezier curves of the mobject (ie [anchor1, handle1, handle2, anchor2, anchor3 ..])
This algorithm basically retrieve them by taking an element every n, where n is the number of control points
of the bezier curve.

* **Parameters:**
  **points** ([*CubicBezierPathLike*](manim.typing.md#manim.typing.CubicBezierPathLike)) – Points from which control points will be extracted.
* **Returns:**
  Bezier control points.
* **Return type:**
  tuple

#### generate_rgbas_array(color, opacity)

First arg can be either a color, or a tuple/list of colors.
Likewise, opacity can either be a float, or a tuple of floats.
If self.sheen_factor is not zero, and only
one color was passed in, a second slightly light color
will automatically be added for the gradient

* **Parameters:**
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *Iterable* *[*[*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor) *]*  *|* *None*)
  * **opacity** (*float* *|* *Iterable* *[**float* *]*)
* **Return type:**
  [FloatRGBA](manim.typing.md#manim.typing.FloatRGBA)

#### get_anchors()

Returns the anchors of the curves forming the VMobject.

* **Returns:**
  The anchors.
* **Return type:**
  [Point3D_Array](manim.typing.md#manim.typing.Point3D_Array)

#### get_anchors_and_handles()

Returns anchors1, handles1, handles2, anchors2,
where (anchors1[i], handles1[i], handles2[i], anchors2[i])
will be four points defining a cubic bezier curve
for any i in range(0, len(anchors1))

* **Returns:**
  Iterable of the anchors and handles.
* **Return type:**
  list[Point3D_Array]

#### get_arc_length(sample_points_per_curve=None)

Return the approximated length of the whole curve.

* **Parameters:**
  **sample_points_per_curve** (*int* *|* *None*) – Number of sample points per curve used to approximate the length. More points result in a better approximation.
* **Returns:**
  The length of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).
* **Return type:**
  float

#### get_color()

Returns the color of the [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

### Examples

```default
>>> from manim import Square, RED
>>> Square(color=RED).get_color() == RED
True
```

* **Return type:**
  [*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)

#### get_curve_functions()

Gets the functions for the curves of the mobject.

* **Returns:**
  The functions for the curves.
* **Return type:**
  Iterable[Callable[[float], [Point3D](manim.typing.md#manim.typing.Point3D)]]

#### get_curve_functions_with_lengths(\*\*kwargs)

Gets the functions and lengths of the curves for the mobject.

* **Parameters:**
  **\*\*kwargs** – The keyword arguments passed to [`get_nth_curve_function_with_length()`](#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_function_with_length)
* **Returns:**
  The functions and lengths of the curves.
* **Return type:**
  Iterable[tuple[Callable[[float], [Point3D](manim.typing.md#manim.typing.Point3D)], float]]

#### get_direction()

Uses [`shoelace_direction()`](manim.utils.space_ops.md#manim.utils.space_ops.shoelace_direction) to calculate the direction.
The direction of points determines in which direction the
object is drawn, clockwise or counterclockwise.

### Examples

The default direction of a [`Circle`](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle) is counterclockwise:

```default
>>> from manim import Circle
>>> Circle().get_direction()
'CCW'
```

* **Returns:**
  Either `"CW"` or `"CCW"`.
* **Return type:**
  `str`

#### get_end_anchors()

Return the end anchors of the bezier curves.

* **Returns:**
  Starting anchors
* **Return type:**
  [Point3D_Array](manim.typing.md#manim.typing.Point3D_Array)

#### get_fill_color()

If there are multiple colors (for gradient)
this returns the first one

* **Return type:**
  [*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)

#### get_fill_opacity()

If there are multiple opacities, this returns the
first

* **Return type:**
  [*ManimFloat*](manim.typing.md#manim.typing.ManimFloat)

#### *static* get_mobject_type_class()

Return the base class of this mobject type.

* **Return type:**
  type[[*VMobject*](#manim.mobject.types.vectorized_mobject.VMobject)]

#### get_nth_curve_function(n)

Returns the expression of the nth curve.

* **Parameters:**
  **n** (*int*) – index of the desired curve.
* **Returns:**
  expression of the nth bezier curve.
* **Return type:**
  Callable[float, [Point3D](manim.typing.md#manim.typing.Point3D)]

#### get_nth_curve_function_with_length(n, sample_points=None)

Returns the expression of the nth curve along with its (approximate) length.

* **Parameters:**
  * **n** (*int*) – The index of the desired curve.
  * **sample_points** (*int* *|* *None*) – The number of points to sample to find the length.
* **Returns:**
  * **curve** (*Callable[[float], Point3D]*) – The function for the nth curve.
  * **length** (`float`) – The length of the nth curve.
* **Return type:**
  tuple[*Callable*[[float], [*Point3D*](manim.typing.md#manim.typing.Point3D)], float]

#### get_nth_curve_length(n, sample_points=None)

Returns the (approximate) length of the nth curve.

* **Parameters:**
  * **n** (*int*) – The index of the desired curve.
  * **sample_points** (*int* *|* *None*) – The number of points to sample to find the length.
* **Returns:**
  **length** – The length of the nth curve.
* **Return type:**
  `float`

#### get_nth_curve_length_pieces(n, sample_points=None)

Returns the array of short line lengths used for length approximation.

* **Parameters:**
  * **n** (*int*) – The index of the desired curve.
  * **sample_points** (*int* *|* *None*) – The number of points to sample to find the length.
* **Return type:**
  The short length-pieces of the nth curve.

#### get_nth_curve_points(n)

Returns the points defining the nth curve of the vmobject.

* **Parameters:**
  **n** (*int*) – index of the desired bezier curve.
* **Returns:**
  points defining the nth bezier curve (anchors, handles)
* **Return type:**
  [CubicBezierPoints](manim.typing.md#manim.typing.CubicBezierPoints)

#### get_num_curves()

Returns the number of curves of the vmobject.

* **Returns:**
  number of curves of the vmobject.
* **Return type:**
  int

#### get_point_mobject(center=None)

The simplest [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) to be transformed to or from self.
Should by a point of the appropriate type

* **Parameters:**
  **center** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*)
* **Return type:**
  [VectorizedPoint](manim.mobject.types.vectorized_mobject.VectorizedPoint.md#manim.mobject.types.vectorized_mobject.VectorizedPoint)

#### get_start_anchors()

Returns the start anchors of the bezier curves.

* **Returns:**
  Starting anchors
* **Return type:**
  [Point3D_Array](manim.typing.md#manim.typing.Point3D_Array)

#### get_subcurve(a, b)

Returns the subcurve of the VMobject between the interval [a, b].
The curve is a VMobject itself.

* **Parameters:**
  * **a** (*float*) – The lower bound.
  * **b** (*float*) – The upper bound.
* **Returns:**
  The subcurve between of [a, b]
* **Return type:**
  [VMobject](#manim.mobject.types.vectorized_mobject.VMobject)

#### get_subpaths()

Returns subpaths formed by the curves of the VMobject.

Subpaths are ranges of curves with each pair of consecutive curves having their end/start points coincident.

* **Returns:**
  subpaths.
* **Return type:**
  list[[CubicSpline](manim.typing.md#manim.typing.CubicSpline)]

#### init_colors(propagate_colors=True)

Initializes the colors.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Parameters:**
  **propagate_colors** (*bool*)
* **Return type:**
  Self

#### insert_n_curves(n)

Inserts n curves to the bezier curves of the vmobject.

* **Parameters:**
  **n** (*int*) – Number of curves to insert.
* **Returns:**
  `self`
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

#### insert_n_curves_to_point_list(n, points)

Given an array of k points defining a bezier curves (anchors and handles), returns points defining exactly k + n bezier curves.

* **Parameters:**
  * **n** (*int*) – Number of desired curves.
  * **points** ([*BezierPathLike*](manim.typing.md#manim.typing.BezierPathLike)) – Starting points.
* **Return type:**
  Points generated.

#### point_from_proportion(alpha)

Gets the point at a proportion along the path of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

* **Parameters:**
  **alpha** (*float*) – The proportion along the the path of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).
* **Returns:**
  The point on the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).
* **Return type:**
  `numpy.ndarray`
* **Raises:**
  * **ValueError** – If `alpha` is not between 0 and 1.
  * **Exception** – If the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) has no points.

### Example

#### pointwise_become_partial(vmobject, a, b)

Given a 2nd [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) `vmobject`, a lower bound `a` and
an upper bound `b`, modify this [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)’s points to
match the portion of the Bézier spline described by `vmobject.points`
with the parameter `t` between `a` and `b`.

* **Parameters:**
  * **vmobject** ([*VMobject*](#manim.mobject.types.vectorized_mobject.VMobject)) – The [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) that will serve as a model.
  * **a** (*float*) – The lower bound for `t`.
  * **b** (*float*) – The upper bound for `t`
* **Returns:**
  The [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) itself, after the transformation.
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)
* **Raises:**
  **TypeError** – If `vmobject` is not an instance of [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

#### proportion_from_point(point)

Returns the proportion along the path of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)
a particular given point is at.

* **Parameters:**
  **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – The Cartesian coordinates of the point which may or may not lie on the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)
* **Returns:**
  The proportion along the path of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).
* **Return type:**
  float
* **Raises:**
  * **ValueError** – If `point` does not lie on the curve.
  * **Exception** – If the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject) has no points.

#### resize_points(new_length, resize_func=<function resize_array>)

Resize the array of anchor points and handles to have
the specified size.

* **Parameters:**
  * **new_length** (*int*) – The new (total) number of points.
  * **resize_func** (*Callable* *[* *[*[*Point3D_Array*](manim.typing.md#manim.typing.Point3D_Array) *,* *int* *]* *,* [*Point3D_Array*](manim.typing.md#manim.typing.Point3D_Array) *]*) – A function mapping a Numpy array (the points) and an integer
    (the target size) to a Numpy array. The default implementation
    is based on Numpy’s `resize` function.
* **Return type:**
  Self

#### reverse_direction()

Reverts the point direction by inverting the point order.

* **Returns:**
  Returns self.
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

### Examples

#### rotate(angle, axis=array([0., 0., 1.]), \*, about_point=None, about_edge=None)

Rotates the [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) around a specified axis and point.

* **Parameters:**
  * **angle** (*float*) – The angle of rotation in radians. Predefined constants such as `DEGREES`
    can also be used to specify the angle in degrees.
  * **axis** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The rotation axis (see [`Rotating`](manim.animation.rotation.Rotating.md#manim.animation.rotation.Rotating) for more).
  * **about_point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*) – The point about which the mobject rotates. If `None`, rotation occurs around
    the center of the mobject.
  * **about_edge** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike) *|* *None*) – The edge about which to apply the scaling.
* **Returns:**
  `self` (for method chaining)
* **Return type:**
  `Mobject`

#### NOTE
To animate a rotation, use [`Rotating`](manim.animation.rotation.Rotating.md#manim.animation.rotation.Rotating) or [`Rotate`](manim.animation.rotation.Rotate.md#manim.animation.rotation.Rotate)
instead of `.animate.rotate(...)`.
The `.animate.rotate(...)` syntax only applies a transformation
from the initial state to the final rotated state
(interpolation between the two states), without showing proper rotational motion
based on the angle (from 0 to the given angle).

### Examples

#### SEE ALSO
[`Rotating`](manim.animation.rotation.Rotating.md#manim.animation.rotation.Rotating), [`Rotate`](manim.animation.rotation.Rotate.md#manim.animation.rotation.Rotate), [`animate`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.animate), `apply_points_function_about_point()`

#### rotate_sheen_direction(angle, axis=array([0., 0., 1.]), family=True)

Rotates the direction of the applied sheen.

* **Parameters:**
  * **angle** (*float*) – Angle by which the direction of sheen is rotated.
  * **axis** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – Axis of rotation.
  * **family** (*bool*)
* **Return type:**
  Self

### Examples

Normal usage:

```default
Circle().set_sheen_direction(UP).rotate_sheen_direction(PI)
```

#### SEE ALSO
[`set_sheen_direction()`](#manim.mobject.types.vectorized_mobject.VMobject.set_sheen_direction)

#### scale(scale_factor, scale_stroke=False, \*, about_point=None, about_edge=None)

Scale the size by a factor.

Default behavior is to scale about the center of the vmobject.

* **Parameters:**
  * **scale_factor** (*float*) – The scaling factor $\alpha$. If $0 < |\alpha| < 1$, the mobject
    will shrink, and for $|\alpha| > 1$ it will grow. Furthermore,
    if $\alpha < 0$, the mobject is also flipped.
  * **scale_stroke** (*bool*) – Boolean determining if the object’s outline is scaled when the object is scaled.
    If enabled, and object with 2px outline is scaled by a factor of .5, it will have an outline of 1px.
  * **kwargs** – Additional keyword arguments passed to
    [`scale()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.scale).
  * **about_point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*)
  * **about_edge** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike) *|* *None*)
* **Returns:**
  `self`
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

### Examples

#### SEE ALSO
`move_to()`

#### scale_handle_to_anchor_distances(factor)

If the distance between a given handle point H and its associated
anchor point A is d, then it changes H to be a distances factor\*d
away from A, but so that the line from A to H doesn’t change.
This is mostly useful in the context of applying a (differentiable)
function, to preserve tangency properties.  One would pull all the
handles closer to their anchors, apply the function then push them out
again.

* **Parameters:**
  **factor** (*float*) – The factor used for scaling.
* **Returns:**
  `self`
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

#### set_anchors_and_handles(anchors1, handles1, handles2, anchors2)

Given two sets of anchors and handles, process them to set them as anchors
and handles of the VMobject.

anchors1[i], handles1[i], handles2[i] and anchors2[i] define the i-th bezier
curve of the vmobject. There are four hardcoded parameters and this is a
problem as it makes the number of points per cubic curve unchangeable from 4
(two anchors and two handles).

* **Returns:**
  `self`
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)
* **Parameters:**
  * **anchors1** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array))
  * **handles1** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array))
  * **handles2** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array))
  * **anchors2** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array))

#### set_cap_style(cap_style)

Sets the cap style of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

* **Parameters:**
  **cap_style** ([*CapStyleType*](manim.constants.CapStyleType.md#manim.constants.CapStyleType)) – The cap style to be set. See [`CapStyleType`](manim.constants.CapStyleType.md#manim.constants.CapStyleType) for options.
* **Returns:**
  `self`
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

### Examples

#### set_color(color, family=True)

Condition is function which takes in one arguments, (x, y, z).
Here it just recurses to submobjects, but in subclasses this
should be further implemented based on the the inner workings
of color

* **Parameters:**
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **family** (*bool*)
* **Return type:**
  Self

#### set_fill(color=None, opacity=None, family=True)

Set the fill color and fill opacity of a [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

* **Parameters:**
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – Fill color of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).
  * **opacity** (*float* *|* *None*) – Fill opacity of the [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).
  * **family** (*bool*) – If `True`, the fill color of all submobjects is also set.
* **Returns:**
  `self`
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

### Examples

#### SEE ALSO
`set_style()`

#### set_points_as_corners(points)

Given an array of points, set them as corners of the
[`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject).

To achieve that, this algorithm sets handles aligned with the anchors
such that the resultant Bézier curve will be the segment between the
two anchors.

* **Parameters:**
  **points** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array)) – Array of points that will be set as corners.
* **Returns:**
  The VMobject itself, after setting the new points as corners.
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)

### Examples

#### set_sheen(factor, direction=None, family=True)

Applies a color gradient from a direction.

* **Parameters:**
  * **factor** (*float*) – The extent of lustre/gradient to apply. If negative, the gradient
    starts from black, if positive the gradient starts from white and
    changes to the current color.
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike) *|* *None*) – Direction from where the gradient is applied.
  * **family** (*bool*)
* **Return type:**
  Self

### Examples

#### set_sheen_direction(direction, family=True)

Sets the direction of the applied sheen.

* **Parameters:**
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – Direction from where the gradient is applied.
  * **family** (*bool*)
* **Return type:**
  Self

### Examples

Normal usage:

```default
Circle().set_sheen_direction(UP)
```

#### SEE ALSO
[`set_sheen()`](#manim.mobject.types.vectorized_mobject.VMobject.set_sheen), [`rotate_sheen_direction()`](#manim.mobject.types.vectorized_mobject.VMobject.rotate_sheen_direction)

#### start_new_path(point)

Append a `point` to the `VMobject.points`, which will be the
beginning of a new Bézier curve in the path given by the points. If
there’s an unfinished curve at the end of `VMobject.points`,
complete it by appending the last Bézier curve’s start anchor as many
times as needed.

* **Parameters:**
  **point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)) – A 3D point to append to `VMobject.points`.
* **Returns:**
  The VMobject itself, after appending `point` and starting a new
  curve.
* **Return type:**
  [`VMobject`](#manim.mobject.types.vectorized_mobject.VMobject)
