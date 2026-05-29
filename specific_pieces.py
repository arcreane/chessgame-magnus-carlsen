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

    def __str__(self) -> str:
        """Retourne l'initiale du Roi."""
        return "K"


class Rook(Piece):
    """
    Représente la Tour dans le jeu d'échecs.
    Se déplace en ligne droite horizontalement ou verticalement.
    """

    def isValidMove(self, newPosition: Position, board: 'Board') -> bool:
        """
        Vérifie si le déplacement de la Tour est valide.
        La Tour se déplace horizontalement ou verticalement sans obstacle.
        """
        if not ('a' <= newPosition.column <= 'h' and 1 <= newPosition.row <= 8):
            return False

        c1 = ord(self.position.column) - ord('a')
        r1 = self.position.row
        c2 = ord(newPosition.column) - ord('a')
        r2 = newPosition.row

        dc = abs(c2 - c1)
        dr = abs(r2 - r1)

        if dc == 0 and dr == 0:
            return False

        # Déplacement horizontal ou vertical uniquement
        if (dc > 0 and dr == 0) or (dc == 0 and dr > 0):
            target_piece = board.getPiece(newPosition)
            if target_piece is not None and target_piece.color == self.color:
                return False
            # Vérification des obstacles sur le chemin
            return board.isPathClear(self.position, newPosition)

        return False

    def __str__(self) -> str:
        """Retourne l'initiale de la Tour."""
        return "R"


class Bishop(Piece):
    """
    Représente le Fou dans le jeu d'échecs.
    Se déplace en diagonale.
    """

    def isValidMove(self, newPosition: Position, board: 'Board') -> bool:
        """
        Vérifie si le déplacement du Fou est valide.
        Le Fou se déplace en diagonale sans obstacle.
        """
        if not ('a' <= newPosition.column <= 'h' and 1 <= newPosition.row <= 8):
            return False

        c1 = ord(self.position.column) - ord('a')
        r1 = self.position.row
        c2 = ord(newPosition.column) - ord('a')
        r2 = newPosition.row

        dc = abs(c2 - c1)
        dr = abs(r2 - r1)

        if dc == 0 and dr == 0:
            return False

        # Déplacement diagonal uniquement (dc == dr)
        if dc == dr:
            target_piece = board.getPiece(newPosition)
            if target_piece is not None and target_piece.color == self.color:
                return False
            # Vérification des obstacles sur le chemin
            return board.isPathClear(self.position, newPosition)

        return False

    def __str__(self) -> str:
        """Retourne l'initiale du Fou."""
        return "B"


class Queen(Piece):
    """
    Représente la Dame dans le jeu d'échecs.
    Se déplace horizontalement, verticalement ou en diagonale.
    """

    def isValidMove(self, newPosition: Position, board: 'Board') -> bool:
        """
        Vérifie si le déplacement de la Dame est valide.
        La Dame combine les mouvements de la Tour et du Fou.
        """
        if not ('a' <= newPosition.column <= 'h' and 1 <= newPosition.row <= 8):
            return False

        c1 = ord(self.position.column) - ord('a')
        r1 = self.position.row
        c2 = ord(newPosition.column) - ord('a')
        r2 = newPosition.row

        dc = abs(c2 - c1)
        dr = abs(r2 - r1)

        if dc == 0 and dr == 0:
            return False

        # Combinaison de la Tour et du Fou
        is_rook_move = (dc > 0 and dr == 0) or (dc == 0 and dr > 0)
        is_bishop_move = (dc == dr)

        if is_rook_move or is_bishop_move:
            target_piece = board.getPiece(newPosition)
            if target_piece is not None and target_piece.color == self.color:
                return False
            # Vérification des obstacles sur le chemin
            return board.isPathClear(self.position, newPosition)

        return False

    def __str__(self) -> str:
        """Retourne l'initiale de la Dame."""
        return "Q"


