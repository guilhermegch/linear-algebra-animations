from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_008_svd_aplicacoes(Scene):
    def construct(self):
        linha1 = MarkupText("<b>Aplicações da SVD</b>", font_size=20)

        self.play(Write(linha1))
        self.play(linha1.animate.to_corner(UP * 2))
        self.wait()

        aplicacoes = [
            "Resolução de equações lineares de matrizes Ax = B para uma matriz não quadrática",
            "Remoção de ruído em dados",
            "Caracterizar a geometria de entrada e de saída de uma transformação linear entre espaços vetoriais.",
            "Estatística: Análise de Componentes Principais (ACP) ou Principal Component Analysis (PCA)",
            "Ranking das pesquisas do Google",
            "Reconhecimento facial no Facebook",
            "Algoritmos de recomendação da Amazon e Netflix",
            "Simplificar o cálculo de formas bilineares",
        ]

        grupo = VGroup().next_to(linha1, DOWN)

        for x in aplicacoes:
            grupo.add(Text(f"- {x}", font_size=18))

        grupo.arrange(DOWN, buff=0.1)

        self.play(Write(grupo))
        self.wait(2)
