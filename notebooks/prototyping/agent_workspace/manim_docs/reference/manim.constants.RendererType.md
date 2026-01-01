# RendererType

Qualified name: `manim.constants.RendererType`

### *class* RendererType(value, names=<not given>, \*values, module=None, qualname=None, type=None, start=1, boundary=None)

Bases: `Enum`

An enumeration of all renderer types that can be assigned to
the `config.renderer` attribute.

Manim’s configuration allows assigning string values to the renderer
setting, the values are then replaced by the corresponding enum object.
In other words, you can run:

```default
config.renderer = "opengl"
```

and checking the renderer afterwards reveals that the attribute has
assumed the value:

```default
<RendererType.OPENGL: 'opengl'>
```

### Attributes

| [`CAIRO`](#manim.constants.RendererType.CAIRO)   | A renderer based on the cairo backend.   |
|--------------------------------------------------|------------------------------------------|
| [`OPENGL`](#manim.constants.RendererType.OPENGL) | An OpenGL-based renderer.                |

#### CAIRO *= 'cairo'*

A renderer based on the cairo backend.

#### OPENGL *= 'opengl'*

An OpenGL-based renderer.
