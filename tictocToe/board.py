from tabulate import tabulate
class Board:

    def __init__(self, size):
        self.size = size
        self.grid = [[" " for _ in range(self.size)] for _  in range(self.size)] 

    def display(self):
        print("\nCurrent Board:")
        # for i in range(self.size):
        #     row = " | ".join(self.grid[i])
        #     print(f" {row} ")
        #     if i < self.size - 1:
        #         print("---" + "+---" *(self.size - 1))
        #     print()

        print(tabulate(self.grid, tablefmt="fancy_grid"))

    
    def add_piece(self, row, col, piece):
        if self.grid[row][col] == " ":
            self.grid[row][col] = piece.symbol
            return True

        return False


    def is_full(self):
        return all(cell != " " for row in self.grid for cell in row )
        
    
    def check_winner(self, symbol):

        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True
        
        for col in range(self.size):
            if all(self.grid[row][col] == symbol for row in range(self.size) ):
                return True

        if all(self.grid[i][i] == symbol for i in range(self.size)):
            return True
        

        if all(self.grid[i][self.size - i - 1] == symbol for i in range(self.size)):
            return True

        return False

    