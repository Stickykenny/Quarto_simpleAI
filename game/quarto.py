from plateau import *
from piece import *
from AI import *




#TODO interface
board= Board()
gameON = True
turn = 1
player_turn = 0

#TODO Choose IA difficulty, make it a while


print("1 - Difficulté Facile ")
print("2 - Difficulté Modéré  ")
print("3 - Difficulté Difficile  ")

difficulty = int(input("Choississez la difficulté : "))

while not(0<= difficulty < 4):
    print("Le niveau de diffuculté n'est pas valide...")
    difficulty = int(input("Choississez la difficulté : "))
    
current_ai = AI(difficulty)

play_order = 1#random.randint(0,1)
if play_order == 0: #Equivalent à un False
    print("L' Intelligence Artificiel commence en premier")
else : 
    print("Le Joueur comence en premier")

board.showGrid()

while gameON :
    #TODO print different for player 2 ?
    print("----------------------------\nTour ",turn,"\n----------------------------")
    
    # CHoix de la pièce
    if play_order :

        print("Vous devez sélectionner une pièce pour l'IA ")
        print("Avec quel pièce l'IA doit-il jouer ?")
        print("-- Pièce disponible [id, valeur]: ")

        print_iterator = 0
        for x in (board.getPieceRemained): 
            if print_iterator == 3 :
                print(x.getPieceInfo)
            else :
                print(x.getPieceInfo, end ='  ')
            print_iterator = (print_iterator+1) % 4

        chosenPiece = None
        choice = int(input("\nid de la piece [0-15]: "))

        while not(-1< choice < 16) or (chosenPiece not in board.getPieceRemained): 
            if not(-1< choice < 16) :
                print("L'id selectionné n'est pas valide...")
                choice = int(input("id de la piece [0-15]: "))
                continue
            chosenPiece = Piece.getPiece(choice)
            if chosenPiece not in board.getPieceRemained :
                print("La piece choisi n'est plus disponible...")
                choice = int(input("id de la piece [0-15]: "))
                continue

    else :
        chosenPiece = current_ai.choosePiece(board, board.getPieceRemained)
        print("L'IA vous a choisi la pièce : ",chosenPiece.getPieceInfo)
        print("Veuillez choisir la case où vous voulez déposer la piece")

    #Choix du placement 
    if not(play_order) :
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
    else :
        position = current_ai.choosePosition(board,chosenPiece)
        board.placerPiece(chosenPiece, position[0], position[1])
        print("L'IA à placer la pièce en (",position[0],",",position[1],")")
    
    print(" \nAffichage après avoir déposé la pièce")
    board.showGrid()
    if turn>3:
        if board.checkState(positionX, positionY)  : 
            if not(play_order) :
                print("Victoire du joueur !")
            else : 
                print("Défaite contre l'IA !")

            gameON = False

    if turn == 16 :
        print("PLUS DE PIECES DISPONIBLE!")
        gameON = False
        print("EGALITE")

    player_turn = (player_turn +1)%2
    turn = turn+1
    play_order = (play_order +1)%2 



x = input("Press enter to close the game")