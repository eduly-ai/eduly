# commands

### Classes

| [`VideoMetadata`](manim.utils.commands.VideoMetadata.md#manim.utils.commands.VideoMetadata)   |    |
|-----------------------------------------------------------------------------------------------|----|

### Functions

### capture(command, cwd=None, command_input=None)

* **Parameters:**
  * **command** (*str*)
  * **cwd** ([*StrOrBytesPath*](manim.typing.md#manim.typing.StrOrBytesPath) *|* *None*)
  * **command_input** (*str* *|* *None*)
* **Return type:**
  tuple[str, str, int]

### get_dir_layout(dirpath)

Get list of paths relative to dirpath of all files in dir and subdirs recursively.

* **Parameters:**
  **dirpath** (*Path*)
* **Return type:**
  *Generator*[str, None, None]

### get_video_metadata(path_to_video)

* **Parameters:**
  **path_to_video** (*str* *|* *PathLike*)
* **Return type:**
  [*VideoMetadata*](manim.utils.commands.VideoMetadata.md#manim.utils.commands.VideoMetadata)
