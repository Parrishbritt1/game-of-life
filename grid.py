class Grid:
    def __init__(self, num_rows, num_cols, cell_width, cell_height, margin):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.margin = margin
        self.grid = self.create_grid()

    def create_grid(self):
        """Creates 2D array filled with 0
        """
        grid = []
        for i in range(self.num_rows):
            grid.append([])
            for _ in range(self.num_cols):
                grid[i].append(0)
        return grid

    def clear_grid(self):
        """Changes all elements in grid to 0
        """
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.grid[i][j] = 0