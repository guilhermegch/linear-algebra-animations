from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_009_svd_matriz_a(Scene):
    def construct(self):

        texto1 = Text("A matemática por trás da SVD")

        self.play(Write(texto1))
        self.wait(1)

        self.play(FadeOut(texto1))
        self.wait()

        equacao = MathTex("A =", "U \\Sigma V^T")

        self.play(Write(equacao))

        self.wait(2)

        equacao_indices = MathTex(
            "A_{m \\times n} =",
            "U_{m \\times m}" "\\Sigma_{m \\times n} V^T_{n \\times n}",
        )

        self.play(ReplacementTransform(equacao, equacao_indices))

        self.wait(1)

        self.play(FadeOut(equacao_indices))

        matriz_a = MathTex(
            r"A_{m \times n} = \begin{bmatrix} | & | &  & | \\ a_1 & a_2 & \cdots & a_n\\ | & | &  & |  \end{bmatrix}"
        )

        self.play(Write(matriz_a))

        self.wait(2)
