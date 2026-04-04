class Position:
    def __init__(self, column: str, row: int):
        self.column = column
        self.row = row

    def __str__(self) -> str:
        return f"{self.column}{self.row}"

if __name__ == "__main__":
    print("Debut des tests de la classe Position...")
    p1 = Position("e", 4)
    print(f"Position creee : {p1}")
    p2 = Position("a", 1)
    print(f"Position creee : {p2}")
    print("Tests Position OK !")