import random
from position import Position



class Player:
    """
    Représente un joueur humain dans la partie d'échecs.
    """

    def __init__(self, name: str, color: int):
        """
        Initialise une nouvelle instance de Player.

        :param name: Le nom du joueur.
        :param color: La couleur des pièces du joueur (0 pour blanc, 1 pour noir).
        """
        self._name = name
        self._color = color

    @property
    def name(self) -> str:
        """Retourne le nom du joueur."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Définit le nom du joueur."""
        self._name = value

    @property
    def color(self) -> int:
        """Retourne la couleur du joueur (0 pour blanc, 1 pour noir)."""
        return self._color

    @color.setter
    def color(self, value: int):
        """Définit la couleur du joueur."""
        self._color = value

    def askMove(self) -> str:
        """
        Demande au joueur de saisir son coup via la console.
        Le format attendu est "Nb1 Nc3" ou "Pe2 Pe4".

        :return: La chaîne saisie par le joueur.
        """
        color_str = "Blanc" if self._color == 0 else "Noir"
        move = input(f"[{color_str}] {self._name}, entrez votre coup (ex: Pe2 Pe4, ou 'save' / 'quit') : ")
        return move.strip()

class AIPlayer(Player):
    """
    Représente un joueur virtuel (Intelligence Artificielle) qui génère ses coups aléatoirement.
    """

    def askMove(self, board=None) -> str:
        """
        Génère un coup au format exact des échecs (ex: "Pe2 Pe4").
        Si un plateau est fourni, l'IA cherche d'abord des coups légaux pour ses pièces.

        :param board: Le plateau de jeu actuel.
        :return: Une chaîne de caractères représentant le coup généré.
        """
        if board is not None:
            # Recherche de tous les coups légaux possibles pour ce joueur
            legal_moves = []
            
            # Lister toutes les pièces du joueur sur le plateau
            for pos_str, piece in board.grid.items():
                if piece is not None and piece.color == self.color:
                    start_pos = Position(pos_str[0], int(pos_str[1]))
                    # Parcourir toutes les cases de l'échiquier pour voir si le déplacement est possible
                    for col in ["a", "b", "c", "d", "e", "f", "g", "h"]:
                        for row in range(1, 9):
                            dest_pos = Position(col, row)
                            # On s'assure de ne pas jouer sur place
                            if start_pos.column != dest_pos.column or start_pos.row != dest_pos.row:
                                if piece.isValidMove(dest_pos, board):
                                    piece_char = str(piece)
                                    move_str = f"{piece_char}{start_pos} {piece_char}{dest_pos}"
                                    legal_moves.append(move_str)
            
            # Si on a trouvé des coups légaux, on en choisit un au hasard
            if legal_moves:
                chosen_move = random.choice(legal_moves)
                print(f"[{'Blanc' if self.color == 0 else 'Noir'}] {self.name} (IA) joue : {chosen_move}")
                return chosen_move

        # Mode aléatoire pur (sans board ou si aucun coup légal trouvé)
        pieces = ["P", "R", "N", "B", "Q", "K"]
        columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
        rows = [1, 2, 3, 4, 5, 6, 7, 8]

        piece = random.choice(pieces)
        c1 = random.choice(columns)
        r1 = random.choice(rows)
        c2 = random.choice(columns)
        r2 = random.choice(rows)

        while c1 == c2 and r1 == r2:
            c2 = random.choice(columns)
            r2 = random.choice(rows)

        move = f"{piece}{c1}{r1} {piece}{c2}{r2}"
        print(f"[{'Blanc' if self.color == 0 else 'Noir'}] {self.name} (IA) joue : {move}")
        return move
