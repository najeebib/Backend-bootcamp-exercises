from .modules.cell import Cell
from .modules.board import Board
from .modules.game_logic import get_rounds_from_user, get_position_from_user, ask_user_enter_cells, round

def main():
    rounds_number = get_rounds_from_user()

    board = Board()
    while ask_user_enter_cells():
        position = get_position_from_user()
        cell = board.get_cell(position)
        cell.change_status("alive")
    for _ in range(rounds_number):
        round(board=board)
        print(board)
if __name__ == "__main__":
    main()
