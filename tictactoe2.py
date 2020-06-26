import random
import sys
# Display
def displayMenu():
    print("Menu".center(50, "="))
    print("""
    1. Tictactoe
    2. Rock Paper Scissors
    3. Quit
    """)


def displayLeaderboard():
    print("Leaderboard".center(50, "="))

# Tictactoe board
board = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}

def theBoard(board):
    print(board["1"] + "|", board["2"] + "|", board["3"] + "|")
    print('=' * 9) 
    print(board["4"] + "|", board["5"] + "|", board["6"] + "|")
    print('=' * 9) 
    print(board["7"] + "|", board["8"] + "|", board["9"] + "|")

# Rock Paper Scissors
# [x] [Ignore] First, it asks if you are ready
# [y] Second, it asks if you want to pick rock, paper or scissors
# [y] Tells you who won
# [x] [Ignore] Asks if you want to do another around, if not stop
player_weapons = {"1":"Rock", "2":"Paper", "3":"Scissors"}
computer_weapons = {"1":"Scissors", "2":"Rock", "3": "Paper"}
def rps():
    while True:
        player_weapon = input("Choose Rock[1] Paper[2] Scissors[3]: ")
        computer_weapon = random.choice(list(computer_weapons))
        print(f"The computer chose: {computer_weapon}")
# Winning scenarios
    if player_weapon == "1" and computer_weapon == "1":
        print("You Win!")
    elif player_weapon == "2" and computer_weapon == "2":
        print("You Win!")
    elif player_weapon == "3" and computer_weapon == "3":
        print("You Win!")
# Tie Scenarios
    elif player_weapon == "1" and computer_weapon == "2":
        print("It's a tie!")
    elif player_weapon == "2" and computer_weapon == "3":
        print("It's a tie!")
    elif player_weapon == "3" and computer_weapon == "1":
        print("It's a tie!")
    else:
        print("Bruh you lost")

# tictactoe
test = [0,1,2,3,4,5,6,7,8,9]
def play_tictactoe():
    symbols = ["O", "X"]
    symbol_player = input("Which symbol do you want to be? O or X: ")
# Deleting O or X from the list and checking whether player has chosen O or X
    if symbol_player == "O":
        del symbols[0]
    elif symbol_player == "X":
        del symbols[1]
    elif symbol_player != "O" or "X":
        print("You didn't choose O or X")
        symbol_player = input("Which symbol do you want to be? O or X: ")
        if symbol_player == "O":
            del symbols[0]
        elif symbol_player == "X":
            del symbols[1]
# Computer choosing O or X and placing his symbol on the board
    symbol_computer = random.choice(symbols)
# The game starts
    for i in range(1,10):
        place_player = input("Place your symbol [1, 2, 3, 4, 5, 6, 7, 8, 9]: ")
        board[place_player] = symbol_player

        theBoard(board)
        place_computer = random.choice(test)
        del test[int(place_computer)]
# Computer places symbol on the board
        board[place_computer] = symbol_computer
        print(f"The computer chose {place_computer}")
        theBoard(board)

# Loop
def loop():
    while True:
        break


# Start of program
while True:
    displayMenu()
    choice = input("Enter: ")
    if choice == "1":
        play_tictactoe()
    elif choice == "2":
        rps()
    elif choice == "3":
        sys.exit()