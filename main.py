from chess.board import Board


def main():

    board = Board()

    print("Initial Board:\n")
    board.print_board()

    
    pawn = board.get_piece("a2")

    print("\nMoving pawn at a2...\n")
    pawn.move()

    print("Board After Move:\n")
    board.print_board()


if __name__ == "__main__":
    main()
for state in Board.load_board_states():
    print(state)