from chess.pieces import Pawn
from chess.pieces import Pawn, Rook, Bishop

pawn1 = Pawn("BLACK", 1)
pawn1.move()

print(pawn1)


pawn1 = Pawn("BLACK", 1)
rook1 = Rook("WHITE", 1)
bishop1 = Bishop("BLACK", 2)

pawn1.move()
rook1.move()
bishop1.move()

print(pawn1)
print(rook1)
print(bishop1)