from position import Position
from piece import Piece
from specific_pieces import King, Queen, Bishop, Knight, Rook, Pawn


class Board:
    

    def __init__(self):
        
        self._grid = {}
        # Initialise toutes les cases à None
        for col_char in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            for row in range(1, 9):
                self._grid[f"{col_char}{row}"] = None

        self._setupInitialPieces()

    def _setupInitialPieces(self):
        
        
        for col_char in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            # Pions blancs sur la ligne 2
            pos_white_pawn = Position(col_char, 2)
            self._grid[str(pos_white_pawn)] = Pawn(pos_white_pawn, 0)
            
            # Pions noirs sur la ligne 7
            pos_black_pawn = Position(col_char, 7)
            self._grid[str(pos_black_pawn)] = Pawn(pos_black_pawn, 1)

        # 2. Placement des pièces majeures
        back_row_setup = [
            (Rook, "a"), (Knight, "b"), (Bishop, "c"), (Queen, "d"),
            (King, "e"), (Bishop, "f"), (Knight, "g"), (Rook, "h")
        ]

        for piece_class, col in back_row_setup:
            # Ligne 1 pour les blancs
            pos_white = Position(col, 1)
            self._grid[str(pos_white)] = piece_class(pos_white, 0)

            # Ligne 8 pour les noirs
            pos_black = Position(col, 8)
            self._grid[str(pos_black)] = piece_class(pos_black, 1)

    @property
    def grid(self) -> dict:
        return self._grid

    def getPiece(self, position: Position) -> Piece or None:
        
        return self._grid.get(str(position), None)

    def getPosition(self, piece: Piece) -> Position or None:
        
        for pos_str, p in self._grid.items():
            if p is piece:
                col = pos_str[0]
                row = int(pos_str[1])
                return Position(col, row)
        return None

    def movePiece(self, start: Position, end: Position):
        
        piece = self.getPiece(start)
        if piece is not None:
            piece.position = end
            self._grid[str(end)] = piece
            self._grid[str(start)] = None

    def isPathClear(self, start: Position, end: Position) -> bool:
        
        c1 = ord(start.column) - ord('a')
        r1 = start.row
        c2 = ord(end.column) - ord('a')
        r2 = end.row

        dc = c2 - c1
        dr = r2 - r1

        # Cas 1 : Mouvement horizontal
        if dr == 0:
            step = 1 if dc > 0 else -1
            for c_idx in range(c1 + step, c2, step):
                check_pos = Position(chr(c_idx + ord('a')), r1)
                if self.getPiece(check_pos) is not None:
                    return False

        # Cas 2 : Mouvement vertical
        elif dc == 0:
            step = 1 if dr > 0 else -1
            for r_idx in range(r1 + step, r2, step):
                check_pos = Position(start.column, r_idx)
                if self.getPiece(check_pos) is not None:
                    return False

        # Cas 3 : Mouvement diagonal
        elif abs(dc) == abs(dr):
            step_c = 1 if dc > 0 else -1
            step_r = 1 if dr > 0 else -1
            c_curr = c1 + step_c
            r_curr = r1 + step_r
            while c_curr != c2 and r_curr != r2:
                check_pos = Position(chr(c_curr + ord('a')), r_curr)
                if self.getPiece(check_pos) is not None:
                    return False
                c_curr += step_c
                r_curr += step_r

        return True


if __name__ == "__main__":
    print("--- Test unitaire de la classe Board ---")
    board = Board()
    
    # Récupérer le pion en e2
    pion_e2 = board.getPiece(Position("e", 2))
    print(f"Pièce en e2 : {pion_e2} (Couleur : {pion_e2.color if pion_e2 else 'Aucune'})")
    
    # Chercher la position de ce pion sur le plateau
    if pion_e2:
        pos_trouvee = board.getPosition(pion_e2)
        print(f"Position trouvée pour la pièce en e2 : {pos_trouvee}")

    # Récupérer une case vide (e4)
    case_e4 = board.getPiece(Position("e", 4))
    print(f"Pièce en e4 : {case_e4}")

    # Tester si le chemin est libre entre e2 et e4
    print(f"Chemin libre entre e2 et e4 ? : {board.isPathClear(Position('e', 2), Position('e', 4))}")
