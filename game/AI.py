import random
import plateau
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
        v = float("-inf")
        for a,s in self.sucessors() :
            v = max(v, self.minValue(s))
        return v
        pass

    def minValue(self, board,depth) :
        if depth <= 0 :
            return -self.evalValue(board)
        v = float("inf")
        for a,s in self.sucessors() :
            v = max(v, self.maxValue(s))
        return v
        pass

    def evalValue(self, board, line, column):

        #Case : Victory on this board
        if board.checkState(board, line, column) :
            return float("inf")


        #here calculate eval 
        g = board.getGrid
        for i in range(4):
            pass
        pass

    def sucessors(self , board):
        pass