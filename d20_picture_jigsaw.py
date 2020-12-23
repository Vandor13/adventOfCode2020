import math
import numpy


class PictureJigsaw:
    rims = (("upper", False), ("upper", True), ("right", False), ("right", True),
            ("lower", False), ("lower", True), ("left", False), ("left", True), )

    def __init__(self, filename: str, no_of_tiles):
        self.tiles = dict()  # To tile_key: [tile_array, tile_rims]
        self.rim_length = int(math.sqrt(no_of_tiles))
        self.read_file(filename, no_of_tiles)
        self.print_tiles()
        self.neighbors = dict()  # [neighbor_id, orientation_index]
        self.corner_pieces = list()
        self.rim_pieces = list()
        self.no_rim_pieces = list()

    def print_tiles(self):
        for tile in self.tiles.items():
            print("Tile with id", tile[0])
            self.print_tile(tile[1])
            # print("Rims:", tile[1][1])
        print()

    @staticmethod
    def print_tile(tile):
        print(tile[0])
        # for row in tile[0]:
        #     print("".join(row))

    def read_file(self, filename: str, no_of_tiles):
        with open(filename, "r") as file:
            for _ in range(no_of_tiles):
                # print(i)
                tile_title = file.readline()
                tile_id = str(tile_title).strip(":\n").split()[1]
                tile_rows = []
                for _ in range(10):
                    tile_rows.append(list(str(file.readline()).strip("\n")))
                file.readline()
                tile_rims = get_rim_list(tile_rows)
                tile_array = numpy.array(tile_rows, str)
                self.tiles[tile_id] = [tile_array, tile_rims]

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
                    neighbors.append([possible_neighbor_key, rim_index])
            self.neighbors[tile_key] = neighbors
            if len(neighbors) == 2:
                self.corner_pieces.append(tile_key)
            elif len(neighbors) == 3:
                self.rim_pieces.append(tile_key)
            else:
                self.no_rim_pieces.append(tile_key)

    def print_neighbors(self):
        corner_multiplication = 1
        for neighbor_list in self.neighbors.items():
            number_of_neighbors = len(neighbor_list[1])
            print("Tile", neighbor_list[0], "has", number_of_neighbors, "neighbors")
            for neighbor in neighbor_list[1]:
                print("Neighbor Index:", neighbor[0], "Orientation:", self.rims[neighbor[1]])
            if number_of_neighbors == 2:
                corner_multiplication *= int(neighbor_list[0])
        print("Multiplication of corner ids:", corner_multiplication)

    def print_piece_types(self):
        print("Corners:", self.corner_pieces)
        print("Rims:", self.rim_pieces)
        print("Rest:", self.no_rim_pieces)

    def rotate_tile(self, key):
        tile = self.tiles[key]
        tile_array = tile[0]
        tile_array = numpy.rot90(tile_array)
        tile[0] = tile_array
        for neighbor in self.neighbors[key]:
            orientation_index = neighbor[1]
            # print("Old orientation:", self.rims[orientation_index])
            orientation_index = (orientation_index - 2) % 8
            # print("New orientation:", self.rims[orientation_index])
            neighbor[1] = orientation_index
        self.tiles[key] = tile

    def flip_tile_ud(self, key):
        tile = self.tiles[key]
        tile_array = tile[0]
        tile_array = numpy.flipud(tile_array)
        tile[0] = tile_array
        for neighbor in self.neighbors[key]:
            orientation_index = neighbor[1]
            if orientation_index in [0, 1, 4, 5]:
                orientation_index = (orientation_index + 4) % 8
                if orientation_index % 2 == 0:
                    orientation_index += 1
                else:
                    orientation_index -= 1
                neighbor[1] = orientation_index
        self.tiles[key] = tile

    def flip_tile_lr(self, key):
        tile = self.tiles[key]
        tile_array = tile[0]
        tile_array = numpy.fliplr(tile_array)
        tile[0] = tile_array
        for neighbor in self.neighbors[key]:
            orientation_index = neighbor[1]
            if orientation_index in [2, 3, 6, 7]:
                orientation_index = (orientation_index + 4) % 8
                neighbor[1] = orientation_index
        self.tiles[key] = tile

    def organize_tiles(self):
        row_ids = list()
        corner_id, right_neighbor, flipped_to_right = self.orient_first_corner()
        row_ids.append(corner_id)
        print("Corner piece after rotation:")
        self.print_tile(self.tiles[corner_id])
        print("Right piece", right_neighbor, "before rotation:")
        self.print_tile(self.tiles[right_neighbor])
        self.orient_to_left(right_neighbor, corner_id, flipped_to_right)
        print("Right piece after rotation:")
        self.print_tile(self.tiles[right_neighbor])
        merge_array = merge_arrays(self.tiles[corner_id][0], self.tiles[right_neighbor][0])
        print_list_array(merge_array)

    def orient_first_corner(self):
        tile_key = self.corner_pieces[0]
        print("Selected cornerpiece:", tile_key)
        print("Corner piece before rotation:")
        self.print_tile(self.tiles[tile_key])
        tile_neighbors = self.neighbors[tile_key]
        print("Before orientation:", tile_neighbors)
        number_of_rotations = 0
        self.flip_tile_ud(tile_key)
        while not (2 <= tile_neighbors[0][1] <= 5) or not (2 <= tile_neighbors[1][1] <= 5):
            number_of_rotations += 1
            self.rotate_tile(tile_key)
            tile_neighbors = self.neighbors[tile_key]
        print("Rotated", number_of_rotations, "times")
        print("After orientation:", tile_neighbors)
        if tile_neighbors[0][1] in [2, 3]:
            right_neighbor = tile_neighbors[0][0]
            flipped = (tile_neighbors[0][1] % 2 == 1)
        else:
            right_neighbor = tile_neighbors[1][0]
            flipped = (tile_neighbors[1][1] % 2 == 1)
        return tile_key, right_neighbor, flipped

    def orient_to_left(self, tile_key, left_neighbor_key, flipped: bool):
        tile = self.tiles[tile_key]
        orientation_to_left_neighbor = None
        for neighbor in self.neighbors[tile_key]:
            if neighbor[0] == left_neighbor_key:
                orientation_to_left_neighbor = neighbor[1]
        amount_of_rotations = (orientation_to_left_neighbor // 2 + 1) % 4
        print("Rotating", amount_of_rotations, "times")
        for _ in range(amount_of_rotations):
            self.rotate_tile(tile_key)
        if flipped != self.rims[orientation_to_left_neighbor][1]:
            self.flip_tile_ud(tile_key)

    def count_fields(self):
        count_of_fields = 0
        for tile in self.tiles.values():
            array = tile[0]
            for i in range(1, len(array)-1):
                line = array[i]
                for j in range(1, len(line)-1):
                    if line[j] == "#":
                        count_of_fields += 1
        return count_of_fields


def get_rim_list(tile) -> list:
    upper_rim = tile[0]
    rim_list = [string_representation(upper_rim), string_representation(upper_rim)[::-1]]
    right_rim = [row[9] for row in tile]
    rim_list.append(string_representation(right_rim))
    rim_list.append(string_representation(right_rim)[::-1])
    lower_rim = tile[9]
    rim_list.append(string_representation(lower_rim))
    rim_list.append(string_representation(lower_rim)[::-1])
    left_rim = [row[0] for row in tile]
    rim_list.append(string_representation(left_rim))
    rim_list.append(string_representation(left_rim)[::-1])
    return rim_list


def string_representation(row: list) -> str:
    return "".join(row)


def count_file_rows(filename: str) -> int:
    with open(filename, "r") as file:
        length = len(file.readlines())
        print("File has ", length, "rows")
        return length


def merge_arrays(array_1: numpy.ndarray, array_2: numpy.ndarray):
    list_array1 = array_1.tolist()
    list_array2 = array_2.tolist()
    new_list_array = []
    for i in range(len(list_array1)):
        new_list_array.append(list_array1[i] + list_array2[i])
    return new_list_array


def print_list_array(array: list):
    for row in array:
        print("".join(row))


# count_file_rows("input20.txt")
picture_jigsaw = PictureJigsaw("input20.txt", 144)
picture_jigsaw.calculate_neighbors()
# picture_jigsaw.rotate_tile("3079")
# picture_jigsaw.print_neighbors()
# picture_jigsaw.print_piece_types()
# picture_jigsaw.organize_tiles()
number_of_fields = picture_jigsaw.count_fields()
print("Number of #:", number_of_fields)
monster_size = 15
fields_with_monster = 15 * 10
print("Solution =", number_of_fields - fields_with_monster)  # 2324
