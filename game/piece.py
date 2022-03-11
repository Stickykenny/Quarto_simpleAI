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
Piece("0000",  False ,False, False, False),
Piece("0001",  False ,False, False, True ),
Piece("0010",  False ,False, True , False),
Piece("0011",  False ,False, True , True ),
Piece("0100",  False ,True , False, False),
Piece("0101",  False ,True , False, True ),
Piece("0110",  False ,True , True , False),
Piece("0111",  False ,True , True , True ),
    
Piece("1000" , True  ,False, False, False),
Piece("1001" , True  ,False, False, True ),
Piece("1010", True  ,False, True , False),
Piece("1011", True  ,False, True , True ),
Piece("1100", True  ,True , False, False),
Piece("1101", True  ,True , False, True ),
Piece("1110", True  ,True , True , False),
Piece("1111", True  ,True , True , True )
]
