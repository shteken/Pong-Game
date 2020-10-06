"""
pong_game_visitor.py
Pong game which sends the game data to bigquery for analysis
the data should be used for authentication

This version is built with object oriented paradigm with visitor design pattern
"""
# Objects to define:
# Game
# Board
# Walls
# Bar
# Ball

import pygame

class Board:
    def accept(self, visitor):
        visitor.visitBody(self)

class Wall:
    def __init__(self, coordinates, wall_thickness, color = (170,170,170)):
        self.color = color
        self.wall_thickness = wall_thickness
        self.coordinates = coordinates

class Bar:
    def __init__(self, screen, start_x = 5, start_y = 240, bar_width = 10, bar_height = 50, color = (170,170,170)):
        self.screen = screen
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.start_x = start_x
        self.start_y = start_y
        self.color = color

class Ball:
    def __init__(self, name):
        self.name = name
    def accept(self, visitor):
        visitor.visitWheel(self)