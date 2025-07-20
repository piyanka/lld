import random

class Dice:
    def roll(self):
        return random.randint(1, 6)
    

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0


class Snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Board:

    def __init__(self, size):
        self.size = size
        self.snakes = [] 
        self.ladders = []

    def add_snake(self, head, tail):
        self.snakes.append(Snake(head, tail))
    
    def add_ladder(self, start, end):
        self.ladders.append(Ladder(start, end))

    def get_next_position(self, pos):
        for snake in self.snakes:
            if snake.head == pos:
                print("Oops! Bitten by a snake 🐍")
                return snake.tail
            
        for ladder in self.ladders:
            if ladder.start == pos:
                print("Yay! Climbed a ladder 🪜")
                return ladder.end
            
        return pos



class GameEngine:

    def __init__(self, board, players):
        self.board = board   
        self.players = players
        self.dice = Dice()

    def play(self):
        while self.players:
            player = self.players.popleft()

            input(f"{player.name}'s turn. Press Enter to roll...")
            roll = self.dice.roll()

            print(f"{player.name} rolled a {roll}")
            next_pos = player.position + roll

            if next_pos > self.board.size:
                print("  Roll too high, stay in place.")
            else:
                final_pos = self.board.get_next_position(next_pos)
                player.position = final_pos
                print(f"  {player.name} moved to {player.position}")

            if player.position == self.board.size:
                print(f"\n🏆 {player.name} wins the game!")
                return 


            self.players.append(player)

        





from collections import deque

players = deque()
players.append(Player("Priyanka"))
players.append(Player("Manish"))


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

game = GameEngine(board, players)
game.play()



