import tkinter as tk
from tkinter import messagebox

def check_winner():
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] and row[0]["text"] != "":
            return row[0]["text"]
    for col in range(3):
        if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] and board[0][col]["text"] != "":
            return board[0][col]["text"]
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != "":
        return board[0][0]["text"]
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != "":
        return board[0][2]["text"]
    return None

def is_draw():
    for row in board:
        for cell in row:
            if cell["text"] == "":
                return False
    return True

def handle_click(row, col):
    global current_player

    if board[row][col]["text"] == "":
        board[row][col]["text"] = current_player
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
            return
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
            return
        current_player = "O" if current_player == "X" else "X"  # Switch player
        label_turn.config(text=f"Player {current_player}'s Turn")
    else:
        messagebox.showwarning("Invalid Move", "Cell already taken. Choose another.")

def reset_board():
    global current_player
    current_player = "X"
    label_turn.config(text=f"Player {current_player}'s Turn")
    for row in board:
        for cell in row:
            cell["text"] = ""

# Initialize GUI
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Current player (X starts first)
current_player = "X"

# Create a label to show the current turn
label_turn = tk.Label(root, text=f"Player {current_player}'s Turn", font=("Arial", 16))
label_turn.grid(row=0, column=0, columnspan=3)

# Create the Tic-Tac-Toe board as buttons
board = [[None for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        board[r][c] = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                                command=lambda row=r, col=c: handle_click(row, col))
        board[r][c].grid(row=r + 1, column=c)

# Add a reset button
reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14), command=reset_board)
reset_button.grid(row=4, column=0, columnspan=3)

# Start the GUI event loop
root.mainloop()
