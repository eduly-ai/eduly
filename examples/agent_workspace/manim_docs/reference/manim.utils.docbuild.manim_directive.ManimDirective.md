# ManimDirective

Qualified name: `manim.utils.docbuild.manim\_directive.ManimDirective`

### *class* ManimDirective(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)

Bases: `Directive`

The manim directive, rendering videos while building
the documentation.

See the module docstring for documentation.

### Methods

| `run`   |    |
|---------|----|

### Attributes

| [`final_argument_whitespace`](#manim.utils.docbuild.manim_directive.ManimDirective.final_argument_whitespace)   | May the final argument contain whitespace?                 |
|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| [`has_content`](#manim.utils.docbuild.manim_directive.ManimDirective.has_content)                               | May the directive have content?                            |
| [`option_spec`](#manim.utils.docbuild.manim_directive.ManimDirective.option_spec)                               | Mapping of option names to validator functions.            |
| [`optional_arguments`](#manim.utils.docbuild.manim_directive.ManimDirective.optional_arguments)                 | Number of optional arguments after the required arguments. |
| [`required_arguments`](#manim.utils.docbuild.manim_directive.ManimDirective.required_arguments)                 | Number of required directive arguments.                    |

#### final_argument_whitespace *= True*

May the final argument contain whitespace?

#### has_content *= True*

May the directive have content?

#### option_spec *= {'hide_source': <class 'bool'>, 'no_autoplay': <class 'bool'>, 'quality': <function ManimDirective.<lambda>>, 'ref_classes': <function ManimDirective.<lambda>>, 'ref_functions': <function ManimDirective.<lambda>>, 'ref_methods': <function ManimDirective.<lambda>>, 'ref_modules': <function ManimDirective.<lambda>>, 'save_as_gif': <class 'bool'>, 'save_last_frame': <class 'bool'>}*

Mapping of option names to validator functions.

#### optional_arguments *= 0*

Number of optional arguments after the required arguments.

#### required_arguments *= 1*

Number of required directive arguments.
