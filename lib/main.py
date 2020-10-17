from game import Game

print('Enter your name:')
user_name = input()
game = Game(user_name)
game.play()