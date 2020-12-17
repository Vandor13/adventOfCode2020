class PocketDimension4d:

    def __init__(self, filename: str):
        self.dimension = None
        self.x_len, self.y_len, self.z_len, self.w_len = 0, 0, 0, 0
        self.read_file(filename)

    def read_file(self, filename: str):
        dimension = [[[]]]
        with open(filename, "r") as file:
            lines = file.readlines()
        for line in lines:
            dimension[0][0].append([char for char in line.rstrip("\n")])
        self.dimension = dimension
        self.x_len = len(dimension[0][0][0])
        self.y_len = len(dimension[0][0])
        self.z_len = 1
        self.w_len = 1
        print("Start dimension has dimensions of: ")
        print("wlen:", self.w_len)
        print("zlen:", self.z_len)
        print("ylen:", self.y_len)
        print("xlen:", self.x_len)

    def enhance_dimension(self):
        new_dimension = [[[[0 for x in range(self.x_len + 2)] for y in range(self.y_len + 2)] for z in
                         range(self.z_len + 2)] for w in range(self.w_len + 2)]
        no_of_active_cubes = 0
        print("New dimension has wlen:", len(new_dimension))
        print("zlen:", len(new_dimension[0]))
        print("ylen:", len(new_dimension[0][0]))
        print("xlen:", len(new_dimension[0][0][0]))
        for w in range(self.w_len):
            for z in range(self.z_len):
                for y in range(self.y_len):
                    for x in range(self.x_len):
                        if self.dimension[w][z][y][x] == "#":
                            # mark all neighbors with +1
                            no_of_neighbors = 0
                            for w2 in range(w, w + 3):
                                for z2 in range(z, z + 3):
                                    for y2 in range(y, y + 3):
                                        for x2 in range(x, x + 3):
                                            # print("z2:", z2, "y2:", y2, "x2:", x2)
                                            if (x2 != x + 1) or (y2 != y + 1) or (z2 != z + 1) or (w2 != w + 1):
                                                new_dimension[w2][z2][y2][x2] = new_dimension[w2][z2][y2][x2] + 1
                                                # if z2 == 1 and y2 == 1 and x2 == 2:
                                                #     print("enhanced by", x, y, z, "Now:", new_dimension[z2][y2][x2])
                                                no_of_neighbors += 1
                            print("No. of neighbors:", no_of_neighbors)
        # self.print_matrix(new_dimension)
        for w in range(self.w_len + 2):
            for z in range(self.z_len + 2):
                for y in range(self.y_len + 2):
                    for x in range(self.x_len + 2):
                        # print("z:", z, "y:", y, "x:", x)
                        if (0 < z < self.z_len + 1) and (0 < y < self.y_len + 1) and (0 < x < self.x_len + 1) and \
                                (0 < w < self.w_len + 1) and self.dimension[w - 1][z - 1][y - 1][x - 1] == "#":
                            if new_dimension[w][z][y][x] == 2 or new_dimension[w][z][y][x] == 3:
                                new_dimension[w][z][y][x] = "#"
                                no_of_active_cubes += 1
                            else:
                                new_dimension[w][z][y][x] = "."
                        elif new_dimension[w][z][y][x] == 3:
                            new_dimension[w][z][y][x] = "#"
                            no_of_active_cubes += 1
                        else:
                            new_dimension[w][z][y][x] = "."
        self.dimension = new_dimension
        self.x_len += 2
        self.y_len += 2
        self.z_len += 2
        self.w_len += 2
        print("Active cubes:", no_of_active_cubes)

    def print_dimension(self):
        for w in range(self.w_len):
            print()
            print("w=", w)
            for z in range(self.z_len):
                print("z=", z)
                for y in range(self.y_len):
                    print("".join(self.dimension[w][z][y]))

    def print_matrix(self, matrix: list):
        for w in matrix:
            print("new w")
            for z in w:
                print("new z")
                for y in z:
                    print(y)


pocket_dimension = PocketDimension4d("input17.txt")
print("Before:")
pocket_dimension.print_dimension()
pocket_dimension.enhance_dimension()
pocket_dimension.enhance_dimension()
pocket_dimension.enhance_dimension()
pocket_dimension.enhance_dimension()
pocket_dimension.enhance_dimension()
pocket_dimension.enhance_dimension()

# pocket_dimension.print_dimension()
