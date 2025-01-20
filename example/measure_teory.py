from manim import *
from fractions import Fraction
from copy import deepcopy

class CantorSet(Scene):




    def new_level(self, left, right, level, max_level=1):
        

        queue = [(left, right, 0)]
        to_draw = {}


        while len(queue) > 0:
            i = queue.pop()

            if i[2] not in to_draw:
                to_draw[i[2]] = []

            left_left = deepcopy(i[0])
            left_right = deepcopy(i[1])/3
            right_left = 2*(deepcopy(i[1])/3)
            right_right = deepcopy(i[1])
            


            to_draw[i[2]].append(self.get_line(left_left, left_right, i[2] + 1))

            to_draw[i[2]].append(self.get_line(right_left, right_right, i[2] + 1))


            if i[2] < max_level:
                queue.append((left_left, left_right, i[2] + 1))

                queue.append((right_left, right_right, i[2] + 1))

        
        for key in to_draw:
            for i in to_draw[key]:
                self.play(Create(i))

    
    def get_line(self, left_frac, right_frac,level):

        

        left = left_frac.numerator/left_frac.denominator
        right = right_frac.numerator/right_frac.denominator

        shift = self.start + self.length*left

        print("Shift: ", shift)
        line = Line((left,0,0)*self.length, (right,0,0)*self.length).shift(level*DOWN).shift(self.start)
        print(self.start*left)

        if left == 0:
            text_left = MathTex("0").shift(level*DOWN).shift(shift)
        else:
            text_left = MathTex("\\frac{%i}{%i}" % (left_frac.numerator, left_frac.denominator)).shift(level*DOWN).shift(shift)


        text_right = MathTex("\\frac{%i}{%i}" % (right_frac.numerator, right_frac.denominator)).shift(level*DOWN).shift(shift + (right,0,0)*self.length)

        group = VGroup()
        group.add(line)
        group.add(text_left)
        group.add(text_right)
        return group


    def construct(self):
        left = LEFT*4
        right = RIGHT*4
        line = Line(left, right)
        self.play(Create(line))
        
        print(right, left)
        self.start = left
        self.end = right
        self.length = self.end - self.start
        
        text_range = MathTex("[0,1]").shift(UP)
        text_zero = MathTex("0").shift(UP*0.5).shift(left)
        text_one = MathTex("1").shift(UP*0.5).shift(right)
        group = VGroup()
        group.add(text_zero)
        group.add(text_one)
        self.play(Write(text_range))
        self.play(Transform(text_range,group))

        l = Fraction(0)
        r = Fraction(1)

        self.new_level(l,r,1)

