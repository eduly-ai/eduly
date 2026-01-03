from manim import *

class BarChartExample(Scene):
    def construct(self):
        # 1. Standard BarChart
        chart = BarChart(
            values=[10, 20, 30, 40, 50],
            bar_names=["A", "B", "C", "D", "E"],
            y_range=[0, 60, 10],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 36},
        )
        
        self.add(chart)
