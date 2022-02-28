from piece import pieces
class Board :
    def __init__(self) :
        self.board = [[None for i in range(4)] for j in range(4)]

    def placerPiece(self, piece, x,y) :
        self.board[x][y] = piece.id
        return 0

    def checkState(self, piece, x, y) :
        """Vérifie si placer une pièce en x y fait terminer la game"""
        return False

    def showGrid(self) :
        """Affiche et renvoi la grille"""
        for i in range(len(self.board)) :
            print(self.board[i])
        return self.board

b= Board()
b.showGrid()
print("\n \nafter putting some pieces")
b.placerPiece(pieces[1], 0,2)

b.placerPiece(pieces[8], 3,3)
b.showGrid()
