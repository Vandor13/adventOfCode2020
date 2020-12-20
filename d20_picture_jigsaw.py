class PictureJigsaw:
    rims = (("upper", False), ("upper", True), ("right", False), ("right", True),
            ("left", False), ("left", True), ("lower", False), ("lower", True),)

    def __init__(self, filename: str, no_of_tiles):
        self.tiles = dict()
        self.read_file(filename, no_of_tiles)
        self.print_tiles()
        self.neighbors = dict()

    def print_tiles(self):
        for tile in self.tiles.items():
            print("Tile with id", tile[0])
            for row in tile[1][0]:
                print("".join(row))
            print("Rims:", tile[1][1])
        print()

    def read_file(self, filename: str, no_of_tiles):
        with open(filename, "r") as file:
            for _ in range(no_of_tiles):
                # print(i)
                tile_title = file.readline()
                tile_id = str(tile_title).strip(":\n").split()[1]
                tile_rows = []
                for _ in range(10):
                    tile_rows.append(str(file.readline()).strip("\n"))
                file.readline()
                tile_rims = get_rim_list(tile_rows)
                self.tiles[tile_id] = [tile_rows, tile_rims]

    def calculate_neighbors(self):
        for tile_key in self.tiles.keys():
            neighbors = []
            tile_rims = self.tiles[tile_key][1]
            for possible_neighbor_key in self.tiles.keys():
                if tile_key == possible_neighbor_key:
                    continue
                neighbor_rims = self.tiles[possible_neighbor_key][1]
                common_rim = list(set(tile_rims) & set(neighbor_rims))
                if len(common_rim) > 0:
                    rim_index = list(tile_rims).index(common_rim[0])
                    neighbors.append([possible_neighbor_key, self.rims[rim_index]])
            self.neighbors[tile_key] = neighbors

    def print_neighbors(self):
        corner_multiplication = 1
        for neighbor_list in self.neighbors.items():
            number_of_neighbors = len(neighbor_list[1])
            print("Tile", neighbor_list[0], "has", number_of_neighbors, "neighbors")
            if number_of_neighbors == 2:
                corner_multiplication *= int(neighbor_list[0])
        print("Multiplication of corner ids:", corner_multiplication)


def get_rim_list(tile) -> list:
    upper_rim = tile[0]
    rim_list = [string_representation(upper_rim), string_representation(upper_rim)[::-1]]
    right_rim = [row[9] for row in tile]
    rim_list.append(string_representation(right_rim))
    rim_list.append(string_representation(right_rim)[::-1])
    left_rim = [row[0] for row in tile]
    rim_list.append(string_representation(left_rim))
    rim_list.append(string_representation(left_rim)[::-1])
    lower_rim = tile[9]
    rim_list.append(string_representation(lower_rim))
    rim_list.append(string_representation(lower_rim)[::-1])
    return rim_list


def string_representation(row: list) -> str:
    return "".join(row)


def count_file_rows(filename: str) -> int:
    with open(filename, "r") as file:
        length = len(file.readlines())
        print("File has ", length, "rows")
        return length


# count_file_rows("input20.txt")
picture_jigsaw = PictureJigsaw("input20.txt", 144)
picture_jigsaw.calculate_neighbors()
picture_jigsaw.print_neighbors()
