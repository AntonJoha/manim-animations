from manim import *


class SquareToCircle(Scene):

    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        square.flip(LEFT)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(square.animate.shift(LEFT))
        self.play(square.animate.rotate(1))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
