from tkinter import *

#initial the main window
root = Tk()
root.geometry("330x550") #set the window size
root.title("Tic Tac Toe" ) #set the window title
root.resizable(0, 0) #disable window resizing

#frame for title
frame1 = Frame(root)
frame1.pack()
#label for the game title
titleLabel = Label(frame1, text="Tic Tac Toe", font=("Arial", 26), bg="purple", fg="white" , width=16)
titleLabel.grid(row=0, column=0)

#frame for the game mode selection
optionFrame = Frame(root, bg="grey")
optionFrame.pack()

#frame for game board
frame2 = Frame(root, bg="red")
frame2.pack()

#dictionary representing the board with positions from 1-9
board = {i: " " for i in range(1, 10)}
turn = "x"  #keep track of whose turn it
game_end = False  #flag to indicate game over
mode = "singlePlayer" #default game mode


#function to switch to singlePlayer mode
def changeModeToSinglePlayer():
    global mode 
    mode = "singlePlayer"
    singlePlayerButton["bg"] = "lightgreen"
    multiPlayerButton["bg"] = "lightgrey"


#function to switch to multiPlayer mode
def changeModeToMultiplayer():
    global mode 
    mode = "multiPlayer"
    multiPlayerButton["bg"] = "lightgreen"
    singlePlayerButton["bg"] = "lightgrey"


#function to update board display
def updateBoard():
    try:
        for key in board.keys():
            buttons[key - 1]["text"] = board[key]
    except Exception as e:
        print(f"Error updating board: {e}")


#function to check for win condition
def checkForWin(player):
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

#function to check if the game is a draw
def checkForDraw():
    return all(board[i] != " " for i in board)

#function to restart the game
def restartGame():
    global game_end
    game_end = False
    try:
        for button in buttons:
            button["text"] = " "
        for i in board.keys():
            board[i] = " "
        titleLabel.config(text="Tic Tac Toe")
    except Exception as e:
        print(f"Error restarting game: {e}")

#minimax algorithm 
def minimax(board, isMaximizing):
    try:
        if checkForWin("o"):
            return 1 
        if checkForWin("x"):
            return -1
        if checkForDraw():
            return 0
        bestScore = -100 if isMaximizing else 100
        for key in board.keys():
            if board[key] == " ":
                board[key] = "o" if isMaximizing else "x"
                score = minimax(board, not isMaximizing)
                board[key] = " "
                bestScore = max(bestScore, score) if isMaximizing else min(bestScore, score)
        return bestScore
    except Exception as e:
        print(f"Error in minimax: {e}")
        return 0

#function for computer move
def playComputer():
    try:
        bestMove = max((key for key in board.keys() if board[key] == " "), key=lambda k: minimax(board, False), default=None)
        if bestMove:
            board[bestMove] = "o"
    except Exception as e:
        print(f"Error playing computer move: {e}")

#function to handle player move
def play(event):
    global turn, game_end
    if game_end:
        return
    try:
        button = event.widget
        clicked = int(str(button)[-1]) if str(button)[-1].isdigit() else 1
        if button["text"] == " " and board.get(clicked, "") == " ":
            board[clicked] = turn
            updateBoard()
            if checkForWin(turn):
                titleLabel.config(text=f"{turn} wins the game")
                game_end = True
            elif checkForDraw():
                titleLabel.config(text="Game Draw")
            else:
                turn = "o" if turn == "x" else "x"
                if mode == "singlePlayer" and turn == "o":
                    playComputer()
                    updateBoard()
                    if checkForWin(turn):
                        titleLabel.config(text=f"{turn} wins the game")
                        game_end = True
                    turn = "x"
    except Exception as e:
        print(f"Error in play function: {e}")

                 # UI DESIGN...........

# Change Mode options
singlePlayerButton = Button(optionFrame , text="SinglePlayer" , width=13 , height=1 , font=("Arial" , 15) , bg="lightgrey" , relief=RAISED , borderwidth=5 , command=changeModeToSinglePlayer)
singlePlayerButton.grid(row=0 , column=0 , columnspan=1 , sticky=NW)

multiPlayerButton = Button(optionFrame , text="Multiplayer" , width=13 , height=1 , font=("Arial" , 15) , bg="lightgrey" , relief=RAISED , borderwidth=5 , command=changeModeToMultiplayer )
multiPlayerButton.grid(row=0 , column=1 , columnspan=1 , sticky=NW)

# Tic Tac Toe Board 

#  First row 

button1 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30) , bg="lightyellow" , relief=RAISED , borderwidth=5)
button1.grid(row = 0 , column=0)
button1.bind("<Button-1>" , play)

button2 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="lightyellow" , relief=RAISED , borderwidth=5 )
button2.grid(row = 0 , column=1)
button2.bind("<Button-1>" , play)

button3 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="lightyellow" , relief=RAISED , borderwidth=5 )
button3.grid(row = 0 , column=2)
button3.bind("<Button-1>" , play)

#  second row 

button4 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="lightyellow" , relief=RAISED , borderwidth=5 )
button4.grid(row = 1 , column=0)
button4.bind("<Button-1>" , play)

button5 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="lightyellow" , relief=RAISED , borderwidth=5 )
button5.grid(row = 1 , column=1)
button5.bind("<Button-1>" , play)

button6 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="lightyellow" , relief=RAISED , borderwidth=5 )
button6.grid(row = 1 , column=2)
button6.bind("<Button-1>" , play)

#  third row 

button7 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30) , bg="lightyellow" , relief=RAISED , borderwidth=5)
button7.grid(row = 2 , column=0)
button7.bind("<Button-1>" , play)

button8 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="lightyellow" , relief=RAISED , borderwidth=5 )
button8.grid(row = 2 , column=1)
button8.bind("<Button-1>" , play)

button9 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30) , bg="lightyellow" , relief=RAISED , borderwidth=5)
button9.grid(row = 2 , column=2)
button9.bind("<Button-1>" , play)

restartButton = Button(frame2 , text="Restart Game" , width=19 , height=1 , font=("Arial" , 20) , bg="Green" , fg="white",relief=RAISED , borderwidth=5 , command=restartGame )
restartButton.grid(row=4 , column=0 , columnspan=3)

buttons = [button1 , button2 , button3 , button4 , button5 , button6 , button7 , button8, button9]

root.mainloop()
