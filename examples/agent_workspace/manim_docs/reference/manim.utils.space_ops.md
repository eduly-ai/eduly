# space_ops

Utility functions for two- and three-dimensional vectors.

### Functions

### R3_to_complex(point)

* **Parameters:**
  **point** (*Sequence* *[**float* *]*)
* **Return type:**
  *ndarray*

### angle_axis_from_quaternion(quaternion)

Gets angle and axis from a quaternion.

* **Parameters:**
  **quaternion** (*Sequence* *[**float* *]*) – The quaternion from which we get the angle and axis.
* **Returns:**
  Gives the angle and axis
* **Return type:**
  Sequence[float]

### angle_between_vectors(v1, v2)

Returns the angle between two vectors.
This angle will always be between 0 and pi

* **Parameters:**
  * **v1** (*ndarray*) – The first vector.
  * **v2** (*ndarray*) – The second vector.
* **Returns:**
  The angle between the vectors.
* **Return type:**
  float

### angle_of_vector(vector)

Returns polar coordinate theta when vector is projected on xy plane.

* **Parameters:**
  **vector** (*Sequence* *[**float* *]*  *|* *ndarray*) – The vector to find the angle for.
* **Returns:**
  The angle of the vector projected.
* **Return type:**
  float

### cartesian_to_spherical(vec)

Returns an array of numbers corresponding to each
polar coordinate value (distance, phi, theta).

* **Parameters:**
  **vec** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – A numpy array or a sequence of floats `[x, y, z]`.
* **Return type:**
  *ndarray*

### center_of_mass(points)

Gets the center of mass of the points in space.

