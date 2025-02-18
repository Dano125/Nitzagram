import pygame, time

from helpers import screen
from constants import *
from classes import ImagePost, TextPost


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

    # ----- ↓↓↓ POSTS!!! ↓↓↓ -----
    posts_list = []

    shrekxy_img = "Images\\shrekxy_img.jpg"
    image_post = ImagePost("Ron", "North Korea", "Long live Kim Jong Un", shrekxy_img, "Music\\Chess_(slowed).mp3")
    posts_list.append(image_post)
    
    ronaldo_img = "Images\\ronaldo.jpg"
    sec_post = ImagePost("Itay", "Portugal", "Long live Ronaldo", ronaldo_img, "Music\\king.mp3")
    posts_list.append(sec_post)

    masts_img = "Images\\masts_img.jpg"
    tre_post = ImagePost("daniel", "Isral", "sus", masts_img, "Music\scary_shrek_ost.mp3", 0.25) #! / Music\me.mp3 is not curappted
    posts_list.append(tre_post)

    man_img = "Images\\man_img.jpg"
    four_post = ImagePost("Ron", "?", "my man", man_img, "Music\\Spider-Man 3 - Black Suit Theme.mp3", 1)
    posts_list.append(four_post)

    work_img = "Images\\work_img.jpg"
    four_post = ImagePost("Itamer", "Mars", "its me in work", work_img, "Music\\Soviet March.mp3", 0.75)
    posts_list.append(four_post)   
     
    text_post = TextPost("Itay", "Tel Aviv", "i love felix from re:zero!", "best nitzagram" ,(150, 50, 0), (230, 230, 250))
    posts_list.append(text_post)

    sad_photo = "Images\sad_NO-img.jpeg"
    smallest_violin = "Music\world_smalles_violin_wav.mp3"
    sad_post = ImagePost("The team behind this app", "Daniel's Shreks dungeon", "It's dark in here", sad_photo, smallest_violin)
    posts_list.append(sad_post)

    long_post = TextPost("Daniel", "Aroma's free wifi", "im addicted to coffee", "1. In the beginning God created the heaven and the earth (Genesis 1:1)", (50, 50, 0), (250, 230, 250))
    posts_list.append(long_post)

    bad_img = "Images/bad_webp.jpg"
    bad_music = "Music/bad.mp3"
    bad_post = ImagePost("Skull_Man69!", "Your head", "Smells like sh!t in here.", bad_img, bad_music)
    posts_list.append(bad_post)

    post_index_to_display = 0
    shere_btn_flag = False
    running = True
    posts_list[post_index_to_display].play_sound()
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # MOUSE EVENTS ↓↓↓
            if event.type == pygame.MOUSEBUTTONDOWN:  # check for mouse events
                mouse_pos = event.pos  # Get mouse position

                if posts_list[post_index_to_display].like_rect.collidepoint(mouse_pos):  # check if mouse click like
                     posts_list[post_index_to_display].add_like()
                     
                if posts_list[post_index_to_display].post_rect.collidepoint(mouse_pos):  # check if mouse click post
                    if post_index_to_display == len(posts_list) - 1:  # go to the next post
                        post_index_to_display = 0
                    else:
                        post_index_to_display += 1
                    
                    pygame.mixer.music.stop()  # clear the previos audio
                    posts_list[post_index_to_display].play_sound()  # if the post has audio attached, play the audio
                # check if mouse click comments
                if posts_list[post_index_to_display].comment_rect.collidepoint(mouse_pos):
                    posts_list[post_index_to_display].add_comment()  # type and add a comment
                
                if posts_list[post_index_to_display].share_rect.collidepoint(mouse_pos):
                    ## Operation no friends ##
                    shere_btn_flag = True

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Shows the next post according to the post index
        posts_list[post_index_to_display].display()

        if shere_btn_flag:
            rec = pygame.Surface((WINDOW_WIDTH/10 * 8, WINDOW_HEIGHT/10 * 2))
            rec.set_alpha(240)
            rec.fill((150,150,150))
            screen.blit(rec, (WINDOW_WIDTH/10, WINDOW_HEIGHT/10 * 4))

            # Shere button roast
            shere_text_pos = (WINDOW_WIDTH/10 * 2 - 5, WINDOW_HEIGHT/100 * 45)
            font = pygame.font.SysFont('chalkduster.ttf', 30)
            comment_text = font.render("lol, You have no friends", True, BLACK)
            text2 = font.render("who are you fooling", True, BLACK)
            screen.blit(comment_text, shere_text_pos)
            screen.blit(text2, (shere_text_pos[0] + 15, shere_text_pos[1] + 35))

        # Update display - without input update everything
        pygame.display.update()

        # Shere button roast 2nd
        if shere_btn_flag:
            time.sleep(2)
            shere_btn_flag = False

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
