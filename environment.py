class DisasterGrid:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.start = (0, 0)
        self.goal = (9, 9)
        # Initial obstacles
        self.add_obstacle(2, 1)
        self.add_obstacle(2, 2)
        self.add_obstacle(2, 3)
        self.add_obstacle(4, 6)
        self.add_obstacle(5, 6)

    def add_obstacle(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 1

    def display(self):
        print("   " + " ".join([str(i) for i in range(self.width)]))
        for y, row in enumerate(self.grid):
            line = [str(cell) for cell in row]
            if y == self.start[1]: line[self.start[0]] = 'S'
            if y == self.goal[1]: line[self.goal[0]] = 'G'
            print(f"{y} | " + " ".join(line))