import pygame
from draw_visitor import DrawVisitor
from move_bar_visitor import MoveBarVisitor
from move_ball_visitor import MoveBallVisitor
from board import Board

class Game:
    def __init__(self):
        self.mainloop = True
        self.width = 640
        self.height = 480
        self.FPS = 60

    def accept(self, visitor):
        visitor.visit_game(self)

    def handle_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end() # pygame window closed by user
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.end() # user pressed ESC

    def end(self):
        self.mainloop = False

    def play(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height)) # screen is created
        clock = pygame.time.Clock()        #create pygame clock object
        milliseconds = clock.tick(self.FPS)  # milliseconds passed since last frame
        seconds = milliseconds / 1000.0 # seconds passed since last frame (float)

        board = Board(self.width, self.height)
        draw_visitor = DrawVisitor(screen)
        move_bar_visitor = MoveBarVisitor()
        move_ball_visitor = MoveBallVisitor(self, seconds)

        while self.mainloop:
            self.handle_quit_event()
            board.accept(move_ball_visitor)
            board.accept(move_bar_visitor)
            board.accept(draw_visitor)
            pygame.display.flip()