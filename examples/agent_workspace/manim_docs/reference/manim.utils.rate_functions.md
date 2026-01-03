# rate_functions

A selection of rate functions, i.e., *speed curves* for animations.
Please find a standard list at [https://easings.net/](https://easings.net/). Here is a picture
for the non-standard ones

There are primarily 3 kinds of standard easing functions:

1. Ease In - The animation has a smooth start.
2. Ease Out - The animation has a smooth end.
3. Ease In Out - The animation has a smooth start as well as smooth end.

#### NOTE
The standard functions are not exported, so to use them you do something like this:
rate_func=rate_functions.ease_in_sine
On the other hand, the non-standard functions, which are used more commonly, are exported and can be used directly.

### Classes

| [`RateFunction`](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction)   |    |
|--------------------------------------------------------------------------------------------------------|----|

### Functions

### double_smooth(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_back(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_bounce(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_circ(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_cubic(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_elastic(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_expo(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_back(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_bounce(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_circ(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_cubic(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_elastic(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_expo(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_quad(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_quart(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_quint(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_out_sine(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_quad(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_quart(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_quint(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_in_sine(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_back(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_bounce(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_circ(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_cubic(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_elastic(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_expo(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_quad(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_quart(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_quint(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### ease_out_sine(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### exponential_decay(t, half_life=0.1)

* **Parameters:**
  * **t** (*float*)
  * **half_life** (*float*)
* **Return type:**
  float

### linear(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### lingering(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### not_quite_there(func=<function smooth>, proportion=0.7)

* **Parameters:**
  * **func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
  * **proportion** (*float*)
* **Return type:**
  [*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction)

### running_start(t, pull_factor=-0.5)

* **Parameters:**
  * **t** (*float*)
  * **pull_factor** (*float*)
* **Return type:**
  float

### rush_from(t, inflection=10.0)

* **Parameters:**
  * **t** (*float*)
  * **inflection** (*float*)
* **Return type:**
  float

### rush_into(t, inflection=10.0)

* **Parameters:**
  * **t** (*float*)
  * **inflection** (*float*)
* **Return type:**
  float

### slow_into(t)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### smooth(t, inflection=10.0)

* **Parameters:**
  * **t** (*float*)
  * **inflection** (*float*)
* **Return type:**
  float

### smoothererstep(t)

Implementation of the 3rd order SmoothStep sigmoid function.
The 1st, 2nd and 3rd derivatives (speed, acceleration and jerk) are zero at the endpoints.
[https://en.wikipedia.org/wiki/Smoothstep](https://en.wikipedia.org/wiki/Smoothstep)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### smootherstep(t)

Implementation of the 2nd order SmoothStep sigmoid function.
The 1st and 2nd derivatives (speed and acceleration) are zero at the endpoints.
[https://en.wikipedia.org/wiki/Smoothstep](https://en.wikipedia.org/wiki/Smoothstep)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### smoothstep(t)

Implementation of the 1st order SmoothStep sigmoid function.
The 1st derivative (speed) is zero at the endpoints.
[https://en.wikipedia.org/wiki/Smoothstep](https://en.wikipedia.org/wiki/Smoothstep)

* **Parameters:**
  **t** (*float*)
* **Return type:**
  float

### squish_rate_func(func, a=0.4, b=0.6)

* **Parameters:**
  * **func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
  * **a** (*float*)
  * **b** (*float*)
* **Return type:**
  [*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction)

### there_and_back(t, inflection=10.0)

* **Parameters:**
  * **t** (*float*)
  * **inflection** (*float*)
* **Return type:**
  float

### there_and_back_with_pause(t, pause_ratio=0.3333333333333333)

* **Parameters:**
  * **t** (*float*)
  * **pause_ratio** (*float*)
* **Return type:**
  float

### unit_interval(function)

* **Parameters:**
  **function** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
* **Return type:**
  [*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction)

### wiggle(t, wiggles=2)

* **Parameters:**
  * **t** (*float*)
  * **wiggles** (*float*)
* **Return type:**
  float

### zero(function)

* **Parameters:**
  **function** ([*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction))
* **Return type:**
  [*RateFunction*](manim.utils.rate_functions.RateFunction.md#manim.utils.rate_functions.RateFunction)
