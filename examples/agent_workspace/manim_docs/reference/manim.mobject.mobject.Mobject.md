# Mobject

Qualified name: `manim.mobject.mobject.Mobject`

### *class* Mobject(color=ManimColor('#FFFFFF'), name=None, dim=3, target=None, z_index=0)

Bases: `object`

Mathematical Object: base class for objects that can be displayed on screen.

There is a compatibility layer that allows for
getting and setting generic attributes with `get_*`
and `set_*` methods. See [`set()`](#manim.mobject.mobject.Mobject.set) for more details.

* **Parameters:**
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *list* *[*[*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *]*)
  * **name** (*str* *|* *None*)
  * **dim** (*int*)
  * **z_index** (*float*)

#### submobjects

The contained objects.

* **Type:**
  List[[`Mobject`](#manim.mobject.mobject.Mobject)]

#### points

The points of the objects.

#### SEE ALSO
[`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

* **Type:**
  `numpy.ndarray`

### Methods

| [`add`](#manim.mobject.mobject.Mobject.add)                                               | Add mobjects as submobjects.                                                                                                                                                    |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`add_animation_override`](#manim.mobject.mobject.Mobject.add_animation_override)         | Add an animation override.                                                                                                                                                      |
| [`add_background_rectangle`](#manim.mobject.mobject.Mobject.add_background_rectangle)     | Add a BackgroundRectangle as submobject.                                                                                                                                        |
| `add_background_rectangle_to_family_members_with_points`                                  |                                                                                                                                                                                 |
| `add_background_rectangle_to_submobjects`                                                 |                                                                                                                                                                                 |
| `add_n_more_submobjects`                                                                  |                                                                                                                                                                                 |
| [`add_to_back`](#manim.mobject.mobject.Mobject.add_to_back)                               | Add all passed mobjects to the back of the submobjects.                                                                                                                         |
| [`add_updater`](#manim.mobject.mobject.Mobject.add_updater)                               | Add an update function to this mobject.                                                                                                                                         |
| [`align_data`](#manim.mobject.mobject.Mobject.align_data)                                 | Aligns the family structure and data of this mobject with another mobject.                                                                                                      |
| [`align_on_border`](#manim.mobject.mobject.Mobject.align_on_border)                       | Direction just needs to be a vector pointing towards side or corner in the 2d plane.                                                                                            |
| `align_points`                                                                            |                                                                                                                                                                                 |
| `align_points_with_larger`                                                                |                                                                                                                                                                                 |
| `align_submobjects`                                                                       |                                                                                                                                                                                 |
| [`align_to`](#manim.mobject.mobject.Mobject.align_to)                                     | Aligns mobject to another [`Mobject`](#manim.mobject.mobject.Mobject) in a certain direction.                                                                                   |
| [`animation_override_for`](#manim.mobject.mobject.Mobject.animation_override_for)         | Returns the function defining a specific animation override for this class.                                                                                                     |
| [`apply_complex_function`](#manim.mobject.mobject.Mobject.apply_complex_function)         | Applies a complex function to a [`Mobject`](#manim.mobject.mobject.Mobject).                                                                                                    |
| `apply_function`                                                                          |                                                                                                                                                                                 |
| `apply_function_to_position`                                                              |                                                                                                                                                                                 |
| `apply_function_to_submobject_positions`                                                  |                                                                                                                                                                                 |
| `apply_matrix`                                                                            |                                                                                                                                                                                 |
| `apply_over_attr_arrays`                                                                  |                                                                                                                                                                                 |
| `apply_points_function_about_point`                                                       |                                                                                                                                                                                 |
| [`apply_to_family`](#manim.mobject.mobject.Mobject.apply_to_family)                       | Apply a function to `self` and every submobject with points recursively.                                                                                                        |
| [`arrange`](#manim.mobject.mobject.Mobject.arrange)                                       | Sorts [`Mobject`](#manim.mobject.mobject.Mobject) next to each other on screen.                                                                                                 |
| [`arrange_in_grid`](#manim.mobject.mobject.Mobject.arrange_in_grid)                       | Arrange submobjects in a grid.                                                                                                                                                  |
| [`arrange_submobjects`](#manim.mobject.mobject.Mobject.arrange_submobjects)               | Arrange the position of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects) with a small buffer.                                                                        |
| [`become`](#manim.mobject.mobject.Mobject.become)                                         | Edit points, colors and submobjects to be identical to another [`Mobject`](#manim.mobject.mobject.Mobject)                                                                      |
| [`center`](#manim.mobject.mobject.Mobject.center)                                         | Moves the center of the mobject to the center of the scene.                                                                                                                     |
| [`clear_updaters`](#manim.mobject.mobject.Mobject.clear_updaters)                         | Remove every updater.                                                                                                                                                           |
| [`copy`](#manim.mobject.mobject.Mobject.copy)                                             | Create and return an identical copy of the [`Mobject`](#manim.mobject.mobject.Mobject) including all [`submobjects`](#manim.mobject.mobject.Mobject.submobjects).               |
| `fade`                                                                                    |                                                                                                                                                                                 |
| `fade_to`                                                                                 |                                                                                                                                                                                 |
| [`family_members_with_points`](#manim.mobject.mobject.Mobject.family_members_with_points) | Filters the list of family members (generated by [`get_family()`](#manim.mobject.mobject.Mobject.get_family)) to include only mobjects with points.                             |
| [`flip`](#manim.mobject.mobject.Mobject.flip)                                             | Flips/Mirrors an mobject about its center.                                                                                                                                      |
| [`generate_points`](#manim.mobject.mobject.Mobject.generate_points)                       | Initializes [`points`](#manim.mobject.mobject.Mobject.points) and therefore the shape.                                                                                          |
| `generate_target`                                                                         |                                                                                                                                                                                 |
| [`get_all_points`](#manim.mobject.mobject.Mobject.get_all_points)                         | Return all points from this mobject and all submobjects.                                                                                                                        |
| `get_array_attrs`                                                                         |                                                                                                                                                                                 |
| [`get_bottom`](#manim.mobject.mobject.Mobject.get_bottom)                                 | Get bottom Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject)                                                                                           |
| `get_boundary_point`                                                                      |                                                                                                                                                                                 |
| [`get_center`](#manim.mobject.mobject.Mobject.get_center)                                 | Get center Point3Ds                                                                                                                                                             |
| `get_center_of_mass`                                                                      |                                                                                                                                                                                 |
| [`get_color`](#manim.mobject.mobject.Mobject.get_color)                                   | Returns the color of the [`Mobject`](#manim.mobject.mobject.Mobject)                                                                                                            |
| [`get_coord`](#manim.mobject.mobject.Mobject.get_coord)                                   | Meant to generalize `get_x`, `get_y` and `get_z`                                                                                                                                |
| [`get_corner`](#manim.mobject.mobject.Mobject.get_corner)                                 | Get corner Point3Ds for certain direction.                                                                                                                                      |
| [`get_critical_point`](#manim.mobject.mobject.Mobject.get_critical_point)                 | Picture a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject).                                                                                                         |
| [`get_edge_center`](#manim.mobject.mobject.Mobject.get_edge_center)                       | Get edge Point3Ds for certain direction.                                                                                                                                        |
| [`get_end`](#manim.mobject.mobject.Mobject.get_end)                                       | Returns the point, where the stroke that surrounds the [`Mobject`](#manim.mobject.mobject.Mobject) ends.                                                                        |
| `get_extremum_along_dim`                                                                  |                                                                                                                                                                                 |
| [`get_family`](#manim.mobject.mobject.Mobject.get_family)                                 | Lists all mobjects in the hierarchy (family) of the given mobject, including the mobject itself and all its submobjects recursively.                                            |
| `get_family_updaters`                                                                     |                                                                                                                                                                                 |
| `get_group_class`                                                                         |                                                                                                                                                                                 |
| `get_image`                                                                               |                                                                                                                                                                                 |
| [`get_left`](#manim.mobject.mobject.Mobject.get_left)                                     | Get left Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject)                                                                                             |
| [`get_merged_array`](#manim.mobject.mobject.Mobject.get_merged_array)                     | Return all of a given attribute from this mobject and all submobjects.                                                                                                          |
| [`get_midpoint`](#manim.mobject.mobject.Mobject.get_midpoint)                             | Get Point3Ds of the middle of the path that forms the  [`Mobject`](#manim.mobject.mobject.Mobject).                                                                             |
| [`get_mobject_type_class`](#manim.mobject.mobject.Mobject.get_mobject_type_class)         | Return the base class of this mobject type.                                                                                                                                     |
| [`get_nadir`](#manim.mobject.mobject.Mobject.get_nadir)                                   | Get nadir (opposite the zenith) Point3Ds of a box bounding a 3D [`Mobject`](#manim.mobject.mobject.Mobject).                                                                    |
| `get_num_points`                                                                          |                                                                                                                                                                                 |
| `get_pieces`                                                                              |                                                                                                                                                                                 |
| [`get_point_mobject`](#manim.mobject.mobject.Mobject.get_point_mobject)                   | The simplest [`Mobject`](#manim.mobject.mobject.Mobject) to be transformed to or from self.                                                                                     |
| `get_points_defining_boundary`                                                            |                                                                                                                                                                                 |
| [`get_right`](#manim.mobject.mobject.Mobject.get_right)                                   | Get right Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject)                                                                                            |
| [`get_start`](#manim.mobject.mobject.Mobject.get_start)                                   | Returns the point, where the stroke that surrounds the [`Mobject`](#manim.mobject.mobject.Mobject) starts.                                                                      |
| [`get_start_and_end`](#manim.mobject.mobject.Mobject.get_start_and_end)                   | Returns starting and ending point of a stroke as a `tuple`.                                                                                                                     |
| [`get_time_based_updaters`](#manim.mobject.mobject.Mobject.get_time_based_updaters)       | Return all updaters using the `dt` parameter.                                                                                                                                   |
| [`get_top`](#manim.mobject.mobject.Mobject.get_top)                                       | Get top Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject)                                                                                              |
| [`get_updaters`](#manim.mobject.mobject.Mobject.get_updaters)                             | Return all updaters.                                                                                                                                                            |
| [`get_x`](#manim.mobject.mobject.Mobject.get_x)                                           | Returns x Point3D of the center of the [`Mobject`](#manim.mobject.mobject.Mobject) as `float`                                                                                   |
| [`get_y`](#manim.mobject.mobject.Mobject.get_y)                                           | Returns y Point3D of the center of the [`Mobject`](#manim.mobject.mobject.Mobject) as `float`                                                                                   |
| [`get_z`](#manim.mobject.mobject.Mobject.get_z)                                           | Returns z Point3D of the center of the [`Mobject`](#manim.mobject.mobject.Mobject) as `float`                                                                                   |
| `get_z_index_reference_point`                                                             |                                                                                                                                                                                 |
| [`get_zenith`](#manim.mobject.mobject.Mobject.get_zenith)                                 | Get zenith Point3Ds of a box bounding a 3D [`Mobject`](#manim.mobject.mobject.Mobject).                                                                                         |
| [`has_no_points`](#manim.mobject.mobject.Mobject.has_no_points)                           | Check if [`Mobject`](#manim.mobject.mobject.Mobject) *does not* contains points.                                                                                                |
| [`has_points`](#manim.mobject.mobject.Mobject.has_points)                                 | Check if [`Mobject`](#manim.mobject.mobject.Mobject) contains points.                                                                                                           |
| [`has_time_based_updater`](#manim.mobject.mobject.Mobject.has_time_based_updater)         | Test if `self` has a time based updater.                                                                                                                                        |
| [`init_colors`](#manim.mobject.mobject.Mobject.init_colors)                               | Initializes the colors.                                                                                                                                                         |
| [`insert`](#manim.mobject.mobject.Mobject.insert)                                         | Inserts a mobject at a specific position into self.submobjects                                                                                                                  |
| [`interpolate`](#manim.mobject.mobject.Mobject.interpolate)                               | Turns this [`Mobject`](#manim.mobject.mobject.Mobject) into an interpolation between `mobject1` and `mobject2`.                                                                 |
| `interpolate_color`                                                                       |                                                                                                                                                                                 |
| [`invert`](#manim.mobject.mobject.Mobject.invert)                                         | Inverts the list of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects).                                                                                                |
| `is_off_screen`                                                                           |                                                                                                                                                                                 |
| [`length_over_dim`](#manim.mobject.mobject.Mobject.length_over_dim)                       | Measure the length of an [`Mobject`](#manim.mobject.mobject.Mobject) in a certain direction.                                                                                    |
| [`match_color`](#manim.mobject.mobject.Mobject.match_color)                               | Match the color with the color of another [`Mobject`](#manim.mobject.mobject.Mobject).                                                                                          |
| [`match_coord`](#manim.mobject.mobject.Mobject.match_coord)                               | Match the Point3Ds with the Point3Ds of another [`Mobject`](#manim.mobject.mobject.Mobject).                                                                                    |
| [`match_depth`](#manim.mobject.mobject.Mobject.match_depth)                               | Match the depth with the depth of another [`Mobject`](#manim.mobject.mobject.Mobject).                                                                                          |
| [`match_dim_size`](#manim.mobject.mobject.Mobject.match_dim_size)                         | Match the specified dimension with the dimension of another [`Mobject`](#manim.mobject.mobject.Mobject).                                                                        |
| [`match_height`](#manim.mobject.mobject.Mobject.match_height)                             | Match the height with the height of another [`Mobject`](#manim.mobject.mobject.Mobject).                                                                                        |
| [`match_points`](#manim.mobject.mobject.Mobject.match_points)                             | Edit points, positions, and submobjects to be identical to another [`Mobject`](#manim.mobject.mobject.Mobject), while keeping the style unchanged.                              |
| [`match_updaters`](#manim.mobject.mobject.Mobject.match_updaters)                         | Match the updaters of the given mobject.                                                                                                                                        |
| [`match_width`](#manim.mobject.mobject.Mobject.match_width)                               | Match the width with the width of another [`Mobject`](#manim.mobject.mobject.Mobject).                                                                                          |
| [`match_x`](#manim.mobject.mobject.Mobject.match_x)                                       | Match x coord.                                                                                                                                                                  |
| [`match_y`](#manim.mobject.mobject.Mobject.match_y)                                       | Match y coord.                                                                                                                                                                  |
| [`match_z`](#manim.mobject.mobject.Mobject.match_z)                                       | Match z coord.                                                                                                                                                                  |
| [`move_to`](#manim.mobject.mobject.Mobject.move_to)                                       | Move center of the [`Mobject`](#manim.mobject.mobject.Mobject) to certain Point3D.                                                                                              |
| [`next_to`](#manim.mobject.mobject.Mobject.next_to)                                       | Move this [`Mobject`](#manim.mobject.mobject.Mobject) next to another's [`Mobject`](#manim.mobject.mobject.Mobject) or Point3D.                                                 |
| `nonempty_submobjects`                                                                    |                                                                                                                                                                                 |
| [`null_point_align`](#manim.mobject.mobject.Mobject.null_point_align)                     | If a [`Mobject`](#manim.mobject.mobject.Mobject) with points is being aligned to one without, treat both as groups, and push the one with points into its own submobjects list. |
| `point_from_proportion`                                                                   |                                                                                                                                                                                 |
| `pose_at_angle`                                                                           |                                                                                                                                                                                 |
| `proportion_from_point`                                                                   |                                                                                                                                                                                 |
| `push_self_into_submobjects`                                                              |                                                                                                                                                                                 |
| `put_start_and_end_on`                                                                    |                                                                                                                                                                                 |
| [`reduce_across_dimension`](#manim.mobject.mobject.Mobject.reduce_across_dimension)       | Find the min or max value from a dimension across all points in this and submobjects.                                                                                           |
| [`remove`](#manim.mobject.mobject.Mobject.remove)                                         | Remove [`submobjects`](#manim.mobject.mobject.Mobject.submobjects).                                                                                                             |
| [`remove_updater`](#manim.mobject.mobject.Mobject.remove_updater)                         | Remove an updater.                                                                                                                                                              |
| [`repeat`](#manim.mobject.mobject.Mobject.repeat)                                         | This can make transition animations nicer                                                                                                                                       |
| `repeat_submobject`                                                                       |                                                                                                                                                                                 |
| `replace`                                                                                 |                                                                                                                                                                                 |
| `rescale_to_fit`                                                                          |                                                                                                                                                                                 |
| [`reset_points`](#manim.mobject.mobject.Mobject.reset_points)                             | Sets [`points`](#manim.mobject.mobject.Mobject.points) to be an empty array.                                                                                                    |
| [`restore`](#manim.mobject.mobject.Mobject.restore)                                       | Restores the state that was previously saved with [`save_state()`](#manim.mobject.mobject.Mobject.save_state).                                                                  |
| [`resume_updating`](#manim.mobject.mobject.Mobject.resume_updating)                       | Enable updating from updaters and animations.                                                                                                                                   |
| `reverse_points`                                                                          |                                                                                                                                                                                 |
| [`rotate`](#manim.mobject.mobject.Mobject.rotate)                                         | Rotates the [`Mobject`](#manim.mobject.mobject.Mobject) around a specified axis and point.                                                                                      |
| [`rotate_about_origin`](#manim.mobject.mobject.Mobject.rotate_about_origin)               | Rotates the [`Mobject`](#manim.mobject.mobject.Mobject) about the ORIGIN, which is at [0,0,0].                                                                                  |
| [`save_image`](#manim.mobject.mobject.Mobject.save_image)                                 | Saves an image of only this [`Mobject`](#manim.mobject.mobject.Mobject) at its position to a png file.                                                                          |
| [`save_state`](#manim.mobject.mobject.Mobject.save_state)                                 | Save the current state (position, color & size).                                                                                                                                |
| [`scale`](#manim.mobject.mobject.Mobject.scale)                                           | Scale the size by a factor.                                                                                                                                                     |
| [`scale_to_fit_depth`](#manim.mobject.mobject.Mobject.scale_to_fit_depth)                 | Scales the [`Mobject`](#manim.mobject.mobject.Mobject) to fit a depth while keeping width/height proportional.                                                                  |
| [`scale_to_fit_height`](#manim.mobject.mobject.Mobject.scale_to_fit_height)               | Scales the [`Mobject`](#manim.mobject.mobject.Mobject) to fit a height while keeping width/depth proportional.                                                                  |
| [`scale_to_fit_width`](#manim.mobject.mobject.Mobject.scale_to_fit_width)                 | Scales the [`Mobject`](#manim.mobject.mobject.Mobject) to fit a width while keeping height/depth proportional.                                                                  |
| [`set`](#manim.mobject.mobject.Mobject.set)                                               | Sets attributes.                                                                                                                                                                |
| [`set_color`](#manim.mobject.mobject.Mobject.set_color)                                   | Condition is function which takes in one arguments, (x, y, z).                                                                                                                  |
| [`set_color_by_gradient`](#manim.mobject.mobject.Mobject.set_color_by_gradient)           |                                                                                                                                                                                 |
| `set_colors_by_radial_gradient`                                                           |                                                                                                                                                                                 |
| `set_coord`                                                                               |                                                                                                                                                                                 |
| [`set_default`](#manim.mobject.mobject.Mobject.set_default)                               | Sets the default values of keyword arguments.                                                                                                                                   |
| `set_submobject_colors_by_gradient`                                                       |                                                                                                                                                                                 |
| `set_submobject_colors_by_radial_gradient`                                                |                                                                                                                                                                                 |
| [`set_x`](#manim.mobject.mobject.Mobject.set_x)                                           | Set x value of the center of the [`Mobject`](#manim.mobject.mobject.Mobject) (`int` or `float`)                                                                                 |
| [`set_y`](#manim.mobject.mobject.Mobject.set_y)                                           | Set y value of the center of the [`Mobject`](#manim.mobject.mobject.Mobject) (`int` or `float`)                                                                                 |
| [`set_z`](#manim.mobject.mobject.Mobject.set_z)                                           | Set z value of the center of the [`Mobject`](#manim.mobject.mobject.Mobject) (`int` or `float`)                                                                                 |
| [`set_z_index`](#manim.mobject.mobject.Mobject.set_z_index)                               | Sets the [`Mobject`](#manim.mobject.mobject.Mobject)'s `z_index` to the value specified in z_index_value.                                                                       |
| [`set_z_index_by_z_Point3D`](#manim.mobject.mobject.Mobject.set_z_index_by_z_Point3D)     | Sets the [`Mobject`](#manim.mobject.mobject.Mobject)'s z Point3D to the value of `z_index`.                                                                                     |
| [`shift`](#manim.mobject.mobject.Mobject.shift)                                           | Shift by the given vectors.                                                                                                                                                     |
| `shift_onto_screen`                                                                       |                                                                                                                                                                                 |
| `show`                                                                                    |                                                                                                                                                                                 |
| [`shuffle`](#manim.mobject.mobject.Mobject.shuffle)                                       | Shuffles the list of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects).                                                                                               |
| [`shuffle_submobjects`](#manim.mobject.mobject.Mobject.shuffle_submobjects)               | Shuffles the order of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects)                                                                                               |
| [`sort`](#manim.mobject.mobject.Mobject.sort)                                             | Sorts the list of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects) by a function defined by `submob_func`.                                                           |
| [`sort_submobjects`](#manim.mobject.mobject.Mobject.sort_submobjects)                     | Sort the [`submobjects`](#manim.mobject.mobject.Mobject.submobjects)                                                                                                            |
| `space_out_submobjects`                                                                   |                                                                                                                                                                                 |
| `split`                                                                                   |                                                                                                                                                                                 |
| `stretch`                                                                                 |                                                                                                                                                                                 |
| `stretch_about_point`                                                                     |                                                                                                                                                                                 |
| [`stretch_to_fit_depth`](#manim.mobject.mobject.Mobject.stretch_to_fit_depth)             | Stretches the [`Mobject`](#manim.mobject.mobject.Mobject) to fit a depth, not keeping width/height proportional.                                                                |
| [`stretch_to_fit_height`](#manim.mobject.mobject.Mobject.stretch_to_fit_height)           | Stretches the [`Mobject`](#manim.mobject.mobject.Mobject) to fit a height, not keeping width/depth proportional.                                                                |
| [`stretch_to_fit_width`](#manim.mobject.mobject.Mobject.stretch_to_fit_width)             | Stretches the [`Mobject`](#manim.mobject.mobject.Mobject) to fit a width, not keeping height/depth proportional.                                                                |
| `surround`                                                                                |                                                                                                                                                                                 |
| [`suspend_updating`](#manim.mobject.mobject.Mobject.suspend_updating)                     | Disable updating from updaters and animations.                                                                                                                                  |
| `throw_error_if_no_points`                                                                |                                                                                                                                                                                 |
| [`to_corner`](#manim.mobject.mobject.Mobject.to_corner)                                   | Moves this [`Mobject`](#manim.mobject.mobject.Mobject) to the given corner of the screen.                                                                                       |
| [`to_edge`](#manim.mobject.mobject.Mobject.to_edge)                                       | Moves this [`Mobject`](#manim.mobject.mobject.Mobject) to the given edge of the screen, without affecting its position in the other dimension.                                  |
| `to_original_color`                                                                       |                                                                                                                                                                                 |
| [`update`](#manim.mobject.mobject.Mobject.update)                                         | Apply all updaters.                                                                                                                                                             |

### Attributes

| [`animate`](#manim.mobject.mobject.Mobject.animate)   | Used to animate the application of any method of `self`.   |
|-------------------------------------------------------|------------------------------------------------------------|
| `animation_overrides`                                 |                                                            |
| [`depth`](#manim.mobject.mobject.Mobject.depth)       | The depth of the mobject.                                  |
| [`height`](#manim.mobject.mobject.Mobject.height)     | The height of the mobject.                                 |
| [`width`](#manim.mobject.mobject.Mobject.width)       | The width of the mobject.                                  |

#### *classmethod* \_add_intrinsic_animation_overrides()

Initializes animation overrides marked with the [`override_animation()`](manim.animation.animation.md#manim.animation.animation.override_animation)
decorator.

* **Return type:**
  None

#### \_assert_valid_submobjects(submobjects)

Check that all submobjects are actually instances of
[`Mobject`](#manim.mobject.mobject.Mobject), and that none of them is `self` (a
[`Mobject`](#manim.mobject.mobject.Mobject) cannot contain itself).

This is an auxiliary function called when adding Mobjects to the
[`submobjects`](#manim.mobject.mobject.Mobject.submobjects) list.

This function is intended to be overridden by subclasses such as
`VMobject`, which should assert that only other VMobjects
may be added into it.

* **Parameters:**
  **submobjects** (*Iterable* *[*[*Mobject*](#manim.mobject.mobject.Mobject) *]*) – The list containing values to validate.
* **Returns:**
  The Mobject itself.
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)
* **Raises:**
  * **TypeError** – If any of the values in submobjects is not a [`Mobject`](#manim.mobject.mobject.Mobject).
  * **ValueError** – If there was an attempt to add a [`Mobject`](#manim.mobject.mobject.Mobject) as its own
        submobject.

#### add(\*mobjects)

Add mobjects as submobjects.

The mobjects are added to [`submobjects`](#manim.mobject.mobject.Mobject.submobjects).

Subclasses of mobject may implement `+` and `+=` dunder methods.

* **Parameters:**
  **mobjects** ([*Mobject*](#manim.mobject.mobject.Mobject)) – The mobjects to add.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)
* **Raises:**
  * **ValueError** – When a mobject tries to add itself.
  * **TypeError** – When trying to add an object that is not an instance of [`Mobject`](#manim.mobject.mobject.Mobject).

### Notes

A mobject cannot contain itself, and it cannot contain a submobject
more than once.  If the parent mobject is displayed, the newly-added
submobjects will also be displayed (i.e. they are automatically added
to the parent Scene).

#### SEE ALSO
[`remove()`](#manim.mobject.mobject.Mobject.remove), [`add_to_back()`](#manim.mobject.mobject.Mobject.add_to_back)

### Examples

```default
>>> outer = Mobject()
>>> inner = Mobject()
>>> outer = outer.add(inner)
```

Duplicates are not added again:

```default
>>> outer = outer.add(inner)
>>> len(outer.submobjects)
1
```

Only Mobjects can be added:

```default
>>> outer.add(3)
Traceback (most recent call last):
...
TypeError: Only values of type Mobject can be added as submobjects of Mobject, but the value 3 (at index 0) is of type int.
```

Adding an object to itself raises an error:

```default
>>> outer.add(outer)
Traceback (most recent call last):
...
ValueError: Cannot add Mobject as a submobject of itself (at index 0).
```

A given mobject cannot be added as a submobject
twice to some parent:

```default
>>> parent = Mobject(name="parent")
>>> child = Mobject(name="child")
>>> parent.add(child, child)
[...] WARNING  ...
parent
>>> parent.submobjects
[child]
```

#### *classmethod* add_animation_override(animation_class, override_func)

Add an animation override.

This does not apply to subclasses.

* **Parameters:**
  * **animation_class** (*type* *[*[*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – The animation type to be overridden
  * **override_func** ([*FunctionOverride*](manim.typing.md#manim.typing.FunctionOverride)) – The function returning an animation replacing the default animation. It gets
    passed the parameters given to the animation constructor.
* **Raises:**
  **MultiAnimationOverrideException** – If the overridden animation was already overridden.
* **Return type:**
  None

#### add_background_rectangle(color=None, opacity=0.75, \*\*kwargs)

Add a BackgroundRectangle as submobject.

The BackgroundRectangle is added behind other submobjects.

This can be used to increase the mobjects visibility in front of a noisy background.

* **Parameters:**
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – The color of the BackgroundRectangle
  * **opacity** (*float*) – The opacity of the BackgroundRectangle
  * **kwargs** – Additional keyword arguments passed to the BackgroundRectangle constructor
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### SEE ALSO
[`add_to_back()`](#manim.mobject.mobject.Mobject.add_to_back), [`BackgroundRectangle`](manim.mobject.geometry.shape_matchers.BackgroundRectangle.md#manim.mobject.geometry.shape_matchers.BackgroundRectangle)

#### add_to_back(\*mobjects)

Add all passed mobjects to the back of the submobjects.

If [`submobjects`](#manim.mobject.mobject.Mobject.submobjects) already contains the given mobjects, they just get moved
to the back instead.

* **Parameters:**
  **mobjects** ([*Mobject*](#manim.mobject.mobject.Mobject)) – The mobjects to add.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### NOTE
Technically, this is done by adding (or moving) the mobjects to
the head of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects). The head of this list is rendered
first, which places the corresponding mobjects behind the
subsequent list members.

* **Raises:**
  * **ValueError** – When a mobject tries to add itself.
  * **TypeError** – When trying to add an object that is not an instance of [`Mobject`](#manim.mobject.mobject.Mobject).
* **Parameters:**
  **mobjects** ([*Mobject*](#manim.mobject.mobject.Mobject))
* **Return type:**
  Self

### Notes

A mobject cannot contain itself, and it cannot contain a submobject
more than once.  If the parent mobject is displayed, the newly-added
submobjects will also be displayed (i.e. they are automatically added
to the parent Scene).

#### SEE ALSO
[`remove()`](#manim.mobject.mobject.Mobject.remove), [`add()`](#manim.mobject.mobject.Mobject.add)

#### add_updater(update_function, index=None, call_updater=False)

Add an update function to this mobject.

Update functions, or updaters in short, are functions that are applied to the
Mobject in every frame.

* **Parameters:**
  * **update_function** ([*Updater*](manim.mobject.mobject.md#manim.mobject.mobject.Updater)) – The update function to be added.
    Whenever [`update()`](#manim.mobject.mobject.Mobject.update) is called, this update function gets called using
    `self` as the first parameter.
    The updater can have a second parameter `dt`. If it uses this parameter,
    it gets called using a second value `dt`, usually representing the time
    in seconds since the last call of [`update()`](#manim.mobject.mobject.Mobject.update).
  * **index** (*int* *|* *None*) – The index at which the new updater should be added in `self.updaters`.
    In case `index` is `None` the updater will be added at the end.
  * **call_updater** (*bool*) – Whether or not to call the updater initially. If `True`, the updater will
    be called using `dt=0`.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

### Examples

#### SEE ALSO
[`get_updaters()`](#manim.mobject.mobject.Mobject.get_updaters), [`remove_updater()`](#manim.mobject.mobject.Mobject.remove_updater), [`UpdateFromFunc`](manim.animation.updaters.update.UpdateFromFunc.md#manim.animation.updaters.update.UpdateFromFunc), [`Rotating`](manim.animation.rotation.Rotating.md#manim.animation.rotation.Rotating), [`rotate()`](#manim.mobject.mobject.Mobject.rotate), [`animate`](#manim.mobject.mobject.Mobject.animate)

#### align_data(mobject, skip_point_alignment=False)

Aligns the family structure and data of this mobject with another mobject.

Afterwards, the two mobjects will have the same number of submobjects
(see `align_submobjects()`) and the same parent structure (see
[`null_point_align()`](#manim.mobject.mobject.Mobject.null_point_align)). If `skip_point_alignment` is `False`,
they will also have the same number of points (see [`align_points()`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject.align_points)).

* **Parameters:**
  * **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject)) – The other mobject this mobject should be aligned to.
  * **skip_point_alignment** (*bool*) – Controls whether or not the computationally expensive
    point alignment is skipped (default: `False`).
* **Return type:**
  None

#### NOTE
This method is primarily used internally by [`become()`](#manim.mobject.mobject.Mobject.become) and the
[`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform) animation to ensure that mobjects are structurally
compatible before transformation.

### Examples

```default
>>> from manim import Rectangle, Line, ORIGIN, RIGHT
>>> rect = Rectangle(width=4.0, height=2.0, grid_xstep=1.0, grid_ystep=0.5)
>>> line = Line(start=ORIGIN,end=RIGHT)
>>> line.align_data(rect)
>>> len(line.get_family()) == len(rect.get_family())
True
>>> line.get_num_points() == rect.get_num_points()
True
```

#### SEE ALSO
[`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform), [`become()`](#manim.mobject.mobject.Mobject.become), [`align_points()`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject.align_points), [`get_family()`](#manim.mobject.mobject.Mobject.get_family)

#### align_on_border(direction, buff=0.5)

Direction just needs to be a vector pointing towards side or
corner in the 2d plane.

* **Parameters:**
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **buff** (*float*)
* **Return type:**
  Self

#### align_to(mobject_or_point, direction=array([0., 0., 0.]))

Aligns mobject to another [`Mobject`](#manim.mobject.mobject.Mobject) in a certain direction.

Examples:
mob1.align_to(mob2, UP) moves mob1 vertically so that its
top edge lines ups with mob2’s top edge.

* **Parameters:**
  * **mobject_or_point** ([*Mobject*](#manim.mobject.mobject.Mobject) *|* [*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  Self

#### *property* animate *: \_AnimationBuilder | Self*

Used to animate the application of any method of `self`.

Any method called on `animate` is converted to an animation of applying
that method on the mobject itself.

For example, `square.set_fill(WHITE)` sets the fill color of a square,
while `square.animate.set_fill(WHITE)` animates this action.

Multiple methods can be put in a single animation once via chaining:

```default
self.play(my_mobject.animate.shift(RIGHT).rotate(PI))
```

#### WARNING
Passing multiple animations for the same [`Mobject`](#manim.mobject.mobject.Mobject) in one
call to [`play()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.play) is discouraged and will most likely
not work properly. Instead of writing an animation like

```default
self.play(
    my_mobject.animate.shift(RIGHT), my_mobject.animate.rotate(PI)
)
```

make use of method chaining.

Keyword arguments that can be passed to [`Scene.play()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.play) can be passed
directly after accessing `.animate`, like so:

```default
self.play(my_mobject.animate(rate_func=linear).shift(RIGHT))
```

This is especially useful when animating simultaneous `.animate` calls that
you want to behave differently:

```default
self.play(
    mobject1.animate(run_time=2).rotate(PI),
    mobject2.animate(rate_func=there_and_back).shift(RIGHT),
)
```

#### SEE ALSO
[`override_animate()`](manim.mobject.mobject.md#manim.mobject.mobject.override_animate)

### Examples

#### WARNING
`.animate`
: will interpolate the [`Mobject`](#manim.mobject.mobject.Mobject) between its points prior to
  `.animate` and its points after applying `.animate` to it. This may
  result in unexpected behavior when attempting to interpolate along paths,
  or rotations (see [`rotate()`](#manim.mobject.mobject.Mobject.rotate)).
  If you want animations to consider the points between, consider using
  [`ValueTracker`](manim.mobject.value_tracker.ValueTracker.md#manim.mobject.value_tracker.ValueTracker) with updaters instead (see [`add_updater()`](#manim.mobject.mobject.Mobject.add_updater)).

#### *classmethod* animation_override_for(animation_class)

Returns the function defining a specific animation override for this class.

* **Parameters:**
  **animation_class** (*type* *[*[*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – The animation class for which the override function should be returned.
* **Returns:**
  The function returning the override animation or `None` if no such animation
  override is defined.
* **Return type:**
  Optional[Callable[[[Mobject](#manim.mobject.mobject.Mobject), …], [Animation](manim.animation.animation.Animation.md#manim.animation.animation.Animation)]]

#### apply_complex_function(function, \*, about_point=None, about_edge=None)

Applies a complex function to a [`Mobject`](#manim.mobject.mobject.Mobject).
The x and y Point3Ds correspond to the real and imaginary parts respectively.

### Example

* **Parameters:**
  * **function** (*Callable* *[* *[**complex* *]* *,* *complex* *]*)
  * **about_point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*)
  * **about_edge** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike) *|* *None*)
* **Return type:**
  Self

#### apply_to_family(func)

Apply a function to `self` and every submobject with points recursively.

* **Parameters:**
  **func** (*Callable* *[* *[*[*Mobject*](#manim.mobject.mobject.Mobject) *]* *,* *None* *]*) – The function to apply to each mobject. `func` gets passed the respective
  (sub)mobject as parameter.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### SEE ALSO
[`family_members_with_points()`](#manim.mobject.mobject.Mobject.family_members_with_points)

#### arrange(direction=array([1., 0., 0.]), buff=0.25, center=True, \*\*kwargs)

Sorts [`Mobject`](#manim.mobject.mobject.Mobject) next to each other on screen.

### Examples

* **Parameters:**
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **buff** (*float*)
  * **center** (*bool*)
* **Return type:**
  Self

#### arrange_in_grid(rows=None, cols=None, buff=0.25, cell_alignment=array([0., 0., 0.]), row_alignments=None, col_alignments=None, row_heights=None, col_widths=None, flow_order='rd', \*\*kwargs)

Arrange submobjects in a grid.

* **Parameters:**
  * **rows** (*int* *|* *None*) – The number of rows in the grid.
  * **cols** (*int* *|* *None*) – The number of columns in the grid.
  * **buff** (*float* *|* *tuple* *[**float* *,* *float* *]*) – The gap between grid cells. To specify a different buffer in the horizontal and
    vertical directions, a tuple of two values can be given - `(row, col)`.
  * **cell_alignment** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The way each submobject is aligned in its grid cell.
  * **row_alignments** (*str* *|* *None*) – The vertical alignment for each row (top to bottom). Accepts the following characters: `"u"` -
    up, `"c"` - center, `"d"` - down.
  * **col_alignments** (*str* *|* *None*) – The horizontal alignment for each column (left to right). Accepts the following characters `"l"` - left,
    `"c"` - center, `"r"` - right.
  * **row_heights** (*Iterable* *[**float* *|* *None* *]*  *|* *None*) – Defines a list of heights for certain rows (top to bottom). If the list contains
    `None`, the corresponding row will fit its height automatically based
    on the highest element in that row.
  * **col_widths** (*Iterable* *[**float* *|* *None* *]*  *|* *None*) – Defines a list of widths for certain columns (left to right). If the list contains `None`, the
    corresponding column will fit its width automatically based on the widest element in that column.
  * **flow_order** (*str*) – The order in which submobjects fill the grid. Can be one of the following values:
    “rd”, “dr”, “ld”, “dl”, “ru”, “ur”, “lu”, “ul”. (“rd” -> fill rightwards then downwards)
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)
* **Raises:**
  * **ValueError** – If `rows` and `cols` are too small to fit all submobjects.
  * **ValueError** – If `cols`, `col_alignments` and `col_widths` or `rows`,
        `row_alignments` and `row_heights` have mismatching sizes.

### Notes

If only one of `cols` and `rows` is set implicitly, the other one will be chosen big
enough to fit all submobjects. If neither is set, they will be chosen to be about the same,
tending towards `cols` > `rows` (simply because videos are wider than they are high).

If both `cell_alignment` and `row_alignments` / `col_alignments` are
defined, the latter has higher priority.

### Examples

#### arrange_submobjects(\*args, \*\*kwargs)

Arrange the position of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects) with a small buffer.

### Examples

* **Return type:**
  Self

#### become(mobject, match_height=False, match_width=False, match_depth=False, match_center=False, stretch=False)

Edit points, colors and submobjects to be identical
to another [`Mobject`](#manim.mobject.mobject.Mobject)

#### NOTE
If both match_height and match_width are `True` then the transformed [`Mobject`](#manim.mobject.mobject.Mobject)
will match the height first and then the width.

* **Parameters:**
  * **match_height** (*bool*) – Whether or not to preserve the height of the original
    [`Mobject`](#manim.mobject.mobject.Mobject).
  * **match_width** (*bool*) – Whether or not to preserve the width of the original
    [`Mobject`](#manim.mobject.mobject.Mobject).
  * **match_depth** (*bool*) – Whether or not to preserve the depth of the original
    [`Mobject`](#manim.mobject.mobject.Mobject).
  * **match_center** (*bool*) – Whether or not to preserve the center of the original
    [`Mobject`](#manim.mobject.mobject.Mobject).
  * **stretch** (*bool*) – Whether or not to stretch the target mobject to match the
    the proportions of the original [`Mobject`](#manim.mobject.mobject.Mobject).
  * **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject))
* **Return type:**
  Self

### Examples

The following examples illustrate how mobject measurements
change when using the `match_...` and `stretch` arguments.
We start with a rectangle that is 2 units high and 4 units wide,
which we want to turn into a circle of radius 3:

```default
>>> from manim import Rectangle, Circle
>>> import numpy as np
>>> rect = Rectangle(height=2, width=4)
>>> circ = Circle(radius=3)
```

With `stretch=True`, the target circle is deformed to match
the proportions of the rectangle, which results in the target
mobject being an ellipse with height 2 and width 4. We can
check that the resulting points satisfy the ellipse equation
$x^2/a^2 + y^2/b^2 = 1$ with $a = 4/2$ and $b = 2/2$
being the semi-axes:

```default
>>> result = rect.copy().become(circ, stretch=True)
>>> result.height, result.width
(np.float64(2.0), np.float64(4.0))
>>> ellipse_points = np.array(result.get_anchors())
>>> ellipse_eq = np.sum(ellipse_points**2 * [1/4, 1, 0], axis=1)
>>> np.allclose(ellipse_eq, 1)
True
```

With `match_height=True` and `match_width=True` the circle is
scaled such that the height or the width of the rectangle will
be preserved, respectively.
The points of the resulting mobject satisfy the circle equation
$x^2 + y^2 = r^2$ for the corresponding radius $r$:

```default
>>> result = rect.copy().become(circ, match_height=True)
>>> result.height, result.width
(np.float64(2.0), np.float64(2.0))
>>> circle_points = np.array(result.get_anchors())
>>> circle_eq = np.sum(circle_points**2, axis=1)
>>> np.allclose(circle_eq, 1)
True
>>> result = rect.copy().become(circ, match_width=True)
>>> result.height, result.width
(np.float64(4.0), np.float64(4.0))
>>> circle_points = np.array(result.get_anchors())
>>> circle_eq = np.sum(circle_points**2, axis=1)
>>> np.allclose(circle_eq, 2**2)
True
```

With `match_center=True`, the resulting mobject is moved such that
its center is the same as the center of the original mobject:

```default
>>> rect = rect.shift(np.array([0, 1, 0]))
>>> np.allclose(rect.get_center(), circ.get_center())
False
>>> result = rect.copy().become(circ, match_center=True)
>>> np.allclose(rect.get_center(), result.get_center())
True
```

#### SEE ALSO
[`align_data()`](#manim.mobject.mobject.Mobject.align_data), `interpolate_color()`

#### center()

Moves the center of the mobject to the center of the scene.

* **Returns:**
  The centered mobject.
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### clear_updaters(recursive=True)

Remove every updater.

* **Parameters:**
  **recursive** (*bool*) – Whether to recursively call `clear_updaters` on all submobjects.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### SEE ALSO
[`remove_updater()`](#manim.mobject.mobject.Mobject.remove_updater), [`add_updater()`](#manim.mobject.mobject.Mobject.add_updater), [`get_updaters()`](#manim.mobject.mobject.Mobject.get_updaters)

#### copy()

Create and return an identical copy of the [`Mobject`](#manim.mobject.mobject.Mobject) including all
[`submobjects`](#manim.mobject.mobject.Mobject.submobjects).

* **Returns:**
  The copy.
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### NOTE
The clone is initially not visible in the Scene, even if the original was.

#### *property* depth *: float*

The depth of the mobject.

* **Return type:**
  `float`

#### SEE ALSO
[`length_over_dim()`](#manim.mobject.mobject.Mobject.length_over_dim)

#### family_members_with_points()

Filters the list of family members (generated by [`get_family()`](#manim.mobject.mobject.Mobject.get_family)) to include only mobjects with points.

* **Returns:**
  A list of mobjects that have points.
* **Return type:**
  list[[Mobject](#manim.mobject.mobject.Mobject)]

### Examples

```default
>>> from manim import Square, Rectangle, VGroup, Group, Mobject, VMobject
>>> s, r, m, v = Square(), Rectangle(), Mobject(), VMobject()
>>> vg = VGroup(s, r)
>>> gr = Group(vg, m, v)
>>> gr.family_members_with_points()
[Square, Rectangle]
```

#### SEE ALSO
[`get_family()`](#manim.mobject.mobject.Mobject.get_family)

#### flip(axis=array([0., 1., 0.]), \*, about_point=None, about_edge=None)

Flips/Mirrors an mobject about its center.

### Examples

* **Parameters:**
  * **axis** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **about_point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*)
  * **about_edge** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike) *|* *None*)
* **Return type:**
  Self

#### generate_points()

Initializes [`points`](#manim.mobject.mobject.Mobject.points) and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  object

#### get_all_points()

Return all points from this mobject and all submobjects.

May contain duplicates; the order is in a depth-first (pre-order)
traversal of the submobjects.

* **Return type:**
  [*Point3D_Array*](manim.typing.md#manim.typing.Point3D_Array)

#### get_bottom()

Get bottom Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject)

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_center()

Get center Point3Ds

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_color()

Returns the color of the [`Mobject`](#manim.mobject.mobject.Mobject)

### Examples

```default
>>> from manim import Square, RED
>>> Square(color=RED).get_color() == RED
True
```

* **Return type:**
  [*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)

#### get_coord(dim, direction=array([0., 0., 0.]))

Meant to generalize `get_x`, `get_y` and `get_z`

* **Parameters:**
  * **dim** (*int*)
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  float

#### get_corner(direction)

Get corner Point3Ds for certain direction.

* **Parameters:**
  **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_critical_point(direction)

Picture a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject).  Such a box has
9 ‘critical points’: 4 corners, 4 edge center, the
center. This returns one of them, along the given direction.

```default
sample = Arc(start_angle=PI / 7, angle=PI / 5)

# These are all equivalent
max_y_1 = sample.get_top()[1]
max_y_2 = sample.get_critical_point(UP)[1]
max_y_3 = sample.get_extremum_along_dim(dim=1, key=1)
```

* **Parameters:**
  **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_edge_center(direction)

Get edge Point3Ds for certain direction.

* **Parameters:**
  **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_end()

Returns the point, where the stroke that surrounds the [`Mobject`](#manim.mobject.mobject.Mobject) ends.

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_family(recurse=True)

Lists all mobjects in the hierarchy (family) of the given mobject,
including the mobject itself and all its submobjects recursively.

* **Parameters:**
  **recurse** (*bool*) – Just for consistency with get_family method in OpenGLMobject.
* **Returns:**
  A list of mobjects in the family of the given mobject.
* **Return type:**
  list[[Mobject](#manim.mobject.mobject.Mobject)]

### Examples

```default
>>> from manim import Square, Rectangle, VGroup, Group, Mobject, VMobject
>>> s, r, m, v = Square(), Rectangle(), Mobject(), VMobject()
>>> vg = VGroup(s, r)
>>> gr = Group(vg, m, v)
>>> gr.get_family()
[Group, VGroup(Square, Rectangle), Square, Rectangle, Mobject, VMobject]
```

#### SEE ALSO
[`family_members_with_points()`](#manim.mobject.mobject.Mobject.family_members_with_points), [`align_data()`](#manim.mobject.mobject.Mobject.align_data)

#### get_left()

Get left Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject)

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_merged_array(array_attr)

Return all of a given attribute from this mobject and all submobjects.

May contain duplicates; the order is in a depth-first (pre-order)
traversal of the submobjects.

* **Parameters:**
  **array_attr** (*str*)
* **Return type:**
  *ndarray*

#### get_midpoint()

Get Point3Ds of the middle of the path that forms the  [`Mobject`](#manim.mobject.mobject.Mobject).

### Examples

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### *static* get_mobject_type_class()

Return the base class of this mobject type.

* **Return type:**
  type[[*Mobject*](#manim.mobject.mobject.Mobject)]

#### get_nadir()

Get nadir (opposite the zenith) Point3Ds of a box bounding a 3D [`Mobject`](#manim.mobject.mobject.Mobject).

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_point_mobject(center=None)

The simplest [`Mobject`](#manim.mobject.mobject.Mobject) to be transformed to or from self.
Should by a point of the appropriate type

#### get_right()

Get right Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject)

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_start()

Returns the point, where the stroke that surrounds the [`Mobject`](#manim.mobject.mobject.Mobject) starts.

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_start_and_end()

Returns starting and ending point of a stroke as a `tuple`.

* **Return type:**
  tuple[[*Point3D*](manim.typing.md#manim.typing.Point3D), [*Point3D*](manim.typing.md#manim.typing.Point3D)]

#### get_time_based_updaters()

Return all updaters using the `dt` parameter.

The updaters use this parameter as the input for difference in time.

* **Returns:**
  The list of time based updaters.
* **Return type:**
  List[`Callable`]

#### SEE ALSO
[`get_updaters()`](#manim.mobject.mobject.Mobject.get_updaters), [`has_time_based_updater()`](#manim.mobject.mobject.Mobject.has_time_based_updater)

#### get_top()

Get top Point3Ds of a box bounding the [`Mobject`](#manim.mobject.mobject.Mobject)

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### get_updaters()

Return all updaters.

* **Returns:**
  The list of updaters.
* **Return type:**
  List[`Callable`]

#### SEE ALSO
[`add_updater()`](#manim.mobject.mobject.Mobject.add_updater), [`get_time_based_updaters()`](#manim.mobject.mobject.Mobject.get_time_based_updaters)

#### get_x(direction=array([0., 0., 0.]))

Returns x Point3D of the center of the [`Mobject`](#manim.mobject.mobject.Mobject) as `float`

* **Parameters:**
  **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  float

#### get_y(direction=array([0., 0., 0.]))

Returns y Point3D of the center of the [`Mobject`](#manim.mobject.mobject.Mobject) as `float`

* **Parameters:**
  **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  float

#### get_z(direction=array([0., 0., 0.]))

Returns z Point3D of the center of the [`Mobject`](#manim.mobject.mobject.Mobject) as `float`

* **Parameters:**
  **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  float

#### get_zenith()

Get zenith Point3Ds of a box bounding a 3D [`Mobject`](#manim.mobject.mobject.Mobject).

* **Return type:**
  [*Point3D*](manim.typing.md#manim.typing.Point3D)

#### has_no_points()

Check if [`Mobject`](#manim.mobject.mobject.Mobject) *does not* contains points.

* **Return type:**
  bool

#### has_points()

Check if [`Mobject`](#manim.mobject.mobject.Mobject) contains points.

* **Return type:**
  bool

#### has_time_based_updater()

Test if `self` has a time based updater.

* **Returns:**
  `True` if at least one updater uses the `dt` parameter, `False`
  otherwise.
* **Return type:**
  `bool`

#### SEE ALSO
[`get_time_based_updaters()`](#manim.mobject.mobject.Mobject.get_time_based_updaters)

#### *property* height *: float*

The height of the mobject.

* **Return type:**
  `float`

### Examples

#### SEE ALSO
[`length_over_dim()`](#manim.mobject.mobject.Mobject.length_over_dim)

#### init_colors()

Initializes the colors.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

* **Return type:**
  object

#### insert(index, mobject)

Inserts a mobject at a specific position into self.submobjects

Effectively just calls  `self.submobjects.insert(index, mobject)`,
where `self.submobjects` is a list.

Highly adapted from `Mobject.add`.

* **Parameters:**
  * **index** (*int*) – The index at which
  * **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject)) – The mobject to be inserted.
* **Return type:**
  None

#### interpolate(mobject1, mobject2, alpha, path_func=<function interpolate>)

Turns this [`Mobject`](#manim.mobject.mobject.Mobject) into an interpolation between `mobject1`
and `mobject2`.

The interpolation is applied to the points and color of the mobject.

* **Parameters:**
  * **mobject1** ([*Mobject*](#manim.mobject.mobject.Mobject)) – The starting Mobject.
  * **mobject2** ([*Mobject*](#manim.mobject.mobject.Mobject)) – The target Mobject.
  * **alpha** (*float*) – Interpolation factor between 0 (at `mobject1`) and 1 (at `mobject2`).
  * **path_func** ([*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)) – The function defining the interpolation path. Defaults to a straight path.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### NOTE
- Both mobjects must have the same number of points. If not, this will raise an error.
  Use [`align_points()`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject.align_points) to match point counts beforehand if needed.
- This method is used internally by the [`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform) animation
  to interpolate between two mobjects during a transformation.

### Examples

#### SEE ALSO
[`Transform`](manim.animation.transform.Transform.md#manim.animation.transform.Transform), [`align_points()`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject.align_points), `interpolate_color()`

#### invert(recursive=False)

Inverts the list of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects).

* **Parameters:**
  **recursive** (*bool*) – If `True`, all submobject lists of this mobject’s family are inverted.
* **Return type:**
  None

### Examples

#### length_over_dim(dim)

Measure the length of an [`Mobject`](#manim.mobject.mobject.Mobject) in a certain direction.

* **Parameters:**
  **dim** (*int*)
* **Return type:**
  float

#### match_color(mobject)

Match the color with the color of another [`Mobject`](#manim.mobject.mobject.Mobject).

* **Parameters:**
  **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject))
* **Return type:**
  Self

#### match_coord(mobject, dim, direction=array([0., 0., 0.]))

Match the Point3Ds with the Point3Ds of another [`Mobject`](#manim.mobject.mobject.Mobject).

* **Parameters:**
  * **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject))
  * **dim** (*int*)
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  Self

#### match_depth(mobject, \*\*kwargs)

Match the depth with the depth of another [`Mobject`](#manim.mobject.mobject.Mobject).

* **Parameters:**
  **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject))
* **Return type:**
  Self

#### match_dim_size(mobject, dim, \*\*kwargs)

Match the specified dimension with the dimension of another [`Mobject`](#manim.mobject.mobject.Mobject).

* **Parameters:**
  * **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject))
  * **dim** (*int*)
