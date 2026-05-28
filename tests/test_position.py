import unittest
from position import Position


class TestPosition(unittest.TestCase):
    """
    Tests unitaires pour la classe Position.
    """

    def test_initialization(self):
        """Vérifie que la position s'initialise correctement et que les propriétés fonctionnent."""
        pos = Position("e", 2)
        self.assertEqual(pos.column, "e")
        self.assertEqual(pos.row, 2)

    def test_setters(self):
        """Vérifie que les setters modifient correctement les coordonnées."""
        pos = Position("a", 1)
        pos.column = "h"
        pos.row = 8
        self.assertEqual(pos.column, "h")
        self.assertEqual(pos.row, 8)

    def test_string_representation(self):
        """Vérifie le formatage sous forme de chaîne de caractères (ex: 'e4')."""
        pos = Position("f", 3)
        self.assertEqual(str(pos), "f3")


if __name__ == "__main__":
    unittest.main()
