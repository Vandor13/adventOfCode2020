import d22_crab_combat


class RecursiveCombat(d22_crab_combat.Combat):
    def __init__(self, player1_deck: list, player2_deck: list, game_no: int):
        super().__init__(player1_deck, player2_deck, game_no)
        self.old_player1_decks = []
        self.old_player2_decks = []

    def play_game(self):
        print()
        print("=== Game", self.game_no, "===")
        winner = None
        while True:
            if get_deck_string(self.player1_deck) in self.old_player1_decks or \
                    get_deck_string(self.player2_deck) in self.old_player2_decks or \
                    len(self.player1_deck) == self.no_of_cards:
                winner = "Player1"
                break
            elif len(self.player2_deck) == self.no_of_cards:
                winner = "Player2"
                break
            self.play_round()
            # if self.round > 30:
            #     exit()
        if self.game_no == 1:
            self.count_score(winner)
        else:
            print("The winner of game", self.game_no, "is", winner, "!")
        return winner

    def play_round(self):
        self.round += 1
        print("-- Round", self.round, "(Game", self.game_no, ") --")
        player_1_deck_string = get_deck_string(self.player1_deck)
        self.old_player1_decks.append(player_1_deck_string)
        player_2_deck_string = get_deck_string(self.player2_deck)
        self.old_player2_decks.append(player_2_deck_string)
        print("Player 1's deck:", player_1_deck_string)
        print("Player 2's deck:", player_2_deck_string)
        player_1_card = self.player1_deck.pop(0)
        player_2_card = self.player2_deck.pop(0)
        print("Player 1 plays:", player_1_card)
        print("Player 2 plays:", player_2_card)
        if int(player_1_card) <= len(self.player1_deck) and int(player_2_card) <= len(self.player2_deck):
            recursive_combat = RecursiveCombat(self.player1_deck[:int(player_1_card)].copy(),
                                               self.player2_deck[:int(player_2_card)].copy(), self.game_no + 1)
            print("Playing a sub-game to determine the winner...")
            winning_player = recursive_combat.play_game()
            print("...anyway, back to game", self.game_no, ".")
            recursive_combat = None
        elif int(player_1_card) > int(player_2_card):
            winning_player = "Player 1"
        else:
            winning_player = "Player 2"
        if winning_player == "Player 1":
            print("Player 1 wins round", self.round, "of game", self.game_no, "!")
            self.player1_deck.append(player_1_card)
            self.player1_deck.append(player_2_card)
        else:
            print("Player 2 wins the round", self.round, "of game", self.game_no, "!")
            self.player2_deck.append(player_2_card)
            self.player2_deck.append(player_1_card)
        print()


def get_deck_string(deck: list):
    return ", ".join(deck)


deck1, deck2 = d22_crab_combat.readfile("input22.txt")
recursive_combat = RecursiveCombat(deck1, deck2, 1)
recursive_combat.play_game()
