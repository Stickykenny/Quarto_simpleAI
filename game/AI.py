import random

from pyparsing import WordStart
from piece import Piece
import plateau
import copy as cp
import numpy as np
class AI :
    def __init__(self, difficulty) :
        self.difficulty = difficulty

    def choosePiece(self, board) : 
        if self.difficulty == 0 :
            print(board.getPieceRemained[0])

        if self.difficulty == 1 :
            return board.getPiece(random.choice(board.getPieceRemained))

        if self.difficulty == 2 :
            winning, notwinning = self.getListWinNeutral(board)
            
            if len(winning) == 0:
                return (board.getPiece(random.choice(notwinning)))
            if len(notwinning) == 0:
                return (board.getPiece(random.choice(winning)))

            if random.uniform(0, 1)> 0.75 :
                #print("gave a winning piece")
                return  (board.getPiece(random.choice(winning)))
            else :
                return  (board.getPiece(random.choice(notwinning)))


        if self.difficulty == 3 :
            winning, notwinning = self.getListWinNeutral(board)
            if len(notwinning) == 0:
                return (board.getPiece(random.choice(winning)))
            return (board.getPiece(random.choice(notwinning)))


    def getListWinNeutral(self, board):
        toCheck = board.getLinesToCheck
        possible = board.getPieceRemained
        winningList = []
    
        # points = nb d'occurence d'un attribut sur le plateau et dont il est possible d'en profiter
        # points =  [ [occurence de valeur 0] ,  [occurence de valeur 1]  ]
        #print(toCheck)
        for line in toCheck :
            cur_points = [0,0,0,0]
            if None in line :
                #print("visiting this",line)
                countNone = 0
                
                for i in range(4):
                    if line[i] == None :
                        countNone += 1
                        continue
                    pieceValues = board.getPiece(line[i]).getPieceValue
                    #print("pv",pieceValues)
                    for j in range(len(pieceValues)) :
                        intJ = int(j)
                        if pieceValues[intJ] == 1:
                            cur_points[intJ] += 1
                #print("this line with 3 pieces has points ;", cur_points)

                #Check all piece in possible winning place  
                
                if countNone == 1 :
                    for p in possible :
                        points= cp.deepcopy(cur_points)
                        #print("deepcopy",points)
                        #print(p)
                        piece =  board.getPiece(p).getPieceValue
                        #print(piece)
                        for u in range(4) :
                            if piece[u] == 1:
                                points[u] += 1       
                        #print("value of this line  ",points) 
                        if 4 in points or 0 in points :

                            #print("cette pièce est gagnante",piece)
                            #print(winningList)
                            #print(possible)
                            winningList.append(p)
                            #possible.remove(piece)
                            #print("remove done")
                    

        # winningList , notwinningList
        notwinningList = [item for item in possible if item not in winningList]
        #print(winningList,"\nk",notwinningList)
        return winningList, notwinningList


    def choosePosition(self, board, piece, turn) : 
        if self.difficulty == 0 :
            return board.getAvailable[0]

        if turn < 3 :
                return random.choice(board.getAvailable)

        if self.difficulty == 1 :
            v, actionSet = self.miniMax(board,piece, 1)
            #print("v value", v)
            if v == 1000000 :
                #print("ct positif")
                #print(actionSet)
                return (actionSet[1],actionSet[2])
            return random.choice(board.getAvailable)
            #Il veut gagner si il le voit direct

        if self.difficulty == 2 :

            actionSet = self.miniMax(board,piece, 2)[1]
            return (actionSet[1],actionSet[2])
            
        if self.difficulty == 3 :
            
            if turn <=4 :
                actionSet = self.miniMax(board,piece, 2)[1]
                return (actionSet[1],actionSet[2])
            if turn <=7 :
                actionSet = self.miniMax(board,piece, 3)[1]
                return (actionSet[1],actionSet[2])
            else :
                actionSet = self.miniMax(board,piece, 4)[1]
                return (actionSet[1],actionSet[2])
            #TODO
            pass


    def miniMax(self, board,piece, depth) :
        #return the a in Action(state) maximaxing Min_value(result(a,state))
        v ,actionSet = self.maxValue(board,depth,alpha=float("-inf"), beta=float("inf"),piece=piece)
        return v, actionSet

        pass

    def maxValue(self, board,depth,alpha, beta,piece = None) :
        if len(board.getPieceRemained) == 0:
            return -self.evalValue(board, depth), None
        if depth <= 0 :
            return self.evalValue(board, depth), None
        if board.checkWin() :
            print("ce plateau gagne pas besoin de chercher plus loin/ in maxvalue")
            board.showGrid()
            return 1000000, None
        bestValue = float("-inf")
        bestAction = (board.getPieceRemained[0],board.getAvailable[0][0],board.getAvailable[0][1])
        #print(depth)
        bestb = board
        for actionSet,nextBoard in self.successors(board, piece) :
            currentMin = self.minValue(nextBoard, depth-1,alpha, beta)
            #print(actionSet, str(actionSet[0]))
            #print("current min",currentMin)
            currentValue = currentMin[0]
            #print("best :",bestValue)
            #print(currentValue)
            if bestValue < currentValue:
                #print("got replaced in maxValue")
                bestb = nextBoard
                bestValue = currentValue
                bestAction = actionSet
            

            if bestValue >= beta :
                #print("best val in maxval",bestValue, bestAction)
                #bestb.showGrid()
                return bestValue, bestAction
            alpha = max(alpha,bestValue)
        #print(bestAction)        
        #print("best val in maxval",bestValue, bestAction)
        #bestb.showGrid()
        return bestValue, bestAction

    def minValue(self, board,depth,alpha, beta,piece = None) :
        if depth <= 0 or len(board.getPieceRemained) == 0:
            return -self.evalValue(board, depth), None
        if board.checkWin() :
            print("ce plateau gagne pas besoin de chercher plus loin")
            board.showGrid()
            return -1000000, None
        bestValue = float("inf")
        bestAction = (board.getPieceRemained[0],board.getAvailable[0][0],board.getAvailable[0][1])
        #print(depth)
        bestb = board
        for actionSet,nextBoard in self.successors(board,piece) :
            currentMax = self.maxValue(nextBoard, depth-1,alpha, beta)
            #print(actionSet, str(actionSet[0]))
            #print("current max",currentMax)
            currentValue = currentMax[0]
            if bestValue > currentValue:
                #print("got replaced in minValue")
                bestValue = currentValue
                bestAction = actionSet
            
            if bestValue >= alpha :
                #print("best val in minval",bestValue, bestAction)
                #bestb.showGrid()
                return bestValue, bestAction
            beta = max(beta,bestValue)
        #print("BESTBEST ===========",bestValue, bestAction)  
        #bb.showGrid()   
        #print("best val in minval",bestValue, bestAction)
        #bestb.showGrid()
        return bestValue, bestAction

    def evalValue(self, board,depth):

        if board.checkWin() :
            #print("win trouvé")
            #board.showGrid()
            #POSITIF
            return -1000000


        #here calculate eval 
        g = board.getGrid
        value = 0
        
        if self.difficulty == 2 :
            
            for lines in board.getLinesToCheck : 
                countNone = 0
                addvalue = 0
                for i in range(4):
                    if lines[i] == None :
                        countNone += 1            
                if countNone == 1 : #y'a 1 case vide pour win et j'veux pas que l'ennemy la
                    addvalue = -400
                if countNone == 2 :
                    addvalue = 50
                if countNone == 3 :
                    addvalue = 100
                if countNone == 4 : #On veut garder le plus de ligne rempli de None
                    addvalue = 200
                value += addvalue

        if self.difficulty == 3 :
            #Cherche à disperser le plus
            for lines in board.getLinesToCheck : 
                countNone = 0
                addvalue = 0
                winning, notwinning =  self.getListWinNeutral(board)
                turn = len(winning) + len(notwinning)
                for i in range(4):
                    if lines[i] == None :
                        countNone += 1      
                if countNone == 0 : #Not win but filled

                #si c'est impair on lui file pièce qui gagne pas, et lui forcément il nous reste que pièce qui gagne
                    #test ex si il reste 2 pièce qui ne gagne pas
                    """
                    - on fournit la pièce qui ne gagne pas
                    - le joueur fournit l'autre pièce
                    - on est obligé de fournit pièce gagnante
                    """
                    #print("line empty test",lines,notwinning)
                    if len(notwinning) % 2 == 0 :
                        addvalue = -600
                    else : 
                        # priorité faible(ne las remmplir)
                        addvalue = +200
                    
                if countNone == 1 : #pour remplir 3ème place
                    """[pair win impair lose]
                    list piece restante [1,2,3,4,5] (2pair) (3impair)
                    [10,12,6,' '] 

                    donne 1
                    recoit 3
                    donne 5
                    recoit un truc qui gagne"""

                    if len(notwinning) % 2 == 0 :
                        addvalue = +600
                    else :
                        # priorité faible(ne las remmplir)
                        addvalue = -500
                                  
                if countNone == 2 :
                    addvalue = -300

                if countNone == 3 :
                    addvalue = -50

                if countNone == 4 : #veut-elle laissé des lignes vides
                    addvalue = 0
                    
                value += addvalue


