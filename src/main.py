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

    #self, x1, y1, num_rows, num_columns, cell_size_x, cell_size_y, win

    maze = Maze(maze_x, maze_y, num_rows, num_columns, cell_size_x, cell_size_y, win)

    # Testing lines, points and line_draw functions
    
    #line1 = Line(Point(100, 100), Point(200, 200))
    #line2 = Line(Point(300, 300), Point(400, 400))
    #win.line_draw(line1, fill_colour="red")
    #win.line_draw(line2, fill_colour="green")

    # Testing cells and cell.draw() functions

    #cell1 = Cell(win)
    #cell1.has_left_wall = False
    #cell1.has_top_wall = False
    #cell1.draw(100, 100, 200, 200)

    #cell2 = Cell(win)
    #cell2.has_right_wall = False
    #cell2.has_bottom_wall = False
    #cell2.draw(350, 350, 450, 450)

    #Cell.draw_move(cell1, cell2)

    win.wait_for_close()

main()