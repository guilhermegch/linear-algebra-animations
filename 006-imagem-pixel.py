from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy import mat
from numpy.lib.function_base import angle
from rich.console import group


class svd_006_imagem_pixel(Scene):
    def construct(self):
        matriz_pb = IntegerMatrix(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 70, 70, 0, 70, 70, 0, 0, 0],
                [0, 0, 70, 220, 220, 70, 220, 220, 70, 0, 0],
                [0, 70, 220, 130, 130, 220, 130, 130, 220, 70, 0],
                [0, 70, 220, 130, 130, 130, 130, 130, 220, 70, 0],
                [0, 0, 70, 220, 130, 130, 130, 220, 70, 0, 0],
                [0, 0, 0, 70, 220, 130, 220, 70, 0, 0, 0],
                [0, 0, 0, 0, 70, 220, 70, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 70, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )

        self.play(FadeIn(matriz_pb))
        self.wait(2)
        self.play(FadeOut(matriz_pb))

        matriz_r = IntegerMatrix(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )

        ent_r = matriz_r.get_entries()

        for k in ent_r:
            if k.get_value() == 1:
                k.set_color("#ff0000")

        matriz_g = IntegerMatrix(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )

        ent_g = matriz_g.get_entries()

        for k in ent_g:
            if k.get_value() == 1:
                k.set_color("#00ff00")

        matriz_b = IntegerMatrix(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )

        ent_b = matriz_b.get_entries()

        for k in ent_b:
            if k.get_value() == 1:
                k.set_color("#0000ff")

        matriz_r.save_state()
        matriz_g.save_state()
        matriz_b.save_state()

        self.play(FadeIn(matriz_r))
        self.wait(1)
        # self.play(FadeOut(matriz_r), FadeIn(matriz_g))
        self.play(ReplacementTransform(matriz_r, matriz_g))
        self.wait(1)
        # self.play(FadeOut(matriz_g), FadeIn(matriz_b))
        self.play(Transform(matriz_g, matriz_b))
        self.wait(1)
        self.play(FadeOut(matriz_b))

        matriz_r.restore()
        matriz_g.restore()
        matriz_b.restore()

        grupo1 = Group(matriz_r, matriz_g, matriz_b)
        grupo1.scale(0.3)

        matriz_r.to_corner(LEFT)
        matriz_g.next_to(matriz_r, RIGHT)
        matriz_b.next_to(matriz_g, RIGHT)

        self.play(FadeIn(grupo1))

        self.wait(2)
