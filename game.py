import pygame.key
from pygame.locals import *
from Players import *
import math
from ImagesAndSounds import *

# Initialize pygame
pygame.init()

# Create a screen (width and height)
screen = pygame.display.set_mode((1200, 700))
# Change Title
pygame.display.set_caption("The last wizard in 3022")
# Change Icon
icon = pygame.image.load("wizard.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

score = 0
font1 = pygame.font.Font("fonts/DREAM GLORY.ttf", 30)
font2 = pygame.font.Font("fonts/Hello Snow.ttf", 13)
font3 = pygame.font.Font("fonts/ARCADE CLASSIC.TTF", 70)
font4 = pygame.font.Font("fonts/zig.ttf", 35)
font5 = pygame.font.Font("fonts/zig.ttf", 25)
Dumbledore = Player()
enemies_1 = []
enemies_2 = []
bullets_enemy = []
projectiles = []
num_of_enemies = 5


def start():
    global score
    global num_of_enemies
    Dumbledore.dead = False
    Dumbledore.alive = True
    Dumbledore.health = 20
    Dumbledore.x = 10
    Dumbledore.y = 350
    score = 0
    Dumbledore.dying_steps = 0
    while len(enemies_1) < num_of_enemies:
        enemies_1.append(Enemy())
    while len(enemies_2) < num_of_enemies:
        enemies_2.append(EnemyLvl2())


def redrawGameWindow():
    global score
    global num_of_enemies

    screen.blit(resized_background, (0, 0))

    # Draw the player on the screen
    Dumbledore.draw(screen, resized_standing, resized_walkLeft, resized_walkRight, resized_attack,
                    resized_dying_player)

    # Draw the first type of enemy on the screen
    for enemy in enemies_1:
        enemy.draw(screen, resized_walkTowardPlayer_1, resized_walkBackward_1, resized_enemy1_attack,
                   resized_dying1)
        # make the enemy attack randomly between his first and 45th step
        if enemy.steps == random.randrange(0, 45):
            # limit the number of bullets on the screen to 5
            if len(bullets_enemy) < 5:
                enemy.attack = True
                bullets_enemy.append(Bullet(enemy.x, enemy.y, enemy.velocity))
        else:
            enemy.attack = False
        # Draw the enemies' bullets on the screen whenever they attacks
        for bullet in bullets_enemy:
            if enemy.attack:
                bullet.fired = True
                robot_shot.play()
            bullet.draw(screen, resized_bullet)
            if not bullet.fired:
                bullets_enemy.pop(bullets_enemy.index(bullet))
        # enemy respawn
        if enemy.dead:
            robot_collapse.play()
            enemies_1.pop(enemies_1.index(enemy))
            score += 5
            enemies_1.append(Enemy())

    # Draw the second type of enemy on the screen
    for enemy in enemies_2:
        enemy.draw(screen, resized_walkTowardPlayer_2, resized_walkBackward_2, resized_enemy2_attack,
                   resized_dying2)
        if enemy.steps == random.randrange(0, 45, 30):
            if len(bullets_enemy) < 5:
                enemy.attack = True
                bullets_enemy.append(Bullet(enemy.x, enemy.y, enemy.velocity))
        else:
            enemy.attack = False
        # Draw the enemies' bullets on the screen whenever they attacks
        for bullet in bullets_enemy:
            if enemy.attack:
                bullet.fired = True
                robot_shot.play()
            bullet.draw(screen, resized_bullet)
            if not bullet.fired:
                bullets_enemy.pop(bullets_enemy.index(bullet))
        # enemy respawn
        if enemy.dead:
            robot_collapse.play()
            enemies_2.pop(enemies_2.index(enemy))
            score += 10
            enemies_2.append(EnemyLvl2())

    # Draw the player's fireball on the screen whenever he attacks
    for projectile in projectiles:
        projectile.draw(screen, resized_fireball)

    # Draw the score
    score_text = font1.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(score_text, (0, 10))

    # Write PH
    Health_text = font2.render('HP: ' + str(Dumbledore.health), True, (255, 255, 255))
    screen.blit(Health_text, (48, 45))

    # Death
    if Dumbledore.health == 0 and not Dumbledore.dead:
        game_over.play()
    if Dumbledore.dead:
        screen.blit(resized_end_screen_bg, (0, 0))
        enemies_1.clear()
        enemies_2.clear()
        bullets_enemy.clear()
        projectiles.clear()

        game_over_text = font3.render('GAME OVER', True, (0, 0, 0))
        game_over_textRect = game_over_text.get_rect()
        game_over_textRect.center = (screen.get_width() // 2, screen.get_height() // 2 - 30)
        screen.blit(game_over_text, game_over_textRect)

        # get the previous high score from the high_score.txt file
        with open("high_score.txt") as f:
            for line in f:
                (none, none, val) = line.split()
                hisc = val
            f.close()
        # check if the actual score is greater than the high score, if yes change the high score to
        # the actual score, else leave it as it is
        if score > int(hisc):
            file = open("high_score.txt", "w")
            file.write('high score: %s\n' % score)
            file.close()
            high_score_txt = font4.render("High score:" + hisc, True, (0, 0, 0))
        else:
            high_score_txt = font4.render("High score:" + hisc, True, (0, 0, 0))

        # show the high score on the screen
        high_score_txtRect = high_score_txt.get_rect()
        high_score_txtRect.center = (screen.get_width() // 2 - 5, screen.get_height() // 2 + 25)
        screen.blit(high_score_txt, high_score_txtRect)

        end_score_text = font4.render("Score:" + str(score), True, (0, 0, 0))
        end_score_textRect = score_text.get_rect()
        end_score_textRect.center = (screen.get_width() // 2 - 20, screen.get_height() // 2 + 65)
        screen.blit(end_score_text, end_score_textRect)

        death_text = font4.render("YOU DIED!", True, (0, 0, 0))
        death_textRect = death_text.get_rect()
        death_textRect.center = (screen.get_width() // 2 + 15, screen.get_height() // 2 + 105)
        screen.blit(death_text, death_textRect)

        instructions_restart = font5.render("(Press R to restart, press esc to go back to main menu)",
                                            True, (250, 250, 255))
        instructions_restartRect = instructions_restart.get_rect()
        instructions_restartRect.center = (screen.get_width() // 2, screen.get_height() // 2 + 145)
        screen.blit(instructions_restart, instructions_restartRect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            start()
        if keys[pygame.K_ESCAPE]:
            start()
    pygame.display.update()


# game loop
def Game():
    redrawGameWindow()
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if Dumbledore.alive:
            if event.type == KEYDOWN:
                # arrow up = character moves up
                if event.key == K_UP:
                    Dumbledore.yVelocity = -8
                    Dumbledore.right = True
                    Dumbledore.left = False
                # arrow down = character moves down
                elif event.key == K_DOWN:
                    Dumbledore.yVelocity = 8
                    Dumbledore.left = True
                    Dumbledore.right = False
                # arrow left = character moves left
                elif event.key == K_LEFT:
                    Dumbledore.xVelocity = -8
                    Dumbledore.left = True
                    Dumbledore.right = False
                # arrow right = character moves right
                elif event.key == K_RIGHT:
                    Dumbledore.xVelocity = 8
                    Dumbledore.right = True
                    Dumbledore.left = False
                else:
                    Dumbledore.right = False
                    Dumbledore.left = False
                    Dumbledore.steps = 0
                # if space is pressed
                if event.key == K_SPACE:
                    Dumbledore.attack = True
                    fireball_shot.play()
                    bulletX = Dumbledore.x
                    bulletY = Dumbledore.y
                    if len(projectiles) < 10:
                        projectiles.append(Fireball(bulletX + 100,
                                                    bulletY))
                    for i in range(len(projectiles)):
                        projectiles[i].fired = True

            if event.type == pygame.KEYUP:
                # if up or down arrow is released
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    Dumbledore.yVelocity = 0
                    Dumbledore.right = False
                    Dumbledore.left = False
                # if left or right arrow is released
                if event.key == K_RIGHT or event.key == K_LEFT:
                    Dumbledore.xVelocity = 0
                    Dumbledore.right = False
                    Dumbledore.left = False
                # if space is released
                if event.key == K_SPACE:
                    Dumbledore.attack = False
        else:
            Dumbledore.right = False
            Dumbledore.left = False
            Dumbledore.attack = False

    if Dumbledore.alive:
        for projectile in projectiles:
            if not projectile.fired:
                projectiles.pop(projectiles.index(projectile))
            # check for collision between fireball and enemies
            for e in range(num_of_enemies):
                distance1 = math.sqrt(math.pow((enemies_1[e].x - projectile.x), 2) + math.pow(
                    (enemies_1[e].y + 15 - projectile.y), 2))
                if distance1 < 50:
                    explosion_sound.play()
                    enemies_1[e].hit()
                    if projectile in projectiles:
                        projectiles.pop(projectiles.index(projectile))

                distance2 = math.sqrt(math.pow((enemies_2[e].x - projectile.x), 2) + math.pow(
                    (enemies_2[e].y + 15 - projectile.y), 2))
                if distance2 < 50:
                    explosion_sound.play()
                    enemies_2[e].hit()
                    if projectile in projectiles:
                        projectiles.pop(projectiles.index(projectile))

        # checking for collision between player and enemy bullets
        for b in bullets_enemy:
            d1 = math.sqrt(math.pow((Dumbledore.x - 5 - b.x), 2) + math.pow(
                (Dumbledore.y + 15 - b.y), 2))
            if d1 < 50:
                Dumbledore.hit()
                player_hurt.play()
                if b in bullets_enemy:
                    bullets_enemy.pop(bullets_enemy.index(b))

        # checking for collision between fireball and bullets
        for projectile in projectiles:
            for b in bullets_enemy:
                distanceFB = math.sqrt(math.pow((projectile.x - b.x), 2) + math.pow(
                    (projectile.y - b.y + 5), 2))
                if distanceFB < 15:
                    impact.play()
                    if projectile in projectiles:
                        projectiles.pop(projectiles.index(projectile))
                    if b in bullets_enemy:
                        bullets_enemy.pop(bullets_enemy.index(b))

    # checking for boundaries
    if Dumbledore.y >= 530:
        Dumbledore.y = 530
    elif Dumbledore.y <= 220:
        Dumbledore.y = 220
    if Dumbledore.x >= 800:
        Dumbledore.x = 800
    elif Dumbledore.x <= 10:
        Dumbledore.x = 10

    Dumbledore.y += Dumbledore.yVelocity
    Dumbledore.x += Dumbledore.xVelocity
