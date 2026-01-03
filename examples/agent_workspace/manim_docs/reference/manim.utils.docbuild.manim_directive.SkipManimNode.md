# SkipManimNode

Qualified name: `manim.utils.docbuild.manim\_directive.SkipManimNode`

### *class* SkipManimNode(rawsource='', \*children, \*\*attributes)

Bases: `Admonition`, `Element`

Auxiliary node class that is used when the `skip-manim` tag is present
or `.pot` files are being built.

Skips rendering the manim directive and outputs a placeholder instead.

### Methods

### Attributes

| `basic_attributes`     | Tuple of attributes which are defined for every Element-derived class instance and can be safely transferred to a different node.   |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `child_text_separator` | Separator for child nodes, used by astext() method.                                                                                 |
| `document`             | Return the document root node of the tree containing this Node.                                                                     |
| `known_attributes`     | Tuple of attributes that are known to the Element base class.                                                                       |
| `line`                 | The line number (1-based) of the beginning of this Node in source.                                                                  |
| `list_attributes`      | Tuple of attributes that are automatically initialized to empty lists for all nodes.                                                |
| `local_attributes`     | Tuple of class-specific attributes that should not be copied with the standard attributes when replacing a node.                    |
| `parent`               | Back-reference to the Node immediately containing this Node.                                                                        |
| `source`               | Path or description of the input source which generated this Node.                                                                  |
| `tagname`              | The element generic identifier.                                                                                                     |
| `rawsource`            | The raw text from which this element was constructed.                                                                               |
| `children`             | List of child nodes (elements and/or Text).                                                                                         |
| `attributes`           | value}.                                                                                                                             |
