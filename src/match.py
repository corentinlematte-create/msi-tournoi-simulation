"""Implémentation de la classe Match."""
from .coach import Coach
from .joueur import Joueur


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
    def equipe1(self):
        return self.__equipe_1

    @property
    def equipe2(self):
        return self.__equipe_2

    @property
    def score_equipe1(self):
        return self.__score_equipe_1

    @property
    def score_equipe2(self):
        return self.__score_equipe_2

    def __eq__(self, autre):
        if type(autre) is not Equipe:
            return NotImplemented
        else:
            return self.nom_officiel == autre.nom_officiel

    def __str__(self):
        return f"{self.nom_abreviation}"

    def __repr__(self):
        return (
                f"Equipe({self.nom_officiel}, {self.nom_abreviation}, "
                f"{self.region}, {self.__joueurs}, {self.__coach})"
                )

    def __lt__(self, autre):
        if type(autre) is not Equipe:
            return NotImplemented
        else:
            return self.nom_officiel < autre.nom_officiel

    def __hash__(self):
        return hash(repr(self))
