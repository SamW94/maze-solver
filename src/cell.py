from point_and_line import *
from window import *

class Cell: 

    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall: 
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.line_draw(line)

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.line_draw(line)

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.line_draw(line)

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.line_draw(line)

    def draw_move(self, to_cell, undo=False):
        if undo:
            line_fill_colour = "gray"
        else:
            line_fill_colour = "red"

        cell1_center_x = (self._x1 + self._x2) / 2
        cell1_centre_y = (self._y1 + self._y2) / 2
        cell2_centre_x = (to_cell._x1 + to_cell._x2) / 2
        cell2_centre_y = (to_cell._y1 + to_cell._y2) / 2

        line = Line(Point(cell1_center_x, cell1_centre_y), Point(cell2_centre_x, cell2_centre_y))

        self._win.line_draw(line, line_fill_colour)
