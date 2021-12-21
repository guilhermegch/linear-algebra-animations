from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_012_svd_matriz_uev(Scene):
    def construct(self):

        matriz_u = MathTex(
            r"""U_{m \times m} = \begin{bmatrix} 
            | & | &  & | \\ 
            u_1 & u_2 & \cdots & u_m \\
            | & | &  & | \\
            \end{bmatrix}"""
        )

        matriz_v = MathTex(
            r"""V_{n \times n} = \begin{bmatrix} 
            | & | &  & | \\ 
            v_1 & v_2 & \cdots & v_n \\
            | & | &  & | \\
            \end{bmatrix}"""
        )

        grupo1 = VGroup(matriz_u, matriz_v).arrange(DOWN)

        self.play(Write(grupo1))

        self.wait(2)
