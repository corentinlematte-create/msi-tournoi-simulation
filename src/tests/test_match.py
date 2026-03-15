"""Tests pour la classe Match."""

import re
from random import seed

import pytest

from ..coach import Coach
from ..equipe import Equipe
from ..joueur import Joueur
from ..match import Match


@pytest.mark.parametrize(
    "best_of, message_erreur",
    [
        ("oui", "best_of doit être parmis : 1,3,5"),
        (12, "best_of doit être parmis : 1,3,5"),
    ],
)
def test_erreur_init_match(best_of: int, message_erreur: str) -> None:
    with pytest.raises(TypeError, match=re.escape(message_erreur)):
        Match(best_of)


def preparer_match_plein():
    m = Match(5)
    e1 = Equipe(
        "Les plus forts",
        "LPF",
        "KR",
        (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
        (Coach("Louis"),),
    )
    e2 = Equipe(
        "Cyber Knights",
        "CK",
        "CN",
        (Joueur("Hugo"), Joueur("Léa"), Joueur("Max"), Joueur("Inès"), Joueur("Tom")),
        (Coach("Marc"),),
    )
    m.ajouter_equipes_et_scores(e1, e2, 2, 3)
    return m


def preparer_match_juste_equipe1():
    m = Match(5)
    e1 = Equipe(
        "Les plus forts",
        "LPF",
        "KR",
        (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
        (Coach("Louis"),),
    )
    m.ajouter_equipe_1(e1)
    return m


def preparer_match_juste_equipe2():
    m = Match(5)
    e2 = Equipe(
        "Cyber Knights",
        "CK",
        "CN",
        (Joueur("Hugo"), Joueur("Léa"), Joueur("Max"), Joueur("Inès"), Joueur("Tom")),
        (Coach("Marc"),),
    )
    m.ajouter_equipe_2(e2)
    return m


def preparer_match_sans_scores():
    m = Match(5)
    e1 = Equipe(
        "Les plus forts",
        "LPF",
        "KR",
        (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
        (Coach("Louis"),),
    )
    e2 = Equipe(
        "Cyber Knights",
        "CK",
        "CN",
        (Joueur("Hugo"), Joueur("Léa"), Joueur("Max"), Joueur("Inès"), Joueur("Tom")),
        (Coach("Marc"),),
    )
    m.ajouter_equipes(e1, e2)
    return m


def preparer_bo1_sans_scores():
    m = Match(1)
    e1 = Equipe(
        "Les plus forts",
        "LPF",
        "KR",
        (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
        (Coach("Louis"),),
    )
    e2 = Equipe(
        "Cyber Knights",
        "CK",
        "CN",
        (Joueur("Hugo"), Joueur("Léa"), Joueur("Max"), Joueur("Inès"), Joueur("Tom")),
        (Coach("Marc"),),
    )
    m.ajouter_equipes(e1, e2)
    return m


@pytest.mark.parametrize(
    "match, representation",
    [
        (preparer_match_sans_scores(), "-----------\n" "| LPF |   |\n" "| CK  |   |\n" "-----------"),
        (preparer_match_juste_equipe1(), "-----------\n" "| LPF |   |\n" "|     |   |\n" "-----------"),
        (preparer_match_juste_equipe2(), "-----------\n" "|     |   |\n" "| CK  |   |\n" "-----------"),
        (preparer_match_plein(), "-----------\n" "| LPF | 2 |\n" "| CK  | 3 |\n" "-----------"),
    ],
)
def test_str_match(match: Match, representation) -> None:
    assert str(match) == representation


@pytest.mark.parametrize(
    "match, equipe_1, message_erreur",
    [
        (
            preparer_match_juste_equipe1(),
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            "equipe1 est déjà donné",
        ),
        (preparer_match_juste_equipe2(), 12, "equipe1 doit être une équipe"),
        (
            preparer_match_juste_equipe2(),
            Equipe(
                "Cyber Knights",
                "CK",
                "CN",
                (Joueur("Hugo"), Joueur("Léa"), Joueur("Max"), Joueur("Inès"), Joueur("Tom")),
                (Coach("Marc"),),
            ),
            "equipe1 doit être une équipe différente de equipe2",
        ),
    ],
)
def test_erreur_ajouter_match1(match: Match, equipe_1: Equipe, message_erreur: str) -> None:
    with pytest.raises(TypeError, match=re.escape(message_erreur)):
        match.ajouter_equipe_1(equipe_1)


@pytest.mark.parametrize(
    "match, equipe_1",
    [
        (
            Match(5),
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
        )
    ],
)
def test_ajouter_equipe1(match: Match, equipe_1: Equipe) -> None:
    match.ajouter_equipe_1(equipe_1)
    assert match.equipe_1 == equipe_1


@pytest.mark.parametrize(
    "match, equipe_2, message_erreur",
    [
        (
            preparer_match_juste_equipe2(),
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            "equipe2 est déjà donné",
        ),
        (preparer_match_juste_equipe1(), 12, "equipe2 doit être une équipe"),
        (
            preparer_match_juste_equipe1(),
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            "equipe2 doit être une équipe différente de equipe1",
        ),
    ],
)
def test_erreur_ajouter_equipe2(match: Match, equipe_2: Equipe, message_erreur: str) -> None:
    with pytest.raises(TypeError, match=re.escape(message_erreur)):
        match.ajouter_equipe_2(equipe_2)


@pytest.mark.parametrize(
    "match, equipe_2",
    [
        (
            Match(5),
            Equipe(
                "Cyber Knights",
                "CK",
                "CN",
                (Joueur("Hugo"), Joueur("Léa"), Joueur("Max"), Joueur("Inès"), Joueur("Tom")),
                (Coach("Marc"),),
            ),
        )
    ],
)
def test_ajouter_match2(match: Match, equipe_2: Equipe) -> None:
    match.ajouter_equipe_2(equipe_2)
    assert match.equipe_2 == equipe_2


@pytest.mark.parametrize(
    "match, equipe_1, equipe_2",
    [
        (
            Match(5),
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            Equipe(
                "Cyber Knights",
                "CK",
                "CN",
                (Joueur("Hugo"), Joueur("Léa"), Joueur("Max"), Joueur("Inès"), Joueur("Tom")),
                (Coach("Marc"),),
            ),
        )
    ],
)
def test_ajouter_matchs(match: Match, equipe_1: Equipe, equipe_2: Equipe) -> None:
    match.ajouter_equipes(equipe_1, equipe_2)
    assert match.equipe_1 == equipe_1
    assert match.equipe_2 == equipe_2


@pytest.mark.parametrize(
    "match, score_equipe_1, score_equipe_2, message_erreur",
    [
        (
            Match(5),
            2,
            3,
            "les équipes doivent d'abord être inscrites",
        ),
        (preparer_match_plein(), 2, 3, "les scores sont déjà donnés"),
        (preparer_match_sans_scores(), "oui", 4, "les scores doivent être des entiers positifs"),
        (preparer_match_sans_scores(), 2, 4, "les scores doivent être cohérents avec le best_of"),
    ],
)
def test_erreur_ajouter_scores(match: Match, score_equipe_1: int, score_equipe_2: int, message_erreur: str) -> None:
    with pytest.raises(TypeError, match=re.escape(message_erreur)):
        match.ajouter_scores(score_equipe_1, score_equipe_2)


@pytest.mark.parametrize(
    "match, score_equipe_1, score_equipe_2",
    [(preparer_match_sans_scores(), 2, 3)],
)
def test_ajouter_scores(match: Match, score_equipe_1: int, score_equipe_2: int) -> None:
    match.ajouter_scores(score_equipe_1, score_equipe_2)
    assert match.score_equipe_1 == score_equipe_1
    assert match.score_equipe_2 == score_equipe_2


@pytest.mark.parametrize(
    "match, equipe_1, equipe_2, score_equipe_1, score_equipe_2",
    [
        (
            Match(5),
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            Equipe(
                "Cyber Knights",
                "CK",
                "CN",
                (Joueur("Hugo"), Joueur("Léa"), Joueur("Max"), Joueur("Inès"), Joueur("Tom")),
                (Coach("Marc"),),
            ),
            2,
            3,
        ),
        (
            Match(1),
            Equipe(
                "Les plus forts",
                "LPF",
                "KR",
                (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
                (Coach("Louis"),),
            ),
            Equipe(
                "Cyber Knights",
                "CK",
                "CN",
                (Joueur("Hugo"), Joueur("Léa"), Joueur("Max"), Joueur("Inès"), Joueur("Tom")),
                (Coach("Marc"),),
            ),
            0,
            1,
        ),
    ],
)
def test_ajouter_equipes_et_scores(
    match: Match, equipe_1: Equipe, equipe_2: Equipe, score_equipe_1: int, score_equipe_2: int
) -> None:
    match.ajouter_equipes_et_scores(equipe_1, equipe_2, score_equipe_1, score_equipe_2)
    assert match.equipe_1 == equipe_1
    assert match.equipe_2 == equipe_2
    assert match.score_equipe_1 == score_equipe_1
    assert match.score_equipe_2 == score_equipe_2


@pytest.mark.parametrize(
    "match, message_erreur",
    [
        (Match(5), "Les équipes doivent être définies pour désigner un gagnant"),
        (preparer_match_sans_scores(), "les scores doivent être inscrits"),
    ],
)
def test_erreur_equipe_gagnante(match: Match, message_erreur: str) -> None:
    with pytest.raises(TypeError, match=re.escape(message_erreur)):
        match.renvoyer_equipe_gagnante()


@pytest.mark.parametrize("match", [preparer_match_plein()])
def test_equipe_gagante(match: Match) -> None:
    assert match.renvoyer_equipe_gagnante() == Equipe(
        "Cyber Knights",
        "CK",
        "CN",
        (Joueur("Hugo"), Joueur("Léa"), Joueur("Max"), Joueur("Inès"), Joueur("Tom")),
        (Coach("Marc"),),
    )


@pytest.mark.parametrize(
    "match, message_erreur",
    [
        (Match(5), "Les équipes doivent être définies pour désigner un gagnant"),
        (preparer_match_sans_scores(), "les scores doivent être inscrits"),
    ],
)
def test_erreur_equipe_perdante(match: Match, message_erreur: str) -> None:
    with pytest.raises(TypeError, match=re.escape(message_erreur)):
        match.renvoyer_equipe_perdante()


@pytest.mark.parametrize("match", [preparer_match_plein()])
def test_equipe_perdante(match: Match) -> None:
    assert match.renvoyer_equipe_perdante() == Equipe(
        "Les plus forts",
        "LPF",
        "KR",
        (Joueur("Pierre"), Joueur("Marie"), Joueur("Jean"), Joueur("Luc"), Joueur("André")),
        (Coach("Louis"),),
    )


@pytest.mark.parametrize(
    "match, expected",
    [
        (preparer_match_plein(), {"CN", "KR"}),
        (preparer_match_juste_equipe1(), {"KR"}),
        (preparer_match_juste_equipe2(), {"CN"}),
        (Match(5), set()),
    ],
)
def test_equipe_region(match: Match, expected: set[str]) -> None:
    assert match.renvoyer_regions_equipes() == expected


@pytest.mark.parametrize(
    "match, score_equipe_1, score_equipe_2, seed_match",
    [
        (preparer_match_sans_scores(), 1, 3, 42),
        (preparer_bo1_sans_scores(), 1, 0, 5),
        (preparer_bo1_sans_scores(), 0, 1, 1),
    ],
)
def test_simulation(match: Match, score_equipe_1: int, score_equipe_2: int, seed_match: int) -> None:
    seed(seed_match)
    match.simuler()
    assert match.score_equipe_1 == score_equipe_1
    assert match.score_equipe_2 == score_equipe_2
