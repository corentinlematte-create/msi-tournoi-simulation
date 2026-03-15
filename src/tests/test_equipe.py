"""Tests pour la classe Equipe."""

import re

import pytest

from ..coach import Coach
from ..equipe import Equipe
from ..joueur import Joueur


@pytest.mark.parametrize(
    "nom_officiel, nom_abreviation, region, joueurs, coachs, message_erreur",
    [
        (
            12,
            "LPF",
            "KR",
            (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
            (Coach("Louis"),),
            "nom_officiel doit être une chaine de caractère",
        ),
        (
            "les plus forts",
            12,
            "KR",
            (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
            (Coach("Louis"),),
            "nom_abreviation est une chaine de caractère",
        ),
        (
            "les plus forts",
            "LESPF",
            "KR",
            (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
            (Coach("Louis"),),
            "nom_abreviation doit contenir entre 2 et 3 caractères",
        ),
        (
            "les plus forts",
            "LPF",
            "Pas de calais",
            (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
            (Coach("Louis"),),
            "region doit être parmi : KR, CN, EMEA, NA, APAC, VN, BR, LAT",
        ),
        (
            "les plus forts",
            "LPF",
            "KR",
            [Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")],
            (Coach("Louis"),),
            "joueurs doit être un tuple de 5 éléments",
        ),
        (
            "les plus forts",
            "LPF",
            "KR",
            (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André"), Joueur("Intrue")),
            (Coach("Louis"),),
            "joueurs doit être un tuple de 5 éléments",
        ),
        (
            "les plus forts",
            "LPF",
            "KR",
            (12, Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
            (Coach("Louis"),),
            "joueurs doit être un tuple d'objet Joueur",
        ),
        (
            "les plus forts",
            "LPF",
            "KR",
            (Joueur("André"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
            (Coach("Louis"),),
            "joueurs doit être un tuple d'objet Joueur unique",
        ),
        (
            "les plus forts",
            "LPF",
            "KR",
            (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
            [Coach("Louis")],
            "coachs doit être un tuple de 1 ou 2 éléments",
        ),
        (
            "les plus forts",
            "LPF",
            "KR",
            (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
            (Coach("Louis"), Coach("Louisette"), Coach("Louisa")),
            "coachs doit être un tuple de 1 ou 2 éléments",
        ),
        (
            "les plus forts",
            "LPF",
            "KR",
            (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
            (12,),
            "coachs doit être un tuple d'objet Coach",
        ),
        (
            "les plus forts",
            "LPF",
            "KR",
            (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
            (Coach("Louis"), Coach("Louis")),
            "coachs doit être un tuple d'objet Coach unique",
        ),
    ],
)
def test_erreur_init_equipe(
    nom_officiel: str,
    nom_abreviation: str,
    region: str,
    joueurs: tuple[Joueur],
    coachs: tuple[Coach],
    message_erreur: str,
) -> None:
    with pytest.raises(TypeError, match=re.escape(message_erreur)):
        Equipe(nom_officiel, nom_abreviation, region, joueurs, coachs)


@pytest.mark.parametrize(
    "nom_officiel, nom_abreviation, region, joueurs, coachs",
    [
        (
            "Les plus forts",
            "LPF",
            "KR",
            (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
            (Coach("Louis"),),
        ),
        (
            "Cyber Knights",
            "CK",
            "CN",
            (Joueur("Hugo"), Joueur("Léa"), Joueur("Max"), Joueur("Inès"), Joueur("Tom")),
            (Coach("Marc"),),
        ),
    ],
)
def test_creation_equipe_valide(
    nom_officiel: str, nom_abreviation: str, region: str, joueurs: tuple[Joueur], coachs: tuple[Coach]
) -> None:
    e = Equipe(nom_officiel, nom_abreviation, region, joueurs, coachs)
    assert e.nom_officiel == nom_officiel
    assert e.nom_abreviation == nom_abreviation
    assert e.region == region


@pytest.mark.parametrize(
    "equipe_a, equipe_b, egalite",
    [
        (
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            True,
        ),
        (
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            Equipe(
                "Les moins forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            False,
        ),
        (
            12,
            Equipe(
                "Les moins forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            NotImplemented,
        ),
    ],
)
def test_eq_equipe(equipe_a: Equipe, equipe_b: Equipe, egalite: bool) -> None:
    if egalite is NotImplemented:
        assert equipe_a.__eq__(equipe_b) is NotImplemented
    else:
        assert equipe_a.__eq__(equipe_b) == egalite


@pytest.mark.parametrize(
    "equipe_a, representation",
    [
        (
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            "LPF",
        )
    ],
)
def test_str_equipe(equipe_a: Equipe, representation: str) -> None:
    assert str(equipe_a) == representation


@pytest.mark.parametrize(
    "equipe_a, representation",
    [
        (
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            "Equipe(Les plus forts, LPF, KR, "
            "(Joueur(Pierre), Joueur(Marie), Joueur(Jean), Joueur(Luc), Joueur(André)), (Coach(Louis),))",
        )
    ],
)
def test_repr_equipe(equipe_a: Equipe, representation: Equipe) -> None:
    assert repr(equipe_a) == representation


@pytest.mark.parametrize(
    "equipe_a, equipe_b, petit",
    [
        (
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            Equipe(
                "Les moins forts",
                "LMF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            False,
        ),
        (
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            Equipe(
                "Les rois forts",
                "LRF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            True,
        ),
        (
            12,
            Equipe(
                "Les moins forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            NotImplemented,
        ),
    ],
)
def test_lt_equipe(equipe_a: Equipe, equipe_b: Equipe, petit: bool) -> None:
    if petit is NotImplemented:
        assert equipe_a.__lt__(equipe_b) is NotImplemented
    else:
        assert equipe_a.__lt__(equipe_b) == petit


@pytest.mark.parametrize(
    "equipe_a, representation",
    [
        (
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            "Equipe(Les plus forts, LPF, KR, "
            "(Joueur(Pierre), Joueur(Marie), Joueur(Jean), Joueur(Luc), Joueur(André)), (Coach(Louis),))",
        )
    ],
)
def test_hash_equipe(equipe_a: Equipe, representation: Equipe) -> None:
    assert hash(equipe_a) == hash(representation)
