# Manim’s building blocks

This document explains the building blocks of manim and will give you all the
necessary tools to start producing your own videos.

Essentially, manim puts at your disposal three different concepts that you can
orchestrate together to produce mathematical animations: the
**mathematical object** (or **mobject** for short), the **animation**, and the
**scene**.  As we will see in the following sections, each of these three
concepts is implemented in manim as a separate class: the [`Mobject`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject),
[`Animation`](../reference/manim.animation.animation.Animation.md#manim.animation.animation.Animation), and [`Scene`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene) classes.

#### NOTE
It is recommended that you read the tutorials [Quickstart](quickstart.md) and
[Manim’s Output Settings](output_and_config.md) before reading this page.

## Mobjects

Mobjects are the basic building blocks for all manim animations.  Each class
that derives from [`Mobject`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) represents an object that can be displayed
on the screen.  For example, simple shapes such as [`Circle`](../reference/manim.mobject.geometry.arc.Circle.md#manim.mobject.geometry.arc.Circle),
[`Arrow`](../reference/manim.mobject.geometry.line.Arrow.md#manim.mobject.geometry.line.Arrow), and [`Rectangle`](../reference/manim.mobject.geometry.polygram.Rectangle.md#manim.mobject.geometry.polygram.Rectangle) are all mobjects.  More complicated
constructs such as [`Axes`](../reference/manim.mobject.graphing.coordinate_systems.Axes.md#manim.mobject.graphing.coordinate_systems.Axes), [`FunctionGraph`](../reference/manim.mobject.graphing.functions.FunctionGraph.md#manim.mobject.graphing.functions.FunctionGraph), or
[`BarChart`](../reference/manim.mobject.graphing.probability.BarChart.md#manim.mobject.graphing.probability.BarChart) are mobjects as well.

If you try to display an instance of [`Mobject`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) on the screen, you will only
see an empty frame.  The reason is that the [`Mobject`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) class is an
abstract base class of all other mobjects, i.e. it does not have any
pre-determined visual shape that can be displayed on the screen.  It is only the
skeleton of a thing that *could* be displayed.  Therefore, you will rarely need
to use plain instances of [`Mobject`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject); instead, you will most likely
create instances of its derived classes.  One of these derived classes is
[`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject).  The `V` stands for Vectorized Mobject.  In essence, a
vmobject is a mobject that uses [vector graphics](https://en.wikipedia.org/wiki/Vector_graphics) to be displayed.  Most of
the time, you will be dealing with vmobjects, though we will continue to use
the term “mobject” to refer to the class of shapes that can be displayed on the
screen, as it is more general.

#### NOTE
Any object that can be displayed on the screen is a `mobject`, even if
it is not necessarily *mathematical* in nature.

### Creating and displaying mobjects

As explained in [Quickstart](quickstart.md), usually all of the code in a manim
script is put inside the [`construct()`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene.construct) method of a [`Scene`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene) class.
To display a mobject on the screen, call the [`add()`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene.add) method of the
containing [`Scene`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene).  This is the principal way of displaying a mobject
on the screen when it is not being animated.  To remove a mobject from the
screen, simply call the [`remove()`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene.remove) method from the containing
[`Scene`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene).

### Placing mobjects

Let’s define a new [`Scene`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene) called `Shapes` and [`add()`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene.add)
some mobjects to it.  This script generates a static picture that displays a
circle, a square, and a triangle:

By default, mobjects are placed at the center of coordinates, or *origin*, when
they are first created.  They are also given some default colors.  Further, the
`Shapes` scene places the mobjects by using the [`shift()`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.shift) method.  The
square is shifted one unit in the `UP` direction from the origin, while the
circle and triangle are shifted one unit `LEFT` and `RIGHT`, respectively.

#### ATTENTION
Unlike other graphics software, manim places the center of
coordinates at the center of the screen.  The positive vertical
direction is up, and the positive horizontal direction is right.
See also the constants `ORIGIN`, `UP`, `DOWN`, `LEFT`,
`RIGHT`, and others, defined in the [`constants`](../reference/manim.constants.md#module-manim.constants) module.

There are many other possible ways to place mobjects on the screen, for example
[`move_to()`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.move_to), [`next_to()`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.next_to), and [`align_to()`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.align_to).  The next scene
`MobjectPlacement` uses all three.

The [`move_to()`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.move_to) method uses absolute units (measured relative to the
`ORIGIN`), while [`next_to()`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.next_to) uses relative units (measured from the
mobject passed as the first argument).  `align_to()` uses `LEFT` not as
measuring units but as a way to determine the border to use for alignment.  The
coordinates of the borders of a mobject are determined using an imaginary
bounding box around it.

### Styling mobjects

The following scene changes the default aesthetics of the mobjects.

This scene uses two of the main functions that change the visual style of a
mobject: `set_stroke()` and [`set_fill()`](../reference/manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject.set_fill).  The former changes the
visual style of the mobject’s border while the latter changes the style of the
interior.  By default, most mobjects have a fully transparent interior so you
must specify the `opacity` parameter to display the color.  An
opacity of `1.0` means fully opaque, while `0.0` means fully transparent.

Only instances of [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) implement `set_stroke()` and
[`set_fill()`](../reference/manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject.set_fill).  Instances of [`Mobject`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) implement
`set_color()` instead.  The vast majority of pre-defined classes
are derived from [`VMobject`](../reference/manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) so it is usually safe to assume that you
have access to `set_stroke()` and [`set_fill()`](../reference/manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject.set_fill).

### Mobject on-screen order

The next scene is exactly the same as the `MobjectStyling` scene from the
previous section, except for exactly one line.

The only difference here (besides the scene name) is the order in which the
mobjects are added to the scene.  In `MobjectStyling`, we added them as
`add(circle, square, triangle)`, whereas in `MobjectZOrder` we add them as
`add(triangle, square, circle)`.

As you can see, the order of the arguments of [`add()`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene.add) determines
the order that the mobjects are displayed on the screen, with the left-most
arguments being put in the back.

## Animations

At the heart of manim is animation.  Generally, you can add an animation to
your scene by calling the [`play()`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene.play) method.

Put simply, animations are procedures that interpolate between two mobjects.
For example, `FadeIn(square)` starts with a fully transparent version of
`square` and ends with a fully opaque version, interpolating between them
by gradually increasing the opacity.  [`FadeOut`](../reference/manim.animation.fading.FadeOut.md#manim.animation.fading.FadeOut) works in the opposite
way: it interpolates from fully opaque to fully transparent.  As another
example, [`Rotate`](../reference/manim.animation.rotation.Rotate.md#manim.animation.rotation.Rotate) starts with the mobject passed to it as argument, and
ends with the same object but rotated by a certain amount, this time
interpolating the mobject’s angle instead of its opacity.

### Animating methods

Any property of a mobject that can be changed can be animated.  In fact, any
method that changes a mobject’s property can be used as an animation, through
the use of [`animate()`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.animate).

[`animate()`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.animate) is a property of all mobjects that animates the methods that come
afterward. For example, `square.set_fill(WHITE)` sets the fill color of
the square, while `square.animate.set_fill(WHITE)` animates this action.

### Animation run time

By default, any animation passed to `play()` lasts for exactly one second.
Use the `run_time` argument to control the duration.

### Creating a custom animation

Even though Manim has many built-in animations, you will find times when you need to smoothly animate from one state of a [`Mobject`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject) to another.
If you find yourself in that situation, then you can define your own custom animation.
You start by extending the [`Animation`](../reference/manim.animation.animation.Animation.md#manim.animation.animation.Animation) class and overriding its [`interpolate_mobject()`](../reference/manim.animation.animation.Animation.md#manim.animation.animation.Animation.interpolate_mobject).
The [`interpolate_mobject()`](../reference/manim.animation.animation.Animation.md#manim.animation.animation.Animation.interpolate_mobject) method receives alpha as a parameter that starts at 0 and changes throughout the animation.
So, you just have to manipulate self.mobject inside Animation according to the alpha value in its interpolate_mobject method.
Then you get all the benefits of [`Animation`](../reference/manim.animation.animation.Animation.md#manim.animation.animation.Animation) such as playing it for different run times or using different rate functions.

Let’s say you start with a number and want to create a [`Transform`](../reference/manim.animation.transform.Transform.md#manim.animation.transform.Transform) animation that transforms it to a target number.
You can do it using [`FadeTransform`](../reference/manim.animation.transform.FadeTransform.md#manim.animation.transform.FadeTransform), which will fade out the starting number and fade in the target number.
But when we think about transforming a number from one to another, an intuitive way of doing it is by incrementing or decrementing it smoothly.
Manim has a feature that allows you to customize this behavior by defining your own custom animation.

You can start by creating your own `Count` class that extends [`Animation`](../reference/manim.animation.animation.Animation.md#manim.animation.animation.Animation).
The class can have a constructor with three arguments, a [`DecimalNumber`](../reference/manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) Mobject, start, and end.
The constructor will pass the [`DecimalNumber`](../reference/manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) Mobject to the super constructor (in this case, the [`Animation`](../reference/manim.animation.animation.Animation.md#manim.animation.animation.Animation) constructor) and will set start and end.

The only thing that you need to do is to define how you want it to look at every step of the animation.
Manim provides you with the alpha value in the [`interpolate_mobject()`](../reference/manim.animation.animation.Animation.md#manim.animation.animation.Animation.interpolate_mobject) method based on frame rate of video, rate function, and run time of animation played.
The alpha parameter holds a value between 0 and 1 representing the step of the currently playing animation.
For example, 0 means the beginning of the animation, 0.5 means halfway through the animation, and 1 means the end of the animation.

In the case of the `Count` animation, you just have to figure out a way to determine the number to display at the given alpha value and then set that value in the [`interpolate_mobject()`](../reference/manim.animation.animation.Animation.md#manim.animation.animation.Animation.interpolate_mobject) method of the `Count` animation.
Suppose you are starting at 50 and incrementing until the [`DecimalNumber`](../reference/manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) reaches 100 at the end of the animation.

* If alpha is 0, you want the value to be 50.
* If alpha is 0.5, you want the value to be 75.
* If alpha is 1, you want the value to be 100.

Generally, you start with the starting number and add only some part of the value to be increment according to the alpha value.
So, the logic of calculating the number to display at each step will be `50 + alpha * (100 - 50)`.
Once you set the calculated value for the [`DecimalNumber`](../reference/manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber), you are done.

#### NOTE
If you’re creating a custom animation and want to use a `rate_func`, you must explicitly apply
`self.rate_func(alpha)` to the parameter you’re animating. For example, try switching the rate
function to `rate_functions.there_and_back` to observe how it affects the counting behavior.

Once you have defined your `Count` animation, you can play it in your [`Scene`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene) for any duration you want for any [`DecimalNumber`](../reference/manim.mobject.text.numbers.DecimalNumber.md#manim.mobject.text.numbers.DecimalNumber) with any rate function.

### Using coordinates of a mobject

Mobjects contain points that define their boundaries.
These points can be used to add other mobjects respectively to each other,
e.g. by methods like [`get_center()`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.get_center) , [`get_top()`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.get_top)
and [`get_start()`](../reference/manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject.get_start). Here is an example of some important coordinates:

### Transforming mobjects into other mobjects

It is also possible to transform a mobject into another mobject like this:

The Transform function maps points of the previous mobject to the points of the
next mobject.
This might result in strange behaviour, e.g. when the dots of one mobject are
arranged clockwise and the other points are arranged counterclockwise.
Here it might help to use the flip function and reposition the points via the
[roll](https://numpy.org/doc/stable/reference/generated/numpy.roll.html)
function of numpy:

## Scenes

The [`Scene`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene) class is the connective tissue of manim.  Every mobject has
to be [`added`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene.add) to a scene to be displayed, or [`removed`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene.remove) from it to cease being displayed.  Every animation has to be
[`played`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene.play) by a scene, and every time interval where no
animation occurs is determined by a call to [`wait()`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene.wait).  All of the
code of your video must be contained in the [`construct()`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene.construct) method of
a class that derives from [`Scene`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene).  Finally, a single file may contain
multiple [`Scene`](../reference/manim.scene.scene.Scene.md#manim.scene.scene.Scene) subclasses if multiple scenes are to be
rendered at the same time.
