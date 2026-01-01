# Section

Qualified name: `manim.scene.section.Section`

### *class* Section(type_, video, name, skip_animations)

Bases: `object`

A [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) can be segmented into multiple Sections.
Refer to [the documentation](../tutorials/output_and_config.md) for more info.
It consists of multiple animations.

* **Parameters:**
  * **type_** (*str*)
  * **video** (*str* *|* *None*)
  * **name** (*str*)
  * **skip_animations** (*bool*)

### type\\_

Can be used by a third party applications to classify different types of sections.

#### video

Path to video file with animations belonging to section relative to sections directory.
If `None`, then the section will not be saved.

#### name

Human readable, non-unique name for this section.

#### skip_animations

Skip rendering the animations in this section when `True`.

#### partial_movie_files

Animations belonging to this section.

#### SEE ALSO
[`DefaultSectionType`](manim.scene.section.DefaultSectionType.md#manim.scene.section.DefaultSectionType), `CairoRenderer.update_skipping_status()`, `OpenGLRenderer.update_skipping_status()`

### Methods

| [`get_clean_partial_movie_files`](#manim.scene.section.Section.get_clean_partial_movie_files)   | Return all partial movie files that are not `None`.          |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [`get_dict`](#manim.scene.section.Section.get_dict)                                             | Get dictionary representation with metadata of output video. |
| [`is_empty`](#manim.scene.section.Section.is_empty)                                             | Check whether this section is empty.                         |

#### get_clean_partial_movie_files()

Return all partial movie files that are not `None`.

* **Return type:**
  list[str]

#### get_dict(sections_dir)

Get dictionary representation with metadata of output video.

The output from this function is used from every section to build the sections index file.
The output video must have been created in the `sections_dir` before executing this method.
This is the main part of the Segmented Video API.

* **Parameters:**
  **sections_dir** (*Path*)
* **Return type:**
  dict[str, *Any*]

#### is_empty()

Check whether this section is empty.

Note that animations represented by `None` are also counted.

* **Return type:**
  bool
