"""Implémentation de la classe MSI2024."""

from .equipe import Equipe
from .msi_2024_bracket import MSI2024Bracket
from .msi_2024_playin import MSI2024PlayIn
from .tournoi import Tournoi


class MSI2024(Tournoi):
    """Tournoi MSI 2024."""

    @property
    def _CHAPEAUX(self) -> dict[str, set[str]]:
        chapeaux = {
            "Chapeau Bracket": {"KR #1", "CN #1", "EMEA #1", "NA #1"},
            "Chapeau Play-In": {"KR #2", "CN #2", "EMEA #2", "NA #2", "APAC #1", "VN #1", "LAT #1", "BR #1"},
        }
        return chapeaux

    def simuler(self) -> None:
        """Permet de simuler la totalité du tournoi MSI2024"""
        play_in: MSI2024PlayIn = MSI2024PlayIn()

        equipes_play_in: dict[str, Equipe] = {
            k: v for k, v in self._equipes.items() if k in self._CHAPEAUX["Chapeau Play-In"]
        }
        play_in.ajouter_equipes(equipes_play_in)

        play_in.simuler()

        qualif_play_in_1: list[Equipe] = list(play_in.renvoyer_classement()["1-2"])
        qualif_play_in_2: list[Equipe] = list(play_in.renvoyer_classement()["3-4"])

        brackets: MSI2024Bracket = MSI2024Bracket()

        equipes_brackets: dict[str, Equipe] = {
            k: v for k, v in self._equipes.items() if k in self._CHAPEAUX["Chapeau Bracket"]
        }
        equipes_brackets |= {"Play-In #1": qualif_play_in_1[0], "Play-In #2": qualif_play_in_1[1]}
        equipes_brackets |= {"Play-In #3": qualif_play_in_2[0], "Play-In #4": qualif_play_in_2[1]}
        brackets.ajouter_equipes(equipes_brackets)

        brackets.simuler()

        self._phases["Play-In"] = play_in
        self._phases["Bracket"] = brackets

    def renvoyer_classement(self) -> dict[str, set[Equipe]]:
        """Renvoie le classement général du tournoi MSI2024"""
        classement_gen_play_in: dict[str, set[Equipe]] = {}
        classement_gen_play_in["9-10"] = self._phases["Play-In"].renvoyer_classement()["5-6"]
        classement_gen_play_in["11-12"] = self._phases["Play-In"].renvoyer_classement()["7-8"]

        classement: dict[str, set[Equipe]] = (self._phases["Bracket"].renvoyer_classement()) | (classement_gen_play_in)
        return classement

    def renvoyer_classement_str(self) -> str:
        """Renvoie le classement sous la forme d'une chaîne de caractères.

        Returns
        -------
        str
            Chaîne de caractères présentant les résultats.
        """

        # Récupère le classement complet du tournoi
        classement: dict[str, set[Equipe]] = self.renvoyer_classement()

        # Remplace les ensembles par des listes triées (pour avoir un ordre déterministe)
        classement_sorted: dict[str, list[Equipe]] = {cle: sorted(valeur) for cle, valeur in classement.items()}

        # Prix
        cagnotte_str_dollar: dict[str, str] = {cle: f"${valeur:,}" for cle, valeur in self._cagnotte.items()}
        lar_prix: int = max(len(value) for value in cagnotte_str_dollar.values())  # largeur pour les prix

        # Equipe
        lar_eq: int = max(len(equipe.nom_officiel) for equipe in self._equipes.values())  # largeur pour les équipes

        string_list = [
            r"=========                            ",
            r"RESULTATS                            ",
            r"=========                            ",
            r"                                     ",
            r" ——————————————————————————————————— ",
            f'| Place | {"Prix":^{lar_prix}} | {"Équipe":<{lar_eq}} |',
            r"|———————|—————————|—————————————————|",
            f'|   1   | {cagnotte_str_dollar["1"]:^{lar_prix}} | {classement_sorted["1"].pop(0).nom_officiel:<{lar_eq}} |',  # noqa: E501
            r"|———————|—————————|—————————————————|",
            f'|   2   | {cagnotte_str_dollar["2"]:^{lar_prix}} | {classement_sorted["2"].pop(0).nom_officiel:<{lar_eq}} |',  # noqa: E501
            r"|———————|—————————|—————————————————|",
            f'|   3   | {cagnotte_str_dollar["3"]:^{lar_prix}} | {classement_sorted["3"].pop(0).nom_officiel:<{lar_eq}} |',  # noqa: E501
            r"|———————|—————————|—————————————————|",
            f'|   4   | {cagnotte_str_dollar["4"]:^{lar_prix}} | {classement_sorted["4"].pop(0).nom_officiel:<{lar_eq}} |',  # noqa: E501
            r"|———————|—————————|—————————————————|",
            f'|       |         | {classement_sorted["5-6"].pop(0).nom_officiel:<{lar_eq}} |',
            f'|  5—6  | {cagnotte_str_dollar["5-6"]:^{lar_prix}} |—————————————————|',
            f'|       |         | {classement_sorted["5-6"].pop(0).nom_officiel:<{lar_eq}} |',
            r"|———————|—————————|—————————————————|",
            f'|       |         | {classement_sorted["7-8"].pop(0).nom_officiel:<{lar_eq}} |',
            f'|  7—8  | {cagnotte_str_dollar["7-8"]:^{lar_prix}} |—————————————————|',
            f'|       |         | {classement_sorted["7-8"].pop(0).nom_officiel:<{lar_eq}} |',
            r"|———————|—————————|—————————————————|",
            f'|       |         | {classement_sorted["9-10"].pop(0).nom_officiel:<{lar_eq}} |',
            f'| 9—10  | {cagnotte_str_dollar["9-10"]:^{lar_prix}} |—————————————————|',
            f'|       |         | {classement_sorted["9-10"].pop(0).nom_officiel:<{lar_eq}} |',
            r"|———————|—————————|—————————————————|",
            f'|       |         | {classement_sorted["11-12"].pop(0).nom_officiel:<{lar_eq}} |',
            f'| 11—12 | {cagnotte_str_dollar["11-12"]:^{lar_prix}} |—————————————————|',
            f'|       |         | {classement_sorted["11-12"].pop(0).nom_officiel:<{lar_eq}} |',
            r" ——————————————————————————————————— ",
        ]

        return "\n".join(string_list)

    def renvoyer_resultats_str(self) -> str:
        """Renvoie les résultats sous la forme d'une chaîne de caractères."""
        playin_str: str = self._phases["Play-In"].renvoyer_resultats_str()
        bracket_str: str = self._phases["Bracket"].renvoyer_resultats_str()
        classement_str: str = self.renvoyer_classement_str()

        largeur_max = max(
            max(
                max(len(string) for string in playin_str.split("\n")),
                max(len(string) for string in bracket_str.split("\n")),
            ),
            max(len(string) for string in classement_str.split("\n")),
        )

        trait = "-" * largeur_max
        ligne_vide = " " * largeur_max

        string = "\n".join(
            [
                ligne_vide,
                str(self),
                ligne_vide,
                trait,
                ligne_vide,
                playin_str,
                ligne_vide,
                trait,
                ligne_vide,
                bracket_str,
                ligne_vide,
                trait,
                ligne_vide,
                classement_str,
                ligne_vide,
                trait,
            ]
        )

        return string
