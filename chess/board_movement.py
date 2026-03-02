class BoardMovement:

    @staticmethod
    def forward(position: str, color: str, steps: int = 1):
        column = position[0]
        row = int(position[1])

        if color == "WHITE":
            new_row = row - steps
        else:
            new_row = row + steps

        return f"{column}{new_row}"

    @staticmethod
    def left(position: str, steps: int = 1):
        column = chr(ord(position[0]) - steps)
        row = position[1]
        return f"{column}{row}"

    @staticmethod
    def right(position: str, steps: int = 1):
        column = chr(ord(position[0]) + steps)
        row = position[1]
        return f"{column}{row}"