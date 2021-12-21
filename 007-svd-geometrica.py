from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_007_svd_geometrica(Scene):
    def construct(self):
        ax = Axes(y_range=[-5, 5, 1], axis_config={"tick_size": 0})

        self.play(FadeIn(ax))

        self.wait()

        # circulo = ax.plot(lambda x: x ** 2, x_range=[0, 10])
        circulo = Circle(radius=2, color=DARK_BLUE)

        self.play(Write(circulo))

        self.wait()

        v1 = Vector([0, 2])
        v1label = MathTex("v_1").next_to(v1.get_center(), LEFT)

        v2 = Vector([2, 0])
        v2label = MathTex("v_2").next_to(v2.get_center(), UP)

        self.add(v1, v1label, v2, v2label)

        self.wait()

        elipse = Ellipse(width=6, height=3)

        u1 = Vector([0, 1.5])
        u1label = MathTex("\\sigma_1 u_1").next_to(u1.get_center(), LEFT)
        u2 = Vector([3, 0])
        u2label = MathTex("\\sigma_2 u_2").next_to(u2.get_center(), UP)

        self.play(
            FadeTransform(circulo, elipse),
            FadeTransform(v1, u1),
            FadeTransform(v2, u2),
            Transform(v1label, u1label),
            Transform(v2label, u2label),
        )
        self.wait()
        self.play(
            Rotate(elipse, PI / 6),
            Rotate(u1, PI / 6, about_point=ORIGIN),
            Rotate(u2, PI / 6, about_point=ORIGIN),
            Rotate(v1label, PI / 6, about_point=ORIGIN),
            Rotate(v2label, PI / 6, about_point=ORIGIN),
        )

        self.wait()
