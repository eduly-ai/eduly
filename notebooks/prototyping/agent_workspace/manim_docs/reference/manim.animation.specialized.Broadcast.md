# Broadcast

Qualified name: `manim.animation.specialized.Broadcast`

### *class* Broadcast(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`LaggedStart`](manim.animation.composition.LaggedStart.md#manim.animation.composition.LaggedStart)

Broadcast a mobject starting from an `initial_width`, up to the actual size of the mobject.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobject to be broadcast.
  * **focal_point** (*Sequence* *[**float* *]*) – The center of the broadcast, by default ORIGIN.
  * **n_mobs** (*int*) – The number of mobjects that emerge from the focal point, by default 5.
  * **initial_opacity** (*float*) – The starting stroke opacity of the mobjects emitted from the broadcast, by default 1.
  * **final_opacity** (*float*) – The final stroke opacity of the mobjects emitted from the broadcast, by default 0.
  * **initial_width** (*float*) – The initial width of the mobjects, by default 0.0.
  * **remover** (*bool*) – Whether the mobjects should be removed from the scene after the animation, by default True.
  * **lag_ratio** (*float*) – The time between each iteration of the mobject, by default 0.2.
  * **run_time** (*float*) – The total duration of the animation, by default 3.
  * **kwargs** (*Any*) – Additional arguments to be passed to [`LaggedStart`](manim.animation.composition.LaggedStart.md#manim.animation.composition.LaggedStart).

### Examples

### Methods

### Attributes

| `run_time`   |    |
|--------------|----|

#### \_original_\_init_\_(mobject, focal_point=array([0., 0., 0.]), n_mobs=5, initial_opacity=1, final_opacity=0, initial_width=0.0, remover=True, lag_ratio=0.2, run_time=3, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **focal_point** (*Sequence* *[**float* *]*)
  * **n_mobs** (*int*)
  * **initial_opacity** (*float*)
  * **final_opacity** (*float*)
  * **initial_width** (*float*)
  * **remover** (*bool*)
  * **lag_ratio** (*float*)
  * **run_time** (*float*)
  * **kwargs** (*Any*)
