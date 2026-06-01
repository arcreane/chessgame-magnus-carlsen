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
        """
        Vérifie si le déplacement du Roi est valide.
        Le Roi se déplace d'une case dans n'importe quelle direction.
        """
        # Vérification des limites du plateau
        if not ('a' <= newPosition.column <= 'h' and 1 <= newPosition.row <= 8):
            return False

        c1 = ord(self.position.column) - ord('a')
        r1 = self.position.row
        c2 = ord(newPosition.column) - ord('a')
        r2 = newPosition.row

        dc = abs(c2 - c1)
        dr = abs(r2 - r1)

        # Pas de déplacement sur place
        if dc == 0 and dr == 0:
            return False

        # Le Roi se déplace d'au plus 1 case en colonne et en ligne
        if dc <= 1 and dr <= 1:
            target_piece = board.getPiece(newPosition)
            # Ne peut pas prendre sa propre couleur
            if target_piece is not None and target_piece.color == self.color:
                return False
            return True

        return False
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
