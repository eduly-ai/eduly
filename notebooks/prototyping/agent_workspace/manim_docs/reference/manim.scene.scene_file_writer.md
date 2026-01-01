# scene_file_writer

The interface between scenes and ffmpeg.

### Classes

| [`SceneFileWriter`](manim.scene.scene_file_writer.SceneFileWriter.md#manim.scene.scene_file_writer.SceneFileWriter)   | SceneFileWriter is the object that actually writes the animations played, into video files, using FFMPEG.   |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|

### Functions

### convert_audio(input_path, output_path, codec_name)

* **Parameters:**
  * **input_path** (*Path*)
  * **output_path** (*Path* *|*  *\_TemporaryFileWrapper* *[**bytes* *]*)
  * **codec_name** (*str*)
* **Return type:**
  None

### to_av_frame_rate(fps)

* **Parameters:**
  **fps** (*float*)
* **Return type:**
  *Fraction*
