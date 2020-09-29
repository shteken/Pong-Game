"""
pong_game.py
Pong game which sends the game data to bigquery for analysis
the data should be used for authentication

This version is built with object oriented paradigm
"""
# Objects to define:
# Game
# Board
# Walls
# Bar
# Ball

import pygame

class Game():

    def __init__(self, FPS = 60):
        self.clock = self.create_clock()
        self.mainloop = True
        self.board = Board() # create the board you can configure the screen size here
        self.wall_lines = {
            'top': [(0, 0), (self.board.width, 0)],
            'right': [(0, self.board.height), (self.board.width, self.board.height)],
            'bottom': [(self.board.width, 0), (self.board.width, self.board.height)],
        }
        self.top_wall = Wall(self.board.background, self.wall_lines['top'])
        self.right_wall = Wall(self.board.background, self.wall_lines['right'])
        self.bottom_wall = Wall(self.board.background, self.wall_lines['bottom'])

    def create_clock(self):
        return pygame.time.Clock()

    def start_game(self):
        pygame.init()
        self.board.create_background()
        self.top_wall.create_wall()
        self.right_wall.create_wall()
        self.bottom_wall.create_wall()
        self.board.create_board()
        self.play()

    def is_end_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.mainloop = False # pygame window closed by user
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.mainloop = False # user pressed ESC

    def play(self):
        while self.mainloop:
            pygame.display.flip()
            self.is_end_game()

class Board():

    def __init__(self, width = 640, height = 480, color = (28, 28, 28)):
        self.width = width
        self.height = height
        self.color = color
        self.screen = self.create_screen()
        self.background = self.create_background()

    def create_screen(self):
        return pygame.display.set_mode((self.width, self.height))
    
    def create_background(self):
        background = pygame.Surface(self.screen.get_size())
        background.fill(self.color)
        background = background.convert()
        return background

    def create_board(self):
        return self.screen.blit(self.background, (0,0))

class Wall():

    def __init__(self, background, coordinates, color = (170,170,170), wall_thickness = 30):
        self.background = background
        self.color = color
        self.wall_thickness = wall_thickness
        self.coordinates = coordinates

    def create_wall(self):
        return pygame.draw.line(self.background, self.color, *self.coordinates, self.wall_thickness)   
     

if __name__ == '__main__':
    g = Game()
    print(g.clock)
    g.start_game()
