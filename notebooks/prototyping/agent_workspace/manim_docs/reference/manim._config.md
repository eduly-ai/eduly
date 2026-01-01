# \_config

Set the global config and logger.

### Functions

### tempconfig(temp)

Temporarily modifies the global `config` object using a context manager.

Inside the `with` statement, the modified config will be used.  After
context manager exits, the config will be restored to its original state.

* **Parameters:**
  **temp** ([*ManimConfig*](manim._config.utils.ManimConfig.md#manim._config.utils.ManimConfig) *|* *dict* *[**str* *,* *Any* *]*) – Object whose keys will be used to temporarily update the global
  `config`.
* **Return type:**
  *Generator*[None, None, None]

### Examples

Use `with tempconfig({...})` to temporarily change the default values of
certain config options.

```pycon
>>> config["frame_height"]
8.0
>>> with tempconfig({"frame_height": 100.0}):
...     print(config["frame_height"])
100.0
>>> config["frame_height"]
8.0
```
