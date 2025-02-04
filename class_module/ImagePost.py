import pygame

from constants import *
from helpers import screen
from class_module import Post


class ImagePost(Post):
    def __init__(self, username, location, description, img_path):
        super().__init__(username, location, description)
        self.img_path = img_path

    def display(self):
        super().display()

        image = pygame.image.load(self.img_path)
        # Fix size
        image = pygame.transform.scale(image, (POST_WIDTH, POST_HEIGHT))
        screen.blit(image, (POST_X_POS, POST_Y_POS))