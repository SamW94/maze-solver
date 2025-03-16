from window import *
from cell import *
from maze import *

def main():
    screen_x = 800
    screen_y = 600
    maze_x = 50
    maze_y = 50
    num_rows = 10
    num_columns = 20
    cell_size_x = (screen_x - (2 * maze_x)) / num_columns
    cell_size_y = (screen_y - (2 * maze_y)) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(maze_x, maze_y, num_rows, num_columns, cell_size_x, cell_size_y, win)
    maze._break_entrance_and_exit()
    maze._solve()


    win.wait_for_close()

main()