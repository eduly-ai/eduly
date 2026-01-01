# CurvesAsSubmobjects

Qualified name: `manim.mobject.types.vectorized\_mobject.CurvesAsSubmobjects`

### *class* CurvesAsSubmobjects(vmobject, \*\*kwargs)

Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)

Convert a curve’s elements to submobjects.

### Examples

### Methods

| [`point_from_proportion`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.point_from_proportion)   | Gets the point at a proportion along the path of the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects).   |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|

### Attributes

| `animate`             | Used to animate the application of any method of `self`.               |
|-----------------------|------------------------------------------------------------------------|
| `animation_overrides` |                                                                        |
| `color`               |                                                                        |
| `depth`               | The depth of the mobject.                                              |
| `fill_color`          | If there are multiple colors (for gradient) this returns the first one |
| `height`              | The height of the mobject.                                             |
| `n_points_per_curve`  |                                                                        |
| `sheen_factor`        |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |
* **Parameters:**
  **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))

#### \_original_\_init_\_(vmobject, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject))
* **Return type:**
  None

#### point_from_proportion(alpha)

Gets the point at a proportion along the path of the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects).

* **Parameters:**
  **alpha** (*float*) – The proportion along the the path of the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects).
* **Returns:**
  The point on the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects).
* **Return type:**
  `numpy.ndarray`
* **Raises:**
  * **ValueError** – If `alpha` is not between 0 and 1.
  * **Exception** – If the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects) has no submobjects, or no submobject has points.
