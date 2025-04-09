import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell==player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all (board[i][2-i] == player for i in range(3)):
        return True

    return False

def get_player_move(board):
    while True:
        try:
            move= int(input("Podaj numer pola(1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("to pole jest już zajęte, wybierz inne.")
        except (ValueError, IndexError):
            print("Nieprawidłowy ruch, spróbuj ponownie.")

def get_computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    mode = input("Wybierz tryb gry: 1 - dwóch graczy, 2 - gra z komputerem: ")
    against_computer = mode == "2"

    for turn in range(9):
        current_player = players[turn % 2]

        if against_computer and current_player == "O":
            print("Ruch komputera...")
            row, col = get_computer_move(board)
        else:
            print(f"Ruch gracza {current_player}.")
            row, col = get_player_move(board)

        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print_board(board)
            print(f"Gracz {current_player} wygrał!")
            return

    print_board(board)
    print("Remis!")

if __name__ == "__main__":
    tic_tac_toe()