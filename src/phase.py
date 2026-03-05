"""Implémentation de la classe Phase."""

import copy
from abc import ABC, abstractmethod

from .competition import Competition
from .match import Match


class Phase(ABC, Competition):
    """Classe modélisant une phase d'un tournoi.

    Une phase d'un tournoi est une compétition donc elle hérite de cette classe.
    """

    @property
    @abstractmethod
    def _TABLEAU_VIDE(self) -> dict[str, dict[str, dict[str, Match] | Match]]:
        ...

    def __init__(self) -> None:
        self._tableau = copy.deepcopy(self._TABLEAU_VIDE())

    @abstractmethod
    def _simuler_tirage(self) -> None:
        """Permet de simuler le tirage de la phase"""
        ...

    @abstractmethod
    def _simuler_tours(self) -> None:
        """Permet de simuler tous les tours de la phase"""
        ...

    def simuler(self):
        """Permet de simuler toute la phase, du tirage aux tours"""
        self._simuler_tirage()
        self._simuler_tours()
