from manim import *

class HorizontalBarChartExample(Scene):
    def construct(self):
        # Create Axes where x is the value and y is the category
        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": False}
        )
        
        values = [20, 45, 70, 10, 90]
        bars = VGroup()
        
        for i, val in enumerate(values):
            # Create a rectangle for each value
            # Width corresponds to value, Height is fixed (e.g. 0.6)
            # Positioned at y = i + 0.5 (center of the interval)
            
            bar_width = axes.coords_to_point(val, 0) - axes.coords_to_point(0, 0)
            bar_width = bar_width[0] # Take x component
            
            bar = Rectangle(
                width=bar_width,
                height=0.6,
                fill_color=BLUE,
                fill_opacity=0.8
            )
            
            # Position the bar
            # Left edge at x=0
            # Y center at i + 0.5
            bar.next_to(axes.c2p(0, i + 0.5), RIGHT, buff=0)
            bars.add(bar)
            
        self.add(axes, bars)
