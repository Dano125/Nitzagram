import pygame

from constants import *
from helpers import screen, read_comment_from_user
from class_module import Post


class Comment:
    def __init__(self, text):
        self.text = text

    def display(self):
        print("A")
