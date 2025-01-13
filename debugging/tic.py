#!/usr/bin/python3

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there's a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """Checks if the game is a draw (board is full and no winner)."""
    for row in board:
        if " " in row:  # If there's an empty space, the game is not a draw
            return False
    return True  # No empty spaces and no winner, it's a draw

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[" "]*3 for _ in range(3)]  # Initial empty board
    player = "X"
    
    while True:
        print_board(board)
        # Input validation loop for row and column
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                # Check if the input is within bounds
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input! Row and column must be between 0 and 2. Try again.")
                    continue
                
                # Check if the spot is already taken
                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue
                
                # If valid, make the move
                board[row][col] = player
                break
            except ValueError:
                print("Invalid input! Please enter numeric values between 0 and 2.")

        # Check if there's a winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
