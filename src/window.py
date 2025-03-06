from tkinter import Tk, BOTH, Canvas
from pointsAndLines import *
from cell import *

class Window:

    def __init__(self, width, height):
        self.running = False
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, width = width, height = height)
        self.canvas.pack()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_colour):
        line.draw(self.canvas, fill_colour)

    def draw_cell(self, cell):
        cell.draw(self.canvas)