import uuid
import pygame
from draw_visitor import DrawVisitor
from move_bar_visitor import MoveBarVisitor
from move_ball_visitor import MoveBallVisitor
from mouse_position import MousePosition
from board import Board

# specify here path to credentials and table_id
positions = MousePosition('./valiant-nucleus-162210-628ad4c9fbe7.json', 'valiant-nucleus-162210.test.positions')

class Game:
    def __init__(self, user_name):
        width = 640
        height = 480
        FPS = 50 # frames per second
        screen = pygame.display.set_mode((width, height)) # screen is created
        clock = pygame.time.Clock() # create pygame clock object
        milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
        seconds = milliseconds / 1000.0 # seconds passed since last frame (float)
        self.user_name = user_name
        self.game_id = uuid.uuid4()
        self.mainloop = True
        self.board = Board(width, height)
        self.draw_visitor = DrawVisitor(screen)
        self.move_bar_visitor = MoveBarVisitor()
        self.move_ball_visitor = MoveBallVisitor(self, seconds)

    def accept(self, visitor):
        """
        visit objects
        """
        visitor.visit_game(self)

    def handle_quit_event(self):
        """
        the user wants to quit the game
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end() # pygame window closed by user
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.end() # user pressed ESC

    def end(self):
        """
        exit the game
        """
        self.mainloop = False

    @positions.save_mouse_position
    def change_frames(self):
        """
        check if the user exit the program, if no then each action visits each object
        """
        self.handle_quit_event()
        self.board.accept(self.move_ball_visitor)
        self.board.accept(self.move_bar_visitor)
        self.board.accept(self.draw_visitor)
        pygame.display.flip()

    @positions.send_data
    def play(self):
        """
        initialize the game and run it
        """
        pygame.init()
        while self.mainloop:
            #print(positions)
            self.change_frames()
        #print(positions)