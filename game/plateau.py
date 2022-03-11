from piece import pieces
class Board :
    def __init__(self) :
        self.board = [[None for i in range(4)] for j in range(4)]

    def placerPiece(self, piece,line,column) :
        # pblrm case dispo
        if self.board[line][column] == None: 
            self.board[line][column] = piece.affichage
            return True
        return False

    def checkState(self,board,piece, line, column) :
        """Vérifie si placer une pièce en x y fait terminer la game (vérifie ligne/colonne/diagonale)
        Retourne Vrai quand ca gagne"""

        """
        VERIF SI LIGNE EST PLEINE ou non 
        diagonale si line == column => diagonale  OU (0,3) (1,2) (2,1) (3,0) # trouver formule diagonale 

        n - x
        récupérer line column 
        
        piece = board[line][column]
        piece.getInfo

        On calcule et dès qu'on trouve un none on stop 
        ou alors check si ya 4 valeurs # bof

        CALCULE
        
        # 1ERE SOLUTION
        piece (0,0) à la valeur 1111
        1,0 / 2,0 /  3,0
        si 1,0    a=0 b=1 c=1 d=1 alors on stop recherche sur a 
        check_a = true
        check b = true
 
        # 2EME SOLUTION GO SUR CA
        on incrémente si True et lorsque on a un 4 ou 0 => WIN
        ligne vide = [0,0,0,0]
        if  0 in list or 4 in list : return True

        colonne vide = [0,0,0,0]

        diag dépends d'une cond


        """
        return False

    def showGrid(self) :
        """Affiche et renvoi la grille"""
        for i in range(len(self.board)) :
            print(self.board[i])
        return self.board



if __name__ == "__main__":
    print('This file "plateau.py"  is ran directly')
    b= Board()
    b.showGrid()
    print("\n \nafter putting some pieces")
    b.placerPiece(pieces[1], 0,2)

    b.placerPiece(pieces[8], 3,3)
    b.showGrid()

    #piecesrestantes
    print(pieces[5].getPieceInfo)
else:
    print('This file "quarto.py" was imported')
