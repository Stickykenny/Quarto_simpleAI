import plateau
import AI
from piece import *




#TODO interface
pieces_restantes = pieces.copy()
gameON = True
turn = 1
player_turn = 0

while gameON :
    print("----------------------------\nTurn ",turn,"\n ----------------------------")
    print("player ",player_turn,"'s turn to play select piece for player ",(player_turn+1)%2)
    print("Which pieces do u want the ennemy to play ?")

    #TODO Make it impossible to put impossible number, here or inside the function
    choice = int(input("Write the id : "))

    print("You've chosen ",Piece.getPiece(choice).showPieceInfo)

    #TODO Show Board 
    #TODO place piece on Board
    #TODO Verify win condition


    if turn >= 16 :
        gameON = False
        print("No one won")

    player_turn += 1
    turn = turn+1



#Still don't understand clearly how this part work, but I'm learning it
if __name__ == "__main__":
    print('This file "quarto.py"  is ran directly')
else:
    print('This file "quarto.py" was imported')