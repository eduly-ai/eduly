# simple_functions

A collection of simple functions.

### TypeVar’s

### *class* ComparableT

```default
TypeVar('ComparableT', bound=Comparable)
```

### Classes

| [`Comparable`](manim.utils.simple_functions.Comparable.md#manim.utils.simple_functions.Comparable)   |    |
|------------------------------------------------------------------------------------------------------|----|

### Functions

### binary_search(function, target, lower_bound, upper_bound, tolerance=0.0001)

Searches for a value in a range by repeatedly dividing the range in half.

To be more precise, performs numerical binary search to determine the
input to `function`, between the bounds given, that outputs `target`
to within `tolerance` (default of 0.0001).
Returns `None` if no input can be found within the bounds.

### Examples

Consider the polynomial $x^2 + 3x + 1$ where we search for
a target value of $11$. An exact solution is $x = 2$.

```default
>>> solution = binary_search(lambda x: x**2 + 3*x + 1, 11, 0, 5)
>>> bool(abs(solution - 2) < 1e-4)
True
>>> solution = binary_search(lambda x: x**2 + 3*x + 1, 11, 0, 5, tolerance=0.01)
>>> bool(abs(solution - 2) < 0.01)
True
```

Searching in the interval $[0, 5]$ for a target value of $71$
does not yield a solution:

```default
>>> binary_search(lambda x: x**2 + 3*x + 1, 71, 0, 5) is None
True
```

* **Parameters:**
  * **function** (*Callable* *[* *[**float* *]* *,* *float* *]*)
  * **target** (*float*)
  * **lower_bound** (*float*)
  * **upper_bound** (*float*)
  * **tolerance** (*float*)
* **Return type:**
  float | None

### choose(n, k)

The binomial coefficient n choose k.

$\binom{n}{k}$ describes the number of possible choices of
$k$ elements from a set of $n$ elements.

### References

- [https://en.wikipedia.org/wiki/Combination](https://en.wikipedia.org/wiki/Combination)
- [https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.comb.html](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.comb.html)

* **Parameters:**
  * **n** (*int*)
  * **k** (*int*)
* **Return type:**
  int

### clip(a, min_a, max_a)

Clips `a` to the interval [`min_a`, `max_a`].

Accepts any comparable objects (i.e. those that support <, >).
Returns `a` if it is between `min_a` and `max_a`.
Otherwise, whichever of `min_a` and `max_a` is closest.

### Examples

```default
>>> clip(15, 11, 20)
15
>>> clip('a', 'h', 'k')
'h'
```

* **Parameters:**
  * **a** ([*ComparableT*](#manim.utils.simple_functions.ComparableT))
  * **min_a** ([*ComparableT*](#manim.utils.simple_functions.ComparableT))
  * **max_a** ([*ComparableT*](#manim.utils.simple_functions.ComparableT))
* **Return type:**
  [*ComparableT*](#manim.utils.simple_functions.ComparableT)

### sigmoid(x)

Returns the output of the logistic function.

The logistic function, a common example of a sigmoid function, is defined
as $\frac{1}{1 + e^{-x}}$.

### References

- [https://en.wikipedia.org/wiki/Sigmoid_function](https://en.wikipedia.org/wiki/Sigmoid_function)
- [https://en.wikipedia.org/wiki/Logistic_function](https://en.wikipedia.org/wiki/Logistic_function)

* **Parameters:**
  **x** (*float*)
* **Return type:**
  float
