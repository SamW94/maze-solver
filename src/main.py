from window import *
from cell import *

def main():
    win = Window(800, 600)
    
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

    win.wait_for_close()

main()