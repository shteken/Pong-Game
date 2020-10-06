import pygame

class DrawVisitor:
    def __init__(self, screen):
        self.screen = screen

    def visit_board(self, board):
        background = pygame.Surface((board.width, board.height)) # background is created
        background.fill(board.color)
        background.convert()
        self.screen.blit(background, (0,0)) # board is drawn 

    def visit_hittable(self, hittable):
        surface = pygame.Surface((hittable.width, hittable.height))
        surface.set_colorkey((0, 0, 0))
        pygame.draw.rect(surface, hittable.color, (0, 0, hittable.width, hittable.height))
        surface = surface.convert_alpha()
        self.screen.blit(surface, (hittable.start_x, hittable.start_y))

    def visit_wall(self, wall):
        self.visit_hittable(wall)

    def visit_bar(self, bar):
        self.visit_hittable(bar)

    def visit_ball(self, ball):
        surface = pygame.Surface((ball.edge_surface, ball.edge_surface))     #create a new surface (black by default)
        surface.set_colorkey((0,0,0))         #make black the transparent color (red,green,blue)
        pygame.draw.circle(surface, ball.color, (ball.ball_r, ball.ball_r), ball.ball_r) # paint white circle
        surface = surface.convert_alpha()
        self.screen.blit(surface, (ball.start_x, ball.start_y))