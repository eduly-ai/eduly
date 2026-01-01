# DefaultSectionType

Qualified name: `manim.scene.section.DefaultSectionType`

### *class* DefaultSectionType(value, names=<not given>, \*values, module=None, qualname=None, type=None, start=1, boundary=None)

Bases: `str`, `Enum`

The type of a section can be used for third party applications.
A presentation system could for example use the types to created loops.

### Examples

This class can be reimplemented for more types:

```default
class PresentationSectionType(str, Enum):
    # start, end, wait for continuation by user
    NORMAL = "presentation.normal"
    # start, end, immediately continue to next section
    SKIP = "presentation.skip"
    # start, end, restart, immediately continue to next section when continued by user
    LOOP = "presentation.loop"
    # start, end, restart, finish animation first when user continues
    COMPLETE_LOOP = "presentation.complete_loop"
```

### Methods

### Attributes

| `NORMAL`   |    |
|------------|----|
