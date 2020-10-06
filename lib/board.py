from wall import Wall
from bar import Bar
from ball import Ball


class Board:
    def __init__(self, width, height, color = (28, 28, 28)):
        self.wall_thickness = 15
        self.width = width
        self.height = height
        self.color = color
        self.elements = [
            Wall(0, 0, self.width, self.wall_thickness), # top
            Wall(self.width - self.wall_thickness, 0, self.wall_thickness, self.height), # right
            Wall(0, self.height - self.wall_thickness, self.width, self.wall_thickness), # bottom
            Bar(),
            Ball()
        ]

    def accept(self, visitor):
        visitor.visit_board(self)
        for element in self.elements:
            element.accept(visitor)