# ShowSubmobjectsOneByOne

Qualified name: `manim.animation.creation.ShowSubmobjectsOneByOne`

### *class* ShowSubmobjectsOneByOne(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`ShowIncreasingSubsets`](manim.animation.creation.ShowIncreasingSubsets.md#manim.animation.creation.ShowIncreasingSubsets)

Show one submobject at a time, removing all previously displayed ones from screen.

### Methods

| `update_submobject_list`   |    |
|----------------------------|----|

### Attributes

| `run_time`   |    |
|--------------|----|
* **Parameters:**
  * **group** (*Iterable* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*)
  * **int_func** (*Callable* *[* *[**np.ndarray* *]* *,* *np.ndarray* *]*)

#### \_original_\_init_\_(group, int_func=<ufunc 'ceil'>, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **group** (*Iterable* *[*[*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *]*)
  * **int_func** (*Callable* *[* *[**ndarray* *]* *,* *ndarray* *]*)
* **Return type:**
  None
