"""Implémentation de la classe Phase."""

import copy
import typing
from abc import abstractmethod

from .competition import Competition


class Phase(Competition):
    """Classe modélisant une phase d'un tournoi.

    Une phase d'un tournoi est une compétition donc elle hérite de cette classe.
    """

    @property
    @abstractmethod
    def _TABLEAU_VIDE(self) -> dict[str, typing.Any]: ...

    def __init__(self) -> None:
        self._tableau: dict[str, dict[str, typing.Any]] = copy.deepcopy(self._TABLEAU_VIDE)

    @abstractmethod
    def _simuler_tirage(self) -> None:
        """Permet de simuler le tirage de la phase"""
        ...

    @abstractmethod
    def _simuler_tours(self) -> None:
        """Permet de simuler tous les tours de la phase"""
        ...

    def simuler(self) -> None:
        """Permet de simuler toute la phase, du tirage aux tours"""
        self._simuler_tirage()
        self._simuler_tours()
