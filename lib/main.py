from draw_visitor import DrawVisitor
from move_bar_visitor import MoveBarVisitor
from move_ball_visitor import MoveBallVisitor
from board import Board
import pygame

mainloop = True
width = 640
height = 480
FPS = 60

pygame.init()
screen = pygame.display.set_mode((width, height)) # screen is created
clock = pygame.time.Clock()        #create pygame clock object
milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
seconds = milliseconds / 1000.0 # seconds passed since last frame (float)

board = Board(width, height)
draw_visitor = DrawVisitor(screen)
move_bar_visitor = MoveBarVisitor()
move_ball_visitor = MoveBallVisitor(seconds)

def is_end_game():
    global mainloop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC

while mainloop:
    is_end_game()
    board.accept(move_ball_visitor)
    board.accept(move_bar_visitor)
    board.accept(draw_visitor)
    pygame.display.flip()