from pointsAndLines import *
from window import *

class Cell:

    def __init__(self, top_left, bottom_right, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self, canvas):
        if self.has_left_wall:
            canvas.create_line(self.top_left.x, self.top_left.y, self.top_left.x, self.bottom_right.y, fill="black", width=2)

        if self.has_right_wall:
            canvas.create_line(self.bottom_right.x, self.top_left.y, self.bottom_right.x, self.bottom_right.y, fill="black", width=2)

        if self.has_top_wall:
            canvas.create_line(self.top_left.x, self.top_left.y, self.bottom_right.x, self.top_left.y, fill="black", width=2)

        if self.has_bottom_wall:
            canvas.create_line(self.bottom_right.x, self.bottom_right.y, self.top_left.x, self.bottom_right.y, fill="black", width=2)
