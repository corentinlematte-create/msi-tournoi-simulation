"""Tests pour la classe _Personne."""

import re

import pytest

from ..personne import Personne


@pytest.mark.parametrize(
    "pseudo, message_erreur",
    [
        ("pseudotroptroptroplong", "pseudo doit contenir entre 2 et 16 caractères"),
        (12, "pseudo doit être une chaine de caractère"),
    ],
)
def test_erreur_init(pseudo: str, message_erreur: str) -> None:
    with pytest.raises(TypeError, match=re.escape(message_erreur)):
        Personne(pseudo)


@pytest.mark.parametrize(
    "pseudo_valide",
    [
        "Alice",
        "Bob",
    ],
)
def test_creation_personne_valide(pseudo_valide: str) -> None:
    p = Personne(pseudo_valide)
    assert p.pseudo == pseudo_valide


@pytest.mark.parametrize(
    "personne_a, personne_b, egalite",
    [
        (Personne("Alice"), Personne("Alice"), True),
        (Personne("Alice"), Personne("Bob"), False),
        (Personne("Alice"), Personne("alice"), False),
        (Personne("Alice"), 12, NotImplemented),
    ],
)
def test_eq(personne_a: Personne, personne_b: Personne, egalite: bool) -> None:
    if egalite is NotImplemented:
        assert (personne_a.__eq__(personne_b)) is NotImplemented
    else:
        assert (personne_a == personne_b) == egalite


@pytest.mark.parametrize(
    "personne_a, representation",
    [(Personne("Alice"), "Alice"), (Personne("Bob"), "Bob")],
)
def test_str(personne_a: Personne, representation: Personne) -> None:
    assert str(personne_a) == representation


@pytest.mark.parametrize(
    "personne_a, representation",
    [(Personne("Alice"), "Personne(Alice)"), (Personne("Bob"), "Personne(Bob)")],
)
def test_repr(personne_a: Personne, representation: Personne) -> None:
    assert repr(personne_a) == representation


@pytest.mark.parametrize(
    "personne_a, representation",
    [(Personne("Alice"), "Personne(Alice)"), (Personne("Bob"), "Personne(Bob)")],
)
def test_hash(personne_a: Personne, representation: Personne) -> None:
    assert hash(personne_a) == hash(representation)
