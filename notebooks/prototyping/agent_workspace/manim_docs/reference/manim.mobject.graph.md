# graph

Mobjects used to represent mathematical graphs (think graph theory, not plotting).

### Type Aliases

### *class* NxGraph

```default
nx.classes.graph.Graph | nx.classes.digraph.DiGraph
```

### Classes

| [`DiGraph`](manim.mobject.graph.DiGraph.md#manim.mobject.graph.DiGraph)                      | A directed graph.                                                                                            |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [`GenericGraph`](manim.mobject.graph.GenericGraph.md#manim.mobject.graph.GenericGraph)       | Abstract base class for graphs (that is, a collection of vertices connected with edges).                     |
| [`Graph`](manim.mobject.graph.Graph.md#manim.mobject.graph.Graph)                            | An undirected graph (vertices connected with edges).                                                         |
| [`LayoutFunction`](manim.mobject.graph.LayoutFunction.md#manim.mobject.graph.LayoutFunction) | A protocol for automatic layout functions that compute a layout for a graph to be used in `change_layout()`. |
