# RerunSceneHandler

Qualified name: `manim.scene.scene.RerunSceneHandler`

### *class* RerunSceneHandler(queue)

Bases: `FileSystemEventHandler`

A class to handle rerunning a Scene after the input file is modified.

### Methods

| [`on_modified`](#manim.scene.scene.RerunSceneHandler.on_modified)   | Called when a file or directory is modified.   |
|---------------------------------------------------------------------|------------------------------------------------|
* **Parameters:**
  **queue** (*Queue* *[*[*SceneInteractAction*](manim.scene.scene.md#manim.scene.scene.SceneInteractAction) *]*)

#### on_modified(event)

Called when a file or directory is modified.

* **Parameters:**
  **event** (`DirModifiedEvent` or `FileModifiedEvent`) – Event representing file/directory modification.
* **Return type:**
  None
