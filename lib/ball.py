class Ball:
    def __init__(self, start_x = 550, start_y = 40, ball_r = 5, dx = 50, dy = 60, color = (238,238,238)):
        self.ball_r = ball_r
        self.color = color
        self.start_x = start_x
        self.start_y = start_y
        self.dx = dx
        self.dy = dy
        self.edge_surface = 2 * self.ball_r
    def accept(self, visitor):
        visitor.visit_ball(self)