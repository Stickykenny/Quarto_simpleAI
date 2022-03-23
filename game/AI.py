import random
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

