"""Implémentation de la classe Equipe."""
from .coach import Coach
from .joueur import Joueur


class Equipe:
    """Classe modélisant une equipe.

    description.
    """

    def __init__(self, nom_officiel, nom_abreviation, region, joueurs, coachs):
        if type(nom_officiel) is not str:
            raise TypeError("nom_officiel doit être une chaine de caractère")
        else:
            self.__nom_officiel = nom_officiel

        if type(nom_abreviation) is not str:
            raise TypeError("nom_abreviation est une chaine de caractère entre 2 et 3 caractères")
        elif len(nom_abreviation) < 2 or len(nom_abreviation) > 3:
            raise TypeError("nom_abreviation doit contenir ")
        else:
            self.__nom_abrevation = nom_abreviation

        if region not in ["KR", "CN", "EMEA", "NA", "APAC", "VN", "BR", "LAT"]:
            raise TypeError("region doit être parmis : KR, CN, EMEA, NA, APAC, VN, BR, LAT")
        else:
            self.__region = region

        if type(joueurs) is not list or len(joueurs) != 5:
            raise TypeError("joueurs doit être une liste de 5 éléments ")
        elif not all(type(j) is Joueur for j in joueurs):
            raise TypeError("joueurs doit être une liste d'objet Joueur")
        elif len(set(joueurs)) != 5:
            raise TypeError("joueurs doit être une liste d'objet Joueur unique")
        else:
            self.__joueurs = joueurs

        if type(coachs) is not list or len(coachs) != 2:
            raise TypeError("coachs doit être une liste de 2 éléments ")
        elif not all(type(c) is Coach for c in coachs):
            raise TypeError("coachs doit être une liste d'objet Coach")
        elif len(set(joueurs)) != 5:
            raise TypeError("coachs doit être une liste d'objet Coach unique")
        else:
            self.__coachs = coachs

    @property
    def nom_officiel(self):
        return self.__nom_officiel

    @property
    def nom_abreviation(self):
        return self.__nom_abrevation

    @property
    def region(self):
        return self.__region

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
