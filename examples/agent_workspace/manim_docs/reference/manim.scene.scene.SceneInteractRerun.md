# SceneInteractRerun

Qualified name: `manim.scene.scene.SceneInteractRerun`

### *class* SceneInteractRerun(sender, \*\*kwargs)

Bases: `object`

Object which, when encountered in `Scene.interact()`, triggers
the rerun of the scene. This object can be queued in `Scene.queue`
for later use in `Scene.interact()`.

* **Parameters:**
  * **sender** (*str*)
  * **kwargs** (*Any*)

#### sender

The name of the entity which issued the rerun of the scene, such as
`"gui"`, `"keyboard"`, `"play"` or `"file"`.

* **Type:**
  str

#### kwargs

Additional keyword arguments when rerunning the scene. Currently,
only `"from_animation_number"` is being used, which determines the
animation from which to start rerunning the scene.

* **Type:**
  dict[str, Any]

### Methods

### Attributes

| [`sender`](#manim.scene.scene.SceneInteractRerun.sender)   |    |
|------------------------------------------------------------|----|
| [`kwargs`](#manim.scene.scene.SceneInteractRerun.kwargs)   |    |
