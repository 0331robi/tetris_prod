import pygame
import sys
from main import pygam

# Pygame initialisieren
pygame.init()

# Fenstergröße und Titel
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Startseite")

# Farben
white = (255, 255, 255)
black = (0, 0, 0)
gray = (100, 100, 100)
light_gray = (170, 170, 170)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
# Schriftarten
font = pygame.font.SysFont(None, 74)
button_font = pygame.font.SysFont(None, 50)

# Texte
title_text = font.render("tetris", True, green)
singleplayer_text = button_font.render("Singleplayer", True, white)
multiplayer_text = button_font.render("Multiplayer", True, white)
quit_text = button_font.render("Exit", True, red)

# Button-Position und -Größe
button_width, button_height = 300, 80
singleplayer_button_rect = pygame.Rect(screen_width // 2 - button_width // 2, 200, button_width, button_height)
multiplayer_button_rect = pygame.Rect(screen_width // 2 - button_width // 2, 300, button_width, button_height)
quit_button_rect = pygame.Rect(screen_width // 2 - button_width // 2, 400, button_width, button_height)


def draw_start_screen():
    screen.fill(black)
    # Titeltext zeichnen
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 100))

    # Buttons zeichnen
    pygame.draw.rect(screen, blue, singleplayer_button_rect)
    screen.blit(singleplayer_text, (singleplayer_button_rect.x + 30, singleplayer_button_rect.y + 15))

    pygame.draw.rect(screen, blue, multiplayer_button_rect)
    screen.blit(multiplayer_text, (multiplayer_button_rect.x + 30, multiplayer_button_rect.y + 15))

    pygame.draw.rect(screen, blue, quit_button_rect)
    screen.blit(quit_text, (quit_button_rect.x + 70, quit_button_rect.y + 15))

    pygame.display.flip()


def main():
    while True:
        draw_start_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if singleplayer_button_rect.collidepoint(event.pos):
                    # Hier könnte der Start des Singleplayer-Spiels implementiert werden
                    print("Singleplayer startet...")  # Dies ist nur ein Platzhalter

                if multiplayer_button_rect.collidepoint(event.pos):
                    # Hier könnte der Start des Multiplayer-Spiels implementiert werden
                    print("Multiplayer startet...")  # Dies ist nur ein Platzhalter
                    multiplayer = Multiplayer()

                if quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()

