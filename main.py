import pygame
from game import Game

pygame.init()

size = (400, 500)
board_size = (10, 20, 20)  # (horizontal_cell_count, vertical_cell_count, cell_size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tetris')

game = Game(board_size, screen)
game.run()

pygame.quit()