#Test
        if self.difficulty == 5:
            #Cherche à disperser le plus
            for lines in board.getLinesToCheck : 
                countNone = 0
                addvalue = 0
                for i in range(4):
                    if lines[i] == None :
                        countNone += 1      
                if countNone == 0 :
                    addvalue = -2    
                if countNone == 1 :
                    addvalue = -4
                if countNone == 2 :
                    addvalue = -6
                if countNone == 3 :
                    addvalue = -8
                if countNone == 4 :
                    addvalue = -10
                value += addvalue


        #board.showGrid()
        #print(value)
        return value

    def successors(self , board, pieceGiven = None):
        """
        Return the set tuple (action, state) of all possibles boards
        from the current board
        action = (piece_id utilisé, ligne, colonne)
        """
        
        emptyCase = board.getAvailable
        result = []
        #print("givenpiece : ",pieceGiven)
        for place in (emptyCase):
            tmp_board = cp.deepcopy(board)
            
            if pieceGiven != None :
                #print("entrered !=None")
                #print((str(pieceGiven),place[0],place[1]))
                piece = pieceGiven#board.getPiece(pieceGiven)
                tmp_board.placerPiece(piece,place[0],place[1])
                action = (piece,place[0],place[1])
                result.append([action,tmp_board])
            else :
                for piece in tmp_board.getPieceRemained :
                    tmp_board = cp.deepcopy(board)
                    #print((piece,place[0],place[1]))
                    #print(tmp_board.getPiece(piece))
                    #print(tmp_board.getPiece(piece).id)
                    tmp_board.placerPiece(tmp_board.getPiece(piece),place[0],place[1])
                    #print(tmp_board.getGrid)
                    #tmp_board.showGrid()
                    action = (piece,place[0],place[1])
                    result.append([action,tmp_board])

        #result = [  (used_piece, line, column) , [grid_obtained] ,  (used_piece, line, column) , [grid_obtained], ... ]
        #print("action possible :",result)
        #for i in result :
        #    print(i[1].showGrid())
        return result