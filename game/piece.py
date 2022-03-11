"""
Classe qui définit et instancie les pièces du jeux de Quarto
"""

class Piece :

    def __init__(self, id, color, size, form, top) :
        """
        color black = True
        size tall = True
        form square = True
        top hollow = True
        """
        self.id = id
        self.black = color
        self.tall = size
        self.square = form
        self.hollow = top
    @property
    def showPieceInfo(self) :
        print(self.id, self.black, self.tall, self.square, self.hollow)
        
    @property
    def getPieceInfo(self) :
        return [self.black,
            self.tall,
            self.square,
            self.hollow,]

    @staticmethod
    def getPiece(id) :
        return pieces[id]




#Instancie les pièces
pieces = [
Piece("0",  False ,False, False, False),
Piece("1",  False ,False, False, True ),
Piece("2",  False ,False, True , False),
Piece("3",  False ,False, True , True ),
Piece("4",  False ,True , False, False),
Piece("5",  False ,True , False, True ),
Piece("6",  False ,True , True , False),
Piece("7",  False ,True , True , True ),
    
Piece("8" , True  ,False, False, False),
Piece("9" , True  ,False, False, True ),
Piece("10", True  ,False, True , False),
Piece("11", True  ,False, True , True ),
Piece("12", True  ,True , False, False),
Piece("13", True  ,True , False, True ),
Piece("14", True  ,True , True , False),
Piece("15", True  ,True , True , True )
]
