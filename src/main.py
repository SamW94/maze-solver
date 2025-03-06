from window import *
from pointsAndLines import *

def main():
    win = Window(800,600)
    line1 = Line(Point(0, 0), Point(300, 300))
    win.draw_line(line1, "red")
    win.wait_for_close()

main()