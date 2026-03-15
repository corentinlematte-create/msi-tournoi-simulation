"""Implémentation de la classe Match."""

from random import randint

from .equipe import Equipe


class Match:
    """
    Représente un match ayant lieu entre deux équipes avec le score de fin.

    Parameters
    -----------
    best_of : int
              Le match se gagne au bout de 'best_of' affrontements.

    equipe_1 : Equipe
              Une des deux équipes qui s'affrontent, initialement none.

    equipe_2 : Equipe
              Une des deux équipes qui s'affrontent, initialement none.

    score_equipe_1 : int
              Nombre de manches gagnées par l'équipe 1 , initialement none.

    score_equipe_2 : int
              Nombre de manches gagnées par l'équipe 2 , initialement none.
    """

    def __init__(self, best_of: int) -> None:
        if best_of not in [1, 3, 5]:
            raise TypeError("best_of doit être parmis : 1,3,5")
        else:
            self.__best_of = best_of

        self.__equipe_1: Equipe | None = None
        self.__equipe_2: Equipe | None = None
        self.__score_equipe_1: int | None = None
        self.__score_equipe_2: int | None = None

    @property
    def best_of(self) -> int:
        return self.__best_of

    @property
    def equipe_1(self) -> Equipe | None:
        return self.__equipe_1

    @property
    def equipe_2(self) -> Equipe | None:
        return self.__equipe_2

    @property
    def score_equipe_1(self) -> int | None:
        return self.__score_equipe_1

    @property
    def score_equipe_2(self) -> int | None:
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

    def ajouter_equipe_1(self, equipe_1: Equipe) -> None:
        """
        Permet de rajouter l'equipe_1 à l'objet Match.

        Parameters
        -----------
        equipe_1: Equipe
                  Une des deux équipes qui s'affrontent.
        """
        if self.__equipe_1 is not None:
            raise TypeError("equipe1 est déjà donné")
        elif type(equipe_1) is not Equipe:
            raise TypeError("equipe1 doit être une équipe")
        elif self.__equipe_2 == equipe_1:
            raise TypeError("equipe1 doit être une équipe différente de equipe2")
        else:
            self.__equipe_1 = equipe_1

    def ajouter_equipe_2(self, equipe_2: Equipe) -> None:
        """
        Permet de rajouter l'equipe_2 à l'objet Match.

        Parameters
        -----------
        equipe_2: Equipe
                  Une des deux équipes qui s'affrontent.
        """
        if self.__equipe_2 is not None:
            raise TypeError("equipe2 est déjà donné")
        elif type(equipe_2) is not Equipe:
            raise TypeError("equipe2 doit être une équipe")
        elif self.__equipe_1 == equipe_2:
            raise TypeError("equipe2 doit être une équipe différente de equipe1")
        else:
            self.__equipe_2 = equipe_2

    def ajouter_equipes(self, equipe_1: Equipe, equipe_2: Equipe) -> None:
        """
        Permet de rajouter l'equipe_1 et l'equipe_2 à l'objet Match.

        Parameters
        -----------
        equipe_1: Equipe
                  Une des deux équipes qui s'affrontent.

        equipe_2: Equipe
                  Une des deux équipes qui s'affrontent.
        """
        self.ajouter_equipe_1(equipe_1)
        self.ajouter_equipe_2(equipe_2)

    def ajouter_scores(self, score_equipe_1: int, score_equipe_2: int) -> None:
        """
        Permet de rajouter le score de l'equipe_1 et le score de l'equipe_2 à l'objet Match

        Parameters
        -----------
        score_equipe_1: int
                  Nombre de manches gagnées par l'équipe 1.

        score_equipe_2: int
                  Nombre de manches gagnées par l'équipe 2.
        """
        if self.__equipe_1 is None or self.__equipe_2 is None:
            raise TypeError("les équipes doivent d'abord être inscrites")
        elif self.__score_equipe_1 is not None and self.__score_equipe_2 is not None:
            raise TypeError("les scores sont déjà donnés")
        elif type(score_equipe_1) is not int or type(score_equipe_2) is not int:
            raise TypeError("les scores doivent être des entiers positifs")
        elif max(score_equipe_1, score_equipe_2) != (self.best_of // 2) + 1:
            raise TypeError("les scores doivent être cohérents avec le best_of")
        else:
            self.__score_equipe_1 = score_equipe_1
            self.__score_equipe_2 = score_equipe_2

    def ajouter_equipes_et_scores(
        self, equipe_1: Equipe, equipe_2: Equipe, score_equipe_1: int, score_equipe_2: int
    ) -> None:
        """
        Permet de rajouter rajouter l'equipe_1, l'equipe_2, le score de l'equipe_1
        et le score de l'equipe_2 à l'objet Match.

        Parameters
        -----------
        equipe_1: Equipe
                  Une des deux équipes qui s'affrontent.

        equipe_2: Equipe
                  Une des deux équipes qui s'affrontent.

        score_equipe_1: int
                  Nombre de manches gagnées par l'équipe 1.

        score_equipe_2: int
                  Nombre de manches gagnées par l'équipe 2.
        """
        self.ajouter_equipes(equipe_1, equipe_2)
        self.ajouter_scores(score_equipe_1, score_equipe_2)

    def renvoyer_equipe_gagnante(self) -> Equipe:
        """
        Permet de renvoyer l'équipe gagnante ayant fait plus de point que l'autre.

        Returns
        -----------
        Equipe
              Equipe ayant fait plus de point que l'autre.
        """
        if self.__equipe_1 is None or self.__equipe_2 is None:
            raise TypeError("Les équipes doivent être définies pour désigner un gagnant")
        elif self.__score_equipe_1 is None or self.__score_equipe_2 is None:
            raise TypeError("les scores doivent être inscrits")
        elif self.__score_equipe_2 < self.__score_equipe_1:
            return self.__equipe_1
        else:
            return self.__equipe_2

    def renvoyer_equipe_perdante(self) -> Equipe:
        """
        Permet de renvoyer l'équipe perdante ayant fait moins de point que l'autre.

        Returns
        -----------
        Equipe
              Equipe ayant fait moins de point que l'autre.
        """
        if self.__equipe_1 is None or self.__equipe_2 is None:
            raise TypeError("Les équipes doivent être définies pour désigner un gagnant")
        elif self.__score_equipe_1 is None or self.__score_equipe_2 is None:
            raise TypeError("les scores doivent être inscrits")
        elif self.__score_equipe_2 < self.__score_equipe_1:
            return self.__equipe_2
        else:
            return self.__equipe_1

    def renvoyer_regions_equipes(self) -> set[str]:
        """
        Permet de renvoyer l'ensemble des régions associées aux équipes.

        Returns
        -----------
        set[str]
              Ensemble des régions associées aux équipes.
        """
        if self.__equipe_1 is None and self.__equipe_2 is not None:
            return {self.__equipe_2.region}
        elif self.__equipe_1 is not None and self.__equipe_2 is None:
            return {self.__equipe_1.region}
        elif self.__equipe_1 is not None and self.__equipe_2 is not None:
            return {self.__equipe_1.region, self.__equipe_2.region}
        else:
            return set()

    def simuler(self) -> None:
        """
        Permet de simuler une partie entre deux équipes en ajoutant les codes finaux.

        """
        point_equipe1: int = 0
        point_equipe2: int = 0
        if self.__best_of == 1:
            win1: int = randint(0, 1)
            if win1 == 1:
                point_equipe1 += 1
            else:
                point_equipe2 += 1
        elif self.__best_of == 3:
            while point_equipe1 < 2 and point_equipe2 < 2:
                win3: int = randint(0, 1)
                if win3 == 1:
                    point_equipe1 += 1
                else:
                    point_equipe2 += 1
        else:
            while point_equipe1 < 3 and point_equipe2 < 3:
                win5: int = randint(0, 1)
                if win5 == 1:
                    point_equipe1 += 1
                else:
                    point_equipe2 += 1
        self.ajouter_scores(point_equipe1, point_equipe2)
