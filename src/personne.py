"""Implémentation de la classe _Personne."""


class _Personne:
    """
    Représente une personne avec son pseudo.

    Parameters
    ----------
    pseudo : str
           Le nom d'utilisateur de la personne.

    """

    def __init__(self, pseudo: str):
        if type(pseudo) is not str:
            raise TypeError("pseudo doit être une chaine de caractère")
        elif len(pseudo) < 2 or len(pseudo) > 16:
            raise TypeError("pseudo doit contenir entre 2 et 16 caractères")
        self.__pseudo = pseudo

    @property
    def pseudo(self) -> str:
        return self.__pseudo

    def __eq__(self, autre: object) -> bool:
        if type(autre) is not self.__class__:
            return NotImplemented
        else:
            return self.pseudo == autre.pseudo

    def __str__(self) -> str:
        return f"{self.pseudo}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.pseudo})"

    def __hash__(self) -> int:
        return hash(repr(self))
