import random
import plateau
import copy as cp
class AI :
    def __init__(self, difficulty) :
        self.difficulty = difficulty

    def choosePiece(self, board, pieces) : 
        if self.difficulty == 0 :
            return pieces[0]

        if self.difficulty == 1 :
            return random.choice(pieces)

        if self.difficulty == 2 :
            #TODO
            
            return random.choice(pieces)


    def choosePosition(self, board, piece) : 
        if self.difficulty == 0 :
            return board.getAvailable[0]

        if self.difficulty == 1 :
            return random.choice(board.getAvailable)

        if self.difficulty == 2 :
            #TODO
            actionSet = self.miniMax(board,piece, 1)
            print("Action choisi par IA : ",actionSet)
            return (actionSet[1],actionSet[2])
            #return random.choice(board.getAvailable)


    def miniMax(self, board,piece, depth) :
        #return the a in Action(state) maximaxing Min_value(result(a,state))
        v ,actionSet = self.maxValue(board,depth, piece)
        return actionSet

        pass

    def maxValue(self, board,depth,piece = None, line = None, column = None) :
        print("current depth",depth)
        if len(board.getPieceRemained) == 0:
            return -self.evalValue(board, line, column), None
        if depth <= 0 :
            return self.evalValue(board, line, column), None
        bestValue = float("-inf")
        bestAction = (board.getPieceRemained[0],board.getAvailable[0][0],board.getAvailable[0][1])
        print(self.successors(board))
        for actionSet,nextBoard in self.successors(board) :
            currentMin = self.minValue(nextBoard, depth-1,line = actionSet[1], column = actionSet[2])
            print(actionSet)
            print("current min",currentMin)
            currentValue = currentMin[0]
            print("best :",bestValue)
            print(currentValue)
            if bestValue < currentValue:
                print("got replaced in maxValue")
                bestValue = currentValue
                bestAction = actionSet
        return bestValue, bestAction

    def minValue(self, board,depth,line = None, column = None) :
        print("current depth",depth)
        if depth <= 0 or len(board.getPieceRemained) == 0:
            return -self.evalValue(board, line, column), None
        bestValue = float("inf")
        bestAction = (board.getPieceRemained[0],board.getAvailable[0][0],board.getAvailable[0][1])
        for actionSet,nextBoard in self.successors(board) :
            currentMax = self.minValue(nextBoard, depth-1,line = actionSet[1], column = actionSet[2])
            print(actionSet)
            print("current max",currentMax)
            currentValue = currentMax[0]
            if bestValue > currentValue:
                print("got replaced in minValue")
                bestValue = currentValue
                bestAction = actionSet
        return bestValue, bestAction

    def evalValue(self, board, lastPlacedLine, lastPlacedColumn):

        #Case : Victory on this board
        #board.showGrid()
        if board.checkState(lastPlacedLine, lastPlacedColumn) :
            print("got to eval float")
            return float("inf")


        #here calculate eval 
        g = board.getGrid
        value = 0
        for lines in board.getLinesToCheck : 
            countNone = 0
            for i in range(4):
                if lines[i] == None :
                    countNone += 1            
            if countNone == 1 : #y'a 1 case vide pour win et j'veux pas que l'ennemy la
                addvalue = -30
            if countNone == 2 :
                addvalue = 20
            if countNone == 3 :
                addvalue = 10
            if countNone == 4 :
                addvalue = 5
            value += addvalue
        print(value)
        return value

    def successors(self , board, pieceGiven = None):
        """
        Return the set tuple (action, state) of all possibles boards
        from the current board
        action = (piece utilisé, ligne, colonne)
        """
        
        emptyCase = board.getAvailable
        result = []
        for place in (emptyCase):
            tmp_board = cp.deepcopy(board)
            if pieceGiven != None :
                #print((str(pieceGiven),place[0],place[1]))
                tmp_board.placerPiece(pieceGiven,place[0],place[1])
                action = (pieceGiven,place[0],place[1])
                result.append([action,tmp_board])
            else :
                for piece in tmp_board.getPieceRemained :
                    #print((str(piece),place[0],place[1]))
                    tmp_board.placerPiece(piece,place[0],place[1])
                    action = (piece,place[0],place[1])
                    result.append([action,tmp_board])

        #result = [  (used_piece, line, column) , [grid_obtained] ,  (used_piece, line, column) , [grid_obtained], ... ]
        #print("action possible :",result)
        return result