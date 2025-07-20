from collections import deque
from player import Player
from board import Board
from gameEngine import GameEngine


if __name__ == "__main__":
    board = Board(size=100)

    #Snakes
    board.add_snake(99, 21)
    board.add_snake(70, 55)
    board.add_snake(52, 42)
    board.add_snake(25, 2)

    #Ladders
    board.add_ladder(4, 56)
    board.add_ladder(12, 50)
    board.add_ladder(40, 69)
    board.add_ladder(65, 95)

    players = deque()
    players.append(Player("Priyanka"))
    players.append(Player("Manish"))

    game = GameEngine(board, players)
    game.play()



