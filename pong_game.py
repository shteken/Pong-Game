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

class Game:

    def __init__(self, FPS = 60, width = 640, height = 480):
        self.clock = self.create_clock()
        self.mainloop = True
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)

    def create_clock(self):
        return pygame.time.Clock()

    def start_game(self):
        pygame.init()
        self.board.create_board() # create the board
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

class Board:

    def __init__(self, width, height, color = (28, 28, 28)):

        self.width = width
        self.height = height
        self.color = color
        self.wall_lines = {
            'top': [(0, 0), (self.width, 0)],
            'right': [(0, self.height), (self.width, self.height)],
            'bottom': [(self.width, 0), (self.width, self.height)],
        }

    def create_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height)) # screen is created
        return self.screen
    
    def create_background(self):
        self.background = pygame.Surface((self.width, self.height)) # background is created
        self.background.fill(self.color)
        self.background = self.background.convert()
        return self.background

    def create_walls(self):
        self.top_wall = Wall(self.background, self.wall_lines['top']) 
        self.right_wall = Wall(self.background, self.wall_lines['right'])
        self.bottom_wall = Wall(self.background, self.wall_lines['bottom'])
        self.top_wall.create_wall() # walls are created
        self.right_wall.create_wall()
        self.bottom_wall.create_wall()
        return self.top_wall, self.right_wall, self.bottom_wall

    def create_board(self):
        self.create_screen()
        self.create_background()
        self.create_walls()
        self.screen.blit(self.background, (0,0)) # board is drawn

class Wall:

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
