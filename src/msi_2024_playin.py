"""Implémentation de la classe MSI2024PlayIn."""

import random as rd

from .equipe import Equipe
from .match import Match
from .phase import Phase


class MSI2024PlayIn(Phase):
    """Play-In (qualifications) du MSI 2024.

    Parameters
    ----------
    equipes = dict[str, Equipe]
        Équipes participant aux qualifications.
    """

    @property
    def _CHAPEAUX(self) -> dict[str, set[str]]:
        chapeaux = {
            "Chapeau 1": {"KR #2", "CN #2"},
            "Chapeau 2": {"EMEA #2", "NA #2"},
            "Chapeau 3": {"APAC #1", "VN #1"},
            "Chapeau 4": {"LAT #1", "BR #1"},
        }
        return chapeaux

    @property
    def _TABLEAU_VIDE(self) -> dict[str, dict[str, dict[str, Match]]]:
        tableau_vide = {
            "Groupe A": {
                "Tour 1": {
                    "Match 1": Match(best_of=3),
                    "Match 2": Match(best_of=3),
                    "Match 3": Match(best_of=3),
                },
                "Tour 2": {
                    "Match 1": Match(best_of=3),
                    "Match 2": Match(best_of=3),
                },
            },
            "Groupe B": {
                "Tour 1": {
                    "Match 1": Match(best_of=3),
                    "Match 2": Match(best_of=3),
                    "Match 3": Match(best_of=3),
                },
                "Tour 2": {
                    "Match 1": Match(best_of=3),
                    "Match 2": Match(best_of=3),
                },
            },
        }
        return tableau_vide

    def _simuler_tirage(self) -> None:
        """Permet de simuler le tirage du PlayIn"""
        ind: list[int] = [rd.randint(0, 1) for _ in range(4)]
        self._tableau["Groupe A"]["Tour 1"]["Match 1"].ajouter_equipe_1(self._chapeaux_equipes["Chapeau 1"][ind[0]])
        self._tableau["Groupe B"]["Tour 1"]["Match 1"].ajouter_equipe_1(
            self._chapeaux_equipes["Chapeau 1"][abs(ind[0] - 1)]
        )
        self._tableau["Groupe A"]["Tour 1"]["Match 2"].ajouter_equipe_1(self._chapeaux_equipes["Chapeau 2"][ind[1]])
        self._tableau["Groupe B"]["Tour 1"]["Match 2"].ajouter_equipe_1(
            self._chapeaux_equipes["Chapeau 2"][abs(ind[1] - 1)]
        )
        self._tableau["Groupe A"]["Tour 1"]["Match 2"].ajouter_equipe_2(self._chapeaux_equipes["Chapeau 3"][ind[2]])
        self._tableau["Groupe B"]["Tour 1"]["Match 2"].ajouter_equipe_2(
            self._chapeaux_equipes["Chapeau 3"][abs(ind[2] - 1)]
        )
        self._tableau["Groupe A"]["Tour 1"]["Match 1"].ajouter_equipe_2(self._chapeaux_equipes["Chapeau 4"][ind[3]])
        self._tableau["Groupe B"]["Tour 1"]["Match 1"].ajouter_equipe_2(
            self._chapeaux_equipes["Chapeau 4"][abs(ind[3] - 1)]
        )

    def __simuler_tour_1_matchs_1_2(self) -> None:
        """Permet de simuler les matchs 1 et 2 du tour 1 et prépare les prochains matchs"""
        self._tableau["Groupe A"]["Tour 1"]["Match 1"].simuler()
        self._tableau["Groupe A"]["Tour 1"]["Match 2"].simuler()
        self._tableau["Groupe B"]["Tour 1"]["Match 1"].simuler()
        self._tableau["Groupe B"]["Tour 1"]["Match 2"].simuler()

        self._tableau["Groupe A"]["Tour 2"]["Match 1"].ajouter_equipes(
            self._tableau["Groupe A"]["Tour 1"]["Match 1"].renvoyer_equipe_gagnante(),
            self._tableau["Groupe A"]["Tour 1"]["Match 2"].renvoyer_equipe_gagnante(),
        )
        self._tableau["Groupe B"]["Tour 2"]["Match 1"].ajouter_equipes(
            self._tableau["Groupe B"]["Tour 1"]["Match 1"].renvoyer_equipe_gagnante(),
            self._tableau["Groupe B"]["Tour 1"]["Match 2"].renvoyer_equipe_gagnante(),
        )
        self._tableau["Groupe A"]["Tour 1"]["Match 3"].ajouter_equipes(
            self._tableau["Groupe A"]["Tour 1"]["Match 1"].renvoyer_equipe_perdante(),
            self._tableau["Groupe A"]["Tour 1"]["Match 2"].renvoyer_equipe_perdante(),
        )
        self._tableau["Groupe B"]["Tour 1"]["Match 3"].ajouter_equipes(
            self._tableau["Groupe B"]["Tour 1"]["Match 1"].renvoyer_equipe_perdante(),
            self._tableau["Groupe B"]["Tour 1"]["Match 2"].renvoyer_equipe_perdante(),
        )

    def __simuler_tour_2_matchs_1(self) -> None:
        """Permet de simuler les matchs 1 du tour 2 et prépare les prochains matchs"""
        self._tableau["Groupe A"]["Tour 2"]["Match 1"].simuler()
        self._tableau["Groupe B"]["Tour 2"]["Match 1"].simuler()

        self._tableau["Groupe A"]["Tour 2"]["Match 2"].ajouter_equipe_1(
            self._tableau["Groupe A"]["Tour 2"]["Match 1"].renvoyer_equipe_perdante()
        )
        self._tableau["Groupe B"]["Tour 2"]["Match 2"].ajouter_equipe_1(
            self._tableau["Groupe B"]["Tour 2"]["Match 1"].renvoyer_equipe_perdante()
        )

    def __simuler_tour_1_matchs_3(self) -> None:
        """Permet de simuler les matchs 3 du tour 1 et prépare les prochains matchs"""
        self._tableau["Groupe A"]["Tour 1"]["Match 3"].simuler()
        self._tableau["Groupe B"]["Tour 1"]["Match 3"].simuler()

        self._tableau["Groupe A"]["Tour 2"]["Match 2"].ajouter_equipe_2(
            self._tableau["Groupe A"]["Tour 1"]["Match 3"].renvoyer_equipe_gagnante()
        )
        self._tableau["Groupe B"]["Tour 2"]["Match 2"].ajouter_equipe_2(
            self._tableau["Groupe B"]["Tour 1"]["Match 3"].renvoyer_equipe_gagnante()
        )

    def __simuler_tour_2_matchs_2(self) -> None:
        """Permet de simuler les matchs 2 du tour 2"""
        self._tableau["Groupe A"]["Tour 2"]["Match 2"].simuler()
        self._tableau["Groupe B"]["Tour 2"]["Match 2"].simuler()

    def _simuler_tours(self) -> None:
        """Permet de simuler tous les matchs du PlayIn"""
        self.__simuler_tour_1_matchs_1_2()
        self.__simuler_tour_2_matchs_1()
        self.__simuler_tour_1_matchs_3()
        self.__simuler_tour_2_matchs_2()

    def renvoyer_classement(self) -> dict[str, set[Equipe]]:
        """Renvoie le classement du PlayIn

        Returns
        -------
        classement : dict[str, set[Equipe]]
            Dictionnaire représentant le classement avec les clés repésentant les classements
            et les valeurs repésentant les équipes qui ont ce classement
        """
        classement: dict[str, set[Equipe]] = {}
        classement["1-2"] = {
            self._tableau["Groupe A"]["Tour 2"]["Match 1"].renvoyer_equipe_gagnante(),
            self._tableau["Groupe B"]["Tour 2"]["Match 1"].renvoyer_equipe_gagnante(),
        }
        classement["3-4"] = {
            self._tableau["Groupe A"]["Tour 2"]["Match 2"].renvoyer_equipe_gagnante(),
            self._tableau["Groupe B"]["Tour 2"]["Match 2"].renvoyer_equipe_gagnante(),
        }
        classement["5-6"] = {
            self._tableau["Groupe A"]["Tour 2"]["Match 2"].renvoyer_equipe_perdante(),
            self._tableau["Groupe B"]["Tour 2"]["Match 2"].renvoyer_equipe_perdante(),
        }
        classement["7-8"] = {
            self._tableau["Groupe A"]["Tour 1"]["Match 3"].renvoyer_equipe_perdante(),
            self._tableau["Groupe B"]["Tour 1"]["Match 3"].renvoyer_equipe_perdante(),
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
            "=================                                        ",
            "PHASE 1 (PLAY-IN)                                        ",
            "=================                                        ",
            "                                                         ",
            " ——————————                    ——————————                ",
            "| GROUPE A |                  | GROUPE B |               ",
            " ——————————                    ——————————                ",
            "                                                         ",
            " —————————       —————————     —————————       ————————— ",
            "| TOUR 1  |     | TOUR 2  |   | TOUR 1  |     | TOUR 2  |",
            " —————————       —————————     —————————       ————————— ",
            "                                                         ",
            " —————————                     —————————                 ",
            "| {!s:<3} | {} |                   | {!s:<3} | {} |                ".format(
                self._tableau["Groupe A"]["Tour 1"]["Match 1"].equipe_1,
                self._tableau["Groupe A"]["Tour 1"]["Match 1"].score_equipe_1,
                self._tableau["Groupe B"]["Tour 1"]["Match 1"].equipe_1,
                self._tableau["Groupe B"]["Tour 1"]["Match 1"].score_equipe_1,
            ),
            "|—————————|——                 |—————————|——              ",
            "| {!s:<3} | {} |  |   —————————    | {!s:<3} | {} |  |   ————————— ".format(
                self._tableau["Groupe A"]["Tour 1"]["Match 1"].equipe_2,
                self._tableau["Groupe A"]["Tour 1"]["Match 1"].score_equipe_2,
                self._tableau["Groupe B"]["Tour 1"]["Match 1"].equipe_2,
                self._tableau["Groupe B"]["Tour 1"]["Match 1"].score_equipe_2,
            ),
            " —————————    ——| {!s:<3} | {} |    —————————    ——| {!s:<3} | {} |".format(
                self._tableau["Groupe A"]["Tour 2"]["Match 1"].equipe_1,
                self._tableau["Groupe A"]["Tour 2"]["Match 1"].score_equipe_1,
                self._tableau["Groupe B"]["Tour 2"]["Match 1"].equipe_1,
                self._tableau["Groupe B"]["Tour 2"]["Match 1"].score_equipe_1,
            ),
            "                |—————————|                   |—————————|",
            " —————————    ——| {!s:<3} | {} |    —————————    ——| {!s:<3} | {} |".format(
                self._tableau["Groupe A"]["Tour 2"]["Match 1"].equipe_2,
                self._tableau["Groupe A"]["Tour 2"]["Match 1"].score_equipe_2,
                self._tableau["Groupe B"]["Tour 2"]["Match 1"].equipe_2,
                self._tableau["Groupe B"]["Tour 2"]["Match 1"].score_equipe_2,
            ),
            "| {!s:<3} | {} |  |   —————————    | {!s:<3} | {} |  |   ————————— ".format(
                self._tableau["Groupe A"]["Tour 1"]["Match 2"].equipe_1,
                self._tableau["Groupe A"]["Tour 1"]["Match 2"].score_equipe_1,
                self._tableau["Groupe B"]["Tour 1"]["Match 2"].equipe_1,
                self._tableau["Groupe B"]["Tour 1"]["Match 2"].score_equipe_1,
            ),
            "|—————————|——                 |—————————|——              ",
            "| {!s:<3} | {} |                   | {!s:<3} | {} |                ".format(
                self._tableau["Groupe A"]["Tour 1"]["Match 2"].equipe_2,
                self._tableau["Groupe A"]["Tour 1"]["Match 2"].score_equipe_2,
                self._tableau["Groupe B"]["Tour 1"]["Match 2"].equipe_2,
                self._tableau["Groupe B"]["Tour 1"]["Match 2"].score_equipe_2,
            ),
            " —————————                     —————————                 ",
            "             |   —————————                 |   ————————— ",
            " —————————    ——| {!s:<3} | {} |    —————————    ——| {!s:<3} | {} |".format(
                self._tableau["Groupe A"]["Tour 2"]["Match 2"].equipe_1,
                self._tableau["Groupe A"]["Tour 2"]["Match 2"].score_equipe_1,
                self._tableau["Groupe B"]["Tour 2"]["Match 2"].equipe_1,
                self._tableau["Groupe B"]["Tour 2"]["Match 2"].score_equipe_1,
            ),
            "| {!s:<3} | {} |     |—————————|   | {!s:<3} | {} |     |—————————|".format(
                self._tableau["Groupe A"]["Tour 1"]["Match 3"].equipe_1,
                self._tableau["Groupe A"]["Tour 1"]["Match 3"].score_equipe_1,
                self._tableau["Groupe B"]["Tour 1"]["Match 3"].equipe_1,
                self._tableau["Groupe B"]["Tour 1"]["Match 3"].score_equipe_1,
            ),
            "|—————————|—————| {!s:<3} | {} |   |—————————|—————| {!s:<3} | {} |".format(
                self._tableau["Groupe A"]["Tour 2"]["Match 2"].equipe_2,
                self._tableau["Groupe A"]["Tour 2"]["Match 2"].score_equipe_2,
                self._tableau["Groupe B"]["Tour 2"]["Match 2"].equipe_2,
                self._tableau["Groupe B"]["Tour 2"]["Match 2"].score_equipe_2,
            ),
            "| {!s:<3} | {} |      —————————    | {!s:<3} | {} |      ————————— ".format(
                self._tableau["Groupe A"]["Tour 1"]["Match 3"].equipe_2,
                self._tableau["Groupe A"]["Tour 1"]["Match 3"].score_equipe_2,
                self._tableau["Groupe B"]["Tour 1"]["Match 3"].equipe_2,
                self._tableau["Groupe B"]["Tour 1"]["Match 3"].score_equipe_2,
            ),
            " —————————                     —————————                 ",
        ]

        return "\n".join(string_list)
