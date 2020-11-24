"""
main.py
Pong game which sends the mouse movement data to bigquery for analysis.
The data could be used, for example, for the authentication of the user in a web service.

This version is built with object oriented paradigm with visitor design pattern
"""
from game import Game

print('Enter your name:')
user_name = input()
game = Game(user_name)
game.play()