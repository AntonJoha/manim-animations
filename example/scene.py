from manim import * 


class CreateCircle(Scene):

    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI/4)


        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle,UP, buff=0.5)
        self.play(Create(circle), Create(square))

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.shift((0.4,2,1)))
        self.play(ReplacementTransform(square, circle))
        self.play(
                square.animate.set_fill(PINK, opacity=0.5)
            )


class TextExample(Scene):
    def construct(self):
        text = MathTex(
                "\\frac{d}{dx}"
            )
        self.play(Write(text))
