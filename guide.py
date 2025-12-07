# ✅ 1. Manim Essentials (Quick Syntax Guide)
# Scene Structure
from manim import *

class MyScene(Scene):
    def construct(self):
        # code goes here

    # Basic Objects (Mobjects)
    circle = Circle()                  # Circle()
    square = Square()                  # Square()
    text = Text("Hello Manim!")        # Text
    line = Line(start=LEFT, end=RIGHT) # Line

    # Adding to Scene
    self.add(circle)       # Instantly appear
    self.play(Create(circle))   # Animate creation

    # Common Animations
    self.play(Write(text))             # Like handwritten effect
    self.play(FadeIn(circle))          # Fade in
    self.play(FadeOut(circle))         # Fade out
    self.play(circle.animate.shift(RIGHT * 2))  # Move
    self.play(circle.animate.scale(1.5))         # Scale
    self.play(Transform(circle, square))        # Transform

    # Colors & Positioning
    circle.set_color(BLUE)
    circle.shift(UP)
    circle.move_to(LEFT)
    square.next_to(circle, RIGHT)

    # Grouping
    group = VGroup(circle, square)
    group.arrange(RIGHT)