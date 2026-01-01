# SceneFileWriter

Qualified name: `manim.scene.scene\_file\_writer.SceneFileWriter`

### *class* SceneFileWriter(renderer, scene_name, \*\*kwargs)

Bases: `object`

SceneFileWriter is the object that actually writes the animations
played, into video files, using FFMPEG.
This is mostly for Manim’s internal use. You will rarely, if ever,
have to use the methods for this class, unless tinkering with the very
fabric of Manim’s reality.

* **Parameters:**
  * **renderer** (*CairoRenderer* *|* *OpenGLRenderer*)
  * **scene_name** (*str*)
  * **kwargs** (*Any*)

#### sections

used to segment scene

* **Type:**
  list of [`Section`](manim.scene.section.Section.md#manim.scene.section.Section)

#### sections_output_dir

where are section videos stored

* **Type:**
  `pathlib.Path`

#### output_name

name of movie without extension and basis for section video names

* **Type:**
  str

Some useful attributes are:
: “write_to_movie” (bool=False)
  : Whether or not to write the animations into a video file.
  <br/>
  “movie_file_extension” (str=”.mp4”)
  : The file-type extension of the outputted video.
  <br/>
  “partial_movie_files”
  : List of all the partial-movie files.

### Methods

| [`add_audio_segment`](#manim.scene.scene_file_writer.SceneFileWriter.add_audio_segment)                   | This method adds an audio segment from an AudioSegment type object and suitable parameters.                                        |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [`add_partial_movie_file`](#manim.scene.scene_file_writer.SceneFileWriter.add_partial_movie_file)         | Adds a new partial movie file path to `scene.partial_movie_files` and current section from a hash.                                 |
| [`add_sound`](#manim.scene.scene_file_writer.SceneFileWriter.add_sound)                                   | This method adds an audio segment from a sound file.                                                                               |
| [`begin_animation`](#manim.scene.scene_file_writer.SceneFileWriter.begin_animation)                       | Used internally by manim to stream the animation to FFMPEG for displaying or writing to a file.                                    |
| [`clean_cache`](#manim.scene.scene_file_writer.SceneFileWriter.clean_cache)                               | Will clean the cache by removing the oldest partial_movie_files.                                                                   |
| [`close_partial_movie_stream`](#manim.scene.scene_file_writer.SceneFileWriter.close_partial_movie_stream) | Close the currently opened video container.                                                                                        |
| `combine_files`                                                                                           |                                                                                                                                    |
| [`combine_to_movie`](#manim.scene.scene_file_writer.SceneFileWriter.combine_to_movie)                     | Used internally by Manim to combine the separate partial movie files that make up a Scene into a single video file for that Scene. |
| [`combine_to_section_videos`](#manim.scene.scene_file_writer.SceneFileWriter.combine_to_section_videos)   | Concatenate partial movie files for each section.                                                                                  |
| [`create_audio_segment`](#manim.scene.scene_file_writer.SceneFileWriter.create_audio_segment)             | Creates an empty, silent, Audio Segment.                                                                                           |
| [`encode_and_write_frame`](#manim.scene.scene_file_writer.SceneFileWriter.encode_and_write_frame)         | For internal use only: takes a given frame in `np.ndarray` format and writes it to the stream                                      |
| [`end_animation`](#manim.scene.scene_file_writer.SceneFileWriter.end_animation)                           | Internally used by Manim to stop streaming to FFMPEG gracefully.                                                                   |
| [`finish`](#manim.scene.scene_file_writer.SceneFileWriter.finish)                                         | Finishes writing to the FFMPEG buffer or writing images to output directory.                                                       |
| [`finish_last_section`](#manim.scene.scene_file_writer.SceneFileWriter.finish_last_section)               | Delete current section if it is empty.                                                                                             |
| [`flush_cache_directory`](#manim.scene.scene_file_writer.SceneFileWriter.flush_cache_directory)           | Delete all the cached partial movie files                                                                                          |
| [`get_resolution_directory`](#manim.scene.scene_file_writer.SceneFileWriter.get_resolution_directory)     | Get the name of the resolution directory directly containing the video file.                                                       |
| [`init_audio`](#manim.scene.scene_file_writer.SceneFileWriter.init_audio)                                 | Preps the writer for adding audio to the movie.                                                                                    |
| [`init_output_directories`](#manim.scene.scene_file_writer.SceneFileWriter.init_output_directories)       | Initialise output directories.                                                                                                     |
| [`is_already_cached`](#manim.scene.scene_file_writer.SceneFileWriter.is_already_cached)                   | Will check if a file named with hash_invocation exists.                                                                            |
| [`listen_and_write`](#manim.scene.scene_file_writer.SceneFileWriter.listen_and_write)                     | For internal use only: blocks until new frame is available on the queue.                                                           |
| [`next_section`](#manim.scene.scene_file_writer.SceneFileWriter.next_section)                             | Create segmentation cut here.                                                                                                      |
| [`open_partial_movie_stream`](#manim.scene.scene_file_writer.SceneFileWriter.open_partial_movie_stream)   | Open a container holding a video stream.                                                                                           |
| `output_image`                                                                                            |                                                                                                                                    |
| [`print_file_ready_message`](#manim.scene.scene_file_writer.SceneFileWriter.print_file_ready_message)     | Prints the "File Ready" message to STDOUT.                                                                                         |
| [`save_image`](#manim.scene.scene_file_writer.SceneFileWriter.save_image)                                 | This method saves the image passed to it in the default image directory.                                                           |
| [`write_frame`](#manim.scene.scene_file_writer.SceneFileWriter.write_frame)                               | Used internally by Manim to write a frame to the FFMPEG input buffer.                                                              |
| [`write_subcaption_file`](#manim.scene.scene_file_writer.SceneFileWriter.write_subcaption_file)           | Writes the subcaption file.                                                                                                        |

### Attributes

| `force_output_as_scene_name`   |    |
|--------------------------------|----|

#### add_audio_segment(new_segment, time=None, gain_to_background=None)

This method adds an audio segment from an AudioSegment type object
and suitable parameters.

* **Parameters:**
  * **new_segment** (*AudioSegment*) – The audio segment to add
  * **time** (*float* *|* *None*) – the timestamp at which the sound should be added.
  * **gain_to_background** (*float* *|* *None*) – The gain of the segment from the background.
* **Return type:**
  None

#### add_partial_movie_file(hash_animation)

Adds a new partial movie file path to `scene.partial_movie_files`
and current section from a hash.

This method will compute the path from the hash. In addition to that it
adds the new animation to the current section.

* **Parameters:**
  **hash_animation** (*str* *|* *None*) – Hash of the animation.
* **Return type:**
  None

#### add_sound(sound_file, time=None, gain=None, \*\*kwargs)

This method adds an audio segment from a sound file.

* **Parameters:**
  * **sound_file** ([*StrPath*](manim.typing.md#manim.typing.StrPath)) – The path to the sound file.
  * **time** (*float* *|* *None*) – The timestamp at which the audio should be added.
  * **gain** (*float* *|* *None*) – The gain of the given audio segment.
  * **\*\*kwargs** (*Any*) – This method uses add_audio_segment, so any keyword arguments
    used there can be referenced here.
* **Return type:**
  None

#### begin_animation(allow_write=False, file_path=None)

Used internally by manim to stream the animation to FFMPEG for
displaying or writing to a file.

* **Parameters:**
  * **allow_write** (*bool*) – Whether or not to write to a video file.
  * **file_path** ([*StrPath*](manim.typing.md#manim.typing.StrPath) *|* *None*)
* **Return type:**
  None

#### clean_cache()

Will clean the cache by removing the oldest partial_movie_files.

* **Return type:**
  None

#### close_partial_movie_stream()

Close the currently opened video container.

Used internally by Manim to first flush the remaining packages
in the video stream holding a partial file, and then close
the corresponding container.

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

#### create_audio_segment()

Creates an empty, silent, Audio Segment.

* **Return type:**
  None

#### encode_and_write_frame(frame, num_frames)

For internal use only: takes a given frame in `np.ndarray` format and
writes it to the stream

* **Parameters:**
  * **frame** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray))
  * **num_frames** (*int*)
* **Return type:**
  None

#### end_animation(allow_write=False)

Internally used by Manim to stop streaming to FFMPEG gracefully.

* **Parameters:**
  **allow_write** (*bool*) – Whether or not to write to a video file.
* **Return type:**
  None

#### finish()

Finishes writing to the FFMPEG buffer or writing images to output directory.
Combines the partial movie files into the whole scene.
If save_last_frame is True, saves the last frame in the default image directory.

* **Return type:**
  None

#### finish_last_section()

Delete current section if it is empty.

* **Return type:**
  None

#### flush_cache_directory()

Delete all the cached partial movie files

* **Return type:**
  None

#### get_resolution_directory()

Get the name of the resolution directory directly containing
the video file.

This method gets the name of the directory that immediately contains the
video file. This name is `<height_in_pixels_of_video>p<frame_rate>`.
For example, if you are rendering an 854x480 px animation at 15fps,
the name of the directory that immediately contains the video,  file
will be `480p15`.

The file structure should look something like:

```default
MEDIA_DIR
    |--Tex
    |--texts
    |--videos
        |--<name_of_file_containing_scene>
            |--<height_in_pixels_of_video>p<frame_rate>
                |--partial_movie_files
                |--<scene_name>.mp4
                |--<scene_name>.srt
```

* **Returns:**
  The name of the directory.
* **Return type:**
  `str`

#### init_audio()

Preps the writer for adding audio to the movie.

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

#### is_already_cached(hash_invocation)

Will check if a file named with hash_invocation exists.

* **Parameters:**
  **hash_invocation** (*str*) – The hash corresponding to an invocation to either scene.play or scene.wait.
* **Returns:**
  Whether the file exists.
* **Return type:**
  `bool`

#### listen_and_write()

For internal use only: blocks until new frame is available on the queue.

* **Return type:**
  None

#### next_section(name, type_, skip_animations)

Create segmentation cut here.

* **Parameters:**
  * **name** (*str*)
  * **type_** (*str*)
  * **skip_animations** (*bool*)
* **Return type:**
  None

#### open_partial_movie_stream(file_path=None)

Open a container holding a video stream.

This is used internally by Manim initialize the container holding
the video stream of a partial movie file.

* **Parameters:**
  **file_path** ([*StrPath*](manim.typing.md#manim.typing.StrPath) *|* *None*)
* **Return type:**
  None

#### print_file_ready_message(file_path)

Prints the “File Ready” message to STDOUT.

* **Parameters:**
  **file_path** ([*StrPath*](manim.typing.md#manim.typing.StrPath))
* **Return type:**
  None

#### save_image(image)

This method saves the image passed to it in the default image directory.

* **Parameters:**
  **image** (*Image*) – The pixel array of the image to save.
* **Return type:**
  None

#### write_frame(frame_or_renderer, num_frames=1)

Used internally by Manim to write a frame to the FFMPEG input buffer.

* **Parameters:**
  * **frame_or_renderer** ([*PixelArray*](manim.typing.md#manim.typing.PixelArray) *|* *OpenGLRenderer*) – Pixel array of the frame.
  * **num_frames** (*int*) – The number of times to write frame.
* **Return type:**
  None

#### write_subcaption_file()

Writes the subcaption file.

* **Return type:**
  None
