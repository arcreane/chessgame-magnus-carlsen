import unittest
from position import Position
from board import Board
from specific_pieces import King, Queen, Bishop, Knight, Rook, Pawn


class TestSpecificPieces(unittest.TestCase):
    """
    Tests unitaires pour les différentes pièces d'échecs (King, Queen, Bishop, Knight, Rook, Pawn).
    """

    def setUp(self):
        """Initialise un plateau vide pour tester les pièces isolées."""
        self.board = Board()
        # Vider complètement le plateau pour les tests unitaires ciblés
        for key in self.board.grid.keys():
            self.board.grid[key] = None

    def test_king_movement(self):
        """Vérifie les mouvements du Roi."""
        king = King(Position("e", 4), 0)  # Roi blanc en e4
        self.board.grid["e4"] = king

        # Mouvements valides (1 case dans toutes les directions)
        self.assertTrue(king.isValidMove(Position("e", 5), self.board))
        self.assertTrue(king.isValidMove(Position("f", 4), self.board))
        self.assertTrue(king.isValidMove(Position("f", 5), self.board))
        self.assertTrue(king.isValidMove(Position("d", 3), self.board))

        # Mouvements invalides (plus d'une case ou sur place)
        self.assertFalse(king.isValidMove(Position("e", 6), self.board))
        self.assertFalse(king.isValidMove(Position("g", 4), self.board))
        self.assertFalse(king.isValidMove(Position("e", 4), self.board))

        # Capture alliée (invalide) vs ennemie (valide)
        self.board.grid["e5"] = Pawn(Position("e", 5), 0)  # Pion ami en e5
        self.assertFalse(king.isValidMove(Position("e", 5), self.board))

        self.board.grid["f5"] = Pawn(Position("f", 5), 1)  # Pion ennemi en f5
        self.assertTrue(king.isValidMove(Position("f", 5), self.board))

    def test_rook_movement(self):
        """Vérifie les mouvements de la Tour."""
        rook = Rook(Position("d", 4), 0)  # Tour blanche en d4
        self.board.grid["d4"] = rook

        # Mouvements valides (horizontal/vertical)
        self.assertTrue(rook.isValidMove(Position("d", 8), self.board))
        self.assertTrue(rook.isValidMove(Position("a", 4), self.board))

        # Mouvements invalides (diagonaux ou biscornus)
        self.assertFalse(rook.isValidMove(Position("e", 5), self.board))

        # Test des obstacles sur le chemin
        self.board.grid["d6"] = Pawn(Position("d", 6), 1)  # Obstacle en d6
        self.assertFalse(rook.isValidMove(Position("d", 7), self.board))
        # Mais capture autorisée en d6
        self.assertTrue(rook.isValidMove(Position("d", 6), self.board))

    def test_bishop_movement(self):
        """Vérifie les mouvements du Fou."""
        bishop = Bishop(Position("d", 4), 0)  # Fou blanc en d4
        self.board.grid["d4"] = bishop

        # Mouvements diagonaux valides
        self.assertTrue(bishop.isValidMove(Position("g", 7), self.board))
        self.assertTrue(bishop.isValidMove(Position("a", 1), self.board))

        # Mouvements non diagonaux invalides
        self.assertFalse(bishop.isValidMove(Position("d", 7), self.board))

        # Obstacles diagonaux
        self.board.grid["f6"] = Pawn(Position("f", 6), 0)  # Allié en f6
        self.assertFalse(bishop.isValidMove(Position("g", 7), self.board))
        self.assertFalse(bishop.isValidMove(Position("f", 6), self.board))

    def test_queen_movement(self):
        """Vérifie les mouvements de la Dame (Tour + Fou)."""
        queen = Queen(Position("d", 4), 0)
        self.board.grid["d4"] = queen

        # Diagonale
        self.assertTrue(queen.isValidMove(Position("g", 7), self.board))
        # Verticale
        self.assertTrue(queen.isValidMove(Position("d", 7), self.board))
        # Invalide
        self.assertFalse(queen.isValidMove(Position("e", 6), self.board))

    def test_knight_movement(self):
        """Vérifie les mouvements du Cavalier (saut d'obstacles et forme en L)."""
        knight = Knight(Position("e", 4), 0)
        self.board.grid["e4"] = knight

        # Mouvements en L valides
        self.assertTrue(knight.isValidMove(Position("f", 6), self.board))
        self.assertTrue(knight.isValidMove(Position("d", 6), self.board))
        self.assertTrue(knight.isValidMove(Position("g", 5), self.board))
        self.assertTrue(knight.isValidMove(Position("c", 3), self.board))

        # Mouvements invalides
        self.assertFalse(knight.isValidMove(Position("e", 6), self.board))
        self.assertFalse(knight.isValidMove(Position("f", 5), self.board))

        # Saut au-dessus des pièces
        self.board.grid["e5"] = Pawn(Position("e", 5), 0)
        self.board.grid["f5"] = Pawn(Position("f", 5), 1)
        # Le cavalier peut toujours aller en f6
        self.assertTrue(knight.isValidMove(Position("f", 6), self.board))

    def test_pawn_movement(self):
        """Vérifie les mouvements spécifiques du Pion."""
        # Pion blanc en e2 (départ)
        pawn_white = Pawn(Position("e", 2), 0)
        self.board.grid["e2"] = pawn_white

        # Avance d'une case
        self.assertTrue(pawn_white.isValidMove(Position("e", 3), self.board))
        # Avance de deux cases (car sur la ligne de départ)
        self.assertTrue(pawn_white.isValidMove(Position("e", 4), self.board))
        # Capture diagonale impossible si pas d'ennemi
        self.assertFalse(pawn_white.isValidMove(Position("d", 3), self.board))

        # Placer un allié devant
        self.board.grid["e3"] = Pawn(Position("e", 3), 0)
        self.assertFalse(pawn_white.isValidMove(Position("e", 3), self.board))
        self.assertFalse(pawn_white.isValidMove(Position("e", 4), self.board))

        # Placer un ennemi en d3
        self.board.grid["d3"] = Pawn(Position("d", 3), 1)
        self.assertTrue(pawn_white.isValidMove(Position("d", 3), self.board))

        # Pion noir en e7 (départ)
        pawn_black = Pawn(Position("e", 7), 1)
        self.board.grid["e7"] = pawn_black
        self.assertTrue(pawn_black.isValidMove(Position("e", 6), self.board))
        self.assertTrue(pawn_black.isValidMove(Position("e", 5), self.board))

    def test_position_boundaries(self):
        """Vérifie que les pièces ne peuvent pas sortir de l'échiquier (limites a-h et 1-8)."""
        pawn = Pawn(Position("e", 2), 0)
        self.assertFalse(pawn.isValidMove(Position("e", 9), self.board))
        self.assertFalse(pawn.isValidMove(Position("i", 2), self.board))


if __name__ == "__main__":
    unittest.main()
