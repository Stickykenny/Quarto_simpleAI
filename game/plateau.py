from piece import *
import numpy as np
class Board :
    def __init__(self) :
        self.board = [[None for i in range(4)] for j in range(4)]
        self.available = [(a,b) for a in range(4) for b in range(4)]
        self.pieces_remained = pieces.copy()

    def placerPiece(self, piece,line,column) :
        # pblrm case dispo
        if self.board[line][column] == None: 
            self.board[line][column] = piece.id
            self.available.remove((line,column))
            self.pieces_remained.remove(piece)
            return True
        return False


    def checkColumn(self, board, line, column) :
        countC = [0,0,0,0]
        for i in range(4) : 
            if board.getGrid[i][column] == None :
                #print("CountC Ya un NONE")
                return False

            countC = np.add(countC, Piece.getPiece(int(board.getGrid[i][column])).getPieceValue)  
        #print("countC value :",countC)

        if 0 in countC :
            #print("0 detected")
            return True
        if 4 in countC :
            #print("4 detected")
            return True
        return False

    def checkLine(self, board, line, column) :
        countL = [0,0,0,0]
        for j in range(4) : 
            if board.getGrid[line][j] == None :
                #print("CountL Ya un NONE")
                return False

            countL = np.add(countL, Piece.getPiece(int(board.getGrid[line][j])).getPieceValue)  
        #print("countL value :",countL)

        if 0 in countL :
            #print("0 detected")
            return True
        if 4 in countL :
            #print("4 detected")
            return True
        return False
        
    def checkDiagonal(self, board, line, column) :
        countD = [0,0,0,0]

        if line == column :
            for d in range(4) : 
                if board.getGrid[d][d] == None :
                    #print("CountD1 Ya un NONE")
                    return False
                countD = np.add(countD, Piece.getPiece(int(board.getGrid[d][d])).getPieceValue)
            #print("countD1 value :",countD)
        
        if (line + column == 3):
            for d in range(4) : 
                if board.getGrid[d][3-d] == None :
                    #print("CountD2 Ya un NONE")
                    return False  
                countD = np.add(countD, Piece.getPiece(int(board.getGrid[d][3-d])).getPieceValue)    
            #print("countD2 value :",countD)


        if 0 in countD :
            #print("0 detected")
            return True
        if 4 in countD :
            #print("4 detected")
            return True
        return False
    

    def checkState(self,board, line, column) :
        """Vérifie si placer une pièce en x y fait terminer la game (vérifie ligne/colonne/diagonale)
        Retourne Vrai quand ca gagne"""

        if board.checkColumn( board, line, column) :
            print("Colonne gagnante")
            return True
        #else : 
            #print("Colonne pas gagnante")

        if board.checkLine( board, line, column) :
            print("Ligne gagnante")
            return True
        #else : 
            #print("Ligne pas gagnante")
            
        if (line == column or (line + column == 3)) :
            if board.checkDiagonal( board, line, column) :
                print("Diagonale gagnante")
                return True
            #else : 
                #print("Diagonale pas gagnante")    
        return False

    def showGrid(self) :
        """Affiche la grille"""
        for i in range(len(self.board)) :
            tmp = []
            for j in range(4) :
                if self.board[i][j] != None :
                    ind = int(self.board[i][j])
                    tmp.append(Piece.getPiece(ind).getPieceInfo[1])
                else :
                    tmp.append('None')
            print(tmp)

    @property
    def getGrid(self) :
        """Renvoi la grille"""
        return self.board

    @property
    def getAvailable(self) :
        """Renvoi la liste des placement possible"""
        #Example :
        #[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
        return self.available

    @property
    def getPieceRemained(self) :
        """Renvoi la grille"""
        return self.pieces_remained


if __name__ == "__main__":
    print('This file "plateau.py"  is ran directly')
    B = Board()


