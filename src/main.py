from window import *
from pointsAndLines import *
from cell import *

def main():
    win = Window(800,600)
    line1 = Line(Point(0, 0), Point(300, 300))
    line2 = Line(Point(300, 0), Point(0, 300))
    win.draw_line(line1, "red")
    win.draw_line(line2, "green")
    cell = Cell(Point(400, 400), Point(450,450), win)
    win.draw_cell(cell)
    win.wait_for_close()

main()