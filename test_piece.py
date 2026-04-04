import unittest
from position import Position
from piece import Piece

class TestPiece(unittest.TestCase):
    
    def test_initialisation(self):
        pos = Position("a", 7)
        piece_noire = Piece(pos, 1)
        self.assertEqual(piece_noire.position.column, "a")
        self.assertEqual(piece_noire.color, 1)

    def test_isValidMove_simplifie(self):
        pos = Position("a", 7)
        piece = Piece(pos, 1)
        nouvelle_pos = Position("a", 6)
        
        self.assertTrue(piece.isValidMove(nouvelle_pos, None))

if __name__ == '__main__':
    unittest.main()