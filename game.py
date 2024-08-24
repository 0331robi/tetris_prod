import pygame
from player import Player
from board import Board

class Game:
    def __init__(self, board_size, screen):
        self.board = Board(board_size)
        self.board2 = Board(board_size)
        self.player = Player(board_size, screen)
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.done = False
        self.drop_speed = 500
        self.last_drop_time = pygame.time.get_ticks()
        self.score = 0
        self.score2 = 0
        self.logo_big = pygame.image.load("baby shark.webp")
        self.logo = pygame.transform.scale(self.logo_big, (700, 500)).convert_alpha()
        self.logo.set_alpha(150)
        self.game_over = False
        self.lose_sound = pygame.mixer.Sound("lose.mp3")

        self.player2 = Player(board_size, screen)
        self.player2.x_position = (board_size[0] // 2 - 2) + 10  # Anpassen der Startposition auf das zweite Spielfeld

    def run(self):
        while not self.done:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                # Steuerung für Spieler 1
                if event.key == pygame.K_a:
                    self.player.move(-1, 0)
                    if self.board.is_collision(self.player):
                        self.player.move(1, 0)
                elif event.key == pygame.K_d:
                    self.player.move(1, 0)
                    if self.board.is_collision(self.player):
                        self.player.move(-1, 0)
                elif event.key == pygame.K_s:
                    self.player.move(0, 1)
                    if self.board.is_collision(self.player):
                        self.player.move(0, -1)
                        self.lock_piece_player1()
                elif event.key == pygame.K_w:
                    self.player.rotate()
                    if self.board.is_collision(self.player):
                        self.player.rotate()
                        self.player.rotate()
                        self.player.rotate()

                # Steuerung für Spieler 2
                elif event.key == pygame.K_LEFT:
                    self.player2.move(-1, 0)
                    if self.board2.is_collision(self.player2):
                        self.player2.move(1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player2.move(1, 0)
                    if self.board2.is_collision(self.player2):
                        self.player2.move(-1, 0)
                elif event.key == pygame.K_DOWN:
                    self.player2.move(0, 1)
                    if self.board2.is_collision(self.player2):
                        self.player2.move(0, -1)
                        self.lock_piece_player2()
                elif event.key == pygame.K_UP:
                    self.player2.rotate()
                    if self.board2.is_collision(self.player2):
                        self.player2.rotate()
                        self.player2.rotate()
                        self.player2.rotate()

    def update(self):
        if pygame.time.get_ticks() - self.last_drop_time > self.drop_speed:
            self.player.move(0, 1)
            self.player2.move(0, 1)
            if self.board.is_collision(self.player):
                self.player.move(0, -1)
                self.lock_piece_player1()
            if self.board2.is_collision(self.player2):
                self.player2.move(0, -1)
                self.lock_piece_player2()
            self.last_drop_time = pygame.time.get_ticks()

    def lock_piece_player1(self):
        self.board.add_shape_to_board(self.player)
        self.score += self.board.clear_lines()
        self.player.reset()
        if self.board.is_collision(self.player):
            self.game_over = True

    def lock_piece_player2(self):
        self.board2.add_shape_to_board(self.player2)
        self.score2 += self.board2.clear_lines()
        self.player2.reset()
        if self.board2.is_collision(self.player2):
            self.game_over = True

    def render(self):
        if not self.game_over:
            self.screen.fill((220, 220, 220))
            self.screen.blit(self.logo, (0, 0))
            self.board.display(self.screen)
            self.board2.display2(self.screen)
            self.player.display()
            self.player2.display2()
            self.draw_grid()
            self.draw_grid1()

            font = pygame.font.SysFont('Calibiri', 25, True, False)
            text = font.render(f"Score {self.score}", True, (40, 102, 2))
            self.screen.blit(text, (200, 40))
            font = pygame.font.SysFont('Calibiri', 25, True, False)
            text = font.render(f"Score {self.score2}", True, (40, 102, 2))
            self.screen.blit(text, (400, 40))
        else:
            self.screen.fill((0, 0, 0))
            font = pygame.font.SysFont('Calibiri', 50, True, False)
            text = font.render(f"Game Over, dein Score war {self.score}!", True, (255, 0, 0))
            self.screen.blit(text, (0, 0))
            self.lose_sound.play()

        pygame.display.flip()

    def draw_grid(self):
        for i in range(self.board.board_size[1]):
            for j in range(self.board.board_size[0]):
                pygame.draw.rect(self.screen, (200, 160, 10),
                                 (j * self.board.board_size[2] + 40, 60 + i * self.board.board_size[2],
                                  self.board.board_size[2], self.board.board_size[2]), 1)

    def draw_grid1(self):
        for i in range(self.board2.board_size[1]):
            for j in range(self.board2.board_size[0]):
                pygame.draw.rect(self.screen, (200, 160, 10),
                                 (j * self.board2.board_size[2] + 450, 60 + i * self.board2.board_size[2],
                                  self.board2.board_size[2], self.board2.board_size[2]), 1)
