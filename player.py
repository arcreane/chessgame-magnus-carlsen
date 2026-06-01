import random
from position import Position



class Player:
    """
    Représente un joueur humain dans la partie d'échecs.
    """

    def __init__(self, name: str, color: int):
        """
        Initialise une nouvelle instance de Player.

        :param name: Le nom du joueur.
        :param color: La couleur des pièces du joueur (0 pour blanc, 1 pour noir).
        """
        self._name = name
        self._color = color

    @property
    def name(self) -> str:
        """Retourne le nom du joueur."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Définit le nom du joueur."""
        self._name = value

    @property
    def color(self) -> int:
        """Retourne la couleur du joueur (0 pour blanc, 1 pour noir)."""
        return self._color

    @color.setter
    def color(self, value: int):
        """Définit la couleur du joueur."""
        self._color = value

    def askMove(self) -> str:
        """
        Demande au joueur de saisir son coup via la console.
        Le format attendu est "Nb1 Nc3" ou "Pe2 Pe4".

        :return: La chaîne saisie par le joueur.
        """
        color_str = "Blanc" if self._color == 0 else "Noir"
        move = input(f"[{color_str}] {self._name}, entrez votre coup (ex: Pe2 Pe4, ou 'save' / 'quit') : ")
        return move.strip()
