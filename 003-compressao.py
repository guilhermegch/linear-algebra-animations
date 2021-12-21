from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_003_compressao(Scene):
    def construct(self):
        linha1 = MarkupText("<b>Compressão sem perdas (lossless)</b>", font_size=20)
        linha2 = MarkupText(
            "- Mesma qualidade que o original",
            font_size=20,
        )
        linha3 = MarkupText(
            "- Informação totalmente recuperada",
            font_size=20,
        )
        linha4 = MarkupText(
            "- Dados médicos, científicos, imagens RAW, etc.",
            font_size=20,
        )

        grupo1 = VGroup(linha1, linha2, linha3, linha4).arrange(DOWN)

        self.play(Write(grupo1))
        self.wait()

        self.play(FadeOut(grupo1))

        vetor1 = MathTex(
            "(22\ 23\ 24\ 24\ 24\ 24\ 24\ 24\ 24\ 25\ 26\ 26\ 26\ 26\ 26\ 26\ 25)"
        ).scale(0.8)
        texto_vetor1 = Text("34 bytes", font_size=20).next_to(vetor1, RIGHT)

        vetor2 = (
            MathTex(
                "(22\ 23\ ",
                "\\text{ff}\ 24\ ",
                "07\ ",
                "25\ ",
                "\\text{ff}\ 26\ ",
                "06\ ",
                "25)",
            )
            .scale(0.8)
            .next_to(vetor1, DOWN)
        )
        vetor2.set_color_by_tex("ff", RED)
        vetor2.set_color_by_tex("07", YELLOW)
        vetor2.set_color_by_tex("06", YELLOW)
        texto_vetor2 = Text("20 bytes", font_size=20).next_to(vetor2, RIGHT)

        self.play(FadeIn(vetor1, texto_vetor1))

        self.wait(1)
        self.play(Write(vetor2))
        self.play(Write(texto_vetor2))

        texto_reducao = Text("Redução de 43,75%", font_size=30).next_to(vetor2, DOWN)

        self.play(FadeIn(texto_reducao))

        self.wait(1)

        grupo2 = Group(vetor1, vetor2, texto_vetor1, texto_vetor2, texto_reducao)

        self.play(FadeOut(grupo2))

        perdas_linha1 = MarkupText("<b>Compressão com perdas (lossy)</b>", font_size=20)
        perdas_linha2 = MarkupText(
            "- Qualidade menor que a original",
            font_size=20,
        )
        perdas_linha3 = MarkupText(
            "- Informação perdida",
            font_size=20,
        )
        perdas_linha4 = MarkupText(
            "- Fotos do Instagram, vídeo da Netflix, música no Spotify, etc.",
            font_size=20,
        )

        grupo3 = VGroup(
            perdas_linha1, perdas_linha2, perdas_linha3, perdas_linha4
        ).arrange(DOWN)

        self.play(Write(grupo3))

        self.wait(2)
