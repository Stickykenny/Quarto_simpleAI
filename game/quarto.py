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
    print("----------------------------\nTour ",turn,"\n ----------------------------")
    print("Joueur ",player_turn," doit sélectionner une pièce pour le Joueur ",(player_turn+1)%2)
    print("Avec quel pièce l'adversaire doit-il jouer ?")

    #TODO Make it impossible to put impossible number, here or inside the function


    # RENDRE IMPOSSIBLE DE REPRENDRE LA MEME PIECE
    choice = int(input("id de la piece [0-15]: "))

    while not(-1< choice < 16): #bloquer Id erroné

        print("L'id selectionné n'est pas valide ")
        choice = int(input("id de la piece [0-15]: "))

    chosenPiece = Piece.getPiece(choice)
    
    while chosenPiece not in pieces_remained :
        print("La piece choisi n'est plus disponible")
        choice = int(input("id de la piece : ")) # afficher 0 -15 
        chosenPiece = Piece.getPiece(choice)


    print("Rappel vous avez choisi la pièce : ",chosenPiece.getPieceInfo) # changer affichage après ?
    
    print("Joueur ",player_turn,"Choisir la case où vous devez déposer la piece")

    #TODO do while case existante <4
    inputcorrect = False
    while not(inputcorrect) : 

        positionX = int(input("Ligne : "))
        positionY = int(input("Colonne :"))
        if positionX >3 or positionX <0 or positionY >3 or positionY <0 :
            print("Merci d'entré une position valide ")
            continue
    
        if board.placerPiece(chosenPiece, positionX, positionY) :
            #redemander 
            inputcorrect = True
        else :
            print("Veuillez selectionner une case disponible ")
    
    pieces_remained.remove(chosenPiece)
    print("\n \nAffichage apre avoir deposé la pièce")
    board.showGrid()

    #TODO Faire la fct checkState
    if board.checkState(chosenPiece, positionX, positionY) : 
        print("Victoire du joueur ",player_turn)

    if turn == 16 : #Jsp si c'est 16 ou autre
        print("PLUS DE PIECES DISPO!")
        
        gameON = False
        print("EGALITE")

    player_turn = (player_turn +1 )%2
    turn = turn+1



#Still don't understand clearly how this part work, but I'm learning it
if __name__ == "__main__":
    print('This file "quarto.py"  is ran directly')
else:
    print('This file "quarto.py" was imported')