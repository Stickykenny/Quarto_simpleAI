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
            return random.choice(board.getAvailable)


    def miniMax(self, board, depth) :
        #return the a in Action(state) maximaxing Min_value(result(a,state))

        pass

    def maxValue(self, board,depth) :
        if depth <= 0 :
            return self.evalValue(board)
        value = float("-inf")
        for actionSet,newBoard in self.sucessors() :
            value = max(value, self.minValue(newBoard, depth-1)[0])
        return value, actionSet

    def minValue(self, board,depth) :
        if depth <= 0 :
            return -self.evalValue(board)
        value = float("inf")
        for actionSet,newBoard in self.sucessors() :
            value = max(value, self.maxValue(newBoard, depth-1)[0])
        return value, actionSet

    def evalValue(self, board, line, column):

        #Case : Victory on this board
        if board.checkState(board, line, column) :
            return float("inf")


        #here calculate eval 
        g = board.getGrid
        value = 10
        for i in range(4):
            
            pass
        pass

    def sucessors(self , board):
        """
        Return the set tuple (action, state) of all possibles boards
        from the current board
        action = (piece utilisé, ligne, colonne)
        """
        
        case_to_test = board.getAvailable
        result = []
        for place in range(case_to_test):
            for piece in tmp_board.getPieceRemained :
                tmp_board = cp.deepcopy(board)
                tmp_board.placerPiece(piece,place[0],place[1])
                action = (piece,place[0],place[1])
                result.append([action,tmp_board])

        #result = [  (used_piece, line, column) , [grid_obtained] ,  (used_piece, line, column) , [grid_obtained], ... ]
        print("action possible :",result)
        return result