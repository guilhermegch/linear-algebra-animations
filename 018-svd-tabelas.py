from math import prod, sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_018_svd_tabelas(Scene):
    def construct(self):

        tabela_montanha = Tex(
            r"""
            \begin{tabular}{|c|c|c|}
            \hline
            \bf{Posto da matriz} & \bf{Tamanho (kb)} & \bf{Diferen\c{c}a} \\
            \hline
            Original & 470 & 0\% \\
            \hline
            Escala de cinza & 352 & 25,11\% \\
            \hline
            500 & 352 & 25,11\% \\
            \hline
            250 & 368 & 21,7\% \\
            \hline
            100 & 332 & 29,36\% \\
            \hline
            50 & 287 & 38,94\% \\
            \hline
            25 & 241 & 48,72\% \\
            \hline
            15 & 206 & 56,17\% \\
            \hline
            10 & 185 & 60,64\% \\
            \hline
            5 & 157 & 66,6\% \\
            \hline
            1 & 121 & 74,26\% \\
            \hline
	        \end{tabular}"""
        )

        tabela_windows = Tex(
            r"""\begin{tabular}{|c|c|c|}
            \hline
            \bf{Posto da matriz} & \bf{Tamanho (kb)} & \bf{Diferen\c{c}a} \\
            \hline
            Original & 1500 & 0,00\% \\
            \hline
            500 & 1100 & 26,67\% \\
            \hline
            250 & 1100 & 26,67\% \\
            \hline
            100 & 1003 & 33,13\% \\
            \hline
            50 & 866 & 42,27\% \\
            \hline
            25 & 725 & 51,67\% \\
            \hline
            15 & 659 & 56,07\% \\
            \hline
            10 & 611 & 59,27\% \\
            \hline
            5 & 560 & 62,67\% \\
            \hline
            1 & 421 & 71,93\% \\
            \hline
	        \end{tabular}"""
        )

        grupo1 = (
            VGroup(tabela_montanha, tabela_windows).arrange(RIGHT, buff=1).scale(0.4)
        )

        self.play(Create(grupo1))

        texto1 = Text("Montanhas", font_size=20).next_to(tabela_montanha, UP)
        texto2 = Text("Paisagem Windows", font_size=20).next_to(tabela_windows, UP)

        self.play(Write(texto1), Write(texto2))

        self.wait(2)
