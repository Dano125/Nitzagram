import pygame
from pygame.examples.cursors import image

from helpers import screen
from constants import *
from classes import Post


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    # ----- ↓↓↓ EMPTY TEST POST!!! ↓↓↓ -----
    test_post = Post.Post("daniel", "beer", "yay", 0, [])
    like_rect = pygame.Rect(LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS, LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT)

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # check for mouse events
                mouse_pos = event.pos  # Get mouse position
                if like_rect.collidepoint(mouse_pos):  # check if mouse click like
                    test_post.add_like()

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # ↓↓↓ TEST!!! ↓↓↓
        test_post.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
