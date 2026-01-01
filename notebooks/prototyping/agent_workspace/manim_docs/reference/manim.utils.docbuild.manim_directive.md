# manim_directive

## A directive for including Manim videos in a Sphinx document

When rendering the HTML documentation, the `.. manim::` directive
implemented here allows to include rendered videos.

Its basic usage that allows processing **inline content**
looks as follows:

```default
.. manim:: MyScene

    class MyScene(Scene):
        def construct(self):
            ...
```

It is required to pass the name of the class representing the
scene to be rendered to the directive.

As a second application, the directive can also be used to
render scenes that are defined within doctests, for example:

```default
.. manim:: DirectiveDoctestExample
    :ref_classes: Dot

    >>> from manim import Create, Dot, RED, Scene
    >>> dot = Dot(color=RED)
    >>> dot.color
    ManimColor('#FC6255')
    >>> class DirectiveDoctestExample(Scene):
    ...     def construct(self):
    ...         self.play(Create(dot))
```

### Options

Options can be passed as follows:

```default
.. manim:: <Class name>
    :<option name>: <value>
```

The following configuration options are supported by the
directive:

> hide_source
> : If this flag is present without argument,
>   the source code is not displayed above the rendered video.

> no_autoplay
> : If this flag is present without argument,
>   the video will not autoplay.

> quality
> : Controls render quality of the video, in analogy to
>   the corresponding command line flags.

> save_as_gif
> : If this flag is present without argument,
>   the scene is rendered as a gif.

> save_last_frame
> : If this flag is present without argument,
>   an image representing the last frame of the scene will
>   be rendered and displayed, instead of a video.

> ref_classes
> : A list of classes, separated by spaces, that is
>   rendered in a reference block after the source code.

> ref_functions
> : A list of functions, separated by spaces,
>   that is rendered in a reference block after the source code.

> ref_methods
> : A list of methods, separated by spaces,
>   that is rendered in a reference block after the source code.

### Classes

| [`ManimDirective`](manim.utils.docbuild.manim_directive.ManimDirective.md#manim.utils.docbuild.manim_directive.ManimDirective)   | The manim directive, rendering videos while building the documentation.                                 |
|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [`SetupMetadata`](manim.utils.docbuild.manim_directive.SetupMetadata.md#manim.utils.docbuild.manim_directive.SetupMetadata)      |                                                                                                         |
| [`SkipManimNode`](manim.utils.docbuild.manim_directive.SkipManimNode.md#manim.utils.docbuild.manim_directive.SkipManimNode)      | Auxiliary node class that is used when the `skip-manim` tag is present or `.pot` files are being built. |

### Functions

### depart(self, node)

* **Parameters:**
  * **self** ([*SkipManimNode*](manim.utils.docbuild.manim_directive.SkipManimNode.md#manim.utils.docbuild.manim_directive.SkipManimNode))
  * **node** (*Element*)
* **Return type:**
  None

### process_name_list(option_input, reference_type)

Reformats a string of space separated class names
as a list of strings containing valid Sphinx references.

### Tests

```default
>>> process_name_list("Tex TexTemplate", "class")
[':class:`~.Tex`', ':class:`~.TexTemplate`']
>>> process_name_list("Scene.play Mobject.rotate", "func")
[':func:`~.Scene.play`', ':func:`~.Mobject.rotate`']
```

* **Parameters:**
  * **option_input** (*str*)
  * **reference_type** (*str*)
* **Return type:**
  list[str]

### setup(app)

* **Parameters:**
  **app** (*Sphinx*)
* **Return type:**
  [SetupMetadata](manim.utils.docbuild.manim_directive.SetupMetadata.md#manim.utils.docbuild.manim_directive.SetupMetadata)

### visit(self, node, name='')

* **Parameters:**
  * **self** ([*SkipManimNode*](manim.utils.docbuild.manim_directive.SkipManimNode.md#manim.utils.docbuild.manim_directive.SkipManimNode))
  * **node** (*Element*)
  * **name** (*str*)
* **Return type:**
  None
