class Hexagons:
    debugging = False
    debugging_part2 = False

    directions = {
        "ne": (1, 1),
        "e": (2, 0),
        "se": (1, -1),
        "sw": (-1, -1),
        "w": (-2, 0),
        "nw": (-1, 1)
    }

    def __init__(self):
        self.black_tiles = set()
        self.instructions = []
        self.move = 0
        self.lowest_x = 0
        self.highest_x = 0
        self.lowest_y = 0
        self.highest_y = 0
        self.last_days_black_tiles = []

    def read_file(self, filename: str):
        with open(filename, "r") as file:
            self.instructions = file.readlines()

    def execute_instructions(self):
        for instruction in self.instructions:
            self.execute_instruction(instruction.strip("\n"))
        print("Number of black tiles:", len(self.black_tiles))
        print("x between", self.lowest_x, "and", self.highest_x)
        print("y between", self.lowest_y, "and", self.highest_y)
        print(self.black_tiles)

    def execute_instruction(self, instruction: str):
        self.move += 1
        if self.debugging:
            print("-- Move", self.move, "--")
            print("Instruction:", instruction)
        instruction_list = list(instruction)
        tile = (0, 0)
        while len(instruction_list) > 0:
            instruction = instruction_list.pop(0)
            if instruction == "n" or instruction == "s":
                instruction = instruction + instruction_list.pop(0)
            step = self.directions[instruction]
            tile = (tile[0] + step[0], tile[1] + step[1])
        self.flip_tile(tile)

    def flip_tile(self, tile: tuple):
        self.lowest_x = min([self.lowest_x, tile[0]])
        self.highest_x = max([self.highest_x, tile[0]])
        self.lowest_y = min([self.lowest_y, tile[1]])
        self.highest_y = max([self.highest_y, tile[1]])
        if tile in self.black_tiles:
            self.black_tiles.remove(tile)
            if self.debugging:
                print("Flipping tile", tile, "back to white")
        else:
            self.black_tiles.add(tile)
            if self.debugging:
                print("Flipping tile", tile, "to black")

    def daily_flip(self, no_of_day):
        print()
        print("-- Day", no_of_day, "--")
        self.last_days_black_tiles = self.black_tiles.copy()
        for x in range(self.lowest_x - 1, self.highest_x + 2):
            for y in range(self.lowest_y - 1, self.highest_y + 2):
                if (x, y) in self.last_days_black_tiles:
                    self.check_black_tile((x, y))
                else:
                    self.check_white_tile((x, y))
        print("End of Day", no_of_day, ":", len(self.black_tiles), "black tiles")

    def check_white_tile(self, tile):
        number_black_tiles = 0
        for offset in self.directions.values():
            if (tile[0] + offset[0], tile[1] + offset[1]) in self.last_days_black_tiles:
                number_black_tiles += 1
            if number_black_tiles > 2:
                break
        if number_black_tiles == 2:
            self.black_tiles.add(tile)
            self.lowest_x = min([self.lowest_x, tile[0]])
            self.highest_x = max([self.highest_x, tile[0]])
            self.lowest_y = min([self.lowest_y, tile[1]])
            self.highest_y = max([self.highest_y, tile[1]])
            if self.debugging_part2:
                print("Flipped", tile, "to black")

    def check_black_tile(self, tile):
        number_black_tiles = 0
        for offset in self.directions.values():
            if (tile[0] + offset[0], tile[1] + offset[1]) in self.last_days_black_tiles:
                number_black_tiles += 1
        if number_black_tiles == 0 or number_black_tiles > 2:
            self.black_tiles.remove(tile)
            if self.debugging_part2:
                print("Flipped", tile, "to white")

    def do_x_days(self, number_of_days: int):
        for i in range(1, number_of_days + 1):
            self.daily_flip(i)


hexagons = Hexagons()
hexagons.read_file("input24.txt")
hexagons.execute_instructions()
# hexagons.daily_flip(1)
hexagons.do_x_days(100)
