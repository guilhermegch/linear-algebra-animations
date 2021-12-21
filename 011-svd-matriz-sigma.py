from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_011_svd_matriz_sigma(Scene):
    def construct(self):

        ordem_crescente = MathTex(
            r"\sigma_1 \geq \sigma_2 \geq \sigma_3 \geq \cdots \geq \sigma_n"
        )

        matriz_sigma = MathTex(
            r"""\Sigma_{m \times n} = \begin{bmatrix} 
            \sigma_1 & 0 & \cdots & 0 \\ 
            0 & \sigma_2 & \cdots & 0 \\
            \vdots & \vdots & \ddots & \vdots \\
            0 & 0 & \cdots & \sigma_n \\
            0 & 0 & \cdots & 0 \\
            \vdots & \vdots & \ddots & \vdots \\
            0 & 0 & \cdots & 0 \\
            \end{bmatrix}"""
        )

        grupo1 = VGroup(ordem_crescente, matriz_sigma).arrange(DOWN)

        self.play(Write(grupo1))

        self.wait(2)
