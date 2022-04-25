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
            winning, notwinning = self.getListWinLose(board)
            
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
            winning, notwinning = self.getListWinLose(board)
            if len(notwinning) == 0:
                return (board.getPiece(random.choice(winning)))
            return (board.getPiece(random.choice(notwinning)))


    def getListWinLose(self, board):
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

            if turn == 1 :
                return random.choice(board.getAvailable)
            actionSet = self.miniMax(board,piece, 2)[1]
            return (actionSet[1],actionSet[2])
            
        if self.difficulty == 3 :
            if turn == 1 :
                return random.choice(board.getAvailable)
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
        bestValue = float("-inf")
        bestAction = (board.getPieceRemained[0],board.getAvailable[0][0],board.getAvailable[0][1])
        #print(depth)
        for actionSet,nextBoard in self.successors(board, piece) :
            currentMin = self.minValue(nextBoard, depth-1,alpha, beta)
            #print(actionSet, str(actionSet[0]))
            #print("current min",currentMin)
            currentValue = currentMin[0]
            #print("best :",bestValue)
            #print(currentValue)
            if bestValue < currentValue:
                #print("got replaced in maxValue")
                bestValue = currentValue
                bestAction = actionSet
            if bestValue >= beta :
                return bestValue, bestAction
            alpha = max(alpha,bestValue)
        #print(bestAction)        
        return bestValue, bestAction

    def minValue(self, board,depth,alpha, beta,piece = None) :
        if depth <= 0 or len(board.getPieceRemained) == 0:
            return -self.evalValue(board, depth), None
        bestValue = float("inf")
        bestAction = (board.getPieceRemained[0],board.getAvailable[0][0],board.getAvailable[0][1])
        #print(depth)
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
                return bestValue, bestAction
            beta = max(beta,bestValue)
        #print("BESTBEST ===========",bestValue, bestAction)  
        #bb.showGrid()   
        return bestValue, bestAction

    def evalValue(self, board,depth, comportement = 3):

        """
        TODO MAKE A PROPER EVAL TEST
        """
        #Evaluate the board for the next turn

        #if board.checkWin() :
        #    if depth %2 == 0 :
        #    #print("got to eval float")
        #        return -99999999999999999999999
        #    else : 
        #        return 99999999999999999999999

        #Case : Victory on this board
        #board.showGrid()
        if board.checkWin() :
            #print("win trouvé")
            #board.showGrid()
            #POSITIF
            return -1000000


        #here calculate eval 
        g = board.getGrid
        value = 0
        
        if comportement == 2 :
            
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

        if comportement == 3 :
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