* **Return type:**
  Self

#### match_height(mobject, \*\*kwargs)

Match the height with the height of another [`Mobject`](#manim.mobject.mobject.Mobject).

* **Parameters:**
  **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject))
* **Return type:**
  Self

#### match_points(mobject, copy_submobjects=True)

Edit points, positions, and submobjects to be identical
to another [`Mobject`](#manim.mobject.mobject.Mobject), while keeping the style unchanged.

### Examples

* **Parameters:**
  * **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject))
  * **copy_submobjects** (*bool*)
* **Return type:**
  Self

#### match_updaters(mobject)

Match the updaters of the given mobject.

* **Parameters:**
  **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject)) – The mobject whose updaters get matched.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### NOTE
All updaters from submobjects are removed, but only updaters of the given
mobject are matched, not those of it’s submobjects.

#### SEE ALSO
[`add_updater()`](#manim.mobject.mobject.Mobject.add_updater), [`clear_updaters()`](#manim.mobject.mobject.Mobject.clear_updaters)

#### match_width(mobject, \*\*kwargs)

Match the width with the width of another [`Mobject`](#manim.mobject.mobject.Mobject).

* **Parameters:**
  **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject))
* **Return type:**
  Self

#### match_x(mobject, direction=array([0., 0., 0.]))

