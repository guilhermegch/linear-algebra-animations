from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_010_svd_autovalores(Scene):
    def construct(self):

        eq1 = Tex(
            r"$$ A^TA = (U \Sigma V^T)^T (U \Sigma V^T) $$",
            r"$$ A^TA = V \Sigma U^T U \Sigma V^T $$",
            r"$$ A^TA = V \Sigma^2 V^T $$",
            r"$$ A^TAV =  V \Sigma^2 V^T V $$",
            r"$$ A^TAV =  V \Sigma^2$$",
        )

        eq2 = Tex(
            r"$$ AA^T = (U \Sigma V^T) (U \Sigma V^T)^T $$",
            r"$$ AA^T = U \Sigma V^T  V \Sigma U^T$$",
            r"$$ AA^T = U \Sigma^2 U^T $$",
            r"$$ AA^TU =  U \Sigma^2 U^T U $$",
            r"$$ AA^TU =  U \Sigma^2 $$",
        )

        grupo1 = VGroup(eq1, eq2).arrange(RIGHT, buff=0.5)

        self.play(Write(grupo1))
        self.wait(2)

        framebox1 = SurroundingRectangle(eq1[4], buff=0.1, color=RED)
        framebox2 = SurroundingRectangle(eq2[4], buff=0.1, color=RED)

        self.play(Create(framebox1), Create(framebox2))
        self.wait(1)

        eq3 = Tex(r"$$ A^TAV =  V \Sigma^2 $$", r"$$ B_1 V = \Sigma^2 V $$")

        eq4 = Tex(r"$$ AA^TU =  U \Sigma^2 $$", r"$$ B_2 U= \Sigma^2 U $$")

        grupo2 = VGroup(eq3, eq4).arrange(RIGHT, buff=0.5)

        framebox3 = SurroundingRectangle(eq3[0], buff=0.1, color=RED)
        framebox4 = SurroundingRectangle(eq4[0], buff=0.1, color=RED)

        self.play(
            FadeOut(grupo1, framebox1, framebox2), FadeIn(grupo2, framebox3, framebox4)
        )

        self.wait(2)
