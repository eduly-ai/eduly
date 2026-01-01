# SVGMobject

Qualified name: `manim.mobject.svg.svg\_mobject.SVGMobject`

### *class* SVGMobject(file_name=None, should_center=True, height=2, width=None, color=None, opacity=None, fill_color=None, fill_opacity=None, stroke_color=None, stroke_opacity=None, stroke_width=None, svg_default=None, path_string_config=None, use_svg_cache=True, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A vectorized mobject created from importing an SVG file.

* **Parameters:**
  * **file_name** (*str* *|* *os.PathLike* *|* *None*) – The path to the SVG file.
  * **should_center** (*bool*) – Whether or not the mobject should be centered after
    being imported.
  * **height** (*float* *|* *None*) – The target height of the mobject, set to 2 Manim units by default.
    If the height and width are both set to `None`, the mobject
    is imported without being scaled.
  * **width** (*float* *|* *None*) – The target width of the mobject, set to `None` by default. If
    the height and the width are both set to `None`, the mobject
    is imported without being scaled.
  * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor)) – The color (both fill and stroke color) of the mobject. If
    `None` (the default), the colors set in the SVG file
    are used.
  * **opacity** (*float* *|* *None*) – The opacity (both fill and stroke opacity) of the mobject.
    If `None` (the default), the opacity set in the SVG file
    is used.
  * **fill_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – The fill color of the mobject. If `None` (the default),
    the fill colors set in the SVG file are used.
  * **fill_opacity** (*float* *|* *None*) – The fill opacity of the mobject. If `None` (the default),
    the fill opacities set in the SVG file are used.
  * **stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*) – The stroke color of the mobject. If `None` (the default),
    the stroke colors set in the SVG file are used.
  * **stroke_opacity** (*float* *|* *None*) – The stroke opacity of the mobject. If `None` (the default),
    the stroke opacities set in the SVG file are used.
  * **stroke_width** (*float* *|* *None*) – The stroke width of the mobject. If `None` (the default),
    the stroke width values set in the SVG file are used.
  * **svg_default** (*dict* *|* *None*) – A dictionary in which fallback values for unspecified
    properties of elements in the SVG file are defined. If
    `None` (the default), `color`, `opacity`, `fill_color`
    `fill_opacity`, `stroke_color`, and `stroke_opacity`
    are set to `None`, and `stroke_width` is set to 0.
  * **path_string_config** (*dict* *|* *None*) – A dictionary with keyword arguments passed to
    [`VMobjectFromSVGPath`](manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.md#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath) used for importing path elements.
    If `None` (the default), no additional arguments are passed.
  * **use_svg_cache** (*bool*) – If True (default), the svg inputs (e.g. file_name, settings)
    will be used as a key and a copy of the created mobject will
    be saved using that key to be quickly retrieved if the same
    inputs need be processed later. For large SVGs which are used
    only once, this can be omitted to improve performance.
  * **kwargs** (*Any*) – Further arguments passed to the parent class.

### Methods

| [`apply_style_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.apply_style_to_mobject)         | Apply SVG style information to the converted mobject.                     |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [`ellipse_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.ellipse_to_mobject)                 | Convert an ellipse or circle element to a vectorized mobject.             |
| [`generate_config_style_dict`](#manim.mobject.svg.svg_mobject.SVGMobject.generate_config_style_dict) | Generate a dictionary holding the default style information.              |
| [`generate_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject)                     | Parse the SVG and translate its elements to submobjects.                  |
| [`get_file_path`](#manim.mobject.svg.svg_mobject.SVGMobject.get_file_path)                           | Search for an existing file based on the specified file name.             |
| [`get_mobjects_from`](#manim.mobject.svg.svg_mobject.SVGMobject.get_mobjects_from)                   | Convert the elements of the SVG to a list of mobjects.                    |
| [`handle_transform`](#manim.mobject.svg.svg_mobject.SVGMobject.handle_transform)                     | Apply SVG transformations to the converted mobject.                       |
| [`init_svg_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.init_svg_mobject)                     | Checks whether the SVG has already been imported and generates it if not. |
| [`line_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.line_to_mobject)                       | Convert a line element to a vectorized mobject.                           |
| [`modify_xml_tree`](#manim.mobject.svg.svg_mobject.SVGMobject.modify_xml_tree)                       | Modifies the SVG element tree to include default style information.       |
| [`move_into_position`](#manim.mobject.svg.svg_mobject.SVGMobject.move_into_position)                 | Scale and move the generated mobject into position.                       |
| [`path_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.path_to_mobject)                       | Convert a path element to a vectorized mobject.                           |
| [`polygon_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.polygon_to_mobject)                 | Convert a polygon element to a vectorized mobject.                        |
| [`polyline_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.polyline_to_mobject)               | Convert a polyline element to a vectorized mobject.                       |
| [`rect_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.rect_to_mobject)                       | Convert a rectangle element to a vectorized mobject.                      |
| [`text_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.text_to_mobject)                       | Convert a text element to a vectorized mobject.                           |

### Attributes

| `animate`                                                          | Used to animate the application of any method of `self`.               |
|--------------------------------------------------------------------|------------------------------------------------------------------------|
| `animation_overrides`                                              |                                                                        |
| `color`                                                            |                                                                        |
| `depth`                                                            | The depth of the mobject.                                              |
| `fill_color`                                                       | If there are multiple colors (for gradient) this returns the first one |
| [`hash_seed`](#manim.mobject.svg.svg_mobject.SVGMobject.hash_seed) | A unique hash representing the result of the generated mobject points. |
| `height`                                                           | The height of the mobject.                                             |
| `n_points_per_curve`                                               |                                                                        |
| `sheen_factor`                                                     |                                                                        |
| `stroke_color`                                                     |                                                                        |
| `width`                                                            | The width of the mobject.                                              |

#### \_original_\_init_\_(file_name=None, should_center=True, height=2, width=None, color=None, opacity=None, fill_color=None, fill_opacity=None, stroke_color=None, stroke_opacity=None, stroke_width=None, svg_default=None, path_string_config=None, use_svg_cache=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **file_name** (*str* *|* *os.PathLike* *|* *None*)
  * **should_center** (*bool*)
  * **height** (*float* *|* *None*)
  * **width** (*float* *|* *None*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **opacity** (*float* *|* *None*)
  * **fill_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **fill_opacity** (*float* *|* *None*)
  * **stroke_color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **stroke_opacity** (*float* *|* *None*)
  * **stroke_width** (*float* *|* *None*)
  * **svg_default** (*dict* *|* *None*)
  * **path_string_config** (*dict* *|* *None*)
  * **use_svg_cache** (*bool*)
  * **kwargs** (*Any*)

#### *static* apply_style_to_mobject(mob, shape)

Apply SVG style information to the converted mobject.

* **Parameters:**
  * **mob** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The converted mobject.
  * **shape** (*GraphicObject*) – The parsed SVG element.
* **Return type:**
  [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

#### *static* ellipse_to_mobject(ellipse)

Convert an ellipse or circle element to a vectorized mobject.

* **Parameters:**
  **ellipse** (*Ellipse* *|* *Circle*) – The parsed SVG ellipse or circle.
* **Return type:**
  [*Circle*](manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle)

#### generate_config_style_dict()

Generate a dictionary holding the default style information.

* **Return type:**
  dict[str, str]

#### generate_mobject()

Parse the SVG and translate its elements to submobjects.

* **Return type:**
  None

#### get_file_path()

Search for an existing file based on the specified file name.

* **Return type:**
  *Path*

#### get_mobjects_from(svg)

Convert the elements of the SVG to a list of mobjects.

* **Parameters:**
  **svg** (*SVG*) – The parsed SVG file.
* **Return type:**
  list[[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)]

#### *static* handle_transform(mob, matrix)

Apply SVG transformations to the converted mobject.

* **Parameters:**
  * **mob** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The converted mobject.
  * **matrix** (*Matrix*) – The transformation matrix determined from the SVG
    transformation.
* **Return type:**
  [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

#### *property* hash_seed *: tuple*

A unique hash representing the result of the generated
mobject points.

Used as keys in the `SVG_HASH_TO_MOB_MAP` caching dictionary.

#### init_svg_mobject(use_svg_cache)

Checks whether the SVG has already been imported and
generates it if not.

#### SEE ALSO
[`SVGMobject.generate_mobject()`](#manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject)

* **Parameters:**
  **use_svg_cache** (*bool*)
* **Return type:**
  None

#### *static* line_to_mobject(line)

Convert a line element to a vectorized mobject.

* **Parameters:**
  **line** (*Line*) – The parsed SVG line.
* **Return type:**
  [*Line*](manim.mobject.geometry.line.Line.md#manim.mobject.geometry.line.Line)

#### modify_xml_tree(element_tree)

Modifies the SVG element tree to include default
style information.

* **Parameters:**
  **element_tree** (*ElementTree*) – The parsed element tree from the SVG file.
* **Return type:**
  *ElementTree*

#### move_into_position()

Scale and move the generated mobject into position.

* **Return type:**
  None

#### path_to_mobject(path)

Convert a path element to a vectorized mobject.

* **Parameters:**
  **path** (*Path*) – The parsed SVG path.
* **Return type:**
  [*VMobjectFromSVGPath*](manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.md#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath)

#### *static* polygon_to_mobject(polygon)

Convert a polygon element to a vectorized mobject.

* **Parameters:**
  **polygon** (*Polygon*) – The parsed SVG polygon.
* **Return type:**
  [*Polygon*](manim.mobject.geometry.polygram.Polygon.md#manim.mobject.geometry.polygram.Polygon)

#### polyline_to_mobject(polyline)

Convert a polyline element to a vectorized mobject.

* **Parameters:**
  **polyline** (*Polyline*) – The parsed SVG polyline.
* **Return type:**
  [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

#### *static* rect_to_mobject(rect)

Convert a rectangle element to a vectorized mobject.

* **Parameters:**
  **rect** (*Rect*) – The parsed SVG rectangle.
* **Return type:**
  [*Rectangle*](manim.mobject.geometry.polygram.Rectangle.md#manim.mobject.geometry.polygram.Rectangle)

#### *static* text_to_mobject(text)

Convert a text element to a vectorized mobject.

#### WARNING
Not yet implemented.

* **Parameters:**
  **text** (*Text*) – The parsed SVG text.
* **Return type:**
  [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)
