import unittest
from position import Position
from board import Board
from specific_pieces import Pawn, Rook, King


class TestBoard(unittest.TestCase):
    """
    Tests unitaires pour la classe Board.
    """

    def setUp(self):
        """Initialise un nouveau plateau pour chaque test."""
        self.board = Board()

    def test_grid_initialization(self):
        """Vérifie que la grille contient bien 64 cases."""
        self.assertEqual(len(self.board.grid), 64)

    def test_initial_pieces_setup(self):
        """Vérifie que les pièces sont correctement placées au début."""
        # Tour blanche en a1
        rook_a1 = self.board.getPiece(Position("a", 1))
        self.assertIsNotNone(rook_a1)
        self.assertTrue(isinstance(rook_a1, Rook))
        self.assertEqual(rook_a1.color, 0)

        # Pion noir en e7
        pawn_e7 = self.board.getPiece(Position("e", 7))
        self.assertIsNotNone(pawn_e7)
        self.assertTrue(isinstance(pawn_e7, Pawn))
        self.assertEqual(pawn_e7.color, 1)

        # Case vide en e4
        self.assertIsNone(self.board.getPiece(Position("e", 4)))

    def test_get_position(self):
        """Vérifie la recherche de la position d'une pièce."""
        pawn_d2 = self.board.getPiece(Position("d", 2))
        self.assertIsNotNone(pawn_d2)
        pos = self.board.getPosition(pawn_d2)
        self.assertEqual(pos.column, "d")
        self.assertEqual(pos.row, 2)

    def test_move_piece(self):
        """Vérifie le déplacement d'une pièce d'une case à une autre."""
        start = Position("e", 2)
        end = Position("e", 4)
        pawn = self.board.getPiece(start)
        self.assertIsNotNone(pawn)

        self.board.movePiece(start, end)
        
        # L'ancienne case doit être vide
        self.assertIsNone(self.board.getPiece(start))
        # La nouvelle case doit contenir le pion
        self.assertEqual(self.board.getPiece(end), pawn)
        # La position interne du pion doit être mise à jour
        self.assertEqual(pawn.position.column, "e")
        self.assertEqual(pawn.position.row, 4)

    def test_is_path_clear_vertical(self):
        """Vérifie le chemin libre sur la verticale."""
        # Chemin bloqué de e1 à e8 (il y a les pions en e2/e7)
        self.assertFalse(self.board.isPathClear(Position("e", 1), Position("e", 8)))
        # Chemin libre de e2 à e6 (on simule le plateau)
        self.board.grid["e7"] = None  # Enlever le pion noir pour le test
        self.assertTrue(self.board.isPathClear(Position("e", 2), Position("e", 6)))

    def test_is_path_clear_horizontal(self):
        """Vérifie le chemin libre sur l'horizontale."""
        # Ligne 4 est vide au départ
        self.assertTrue(self.board.isPathClear(Position("a", 4), Position("h", 4)))
        # Mettre un obstacle en d4
        self.board.grid["d4"] = Pawn(Position("d", 4), 0)
        self.assertFalse(self.board.isPathClear(Position("a", 4), Position("h", 4)))

    def test_is_path_clear_diagonal(self):
        """Vérifie le chemin libre sur les diagonales."""
        # Diagonale a3-f8 est initialement bloquée par le pion e7
        self.assertFalse(self.board.isPathClear(Position("a", 3), Position("f", 8)))
        # Enlever l'obstacle e7
        self.board.grid["e7"] = None
        self.assertTrue(self.board.isPathClear(Position("a", 3), Position("f", 8)))


if __name__ == "__main__":
    unittest.main()
