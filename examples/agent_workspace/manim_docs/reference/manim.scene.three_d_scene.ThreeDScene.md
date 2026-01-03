# ThreeDScene

Qualified name: `manim.scene.three\_d\_scene.ThreeDScene`

### *class* ThreeDScene(camera_class=<class 'manim.camera.three_d_camera.ThreeDCamera'>, ambient_camera_rotation=None, default_angled_camera_orientation_kwargs=None, \*\*kwargs)

Bases: [`Scene`](manim.scene.scene.Scene.md#manim.scene.scene.Scene)

This is a Scene, with special configurations and properties that
make it suitable for Three Dimensional Scenes.

### Methods

| [`add_fixed_in_frame_mobjects`](#manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects)                           | This method is used to prevent the rotation and movement of mobjects as the camera moves around.                                       |
|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [`add_fixed_orientation_mobjects`](#manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects)                     | This method is used to prevent the rotation and tilting of mobjects as the camera moves around.                                        |
| [`begin_3dillusion_camera_rotation`](#manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation)                 | This method creates a 3D camera rotation illusion around the current camera orientation.                                               |
| [`begin_ambient_camera_rotation`](#manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation)                       | This method begins an ambient rotation of the camera about the Z_AXIS, in the anticlockwise direction                                  |
| [`get_moving_mobjects`](#manim.scene.three_d_scene.ThreeDScene.get_moving_mobjects)                                           | This method returns a list of all of the Mobjects in the Scene that are moving, that are also in the animations passed.                |
| [`move_camera`](#manim.scene.three_d_scene.ThreeDScene.move_camera)                                                           | This method animates the movement of the camera to the given spherical coordinates.                                                    |
| [`remove_fixed_in_frame_mobjects`](#manim.scene.three_d_scene.ThreeDScene.remove_fixed_in_frame_mobjects)                     | This method undoes what add_fixed_in_frame_mobjects does.                                                                              |
| [`remove_fixed_orientation_mobjects`](#manim.scene.three_d_scene.ThreeDScene.remove_fixed_orientation_mobjects)               | This method "unfixes" the orientation of the mobjects passed, meaning they will no longer be at the same angle relative to the camera. |
| [`set_camera_orientation`](#manim.scene.three_d_scene.ThreeDScene.set_camera_orientation)                                     | This method sets the orientation of the camera in the scene.                                                                           |
| [`set_to_default_angled_camera_orientation`](#manim.scene.three_d_scene.ThreeDScene.set_to_default_angled_camera_orientation) | This method sets the default_angled_camera_orientation to the keyword arguments passed, and sets the camera to that orientation.       |
| [`stop_3dillusion_camera_rotation`](#manim.scene.three_d_scene.ThreeDScene.stop_3dillusion_camera_rotation)                   | This method stops all illusion camera rotations.                                                                                       |
| [`stop_ambient_camera_rotation`](#manim.scene.three_d_scene.ThreeDScene.stop_ambient_camera_rotation)                         | This method stops all ambient camera rotation.                                                                                         |

### Attributes

| `camera`   |                                        |
|------------|----------------------------------------|
| `time`     | The time since the start of the scene. |

#### add_fixed_in_frame_mobjects(\*mobjects)

This method is used to prevent the rotation and movement
of mobjects as the camera moves around. The mobject is
essentially overlaid, and is not impacted by the camera’s
movement in any way.

* **Parameters:**
  **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The Mobjects whose orientation must be fixed.

#### add_fixed_orientation_mobjects(\*mobjects, \*\*kwargs)

This method is used to prevent the rotation and tilting
of mobjects as the camera moves around. The mobject can
still move in the x,y,z directions, but will always be
at the angle (relative to the camera) that it was at
when it was passed through this method.)

* **Parameters:**
  * **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The Mobject(s) whose orientation must be fixed.
  * **\*\*kwargs** – 

    Some valid kwargs are
    : use_static_center_func : bool
      center_func : function

#### begin_3dillusion_camera_rotation(rate=1, origin_phi=None, origin_theta=None)

This method creates a 3D camera rotation illusion around
the current camera orientation.

* **Parameters:**
  * **rate** (*float*) – The rate at which the camera rotation illusion should operate.
  * **origin_phi** (*float* *|* *None*) – The polar angle the camera should move around. Defaults
    to the current phi angle.
  * **origin_theta** (*float* *|* *None*) – The azimutal angle the camera should move around. Defaults
    to the current theta angle.

#### begin_ambient_camera_rotation(rate=0.02, about='theta')

This method begins an ambient rotation of the camera about the Z_AXIS,
in the anticlockwise direction

* **Parameters:**
  * **rate** (*float*) – The rate at which the camera should rotate about the Z_AXIS.
    Negative rate means clockwise rotation.
  * **about** (*str*) – one of 3 options: [“theta”, “phi”, “gamma”]. defaults to theta.

#### get_moving_mobjects(\*animations)

This method returns a list of all of the Mobjects in the Scene that
are moving, that are also in the animations passed.

* **Parameters:**
  **\*animations** ([*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation)) – The animations whose mobjects will be checked.

#### move_camera(phi=None, theta=None, gamma=None, zoom=None, focal_distance=None, frame_center=None, added_anims=[], \*\*kwargs)

This method animates the movement of the camera
to the given spherical coordinates.

* **Parameters:**
  * **phi** (*float* *|* *None*) – The polar angle i.e the angle between Z_AXIS and Camera through ORIGIN in radians.
  * **theta** (*float* *|* *None*) – The azimuthal angle i.e the angle that spins the camera around the Z_AXIS.
  * **focal_distance** (*float* *|* *None*) – The radial focal_distance between ORIGIN and Camera.
  * **gamma** (*float* *|* *None*) – The rotation of the camera about the vector from the ORIGIN to the Camera.
  * **zoom** (*float* *|* *None*) – The zoom factor of the camera.
  * **frame_center** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *Sequence* *[**float* *]*  *|* *None*) – The new center of the camera frame in cartesian coordinates.
  * **added_anims** (*Iterable* *[*[*Animation*](manim.animation.animation.Animation.md#manim.animation.animation.Animation) *]*) – Any other animations to be played at the same time.

#### remove_fixed_in_frame_mobjects(\*mobjects)

> This method undoes what add_fixed_in_frame_mobjects does.
> It allows the mobject to be affected by the movement of
> the camera.
* **Parameters:**
  **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The Mobjects whose position and orientation must be unfixed.

#### remove_fixed_orientation_mobjects(\*mobjects)

This method “unfixes” the orientation of the mobjects
passed, meaning they will no longer be at the same angle
relative to the camera. This only makes sense if the
mobject was passed through add_fixed_orientation_mobjects first.

* **Parameters:**
  **\*mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject)) – The Mobjects whose orientation must be unfixed.

#### set_camera_orientation(phi=None, theta=None, gamma=None, zoom=None, focal_distance=None, frame_center=None, \*\*kwargs)

This method sets the orientation of the camera in the scene.

* **Parameters:**
  * **phi** (*float* *|* *None*) – The polar angle i.e the angle between Z_AXIS and Camera through ORIGIN in radians.
  * **theta** (*float* *|* *None*) – The azimuthal angle i.e the angle that spins the camera around the Z_AXIS.
  * **focal_distance** (*float* *|* *None*) – The focal_distance of the Camera.
  * **gamma** (*float* *|* *None*) – The rotation of the camera about the vector from the ORIGIN to the Camera.
  * **zoom** (*float* *|* *None*) – The zoom factor of the scene.
  * **frame_center** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) *|* *Sequence* *[**float* *]*  *|* *None*) – The new center of the camera frame in cartesian coordinates.

#### set_to_default_angled_camera_orientation(\*\*kwargs)

This method sets the default_angled_camera_orientation to the
keyword arguments passed, and sets the camera to that orientation.

* **Parameters:**
  **\*\*kwargs** – Some recognised kwargs are phi, theta, focal_distance, gamma,
  which have the same meaning as the parameters in set_camera_orientation.

#### stop_3dillusion_camera_rotation()

This method stops all illusion camera rotations.

#### stop_ambient_camera_rotation(about='theta')

This method stops all ambient camera rotation.
