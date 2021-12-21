from math import prod, sqrt
from os import write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_016_svd_exemplo(Scene):
    def construct(self):

        matriz_a = MathTex(
            r"""\begin{bmatrix} 
            1 & 2 & 3 \\ 
            4 & 5 & 6 \\  
            \end{bmatrix}""",
            "=",
        ).save_state()

        matriz_u = MathTex(
            r"""\begin{bmatrix} 
            -0,3863 & -0,9224 \\ 
            -0,9224 & 0,3863  \\
            \end{bmatrix}"""
        )

        matriz_sigma = MathTex(
            r"""\begin{bmatrix} 
            9,5080 & 0 \\
            0 & 0,7729 \\
            \end{bmatrix}"""
        )

        matriz_v = MathTex(
            r"""\begin{bmatrix} 
            -0,4287 & 0,8060 \\
            -0,5663 & 0,1124 \\
            -0,7039 & -0,5812 \\
            \end{bmatrix}"""
        )

        grupo1 = (
            VGroup(matriz_a, matriz_u, matriz_sigma, matriz_v).arrange(RIGHT).scale(0.6)
        ).save_state()

        self.play(FadeIn(grupo1))
        self.wait(2)

        produto1 = MathTex(
            r"u_1 \sigma_1 v^T_1 =",
            r"""\begin{bmatrix} 
            -0,3863 & -0,9224 \\ 
            -0,9224 & 0,3863  \\
            \end{bmatrix}""",
            r"""\begin{bmatrix} 
            9,5080 & 0 \\
            0 & 0 \\
            \end{bmatrix}""",
            r"""\begin{bmatrix} 
            -0,4287 & -0,5663 & -0,7039 \\
            0,8060 & 0,1124 & -0,5812 \\
            \end{bmatrix}""",
        ).scale(0.6)

        self.play(
            ReplacementTransform(grupo1[0], produto1[0]),
            FadeTransform(grupo1[1], produto1[1]),
        )
        self.wait(0.5)
        self.play(ReplacementTransform(grupo1[2], produto1[2]))
        self.wait(0.5)
        self.play(ReplacementTransform(grupo1[3], produto1[3]))
        self.wait(2)

        resultado1 = MathTex(
            r"u_1 \sigma_1 v^T_1 =",
            r"""\begin{bmatrix}
            1,5745 && 2,0801 && 2,9857 \\
            3,7593 && 4,9664 && 6,1734 \\
            \end{bmatrix}""",
        ).save_state()

        self.play(FadeTransform(produto1, resultado1))
        self.wait(2)

        grupo1.restore()
        self.play(resultado1.animate.scale(0.4))
        self.play(resultado1.animate.to_corner(UP), FadeIn(grupo1))
        self.wait(2)

        produto2 = MathTex(
            r"u_2 \sigma_2 v^T_2 =",
            r"""\begin{bmatrix} 
            -0,3863 & -0,9224 \\ 
            -0,9224 & 0,3863  \\
            \end{bmatrix}""",
            r"""\begin{bmatrix} 
            0 & 0 \\
            0 & 0,7729 \\
            \end{bmatrix}""",
            r"""\begin{bmatrix} 
            -0,4287 & -0,5663 & -0,7039 \\
            0,8060 & 0,1124 & -0,5812 \\
            \end{bmatrix}""",
        ).scale(0.6)

        self.play(
            ReplacementTransform(grupo1[0], produto2[0]),
            FadeTransform(grupo1[1], produto2[1]),
        )
        self.wait(0.5)
        self.play(ReplacementTransform(grupo1[2], produto2[2]))
        self.wait(0.5)
        self.play(ReplacementTransform(grupo1[3], produto2[3]))
        self.wait(2)

        resultado2 = MathTex(
            r"u_2 \sigma_2 v^T_2 =",
            r"""\begin{bmatrix}
            -0,5745 && -0,081 && 0,0143 \\
            0,2406 && 0,0336 && -0,1735 \\
            \end{bmatrix}""",
        ).save_state()

        self.play(FadeTransform(produto2, resultado2))
        self.wait(2)
        self.play(resultado2.animate.shift(DOWN))
        self.play(resultado1.animate.restore().next_to(resultado2, UP))
        self.wait(2)
        self.play(FadeOut(resultado1, resultado2))

        resultado3 = MathTex(
            r"""\begin{bmatrix}
            1,5745 && 2,0801 && 2,9857 \\
            3,7593 && 4,9664 && 6,1734 \\
            \end{bmatrix}""",
            "+",
            r"""\begin{bmatrix}
            -0,5745 && -0,081 && 0,0143 \\
            0,2406 && 0,0336 && -0,1735 \\
            \end{bmatrix}""",
        ).scale(0.6)

        self.play(Write(resultado3))
        self.wait(2)

        self.play(Transform(resultado3, matriz_a.restore()[0]))
        self.wait(2)
