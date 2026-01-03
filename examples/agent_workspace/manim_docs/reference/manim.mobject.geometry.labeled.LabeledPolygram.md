# LabeledPolygram

Qualified name: `manim.mobject.geometry.labeled.LabeledPolygram`

### *class* LabeledPolygram(\*vertex_groups, label, precision=0.01, label_config=None, box_config=None, frame_config=None, \*\*kwargs)

Bases: [`Polygram`](manim.mobject.geometry.polygram.Polygram.md#manim.mobject.geometry.polygram.Polygram)

Constructs a polygram containing a label box at its pole of inaccessibility.

* **Parameters:**
  * **vertex_groups** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array)) – Vertices passed to the [`Polygram`](manim.mobject.geometry.polygram.Polygram.md#manim.mobject.geometry.polygram.Polygram) constructor.
  * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text)) – Label that will be displayed on the Polygram.
  * **precision** (*float*) – The precision used by the PolyLabel algorithm.
  * **label_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – A dictionary containing the configuration for the label.
    This is only applied if `label` is of type `str`.
  * **box_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – A dictionary containing the configuration for the background box.
  * **frame_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*) – 

    A dictionary containing the configuration for the frame.

    #### NOTE
    The PolyLabel Algorithm expects each vertex group to form a closed ring.
    If the input is open, [`LabeledPolygram`](#manim.mobject.geometry.labeled.LabeledPolygram) will attempt to close it.
    This may cause the polygon to intersect itself leading to unexpected results.
  * **kwargs** (*Any*)

### Examples

### Methods

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

#### \_original_\_init_\_(\*vertex_groups, label, precision=0.01, label_config=None, box_config=None, frame_config=None, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **vertex_groups** ([*Point3DLike_Array*](manim.typing.md#manim.typing.Point3DLike_Array))
  * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.md#manim.mobject.text.tex_mobject.Tex) *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.md#manim.mobject.text.tex_mobject.MathTex) *|* [*Text*](manim.mobject.text.text_mobject.Text.md#manim.mobject.text.text_mobject.Text))
  * **precision** (*float*)
  * **label_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **box_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **frame_config** (*dict* *[**str* *,* *Any* *]*  *|* *None*)
  * **kwargs** (*Any*)
* **Return type:**
  None
