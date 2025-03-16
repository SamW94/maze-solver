from cell import *
import time
import random


class Maze:

    def __init__(self, x1, y1, num_rows, num_columns, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        

    def _create_cells(self):
        for i in range(self._num_rows):
            row_of_cells = []
            for j in range(self._num_columns):
                row_of_cells.append(Cell(self._win))
            self._cells.append(row_of_cells)
        
        for i in range(self._num_rows):
            for j in range(self._num_columns):
                self._draw_cell(i, j)

    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        
        x1 = self._x1 + (j * self._cell_size_x)
        y1 = self._y1 + (i * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)

        exit_cell = self._cells[self._num_rows - 1][self._num_columns - 1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_columns - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            unvisited_neighbouring_cells = []
            if i > 0:
                if self._cells[i - 1][j]._visited is False:
                    unvisited_neighbouring_cells.append((i - 1, j))
            
            if i < (self._num_rows - 1):
                if self._cells[i + 1][j]._visited is False:
                    unvisited_neighbouring_cells.append((i + 1, j))

            if j > 0:
                if self._cells[i][j - 1]._visited is False:
                    unvisited_neighbouring_cells.append((i, j - 1))
            
            if j < (self._num_columns - 1):
                if self._cells[i][j + 1]._visited is False:
                    unvisited_neighbouring_cells.append((i, j + 1))

            if len(unvisited_neighbouring_cells) == 0:
                self._draw_cell(i, j)
                return
            
            random_index = random.randrange(len(unvisited_neighbouring_cells))
            next_i, next_j = unvisited_neighbouring_cells[random_index]


            if next_i > i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif next_i < i:
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif next_j > j:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            elif next_j < j:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
                        
            self._draw_cell(i, j)

            self._break_walls_r(next_i, next_j)


    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell._visited = False

    
    def _solve(self, i=0, j=0):
        return self._solve_r(i, j)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j]._visited = True

        if i == (self._num_rows - 1) and j == (self._num_columns - 1):
            return True
        
        directions = []

        if i > 0 and self._cells[i - 1][j].has_bottom_wall is False:
            directions.append((i - 1, j))
        if i < (self._num_rows - 1) and self._cells[i + 1][j].has_top_wall is False:
            directions.append((i + 1, j))
        if j > 0 and self._cells[i][j - 1].has_right_wall is False:
            directions.append((i, j - 1))
        if j < (self._num_columns - 1) and self._cells[i][j + 1].has_left_wall is False:
            directions.append((i, j + 1))

        for direction in directions:
            if self._cells[direction[0]][direction[1]]._visited is False:
                self._cells[i][j].draw_move(self._cells[direction[0]][direction[1]])
                if self._solve_r(direction[0], direction[1]) == True:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[direction[0]][direction[1]], undo=True)

            if len(directions) == 0:
                return False