# utils

Utilities to create and set the config.

The main class exported by this module is [`ManimConfig`](manim._config.utils.ManimConfig.md#manim._config.utils.ManimConfig).  This class
contains all configuration options, including frame geometry (e.g. frame
height/width, frame rate), output (e.g. directories, logging), styling
(e.g. background color, transparency), and general behavior (e.g. writing a
movie vs writing a single frame).

See [Configuration](../guides/configuration.md) for an introduction to Manim’s configuration system.

### Classes

| [`ManimConfig`](manim._config.utils.ManimConfig.md#manim._config.utils.ManimConfig)   | Dict-like class storing all config options.   |
|---------------------------------------------------------------------------------------|-----------------------------------------------|
| [`ManimFrame`](manim._config.utils.ManimFrame.md#manim._config.utils.ManimFrame)      |                                               |

### Functions

### config_file_paths()

The paths where `.cfg` files will be searched for.

When manim is first imported, it processes any `.cfg` files it finds.  This
function returns the locations in which these files are searched for.  In
ascending order of precedence, these are: the library-wide config file, the
user-wide config file, and the folder-wide config file.

The library-wide config file determines manim’s default behavior.  The
user-wide config file is stored in the user’s home folder, and determines
the behavior of manim whenever the user invokes it from anywhere in the
system.  The folder-wide config file only affects scenes that are in the
same folder.  The latter two files are optional.

These files, if they exist, are meant to loaded into a single
`configparser.ConfigParser` object, and then processed by
[`ManimConfig`](manim._config.utils.ManimConfig.md#manim._config.utils.ManimConfig).

* **Returns:**
  List of paths which may contain `.cfg` files, in ascending order of
  precedence.
* **Return type:**
  List[`Path`]

#### SEE ALSO
[`make_config_parser()`](#manim._config.utils.make_config_parser), [`ManimConfig.digest_file()`](manim._config.utils.ManimConfig.md#manim._config.utils.ManimConfig.digest_file), [`ManimConfig.digest_parser()`](manim._config.utils.ManimConfig.md#manim._config.utils.ManimConfig.digest_parser)

### Notes

The location of the user-wide config file is OS-specific.

### make_config_parser(custom_file=None)

Make a `ConfigParser` object and load any `.cfg` files.

The user-wide file, if it exists, overrides the library-wide file.  The
folder-wide file, if it exists, overrides the other two.

The folder-wide file can be ignored by passing `custom_file`.  However,
the user-wide and library-wide config files cannot be ignored.

* **Parameters:**
  **custom_file** ([*StrPath*](manim.typing.md#manim.typing.StrPath) *|* *None*) – Path to a custom config file.  If used, the folder-wide file in the
  relevant directory will be ignored, if it exists.  If None, the
  folder-wide file will be used, if it exists.
* **Returns:**
  A parser containing the config options found in the .cfg files that
  were found.  It is guaranteed to contain at least the config options
  found in the library-wide file.
* **Return type:**
  `ConfigParser`

#### SEE ALSO
[`config_file_paths()`](#manim._config.utils.config_file_paths)
