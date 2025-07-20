from dice import Dice

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