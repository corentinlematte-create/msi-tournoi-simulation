"""Implémentation de la classe _Personne."""


class Personne:
    """Classe modélisant une personne.

    description.
    """

    def __init__(self, pseudo):
        if type(pseudo) is not str:
            raise TypeError("pseudo doit être une chaine de caractère")
        elif len(pseudo) < 2 or len(pseudo) > 16:
            raise TypeError("pseudo doit contenir entre 2 et 16 caractères")
        self.__pseudo = pseudo

    @property
    def pseudo(self):
        return self.__pseudo

    def __eq__(self, autre):
        if type(autre) is not Personne:
            return NotImplemented
        else:
            return self.pseudo == autre.pseudo

    def __str__(self):
        return f"{self.pseudo}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.pseudo})"

    def __hash__(self):
        return hash(repr(self))
