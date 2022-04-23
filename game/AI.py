import random
from piece import Piece
import plateau
import copy as cp
import numpy as np
class AI :
    def __init__(self, difficulty) :
        self.difficulty = difficulty

    def choosePiece(self, board) : 
        if self.difficulty == 0 :
            #print(board.getPieceRemained[0])
            return board.getPiece(self.chooseWorstPiece(board))

        if self.difficulty == 1 :
            return board.getPiece(random.choice(board.getPieceRemained))

        if self.difficulty == 2 :
            #TODO
            #return board.getPiece(self.chooseWorstPiece(board))
            return board.getPiece(random.choice(board.getPieceRemained))

    def chooseWorstPiece(self, board):
        toCheck = board.getLinesToCheck
        possible = board.getPieceRemained

        #points = nb d'occurence d'un attribut sur le plateau et dont il est possible d'en profiter
        # points =  [ [occurence de valeur 0] ,  [occurence de valeur 1]  ]
        points = [[0,0,0,0],[0,0,0,0]]
        for line in toCheck :
            if None in line :
                for i in range(4):
                    if i == None :
                        continue
                    pieceValues = board.getPiece(i).getPieceValue
                    print("pv",pieceValues)
                    for j in range(len(pieceValues)) :
                        intJ = int(j)
                        if pieceValues[intJ] == 1:
                            points[1][intJ] += 1
                        else :
                            points[0][intJ] += 1

        print(points)
        print("===============points======================")
        worstPieceID = possible[0]
        worstValue = float("inf")
        for p in possible :
            current = bin(p)[2:].zfill(4)
            print("cur",current)
            currentValue = 0
            for i in current :
                if i == "0" :
                    currentValue += points[0][int(i)]
                else : 
                    currentValue += points[1][int(i)]
            print(currentValue)
            if worstValue > currentValue :
                print("changed ",worstPieceID, "to this :",p)
                worstPieceID = p
                worstValue = currentValue
        print("returned this piece :",worstPieceID, " / with value of :",worstValue)
        return worstPieceID

    def choosePosition(self, board, piece) : 
        if self.difficulty == 0 :
            return board.getAvailable[0]

        if self.difficulty == 1 :
            return random.choice(board.getAvailable)

        if self.difficulty == 2 :
            #TODO
            actionSet = self.miniMax(board,piece, 2)
            #print("Action choisi par IA : ",actionSet)
            return (actionSet[1],actionSet[2])
            #return random.choice(board.getAvailable)


    def miniMax(self, board,piece, depth) :
        #return the a in Action(state) maximaxing Min_value(result(a,state))
        v ,actionSet = self.maxValue(board,depth, piece)
        return actionSet

        pass

    def maxValue(self, board,depth,piece = None) :
        if len(board.getPieceRemained) == 0:
            return -self.evalValue(board), None
        if depth <= 0 :
            return self.evalValue(board), None
        bestValue = float("-inf")
        bestAction = (board.getPieceRemained[0],board.getAvailable[0][0],board.getAvailable[0][1])
        for actionSet,nextBoard in self.successors(board, piece) :
            currentMin = self.minValue(nextBoard, depth-1)
            #print(actionSet, str(actionSet[0]))
            #print("current min",currentMin)
            currentValue = currentMin[0]
            #print("best :",bestValue)
            #print(currentValue)
            if bestValue < currentValue:
                #print("got replaced in maxValue")
                bestValue = currentValue
                bestAction = actionSet
        #print(bestAction)        
        return bestValue, bestAction

    def minValue(self, board,depth,piece = None) :
        if depth <= 0 or len(board.getPieceRemained) == 0:
            return -self.evalValue(board), None
        bestValue = float("inf")
        bestAction = (board.getPieceRemained[0],board.getAvailable[0][0],board.getAvailable[0][1])
        for actionSet,nextBoard in self.successors(board,piece) :
            currentMax = self.maxValue(nextBoard, depth-1)
            #print(actionSet, str(actionSet[0]))
            #print("current max",currentMax)
            currentValue = currentMax[0]
            if bestValue > currentValue:
                #print("got replaced in minValue")
                bestValue = currentValue
                bestAction = actionSet
                #bb = nextBoard
        #print("BESTBEST ===========",bestValue, bestAction)  
        #bb.showGrid()   
        return bestValue, bestAction

    def evalValue(self, board):

        """
        TODO MAKE A PROPER EVAL TEST
        """
        #Evaluate the board for the next turn


        #Case : Victory on this board
        #board.showGrid()
        if board.checkWin() :
            #print("got to eval float")
            return 1000


        #here calculate eval 
        g = board.getGrid
        value = 0
        for lines in board.getLinesToCheck : 
            countNone = 0
            addvalue = 0
            for i in range(4):
                if lines[i] == None :
                    countNone += 1            
            if countNone == 1 : #y'a 1 case vide pour win et j'veux pas que l'ennemy la
                addvalue = -30
            if countNone == 2 :
                addvalue = 20
            if countNone == 3 :
                addvalue = -10
            if countNone == 4 :
                addvalue = -1
            value += addvalue
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
                #print((str(pieceGiven),place[0],place[1]))
                piece = pieceGiven#board.getPiece(pieceGiven)
                tmp_board.placerPiece(piece,place[0],place[1])
                action = (piece,place[0],place[1])
                result.append([action,tmp_board])
            else :
                for piece in tmp_board.getPieceRemained :
                    #print((str(piece),place[0],place[1]))
                    tmp_board.placerPiece(board.getPiece(piece),place[0],place[1])
                    action = (piece,place[0],place[1])
                    result.append([action,tmp_board])

        #result = [  (used_piece, line, column) , [grid_obtained] ,  (used_piece, line, column) , [grid_obtained], ... ]
        #print("action possible :",result)
        #for i in result :
        #    print(i[1].showGrid())
        return result