* **Parameters:**
  **points** ([*PointNDLike_Array*](manim.typing.md#manim.typing.PointNDLike_Array)) – The points to find the center of mass from.
* **Returns:**
  The center of mass of the points.
* **Return type:**
  np.ndarray

### compass_directions(n=4, start_vect=array([1., 0., 0.]))

Finds the cardinal directions using tau.

* **Parameters:**
  * **n** (*int*) – The amount to be rotated, by default 4
  * **start_vect** (*ndarray*) – The direction for the angle to start with, by default RIGHT
* **Returns:**
  The angle which has been rotated.
* **Return type:**
  np.ndarray

### complex_func_to_R3_func(complex_func)

* **Parameters:**
  **complex_func** (*Callable* *[* *[**complex* *]* *,* *complex* *]*)
* **Return type:**
  *Callable*[[[*Point3DLike*](manim.typing.md#manim.typing.Point3DLike)], [*Point3D*](manim.typing.md#manim.typing.Point3D)]

### complex_to_R3(complex_num)

* **Parameters:**
  **complex_num** (*complex*)
* **Return type:**
  *ndarray*

### cross(v1, v2)

* **Parameters:**
  * **v1** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **v2** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  [*Vector3D*](manim.typing.md#manim.typing.Vector3D)

### cross2d(a, b)

Compute the determinant(s) of the passed
vector (sequences).

* **Parameters:**
  * **a** ([*Vector2D*](manim.typing.md#manim.typing.Vector2D) *|* [*Vector2D_Array*](manim.typing.md#manim.typing.Vector2D_Array)) – A vector or a sequence of vectors.
  * **b** ([*Vector2D*](manim.typing.md#manim.typing.Vector2D) *|* [*Vector2D_Array*](manim.typing.md#manim.typing.Vector2D_Array)) – A vector or a sequence of vectors.
* **Returns:**
  The determinant or sequence of determinants
  of the first two components of the specified
  vectors.
* **Return type:**
  Sequence[float] | float

### Examples

```pycon
>>> cross2d(np.array([1, 2]), np.array([3, 4]))
np.int64(-2)
>>> cross2d(
...     np.array([[1, 2, 0], [1, 0, 0]]),
...     np.array([[3, 4, 0], [0, 1, 0]]),
... )
array([-2,  1])
```

### earclip_triangulation(verts, ring_ends)

Returns a list of indices giving a triangulation
of a polygon, potentially with holes.

* **Parameters:**
  * **verts** (*ndarray*) – verts is a numpy array of points.
  * **ring_ends** (*list*) – ring_ends is a list of indices indicating where
    the ends of new paths are.
* **Returns:**
  A list of indices giving a triangulation of a polygon.
* **Return type:**
  list

### find_intersection(p0s, v0s, p1s, v1s, threshold=1e-05)

Return the intersection of a line passing through p0 in direction v0
with one passing through p1 in direction v1 (or array of intersections
from arrays of such points/directions).
For 3d values, it returns the point on the ray p0 + v0 \* t closest to the
ray p1 + v1 \* t

* **Parameters:**
  * **p0s** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array))
  * **v0s** ([*Vector3DLike_Array*](manim.typing.md#manim.typing.Vector3DLike_Array))
  * **p1s** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array))
  * **v1s** ([*Vector3DLike_Array*](manim.typing.md#manim.typing.Vector3DLike_Array))
  * **threshold** (*float*)
* **Return type:**
  list[[*Point3D*](manim.typing.md#manim.typing.Point3D)]

### get_unit_normal(v1, v2, tol=1e-06)

Gets the unit normal of the vectors.

* **Parameters:**
  * **v1** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The first vector.
  * **v2** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The second vector
  * **tol** (*float*) – [description], by default 1e-6
* **Returns:**
  The normal of the two vectors.
* **Return type:**
  np.ndarray

### get_winding_number(points)

Determine the number of times a polygon winds around the origin.

The orientation is measured mathematically positively, i.e.,
counterclockwise.

* **Parameters:**
  **points** (*Sequence* *[**ndarray* *]*) – The vertices of the polygon being queried.
* **Return type:**
  float

### Examples

```pycon
>>> from manim import Square, get_winding_number
>>> polygon = Square()
>>> get_winding_number(polygon.get_vertices())
np.float64(1.0)
>>> polygon.shift(2 * UP)
Square
>>> get_winding_number(polygon.get_vertices())
np.float64(0.0)
```

### line_intersection(line1, line2)

Returns the intersection point of two lines, each defined by
a pair of distinct points lying on the line.

* **Parameters:**
  * **line1** (*Sequence* *[**ndarray* *]*) – A list of two points that determine the first line.
  * **line2** (*Sequence* *[**ndarray* *]*) – A list of two points that determine the second line.
* **Returns:**
  The intersection points of the two lines which are intersecting.
* **Return type:**
  np.ndarray
* **Raises:**
  **ValueError** – Error is produced if the two lines don’t intersect with each other
      or if the coordinates don’t lie on the xy-plane.

### midpoint(point1, point2)

Gets the midpoint of two points.

* **Parameters:**
  * **point1** (*Sequence* *[**float* *]*) – The first point.
  * **point2** (*Sequence* *[**float* *]*) – The second point.
* **Returns:**
  The midpoint of the points
* **Return type:**
  [Union](manim.mobject.geometry.boolean_ops.Union.md#manim.mobject.geometry.boolean_ops.Union)[float, np.ndarray]

### norm_squared(v)

* **Parameters:**
  **v** (*float*)
* **Return type:**
  float

### normalize(vect, fall_back=None)

* **Parameters:**
  * **vect** (*ndarray* *|* *tuple* *[**float* *]*)
  * **fall_back** (*ndarray* *|* *None*)
* **Return type:**
  *ndarray*

### normalize_along_axis(array, axis)

Normalizes an array with the provided axis.

* **Parameters:**
  * **array** (*ndarray*) – The array which has to be normalized.
  * **axis** (*ndarray*) – The axis to be normalized to.
* **Returns:**
  Array which has been normalized according to the axis.
* **Return type:**
  np.ndarray

### perpendicular_bisector(line, norm_vector=array([0., 0., 1.]))

Returns a list of two points that correspond
to the ends of the perpendicular bisector of the
two points given.

* **Parameters:**
  * **line** (*Sequence* *[**ndarray* *]*) – a list of two numpy array points (corresponding
    to the ends of a line).
  * **norm_vector** ([*Vector3D*](manim.typing.md#manim.typing.Vector3D)) – the vector perpendicular to both the line given
    and the perpendicular bisector.
* **Returns:**
  A list of two numpy array points that correspond
  to the ends of the perpendicular bisector
* **Return type:**
  list

### quaternion_conjugate(quaternion)

Used for finding the conjugate of the quaternion

* **Parameters:**
  **quaternion** (*Sequence* *[**float* *]*) – The quaternion for which you want to find the conjugate for.
* **Returns:**
  The conjugate of the quaternion.
* **Return type:**
  np.ndarray

### quaternion_from_angle_axis(angle, axis, axis_normalized=False)

Gets a quaternion from an angle and an axis.
For more information, check [this Wikipedia page](https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles).

* **Parameters:**
  * **angle** (*float*) – The angle for the quaternion.
  * **axis** (*ndarray*) – The axis for the quaternion
  * **axis_normalized** (*bool*) – Checks whether the axis is normalized, by default False
* **Returns:**
  Gives back a quaternion from the angle and axis
* **Return type:**
  list[float]

### quaternion_mult(\*quats)

Gets the Hamilton product of the quaternions provided.
For more information, check [this Wikipedia page](https://en.wikipedia.org/wiki/Quaternion).

* **Returns:**
  Returns a list of product of two quaternions.
* **Return type:**
  [Union](manim.mobject.geometry.boolean_ops.Union.md#manim.mobject.geometry.boolean_ops.Union)[np.ndarray, List[[Union](manim.mobject.geometry.boolean_ops.Union.md#manim.mobject.geometry.boolean_ops.Union)[float, np.ndarray]]]
* **Parameters:**
  **quats** (*Sequence* *[**float* *]*)

### regular_vertices(n, \*, radius=1, start_angle=None)

Generates regularly spaced vertices around a circle centered at the origin.

* **Parameters:**
  * **n** (*int*) – The number of vertices
  * **radius** (*float*) – The radius of the circle that the vertices are placed on.
  * **start_angle** (*float* *|* *None*) – 

    The angle the vertices start at.

    If unspecified, for even `n` values, `0` will be used.
    For odd `n` values, 90 degrees is used.
* **Returns:**
  * **vertices** (`numpy.ndarray`) – The regularly spaced vertices.
  * **start_angle** (`float`) – The angle the vertices start at.
* **Return type:**
  tuple[*ndarray*, float]

### rotate_vector(vector, angle, axis=array([0., 0., 1.]))

Function for rotating a vector.

* **Parameters:**
  * **vector** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The vector to be rotated.
  * **angle** (*float*) – The angle to be rotated by.
  * **axis** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike)) – The axis to be rotated, by default OUT
* **Returns:**
  The rotated vector with provided angle and axis.
* **Return type:**
  np.ndarray
* **Raises:**
  **ValueError** – If vector is not of dimension 2 or 3.

### rotation_about_z(angle)

Returns a rotation matrix for a given angle.

* **Parameters:**
  **angle** (*float*) – Angle for the rotation matrix.
* **Returns:**
  Gives back the rotated matrix.
* **Return type:**
  np.ndarray

### rotation_matrix(angle, axis, homogeneous=False)

Rotation in R^3 about a specified axis of rotation.

* **Parameters:**
  * **angle** (*float*)
  * **axis** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
  * **homogeneous** (*bool*)
* **Return type:**
  *ndarray*

### rotation_matrix_from_quaternion(quat)

* **Parameters:**
  **quat** (*ndarray*)
* **Return type:**
  *ndarray*

### rotation_matrix_transpose(angle, axis)

* **Parameters:**
  * **angle** (*float*)
  * **axis** ([*Vector3DLike*](manim.typing.md#manim.typing.Vector3DLike))
* **Return type:**
  *ndarray*

### rotation_matrix_transpose_from_quaternion(quat)

Converts the quaternion, quat, to an equivalent rotation matrix representation.
For more information, check [this page](https://in.mathworks.com/help/driving/ref/quaternion.rotmat.html).

* **Parameters:**
  **quat** (*ndarray*) – The quaternion which is to be converted.
* **Returns:**
  Gives back the Rotation matrix representation, returned as a 3-by-3
  matrix or 3-by-3-by-N multidimensional array.
* **Return type:**
  List[np.ndarray]

### shoelace(x_y)

2D implementation of the shoelace formula.

* **Returns:**
  Returns signed area.
* **Return type:**
  `float`
* **Parameters:**
  **x_y** ([*Point2D_Array*](manim.typing.md#manim.typing.Point2D_Array))

### shoelace_direction(x_y)

Uses the area determined by the shoelace method to determine whether
the input set of points is directed clockwise or counterclockwise.

* **Returns:**
  Either `"CW"` or `"CCW"`.
* **Return type:**
  `str`
* **Parameters:**
  **x_y** ([*Point2D_Array*](manim.typing.md#manim.typing.Point2D_Array))

### spherical_to_cartesian(spherical)

Returns a numpy array `[x, y, z]` based on the spherical
coordinates given.

* **Parameters:**
  **spherical** (*Sequence* *[**float* *]*) – 

  A list of three floats that correspond to the following:

  r - The distance between the point and the origin.

  theta - The azimuthal angle of the point to the positive x-axis.

  phi - The vertical angle of the point to the positive z-axis.
* **Return type:**
  *ndarray*

### thick_diagonal(dim, thickness=2)

* **Parameters:**
  * **dim** (*int*)
  * **thickness** (*int*)
* **Return type:**
  [*MatrixMN*](manim.typing.md#manim.typing.MatrixMN)

### z_to_vector(vector)

Returns some matrix in SO(3) which takes the z-axis to the
(normalized) vector provided as an argument

* **Parameters:**
  **vector** (*ndarray*)
* **Return type:**
  *ndarray*
