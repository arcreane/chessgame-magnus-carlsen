import unittest
from position import Position

class TestPosition(unittest.TestCase):
    
    def test_initialisation(self):
        p = Position("e", 4)
        self.assertEqual(p.column, "e")
        self.assertEqual(p.row, 4)

    def test_affichage_str(self):
        p = Position("a", 1)
        self.assertEqual(str(p), "a1")

if __name__ == '__main__':
    unittest.main()