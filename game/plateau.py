class Board :
    def __init__(self) :
        self.board = [[None for i in range(4)] for j in range(4)]

    def placerPiece(self, piece) :
        return 0

    def checkState(self, piece, x, y) :
        """Vérifie si placer une pièce en x y fait terminer la game"""
        return False