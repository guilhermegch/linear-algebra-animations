from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_013_svd_produto_matriz(Scene):
    def construct(self):

        equacao = MathTex("A =", "U \\Sigma V^T")

        self.play(Write(equacao))

        self.wait(2)

        matriz_a = MathTex(
            r"""\begin{bmatrix} 
            | & | &  & | \\ 
            a_1 & a_2 & \cdots & a_n \\ 
            | & | &  & | \\  
            \end{bmatrix} = """
        )

        matriz_sigma = MathTex(
            r"""\begin{bmatrix} 
            \sigma_1 & 0 & \cdots & 0 \\ 
            0 & \sigma_2 & \cdots & 0 \\
            \vdots & \vdots & \ddots & \vdots \\
            0 & 0 & \cdots & \sigma_n \\
            0 & 0 & \cdots & 0 \\
            \vdots & \vdots & \ddots & \vdots \\
            0 & 0 & \cdots & 0 \\
            \end{bmatrix}"""
        )
        matriz_u = MathTex(
            r"""\begin{bmatrix} 
            | & | &  & | \\ 
            u_1 & u_2 & \cdots & u_m \\
            | & | &  & | \\
            \end{bmatrix}"""
        )

        matriz_v = MathTex(
            r"""\begin{bmatrix} 
            - & v_1 & - \\ 
            - & v_2 & - \\ 
            - & v_3 & - \\ 
             & \vdots &  \\ 
            - & v_n & - \\ 
            \end{bmatrix}"""
        )

        grupo1 = (
            VGroup(matriz_a, matriz_u, matriz_sigma, matriz_v).arrange(RIGHT).scale(0.6)
        )

        self.play(ReplacementTransform(equacao, grupo1))
        self.wait(2)
        self.play(Wiggle(grupo1[3]))
        self.wait(2)
