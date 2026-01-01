# LayoutFunction

Qualified name: `manim.mobject.graph.LayoutFunction`

### *class* LayoutFunction(\*args, \*\*kwargs)

Bases: `Protocol`

A protocol for automatic layout functions that compute a layout for a graph to be used in `change_layout()`.

#### NOTE
The layout function must be a pure function, i.e., it must not modify the graph passed to it.

### Examples

Here is an example that arranges nodes in an n x m grid in sorted order.

Several automatic layouts are provided by manim, and can be used by passing their name as the `layout` parameter to `change_layout()`.
Alternatively, a custom layout function can be passed to `change_layout()` as the `layout` parameter. Such a function must adhere to the [`LayoutFunction`](#manim.mobject.graph.LayoutFunction) protocol.

The [`LayoutFunction`](#manim.mobject.graph.LayoutFunction) s provided by manim are illustrated below:

- Circular Layout: places the vertices on a circle

- Kamada Kawai Layout: tries to place the vertices such that the given distances between them are respected

- Partite Layout: places vertices into distinct partitions

- Planar Layout: places vertices such that edges do not cross

- Random Layout: randomly places vertices

- Shell Layout: places vertices in concentric circles

- Spectral Layout: places vertices using the eigenvectors of the graph Laplacian (clusters nodes which are an approximation of the ratio cut)

- Sprial Layout: places vertices in a spiraling pattern

- Spring Layout: places nodes according to the Fruchterman-Reingold force-directed algorithm (attempts to minimize edge length while maximizing node separation)

- Tree Layout: places vertices into a tree with a root node and branches (can only be used with legal trees)

### Methods
