# VDict

Qualified name: `manim.mobject.types.vectorized\_mobject.VDict`

### *class* VDict(mapping_or_iterable={}, show_keys=False, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A VGroup-like class, also offering submobject access by
key, like a python dict

* **Parameters:**
  * **mapping_or_iterable** (*Mapping* *[**Hashable* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*  *|* *Iterable* *[**tuple* *[**Hashable* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *]*) – The parameter specifying the key-value mapping of keys and mobjects.
  * **show_keys** (*bool*) – Whether to also display the key associated with
    the mobject. This might be useful when debugging,
    especially when there are a lot of mobjects in the
    [`VDict`](#manim.mobject.types.vectorized_mobject.VDict). Defaults to False.
  * **kwargs** – Other arguments to be passed to Mobject.

#### show_keys

Whether to also display the key associated with
the mobject. This might be useful when debugging,
especially when there are a lot of mobjects in the
[`VDict`](#manim.mobject.types.vectorized_mobject.VDict). When displayed, the key is towards
the left of the mobject.
Defaults to False.

* **Type:**
  `bool`

#### submob_dict

Is the actual python dictionary that is used to bind
the keys to the mobjects.

* **Type:**
  `dict`

### Examples

### Methods

| [`add`](#manim.mobject.types.vectorized_mobject.VDict.add)                                 | Adds the key-value pairs to the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object.                                                                                                 |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`add_key_value_pair`](#manim.mobject.types.vectorized_mobject.VDict.add_key_value_pair)   | A utility function used by [`add()`](#manim.mobject.types.vectorized_mobject.VDict.add) to add the key-value pair to [`submob_dict`](#manim.mobject.types.vectorized_mobject.VDict.submob_dict). |
| [`get_all_submobjects`](#manim.mobject.types.vectorized_mobject.VDict.get_all_submobjects) | To get all the submobjects associated with a particular [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object                                                                          |
| [`remove`](#manim.mobject.types.vectorized_mobject.VDict.remove)                           | Removes the mobject from the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object having the key key                                                                                  |

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

#### \_original_\_init_\_(mapping_or_iterable={}, show_keys=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mapping_or_iterable** (*Mapping* *[**Hashable* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*  *|* *Iterable* *[**tuple* *[**Hashable* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *]*)
  * **show_keys** (*bool*)
* **Return type:**
  None

#### add(mapping_or_iterable)

Adds the key-value pairs to the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object.

Also, it internally adds the value to the submobjects `list`
of [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject), which is responsible for actual on-screen display.

* **Parameters:**
  **mapping_or_iterable** (*Mapping* *[**Hashable* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*  *|* *Iterable* *[**tuple* *[**Hashable* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *]*) – The parameter specifying the key-value mapping of keys and mobjects.
* **Returns:**
  Returns the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object on which this method was called.
* **Return type:**
  [`VDict`](#manim.mobject.types.vectorized_mobject.VDict)

### Examples

Normal usage:

```default
square_obj = Square()
my_dict.add([("s", square_obj)])
```

#### add_key_value_pair(key, value)

A utility function used by [`add()`](#manim.mobject.types.vectorized_mobject.VDict.add) to add the key-value pair
to [`submob_dict`](#manim.mobject.types.vectorized_mobject.VDict.submob_dict). Not really meant to be used externally.

* **Parameters:**
  * **key** (*Hashable*) – The key of the submobject to be added.
  * **value** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The mobject associated with the key
* **Return type:**
  None
* **Raises:**
  **TypeError** – If the value is not an instance of VMobject

### Examples

Normal usage:

```default
square_obj = Square()
self.add_key_value_pair("s", square_obj)
```

#### get_all_submobjects()

To get all the submobjects associated with a particular [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object

* **Returns:**
  All the submobjects associated with the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object
* **Return type:**
  `dict_values`

### Examples

Normal usage:

```default
for submob in my_dict.get_all_submobjects():
    self.play(Create(submob))
```

#### remove(key)

Removes the mobject from the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object having the key key

Also, it internally removes the mobject from the submobjects `list`
of [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject), (which is responsible for removing it from the screen)

* **Parameters:**
  **key** (*Hashable*) – The key of the submoject to be removed.
* **Returns:**
  Returns the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object on which this method was called.
* **Return type:**
  [`VDict`](#manim.mobject.types.vectorized_mobject.VDict)

### Examples

Normal usage:

```default
my_dict.remove("square")
```
