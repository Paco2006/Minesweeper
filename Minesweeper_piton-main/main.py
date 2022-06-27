from game import Game
from board import Board

size = (20, 50) #goleminata na blokcheto
prob = 0.1 #procenta - bombi/blokcheta
board = Board(size, prob) #goleminata na poleto i kolko bombi ima
screenSize = (1700, 800) #goleminata na terminala/igrata
game = Game(board, screenSize) #igrata - pole i zarmeri
game.run() #runvame igrata
