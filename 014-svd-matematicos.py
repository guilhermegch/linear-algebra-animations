from math import sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_014_svd_matematicos(Scene):
    def construct(self):
        linha1 = MarkupText("<b>Matemáticos da SVD</b>", font_size=20)

        self.play(Write(linha1))
        self.play(linha1.animate.to_corner(UP * 2))
        self.wait()

        imagens_path = "./images"

        beltrami = ImageMobject(f"{imagens_path}/beltrami.png")
        jordan = ImageMobject(f"{imagens_path}/jordan.png").scale(1.4)
        sylvester = ImageMobject(f"{imagens_path}/sylvester.png")
        schmidt = ImageMobject(f"{imagens_path}/schmidt.png")
        weyl = ImageMobject(f"{imagens_path}/weyl.png")

        grupo1 = Group(beltrami, jordan, sylvester, schmidt, weyl).arrange(
            RIGHT, buff=1.2
        )

        beltrami_txt = Text("Eugenio Beltrami", font_size=18).next_to(beltrami, DOWN)
        beltrami_ano = Text("(1835-1899)", font_size=18).next_to(beltrami_txt, DOWN)

        jordan_txt = Text("Camille Jordan", font_size=18).next_to(jordan, DOWN)
        jordan_ano = Text("(1838-1921)", font_size=18).next_to(jordan_txt, DOWN)

        sylvester_txt = Text("James Joseph", font_size=18).next_to(sylvester, DOWN)
        sylvester_txt2 = Text("Sylvester", font_size=18).next_to(sylvester_txt, DOWN)
        sylvester_ano = Text("(1814-1897)", font_size=18).next_to(sylvester_txt2, DOWN)

        schmidt_txt = Text("Erhard Schmidt", font_size=18).next_to(schmidt, DOWN)
        schmidt_ano = Text("(1876-1959)", font_size=18).next_to(schmidt_txt, DOWN)

        weyl_txt = Text("Hermann Weyl", font_size=18).next_to(weyl, DOWN)
        weyl_ano = Text("(1885-1955)", font_size=18).next_to(weyl_txt, DOWN)

        grupo2 = VGroup(
            beltrami_txt,
            jordan_txt,
            sylvester_txt,
            sylvester_txt2,
            schmidt_txt,
            weyl_txt,
        )
        grupo3 = VGroup(beltrami_ano, jordan_ano, sylvester_ano, schmidt_ano, weyl_ano)

        self.play(FadeIn(grupo1), Write(grupo2), Write(grupo3))
        self.wait(2)
        self.play(FadeOut(grupo1, grupo2, grupo3))

        linha2 = MarkupText("<b>Forma bilinear</b>", font_size=20).to_corner(UP * 2)

        forma_bilinear = MathTex("f(x,y) = x^T A y")
        forma_bilinear_matriz = MathTex("U^T A V = \Sigma").next_to(
            forma_bilinear, DOWN
        )

        self.play(
            FadeTransform(linha1, linha2),
            Write(forma_bilinear),
            Write(forma_bilinear_matriz),
        )

        self.wait(2)
