from math import sqrt
from os import WEXITED, write
from manim import *
from manim.utils import tex
from manim.utils.family_ops import restructure_list_to_exclude_certain_family_members
from numpy.lib.function_base import angle


class svd_002_dsn(Scene):
    def construct(self):
        linha1 = MarkupText("<b>Missões que utilizam a DSN</b>", font_size=20)

        self.play(Write(linha1))
        self.play(linha1.animate.to_corner(UP * 2))
        self.wait()

        texto1 = (
            Tex(
                r"ACE, AIRS, Akatsuki (PLC), Argomoon, ARTEMIS, Astrobotic, Bepi-Columbo, BioSentinel, Cislunar Autonomous Positioning System Technology, Chandra X-Ray Observatory, Chandrayaan-2, Cluster 2, Cubesat for the observation of Solar Particles (CuSP), CU-E3, Deep Space Climate Observatory (DSCOVR), Double Asteroid Redirection Test (DART), Dragonfly, ECOSTRESS, Emirates Mars Mission (EMM), EQUULEUS, Europa Clipper, ExoMars Trace Gas Orbiter (TGO), ExoMars Rover/Surface Platform (RSP), Artemis I, Artemis II, Artemis III, Exploration Upper Stage (EUS), Gaia, Geotail, Hayabusa-2, Hubble, Human Landing System (HLS), International Gamma-Ray Astrophysics Laboratory (INTEGRAL), Interstellar Mapping and Accerleration Probe (IMAP), InSight, Jason-3, JUNO, Jupiter Icy Moons Explorer (JUICE), JWST, KPLO, LRO, Light Italian Cubesat for Imagaing of Asteroids (LICIAcube), Lucy, Lunar Flashlight, Lunar Hydrogen Mapper, Lunar Ice Cube, Magnetospheric MultiScale (MMS1,2,3,4), Mars '01 Odyssey, Mars 2020, MAVEN, Mars Express Orbiter (MEX), Mars Orbiter Mission (MOM), Mars Reconnaissance Orbiter (MRO), Mars Science Laboratory (MSL), Multi-Angle Imager for Aerosols (MAIA), NASA-ISRO SAR (NISAR), Near Earth Asteroid Scout, New Horizons Pluto-Charon, Orbiting Carbon Observatory 2 (OCO2), Orbiting Carbon Observatory 3 (OCO3), OMOTENASHI, OSIRIS-REx, Parker Solar Probe (SPP), Power and Propulsion Element (PPE) of NASA's Lunar Gateway, Psyche, Sentinel-6, SOHO, Soil Moisture Active/Passive (SMAP), Spectro-Photometer for the History of the Universe, Epoch of Reionization and Ices Explorer (SPHEREx), STEREO Ahead, Sun Radio Interferometer Space Experiment (SunRISE), Surface Water Ocean Topography (SWOT), Team Miles, Transiting Exoplanet Survey Satellite (TESS) Volitiles investigating Polar Exploration Rover (VIPER), Voyager 1 \& 2, WIND, X-ray Multi-Mirror Mission (XMM), WFIRST",
                font_size=18,
                width=350,
            ).next_to(linha1, DOWN)
            # .scale(0.8)
        )

        self.play(FadeIn(texto1))

        self.wait(2)
