from abc import ABC, abstractmethod


class BaseChessPiece(ABC):

    def __init__(self, color: str, name: str, symbol: str, identifier: int):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.position = None
        self.is_alive = True

    @abstractmethod
    def move(self, movement: str):
       
        print(movement)

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
        movement = "Pawn moves forward 1 position"
        super().move(movement)


class Rook(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Rook", "R", identifier)

    def move(self):
        movement = "Rook moves in a straight line"
        super().move(movement)


class Bishop(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Bishop", "B", identifier)

    def move(self):
        movement = "Bishop moves diagonally"
        super().move(movement)