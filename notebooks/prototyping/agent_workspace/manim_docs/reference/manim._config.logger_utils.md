# logger_utils

Utilities to create and set the logger.

Manim’s logger can be accessed as `manim.logger`, or as
`logging.getLogger("manim")`, once the library has been imported.  Manim also
exports a second object, `console`, which should be used to print on screen
messages that need not be logged.

Both `logger` and `console` use the `rich` library to produce rich text
format.

### Classes

| [`JSONFormatter`](manim._config.logger_utils.JSONFormatter.md#manim._config.logger_utils.JSONFormatter)   | A formatter that outputs logs in a custom JSON format.   |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------|

### Functions

### make_logger(parser, verbosity)

Make the manim logger and console.

* **Parameters:**
  * **parser** (*SectionProxy*) – A parser containing any .cfg files in use.
  * **verbosity** (*str*) – The verbosity level of the logger.
* **Returns:**
  The manim logger and consoles. The first console outputs
  to stdout, the second to stderr. All use the theme returned by
  [`parse_theme()`](#manim._config.logger_utils.parse_theme).
* **Return type:**
  `logging.Logger`, `rich.Console`, `rich.Console`

#### SEE ALSO
[`make_config_parser()`](manim._config.utils.md#manim._config.utils.make_config_parser), [`parse_theme()`](#manim._config.logger_utils.parse_theme)

### Notes

The `parser` is assumed to contain only the options related to
configuring the logger at the top level.

### parse_theme(parser)

Configure the rich style of logger and console output.

* **Parameters:**
  **parser** (*SectionProxy*) – A parser containing any .cfg files in use.
* **Returns:**
  The rich theme to be used by the manim logger.
* **Return type:**
  `rich.Theme`

#### SEE ALSO
[`make_logger()`](#manim._config.logger_utils.make_logger)

### set_file_logger(scene_name, module_name, log_dir)

Add a file handler to manim logger.

The path to the file is built using `config.log_dir`.

* **Parameters:**
  * **scene_name** (*str*) – The name of the scene, used in the name of the log file.
  * **module_name** (*str*) – The name of the module, used in the name of the log file.
  * **log_dir** (*Path*) – Path to the folder where log files are stored.
* **Return type:**
  None
