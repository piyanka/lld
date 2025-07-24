from tabulate import tabulate
from collections import deque
from board import Board
from player import Player
from gameEngine import GameEngine
from crossPiece import CrossPiece
from naoughtPiece import NaoughtPiece

if __name__ == "__main__":

    print("🎮 Welcome to Tic-Tac-Toe!")
    size = input("Enter board size (default is 3): ")
    try:
        size = int(size)
        if size < 3:
            print("Minimum board size is 3. Setting to 3.")
            size = 3
    except ValueError:
        size = 3

  

    name1 = input("Enter the name of first player: ") or "player1"
    name2 = input("Enter the name of second player: ") or "player2"

    while True:
        symbol = input(f"{name1}, choose your symbol (X or O): ").strip().upper()
        if symbol == 'X':
            player1 = Player(name1, CrossPiece())
            player2 = Player(name2, NaoughtPiece())
            break
        elif symbol == 'O':
            player1 = Player(name1, NaoughtPiece())
            player2 = Player(name2, CrossPiece())
            break
        else:
            print("⚠️ Invalid input. Please choose 'X' or 'O'.")

    board = Board(size)


    players = deque([player1, player2])

    game = GameEngine(board, players)
    game.play()



