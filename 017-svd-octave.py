from math import prod, sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_017_svd_octave(Scene):
    def construct(self):

        code_path = "./code"

        octave_peb = Code(
            file_name=f"{code_path}/comprimir.m",
            tab_width=4,
            background="window",
            language="matlab",
        ).scale(0.6)

        self.play(Write(octave_peb))
        self.wait(2)
        self.play(FadeOut(octave_peb))
        self.wait(2)

        octave_colorido = Code(
            file_name=f"{code_path}/comprimir_colorido.m",
            tab_width=4,
            background="window",
            language="matlab",
        ).scale(0.6)

        self.play(Write(octave_colorido))
        self.wait(2)
        self.play(FadeOut(octave_colorido))
        self.wait(2)
