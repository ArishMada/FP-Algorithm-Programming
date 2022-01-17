import pygame.event
from game import *
from manual import manual_page
import time

pygame.init()

screen = pygame.display.set_mode((1200, 700))
started = True
running = False
pause = False
instruction = False
loading = False


# initialize the pause function for when the user clicks on p
def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(resized_background, (0, 0))
        font8 = pygame.font.Font("fonts/DREAM GLORY.ttf", 90)
        pause_text = font8.render('Paused', True, (255, 255, 255))
        screen.blit(pause_text, (450, 240))
        button("CONTINUE", 100, 500, 300, 50, 45, "continue")
        button("QUIT", 900, 500, 200, 50, 45, "quit")

        pygame.display.update()


# initializing a loading screen because the time to lunch the game is too fast
def loading_screen():
    loading_background = pygame.Surface(screen.get_size())
    loading_background.fill((0, 0, 0))
    for sec in range(3):
        screen.blit(loading_background, (0, 0))
        screen.blit(font4.render('Starting in ' + str(3 - sec), True, (255, 255, 255)), (410, 320))
        pygame.display.update()
        time.sleep(1)


def button(msg, x, y, width, height, fontSize, action=None):
    global started, instruction, pause, running, loading

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # text (placed in the middle of the rectangle that represent the button)
    font6 = pygame.font.Font("fonts/zig.ttf", fontSize)
    white_text = font6.render(msg, True, (255, 255, 255))
    black_text = font6.render(msg, True, (0, 0, 0))
    textRect = white_text.get_rect()
    textRect.center = (x + width / 2, y + height / 2)
    screen.blit(white_text, textRect)
    # check hover
    # check x and y coordinate of the mouse
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, (250, 250, 250), (x, y, width, height))
        screen.blit(black_text, textRect)
        if click[0] == 1 and action is not None:
            button_click.play()
            if action == "play":
                start()
                loading_screen()
                running = True
                started = False
            elif action == "continue":
                running = True
                pause = False
            elif action == "quit":
                instruction = False
                running = False
                started = True
                main()
            elif action == "manual":
                instruction = True
                started = False
            elif action == "reset":
                file = open("high_score.txt", "w")
                file.write('high score: %s\n' % "0")
                file.close()
            elif action == "exit":
                exit()
    else:
        pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
        screen.blit(white_text, textRect)


def main():
    global started, running, pause, instruction, loading
    while started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        font7 = pygame.font.Font("fonts/DREAM GLORY.ttf", 70)
        screen.blit(resized_main_menu_bg, (0, 0))
        game_name = font7.render('The Last wizard in 3022', True, (255, 255, 255))
        game_nameRect = game_name.get_rect()
        game_nameRect.center = (screen.get_width() // 2, screen.get_height() // 2 - 120)
        screen.blit(game_name, game_nameRect)

        with open("high_score.txt") as f:
            for line in f:
                (none, none, val) = line.split()
                hisc = val
            f.close()
        font8 = pygame.font.Font("fonts/MotionControl-Bold.otf", 45)
        highscore_text = font8.render("High score: " + hisc, True, (255, 255, 255))
        screen.blit(highscore_text, (485, 320))

        # button 1: to start the game
        button('START', 450, 400, 300, 50, 45, "play")

        # button 2: to go to the instruction page
        button('MANUAL', 480, 480, 240, 50, 45, "manual")

        # button 3: to exit the game
        button('EXIT', 480, 560, 240, 50, 45, "exit")

        pygame.display.update()
    while running:
        Game()
        for event in pygame.event.get():
            # Initialize quit button
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            running = False
            pause = True
            paused()
        if keys[pygame.K_ESCAPE] and Dumbledore.dead:
            started = True
            running = False
            main()
        if keys[pygame.K_r] and Dumbledore.dead:
            loading_screen()
    while instruction:
        manual_page()
        button("BACK", 800, 500, 200, 50, 45, "quit")
        button("Reset high score", 880, 640, 250, 50, 18, "reset")
        pygame.display.update()


main()
