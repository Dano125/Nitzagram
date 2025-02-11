import pygame

from constants import *
from helpers import screen, from_text_to_array
from class_module import Post


class TextPost(Post):
    def __init__(self, username, location, description, text, text_color, background_color, sound=None):
        super().__init__(username, location, description, sound)
        self.text = text
        self.text_color = text_color
        self.bg_color = background_color

    def display(self):
        super().display()

        bg_rect = pygame.rect.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.bg_color, bg_rect)

        font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
        text_list = from_text_to_array(self.text)
        for i in text_list:
            text = font.render(i, True, self.text_color)
            text_rect = text.get_rect(center=(POST_X_POS + POST_WIDTH // 2, ((POST_Y_POS + POST_HEIGHT // 2) - ((TEXT_POST_LINE_HEIGHT * len(text_list)) // 2) + TEXT_POST_LINE_HEIGHT * text_list.index(i))))
            screen.blit(text, text_rect)



