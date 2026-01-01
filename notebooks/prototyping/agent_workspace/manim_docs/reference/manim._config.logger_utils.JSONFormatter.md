# JSONFormatter

Qualified name: `manim.\_config.logger\_utils.JSONFormatter`

### *class* JSONFormatter(fmt=None, datefmt=None, style='%', validate=True, \*, defaults=None)

Bases: `Formatter`

A formatter that outputs logs in a custom JSON format.

This class is used internally for testing purposes.

Initialize the formatter with specified format strings.

Initialize the formatter either with the specified format string, or a
default as described above. Allow for specialized date formatting with
the optional datefmt argument. If datefmt is omitted, you get an
ISO8601-like (or RFC 3339-like) format.

Use a style parameter of ‘%’, ‘{’ or ‘$’ to specify that you want to
use one of %-formatting, `str.format()` (`{}`) formatting or
`string.Template` formatting in your format string.

#### Versionchanged
Changed in version 3.2: Added the `style` parameter.

### Methods

| [`format`](#manim._config.logger_utils.JSONFormatter.format)   | Format the record in a custom JSON format.   |
|----------------------------------------------------------------|----------------------------------------------|

### Attributes

| `default_msec_format`   |    |
|-------------------------|----|
| `default_time_format`   |    |

#### format(record)

Format the record in a custom JSON format.

* **Parameters:**
  **record** (*LogRecord*)
* **Return type:**
  str
