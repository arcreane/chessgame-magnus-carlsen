from position import Position

class Piece:
    """
    Classe de base representant une piece du jeu d'echecs.
    """
    def __init__(self, position: Position, color: int):
        self.position = position
        self.color = color  # 0 pour blanc, 1 pour noir

    def isValidMove(self, newPosition: Position, board) -> bool:
        """
        Verifie si le deplacement vers newPosition est valide.
        Version initiale simplifiee : retourne toujours True.
        """
        return True

# Tests de la classe Piece
if __name__ == "__main__":
    print("Debut des tests de la classe Piece...")
    
    pos = Position("e", 2)
    
    pion_blanc = Piece(pos, 0)
    
    print(f"Piece creee a la position {pion_blanc.position} avec la couleur {pion_blanc.color}")
    
    nouvelle_pos = Position("e", 4)
    est_valide = pion_blanc.isValidMove(nouvelle_pos, None)
    print(f"Le deplacement vers {nouvelle_pos} est-il valide ? {est_valide}")
    
    print("Tests Piece OK !")