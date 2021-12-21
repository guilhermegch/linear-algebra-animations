from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_019_final(Scene):
    def construct(self):
        linha1 = MarkupText("<b>Obrigado!!</b>", font_size=20)

        self.play(Write(linha1))
        self.wait(4)
