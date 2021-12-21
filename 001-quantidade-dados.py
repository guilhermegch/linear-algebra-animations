from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_001_quantidade_dados(Scene):
    def construct(self):
        texto = Text("Full HD (1080p)")
        rect1 = Rectangle(color=WHITE, width=8.0, height=4.5)

        self.play(FadeIn(texto), Write(rect1))
        self.wait(1)

        rect1.save_state()

        largura = Text("1920 pixels", font_size=20).next_to(rect1, DOWN)
        altura = Text("1080 pixels", font_size=20).next_to(rect1, RIGHT)

        self.play(Write(largura), Write(altura))

        self.wait(1)

        self.play(
            FadeOut(largura, altura, texto),
            rect1.animate.scale(0.3),
        )
        self.play(
            rect1.animate.to_corner(LEFT),
        )
        self.wait()

        pixels = "1920 \\times 1080 = 2.079.600\ \\text{pixels/frame}"
        frames = "2.079.600\ \\text{pixels/frame} \\times 30\ \\text{frames/segundo} = 62.208.000\ \\text{pixels/segundo}"
        color_depth = (
            "8\ \\text{bits por cor} \\times 3\ \\text{cores (RGB)} = 24\ \\text{bits}"
        )
        banda = "62.208.000\ \\text{pixels/segundo} \\times 24\ \\text{bits/pixel}"
        resultado = "1.492.992.000\ \\text{bits/segundo}"
        resultado_comprimido = MathTex("\\approx 1,5\ \\text{gigabits/segundo}")

        conta = Tex(
            f"$${pixels}$$\\ $${frames}$$ \\ $${color_depth}$$ \\ $${banda}$$ \\ $${resultado}$$",
            font_size=30,
        ).next_to(rect1, RIGHT)

        self.play(Write(conta))
        self.wait(1)

        self.play(
            Restore(rect1),
            Transform(conta, resultado_comprimido),
            FadeIn(largura, altura),
        )
        self.wait(1)
