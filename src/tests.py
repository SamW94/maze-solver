import unittest
from maze import Maze
from cell import *
from window import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_large_cells(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 30
        cell_size_y = 30
        m2 = Maze(100, 100, num_rows, num_cols, cell_size_x, cell_size_y)
        self.assertEqual(
            m2._cell_size_x,
            cell_size_x,
        )
        self.assertEqual(
            m2._cell_size_y, 
            cell_size_y
        )

    def test_maze_create_cells_lots_of_columns(self):
        num_cols = 60
        num_rows = 1
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m3._cells),
            num_rows,
        )
        self.assertEqual(
            len(m3._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_lots_of_rows(self):
        num_cols = 1
        num_rows = 60
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m4._cells),
            num_rows,
        )
        self.assertEqual(
            len(m4._cells[0]),
            num_cols,
        )

    def test_break_entrance_cell(self):
        num_cols = 12
        num_rows = 10
        m5 = Maze(0, 0, num_rows, num_cols, 10, 10)

        entrance_cell = m5._cells[0][0]
        m5._break_entrance_and_exit()
        self.assertEqual(
            entrance_cell.has_top_wall,
            False,
        )

    def test_break_exit_cell(self):
        num_cols = 12
        num_rows = 10
        m6 = Maze(0, 0, num_rows, num_cols, 10, 10)

        exit_cell = m6._cells[-1][-1]
        m6._break_entrance_and_exit()
        self.assertEqual(
            exit_cell.has_bottom_wall,
            False,
        )


    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m7 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for row in m7._cells:
            for cell in row:
                self.assertEqual(
                    cell._visited,
                    False
                )

if __name__ == "__main__":
    unittest.main()
