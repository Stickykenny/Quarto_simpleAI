from plateau import *
import AI
from piece import *




#TODO interface
pieces_remained = pieces.copy()
board= Board()
gameON = True
turn = 1
player_turn = 0
board.showGrid()


while gameON :
    #TODO print different for player 2 ?
    print("----------------------------\nTour ",turn,"\n----------------------------")
    print("Joueur ",player_turn,"doit sélectionner une pièce pour le Joueur ",(player_turn+1)%2)
    print("Avec quel pièce l'adversaire doit-il jouer ?")

    chosenPiece = None
    choice = int(input("id de la piece [0-15]: "))

    while not(-1< choice < 16) or (chosenPiece not in pieces_remained): 

        
        if not(-1< choice < 16) :
            print("L'id selectionné n'est pas valide...")
            choice = int(input("id de la piece [0-15]: "))
            continue

        chosenPiece = Piece.getPiece(choice)

        if chosenPiece not in pieces_remained :
            print("La piece choisi n'est plus disponible...")
            choice = int(input("id de la piece [0-15]: "))
            continue

    print("Rappel vous avez choisi la pièce : ",chosenPiece.getPieceInfo)
    print("Joueur ",((player_turn+1)%2),"Choisir la case où vous devez déposer la piece")


    inputcorrect = False
    while not(inputcorrect) : 

        positionX = int(input("Ligne :   "))
        positionY = int(input("Colonne : "))
        if positionX >3 or positionX <0 or positionY >3 or positionY <0 :
            print("Merci d'entré une position valide... ")
            continue
    
        if board.placerPiece(chosenPiece, positionX, positionY) :
            inputcorrect = True
        else :
            print("Veuillez selectionner une case disponible...")
    
    pieces_remained.remove(chosenPiece)
    print("\n \nAffichage après avoir déposé la pièce")
    board.showGrid()

    if board.checkState(board, positionX, positionY)  : 
        print("Victoire du joueur ",player_turn)
        gameON = False

    if turn == 16 :
        print("PLUS DE PIECES DISPONIBLE!")
        gameON = False
        print("EGALITE")

    player_turn = (player_turn +1 )%2
    turn = turn+1



#Still don't understand clearly how this part work, but I'm learning it
if __name__ == "__main__":
    print('This file "quarto.py"  is ran directly')
else:
    print('This file "quarto.py" was imported')