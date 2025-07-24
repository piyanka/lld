class GameEngine:
    def __init__(self, board, players):
        self.board = board
        self.players = players


    def play(self):
        while True:
            current_player = self.players.popleft()
            print(f"{current_player.name}'s turn {current_player.piece.symbol}:")

            self.board.display()

            try:
                row = int(input("Enter row (0 to self.board.size - 1): "))
                col = int(input("Enter column (0 to self.board.size - 1): "))
            except ValueError:
                print("Invalid Input, please enter interger value")
                continue

            if not (0 <= row < self.board.size and 0 <= col < self.board.size):
                print("Move out of bounds. Try again.")
                continue

            success = self.board.add_piece(row, col, current_player.piece)
            if not success:
                print("⚠️ Cell already taken. Try a different move.")
                continue

            if self.board.check_winner(current_player.piece.symbol):
                self.board.display()
                print(f"🏆 {current_player.name} wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("🤝 It's a draw!")
                break

            self.players.append(current_player)
