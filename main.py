import pygame
from game import Game

class Multiplayer:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("fluch der Karibik.ogg")

        pygame.init()

        size = (700,  500)
        board_size = (10, 20, 20)  # (horizontal_cell_count, vertical_cell_count, cell_size)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Tetris')

        game = Game(board_size, screen)


        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

        game.run()
        pygame.quit()


        pygame.quit()

