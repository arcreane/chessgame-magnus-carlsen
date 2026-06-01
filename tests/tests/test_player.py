if __name__ == "__main__":
    print("--- Test unitaire de la classe Player et AIPlayer ---")
    humain = Player("Thomas", 0)
    print(f"Joueur humain créé : {humain.name}, Couleur : {humain.color}")
    
    ia = AIPlayer("Robot-1", 1)
    print(f"Joueur IA créé : {ia.name}, Couleur : {ia.color}")
    
    # Test askMove de l'IA (génère un coup aléatoire)
    coup_ia = ia.askMove()
    print(f"Coup aléatoire généré par l'IA : {coup_ia}")
