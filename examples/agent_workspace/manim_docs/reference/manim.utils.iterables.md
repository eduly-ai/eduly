# iterables

Operations on iterables.

### TypeVar’s

### *class* T

```default
TypeVar('T')
```

### *class* U

```default
TypeVar('U')
```

### *class* F

```default
TypeVar('F', np.float64, np.int_)
```

### *class* H

```default
TypeVar('H', bound=Hashable)
```

### Functions

### adjacent_n_tuples(objects, n)

Returns the Sequence objects cyclically split into n length tuples.

#### SEE ALSO
[`adjacent_pairs`](#manim.utils.iterables.adjacent_pairs)
: alias with n=2

### Examples

```pycon
>>> list(adjacent_n_tuples([1, 2, 3, 4], 2))
[(1, 2), (2, 3), (3, 4), (4, 1)]
>>> list(adjacent_n_tuples([1, 2, 3, 4], 3))
[(1, 2, 3), (2, 3, 4), (3, 4, 1), (4, 1, 2)]
```

* **Parameters:**
  * **objects** (*Sequence* *[*[*T*](#manim.utils.iterables.T) *]*)
  * **n** (*int*)
* **Return type:**
  zip[tuple[[T](#manim.utils.iterables.T), …]]

### adjacent_pairs(objects)

Alias for `adjacent_n_tuples(objects, 2)`.

#### SEE ALSO
[`adjacent_n_tuples`](#manim.utils.iterables.adjacent_n_tuples)

### Examples

```pycon
>>> list(adjacent_pairs([1, 2, 3, 4]))
[(1, 2), (2, 3), (3, 4), (4, 1)]
```

* **Parameters:**
  **objects** (*Sequence* *[*[*T*](#manim.utils.iterables.T) *]*)
* **Return type:**
  zip[tuple[[T](#manim.utils.iterables.T), …]]

### all_elements_are_instances(iterable, Class)

Returns `True` if all elements of iterable are instances of Class.
False otherwise.

* **Parameters:**
  * **iterable** (*Iterable* *[**object* *]*)
  * **Class** (*type* *[**object* *]*)
* **Return type:**
  bool

### batch_by_property(items, property_func)

Takes in a Sequence, and returns a list of tuples, (batch, prop)
such that all items in a batch have the same output when
put into the Callable property_func, and such that chaining all these
batches together would give the original Sequence (i.e. order is
preserved).

### Examples

```pycon
>>> batch_by_property([(1, 2), (3, 4), (5, 6, 7), (8, 9)], len)
[([(1, 2), (3, 4)], 2), ([(5, 6, 7)], 3), ([(8, 9)], 2)]
```

* **Parameters:**
  * **items** (*Iterable* *[*[*T*](#manim.utils.iterables.T) *]*)
  * **property_func** (*Callable* *[* *[*[*T*](#manim.utils.iterables.T) *]* *,* [*U*](#manim.utils.iterables.U) *]*)
* **Return type:**
  list[tuple[list[[*T*](#manim.utils.iterables.T)], [*U*](#manim.utils.iterables.U) | None]]

### concatenate_lists(\*list_of_lists)

Combines the Iterables provided as arguments into one list.

### Examples

```pycon
>>> concatenate_lists([1, 2], [3, 4], [5])
[1, 2, 3, 4, 5]
```

* **Parameters:**
  **list_of_lists** (*Iterable* *[*[*T*](#manim.utils.iterables.T) *]*)
* **Return type:**
  list[[*T*](#manim.utils.iterables.T)]

### hash_obj(obj)

Determines a hash, even of potentially mutable objects.

* **Parameters:**
  **obj** (*object*)
* **Return type:**
  int

### list_difference_update(l1, l2)

Returns a list containing all the elements of l1 not in l2.

### Examples

```pycon
>>> list_difference_update([1, 2, 3, 4], [2, 4])
[1, 3]
```

* **Parameters:**
  * **l1** (*Iterable* *[*[*T*](#manim.utils.iterables.T) *]*)
  * **l2** (*Iterable* *[*[*T*](#manim.utils.iterables.T) *]*)
* **Return type:**
  list[[*T*](#manim.utils.iterables.T)]

### list_update(l1, l2)

Used instead of `set.update()` to maintain order,
: making sure duplicates are removed from l1, not l2.
  Removes overlap of l1 and l2 and then concatenates l2 unchanged.

### Examples

```pycon
>>> list_update([1, 2, 3], [2, 4, 4])
[1, 3, 2, 4, 4]
```

* **Parameters:**
  * **l1** (*Iterable* *[*[*T*](#manim.utils.iterables.T) *]*)
  * **l2** (*Iterable* *[*[*T*](#manim.utils.iterables.T) *]*)
* **Return type:**
  list[[*T*](#manim.utils.iterables.T)]

### listify(obj: str) → list[str]

### listify(obj: Iterable[[T](#manim.utils.iterables.T)]) → list[[T](#manim.utils.iterables.T)]

### listify(obj: [T](#manim.utils.iterables.T)) → list[[T](#manim.utils.iterables.T)]

Converts obj to a list intelligently.

### Examples

```pycon
>>> listify("str")
['str']
>>> listify((1, 2))
[1, 2]
>>> listify(len)
[<built-in function len>]
```

### make_even(iterable_1, iterable_2)

Extends the shorter of the two iterables with duplicate values until its
: length is equal to the longer iterable (favours earlier elements).

#### SEE ALSO
[`make_even_by_cycling`](#manim.utils.iterables.make_even_by_cycling)
: cycles elements instead of favouring earlier ones

### Examples

```pycon
>>> make_even([1, 2], [3, 4, 5, 6])
([1, 1, 2, 2], [3, 4, 5, 6])

>>> make_even([1, 2], [3, 4, 5, 6, 7])
([1, 1, 1, 2, 2], [3, 4, 5, 6, 7])
```

* **Parameters:**
  * **iterable_1** (*Iterable* *[*[*T*](#manim.utils.iterables.T) *]*)
  * **iterable_2** (*Iterable* *[*[*U*](#manim.utils.iterables.U) *]*)
* **Return type:**
  tuple[list[[*T*](#manim.utils.iterables.T)], list[[*U*](#manim.utils.iterables.U)]]

### make_even_by_cycling(iterable_1, iterable_2)

Extends the shorter of the two iterables with duplicate values until its
: length is equal to the longer iterable (cycles over shorter iterable).

#### SEE ALSO
[`make_even`](#manim.utils.iterables.make_even)
: favours earlier elements instead of cycling them

### Examples

```pycon
>>> make_even_by_cycling([1, 2], [3, 4, 5, 6])
([1, 2, 1, 2], [3, 4, 5, 6])

>>> make_even_by_cycling([1, 2], [3, 4, 5, 6, 7])
([1, 2, 1, 2, 1], [3, 4, 5, 6, 7])
```

* **Parameters:**
  * **iterable_1** (*Collection* *[*[*T*](#manim.utils.iterables.T) *]*)
  * **iterable_2** (*Collection* *[*[*U*](#manim.utils.iterables.U) *]*)
* **Return type:**
  tuple[list[[*T*](#manim.utils.iterables.T)], list[[*U*](#manim.utils.iterables.U)]]

### remove_list_redundancies(lst)

Used instead of `list(set(l))` to maintain order.
Keeps the last occurrence of each element.

* **Parameters:**
  **lst** (*Reversible* *[*[*H*](#manim.utils.iterables.H) *]*)
* **Return type:**
  list[[*H*](#manim.utils.iterables.H)]

### remove_nones(sequence)

Removes elements where bool(x) evaluates to False.

### Examples

```pycon
>>> remove_nones(["m", "", "l", 0, 42, False, True])
['m', 'l', 42, True]
```

* **Parameters:**
  **sequence** (*Iterable* *[*[*T*](#manim.utils.iterables.T) *|* *None* *]*)
* **Return type:**
  list[[*T*](#manim.utils.iterables.T)]

### resize_array(nparray, length)

Extends/truncates nparray so that `len(result) == length`.
: The elements of nparray are cycled to achieve the desired length.

#### SEE ALSO
[`resize_preserving_order`](#manim.utils.iterables.resize_preserving_order)
: favours earlier elements instead of cycling them

[`make_even_by_cycling`](#manim.utils.iterables.make_even_by_cycling)
: similar cycling behaviour for balancing 2 iterables

### Examples

```pycon
>>> points = np.array([[1, 2], [3, 4]])
>>> resize_array(points, 1)
array([[1, 2]])
>>> resize_array(points, 3)
array([[1, 2],
       [3, 4],
       [1, 2]])
>>> resize_array(points, 2)
array([[1, 2],
       [3, 4]])
```

* **Parameters:**
  * **nparray** (*npt.NDArray* *[*[*F*](#manim.utils.iterables.F) *]*)
  * **length** (*int*)
* **Return type:**
  npt.NDArray[[F](#manim.utils.iterables.F)]

### resize_preserving_order(nparray, length)

Extends/truncates nparray so that `len(result) == length`.
: The elements of nparray are duplicated to achieve the desired length
  (favours earlier elements).
  <br/>
  Constructs a zeroes array of length if nparray is empty.

#### SEE ALSO
[`resize_array`](#manim.utils.iterables.resize_array)
: cycles elements instead of favouring earlier ones

[`make_even`](#manim.utils.iterables.make_even)
: similar earlier-favouring behaviour for balancing 2 iterables

### Examples

```pycon
>>> resize_preserving_order(np.array([]), 5)
array([0., 0., 0., 0., 0.])

>>> nparray = np.array([[1, 2], [3, 4]])
>>> resize_preserving_order(nparray, 1)
array([[1, 2]])

>>> resize_preserving_order(nparray, 3)
array([[1, 2],
       [1, 2],
       [3, 4]])
```

* **Parameters:**
  * **nparray** (*npt.NDArray* *[**np.float64* *]*)
  * **length** (*int*)
* **Return type:**
  npt.NDArray[np.float64]

### resize_with_interpolation(nparray, length)

Extends/truncates nparray so that `len(result) == length`.
: New elements are interpolated to achieve the desired length.
  <br/>
  Note that if nparray’s length changes, its dtype may too
  (e.g. int -> float: see Examples)

#### SEE ALSO
[`resize_array`](#manim.utils.iterables.resize_array)
: cycles elements instead of interpolating

[`resize_preserving_order`](#manim.utils.iterables.resize_preserving_order)
: favours earlier elements instead of interpolating

### Examples

```pycon
>>> nparray = np.array([[1, 2], [3, 4]])
>>> resize_with_interpolation(nparray, 1)
array([[1., 2.]])
>>> resize_with_interpolation(nparray, 4)
array([[1.        , 2.        ],
       [1.66666667, 2.66666667],
       [2.33333333, 3.33333333],
       [3.        , 4.        ]])
>>> nparray = np.array([[[1, 2], [3, 4]]])
>>> nparray = np.array([[1, 2], [3, 4], [5, 6]])
>>> resize_with_interpolation(nparray, 4)
array([[1.        , 2.        ],
       [2.33333333, 3.33333333],
       [3.66666667, 4.66666667],
       [5.        , 6.        ]])
>>> nparray = np.array([[1, 2], [3, 4], [1, 2]])
>>> resize_with_interpolation(nparray, 4)
array([[1.        , 2.        ],
       [2.33333333, 3.33333333],
       [2.33333333, 3.33333333],
       [1.        , 2.        ]])
```

* **Parameters:**
  * **nparray** (*npt.NDArray* *[*[*F*](#manim.utils.iterables.F) *]*)
  * **length** (*int*)
* **Return type:**
  npt.NDArray[[F](#manim.utils.iterables.F)]

### stretch_array_to_length(nparray, length)

* **Parameters:**
  * **nparray** (*npt.NDArray* *[*[*F*](#manim.utils.iterables.F) *]*)
  * **length** (*int*)
* **Return type:**
  npt.NDArray[[F](#manim.utils.iterables.F)]

### tuplify(obj: str) → tuple[str]

### tuplify(obj: Iterable[[T](#manim.utils.iterables.T)]) → tuple[[T](#manim.utils.iterables.T)]

### tuplify(obj: [T](#manim.utils.iterables.T)) → tuple[[T](#manim.utils.iterables.T)]

Converts obj to a tuple intelligently.

### Examples

```pycon
>>> tuplify("str")
('str',)
>>> tuplify([1, 2])
(1, 2)
>>> tuplify(len)
(<built-in function len>,)
```

### uniq_chain(\*args)

Returns a generator that yields all unique elements of the Iterables
: provided via args in the order provided.

### Examples

```pycon
>>> gen = uniq_chain([1, 2], [2, 3], [1, 4, 4])
>>> from collections.abc import Generator
>>> isinstance(gen, Generator)
True
>>> tuple(gen)
(1, 2, 3, 4)
```

* **Parameters:**
  **args** (*Iterable* *[*[*T*](#manim.utils.iterables.T) *]*)
* **Return type:**
  *Generator*[[*T*](#manim.utils.iterables.T), None, None]
