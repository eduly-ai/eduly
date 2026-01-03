# GenericGraph

Qualified name: `manim.mobject.graph.GenericGraph`

### *class* GenericGraph(vertices, edges, labels=False, label_fill_color=ManimColor('#000000'), layout='spring', layout_scale=2, layout_config=None, vertex_type=<class 'manim.mobject.geometry.arc.Dot'>, vertex_config=None, vertex_mobjects=None, edge_type=<class 'manim.mobject.geometry.line.Line'>, partitions=None, root_vertex=None, edge_config=None)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

Abstract base class for graphs (that is, a collection of vertices
connected with edges).

Graphs can be instantiated by passing both a list of (distinct, hashable)
vertex names, together with list of edges (as tuples of vertex names). See
the examples for concrete implementations of this class for details.

#### NOTE
This implementation uses updaters to make the edges move with
the vertices.

#### SEE ALSO
[`Graph`](manim.mobject.graph.Graph.md#manim.mobject.graph.Graph), [`DiGraph`](manim.mobject.graph.DiGraph.md#manim.mobject.graph.DiGraph)

* **Parameters:**
  * **vertices** (*Sequence* *[**Hashable* *]*) – A list of vertices. Must be hashable elements.
  * **edges** (*Sequence* *[**tuple* *[**Hashable* *,* *Hashable* *]* *]*) – A list of edges, specified as tuples `(u, v)` where both `u`
    and `v` are vertices.
  * **labels** (*bool* *|* *dict*) – Controls whether or not vertices are labeled. If `False` (the default),
    the vertices are not labeled; if `True` they are labeled using their
    names (as specified in `vertices`) via [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex). Alternatively,
    custom labels can be specified by passing a dictionary whose keys are
    the vertices, and whose values are the corresponding vertex labels
    (rendered via, e.g., [`Text`](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text) or [`Tex`](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex)).
  * **label_fill_color** (*str*) – Sets the fill color of the default labels generated when `labels`
    is set to `True`. Has no effect for other values of `labels`.
  * **layout** (*LayoutName* *|* *dict* *[**Hashable* *,* [*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *]*  *|* [*LayoutFunction*](manim.mobject.graph.LayoutFunction.md#manim.mobject.graph.LayoutFunction)) – Either one of `"spring"` (the default), `"circular"`, `"kamada_kawai"`,
    `"planar"`, `"random"`, `"shell"`, `"spectral"`, `"spiral"`, `"tree"`, and `"partite"`
    for automatic vertex positioning primarily using `networkx`
    (see [their documentation](https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout)
    for more details), a dictionary specifying a coordinate (value)
    for each vertex (key) for manual positioning, or a .:class:~.LayoutFunction with a user-defined automatic layout.
  * **layout_config** (*dict* *|* *None*) – Only for automatic layouts. A dictionary whose entries
    are passed as keyword arguments to the named layout or automatic layout function
    specified via `layout`.
    The `tree` layout also accepts a special parameter `vertex_spacing`
    passed as a keyword argument inside the `layout_config` dictionary.
    Passing a tuple `(space_x, space_y)` as this argument overrides
    the value of `layout_scale` and ensures that vertices are arranged
    in a way such that the centers of siblings in the same layer are
    at least `space_x` units apart horizontally, and neighboring layers
    are spaced `space_y` units vertically.
  * **layout_scale** (*float* *|* *tuple* *[**float* *,* *float* *,* *float* *]*) – The scale of automatically generated layouts: the vertices will
    be arranged such that the coordinates are located within the
    interval `[-scale, scale]`. Some layouts accept a tuple `(scale_x, scale_y)`
    causing the first coordinate to be in the interval `[-scale_x, scale_x]`,
    and the second in `[-scale_y, scale_y]`. Default: 2.
  * **vertex_type** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The mobject class used for displaying vertices in the scene.
  * **vertex_config** (*dict* *|* *None*) – Either a dictionary containing keyword arguments to be passed to
    the class specified via `vertex_type`, or a dictionary whose keys
    are the vertices, and whose values are dictionaries containing keyword
    arguments for the mobject related to the corresponding vertex.
  * **vertex_mobjects** (*dict* *|* *None*) – A dictionary whose keys are the vertices, and whose values are
    mobjects to be used as vertices. Passing vertices here overrides
    all other configuration options for a vertex.
  * **edge_type** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The mobject class used for displaying edges in the scene.
    Must be a subclass of [`Line`](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line) for default updaters to work.
  * **edge_config** (*dict* *|* *None*) – Either a dictionary containing keyword arguments to be passed
    to the class specified via `edge_type`, or a dictionary whose
    keys are the edges, and whose values are dictionaries containing
    keyword arguments for the mobject related to the corresponding edge.
  * **partitions** (*Sequence* *[**Sequence* *[**Hashable* *]* *]*  *|* *None*)
  * **root_vertex** (*Hashable* *|* *None*)

### Methods

| [`add_edges`](#manim.mobject.graph.GenericGraph.add_edges)             | Add new edges to the graph.                                                                                                                                                         |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`add_vertices`](#manim.mobject.graph.GenericGraph.add_vertices)       | Add a list of vertices to the graph.                                                                                                                                                |
| [`change_layout`](#manim.mobject.graph.GenericGraph.change_layout)     | Change the layout of this graph.                                                                                                                                                    |
| [`from_networkx`](#manim.mobject.graph.GenericGraph.from_networkx)     | Build a [`Graph`](manim.mobject.graph.Graph.md#manim.mobject.graph.Graph) or [`DiGraph`](manim.mobject.graph.DiGraph.md#manim.mobject.graph.DiGraph) from a given `networkx` graph. |
| [`remove_edges`](#manim.mobject.graph.GenericGraph.remove_edges)       | Remove several edges from the graph.                                                                                                                                                |
| [`remove_vertices`](#manim.mobject.graph.GenericGraph.remove_vertices) | Remove several vertices from the graph.                                                                                                                                             |

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

#### \_add_edge(edge, edge_type=<class 'manim.mobject.geometry.line.Line'>, edge_config=None)

Add a new edge to the graph.

* **Parameters:**
  * **edge** (*tuple* *[**Hashable* *,* *Hashable* *]*) – The edge (as a tuple of vertex identifiers) to be added. If a non-existing
    vertex is passed, a new vertex with default settings will be created. Create
    new vertices yourself beforehand to customize them.
  * **edge_type** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The mobject class used for displaying edges in the scene.
  * **edge_config** (*dict* *|* *None*) – A dictionary containing keyword arguments to be passed
    to the class specified via `edge_type`.
* **Returns:**
  A group containing all newly added vertices and edges.
* **Return type:**
  [Group](manim.mobject.mobject.Group.md#manim.mobject.mobject.Group)

#### \_add_vertex(vertex, position=None, label=False, label_fill_color=ManimColor('#000000'), vertex_type=<class 'manim.mobject.geometry.arc.Dot'>, vertex_config=None, vertex_mobject=None)

Add a vertex to the graph.

* **Parameters:**
  * **vertex** (*Hashable*) – A hashable vertex identifier.
  * **position** ([*Point3DLike*](manim.typing.md#manim.typing.Point3DLike) *|* *None*) – The coordinates where the new vertex should be added. If `None`, the center
    of the graph is used.
  * **label** (*bool*) – Controls whether or not the vertex is labeled. If `False` (the default),
    the vertex is not labeled; if `True` it is labeled using its
    names (as specified in `vertex`) via [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex). Alternatively,
    any [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) can be passed to be used as the label.
  * **label_fill_color** (*str*) – Sets the fill color of the default labels generated when `labels`
    is set to `True`. Has no effect for other values of `label`.
  * **vertex_type** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The mobject class used for displaying vertices in the scene.
  * **vertex_config** (*dict* *|* *None*) – A dictionary containing keyword arguments to be passed to
    the class specified via `vertex_type`.
  * **vertex_mobject** (*dict* *|* *None*) – The mobject to be used as the vertex. Overrides all other
    vertex customization options.
* **Return type:**
  [Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

#### *static* \_empty_networkx_graph()

Return an empty networkx graph for the given graph type.

* **Return type:**
  *Graph*

#### \_original_\_init_\_(vertices, edges, labels=False, label_fill_color=ManimColor('#000000'), layout='spring', layout_scale=2, layout_config=None, vertex_type=<class 'manim.mobject.geometry.arc.Dot'>, vertex_config=None, vertex_mobjects=None, edge_type=<class 'manim.mobject.geometry.line.Line'>, partitions=None, root_vertex=None, edge_config=None)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vertices** (*Sequence* *[**Hashable* *]*)
  * **edges** (*Sequence* *[**tuple* *[**Hashable* *,* *Hashable* *]* *]*)
  * **labels** (*bool* *|* *dict*)
  * **label_fill_color** (*str*)
  * **layout** (*Literal* *[* *'circular'* *,*  *'kamada_kawai'* *,*  *'partite'* *,*  *'planar'* *,*  *'random'* *,*  *'shell'* *,*  *'spectral'* *,*  *'spiral'* *,*  *'spring'* *,*  *'tree'* *]*  *|* *dict* *[* *~collections.abc.Hashable* *,*  *~manim.typing.Point3DLike* *]*  *|*  *~manim.mobject.graph.LayoutFunction*)
  * **layout_scale** (*float* *|* *tuple* *[**float* *,* *float* *,* *float* *]*)
  * **layout_config** (*dict* *|* *None*)
  * **vertex_type** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*)
  * **vertex_config** (*dict* *|* *None*)
  * **vertex_mobjects** (*dict* *|* *None*)
  * **edge_type** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*)
  * **partitions** (*Sequence* *[**Sequence* *[**Hashable* *]* *]*  *|* *None*)
  * **root_vertex** (*Hashable* *|* *None*)
  * **edge_config** (*dict* *|* *None*)
* **Return type:**
  None

#### \_populate_edge_dict(edges, edge_type)

Helper method for populating the edges of the graph.

* **Parameters:**
  * **edges** (*list* *[**tuple* *[**Hashable* *,* *Hashable* *]* *]*)
  * **edge_type** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*)

#### \_remove_edge(edge)

Remove an edge from the graph.

* **Parameters:**
  **edge** (*tuple* *[**Hashable* *]*) – The edge (i.e., a tuple of vertex identifiers) to be removed from the graph.
* **Returns:**
  The removed edge.
* **Return type:**
  [Mobject](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)

#### \_remove_vertex(vertex)

Remove a vertex (as well as all incident edges) from the graph.

* **Parameters:**
  **vertex** – The identifier of a vertex to be removed.
* **Returns:**
  A mobject containing all removed objects.
* **Return type:**
  [Group](manim.mobject.mobject.Group.md#manim.mobject.mobject.Group)

#### add_edges(\*edges, edge_type=<class 'manim.mobject.geometry.line.Line'>, edge_config=None, \*\*kwargs)

Add new edges to the graph.

* **Parameters:**
  * **edges** (*tuple* *[**Hashable* *,* *Hashable* *]*) – Edges (as tuples of vertex identifiers) to be added. If a non-existing
    vertex is passed, a new vertex with default settings will be created. Create
    new vertices yourself beforehand to customize them.
  * **edge_type** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The mobject class used for displaying edges in the scene.
  * **edge_config** (*dict* *|* *None*) – A dictionary either containing keyword arguments to be passed
    to the class specified via `edge_type`, or a dictionary
    whose keys are the edge tuples, and whose values are dictionaries
    containing keyword arguments to be passed for the construction
    of the corresponding edge.
  * **kwargs** – Any further keyword arguments are passed to [`add_vertices()`](#manim.mobject.graph.GenericGraph.add_vertices)
    which is used to create new vertices in the passed edges.
* **Returns:**
  A group containing all newly added vertices and edges.
* **Return type:**
  [Group](manim.mobject.mobject.Group.md#manim.mobject.mobject.Group)

#### add_vertices(\*vertices, positions=None, labels=False, label_fill_color=ManimColor('#000000'), vertex_type=<class 'manim.mobject.geometry.arc.Dot'>, vertex_config=None, vertex_mobjects=None)

Add a list of vertices to the graph.

* **Parameters:**
  * **vertices** (*Hashable*) – Hashable vertex identifiers.
  * **positions** (*dict* *|* *None*) – A dictionary specifying the coordinates where the new vertices should be added.
    If `None`, all vertices are created at the center of the graph.
  * **labels** (*bool*) – Controls whether or not the vertex is labeled. If `False` (the default),
    the vertex is not labeled; if `True` it is labeled using its
    names (as specified in `vertex`) via [`MathTex`](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex). Alternatively,
    any [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) can be passed to be used as the label.
  * **label_fill_color** (*str*) – Sets the fill color of the default labels generated when `labels`
    is set to `True`. Has no effect for other values of `labels`.
  * **vertex_type** (*type* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*) – The mobject class used for displaying vertices in the scene.
  * **vertex_config** (*dict* *|* *None*) – A dictionary containing keyword arguments to be passed to
    the class specified via `vertex_type`.
  * **vertex_mobjects** (*dict* *|* *None*) – A dictionary whose keys are the vertex identifiers, and whose
    values are mobjects that should be used as vertices. Overrides
    all other vertex customization options.
  * **self** ([*Graph*](manim.mobject.graph.Graph.md#manim.mobject.graph.Graph))

#### change_layout(layout='spring', layout_scale=2, layout_config=None, partitions=None, root_vertex=None)

Change the layout of this graph.

See the documentation of [`Graph`](manim.mobject.graph.Graph.md#manim.mobject.graph.Graph) for details about the
keyword arguments.

### Examples

* **Parameters:**
  * **layout** (*Literal* *[* *'circular'* *,*  *'kamada_kawai'* *,*  *'partite'* *,*  *'planar'* *,*  *'random'* *,*  *'shell'* *,*  *'spectral'* *,*  *'spiral'* *,*  *'spring'* *,*  *'tree'* *]*  *|* *dict* *[* *~collections.abc.Hashable* *,*  *~manim.typing.Point3DLike* *]*  *|*  *~manim.mobject.graph.LayoutFunction*)
  * **layout_scale** (*float* *|* *tuple* *[**float* *,* *float* *,* *float* *]*)
  * **layout_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **partitions** (*list* *[**list* *[**Hashable* *]* *]*  *|* *None*)
  * **root_vertex** (*Hashable* *|* *None*)
* **Return type:**
  [*Graph*](manim.mobject.graph.Graph.md#manim.mobject.graph.Graph)

#### *classmethod* from_networkx(nxgraph, \*\*kwargs)

Build a [`Graph`](manim.mobject.graph.Graph.md#manim.mobject.graph.Graph) or [`DiGraph`](manim.mobject.graph.DiGraph.md#manim.mobject.graph.DiGraph) from a
given `networkx` graph.

* **Parameters:**
  * **nxgraph** (*Graph* *|* *DiGraph*) – A `networkx` graph or digraph.
  * **\*\*kwargs** – Keywords to be passed to the constructor of [`Graph`](manim.mobject.graph.Graph.md#manim.mobject.graph.Graph).

### Examples

#### remove_edges(\*edges)

Remove several edges from the graph.

* **Parameters:**
  **edges** (*tuple* *[**Hashable* *]*) – Edges to be removed from the graph.
* **Returns:**
  A group containing all removed edges.
* **Return type:**
  [Group](manim.mobject.mobject.Group.md#manim.mobject.mobject.Group)

#### remove_vertices(\*vertices)

Remove several vertices from the graph.

* **Parameters:**
  **vertices** – Vertices to be removed from the graph.

### Examples

```default
>>> G = Graph([1, 2, 3], [(1, 2), (2, 3)])
>>> removed = G.remove_vertices(2, 3); removed
VGroup(Line, Line, Dot, Dot)
>>> G
Undirected graph on 1 vertices and 0 edges
```