class Knight(Piece):
    """
    Représente le Cavalier dans le jeu d'échecs.
    Se déplace en L et peut sauter au-dessus des autres pièces.
    """

    def isValidMove(self, newPosition: Position, board: 'Board') -> bool:
        """
        Vérifie si le déplacement du Cavalier est valide.
        Le Cavalier se déplace en L (2 cases dans un sens et 1 dans l'autre).
        """
        if not ('a' <= newPosition.column <= 'h' and 1 <= newPosition.row <= 8):
            return False

        c1 = ord(self.position.column) - ord('a')
        r1 = self.position.row
        c2 = ord(newPosition.column) - ord('a')
        r2 = newPosition.row

        dc = abs(c2 - c1)
        dr = abs(r2 - r1)

        # Déplacement en L : (1, 2) ou (2, 1)
        if (dc == 1 and dr == 2) or (dc == 2 and dr == 1):
            target_piece = board.getPiece(newPosition)
            # Ne peut pas prendre sa propre couleur
            if target_piece is not None and target_piece.color == self.color:
                return False
            return True

        return False

    def __str__(self) -> str:
        """Retourne l'initiale du Cavalier (N pour kNight)."""
        return "N"


class Pawn(Piece):
    """
    Représente le Pion dans le jeu d'échecs.
    Se déplace d'une case vers l'avant (deux au premier coup) et prend en diagonale.
    """

    def isValidMove(self, newPosition: Position, board: 'Board') -> bool:
        """
        Vérifie si le déplacement du Pion est valide.
        Gère l'avancement d'une ou deux cases, et les captures en diagonale.
        """
        if not ('a' <= newPosition.column <= 'h' and 1 <= newPosition.row <= 8):
            return False

        c1 = ord(self.position.column) - ord('a')
        r1 = self.position.row
        c2 = ord(newPosition.column) - ord('a')
        r2 = newPosition.row

        dc = abs(c2 - c1)
        dr = r2 - r1  # Différence signée car la direction dépend de la couleur

        direction = 1 if self.color == 0 else -1
        start_row = 2 if self.color == 0 else 7

        # 1. Déplacement tout droit (pas de capture)
        if dc == 0:
            # Avancer d'une case
            if dr == direction:
                return board.getPiece(newPosition) is None
            # Avancer de deux cases depuis la ligne de départ
            elif dr == 2 * direction and r1 == start_row:
                intermediate_pos = Position(self.position.column, r1 + direction)
                return (board.getPiece(intermediate_pos) is None and 
                        board.getPiece(newPosition) is None)

        # 2. Capture en diagonale
        elif dc == 1 and dr == direction:
            target_piece = board.getPiece(newPosition)
            # Il doit y avoir une pièce ennemie sur la case de destination
            return target_piece is not None and target_piece.color != self.color

        return False

    def __str__(self) -> str:
        """Retourne l'initiale du Pion."""
        return "P"


if __name__ == "__main__":
    print("--- Test unitaire des Pièces Spécifiques ---")
    # Pour tester, on simule un faux plateau avec un dictionnaire vide ou bouchonné
    class FakeBoard:
        def __init__(self):
            self.pieces = {}
        def getPiece(self, pos):
            return self.pieces.get(str(pos), None)
        def isPathClear(self, start, end):
            return True

    board = FakeBoard()
    
    # 1. Test du Cavalier
    knight = Knight(Position("g", 1), 0)
    print(f"Cavalier initialisé en {knight.position}")
    print(f"Cavalier vers f3 (valide) : {knight.isValidMove(Position('f', 3), board)}")
    print(f"Cavalier vers g3 (invalide) : {knight.isValidMove(Position('g', 3), board)}")

    # 2. Test du Pion
    pawn = Pawn(Position("e", 2), 0) # Pion blanc
    print(f"Pion blanc initialisé en {pawn.position}")
    print(f"Pion blanc avance d'une case (valide) : {pawn.isValidMove(Position('e', 3), board)}")
    print(f"Pion blanc avance de deux cases (valide car départ) : {pawn.isValidMove(Position('e', 4), board)}")
    
    # Simuler une pièce ennemie en d3 pour tester la capture
    board.pieces["d3"] = Pawn(Position("d", 3), 1)
    print(f"Pion blanc capture en d3 (valide) : {pawn.isValidMove(Position('d', 3), board)}")
