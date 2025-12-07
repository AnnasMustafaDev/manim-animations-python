from manim import *
# Create an animation where:
# A square appears
# It moves to the right
# A circle fades in next to it
# The circle and square rotate together


# Change the circle color to green
# Make the square scale up by 1.3x before rotating
# Make the circle appear above the square, not next to it


# Modify the scene so that:
# After rotation,
# the circle moves to the left side of the square.
# Then both objects change color:
# square → BLUE
# circle → YELLOW
# Finally, make both shapes fade out together.
# You can add these lines after the rotation animation


# 1️⃣ A triangle that appears after the circle fades out
# 2️⃣ The triangle should:
# Start at the top
# Move down to the center
# Rotate 180°
# Change color to PURPLE

# 3️⃣ Everything should end with:
# Square, circle, triangle all shrinking to nothing (scale to 0)

class MyScene3(Scene):
    def construct(self):
        circle = Circle().set_color(GREEN)
        square = Square().set_color(RED)
        triangle = Triangle().set_color(BLUE)




        # Create square
        self.play(Create(square))

        # Rotate square 360 degrees
        self.play(Rotate(square, angle=2*PI))

        # Circle grows from tiny to normal size
        circle.scale(0.1)
        self.play(circle.animate.scale(10))

        # Move square to the right
        self.play(square.animate.shift(RIGHT * 2))

        # Position circle above square, then fade it in
        circle.next_to(square, UP) ## can be animated
        self.play(FadeOut(circle))

        # Create triangle
        self.play(Create(triangle))
        self.play(triangle.animate.shift(DOWN * 2))

        self.play(Rotate(triangle, angle=PI))
        self.play(triangle.animate.set_color(PURPLE))

        # Scale square
        self.play(square.animate.scale(1.3))

        # Rotate both together
        group = VGroup(square, circle, triangle)
        self.play(Rotate(group, angle=PI/2))

        # Move circle to the left of the square
        self.play(circle.animate.move_to(square.get_center() + LEFT * 4))
        self.play(triangle.animate.move_to(square.get_center() + RIGHT * 4))

        # Change colors
        self.play(
            square.animate.set_color(BLUE),
            circle.animate.set_color(YELLOW)
        )

        # Fade both out
        self.play(FadeOut(group))
        self.play(group.animate.scale(0))
        self.wait()

class MyScene2(Scene):
    def construct(self):
        circle = Circle().set_color(GREEN)
        square = Square().set_color(RED)

        # Create square
        self.play(Create(square))

        # Rotate square 360 degrees
        self.play(Rotate(square, angle=2*PI))

        # Circle grows from tiny to normal size
        circle.scale(0.1)
        self.play(circle.animate.scale(10))

        # Move square to the right
        self.play(square.animate.shift(RIGHT * 2))

        # Position circle above square, then fade it in
        circle.next_to(square, UP) ## can be animated
        self.play(FadeIn(circle))

        # Scale square
        self.play(square.animate.scale(1.3))

        # Rotate both together
        group = VGroup(square, circle)
        self.play(Rotate(group, angle=PI/2))

        # Move circle to the left of the square
        self.play(circle.animate.move_to(square.get_center() + LEFT * 4))

        # Change colors
        self.play(
            square.animate.set_color(BLUE),
            circle.animate.set_color(YELLOW)
        )

        # Fade both out
        self.play(FadeOut(group))
        self.wait()
