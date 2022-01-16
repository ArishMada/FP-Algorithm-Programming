import pygame
from pygame import mixer

pygame.init()

# IMAGES
# Main menu background
main_menu_bg = pygame.image.load("main menu.jpg")
resized_main_menu_bg = pygame.transform.scale(main_menu_bg, (1200, 720))

# Background
background = pygame.image.load("bg.png")
resized_background = pygame.transform.scale(background, (1200, 720))

# Player standing
standing = [pygame.image.load("player image/1_IDLE_000.png"),
            pygame.image.load("player image/1_IDLE_001.png"),
            pygame.image.load("player image/1_IDLE_002.png"),
            pygame.image.load("player image/1_IDLE_003.png"),
            pygame.image.load("player image/1_IDLE_004.png")]
resized_standing = []
for i in range(len(standing)):
    resized_standing.append(pygame.transform.scale(standing[i], (90, 90)))

# Player walking toward the right
walkRight = [pygame.image.load("player image/2_RUN_000.png"),
             pygame.image.load("player image/2_RUN_001.png"),
             pygame.image.load("player image/2_RUN_002.png"),
             pygame.image.load("player image/2_RUN_003.png"),
             pygame.image.load("player image/2_RUN_004.png")]

resized_walkRight = []
for i in range(len(walkRight)):
    resized_walkRight.append(pygame.transform.scale(walkRight[i], (103, 103)))

# Player walking toward the left
walkLeft = [pygame.image.load("player image/2_RUN_004.png"),
            pygame.image.load("player image/2_RUN_003.png"),
            pygame.image.load("player image/2_RUN_002.png"),
            pygame.image.load("player image/2_RUN_001.png"),
            pygame.image.load("player image/2_RUN_000.png")]

resized_walkLeft = []
for i in range(len(walkLeft)):
    resized_walkLeft.append(pygame.transform.scale(walkLeft[i], (103, 103)))

# Player in attacking position
attack = pygame.image.load("player image/ATTACK.png")

resized_attack = pygame.transform.scale(attack, (150, 100))

# Player dying
dying_player = [pygame.image.load("player image/4_DIE_000.png"),
                pygame.image.load("player image/4_DIE_001.png"),
                pygame.image.load("player image/4_DIE_002.png"),
                pygame.image.load("player image/4_DIE_003.png"),
                pygame.image.load("player image/4_DIE_004.png")]

resized_dying_player = []
for i in range(len(dying_player)):
    resized_dying_player.append(pygame.transform.scale(dying_player[i], (100, 100)))

# Fireball
fireball = pygame.image.load("player image/Shot.png")

resized_fireball = pygame.transform.scale(fireball, (70, 70))

# Robot1 walking toward the player and backward
walkTowardPlayer_1 = [pygame.image.load("enemy1 image/Walk_000.png"),
                      pygame.image.load("enemy1 image/Walk_001.png"),
                      pygame.image.load("enemy1 image/Walk_002.png"),
                      pygame.image.load("enemy1 image/Walk_003.png"),
                      pygame.image.load("enemy1 image/Walk_004.png"),
                      pygame.image.load("enemy1 image/Walk_005.png"),
                      pygame.image.load("enemy1 image/Walk_006.png"),
                      pygame.image.load("enemy1 image/Walk_007.png"),
                      pygame.image.load("enemy1 image/Walk_008.png"),
                      pygame.image.load("enemy1 image/Walk_009.png"),
                      pygame.image.load("enemy1 image/Walk_010.png"),
                      pygame.image.load("enemy1 image/Walk_011.png")]

resized_walkTowardPlayer_1 = []
for i in range(len(walkTowardPlayer_1)):
    resized_walkTowardPlayer_1.append(pygame.transform.scale(walkTowardPlayer_1[i], (100, 100)))

walkBackward_1 = [pygame.image.load("enemy1 image/Walk_011.png"),
                  pygame.image.load("enemy1 image/Walk_010.png"),
                  pygame.image.load("enemy1 image/Walk_009.png"),
                  pygame.image.load("enemy1 image/Walk_008.png"),
                  pygame.image.load("enemy1 image/Walk_007.png"),
                  pygame.image.load("enemy1 image/Walk_006.png"),
                  pygame.image.load("enemy1 image/Walk_005.png"),
                  pygame.image.load("enemy1 image/Walk_004.png"),
                  pygame.image.load("enemy1 image/Walk_003.png"),
                  pygame.image.load("enemy1 image/Walk_002.png"),
                  pygame.image.load("enemy1 image/Walk_001.png"),
                  pygame.image.load("enemy1 image/Walk_000.png")]

resized_walkBackward_1 = []
for i in range(len(walkBackward_1)):
    resized_walkBackward_1.append(pygame.transform.scale(walkBackward_1[i], (100, 100)))

