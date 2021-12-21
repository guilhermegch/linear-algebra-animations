from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy import mat
from numpy.lib.function_base import angle
from rich.console import group


class svd_005_imagem_matriz(Scene):
    def construct(self):
        texto = Text("Imagem")
        rect1 = Rectangle(color=WHITE, width=5.0, height=5.5)
        rect2 = Rectangle(
            color=WHITE, width=5.0, height=5.5, grid_xstep=0.5, grid_ystep=0.5
        )
        self.play(FadeIn(texto), Write(rect1))
        self.wait(1)

        largura = Text("10 pixels", font_size=20).next_to(rect1, DOWN)
        altura = Text("11 pixels", font_size=20).next_to(rect1, RIGHT)

        self.play(Write(largura), Write(altura))

        self.wait(3)

        self.play(FadeOut(texto), ReplacementTransform(rect1, rect2))
        self.wait(2)
        matriz_img = MathTex(r"Imagem_{10 \times 11}")
        self.play(FadeOut(largura, altura), Transform(rect2, matriz_img))
        self.wait(2)
