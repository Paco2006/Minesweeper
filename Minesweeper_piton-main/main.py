from game import Game
from board import Board

size = (20, 50)
prob = 0.1
board = Board(size, prob)
screenSize = (1700, 800)
game = Game(board, screenSize)
game.run()
