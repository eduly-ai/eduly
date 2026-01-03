# paths

Functions determining transformation paths between sets of points.

### Functions

### clockwise_path()

This function transforms each point by moving clockwise around a half circle.

### Examples

* **Return type:**
  [*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)

### counterclockwise_path()

This function transforms each point by moving counterclockwise around a half circle.

### Examples

* **Return type:**
  [*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)

### path_along_arc(arc_angle, axis=array([0., 0., 1.]))

This function transforms each point by moving it along a circular arc.

* **Parameters:**
  * **arc_angle** (*float*) – The angle each point traverses around a circular arc.
  * **axis** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The axis of rotation.
* **Return type:**
  [*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)

### Examples

### path_along_circles(arc_angle, circles_centers, axis=array([0., 0., 1.]))

This function transforms each point by moving it roughly along a circle, each with its own specified center.

The path may be seen as each point smoothly changing its orbit from its starting position to its destination.

* **Parameters:**
  * **arc_angle** (*float*) – The angle each point traverses around the quasicircle.
  * **circles_centers** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array)) – The centers of each point’s quasicircle to rotate around.
  * **axis** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The axis of rotation.
* **Return type:**
  [*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)

### Examples

### spiral_path(angle, axis=array([0., 0., 1.]))

This function transforms each point by moving along a spiral to its destination.

* **Parameters:**
  * **angle** (*float*) – The angle each point traverses around a spiral.
  * **axis** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The axis of rotation.
* **Return type:**
  [*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)

### Examples

### straight_path()

Simplest path function. Each point in a set goes in a straight path toward its destination.

### Examples

* **Return type:**
  [*PathFuncType*](manim.typing.md#manim.typing.PathFuncType)
