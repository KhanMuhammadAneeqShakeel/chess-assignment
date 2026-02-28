from chess.pieces import Pawn, Rook, Bishop, Knight, Queen, King


class Board:

    def __init__(self):
    
        self.squares = {
            f"{chr(col)}{row}": None
            for col in range(ord('a'), ord('i'))
            for row in range(1, 9)
        }

    def setup_board(self):

        self.squares["a1"] = Rook("BLACK", 1)
        self.squares["b1"] = Knight("BLACK", 1)
        self.squares["c1"] = Bishop("BLACK", 1)
        self.squares["d1"] = Queen("BLACK", 1)
        self.squares["e1"] = King("BLACK", 1)
        self.squares["f1"] = Bishop("BLACK", 2)
        self.squares["g1"] = Knight("BLACK", 2)
        self.squares["h1"] = Rook("BLACK", 2)

        black_pawns = {
            f"{chr(col)}2": Pawn("BLACK", col - ord('a') + 1)
            for col in range(ord('a'), ord('i'))
        }

        self.squares.update(black_pawns)

     
        self.squares["a8"] = Rook("WHITE", 1)
        self.squares["b8"] = Knight("WHITE", 1)
        self.squares["c8"] = Bishop("WHITE", 1)
        self.squares["d8"] = Queen("WHITE", 1)
        self.squares["e8"] = King("WHITE", 1)
        self.squares["f8"] = Bishop("WHITE", 2)
        self.squares["g8"] = Knight("WHITE", 2)
        self.squares["h8"] = Rook("WHITE", 2)

        white_pawns = {
            f"{chr(col)}7": Pawn("WHITE", col - ord('a') + 1)
            for col in range(ord('a'), ord('i'))
        }

        self.squares.update(white_pawns)

    def print_board(self):
        for row in range(1, 9):
            current_row = [
                self.squares[f"{chr(col)}{row}"]
                for col in range(ord('a'), ord('i'))
            ]
            print(current_row)