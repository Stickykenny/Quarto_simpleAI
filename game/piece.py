"""
Classe qui définit et instancie les pièces du jeux de Quarto
"""

class Piece :

    def __init__(self, id, affichage) :
        """
        color black = True
        size tall = True
        form square = True
        top hollow = True
        TODO R2EXPLIQUER affichage



        """
        self.id = id
        self.affichage = affichage
        self.value = [int(x) for x in self.affichage] 
      
    @property
    def showPieceInfo(self) :
        print(self.affichage)
        
    @property
    def getPieceInfo(self) :
        return [self.id,
            self.affichage]

    @property
    def getPieceValue(self) :
        return self.value

    @staticmethod
    def getPiece(id) :
        return pieces[id]




#Instancie les pièces
pieces = [
Piece("0","0000"),
Piece("1","0001"),
Piece("2","0010"),
Piece("3","0011"),
Piece("4","0100"),
Piece("5","0101"),
Piece("6","0110"),
Piece("7","0111"),
    
Piece("8","1000" ),
Piece("9","1001" ),
Piece("10","1010"),
Piece("11","1011"),
Piece("12","1100"),
Piece("13","1101"),
Piece("14","1110"),
Piece("15","1111")
]
