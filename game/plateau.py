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


    def checkColumn(self, line, column) :
        countC = [0,0,0,0]
        for i in range(4) : 
            if self.getGrid[i][column] == None :
                #print("CountC Ya un NONE")
                return False

            countC = np.add(countC, Piece.getPiece(int(self.getGrid[i][column])).getPieceValue)  
        #print("countC value :",countC)

        if 0 in countC :
            #print("0 detected")
            return True
        if 4 in countC :
            #print("4 detected")
            return True
        return False

    def checkLine(self, line, column) :
        countL = [0,0,0,0]
        for j in range(4) : 
            if self.getGrid[line][j] == None :
                #print("CountL Ya un NONE")
                return False

            countL = np.add(countL, Piece.getPiece(int(self.getGrid[line][j])).getPieceValue)  
        #print("countL value :",countL)

        if 0 in countL :
            #print("0 detected")
            return True
        if 4 in countL :
            #print("4 detected")
            return True
        return False
        
    def checkDiagonal(self, line, column) :
        countD = [0,0,0,0]

        if line == column :
            for d in range(4) : 
                if self.getGrid[d][d] == None :
                    #print("CountD1 Ya un NONE")
                    return False
                countD = np.add(countD, Piece.getPiece(int(self.getGrid[d][d])).getPieceValue)
            #print("countD1 value :",countD)
        
        if (line + column == 3):
            for d in range(4) : 
                if self.getGrid[d][3-d] == None :
                    #print("CountD2 Ya un NONE")
                    return False  
                countD = np.add(countD, Piece.getPiece(int(self.getGrid[d][3-d])).getPieceValue)    
            #print("countD2 value :",countD)


        if 0 in countD :
            #print("0 detected")
            return True
        if 4 in countD :
            #print("4 detected")
            return True
        return False
    

    def checkState(self, line, column) :
        """Vérifie si placer une pièce en x y fait terminer la game (vérifie ligne/colonne/diagonale)
        Retourne Vrai quand ca gagne"""

        if self.checkColumn( line, column) :
            #print("Colonne gagnante")
            return True
        #else : 
            #print("Colonne pas gagnante")

        if self.checkLine( line, column) :
            #print("Ligne gagnante")
            return True
        #else : 
            #print("Ligne pas gagnante")
            
        if (line == column or (line + column == 3)) :
            if self.checkDiagonal(line, column) :
                #print("Diagonale gagnante")
                return True
            #else : 
                #print("Diagonale pas gagnante")    
        return False

    def showGrid(self) :
        """Affiche la grille"""
        print("      _\   0   |   1   |   2   |   3   |")
        for i in range(len(self.board)) :
            print("  ",i,end="  _ ")
            tmp = []
            for j in range(4) :
                if self.board[i][j] != None :
                    ind = int(self.board[i][j])
                    tmp.append(Piece.getPiece(ind).getPieceInfo[1])
                else :
                    tmp.append('    ')
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

    @property
    def getLinesToCheck(self) :
        """Renvoi l'ensemble des lignes que le jeu doit vérifier"""
        result = []
        line = []
        column,column1,column2,column3,column4 = ([] for i in range(5))
        diagonal,diag,antidiag = ([] for i in range(3))
        for i in range(4):
            line.append(self.getGrid[i])
            column1.append(self.getGrid[i][0])
            column2.append(self.getGrid[i][1])
            column3.append(self.getGrid[i][2])
            column4.append(self.getGrid[i][3])
            diag.append(self.getGrid[i][i])
            antidiag.append(self.getGrid[3-i][i])
        diagonal.append(diag)
        diagonal.append(antidiag)
        for concat in [column1,column2,column3,column4] :
            column.append(concat)
        result = line +column + diagonal
        return result
import time

if __name__ == "__main__":
    start_time = time.time()
    print('This file "plateau.py"  is ran directly')
    B = Board()
    #print(B.getGrid)
    B.placerPiece(pieces[0],0,0)
    B.placerPiece(pieces[1],1,1)
    B.placerPiece(pieces[2],2,2)
    B.placerPiece(pieces[3],3,3)
    B.placerPiece(pieces[5],1,2)
    print(B.getLinesToCheck)
    B.showGrid()
    print("--- %s seconds ---" % (time.time() - start_time))