Match x coord. to the x coord. of another [`Mobject`](#manim.mobject.mobject.Mobject).

* **Parameters:**
  **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject))
* **Return type:**
  Self

#### match_y(mobject, direction=array([0., 0., 0.]))

Match y coord. to the x coord. of another [`Mobject`](#manim.mobject.mobject.Mobject).

* **Parameters:**
  **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject))
* **Return type:**
  Self

#### match_z(mobject, direction=array([0., 0., 0.]))

Match z coord. to the x coord. of another [`Mobject`](#manim.mobject.mobject.Mobject).

* **Parameters:**
  **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject))
* **Return type:**
  Self

#### move_to(point_or_mobject, aligned_edge=array([0., 0., 0.]), coor_mask=array([1, 1, 1]))

Move center of the [`Mobject`](#manim.mobject.mobject.Mobject) to certain Point3D.

* **Parameters:**
  * **point_or_mobject** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* [*Mobject*](#manim.mobject.mobject.Mobject))
  * **aligned_edge** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **coor_mask** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  Self

#### next_to(mobject_or_point, direction=array([1., 0., 0.]), buff=0.25, aligned_edge=array([0., 0., 0.]), submobject_to_align=None, index_of_submobject_to_align=None, coor_mask=array([1, 1, 1]))

Move this [`Mobject`](#manim.mobject.mobject.Mobject) next to another’s [`Mobject`](#manim.mobject.mobject.Mobject) or Point3D.

### Examples

* **Parameters:**
  * **mobject_or_point** ([*Mobject*](#manim.mobject.mobject.Mobject) *|* [*Point3DLike*](manim.typing.md#manim.typing.Point3DLike))
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **buff** (*float*)
  * **aligned_edge** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **submobject_to_align** ([*Mobject*](#manim.mobject.mobject.Mobject) *|* *None*)
  * **index_of_submobject_to_align** (*int* *|* *None*)
  * **coor_mask** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  Self

#### null_point_align(mobject)

If a [`Mobject`](#manim.mobject.mobject.Mobject) with points is being aligned to
one without, treat both as groups, and push
the one with points into its own submobjects
list.

* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)
* **Parameters:**
  **mobject** ([*Mobject*](#manim.mobject.mobject.Mobject))

#### reduce_across_dimension(reduce_func, dim)

Find the min or max value from a dimension across all points in this and submobjects.

* **Parameters:**
  * **reduce_func** (*Callable*)
  * **dim** (*int*)

#### remove(\*mobjects)

Remove [`submobjects`](#manim.mobject.mobject.Mobject.submobjects).

The mobjects are removed from [`submobjects`](#manim.mobject.mobject.Mobject.submobjects), if they exist.

Subclasses of mobject may implement `-` and `-=` dunder methods.

* **Parameters:**
  **mobjects** ([*Mobject*](#manim.mobject.mobject.Mobject)) – The mobjects to remove.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### SEE ALSO
[`add()`](#manim.mobject.mobject.Mobject.add)

#### remove_updater(update_function)

Remove an updater.

If the same updater is applied multiple times, every instance gets removed.

* **Parameters:**
  **update_function** ([*Updater*](manim.mobject.mobject.md#manim.mobject.mobject.Updater)) – The update function to be removed.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### SEE ALSO
[`clear_updaters()`](#manim.mobject.mobject.Mobject.clear_updaters), [`add_updater()`](#manim.mobject.mobject.Mobject.add_updater), [`get_updaters()`](#manim.mobject.mobject.Mobject.get_updaters)

#### repeat(count)

This can make transition animations nicer

* **Parameters:**
  **count** (*int*)
* **Return type:**
  Self

#### reset_points()

Sets [`points`](#manim.mobject.mobject.Mobject.points) to be an empty array.

* **Return type:**
  None

#### restore()

Restores the state that was previously saved with [`save_state()`](#manim.mobject.mobject.Mobject.save_state).

* **Return type:**
  Self

#### resume_updating(recursive=True)

Enable updating from updaters and animations.

* **Parameters:**
  **recursive** (*bool*) – Whether to recursively enable updating on all submobjects.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### SEE ALSO
[`suspend_updating()`](#manim.mobject.mobject.Mobject.suspend_updating), [`add_updater()`](#manim.mobject.mobject.Mobject.add_updater)

#### rotate(angle, axis=array([0., 0., 1.]), \*, about_point=None, about_edge=None)

Rotates the [`Mobject`](#manim.mobject.mobject.Mobject) around a specified axis and point.

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
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### NOTE
To animate a rotation, use [`Rotating`](manim.animation.rotation.Rotating.md#manim.animation.rotation.Rotating) or [`Rotate`](manim.animation.rotation.Rotate.md#manim.animation.rotation.Rotate)
instead of `.animate.rotate(...)`.
The `.animate.rotate(...)` syntax only applies a transformation
from the initial state to the final rotated state
(interpolation between the two states), without showing proper rotational motion
based on the angle (from 0 to the given angle).

### Examples

#### SEE ALSO
[`Rotating`](manim.animation.rotation.Rotating.md#manim.animation.rotation.Rotating), [`Rotate`](manim.animation.rotation.Rotate.md#manim.animation.rotation.Rotate), [`animate`](#manim.mobject.mobject.Mobject.animate), `apply_points_function_about_point()`

#### rotate_about_origin(angle, axis=array([0., 0., 1.]))

Rotates the [`Mobject`](#manim.mobject.mobject.Mobject) about the ORIGIN, which is at [0,0,0].

* **Parameters:**
  * **angle** (*float*)
  * **axis** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  Self

#### save_image(name=None)

Saves an image of only this [`Mobject`](#manim.mobject.mobject.Mobject) at its position to a png
file.

* **Parameters:**
  **name** (*str* *|* *None*)
* **Return type:**
  None

#### save_state()

Save the current state (position, color & size). Can be restored with [`restore()`](#manim.mobject.mobject.Mobject.restore).

* **Return type:**
  Self

#### scale(scale_factor, \*, about_point=None, about_edge=None)

Scale the size by a factor.

Default behavior is to scale about the center of the mobject.

* **Parameters:**
  * **scale_factor** (*float*) – The scaling factor $\alpha$. If $0 < |\alpha| < 1$, the mobject
    will shrink, and for $|\alpha| > 1$ it will grow. Furthermore,
    if $\alpha < 0$, the mobject is also flipped.
  * **about_point** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*) – The point about which to apply the scaling.
  * **about_edge** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike) *|* *None*) – The edge about which to apply the scaling.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

### Examples

#### SEE ALSO
[`move_to()`](#manim.mobject.mobject.Mobject.move_to)

#### scale_to_fit_depth(depth, \*\*kwargs)

Scales the [`Mobject`](#manim.mobject.mobject.Mobject) to fit a depth while keeping width/height proportional.

* **Parameters:**
  **depth** (*float*)
* **Return type:**
  Self

#### scale_to_fit_height(height, \*\*kwargs)

Scales the [`Mobject`](#manim.mobject.mobject.Mobject) to fit a height while keeping width/depth proportional.

* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)
* **Parameters:**
  **height** (*float*)

### Examples

```default
>>> from manim import *
>>> sq = Square()
>>> sq.width
np.float64(2.0)
>>> sq.scale_to_fit_height(5)
Square
>>> sq.height
np.float64(5.0)
>>> sq.width
np.float64(5.0)
```

#### scale_to_fit_width(width, \*\*kwargs)

Scales the [`Mobject`](#manim.mobject.mobject.Mobject) to fit a width while keeping height/depth proportional.

* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)
* **Parameters:**
  **width** (*float*)

### Examples

```default
>>> from manim import *
>>> sq = Square()
>>> sq.height
np.float64(2.0)
>>> sq.scale_to_fit_width(5)
Square
>>> sq.width
np.float64(5.0)
>>> sq.height
np.float64(5.0)
```

#### set(\*\*kwargs)

Sets attributes.

I.e. `my_mobject.set(foo=1)` applies `my_mobject.foo = 1`.

This is a convenience to be used along with [`animate`](#manim.mobject.mobject.Mobject.animate) to
animate setting attributes.

In addition to this method, there is a compatibility
layer that allows `get_*` and `set_*` methods to
get and set generic attributes. For instance:

```default
>>> mob = Mobject()
>>> mob.set_foo(0)
Mobject
>>> mob.get_foo()
0
>>> mob.foo
0
```

This compatibility layer does not interfere with any
`get_*` or `set_*` methods that are explicitly
defined.

#### WARNING
This compatibility layer is for backwards compatibility
and is not guaranteed to stay around. Where applicable,
please prefer getting/setting attributes normally or with
the [`set()`](#manim.mobject.mobject.Mobject.set) method.

* **Parameters:**
  **\*\*kwargs** – The attributes and corresponding values to set.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

### Examples

```default
>>> mob = Mobject()
>>> mob.set(foo=0)
Mobject
>>> mob.foo
0
```

#### set_color(color=ManimColor('#FFFF00'), family=True)

Condition is function which takes in one arguments, (x, y, z).
Here it just recurses to submobjects, but in subclasses this
should be further implemented based on the the inner workings
of color

* **Parameters:**
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))
  * **family** (*bool*)
* **Return type:**
  Self

#### set_color_by_gradient(\*colors)

* **Parameters:**
  * **colors** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor)) – The colors to use for the gradient. Use like set_color_by_gradient(RED, BLUE, GREEN).
  * **ManimColor.parse****(****color****)** (*self.color =*)
  * **self** (*return*)
* **Return type:**
  Self

#### *classmethod* set_default(\*\*kwargs)

Sets the default values of keyword arguments.

If this method is called without any additional keyword
arguments, the original default values of the initialization
method of this class are restored.

* **Parameters:**
  **kwargs** – Passing any keyword argument will update the default
  values of the keyword arguments of the initialization
  function of this class.
* **Return type:**
  None

### Examples

```default
>>> from manim import Square, GREEN
>>> Square.set_default(color=GREEN, fill_opacity=0.25)
>>> s = Square(); s.color, s.fill_opacity
(ManimColor('#83C167'), 0.25)
>>> Square.set_default()
>>> s = Square(); s.color, s.fill_opacity
(ManimColor('#FFFFFF'), 0.0)
```

#### set_x(x, direction=array([0., 0., 0.]))

Set x value of the center of the [`Mobject`](#manim.mobject.mobject.Mobject) (`int` or `float`)

* **Parameters:**
  * **x** (*float*)
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  Self

#### set_y(y, direction=array([0., 0., 0.]))

Set y value of the center of the [`Mobject`](#manim.mobject.mobject.Mobject) (`int` or `float`)

* **Parameters:**
  * **y** (*float*)
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  Self

#### set_z(z, direction=array([0., 0., 0.]))

Set z value of the center of the [`Mobject`](#manim.mobject.mobject.Mobject) (`int` or `float`)

* **Parameters:**
  * **z** (*float*)
  * **direction** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  Self

#### set_z_index(z_index_value, family=True)

Sets the [`Mobject`](#manim.mobject.mobject.Mobject)’s `z_index` to the value specified in z_index_value.

* **Parameters:**
  * **z_index_value** (*float*) – The new value of `z_index` set.
  * **family** (*bool*) – If `True`, the `z_index` value of all submobjects is also set.
* **Returns:**
  The Mobject itself, after `z_index` is set. For chaining purposes. (Returns self.)
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

### Examples

#### set_z_index_by_z_Point3D()

Sets the [`Mobject`](#manim.mobject.mobject.Mobject)’s z Point3D to the value of `z_index`.

* **Returns:**
  The Mobject itself, after `z_index` is set. (Returns self.)
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### shift(\*vectors)

Shift by the given vectors.

* **Parameters:**
  **vectors** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – Vectors to shift by. If multiple vectors are given, they are added
  together.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### SEE ALSO
[`move_to()`](#manim.mobject.mobject.Mobject.move_to)

#### shuffle(recursive=False)

Shuffles the list of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects).

* **Parameters:**
  **recursive** (*bool*)
* **Return type:**
  None

#### shuffle_submobjects(\*args, \*\*kwargs)

Shuffles the order of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects)

### Examples

* **Return type:**
  None

#### sort(point_to_num_func=<function Mobject.<lambda>>, submob_func=None)

Sorts the list of [`submobjects`](#manim.mobject.mobject.Mobject.submobjects) by a function defined by `submob_func`.

* **Parameters:**
  * **point_to_num_func** (*Callable* *[* *[*[*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *]* *,* *float* *]*)
  * **submob_func** (*Callable* *[* *[*[*Mobject*](#manim.mobject.mobject.Mobject) *]* *,* *Any* *]*  *|* *None*)
* **Return type:**
  Self

#### sort_submobjects(\*args, \*\*kwargs)

Sort the [`submobjects`](#manim.mobject.mobject.Mobject.submobjects)

* **Return type:**
  Self

#### stretch_to_fit_depth(depth, \*\*kwargs)

Stretches the [`Mobject`](#manim.mobject.mobject.Mobject) to fit a depth, not keeping width/height proportional.

* **Parameters:**
  **depth** (*float*)
* **Return type:**
  Self

#### stretch_to_fit_height(height, \*\*kwargs)

Stretches the [`Mobject`](#manim.mobject.mobject.Mobject) to fit a height, not keeping width/depth proportional.

* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)
* **Parameters:**
  **height** (*float*)

### Examples

```default
>>> from manim import *
>>> sq = Square()
>>> sq.width
np.float64(2.0)
>>> sq.stretch_to_fit_height(5)
Square
>>> sq.height
np.float64(5.0)
>>> sq.width
np.float64(2.0)
```

#### stretch_to_fit_width(width, \*\*kwargs)

Stretches the [`Mobject`](#manim.mobject.mobject.Mobject) to fit a width, not keeping height/depth proportional.

* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)
* **Parameters:**
  **width** (*float*)

### Examples

```default
>>> from manim import *
>>> sq = Square()
>>> sq.height
np.float64(2.0)
>>> sq.stretch_to_fit_width(5)
Square
>>> sq.width
np.float64(5.0)
>>> sq.height
np.float64(2.0)
```

#### suspend_updating(recursive=True)

Disable updating from updaters and animations.

* **Parameters:**
  **recursive** (*bool*) – Whether to recursively suspend updating on all submobjects.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### SEE ALSO
[`resume_updating()`](#manim.mobject.mobject.Mobject.resume_updating), [`add_updater()`](#manim.mobject.mobject.Mobject.add_updater)

#### to_corner(corner=array([-1., -1., 0.]), buff=0.5)

Moves this [`Mobject`](#manim.mobject.mobject.Mobject) to the given corner of the screen.

* **Returns:**
  The newly positioned mobject.
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)
* **Parameters:**
  * **corner** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **buff** (*float*)

### Examples

#### to_edge(edge=array([-1., 0., 0.]), buff=0.5)

Moves this [`Mobject`](#manim.mobject.mobject.Mobject) to the given edge of the screen,
without affecting its position in the other dimension.

* **Returns:**
  The newly positioned mobject.
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)
* **Parameters:**
  * **edge** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **buff** (*float*)

### Examples

#### update(dt=0, recursive=True)

Apply all updaters.

Does nothing if updating is suspended.

* **Parameters:**
  * **dt** (*float*) – The parameter `dt` to pass to the update functions. Usually this is the
    time in seconds since the last call of `update`.
  * **recursive** (*bool*) – Whether to recursively update all submobjects.
* **Returns:**
  `self`
* **Return type:**
  [`Mobject`](#manim.mobject.mobject.Mobject)

#### SEE ALSO
[`add_updater()`](#manim.mobject.mobject.Mobject.add_updater), [`get_updaters()`](#manim.mobject.mobject.Mobject.get_updaters)

#### *property* width *: float*

The width of the mobject.

* **Return type:**
  `float`

### Examples

#### SEE ALSO
[`length_over_dim()`](#manim.mobject.mobject.Mobject.length_over_dim)
