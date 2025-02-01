import pygame

from constants import *
from helpers import screen, read_comment_from_user
from class_module import Post


class TextPost(Post):
    def __init__(self, username, location, description):
        super().__init__(username, location, description)

    def display(self):
        super().display()

        background_color = (255, 255, 255)  
        text_color = (0, 0, 0)  
        font = pygame.font.Font(None, 36) 
        pygame.draw.rect(screen, background_color, (POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))

        text_surface = font.render(self.description, True, text_color)

        text_rect = text_surface.get_rect(center=(POST_X_POS + POST_WIDTH // 2, POST_Y_POS + POST_HEIGHT // 2))

        screen.blit(text_surface, text_rect)

