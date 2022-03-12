from piece import *
import numpy as np
class Board :
    def __init__(self) :
        self.board = [[None for i in range(4)] for j in range(4)]

    def placerPiece(self, piece,line,column) :
        # pblrm case dispo
        if self.board[line][column] == None: 
            self.board[line][column] = piece.id
            return True
        return False


    def checkColumn(self, board, line, column) :
        countC = [0,0,0,0]
        for i in range(4) : 
            if board.getGrid[i][column] == None :
                print("CountC Ya un NONE")
                return False

            countC = np.add(countC, Piece.getPiece(int(board.getGrid[i][column])).getPieceValue)  
        print("countC value :",countC)

        if 0 in countC :
            print("0 detected")
            return True
        if 4 in countC :
            print("4 detected")
            return True
        return False

    def checkLine(self, board, line, column) :
        countL = [0,0,0,0]
        for j in range(4) : 
            if board.getGrid[line][j] == None :
                print("CountL Ya un NONE")
                return False

            countL = np.add(countL, Piece.getPiece(int(board.getGrid[line][j])).getPieceValue)  
        print("countL value :",countL)

        if 0 in countL :
            print("0 detected")
            return True
        if 4 in countL :
            print("4 detected")
            return True
        return False
        
    def checkDiagonal(self, board, line, column) :
        countD = [0,0,0,0]
        if line == column :
            for d in range(4) : 
                if board.getGrid[d][d] == None :
                    print("CountL Ya un NONE")
                    return False
                countD = np.add(countD, Piece.getPiece(int(board.getGrid[d][d])).getPieceValue)
            print("countD value :",countD)

        if (line + column == 3):
            for d in range(4) : 
                if board.getGrid[d][d] == None :
                    print("CountL Ya un NONE")
                    return False  
                countD = np.add(countD, Piece.getPiece(int(board.getGrid[d][3-d])).getPieceValue)    
            print("countD value :",countD)
     
        if 0 in countD :
            print("0 detected")
            return True
        if 4 in countD :
            print("4 detected")
            return True
        return False

    def checkState(self,board, line, column) :
        """Vérifie si placer une pièce en x y fait terminer la game (vérifie ligne/colonne/diagonale)
        Retourne Vrai quand ca gagne"""

        if board.checkColumn( board, line, column) :
            print("Colonne gagnante")
            return True
        else : 
            print("Colonne pas gagnante")

        if board.checkLine( board, line, column) :
            print("Ligne gagnante")
            return True
        else : 
            print("Ligne pas gagnante")

        if board.checkDiagonal( board, line, column) :
            print("Diagonale gagnante")
            return True
        else : 
            print("Diagonale pas gagnante")    

        #TODO diagonale

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
        """Affiche la grille"""
        for i in range(len(self.board)) :
            print(self.board[i])

    @property
    def getGrid(self) :
        """Renvoi la grille"""
        return self.board


""" 
if __name__ == "__main__":
    print('This file "plateau.py"  is ran directly')
    b= Board()
    b.placerPiece(pieces[0], 0,0)
    b.placerPiece(pieces[1], 0,1)
    b.placerPiece(pieces[2], 0,2)
    b.placerPiece(pieces[12], 0,3)
    #15 0 13 9
    b.showGrid()
    b.checkState(b, 0, 0)
    #piecesrestantes
    #print(pieces[5].getPieceInfo)
else:
    print('This file "quarto.py" was imported')  
"""