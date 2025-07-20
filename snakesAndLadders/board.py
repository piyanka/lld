from snake import Snake
from ladder import Ladder

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