import unittest
import os
from chess import Chess
from player import Player, AIPlayer
from position import Position
from specific_pieces import Pawn


class TestChess(unittest.TestCase):
    """
    Tests unitaires pour le moteur de jeu Chess.
    """

    def setUp(self):
        """Prépare un moteur de jeu pour les tests."""
        self.game = Chess()
        # Initialisation rapide de deux joueurs simulés pour les tests
        self.p1 = Player("Alice", 0)
        self.p2 = AIPlayer("Bob-IA", 1)
        self.game._players = [self.p1, self.p2]
        self.game._currentPlayer = self.p1

    def test_initialization(self):
        """Vérifie l'état après initialisation."""
        self.assertEqual(len(self.game.players), 2)
        self.assertEqual(self.game.currentPlayer, self.p1)
        self.assertIsNotNone(self.game.board)

    def test_switch_player(self):
        """Vérifie le changement de joueur actif."""
        self.game.switchPlayer()
        self.assertEqual(self.game.currentPlayer, self.p2)
        self.game.switchPlayer()
        self.assertEqual(self.game.currentPlayer, self.p1)

    def test_is_valid_move_syntax(self):
        """Vérifie le rejet des coups syntaxiquement incorrects."""
        # Trop court/long
        self.assertFalse(self.game.isValidMove("Pe2"))
        self.assertFalse(self.game.isValidMove("Pe2 Pe45"))
        # Mauvais séparateur
        self.assertFalse(self.game.isValidMove("Pe2-Pe4"))
        # Pièces différentes au départ/arrivée
        self.assertFalse(self.game.isValidMove("Pe2 Ne4"))
        # Pièce invalide
        self.assertFalse(self.game.isValidMove("Xe2 Xe4"))
        # Hors limites
        self.assertFalse(self.game.isValidMove("Pe2 Pe9"))
        self.assertFalse(self.game.isValidMove("Pi2 Pi4"))

    def test_is_valid_move_logic(self):
        """Vérifie la logique de validation des coups légaux."""
        # Coup de pion blanc valide au premier tour
        self.assertTrue(self.game.isValidMove("Pe2 Pe4"))
        # Essayer de déplacer une pièce noire alors que c'est le tour du blanc (invalide)
        self.assertFalse(self.game.isValidMove("Pe7 Pe5"))
        # Essayer de déplacer une pièce qui n'existe pas ou n'est pas sur la case de départ
        self.assertFalse(self.game.isValidMove("Qe2 Qe4"))  # Il n'y a pas de Reine en e2 au départ

    def test_save_and_load_game(self):
        """Vérifie que la sauvegarde et la restauration de l'état fonctionnent."""
        temp_filename = "test_partie_temp.json"

        # Effectuer un mouvement pour modifier l'état initial
        move = "Pe2 Pe4"
        self.assertTrue(self.game.isValidMove(move))
        self.game.updateBoard(move)
        self.game.switchPlayer()  # Le joueur actif est maintenant Bob (Noir)

        try:
            # Sauvegarder
            self.game.saveGame(temp_filename)
            self.assertTrue(os.path.exists(temp_filename))

            # Créer un nouveau moteur de jeu vide et charger l'état
            new_game = Chess()
            new_game.loadGame(temp_filename)

            # Vérifier que les joueurs sont restaurés
            self.assertEqual(len(new_game.players), 2)
            self.assertEqual(new_game.players[0].name, "Alice")
            self.assertEqual(new_game.players[0].color, 0)
            self.assertEqual(new_game.players[1].name, "Bob-IA")
            self.assertEqual(new_game.players[1].color, 1)
            self.assertTrue(isinstance(new_game.players[1], AIPlayer))

            # Vérifier que le joueur actif est bien le second joueur (Bob)
            self.assertEqual(new_game.currentPlayer.name, "Bob-IA")

            # Vérifier l'état du plateau (le pion e2 a été déplacé en e4)
            self.assertIsNone(new_game.board.getPiece(Position("e", 2)))
            pawn_e4 = new_game.board.getPiece(Position("e", 4))
            self.assertIsNotNone(pawn_e4)
            self.assertTrue(isinstance(pawn_e4, Pawn))
            self.assertEqual(pawn_e4.color, 0)

        finally:
            # Nettoyage du fichier temporaire
            if os.path.exists(temp_filename):
                os.remove(temp_filename)


if __name__ == "__main__":
    unittest.main()