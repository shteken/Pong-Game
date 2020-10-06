from draw_visitor import DrawVisitor
from move_bar_visitor import MoveBarVisitor
from board import Board
import pygame

mainloop = True
width = 640
height = 480

pygame.init()
screen = pygame.display.set_mode((width, height)) # screen is created
board = Board(width, height)
draw_visitor = DrawVisitor(screen)
move_bar_visitor = MoveBarVisitor()

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
    board.accept(move_bar_visitor)
    board.accept(draw_visitor)
    pygame.display.flip()