# DummySceneFileWriter

Qualified name: `manim.utils.testing.\_test\_class\_makers.DummySceneFileWriter`

### *class* DummySceneFileWriter(renderer, scene_name, \*\*kwargs)

Bases: [`SceneFileWriter`](manim.scene.scene_file_writer.SceneFileWriter.md#manim.scene.scene_file_writer.SceneFileWriter)

Delegate of SceneFileWriter used to test the frames.

### Methods

| [`add_partial_movie_file`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.add_partial_movie_file)       | Adds a new partial movie file path to `scene.partial_movie_files` and current section from a hash.                                 |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [`begin_animation`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.begin_animation)                     | Used internally by manim to stream the animation to FFMPEG for displaying or writing to a file.                                    |
| [`clean_cache`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.clean_cache)                             | Will clean the cache by removing the oldest partial_movie_files.                                                                   |
| [`combine_to_movie`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_movie)                   | Used internally by Manim to combine the separate partial movie files that make up a Scene into a single video file for that Scene. |
| [`combine_to_section_videos`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_section_videos) | Concatenate partial movie files for each section.                                                                                  |
| [`end_animation`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.end_animation)                         | Internally used by Manim to stop streaming to FFMPEG gracefully.                                                                   |
| [`init_output_directories`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.init_output_directories)     | Initialise output directories.                                                                                                     |
| [`write_frame`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.write_frame)                             | Used internally by Manim to write a frame to the FFMPEG input buffer.                                                              |

### Attributes

| `force_output_as_scene_name`   |    |
|--------------------------------|----|
* **Parameters:**
  * **renderer** (*CairoRenderer* *|* *OpenGLRenderer*)
  * **scene_name** (*str*)
  * **kwargs** (*Any*)

#### add_partial_movie_file(hash_animation)

Adds a new partial movie file path to `scene.partial_movie_files`
and current section from a hash.

This method will compute the path from the hash. In addition to that it
adds the new animation to the current section.

* **Parameters:**
  **hash_animation** (*str* *|* *None*) – Hash of the animation.
* **Return type:**
  None

#### begin_animation(allow_write=True, file_path=None)

Used internally by manim to stream the animation to FFMPEG for
displaying or writing to a file.

* **Parameters:**
  * **allow_write** (*bool*) – Whether or not to write to a video file.
  * **file_path** ([*StrPath*](manim.typing.md#manim.typing.StrPath) *|* *None*)
* **Return type:**
  Any

#### clean_cache()

Will clean the cache by removing the oldest partial_movie_files.

* **Return type:**
  None

#### combine_to_movie()

Used internally by Manim to combine the separate
partial movie files that make up a Scene into a single
video file for that Scene.

* **Return type:**
  None

#### combine_to_section_videos()

Concatenate partial movie files for each section.

* **Return type:**
  None

#### end_animation(allow_write=False)

Internally used by Manim to stop streaming to FFMPEG gracefully.

* **Parameters:**
  **allow_write** (*bool*) – Whether or not to write to a video file.
* **Return type:**
  None

#### init_output_directories(scene_name)

Initialise output directories.

### Notes

The directories are read from `config`, for example
`config['media_dir']`.  If the target directories don’t already
exist, they will be created.

* **Parameters:**
  **scene_name** (*str*)
* **Return type:**
  None

#### write_frame(frame_or_renderer, num_frames=1)

Used internally by Manim to write a frame to the FFMPEG input buffer.

* **Parameters:**
  * **frame_or_renderer** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray) *|* *OpenGLRenderer*) – Pixel array of the frame.
  * **num_frames** (*int*) – The number of times to write frame.
* **Return type:**
  None
