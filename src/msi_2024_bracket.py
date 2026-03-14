"""Implémentation de la classe MSI2024Bracket."""

import random as rd

from .equipe import Equipe
from .match import Match
from .phase import Phase


class MSI2024Bracket(Phase):
    """Phase finale du MSI 2024.

    Parameters
    ----------
    equipes = dict[str, Equipe]
        Équipes participant à la phase finale.
    """

    @property
    def _CHAPEAUX(self) -> dict[str, set[str]]:
        chapeaux = {
            "Chapeau 1": {"KR #1", "CN #1"},
            "Chapeau 2": {"EMEA #1", "NA #1"},
            "Chapeau 3": {"Play-In #1", "Play-In #2"},
            "Chapeau 4": {"Play-In #3", "Play-In #4"},
        }
        return chapeaux

    @property
    def _TABLEAU_VIDE(self) -> dict[str, dict[str, Match]]:
        tableau_vide = {
            "Tour 1": {
                "Match 1": Match(best_of=5),
                "Match 2": Match(best_of=5),
                "Match 3": Match(best_of=5),
                "Match 4": Match(best_of=5),
                "Match 5": Match(best_of=5),
                "Match 6": Match(best_of=5),
            },
            "Tour 2": {
                "Match 1": Match(best_of=5),
                "Match 2": Match(best_of=5),
                "Match 3": Match(best_of=5),
                "Match 4": Match(best_of=5),
            },
            "Tour 3": {
                "Match 1": Match(best_of=5),
            },
            "Tour 4": {
                "Match 1": Match(best_of=5),
                "Match 2": Match(best_of=5),
            },
            "Tour 5": {
                "Match 1": Match(best_of=5),
            },
        }
        return tableau_vide

    def _simuler_tirage(self) -> None:
        """Permet de simuler le tirage des Brackets"""
        ind: list[int] = [rd.randint(0, 1) for _ in range(4)]

        # Chapeau 1
        self._tableau["Tour 1"]["Match 1"].ajouter_equipe_1(self._chapeaux_equipes["Chapeau 1"][ind[0]])
        self._tableau["Tour 1"]["Match 4"].ajouter_equipe_1(self._chapeaux_equipes["Chapeau 1"][abs(ind[0] - 1)])

        # Chapeau 2
        region_3: set[str] = {
            self._chapeaux_equipes["Chapeau 3"][0].region,
            self._chapeaux_equipes["Chapeau 3"][1].region,
        }
        region_4: set[str] = {
            self._chapeaux_equipes["Chapeau 4"][0].region,
            self._chapeaux_equipes["Chapeau 4"][1].region,
        }
        if (
            (
                self._chapeaux_equipes["Chapeau 1"][ind[0]].region in region_3
                and self._chapeaux_equipes["Chapeau 2"][ind[1]].region in region_3
            )
            or (
                self._chapeaux_equipes["Chapeau 1"][abs(ind[0] - 1)].region in region_3
                and self._chapeaux_equipes["Chapeau 2"][abs(ind[1] - 1)].region in region_3
            )
            or (
                self._chapeaux_equipes["Chapeau 1"][ind[0]].region in region_4
                and self._chapeaux_equipes["Chapeau 2"][ind[1]].region in region_4
            )
            or (
                self._chapeaux_equipes["Chapeau 1"][abs(ind[0] - 1)].region in region_4
                and self._chapeaux_equipes["Chapeau 2"][abs(ind[1] - 1)].region in region_4
            )
        ):
            self._tableau["Tour 1"]["Match 3"].ajouter_equipe_1(self._chapeaux_equipes["Chapeau 2"][ind[1]])
            self._tableau["Tour 1"]["Match 2"].ajouter_equipe_1(self._chapeaux_equipes["Chapeau 2"][abs(ind[1] - 1)])
        else:
            self._tableau["Tour 1"]["Match 2"].ajouter_equipe_1(self._chapeaux_equipes["Chapeau 2"][ind[1]])
            self._tableau["Tour 1"]["Match 3"].ajouter_equipe_1(self._chapeaux_equipes["Chapeau 2"][abs(ind[1] - 1)])

        # Chapeau 3
        region_part1: set[str] = (
            self._tableau["Tour 1"]["Match 1"].renvoyer_regions_equipes()
            | self._tableau["Tour 1"]["Match 2"].renvoyer_regions_equipes()
        )
        region_part2: set[str] = (
            self._tableau["Tour 1"]["Match 3"].renvoyer_regions_equipes()
            | self._tableau["Tour 1"]["Match 4"].renvoyer_regions_equipes()
        )
        if (self._chapeaux_equipes["Chapeau 3"][ind[2]].region in region_part1) or (
            self._chapeaux_equipes["Chapeau 3"][abs(ind[2] - 1)].region in region_part2
        ):
            self._tableau["Tour 1"]["Match 3"].ajouter_equipe_2(self._chapeaux_equipes["Chapeau 3"][ind[2]])
            self._tableau["Tour 1"]["Match 2"].ajouter_equipe_2(self._chapeaux_equipes["Chapeau 3"][abs(ind[2] - 1)])
        else:
            self._tableau["Tour 1"]["Match 2"].ajouter_equipe_2(self._chapeaux_equipes["Chapeau 3"][ind[2]])
            self._tableau["Tour 1"]["Match 3"].ajouter_equipe_2(self._chapeaux_equipes["Chapeau 3"][abs(ind[2] - 1)])

        # Chapeau 4
        if (self._chapeaux_equipes["Chapeau 4"][ind[3]].region in region_part1) or (
            self._chapeaux_equipes["Chapeau 4"][abs(ind[3] - 1)].region in region_part2
        ):
            self._tableau["Tour 1"]["Match 4"].ajouter_equipe_2(self._chapeaux_equipes["Chapeau 4"][ind[3]])
            self._tableau["Tour 1"]["Match 1"].ajouter_equipe_2(self._chapeaux_equipes["Chapeau 4"][abs(ind[3] - 1)])
        else:
            self._tableau["Tour 1"]["Match 1"].ajouter_equipe_2(self._chapeaux_equipes["Chapeau 4"][ind[3]])
            self._tableau["Tour 1"]["Match 4"].ajouter_equipe_2(self._chapeaux_equipes["Chapeau 4"][abs(ind[3] - 1)])

    def __simuler_tour_1_matchs_1_a_4(self) -> None:
        """Permet de simuler les matchs 1 à 4 du tour 1 et prépare les prochains matchs"""
        self._tableau["Tour 1"]["Match 1"].simuler()
        self._tableau["Tour 1"]["Match 2"].simuler()
        self._tableau["Tour 1"]["Match 3"].simuler()
        self._tableau["Tour 1"]["Match 4"].simuler()

        self._tableau["Tour 2"]["Match 1"].ajouter_equipes(
            self._tableau["Tour 1"]["Match 1"].renvoyer_equipe_gagnante(),
            self._tableau["Tour 1"]["Match 2"].renvoyer_equipe_gagnante(),
        )
        self._tableau["Tour 2"]["Match 2"].ajouter_equipes(
            self._tableau["Tour 1"]["Match 3"].renvoyer_equipe_gagnante(),
            self._tableau["Tour 1"]["Match 4"].renvoyer_equipe_gagnante(),
        )
        self._tableau["Tour 1"]["Match 5"].ajouter_equipes(
            self._tableau["Tour 1"]["Match 1"].renvoyer_equipe_perdante(),
            self._tableau["Tour 1"]["Match 2"].renvoyer_equipe_perdante(),
        )
        self._tableau["Tour 1"]["Match 6"].ajouter_equipes(
            self._tableau["Tour 1"]["Match 3"].renvoyer_equipe_perdante(),
            self._tableau["Tour 1"]["Match 4"].renvoyer_equipe_perdante(),
        )

    def __simuler_tour_2_matchs_1_2(self) -> None:
        """Permet de simuler les matchs 1 et 2 du tour 2 et prépare les prochains matchs"""
        self._tableau["Tour 2"]["Match 1"].simuler()
        self._tableau["Tour 2"]["Match 2"].simuler()

        self._tableau["Tour 4"]["Match 1"].ajouter_equipes(
            self._tableau["Tour 2"]["Match 1"].renvoyer_equipe_gagnante(),
            self._tableau["Tour 2"]["Match 2"].renvoyer_equipe_gagnante(),
        )
        self._tableau["Tour 2"]["Match 3"].ajouter_equipe_1(
            self._tableau["Tour 2"]["Match 1"].renvoyer_equipe_perdante()
        )
        self._tableau["Tour 2"]["Match 4"].ajouter_equipe_1(
            self._tableau["Tour 2"]["Match 2"].renvoyer_equipe_perdante()
        )

    def __simuler_tour_1_matchs_5_6(self) -> None:
        """Permet de simuler les matchs 5 et 6 du tour 1 et prépare les prochains matchs"""
        self._tableau["Tour 1"]["Match 5"].simuler()
        self._tableau["Tour 1"]["Match 6"].simuler()

        self._tableau["Tour 2"]["Match 3"].ajouter_equipe_2(
            self._tableau["Tour 1"]["Match 5"].renvoyer_equipe_gagnante()
        )
        self._tableau["Tour 2"]["Match 4"].ajouter_equipe_2(
            self._tableau["Tour 1"]["Match 6"].renvoyer_equipe_gagnante()
        )

    def __simuler_tour_2_matchs_3_4(self) -> None:
        """Permet de simuler les matchs 3 et 4 du tour 2 et prépare les prochains matchs"""
        self._tableau["Tour 2"]["Match 3"].simuler()
        self._tableau["Tour 2"]["Match 4"].simuler()

        self._tableau["Tour 3"]["Match 1"].ajouter_equipes(
            self._tableau["Tour 2"]["Match 3"].renvoyer_equipe_gagnante(),
            self._tableau["Tour 2"]["Match 4"].renvoyer_equipe_gagnante(),
        )

    def __simuler_tour_4_match_1(self) -> None:
        """Permet de simuler le match 1 du tour 4 et prépare les prochains matchs"""
        self._tableau["Tour 4"]["Match 1"].simuler()

        self._tableau["Tour 5"]["Match 1"].ajouter_equipe_1(
            self._tableau["Tour 4"]["Match 1"].renvoyer_equipe_gagnante()
        )
        self._tableau["Tour 4"]["Match 2"].ajouter_equipe_1(
            self._tableau["Tour 4"]["Match 1"].renvoyer_equipe_perdante()
        )

    def __simuler_tour_3(self) -> None:
        """Permet de simuler le tour 3 et prépare les prochains matchs"""
        self._tableau["Tour 3"]["Match 1"].simuler()

        self._tableau["Tour 4"]["Match 2"].ajouter_equipe_2(
            self._tableau["Tour 3"]["Match 1"].renvoyer_equipe_gagnante()
        )

    def __simuler_tour_4_match_2(self) -> None:
        """Permet de simuler le match 2 du tour 4 et prépare le prochain match"""
        self._tableau["Tour 4"]["Match 2"].simuler()

        self._tableau["Tour 5"]["Match 1"].ajouter_equipe_2(
            self._tableau["Tour 4"]["Match 2"].renvoyer_equipe_gagnante()
        )

    def __simuler_tour_5(self) -> None:
        """Permet de simuler le tour 5"""
        self._tableau["Tour 5"]["Match 1"].simuler()

    def _simuler_tours(self) -> None:
        """Permet de simuler tous les matchs des Brackets"""
        self.__simuler_tour_1_matchs_1_a_4()
        self.__simuler_tour_2_matchs_1_2()
        self.__simuler_tour_1_matchs_5_6()
        self.__simuler_tour_2_matchs_3_4()
        self.__simuler_tour_4_match_1()
        self.__simuler_tour_3()
        self.__simuler_tour_4_match_2()
        self.__simuler_tour_5()

    def renvoyer_classement(self) -> dict[str, set[Equipe]]:
        """Renvoie le classement des Brackets

        Returns
        -------
        classement : dict[str, set(Equipe)]
            Dictionnaire représentant le classement avec les clés repésentant les classements
            et les valeurs repésentant les équipes qui ont ce classement
        """
        classement: dict[str, set[Equipe]] = {}
        classement["1"] = {self._tableau["Tour 5"]["Match 1"].renvoyer_equipe_gagnante()}
        classement["2"] = {self._tableau["Tour 5"]["Match 1"].renvoyer_equipe_perdante()}
        classement["3"] = {self._tableau["Tour 4"]["Match 2"].renvoyer_equipe_perdante()}
        classement["4"] = {self._tableau["Tour 3"]["Match 1"].renvoyer_equipe_perdante()}
        classement["5-6"] = {
            self._tableau["Tour 2"]["Match 3"].renvoyer_equipe_perdante(),
            self._tableau["Tour 2"]["Match 4"].renvoyer_equipe_perdante(),
        }
        classement["7-8"] = {
            self._tableau["Tour 1"]["Match 5"].renvoyer_equipe_perdante(),
            self._tableau["Tour 1"]["Match 6"].renvoyer_equipe_perdante(),
        }
        return classement

    def renvoyer_resultats_str(self) -> str:
        """Renvoie les résultats sous la forme d'une chaîne de caractères.

        Returns
        -------
        str
            Chaîne de caractères présentant les résultats.
        """

        string_list = [
            "=================                                                          ",
            "PHASE 2 (BRACKET)                                                          ",
            "=================                                                          ",
            "                                                                           ",
            "                                                                           ",
            " —————————       —————————       —————————       —————————       ————————— ",
            "| TOUR 1  |     | TOUR 2  |     | TOUR 3  |     | TOUR 4  |     | TOUR 5  |",
            " —————————       —————————       —————————       —————————       ————————— ",
            "                                                                           ",
            " —————————                                                                 ",
            "| {!s:<3} | {} |                                                                ".format(
                self._tableau["Tour 1"]["Match 1"].equipe_1, self._tableau["Tour 1"]["Match 1"].score_equipe_1
            ),
            "|—————————|——                                                              ",
            "| {!s:<3} | {} |  |   —————————                                                 ".format(
                self._tableau["Tour 1"]["Match 1"].equipe_2, self._tableau["Tour 1"]["Match 1"].score_equipe_2
            ),
            " —————————    ——| {!s:<3} | {} |                                                ".format(
                self._tableau["Tour 2"]["Match 1"].equipe_1, self._tableau["Tour 2"]["Match 1"].score_equipe_1
            ),
            "                |—————————|                                                ",
            " —————————    ——| {!s:<3} | {} |——                                              ".format(
                self._tableau["Tour 2"]["Match 1"].equipe_2, self._tableau["Tour 2"]["Match 1"].score_equipe_2
            ),
            "| {!s:<3} | {} |  |   —————————   |                                             ".format(
                self._tableau["Tour 1"]["Match 2"].equipe_1, self._tableau["Tour 1"]["Match 2"].score_equipe_1
            ),
            "|—————————|——                |                                             ",
            "| {!s:<3} | {} |                  |                   —————————                 ".format(
                self._tableau["Tour 1"]["Match 2"].equipe_2, self._tableau["Tour 1"]["Match 2"].score_equipe_2
            ),
            " —————————                    ——————————————————| {!s:<3} | {} |                ".format(
                self._tableau["Tour 4"]["Match 1"].equipe_1, self._tableau["Tour 4"]["Match 1"].score_equipe_1
            ),
            "                                                |—————————|——              ",
            " —————————                    ——————————————————| {!s:<3} | {} |  |             ".format(
                self._tableau["Tour 4"]["Match 1"].equipe_2, self._tableau["Tour 4"]["Match 1"].score_equipe_2
            ),
            "| {!s:<3} | {} |                  |                   —————————   |             ".format(
                self._tableau["Tour 1"]["Match 3"].equipe_1, self._tableau["Tour 1"]["Match 3"].score_equipe_1
            ),
            "|—————————|——                |                               |             ",
            "| {!s:<3} | {} |  |   —————————   |                               |             ".format(
                self._tableau["Tour 1"]["Match 3"].equipe_2, self._tableau["Tour 1"]["Match 3"].score_equipe_2
            ),
            " —————————    ——| {!s:<3} | {} |  |                               |             ".format(
                self._tableau["Tour 2"]["Match 2"].equipe_1, self._tableau["Tour 2"]["Match 2"].score_equipe_1
            ),
            "                |—————————|——                                |   ————————— ",
            " —————————    ——| {!s:<3} | {} |                                   ——| {!s:<3} | {} |".format(
                self._tableau["Tour 2"]["Match 2"].equipe_2,
                self._tableau["Tour 2"]["Match 2"].score_equipe_2,
                self._tableau["Tour 5"]["Match 1"].equipe_1,
                self._tableau["Tour 5"]["Match 1"].score_equipe_1,
            ),
            "| {!s:<3} | {} |  |   —————————                                      |—————————|".format(
                self._tableau["Tour 1"]["Match 4"].equipe_1, self._tableau["Tour 1"]["Match 4"].score_equipe_1
            ),
            "|—————————|——                                                 ——| {!s:<3} | {} |".format(
                self._tableau["Tour 5"]["Match 1"].equipe_2, self._tableau["Tour 5"]["Match 1"].score_equipe_2
            ),
            "| {!s:<3} | {} |                                                  |   ————————— ".format(
                self._tableau["Tour 1"]["Match 4"].equipe_2, self._tableau["Tour 1"]["Match 4"].score_equipe_2
            ),
            " —————————                                                   |             ",
            "             |   —————————                                   |             ",
            " —————————    ——| {!s:<3} | {} |                                  |             ".format(
                self._tableau["Tour 2"]["Match 3"].equipe_1, self._tableau["Tour 2"]["Match 3"].score_equipe_1
            ),
            "| {!s:<3} | {} |     |—————————|——                |   —————————   |             ".format(
                self._tableau["Tour 1"]["Match 5"].equipe_1, self._tableau["Tour 1"]["Match 5"].score_equipe_1
            ),
            "|—————————|—————| {!s:<3} | {} |  |   —————————    ——| {!s:<3} | {} |  |             ".format(
                self._tableau["Tour 2"]["Match 3"].equipe_2,
                self._tableau["Tour 2"]["Match 3"].score_equipe_2,
                self._tableau["Tour 4"]["Match 2"].equipe_1,
                self._tableau["Tour 4"]["Match 2"].score_equipe_1,
            ),
            "| {!s:<3} | {} |      —————————    ——| {!s:<3} | {} |     |—————————|——              ".format(
                self._tableau["Tour 1"]["Match 5"].equipe_2,
                self._tableau["Tour 1"]["Match 5"].score_equipe_2,
                self._tableau["Tour 3"]["Match 1"].equipe_1,
                self._tableau["Tour 3"]["Match 1"].score_equipe_1,
            ),
            " —————————                      |—————————|—————| {!s:<3} | {} |                ".format(
                self._tableau["Tour 4"]["Match 2"].equipe_2, self._tableau["Tour 4"]["Match 2"].score_equipe_2
            ),
            "             |   —————————    ——| {!s:<3} | {} |      —————————                 ".format(
                self._tableau["Tour 3"]["Match 1"].equipe_2, self._tableau["Tour 3"]["Match 1"].score_equipe_2
            ),
            " —————————    ——| {!s:<3} | {} |  |   —————————                                 ".format(
                self._tableau["Tour 2"]["Match 4"].equipe_1, self._tableau["Tour 2"]["Match 4"].score_equipe_1
            ),
            "| {!s:<3} | {} |     |—————————|——                                              ".format(
                self._tableau["Tour 1"]["Match 6"].equipe_1, self._tableau["Tour 1"]["Match 6"].score_equipe_1
            ),
            "|—————————|—————| {!s:<3} | {} |                                                ".format(
                self._tableau["Tour 2"]["Match 4"].equipe_2, self._tableau["Tour 2"]["Match 4"].score_equipe_2
            ),
            "| {!s:<3} | {} |      —————————                                                 ".format(
                self._tableau["Tour 1"]["Match 6"].equipe_2, self._tableau["Tour 1"]["Match 6"].score_equipe_2
            ),
            " —————————                                                                 ",
        ]

        return "\n".join(string_list)