# Robot2 walking toward the player and backward
walkTowardPlayer_2 = [pygame.image.load("enemy2 image/Walk_000.png"),
                      pygame.image.load("enemy2 image/Walk_001.png"),
                      pygame.image.load("enemy2 image/Walk_002.png"),
                      pygame.image.load("enemy2 image/Walk_003.png"),
                      pygame.image.load("enemy2 image/Walk_004.png"),
                      pygame.image.load("enemy2 image/Walk_005.png"),
                      pygame.image.load("enemy2 image/Walk_006.png"),
                      pygame.image.load("enemy2 image/Walk_007.png"),
                      pygame.image.load("enemy2 image/Walk_008.png"),
                      pygame.image.load("enemy2 image/Walk_009.png"),
                      pygame.image.load("enemy2 image/Walk_010.png"),
                      pygame.image.load("enemy2 image/Walk_011.png")]

resized_walkTowardPlayer_2 = []
for i in range(len(walkTowardPlayer_2)):
    resized_walkTowardPlayer_2.append(pygame.transform.scale(walkTowardPlayer_2[i], (100, 100)))

walkBackward_2 = [pygame.image.load("enemy2 image/Walk_011.png"),
                  pygame.image.load("enemy2 image/Walk_010.png"),
                  pygame.image.load("enemy2 image/Walk_009.png"),
                  pygame.image.load("enemy2 image/Walk_008.png"),
                  pygame.image.load("enemy2 image/Walk_007.png"),
                  pygame.image.load("enemy2 image/Walk_006.png"),
                  pygame.image.load("enemy2 image/Walk_005.png"),
                  pygame.image.load("enemy2 image/Walk_004.png"),
                  pygame.image.load("enemy2 image/Walk_003.png"),
                  pygame.image.load("enemy2 image/Walk_002.png"),
                  pygame.image.load("enemy2 image/Walk_001.png"),
                  pygame.image.load("enemy2 image/Walk_000.png")]

resized_walkBackward_2 = []
for i in range(len(walkBackward_1)):
    resized_walkBackward_2.append(pygame.transform.scale(walkBackward_2[i], (100, 100)))

# Robots attacking
enemy1_attack = pygame.image.load("enemy1 image/Shot.png")
resized_enemy1_attack = pygame.transform.scale(enemy1_attack, (110, 110))
enemy2_attack = pygame.image.load("enemy2 image/Shot.png")
resized_enemy2_attack = pygame.transform.scale(enemy2_attack, (100, 100))

# Robots death
dying1 = [pygame.image.load("enemy1 image/Death_001.png"),
          pygame.image.load("enemy1 image/Death_002.png"),
          pygame.image.load("enemy1 image/Death_003.png"),
          pygame.image.load("enemy1 image/Death_004.png"),
          pygame.image.load("enemy1 image/Death_005.png"),
          pygame.image.load("enemy1 image/Death_006.png"),
          pygame.image.load("enemy1 image/Death_007.png"),
          pygame.image.load("enemy1 image/Death_008.png")]

resized_dying1 = []
for i in range(len(dying1)):
    resized_dying1.append(pygame.transform.scale(dying1[i], (120, 120)))

dying2 = [pygame.image.load("enemy2 image/Death_001.png"),
          pygame.image.load("enemy2 image/Death_002.png"),
          pygame.image.load("enemy2 image/Death_003.png"),
          pygame.image.load("enemy2 image/Death_004.png"),
          pygame.image.load("enemy2 image/Death_005.png"),
          pygame.image.load("enemy2 image/Death_006.png"),
          pygame.image.load("enemy2 image/Death_007.png"),
          pygame.image.load("enemy2 image/Death_008.png")]

resized_dying2 = []
for i in range(len(dying2)):
    resized_dying2.append(pygame.transform.scale(dying2[i], (120, 120)))

# enemy bullet
bullet = pygame.image.load("enemy_bullet.png")
resized_bullet = pygame.transform.scale(bullet, (50, 50))

# End screen background
end_screen_bg = pygame.image.load("end screen.jpg")
resized_end_screen_bg = pygame.transform.scale(end_screen_bg, (1200, 720))

# Controls
arrow_keys = pygame.image.load("arrow keys.jpg")
resized_arrow_keys = pygame.transform.scale(arrow_keys, (100, 80))
space_bar = pygame.image.load("spacebar.png")
resized_space_bar = pygame.transform.scale(space_bar, (150, 50))
P_key = pygame.image.load("P_key.png")
resized_P_key = pygame.transform.scale(P_key, (70, 70))
# End of IMAGES

# Sound effects
# player
fireball_shot = mixer.Sound("sound effects/fireball.wav")
player_hurt = mixer.Sound("sound effects/bullet-impact.wav")

# enemy
robot_collapse = mixer.Sound("sound effects/robot-collapse.wav")
robot_shot = mixer.Sound("sound effects/fired.wav")
explosion_sound = mixer.Sound("sound effects/explosion.wav")

# mechanisms
impact = mixer.Sound("sound effects/impact.wav")
button_click = mixer.Sound("sound effects/button.wav")
game_over = mixer.Sound("sound effects/game-over.wav")
