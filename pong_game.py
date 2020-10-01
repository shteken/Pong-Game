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

    def __init__(self, FPS = 60, width = 640, height = 480, wall_thickness = 30):
        self.clock = self.create_clock()
        self.mainloop = True
        self.width = width
        self.height = height
        self.wall_thickness = wall_thickness
        self.screen = self.create_screen()
        self.board = Board(self.screen, self.width, self.height, self.wall_thickness)
        self.bar = Bar(self.screen)

    def create_clock(self):
        return pygame.time.Clock()

    def create_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height)) # screen is created
        return self.screen

    def start_game(self):
        pygame.init()
        self.board.create_board() # create the board
        self.bar.create_bar() # create the bar
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
            self.is_end_game()
            self.board.draw_board()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.bar.move_bar(mouse_y, self.wall_thickness, self.height)
            pygame.display.flip()


class Board:

    def __init__(self, screen, width, height, wall_thickness, color = (28, 28, 28)):
        self.screen = screen
        self.width = width
        self.height = height
        self.color = color
        self.wall_thickness = wall_thickness
        self.wall_lines = {
            'top': [(0, 0), (self.width, 0)],
            'right': [(0, self.height), (self.width, self.height)],
            'bottom': [(self.width, 0), (self.width, self.height)],
        }
    
    def create_background(self):
        self.background = pygame.Surface((self.width, self.height)) # background is created
        self.background.fill(self.color)
        self.background = self.background.convert()
        return self.background

    def create_walls(self):
        self.top_wall = Wall(self.background, self.wall_lines['top'], self.wall_thickness) 
        self.right_wall = Wall(self.background, self.wall_lines['right'], self.wall_thickness)
        self.bottom_wall = Wall(self.background, self.wall_lines['bottom'], self.wall_thickness)
        self.top_wall.create_wall() # walls are created
        self.right_wall.create_wall()
        self.bottom_wall.create_wall()
        return self.top_wall, self.right_wall, self.bottom_wall

    def create_board(self):
        self.create_background()
        self.create_walls()

    def draw_board(self):
        self.screen.blit(self.background, (0,0)) # board is drawn 

class Wall:

    def __init__(self, background, coordinates, wall_thickness, color = (170,170,170)):
        self.background = background
        self.color = color
        self.wall_thickness = wall_thickness
        self.coordinates = coordinates

    def create_wall(self):
        return pygame.draw.line(self.background, self.color, *self.coordinates, self.wall_thickness)   

class Bar:

    def __init__(self, screen, bar_width = 10, bar_height = 50, color = (170,170,170), start_x = 5, start_y = 240):
        self.screen = screen
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.start_x = start_x
        self.start_y = start_y
        self.color = color
    
    def create_bar(self):
        print(self.bar_width, self.bar_height)
        self.barsurface = pygame.Surface((self.bar_width, self.bar_height))
        self.barsurface.set_colorkey((0, 0, 0))
        # pygame.draw.rect(surface, color, rect)
        self.barrect = self.barsurface.get_rect()
        pygame.draw.rect(self.barsurface, self.color, (0, 0, self.bar_width, self.bar_height))
        self.barsurface = self.barsurface.convert_alpha()
        self.screen.blit(self.barsurface, (self.start_x, self.start_y))
        return self.barsurface
    
    def move_bar(self, mouse_y, wall_thickness, height):
        new_y = mouse_y
        if new_y <= wall_thickness/2:
            new_y = int(wall_thickness/2)
        elif new_y >= height - self.bar_height - wall_thickness/2:
            new_y = int(height - self.bar_height - wall_thickness/2)
        self.screen.blit(self.barsurface, (self.start_x, new_y))

if __name__ == '__main__':
    g = Game()
    print(g.clock)
    g.start_game()
