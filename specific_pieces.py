from typing import TYPE_CHECKING
from position import Position
from piece import Piece

if TYPE_CHECKING:
    from board import Board


class King(Piece):
    """
    Représente le Roi dans le jeu d'échecs.
    Se déplace d'une seule case dans toutes les directions.
    """

    def isValidMove(self, newPosition: Position, board: 'Board') -> bool:
        # TODO: À implémenter par Maxime
        raise NotImplementedError("isValidMove() non implémentée pour King")

    def __str__(self) -> str:
        return "K"


class Rook(Piece):
    """
    Représente la Tour dans le jeu d'échecs.
    Se déplace en ligne droite horizontalement ou verticalement.
    """

    def isValidMove(self, newPosition: Position, board: 'Board') -> bool:
        # TODO: À implémenter par Matthias
        raise NotImplementedError("isValidMove() non implémentée pour Rook")

    def __str__(self) -> str:
        return "R"


class Bishop(Piece):
    """
    Représente le Fou dans le jeu d'échecs.
    Se déplace en diagonale.
    """

    def isValidMove(self, newPosition: Position, board: 'Board') -> bool:
        # TODO: À implémenter par Antonin
        raise NotImplementedError("isValidMove() non implémentée pour Bishop")

    def __str__(self) -> str:
        return "B"


class Queen(Piece):
    """
    Représente la Dame dans le jeu d'échecs.
    Se déplace horizontalement, verticalement ou en diagonale.
    """

    def isValidMove(self, newPosition: Position, board: 'Board') -> bool:
        # TODO: À implémenter par Maxime
        raise NotImplementedError("isValidMove() non implémentée pour Queen")

    def __str__(self) -> str:
        return "Q"


class Knight(Piece):
    """
    Représente le Cavalier dans le jeu d'échecs.
    Se déplace en L et peut sauter au-dessus des autres pièces.
    """

    def isValidMove(self, newPosition: Position, board: 'Board') -> bool:
        # TODO: À implémenter par Antonin
        raise NotImplementedError("isValidMove() non implémentée pour Knight")

    def __str__(self) -> str:
        return "N"


class Pawn(Piece):
    """
    Représente le Pion dans le jeu d'échecs.
    Se déplace d'une case vers l'avant (deux au premier coup) et prend en diagonale.
    """

    def isValidMove(self, newPosition: Position, board: 'Board') -> bool:
        # TODO: À implémenter par Matthias
        raise NotImplementedError("isValidMove() non implémentée pour Pawn")

    def __str__(self) -> str:
        return "P"
