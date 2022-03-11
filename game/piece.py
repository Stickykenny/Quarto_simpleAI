"""
Classe qui définit et instancie les pièces du jeux de Quarto
"""

class Piece :

    def __init__(self, id, affichage, color, size, form, top) :
        """
        color black = True
        size tall = True
        form square = True
        top hollow = True
        """
        self.id = id
        self.affichage = affichage
        self.black = color
        self.tall = size
        self.square = form
        self.hollow = top

    @property
    def showPieceInfo(self) :
        print(self.affichage)
        
    @property
    def getPieceInfo(self) :
        return [self.id,
            self.affichage]

    @staticmethod
    def getPiece(id) :
        return pieces[id]




#Instancie les pièces
pieces = [
Piece("0","0000",  False ,False, False, False),
Piece("1","0001",  False ,False, False, True ),
Piece("2","0010",  False ,False, True , False),
Piece("3","0011",  False ,False, True , True ),
Piece("4","0100",  False ,True , False, False),
Piece("5","0101",  False ,True , False, True ),
Piece("6","0110",  False ,True , True , False),
Piece("7","0111",  False ,True , True , True ),
    
Piece("8","1000" , True  ,False, False, False),
Piece("9","1001" , True  ,False, False, True ),
Piece("10","1010", True  ,False, True , False),
Piece("11","1011", True  ,False, True , True ),
Piece("12","1100", True  ,True , False, False),
Piece("13","1101", True  ,True , False, True ),
Piece("14","1110", True  ,True , True , False),
Piece("15","1111", True  ,True , True , True )
]
