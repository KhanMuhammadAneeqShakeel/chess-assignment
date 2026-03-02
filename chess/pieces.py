import json
from abc import ABC
from chess.board_movement import BoardMovement


class BaseChessPiece(dict, ABC):

    def __init__(self, color: str, name: str, symbol: str, identifier: int):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.position = None
        self.board = None
        self.is_alive = True

        dict.__init__(
            self,
            color=color,
            name=name,
            symbol=symbol,
            identifier=identifier,
        )

    def set_initial_position(self, position: str):
        self.position = position

    def define_board(self, board):
        self.board = board

    def move(self, new_position: str):

        if self.board is None:
            print("Board not defined for this piece")
            return

        if new_position not in self.board.squares:
            print("Invalid move (outside board)")
            return

        target_piece = self.board.get_piece(new_position)

        if target_piece is not None:
            if target_piece.color != self.color:
                target_piece.die()
            else:
                print("Cannot move to square occupied by your own piece")
                return

        self.board.squares[self.position] = None
        self.position = new_position
        self.board.squares[new_position] = self

        print(f"{self.name} moved to {self.position}")
        self.board.save_board()

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"


class Pawn(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Pawn", "-", identifier)

    def move(self):
        movement = BoardMovement.forward(self.position, self.color, 1)
        super().move(movement)


class Rook(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Rook", "R", identifier)

    def move(self, direction: str, steps: int):

        column = self.position[0]
        row = int(self.position[1])

        if direction == "up":
            row += steps
        elif direction == "down":
            row -= steps
        elif direction == "left":
            column = chr(ord(column) - steps)
        elif direction == "right":
            column = chr(ord(column) + steps)

        new_position = f"{column}{row}"
        super().move(new_position)


class Bishop(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Bishop", "B", identifier)

    def move(self, direction: str, steps: int):

        column = ord(self.position[0])
        row = int(self.position[1])

        if direction == "up-right":
            column += steps
            row += steps
        elif direction == "up-left":
            column -= steps
            row += steps
        elif direction == "down-right":
            column += steps
            row -= steps
        elif direction == "down-left":
            column -= steps
            row -= steps

        new_position = f"{chr(column)}{row}"
        super().move(new_position)


class Knight(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Knight", "N", identifier)

    def move(self, direction: str):

        column = ord(self.position[0])
        row = int(self.position[1])

        if direction == "up-right":
            column += 1
            row += 2
        elif direction == "up-left":
            column -= 1
            row += 2
        elif direction == "down-right":
            column += 1
            row -= 2
        elif direction == "down-left":
            column -= 1
            row -= 2

        new_position = f"{chr(column)}{row}"
        super().move(new_position)


class Queen(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Queen", "Q", identifier)

    def move(self, direction: str, steps: int):

        column = ord(self.position[0])
        row = int(self.position[1])

        if direction == "up":
            row += steps
        elif direction == "down":
            row -= steps
        elif direction == "left":
            column -= steps
        elif direction == "right":
            column += steps
        elif direction == "up-right":
            column += steps
            row += steps
        elif direction == "up-left":
            column -= steps
            row += steps
        elif direction == "down-right":
            column += steps
            row -= steps
        elif direction == "down-left":
            column -= steps
            row -= steps

        new_position = f"{chr(column)}{row}"
        super().move(new_position)


class King(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "King", "K", identifier)

    def move(self, direction: str):

        column = ord(self.position[0])
        row = int(self.position[1])

        if direction == "up":
            row += 1
        elif direction == "down":
            row -= 1
        elif direction == "left":
            column -= 1
        elif direction == "right":
            column += 1
        elif direction == "up-right":
            column += 1
            row += 1
        elif direction == "up-left":
            column -= 1
            row += 1
        elif direction == "down-right":
            column += 1
            row -= 1
        elif direction == "down-left":
            column -= 1
            row -= 1

        new_position = f"{chr(column)}{row}"
        super().move(new_position)