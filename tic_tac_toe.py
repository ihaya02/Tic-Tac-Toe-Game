import numpy as np

board = np.full((3, 3), ' ')

def print_board():
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(player):
    for i in range(3):
        if all(board[i, :] == player) or all(board[:, i] == player):
            return True

    if all(np.diag(board) == player) or all(np.diag(np.fliplr(board)) == player):
        return True

    return False

def is_draw():
    return ' ' not in board

player = 'X'

while True:
    print_board()
    try:
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))
    except ValueError:
        print("Please enter numbers only.")
        continue

    if row not in range(3) or col not in range(3):
        print("Invalid position. Choose numbers between 0 and 2.")
        continue

    if board[row, col] != ' ':
        print("This spot is already taken. Try again.")
        continue

    board[row, col] = player

    if check_winner(player):
        print_board()
        print(f"Player {player} wins!")
        break

    if is_draw():
        print_board()
        print("It's a draw!")
        break

    player = 'O' if player == 'X' else 'X'
