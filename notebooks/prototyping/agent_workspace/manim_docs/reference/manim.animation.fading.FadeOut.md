# FadeOut

Qualified name: `manim.animation.fading.FadeOut`

### *class* FadeOut(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: `_Fade`

Fade out [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) s.

* **Parameters:**
  * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The mobjects to be faded out.
  * **shift** – The vector by which the mobject shifts while being faded out.
  * **target_position** – The position to which the mobject moves while being faded out. In case another
    mobject is given as target position, its center is used.
  * **scale** – The factor by which the mobject is scaled while being faded out.
  * **kwargs** (*Any*)

### Examples

### Methods

| [`clean_up_from_scene`](#manim.animation.fading.FadeOut.clean_up_from_scene)   | Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation.   |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `create_target`                                                                |                                                                                                             |

### Attributes

| `path_arc`   |    |
|--------------|----|
| `path_func`  |    |
| `run_time`   |    |

#### \_original_\_init_\_(\*mobjects, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **kwargs** (*Any*)
* **Return type:**
  None

#### clean_up_from_scene(scene)

Clean up the [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene) after finishing the animation.

This includes to [`remove()`](manim.scene.scene.Scene.md#manim.scene.scene.Scene.remove) the Animation’s
[`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) if the animation is a remover.

* **Parameters:**
  **scene** ([*Scene*](manim.scene.scene.Scene.md#manim.scene.scene.Scene)) – The scene the animation should be cleaned up from.
* **Return type:**
  None
