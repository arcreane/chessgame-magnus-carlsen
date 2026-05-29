import unittest
from position import Position
from piece import Piece


class TestPiece(unittest.TestCase):
    """
    Tests unitaires pour la classe de base Piece.
    """

    def test_initialization(self):
        """Vérifie l'initialisation et l'encapsulation de la pièce."""
        pos = Position("c", 1)
        piece = Piece(pos, 1)  # Pièce noire en c1
        self.assertEqual(piece.position, pos)
        self.assertEqual(piece.color, 1)

    def test_setters(self):
        """Vérifie la modification de la position et de la couleur par les propriétés."""
        pos1 = Position("a", 1)
        pos2 = Position("a", 2)
        piece = Piece(pos1, 0)
        
        piece.position = pos2
        piece.color = 1
        
        self.assertEqual(piece.position, pos2)
        self.assertEqual(piece.color, 1)

    def test_is_valid_move_stub(self):
        """Vérifie que la méthode stub de base retourne True par défaut."""
        pos1 = Position("e", 2)
        pos2 = Position("e", 4)
        piece = Piece(pos1, 0)
        self.assertTrue(piece.isValidMove(pos2, None))


if __name__ == "__main__":
    unittest.main()
