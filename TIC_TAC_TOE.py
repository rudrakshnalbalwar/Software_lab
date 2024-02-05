import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if all(cell == row[0] and cell != ' ' for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(3)):
        return True
    if all(board[i][2 - i] == board[0][2] and board[i][2 - i] != ' ' for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            row, col = divmod(move - 1, 3)
            if 1 <= move <= 9 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Please choose an empty position.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_move(board):
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_positions)

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        # Player's move
        player_row, player_col = player_move(board)
        board[player_row][player_col] = 'X'
        print_board(board)

        if check_winner(board):
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        # Computer's move
        print("Computer's move:")
        computer_row, computer_col = computer_move(board)
        board[computer_row][computer_col] = 'O'
        print_board(board)

        if check_winner(board):
            print("Sorry, you lose. Better luck next time!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()