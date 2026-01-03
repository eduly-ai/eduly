# VGroup

Qualified name: `manim.mobject.types.vectorized\_mobject.VGroup`

### *class* VGroup(\*vmobjects, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A group of vectorized mobjects.

This can be used to group multiple [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) instances together
in order to scale, move, … them together.

### Notes

When adding the same mobject more than once, repetitions are ignored.
Use [`Mobject.copy()`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.copy) to create a separate copy which can then
be added to the group.

### Examples

To add `VGroup`, you can either use the
[`add()`](#manim.mobject.types.vectorized_mobject.VGroup.add) method, or use the + and += operators. Similarly, you
can subtract elements of a VGroup via `remove()` method, or
- and -= operators:

```pycon
>>> from manim import Triangle, Square, VGroup
>>> vg = VGroup()
>>> triangle, square = Triangle(), Square()
>>> vg.add(triangle)
VGroup(Triangle)
>>> vg + square  # a new VGroup is constructed
VGroup(Triangle, Square)
>>> vg  # not modified
VGroup(Triangle)
>>> vg += square
>>> vg  # modifies vg
VGroup(Triangle, Square)
>>> vg.remove(triangle)
VGroup(Square)
>>> vg - square  # a new VGroup is constructed
VGroup()
>>> vg  # not modified
VGroup(Square)
>>> vg -= square
>>> vg  # modifies vg
VGroup()
```

### Methods

| [`add`](#manim.mobject.types.vectorized_mobject.VGroup.add)   | Checks if all passed elements are an instance, or iterables of VMobject and then adds them to submobjects   |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|

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
  * **vmobjects** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *Iterable* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*)
  * **kwargs** (*Any*)

#### \_original_\_init_\_(\*vmobjects, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vmobjects** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *Iterable* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*)
  * **kwargs** (*Any*)
* **Return type:**
  None

#### add(\*vmobjects)

Checks if all passed elements are an instance, or iterables of VMobject and then adds them to submobjects

* **Parameters:**
  **vmobjects** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *|* *Iterable* *[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*) – List or iterable of VMobjects to add
* **Return type:**
  [`VGroup`](#manim.mobject.types.vectorized_mobject.VGroup)
* **Raises:**
  **TypeError** – If one element of the list, or iterable is not an instance of VMobject

### Examples

The following example shows how to add individual or multiple VMobject instances through the VGroup
constructor and its .add() method.

A VGroup can be created using iterables as well. Keep in mind that all generated values from an
iterable must be an instance of VMobject. This is demonstrated below:

To facilitate this, the iterable is unpacked before its individual instances are added to the VGroup.
As a result, when you index a VGroup, you will never get back an iterable.
Instead, you will always receive VMobject instances, including those
that were part of the iterable/s that you originally added to the VGroup.
