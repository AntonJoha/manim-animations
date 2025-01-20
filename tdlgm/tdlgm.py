from manim import *




class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))



class Training(MovingCameraScene):

    def make_generator(self):

        recs = []
        for i in range(3):
            r = Rectangle(color=GREEN, height=1, width=1.5)
            r.set_fill(GREEN, opacity=0.5)
            r.shift((1.5*i)*DOWN)
            recs.append(r)
        for i in recs:
            self.play(Create(i))
        
        info = Tex("Generator").shift(UP)

        self.play(Write(info))

        info = Tex("These\\\\are\\\\the\\\\layers").shift(DOWN*1.5 + RIGHT*1.5)
        h = MathTex("h_3 \\\\\\\\ h_2 \\\\\\\\ h_1").shift(DOWN*1.5)

        self.play(Write(info), Write(h))
        self.wait(0.5)
        self.play(Unwrite(info))

    
    def make_recognition(self):


        recs = []
        for i in range(3):
            r = Rectangle(color=RED, height=1, width=1.5)
            r.set_fill(RED, opacity=0.5)
            r.shift((1.5*i)*DOWN + RIGHT*4)
            recs.append(r)
        for i in recs:
            self.play(Create(i),run_time=0.5)
        
        info = Tex("Recognition").shift(UP + RIGHT*4)

        self.play(Write(info), run_time=0.7)

        h = MathTex("q_3 \\\\\\\\ q_2 \\\\\\\\ q_1").shift(DOWN*1.5 + RIGHT*4)

        self.play(Write(h), run_time=0.5)

    def make_state_recognition(self):


        recs = []
        for i in range(1,3):
            r = Rectangle(color=RED, height=1, width=1.5)
            r.set_fill(RED, opacity=0.5)
            r.shift((1.5*i)*DOWN + LEFT*4)
            recs.append(r)
        for i in recs:
            self.play(Create(i),run_time=0.5)
        
        info = Tex("State recognition").shift(UP + LEFT*4)

        self.play(Write(info), run_time=0.7)

        h = MathTex("k_2 \\\\\\\\ k_1").shift(DOWN*2.3 + LEFT*4)

        self.play(Write(h),run_time=0.5)


    def make_vector(self):

        one = MathTex("\\text{One entry} v_t = ").shift(DOWN*5)
        sequence = MathTex("\\text{Sequence of entries} \\{v_{t},\\ldots,v_{t+N}\\} = " ).shift(DOWN*5 + LEFT*2)

        ball = Circle(radius=0.5).shift(DOWN*5 + RIGHT*2.3)
        ball.set_fill(RED, opacity=0.5)
 

        self.play(Create(ball), Write(one))

        
        seq = Group()
        save = []
        for i in range(10):
            b = Circle(radius=0.1).shift(DOWN*5 + RIGHT*(2.3 + i*0.2))
            b.set_fill(RED, opacity=0.5)
            seq.add(b)
            save.append(b)


        self.play(FadeOut(ball), Transform(one, sequence))

        vector = Circle(radius=0.5, color=GREEN).set_fill(GREEN, opacity=0.5).shift(DOWN*5 + RIGHT*2.5)

        self.play(FadeIn(seq))
        self.play(Transform(seq,vector))



        left = vector.copy()
        right = vector
        self.play(Unwrite(one), run_time=0.3)
        self.play(left.animate.move_to(LEFT*4 + DOWN*4).scale(0.5), seq.animate.move_to(RIGHT*4 + DOWN*4).scale(0.5), run_time=0.5)
        

        self.play(left.animate.move_to(LEFT*4 + DOWN*3), seq.animate.move_to(RIGHT*4 + DOWN*3), run_time=0.5)
        
        s_1 = left.copy()
        s_1.set_fill(LIGHT_PINK)
        s_1.set_color(LIGHT_PINK)
        self.add(s_1)
        xi_1 = seq.copy()
        xi_1.set_fill(BLUE)
        xi_1.set_color(BLUE)
        self.add(xi_1)
        self.play(xi_1.animate.move_to(RIGHT*2.5 + DOWN*3), seq.animate.move_to(RIGHT*4 + DOWN*1.5), s_1.animate.move_to(LEFT*2.5 + DOWN*3), left.animate.move_to(LEFT*4 + DOWN*1.5))


        s_2 = left.copy()
        s_2.set_fill(LIGHT_PINK)
        s_2.set_color(LIGHT_PINK)
        self.add(s_2)
        xi_2 = seq.copy()
        xi_2.set_fill(BLUE).set_color(BLUE)


        self.play(xi_2.animate.move_to(RIGHT*2.5 + DOWN*1.5), seq.animate.move_to(RIGHT*4), s_2.animate.move_to(LEFT*2.5 + DOWN*1.5), FadeOut(left))
        
        xi_3 = seq.copy().set_fill(BLUE).set_color(BLUE)
        self.play(xi_3.animate.move_to(RIGHT*2.5), FadeOut(seq))

        text = Tex("The generator reconstructs based on latent variables").shift(DOWN*5)


        self.play(xi_3.animate.move_to(RIGHT*0), Write(text))
        xi_3.set_color(GOLD).set_fill(GOLD)
        self.play(xi_3.animate.move_to(DOWN*1.5), xi_2.animate.move_to(DOWN*1.5), s_2.animate.move_to(DOWN*1.5))

        s_2.set_fill(GOLD).set_color(GOLD)
        self.play(FadeOut(xi_3), FadeOut(xi_2), s_2.animate.move_to(DOWN*3), s_1.animate.move_to(DOWN*3), xi_1.animate.move_to(DOWN*3))

        generated = MathTex("\\text{Generated value} = ").shift(DOWN*5)
        self.play(s_2.animate.scale(1.5).move_to(DOWN*5 + RIGHT*3), Transform(text,generated), FadeOut(xi_1), FadeOut(s_1))





    def construct(self):
        self.camera.frame.save_state()
        self.make_generator()

        self.make_recognition()
        self.make_state_recognition()

        self.wait(0.5)
        
        self.play(self.camera.frame.animate.move_to(DOWN*2.5))

        self.make_vector()



        self.wait(1)
