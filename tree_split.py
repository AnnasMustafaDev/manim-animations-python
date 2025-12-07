
from manim import *
import numpy as np

class DecisionTreeSplit(Scene):
    def construct(self):
        # 1. Setup the Coordinate System and Axes
        self.axes = Axes(
            x_range=[0, 10, 1], 
            y_range=[0, 10, 1], 
            x_length=7, 
            y_length=7, 
            axis_config={"include_numbers": True}
        ).to_edge(LEFT, buff=0.5)
        
        x_label = self.axes.get_x_axis_label("Feature 1 (X)").shift(DOWN * 0.5)
        y_label = self.axes.get_y_axis_label("Feature 2 (Y)").shift(LEFT * 0.5)

        self.play(
            Create(self.axes), 
            Write(x_label), 
            Write(y_label)
        )

        # 2. Generate Sample Data
        np.random.seed(42)
        
        # Class 0 (Blue) - Top Left
        X0 = np.random.uniform(1, 5, size=(50, 1))
        Y0 = np.random.uniform(5, 9, size=(50, 1))
        data_class0 = np.hstack([X0, Y0])

        # Class 1 (Red) - Bottom Right
        X1 = np.random.uniform(5, 9, size=(50, 1))
        Y1 = np.random.uniform(1, 5, size=(50, 1))
        data_class1 = np.hstack([X1, Y1])

        # 3. Plot the Data Points
        points = VGroup()
        for x, y in data_class0:
            points.add(Dot(self.axes.coords_to_point(x, y), color=BLUE, radius=0.05))
        for x, y in data_class1:
            points.add(Dot(self.axes.coords_to_point(x, y), color=RED, radius=0.05))
            
        title = Text("Initial Data Space (Root Node)").to_edge(UP).scale(0.8)
        self.play(Write(title), lag_ratio=0.5)
        self.play(
            LaggedStart(*[Create(p) for p in points], lag_ratio=0.01),
            run_time=2
        )
        self.wait(1)

        # --- SPLIT 1: Vertical split on X-axis at X=5 (YELLOW) ---
        split1_x = 5.0
        p1_start = self.axes.coords_to_point(split1_x, 0)
        p1_end = self.axes.coords_to_point(split1_x, 10)
        split_line1 = Line(p1_start, p1_end, color=YELLOW, stroke_width=4)
        
        text1 = Text(f"Split 1: Feature 1 < {split1_x}").next_to(self.axes, RIGHT, buff=0.5).shift(UP*1.5).scale(0.6)
        
        self.play(Create(split_line1), Write(text1))
        self.wait(1)

        # --- SPLIT 2: Horizontal split in the left region (X <= 5) at Y=5 (ORANGE) ---
        split2_y = 5.0
        p2_start = self.axes.coords_to_point(0, split2_y)
        p2_end = self.axes.coords_to_point(split1_x, split2_y)
        split_line2 = Line(p2_start, p2_end, color=ORANGE, stroke_width=4)
        
        text2 = Text(f"Split 2 (Left): Feature 2 < {split2_y}").next_to(text1, DOWN, aligned_edge=LEFT).scale(0.6)
        
        self.play(Create(split_line2), Write(text2))
        self.wait(1)

        # --- SPLIT 3: Horizontal split in the right region (X > 5) at Y=5.5 (GREEN) ---
        split3_y = 5.5
        p3_start = self.axes.coords_to_point(split1_x, split3_y)
        p3_end = self.axes.coords_to_point(10, split3_y)
        split_line3 = Line(p3_start, p3_end, color=GREEN, stroke_width=4)
        
        text3 = Text(f"Split 3 (Right): Feature 2 < {split3_y}").next_to(text2, DOWN, aligned_edge=LEFT).scale(0.6)
        
        self.play(Create(split_line3), Write(text3))
        self.wait(1)
        
        # Cleanup Text
        self.play(FadeOut(VGroup(text1, text2, text3)))

        # --- FINAL REGIONS ---
        # We use Polygon and c2p (coords_to_point) to explicitly define the corners
        
        # Region 1 (Top-Left): X: 0->5, Y: 5->10 (BLUE)
        rect1 = Polygon(
            self.axes.c2p(0, 5), self.axes.c2p(5, 5), 
            self.axes.c2p(5, 10), self.axes.c2p(0, 10),
            color=BLUE, fill_opacity=0.3, stroke_width=0
        )
        
        # Region 2 (Bottom-Left): X: 0->5, Y: 0->5 (RED)
        rect2 = Polygon(
            self.axes.c2p(0, 0), self.axes.c2p(5, 0), 
            self.axes.c2p(5, 5), self.axes.c2p(0, 5),
            color=RED, fill_opacity=0.3, stroke_width=0
        )

        # Region 3 (Top-Right): X: 5->10, Y: 5.5->10 (BLUE)
        rect3 = Polygon(
            self.axes.c2p(5, 5.5), self.axes.c2p(10, 5.5), 
            self.axes.c2p(10, 10), self.axes.c2p(5, 10),
            color=BLUE, fill_opacity=0.3, stroke_width=0
        )
        
        # Region 4 (Bottom-Right): X: 5->10, Y: 0->5.5 (RED)
        rect4 = Polygon(
            self.axes.c2p(5, 0), self.axes.c2p(10, 0), 
            self.axes.c2p(10, 5.5), self.axes.c2p(5, 5.5),
            color=RED, fill_opacity=0.3, stroke_width=0
        )

        # Ensure lines and points are on top of the colored regions
        self.bring_to_front(points, split_line1, split_line2, split_line3)
        
        final_title = Text("Final Decision Boundaries").to_edge(UP).scale(0.8)
        self.play(
            Transform(title, final_title),
            FadeIn(VGroup(rect1, rect2, rect3, rect4), run_time=2)
        )
        self.wait(3)

        # FIX IS HERE: We unpack the list using *
        self.play(FadeOut(*self.mobjects))