# RandomColorGenerator

Qualified name: `manim.utils.color.core.RandomColorGenerator`

### *class* RandomColorGenerator(seed=None, sample_colors=None)

Bases: `object`

### Methods

| [`next`](#manim.utils.color.core.RandomColorGenerator.next)   | Returns the next color from the configured color list.   |
|---------------------------------------------------------------|----------------------------------------------------------|
* **Parameters:**
  * **seed** (*int* *|* *None*)
  * **sample_colors** (*list* *[*[*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor) *]*  *|* *None*)

#### *classmethod* \_random_color()

Internal method to generate a random color using the singleton instance of
RandomColorGenerator.
It will be used by proxy method random_color publicly available
and makes it backwards compatible.

* **Returns:**
  A randomly selected color from the configured color list of
  the singleton instance.
* **Return type:**
  [ManimColor](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)

#### \_singleton *: [RandomColorGenerator](#manim.utils.color.core.RandomColorGenerator) | None* *= None*

A generator for producing random colors from a given list of Manim colors,
optionally in a reproducible sequence using a seed value.

When initialized with a specific seed, this class produces a deterministic
sequence of [`ManimColor`](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor) instances. If no seed is provided, the selection is
non-deterministic using Python’s global random state.

* **Parameters:**
  * **seed** – A seed value to initialize the internal random number generator.
    If `None` (the default), colors are chosen using the global random state.
  * **sample_colors** – A custom list of Manim colors to sample from. Defaults to the full Manim
    color palette.

### Examples

Without a seed (non-deterministic):

```default
>>> from manim import RandomColorGenerator, ManimColor, RED, GREEN, BLUE
>>> rnd = RandomColorGenerator()
>>> isinstance(rnd.next(), ManimColor)
True
```

With a seed (deterministic sequence):

```default
>>> rnd = RandomColorGenerator(42)
>>> rnd.next()
ManimColor('#ECE7E2')
>>> rnd.next()
ManimColor('#BBBBBB')
>>> rnd.next()
ManimColor('#BBBBBB')
```

Re-initializing with the same seed gives the same sequence:

```default
>>> rnd2 = RandomColorGenerator(42)
>>> rnd2.next()
ManimColor('#ECE7E2')
>>> rnd2.next()
ManimColor('#BBBBBB')
>>> rnd2.next()
ManimColor('#BBBBBB')
```

Using a custom color list:

```default
>>> custom_palette = [RED, GREEN, BLUE]
>>> rnd_custom = RandomColorGenerator(1, sample_colors=custom_palette)
>>> rnd_custom.next() in custom_palette
True
>>> rnd_custom.next() in custom_palette
True
```

Without a seed and custom palette (non-deterministic):

```default
>>> rnd_nodet = RandomColorGenerator(sample_colors=[RED])
>>> rnd_nodet.next()
ManimColor('#FC6255')
```

#### next()

Returns the next color from the configured color list.

* **Returns:**
  A randomly selected color from the specified color list.
* **Return type:**
  [ManimColor](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)

### Examples

Usage:

```default
>>> from manim import RandomColorGenerator, RED
>>> rnd = RandomColorGenerator(sample_colors=[RED])
>>> rnd.next()
ManimColor('#FC6255')
```
