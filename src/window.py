from tkinter import Tk, BOTH, Canvas
from point_and_line import *

class Window: 

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Sam's Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height = height, width = width)
        self.__canvas.pack()
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def line_draw(self, line, fill_colour="black"):
        line.draw(self.__canvas, fill_colour)
