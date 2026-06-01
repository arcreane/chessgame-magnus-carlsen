import json
import os
from position import Position
from board import Board
from player import Player, AIPlayer
from specific_pieces import King, Queen, Bishop, Knight, Rook, Pawn


class Chess:
    """
    Gère le plateau, les joueurs, la boucle de jeu, la validation des coups et la sauvegarde.
    """

    def __init__(self):
        """

        """
        self._board = Board()
        self._players = []
        self._currentPlayer = None

    @property
    def board(self) -> Board:
        """Retourne le plateau de jeu."""
        return self._board

    @property
    def players(self) -> list:
        """Retourne la liste des joueurs."""
        return self._players

    @property
    def currentPlayer(self) -> Player:
        """Retourne le joueur actif."""
        return self._currentPlayer

    def initPlayers(self):
        """
        Initialise les joueurs en demandant leurs noms.
        """
        print("--- Initialisation des Joueurs ---")
        name1 = input("Entrez le nom du Joueur 1 (Blancs) [Saisir 'AI' pour l'ordinateur] : ").strip()
        if not name1:
            name1 = "Joueur 1"
        if name1.upper() == "AI":
            self._players.append(AIPlayer("Robot-Blanc", 0))
        else:
            self._players.append(Player(name1, 0))

        name2 = input("Entrez le nom du Joueur 2 (Noirs) [Saisir 'AI' pour l'ordinateur] : ").strip()
        if not name2:
            name2 = "Joueur 2"
        if name2.upper() == "AI":
            self._players.append(AIPlayer("Robot-Noir", 1))
        else:
            self._players.append(Player(name2, 1))

        self._currentPlayer = self._players[0]

    def displayBoard(self):
        """
        Affiche l'échiquier dans la console de manière lisible.
        Les pièces blanches sont affichées en MAJUSCULES, les noires en minuscules.
        """
        print("\n   a  b  c  d  e  f  g  h")
        print("  +----------------------+")
        for row in range(8, 0, -1):
            row_str = f"{row} |"
            for col_char in ["a", "b", "c", "d", "e", "f", "g", "h"]:
                piece = self._board.getPiece(Position(col_char, row))
                if piece is None:
                    row_str += " . "
                else:
                    symbol = str(piece)
                    # Blanc en majuscule, Noir en minuscule
                    symbol_char = symbol.upper() if piece.color == 0 else symbol.lower()
                    row_str += f" {symbol_char} "
            row_str += f"| {row}"
            print(row_str)
        print("  +----------------------+")
        print("   a  b  c  d  e  f  g  h\n")

    def isValidMove(self, move: str) -> bool:
        """

        """
        # Vérification syntaxique de la saisie (longueur de 7, espace au milieu)
        if len(move) != 7 or move[3] != ' ':
            return False

        p1, col1_str, row1_str = move[0], move[1], move[2]
        p2, col2_str, row2_str = move[4], move[5], move[6]

        pieces = ['P', 'R', 'N', 'B', 'Q', 'K']
        if p1 not in pieces or p2 not in pieces or p1 != p2:
            return False

        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        rows = ['1', '2', '3', '4', '5', '6', '7', '8']
        if col1_str not in columns or col2_str not in columns or row1_str not in rows or row2_str not in rows:
            return False

        # Conversion en objets de position
        start_pos = Position(col1_str, int(row1_str))
        end_pos = Position(col2_str, int(row2_str))

        # Récupération de la pièce sur le plateau
        piece = self._board.getPiece(start_pos)
        if piece is None:
            return False

        # Vérifier que la pièce appartient bien au joueur actif
        if piece.color != self._currentPlayer.color:
            return False

        # Vérifier que le type de pièce correspond à la lettre saisie
        if str(piece) != p1:
            return False

        #
        return piece.isValidMove(end_pos, self._board)

    def isCheckMate(self) -> bool:
        """
        Détermine si la partie est terminée par échec et mat.

        """
        return False

    def updateBoard(self, move: str):
        """
        Met à jour le plateau de jeu après validation d'un coup.


        """
        col1_str, row1_str = move[1], move[2]
        col2_str, row2_str = move[5], move[6]

        start_pos = Position(col1_str, int(row1_str))
        end_pos = Position(col2_str, int(row2_str))

        self._board.movePiece(start_pos, end_pos)

    def switchPlayer(self):
        """
        Bascule le tour de jeu entre les deux joueurs.
        """
        if self._currentPlayer == self._players[0]:
            self._currentPlayer = self._players[1]
        else:
            self._currentPlayer = self._players[0]

    def saveGame(self, filename: str):
        """
        Sauvegarde l'état actuel de la partie dans un fichier JSON.


        """
        state = {
            "players": [
                {
                    "name": self._players[0].name,
                    "color": self._players[0].color,
                    "is_ai": isinstance(self._players[0], AIPlayer)
                },
                {
                    "name": self._players[1].name,
                    "color": self._players[1].color,
                    "is_ai": isinstance(self._players[1], AIPlayer)
                }
            ],
            "currentPlayerIndex": 0 if self._currentPlayer == self._players[0] else 1,
            "board": {
                pos_str: {"type": str(piece), "color": piece.color}
                for pos_str, piece in self._board.grid.items() if piece is not None
            }
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=4, ensure_ascii=False)

    def loadGame(self, filename: str):
        """
        Restaure une partie sauvegardée depuis un fichier JSON.


        """
        with open(filename, 'r', encoding='utf-8') as f:
            state = json.load(f)

        # 1. Restauration des joueurs
        self._players = []
        for p_data in state["players"]:
            if p_data["is_ai"]:
                self._players.append(AIPlayer(p_data["name"], p_data["color"]))
            else:
                self._players.append(Player(p_data["name"], p_data["color"]))

        self._currentPlayer = self._players[state["currentPlayerIndex"]]

        # 2. Vider et reconstruire le plateau
        self._board.grid.clear()
        for col_char in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            for row in range(1, 9):
                self._board.grid[f"{col_char}{row}"] = None

        piece_mapping = {
            "K": King,
            "Q": Queen,
            "B": Bishop,
            "N": Knight,
            "R": Rook,
            "P": Pawn
        }

        for pos_str, p_data in state["board"].items():
            col = pos_str[0]
            row = int(pos_str[1])
            pos = Position(col, row)
            piece_class = piece_mapping[p_data["type"]]
            self._board.grid[pos_str] = piece_class(pos, p_data["color"])

    def play(self):
        """
        Boucle principale du jeu gérant les tours alternés.
        """
        print("========================================")
        print("          BIENVENUE AUX ÉCHECS          ")
        print("========================================\n")

        charger = input("Voulez-vous charger une partie existante ? (o/n) : ").strip().lower()
        if charger == 'o':
            filename = input("Nom du fichier de sauvegarde à charger (ex: partie.json) : ").strip()
            if os.path.exists(filename):
                try:
                    self.loadGame(filename)
                    print("\nPartie restaurée avec succès !\n")
                except Exception as e:
                    print(f"Erreur lors du chargement : {e}. Création d'une nouvelle partie.")
                    self.initPlayers()
            else:
                print("Fichier introuvable. Création d'une nouvelle partie.")
                self.initPlayers()
        else:
            self.initPlayers()

        print("\nDébut de la partie. Entrez vos coups sous la forme 'Pe2 Pe4'.")
        print("Vous pouvez saisir 'save' pour sauvegarder la partie ou 'quit' pour quitter.\n")

        # Boucle principale
        while not self.isCheckMate():
            self.displayBoard()

            valid_move = False
            while not valid_move:
                # Si c'est l'IA, on lui passe le board pour accélérer son choix de coups
                if isinstance(self._currentPlayer, AIPlayer):
                    move = self._currentPlayer.askMove(board=self._board)
                else:
                    move = self._currentPlayer.askMove()

                # Commandes système
                if move.lower() == "save":
                    filename = input("Nom du fichier de sauvegarde (ex: partie.json) : ").strip()
                    try:
                        self.saveGame(filename)
                        print("Sauvegarde effectuée !")
                    except Exception as e:
                        print(f"Erreur lors de la sauvegarde : {e}")
                    continue
                elif move.lower() == "quit":
                    print("\nPartie interrompue. À bientôt !")
                    return

                # Validation et exécution du coup
                if self.isValidMove(move):
                    self.updateBoard(move)
                    valid_move = True
                    print(f"Coup validé et joué !")
                else:
                    # L'IA réessaie silencieusement, l'humain reçoit un message d'erreur
                    if not isinstance(self._currentPlayer, AIPlayer):
                        print(
                            "Coup invalide. Vérifiez la syntaxe (ex: 'Pe2 Pe4') et le déplacement autorisé de la pièce.")

            self.switchPlayer()


if __name__ == "__main__":
    print("--- Test unitaire de la classe Chess ---")
    game = Chess()

    # Simulation manuelle simplifiée pour tester
    p1 = Player("Alice", 0)
    p2 = Player("Bob", 1)
    game._players = [p1, p2]
    game._currentPlayer = p1

    print("Test validation d'un coup blanc valide (pion e2 e4) :")
    coup = "Pe2 Pe4"
    if game.isValidMove(coup):
        print(f"Le coup {coup} est valide !")
        game.updateBoard(coup)
        game.displayBoard()
    else:
        print(f"Le coup {coup} est invalide !")