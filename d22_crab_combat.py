class Combat:
    def __init__(self, player1_deck: list, player2_deck: list, game_no: int):
        self.player1_deck = player1_deck
        self.player2_deck = player2_deck
        self.no_of_cards = len(self.player1_deck) + len(self.player2_deck)
        self.round = 0
        self.game_no = game_no
        # print("Player1 deck:", self.player1_deck)
        # print("Player2 deck:", self.player2_deck)

    def play_game(self):
        print("=== Game", self.game_no, "===")
        while len(self.player1_deck) < self.no_of_cards and len(self.player2_deck) < self.no_of_cards:
            self.play_round()
            # if self.round > 30:
            #     exit()
        if self.game_no == 1:
            self.count_score()
        return "Player1" if len(self.player1_deck) == self.no_of_cards else "Player2"

    def play_round(self):
        self.round += 1
        print("-- Round", self.round, "--")
        print("Player 1's deck:", ", ".join(self.player1_deck))
        print("Player 2's deck:", ", ".join(self.player2_deck))
        player_1_card = self.player1_deck.pop(0)
        player_2_card = self.player2_deck.pop(0)
        print("Player 1 plays:", player_1_card)
        print("Player 2 plays:", player_2_card)
        if int(player_1_card) > int(player_2_card):
            print("Player 1 wins the round!")
            self.player1_deck.append(player_1_card)
            self.player1_deck.append(player_2_card)
        else:
            print("Player 2 wins the round!")
            self.player2_deck.append(player_2_card)
            self.player2_deck.append(player_1_card)
        print()

    def count_score(self, winner = None):
        if winner == "Player 1" or len(self.player1_deck) == self.no_of_cards:
            deck = self.player1_deck
            print("Winner is Player1!")
        else:
            deck = self.player2_deck
            print("Winner is Player2!")
        score = 0
        for i in range(len(deck)):
            card = deck.pop()
            score += (i + 1) * int(card)
        print("Score:", score)


def readfile(filename: str):
    with open(filename, "r") as file:
        line = file.readline()
        player = None
        player1_deck = []
        player2_deck = []
        current_deck = []
        while True:
            if line.startswith("Player"):
                player = line.strip(":\n")
            elif line == "\n" or not line:
                if player == "Player 1":
                    player1_deck = current_deck
                    current_deck = []
                else:
                    player2_deck = current_deck
                    current_deck = []
                if not line:
                    break
            else:
                current_deck.append(line.strip("\n"))
            line = file.readline()
        return player1_deck, player2_deck


deck1, deck2 = readfile("input22.txt")
combat = Combat(deck1, deck2, 1)
combat.play_game()
