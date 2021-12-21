from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_015_svd_expansao(Scene):
    def construct(self):

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

        self.play(FadeIn(grupo1))
        self.wait(2)

        soma = MathTex(
            r"A = u_1 \sigma_1 v_1 + u_2 \sigma_2 v_2 + u_3 \sigma_3 v_3 + \cdots + u_n \sigma_n v_n + 0 + 0 + 0 + \cdots"
        ).scale(0.7)

        soma_matriz = MathTex(
            r"""A = 
            \begin{bmatrix} | \\ u_1 \\ | \end{bmatrix}\sigma_1 \begin{bmatrix} - & v_1 & - \end{bmatrix}
            + \begin{bmatrix} | \\ u_2 \\ | \end{bmatrix}\sigma_2 \begin{bmatrix} - & v_2 & - \end{bmatrix}
            + \cdots
            + \begin{bmatrix} | \\ u_n \\ | \end{bmatrix}\sigma_n \begin{bmatrix} - & v_n & - \end{bmatrix}
            """
        ).scale(0.6)

        self.play(ReplacementTransform(grupo1, soma_matriz))
        self.wait(2)
        self.play(ReplacementTransform(soma_matriz, soma))

        self.wait(2)
