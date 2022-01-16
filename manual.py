from ImagesAndSounds import resized_main_menu_bg, resized_arrow_keys, resized_space_bar, resized_P_key
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 700))
font1 = pygame.font.Font("fonts/DREAM GLORY.ttf", 70)
font2 = pygame.font.Font("fonts/zig.ttf", 15)
font3 = pygame.font.Font("fonts/DREAM GLORY.ttf", 35)
font4 = pygame.font.Font("fonts/MotionControl-Bold.otf", 28)


def manual_page():
    screen.blit(resized_main_menu_bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    title_text1 = font1.render('Instructions', True, (255, 255, 255))
    titleRect = title_text1.get_rect()
    titleRect.center = (screen.get_width() // 2, 100)
    screen.blit(title_text1, titleRect)
    text1 = font2.render("You are the last wizard on earth Dumbledore, the one and only that can"
                         " save the rest of humanity.", True, (255, 255, 255))
    text2 = font2.render("use your fireballs to kill all the robots but be careful it's not as "
                         "easy as it might sound.", True, (255, 255, 255))
    text3 = font2.render("When the robots are touched by your fireballs they lose 1hp, if their "
                         "health is empty they die.", True, (255, 255, 255))
    text4 = font2.render("The enemies' bullets make 1 point of damage, if one meets one of your "
                         "fireballs they both disappear.", True, (255, 255, 255))
    title_text2 = font3.render("CONTROLS:", True, (255, 255, 255))
    control1 = font4.render(": use the arrow keys to move up/down/left/right", True, (0, 0, 0))
    control2 = font4.render(": use the space bar to shoot fireballs", True, (0, 0, 0))
    control3 = font4.render(": use 'P' to pause the game", True, (0, 0, 0))
    screen.blit(text1, (30, 200))
    screen.blit(text2, (30, 215))
    screen.blit(text3, (30, 230))
    screen.blit(text4, (10, 245))
    screen.blit(title_text2, (50, 290))
    screen.blit(resized_arrow_keys, (150, 355))
    screen.blit(control1, (300, 375))
    screen.blit(resized_space_bar, (120, 470))
    screen.blit(control2, (300, 470))
    screen.blit(resized_P_key, (160, 550))
    screen.blit(control3, (300, 570))


