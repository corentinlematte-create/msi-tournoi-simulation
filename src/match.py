"""Implémentation de la classe Match."""
from math import ceil
from random import randint

from .equipe import Equipe


class Match:
    """Classe modélisant un match.

    description.
    """

    def __init__(self, best_of):
        if best_of not in [1, 3, 5]:
            raise TypeError("best_of doit être parmis : 1,3,5")
        else:
            self.__best_of = best_of

        self.__equipe_1 = None
        self.__equipe_2 = None
        self.__score_equipe_1 = None
        self.__score_equipe_2 = None

    @property
    def best_of(self):
        return self.__best_of

    @property
    def equipe_1(self):
        return self.__equipe_1

    @property
    def equipe_2(self):
        return self.__equipe_2

    @property
    def score_equipe_1(self):
        return self.__score_equipe_1

    @property
    def score_equipe_2(self):
        return self.__score_equipe_2

    def __str__(self) -> str:
        eq1: str = "   "
        eq2: str = "   "
        score1: str = " "
        score2: str = " "
        if self.__equipe_1 is not None:
            eq1 = self.__equipe_1.nom_abreviation
        if self.__equipe_2 is not None:
            eq2 = self.__equipe_2.nom_abreviation
        if self.__score_equipe_1 is not None:
            score1 = str(self.__score_equipe_1)
        if self.__score_equipe_2 is not None:
            score2 = str(self.__score_equipe_2)
        bord = "-" * 11
        ligne1 = f"| {eq1:3} | {score1:1} |"
        ligne2 = f"| {eq2:3} | {score2:1} |"
        return f"{bord}\n{ligne1}\n{ligne2}\n{bord}"

    # def __str__(self):
    #     if (
    #         self.__equipe_1 is None and
    #         self.__equipe_2 is None and
    #         self.__score_equipe_1 is None and
    #         self.__score_equipe_2 is None
    #     ):
    #         return (
    #             "-----------\n"
    #             "|      |   |\n"
    #             "|      |   |\n"
    #             "-----------"
    #         )
    #     elif (
    #         self.__equipe_1 is None and
    #         self.__equipe_2 is None and
    #         self.__score_equipe_1 is not None and
    #         self.__score_equipe_2 is not None
    #     ):
    #         return (
    #             f"-----------\n"
    #             f"|         | {self.__score_equipe_1}  |\n"
    #             f"|         | {self.__score_equipe_2}  |\n"
    #             f"-----------"
    #         )
    #     elif (
    #         self.__equipe_1 is not None and
    #         self.__equipe_2 is None and
    #         self.__score_equipe_1 is None and
    #         self.__score_equipe_2 is None
    #     ):
    #         return (
    #             f"-----------\n"
    #             f"|   {self.__equipe_1}   | {self.__score_equipe_1}  |\n"
    #             f"|                       | {self.__score_equipe_2}  |\n"
    #             f"-----------"
    #         )

    def ajouter_equipe_1(self, equipe1):
        if self.__equipe_1 is not None:
            raise TypeError("equipe1 est déjà donné")
        elif type(equipe1) is not Equipe:
            raise TypeError("equipe1 doit être une équipe")
        elif self.__equipe_2 == equipe1:
            raise TypeError("equipe1 doit être une équipedifférente de equipe2")
        else:
            self.__equipe_1 = equipe1

    def ajouter_equipe_2(self, equipe2):
        if self.__equipe_2 is not None:
            raise TypeError("equipe2 est déjà donné")
        elif type(equipe2) is not Equipe:
            raise TypeError("equipe2 doit être une équipe")
        elif self.__equipe_1 == equipe2:
            raise TypeError("equipe2 doit être une équipedifférente de equipe1")
        else:
            self.__equipe_2 = equipe2

    def ajouter_equipes(self, equipe1, equipe2):
        self.ajouter_equipe_1(equipe1)
        self.ajouter_equipe_2(equipe1)

    def ajouter_score(self, score_equipe_1, score_equipe_2):
        if self.__equipe_2 is None or self.__equipe_2 is None:
            raise TypeError("les équipes doivent d'abord être inscrites")
        elif self.__score_equipe_1 is not None and self.__score_equipe_1 is not None:
            raise TypeError("les scores sont déjà donnés")
        elif type(score_equipe_1) is not int or type(score_equipe_2) is not int:
            raise TypeError("les scores doivent être des entiers positifs")
        elif score_equipe_1 + score_equipe_2 == self.best_of:
            raise ValueError("les scores doivent être cohérents avec le best_of")
        else:
            self.score_equipe_1 = score_equipe_1
            self.score_equipe_2 = score_equipe_2

    def ajouter_equipes_et_scores(self, equipe1, equipe2, score_equipe1, score_equipe2):
        self.ajouter_equipes(equipe1, equipe2)
        self.ajouter_score(score_equipe1, score_equipe2)

    def renvoyer_equipe_gagnante(self):
        if self.__score_equipe_1 is None or self.__score_equipe_2 is None:
            raise ValueError("les scores doivent être inscrits")
        elif self.__score_equipe2 < self.__score_equipe1:
            return self.__equipe1
        else:
            return self.__equipe2

    def renvoyer_equipe_perdante(self):
        if self.__score_equipe_1 is None or self.__score_equipe_2 is None:
            raise ValueError("les scores doivent être inscrits")
        elif self.__score_equipe_2 < self.__score_equipe_1:
            return self.__equipe_2
        else:
            return self.__equipe_1

    def renvoyer_regions_equipes(self):
        if self.__equipe_1 is None and self.__equipe_2 is None:
            return {}
        elif self.__equipe_1 is None and self.__equipe2 is not None:
            return {self.__equipe_2.__region}
        elif self.__equipe_1 is not None and self.__equipe_2 is None:
            return {self.__equipe_1.__region}
        else:
            return {self.__equipe_1.__region, self.__equipe_2.__region}

    def simuler(self):
        if self.__equipe_1 is None or self.__equipe_2 is None:
            raise ValueError("Il faut deux équipes pour jouer un match")
        point_equipe1: int = 0
        point_equipe2: int = 0
        if self.__best_of == 1:
            win: int = randint(0, 1)
            if win == 1:
                point_equipe1 += 1
            else:
                point_equipe2 += 1
        elif self.__best_of == 3:
            while point_equipe1 < 2 and point_equipe2 < 2:
                win: int = randint(0, 1)
                if win == 1:
                    point_equipe1 += 1
                else:
                    point_equipe2 += 1
        else:
            while point_equipe1 < 3 and point_equipe2 < 3:
                win: int = randint(0, 1)
                if win == 1:
                    point_equipe1 += 1
                else:
                    point_equipe2 += 1
        self.ajouter_score(point_equipe1, point_equipe2)
