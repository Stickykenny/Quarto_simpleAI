import random
import copy as cp
from piece import *

class AI :
    def __init__(self, difficulty) :
        self.difficulty = difficulty
        self.nodeexplo = 0

    def choosePiece(self, board) : 
        if self.difficulty == 0 :
            return(board.getPiece(board.getPieceRemained[0]))

        if self.difficulty == 1 :
            return board.getPiece(random.choice(board.getPieceRemained))

        if self.difficulty == 2 :
            winning, notwinning = self.getListWinNeutral(board)
            
            if len(winning) == 0:
                return (board.getPiece(random.choice(notwinning)))
            if len(notwinning) == 0:
                return (board.getPiece(random.choice(winning)))

            if random.uniform(0, 1)> 0.75 :
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
        for line in toCheck :
            cur_points = [0,0,0,0]
            if None in line :
                countNone = 0
                
                for i in range(4):
                    if line[i] == None :
                        countNone += 1
                        continue
                    pieceValues = board.getPiece(line[i]).getPieceValue
                    for j in range(len(pieceValues)) :
                        intJ = int(j)
                        if pieceValues[intJ] == 1:
                            cur_points[intJ] += 1

                #Check all piece in possible winning place  
                
                if countNone == 1 :
                    for p in possible :
                        points= cp.deepcopy(cur_points)
                        piece =  board.getPiece(p).getPieceValue
                        for u in range(4) :
                            if piece[u] == 1:
                                points[u] += 1       
                        if 4 in points or 0 in points :

                            if p not in winningList:
                                winningList.append(p)
                           
        notwinningList = [item for item in possible if item not in winningList]
        
        return winningList, notwinningList


    def choosePosition(self, board, piece, turn) : 
        if self.difficulty == 0 :
            #Test difficulty
            actionSet = self.miniMax(board,piece, 2)[1]
            return (actionSet[1],actionSet[2])

        if turn < 3 :
                return random.choice(board.getAvailable)

        if self.difficulty == 1 :
            v, actionSet = self.miniMax(board,piece, 1)
            if v == 1000000 :
                return (actionSet[1],actionSet[2])
            return random.choice(board.getAvailable)

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


    def miniMax(self, board,piece, depth) :
        #return the a in Action(state) maximaxing Min_value(result(a,state))
        v ,actionSet = self.maxValue(board,depth,alpha=float("-inf"), beta=float("inf"),piece=piece)
        print("node explored",self.nodeexplo)
        self.nodeexplo = 0
        return v, actionSet


    def maxValue(self, board,depth,alpha, beta,piece = None) :
        if board.checkWin() :
            return -1000000, None
        if len(board.getPieceRemained) == 0:
            #Cas partie finie sans gagnant : Egalité (connoté négativement)
            return -500000, None
        if depth <= 0 :
            return self.evalValue(board, depth), None
        bestValue = float("-inf")
        bestAction = (board.getPieceRemained[0],board.getAvailable[0][0],board.getAvailable[0][1])

        for actionSet,nextBoard in self.successors(board, piece) :
            self.nodeexplo += 1
            currentMin = self.minValue(nextBoard, depth-1,alpha, beta)

            currentValue = currentMin[0]
 
            if bestValue < currentValue:
                bestValue = currentValue
                bestAction = actionSet


            if bestValue >= beta :

                return bestValue, bestAction
            alpha = max(alpha,bestValue)

        return bestValue, bestAction

    def minValue(self, board,depth,alpha, beta,piece = None) :
        if board.checkWin() :
        #Si la grille reçu est déjà gagnante, => ca veut dire que la grille faite par l'IA est gagnante
            
            return 1000000, None
        if len(board.getPieceRemained) == 0:
            #Cas partie finie sans gagnant : Egalité (connoté négativement)
            return -500000, None
        if depth <= 0 :
            return -self.evalValue(board, depth), None
    
        bestValue = float("inf")
        bestAction = (board.getPieceRemained[0],board.getAvailable[0][0],board.getAvailable[0][1])

        for actionSet,nextBoard in self.successors(board,piece) :
            self.nodeexplo += 1
            currentMax = self.maxValue(nextBoard, depth-1,alpha, beta)
            currentValue = currentMax[0]
            if bestValue > currentValue:
                bestValue = currentValue
                bestAction = actionSet

            if bestValue >= alpha :
                return bestValue, bestAction
            beta = max(beta,bestValue)

        return bestValue, bestAction

    def evalValue(self, board,depth):

        def checkAnySimilar(piece, model) :
            for i in range(4):
                if int(piece[i]) == model[i] :
                    return True

        if board.checkWin() :
            return 1000000

        value = 0
        
        if self.difficulty == 2 :
            
            for lines in board.getLinesToCheck : 
                countNone = 0
                addvalue = 0
                for i in range(4):
                    if lines[i] == None :
                        countNone += 1            
                if countNone == 1 : #y'a 1 case vide pour win et j'veux pas que l'ennemy la
                    addvalue = 400
                if countNone == 2 :
                    addvalue = -50
                if countNone == 3 :
                    addvalue = -100
                if countNone == 4 : #On veut garder le plus de ligne rempli de None
                    addvalue = -200
                value += addvalue

        if self.difficulty == 3 or self.difficulty == 0:
            for lines in board.getLinesToCheck : 
                countNone = 0
                addvalue = 0
                for i in range(4):
                    if lines[i] == None :
                        countNone += 1      
                compteur = [0,0,0,0]
                model = [5,5,5,5]
                notwinning = []
                winning = []


                if countNone == 1 : #pour remplir 3ème place
                    for i in lines : 
                        if i == None :
                            continue
                        i = bin(int(i))[2:].zfill(4)
                        for j in range(4) :
                            compteur[j] += int(i[j])
                            
                        for y in range(4):
                            if compteur[y]== 0 :
                                model[y] = 0
                            if compteur[y]== 3 : 
                                model[y] = 1
                    

                    for p in board.getPieceRemained : 
                        piece = bin(int(p))[2:].zfill(4)
                        
                        if checkAnySimilar(piece, model) :
                            winning.append(p)
                        else : 
                            notwinning.append(p)
                    """"
                    not winning après placer en 3eme place = [1,2,3]
                    IA donne 1
                    Nous on donne 2
                    IA donne 3 
                    Joueru donne gagnat à IA
                    => Si c'est impair => IA GAGNE
                    """
                    if len(notwinning) % 2 == 0 :
                        addvalue = -2000
                    else :
                        # priorité faible(ne las remmplir)
                        addvalue = +2000

                if countNone == 0 : #Cas bloquer une ligne
                    #Not win but filled
                    addvalue = 0
                
                                  
                if countNone == 2 :
                    addvalue = +300

                if countNone == 3 :
                    addvalue = +50

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
                    addvalue = 2    
                if countNone == 1 :
                    addvalue = 4
                if countNone == 2 :
                    addvalue = 6
                if countNone == 3 :
                    addvalue = 8
                if countNone == 4 :
                    addvalue = 10
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
        for place in (emptyCase):
            tmp_board = cp.deepcopy(board)
            
            if pieceGiven != None :
                piece = pieceGiven#board.getPiece(pieceGiven)
                tmp_board.placerPiece(piece,place[0],place[1])
                action = (piece,place[0],place[1])
                result.append([action,tmp_board])
            else :
                for piece in tmp_board.getPieceRemained :
                    tmp_board = cp.deepcopy(board)
                    tmp_board.placerPiece(tmp_board.getPiece(piece),place[0],place[1])
                    #print(tmp_board.getGrid)
                    #tmp_board.showGrid()
                    action = (piece,place[0],place[1])
                    result.append([action,tmp_board])


        return result

