import random

class SnakeLadderGame:
    def __init__(self, size=100):
        self.size = size
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.players = {}

    def add_player(self, name, color):
        self.players[name] = {"position": 0, "color": color}

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player, steps):
        self.players[player]["position"] += steps
        if self.players[player]["position"] in self.snakes:
            print(f"Sorry! {player} got bitten by a snake at position {self.players[player]['position']}")
            self.players[player]["position"] = self.snakes[self.players[player]["position"]]
        elif self.players[player]["position"] in self.ladders:
            print(f"Wooh! {player} climbed a ladder to position {self.players[player]['position']}")
            self.players[player]["position"] = self.ladders[self.players[player]["position"]]
        print(f"{player} moved to position {self.players[player]['position']}")

    def display_board(self):
        print("Current Board:")
        for i in range(self.size, 0, -10):
            row = ""
            for j in range(10):
                position = i - j
                marker = ""
                for player, info in self.players.items():
                    if info["position"] == position:
                        marker += f"\033[1;{info['color']}m{player[0].upper()}\033[0m"
                        break
                if not marker:
                    if position in self.snakes:
                        marker = f"S{self.snakes[position]}".rjust(3)
                    elif position in self.ladders:
                        marker = f"L{self.ladders[position]}".rjust(3)
                    else:
                        marker = str(position).rjust(3)
                row += f"| {marker} "
            print(row + "|")
            print("+----+" * 10)

    def play(self):
        while True:
            self.display_board()
            for player in self.players:
                input(f"{player}, press Enter to roll the dice...")
                steps = self.roll_dice()
                print(f"{player} rolled a {steps}")
                self.move_player(player, steps)
                if self.players[player]["position"] >= self.size:
                    print(f"Congratulations! {player} wins!")
                    return

if __name__ == "__main__":
    game = SnakeLadderGame()
    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        name = input(f"Enter the name of player {i+1}: ")
        color = input(f"Enter the color of player {i+1} (e.g., 31 for red, 32 for green, 33 for yellow,Blue: 34,Magenta: 35,Cyan: 36): ")
        game.add_player(name, color)
    game.play()
