from math import sqrt
from os import WEXITED, write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_004_algoritmos_compressao(Scene):
    def construct(self):
        linha1 = MarkupText("<b>Algoritmos de compressão</b>", font_size=20)

        linha2 = Text("- Frequência de caracteres", font_size=20).next_to(linha1, DOWN)
        linha3 = Text("- Huffman", font_size=20).next_to(linha2, DOWN)
        linha4 = Text("- LZW (GIF)", font_size=20).next_to(linha3, DOWN)
        linha5 = Text(
            "- DWT: Transformada Discreta de Wavelet (JPEG2000)", font_size=20
        ).next_to(linha4, DOWN)
        linha6 = Text("- Transformada Discreta do Cosseno (DCT)", font_size=20).next_to(
            linha5, DOWN
        )
        linha7 = Text("- SVD", font_size=20).next_to(linha6, DOWN)

        grupo1 = VGroup(linha1, linha2, linha3, linha4, linha5, linha6, linha7).arrange(
            DOWN
        )

        self.play(Write(grupo1))

        self.wait(2)
