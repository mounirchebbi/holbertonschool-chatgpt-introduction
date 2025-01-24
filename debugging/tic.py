#!/usr/bin/python3
def print_board(board):
    """
    Print the current state of the Tic-tac-toe board.
    
    Args:
        board (list): 3x3 list representing the game board
    """
    print("\nCurrent Board:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Don't print line after the last row
            print("-" * 9)

def check_winner(board):
    """
    Check if there's a winner in the current board state.
    
    Args:
        board (list): 3x3 list representing the game board
        
    Returns:
        bool: True if there's a winner, False otherwise
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if (board[0][col] == board[1][col] == board[2][col] 
            and board[0][col] != " "):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Check if the board is full (draw condition).
    
    Args:
        board (list): 3x3 list representing the game board
        
    Returns:
        bool: True if board is full, False otherwise
    """
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """
    Main game function for Tic-tac-toe.
    Handles game loop and player turns.
    """
    # Initialize empty 3x3 board
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    print("Welcome to Tic-tac-toe!")
    print("Players take turns entering row and column numbers (0-2)")
    
    while True:
        print_board(board)
        
        # Get player input
        try:
            print(f"\nPlayer {player}'s turn")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            # Validate input
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid input! Row and column must be between 0 and 2.")
                continue
                
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
                
            # Make move
            board[row][col] = player
            
            # Check for winner
            if check_winner(board):
                print_board(board)
                print(f"\nCongratulations! Player {player} wins!")
                break
                
            # Check for draw
            if is_board_full(board):
                print_board(board)
                print("\nGame Over! It's a draw!")
                break
                
            # Switch players
            player = "O" if player == "X" else "X"
            
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        except IndexError:
            print("Invalid input! Row and column must be between 0 and 2.")

if __name__ == "__main__":
    try:
        tic_tac_toe()
    except KeyboardInterrupt:
        print("\nGame terminated by user.")
