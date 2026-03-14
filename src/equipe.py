"""Implémentation de la classe Equipe."""

from .coach import Coach
from .joueur import Joueur


class Equipe:
    """
    Représente une equipe avec ses joueurs, coachs et autres caractéristiques.

    Parameters
    -----------
    nom_officiel : str
                   Le nom officiele de l'équipe.

    nom_breviation : str
                   Le nom abrégé de l'équipe.

    region : str
                   La region de l'équipe parmi: KR, CN, EMEA, NA, APAC, VN, BR, LAT.

    joueurs: tuple[Joueur]
                   L'ensemble des joueurs de l'équipes.

    coachs: tuple[Coach]
                   L'ensemble des coach de l'équipes.

    """

    def __init__(
        self, nom_officiel: str, nom_abreviation: str, region: str, joueurs: tuple[Joueur], coachs: tuple[Coach]
    ) -> None:
        if type(nom_officiel) is not str:
            raise TypeError("nom_officiel doit être une chaine de caractère")
        else:
            self.__nom_officiel: str = nom_officiel

        if type(nom_abreviation) is not str:
            raise TypeError("nom_abreviation est une chaine de caractère entre 2 et 3 caractères")
        elif len(nom_abreviation) < 2 or len(nom_abreviation) > 3:
            raise TypeError("nom_abreviation doit contenir ")
        else:
            self.__nom_abreviation: str = nom_abreviation

        if region not in ["KR", "CN", "EMEA", "NA", "APAC", "VN", "BR", "LAT"]:
            raise TypeError("region doit être parmi : KR, CN, EMEA, NA, APAC, VN, BR, LAT")
        else:
            self.__region: str = region

        if type(joueurs) is not tuple or len(joueurs) != 5:
            raise TypeError("joueurs doit être un tuple de 5 éléments ")
        elif not all(type(j) is Joueur for j in joueurs):
            raise TypeError("joueurs doit être un tuple d'objet Joueur")
        elif len(set(joueurs)) != 5:
            raise TypeError("joueurs doit être un tuple d'objet Joueur unique")
        else:
            self.__joueurs: tuple[Joueur] = joueurs

        if type(coachs) is not tuple or len(coachs) > 2 or len(coachs) < 1:
            raise TypeError("coachs doit être un tuple de 1 ou 2 éléments ")
        elif not all(type(c) is Coach for c in coachs):
            raise TypeError("coachs doit être un tuple d'objet Coach")
        elif len(set(joueurs)) != 5:
            raise TypeError("coachs doit être un tuple d'objet Coach unique")
        else:
            self.__coachs: tuple[Coach] = coachs

    @property
    def nom_officiel(self) -> str:
        return self.__nom_officiel

    @property
    def nom_abreviation(self) -> str:
        return self.__nom_abreviation

    @property
    def region(self) -> str:
        return self.__region

    def __eq__(self, autre: object) -> bool:
        if type(autre) is not Equipe:
            return NotImplemented
        else:
            return self.nom_officiel == autre.nom_officiel

    def __str__(self) -> str:
        return f"{self.nom_abreviation}"

    def __repr__(self) -> str:
        return f"Equipe({self.nom_officiel}, {self.nom_abreviation}, {self.region}, {self.__joueurs}, {self.__coachs})"

    def __lt__(self, autre: object) -> bool:
        if type(autre) is not Equipe:
            return NotImplemented
        else:
            return self.nom_officiel < autre.nom_officiel

    def __hash__(self) -> int:
        return hash(repr(self))
