import pygame

class MoveBallVisitor:
    def __init__(self, seconds):
        self.seconds = seconds

    def visit_board(self, board):
        self.walls = []

    def visit_wall(self, wall):
        self.walls.append(wall)

    def visit_bar(self, bar):
        self.walls.append(bar)

    def visit_ball(self, ball):
        switch_dx = 1
        switch_dy = 1
        new_x = ball.start_x
        new_y = ball.start_y
        new_x += ball.dx * self.seconds
        new_y += ball.dy * self.seconds
        x_ball, y_ball, ball_r = ball.get_coordinates()
        for wall in self.walls:
            x1, y1, x2, y2 = wall.get_coordinates()
            if y_ball <= y2 and y_ball >= y1 and x_ball >= x2 and new_x < x2: # hit on the right side of wall
                switch_dx = -1
            if y_ball <= y2 and y_ball >= y1 and x_ball <= x1 and new_x > x1: # hit on the left side of wall
                switch_dx = -1
            if x_ball <= x2 and x_ball >= x1 and y_ball >= y2 and new_y < y2: # hit on the bottom side of wall
                switch_dy = -1
            if x_ball <= x2 and x_ball >= x1 and y_ball <= y1 and new_y > y1: # hit on the top side of wall
                switch_dy = -1
        ball.change_direction(switch_dx, switch_dy)
        new_x = ball.start_x
        new_y = ball.start_y
        new_x += ball.dx * self.seconds
        new_y += ball.dy * self.seconds
        ball.move(new_x, new_y)
        
        