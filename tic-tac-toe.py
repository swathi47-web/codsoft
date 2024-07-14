import tkinter as tk
import random
import pygame

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Global variables
board = [" " for _ in range(9)]
currentPlayer = "X"
winner = None
gameRunning = True

# Initialize Pygame mixer
pygame.mixer.init()

# Load and play background music
pygame.mixer.music.load(r'C:\Users\HP\Downloads\Feel-Good(chosic.com).mp3')  # Ensure the file path is correct
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely


# Functions to handle the game logic
def checkWinner():
    global winner, gameRunning
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] and board[cond[0]] != " ":
            winner = board[cond[0]]
            gameRunning = False
            displayWinner()
            return True
    if " " not in board:
        winner = "Tie"
        gameRunning = False
        displayWinner()
        return True
    return False

def displayWinner():
    if winner == "Tie":
        label.config(text="It's a Tie!")
    else:
        label.config(text=f"The winner is {winner}!")

def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"
    label.config(text=f"Player {currentPlayer}'s turn")

def playerMove(index):
    if gameRunning and board[index] == " ":
        board[index] = currentPlayer
        buttons[index].config(text=currentPlayer)
        if not checkWinner():
            switchPlayer()
            computerMove()

def computerMove():
    bestMove = getBestMove()
    if bestMove is not None:
        board[bestMove] = "O"
        buttons[bestMove].config(text="O")
        if not checkWinner():
            switchPlayer()

def getBestMove():
    # Check if computer can win in the next move
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if isWinner("O"):
                board[i] = " "
                return i
            board[i] = " "

    # Check if player can win in the next move and block them
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if isWinner("X"):
                board[i] = " "
                return i
            board[i] = " "

    # Otherwise, choose a random available spot
    available_moves = [i for i, x in enumerate(board) if x == " "]
    return random.choice(available_moves) if available_moves else None

def isWinner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] and board[cond[0]] == player:
            return True
    return False

# Setting up the GUI
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2,
                       command=lambda i=i: playerMove(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

label = tk.Label(root, text="Player X's turn", font=('normal', 20))
label.grid(row=3, column=0, columnspan=3)

# Start the main loop
root.mainloop()

# Quit pygame when the game window is closed
pygame.mixer.music.stop()
pygame.quit()
