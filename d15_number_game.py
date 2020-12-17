class NumberGame():
    def __init__(self, starting_number: list):
        self.turn_numbers = dict()
        self.turn = 1
        self.next_number = 0
        for number in starting_number:
            self.turn_numbers[number] = self.turn
            print("Said", number, "as starting number on turn", self.turn)
            self.turn += 1
        self.next_number = 0

    def take_turn(self) -> int:
        if self.next_number in self.turn_numbers.keys():
            after_next_number = self.turn - self.turn_numbers[self.next_number]
            self.turn_numbers[self.next_number] = self.turn
            if self.turn % 100000 == 0:
                print("Said", self.next_number, "on turn", self.turn)
            self.next_number = after_next_number
            self.turn += 1
            return self.next_number
        else:
            self.turn_numbers[self.next_number] = self.turn
            if self.turn % 100000 == 0:
                print("Said", self.next_number, "on turn", self.turn)
            self.next_number = 0
            self.turn += 1
            return 0


number_game = NumberGame([16,1,0,18,12,14,19])
for _ in range(30000000):
    number_game.take_turn()