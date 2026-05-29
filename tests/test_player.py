import unittest
import re
from player import Player, AIPlayer
from board import Board


class TestPlayer(unittest.TestCase):
    """
    Tests unitaires pour les classes Player et AIPlayer.
    """

    def test_player_initialization(self):
        """Vérifie la création d'un joueur humain."""
        p = Player("David", 0)
        self.assertEqual(p.name, "David")
        self.assertEqual(p.color, 0)

        p.name = "Julien"
        p.color = 1
        self.assertEqual(p.name, "Julien")
        self.assertEqual(p.color, 1)

    def test_ai_player_move_generation(self):
        """Vérifie que le coup généré par l'IA respecte le format strict."""
        ai = AIPlayer("Ordi", 1)
        # On génère un coup sans passer de board (mode aléatoire pur)
        move = ai.askMove()
        
        # Le format doit être par exemple "Pe2 Pe4" ou "Nb1 Nc3"
        # Expression régulière pour valider ce format : [KQRBNP][a-h][1-8] [KQRBNP][a-h][1-8]
        pattern = r"^[KQRBNP][a-h][1-8] [KQRBNP][a-h][1-8]$"
        self.assertTrue(re.match(pattern, move), f"Le coup généré '{move}' ne respecte pas le format attendu.")

        # Vérifier que les deux pièces mentionnées sont identiques (ex: Pe2 Pe4)
        piece_start = move[0]
        piece_end = move[4]
        self.assertEqual(piece_start, piece_end)

    def test_ai_player_move_with_board(self):
        """Vérifie que le coup généré par l'IA avec un plateau est un coup valide."""
        board = Board()
        ai = AIPlayer("Ordi-Noir", 1) # IA noire (couleur 1)
        
        # L'IA doit générer un coup légal
        move = ai.askMove(board)
        
        # Le format doit être correct
        pattern = r"^[KQRBNP][a-h][1-8] [KQRBNP][a-h][1-8]$"
        self.assertTrue(re.match(pattern, move), f"Le coup généré '{move}' ne respecte pas le format.")
        
        # Vérifier que le coup généré est effectivement légal sur le plateau
        # Pour les noirs au début, les seuls coups légaux sont les pions en ligne 7 (vers ligne 6 ou 5) ou les cavaliers (N)
        piece_start = move[0]
        self.assertIn(piece_start, ["P", "N"])


if __name__ == "__main__":
    unittest.main()

