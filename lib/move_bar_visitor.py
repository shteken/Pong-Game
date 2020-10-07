import pygame

class MoveBarVisitor:     
    def visit_board(self, board):
        self.walls = []

    def visit_wall(self, wall):
        self.walls.append(wall)

    def visit_bar(self, bar):
        _mouse_x, mouse_y = pygame.mouse.get_pos()
        new_y = mouse_y
        
        x_bar_left, _y_bar_top, x_bar_right, _y_bar_bottom = bar.get_coordinates()
        x_bar = (x_bar_left + x_bar_right) // 2
        for wall in self.walls:
            x1, y1, x2, y2 = wall.get_coordinates()
            if x_bar >= x1 and x_bar <= x2 and new_y + bar.height >= y1 and new_y <= y2:
                if bar.start_y > y1:
                    new_y = y1 + wall.height
                else:
                    new_y = y1 - bar.height
        bar.move(bar.start_x, new_y)

    def visit_ball(self, ball):
        pass