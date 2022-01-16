import pygame
import random

pygame.init()


# Player
class Player:
    def __init__(self):
        self.x = 10
        self.y = 350
        self.xVelocity = 0
        self.yVelocity = 0
        self.left = False
        self.right = False
        self.attack = False
        self.steps = 0
        self.dying_steps = 0
        self.health = 20
        self.alive = True
        self.dead = False

    def draw(self, screen, imageStanding, imageLeft, imageRight, imageAttack, imageDeath):
        if self.alive:
            if self.steps + 1 >= 15:
                self.steps = 0

            if self.left:
                screen.blit(imageLeft[self.steps // 3], (self.x, self.y))
                self.steps += 1
            elif self.right:
                screen.blit(imageRight[self.steps // 3], (self.x, self.y))
                self.steps += 1
            elif self.attack:
                screen.blit(imageAttack, (self.x, self.y))

            else:
                screen.blit(imageStanding[self.steps // 3], (self.x, self.y))
                self.steps += 1
        else:
            if not self.dead:
                self.dying_steps += 1
            if self.dying_steps < 15:
                screen.blit(imageDeath[self.dying_steps // 3], (self.x, self.y))
            if self.dying_steps >= 15:
                self.dying_steps += 0
                self.dead = True

        # health boxes
        pygame.draw.rect(screen, (255, 0, 0), (15, 50, 120, 20))
        pygame.draw.rect(screen, (0, 0, 255), (15, 50, 120 - (6 * (20 - self.health)), 20))

    def hit(self):
        if self.health > 1:
            self.health -= 1
        elif self.health == 1:
            self.health -= 1
            self.alive = False


class Fireball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 8
        self.fired = False

    def draw(self, screen, imageFireball):
        self.x += self.velocity
        if self.fired:
            screen.blit(imageFireball, (self.x, self.y))
        if 1100 <= self.x:
            self.fired = False


class Enemy:
    def __init__(self):
        self.x = random.randint(800, 1100)
        self.y = random.randint(220, 530)
        self.steps = 0
        self.velocity = random.randrange(-3, -1)
        self.attack = False
        self.health = 5
        self.alive = True
        self.dead = False

    def draw(self, screen, imageLeft, imageRight, imageAttack, deathImg):
        self.steps += 1
        if self.alive:
            self.move()
            if self.steps >= 48:
                self.steps = 0

            # initializing movements
            if self.attack:
                screen.blit(imageAttack, (self.x, self.y))
            else:
                if self.velocity > 0:
                    screen.blit(imageRight[self.steps // 4], (self.x, self.y))
                else:
                    screen.blit(imageLeft[self.steps // 4], (self.x, self.y))

            # health box
            pygame.draw.rect(screen, (255, 0, 0), (self.x + 18, self.y - 7, 50, 10))
            pygame.draw.rect(screen, (0, 255, 0),
                             (self.x + 18, self.y - 7, 50 - (10 * (5 - self.health)), 10))
        else:
            if self.steps < 48:
                screen.blit(deathImg[self.steps // 6], (self.x, self.y))
            if self.steps >= 48:
                self.dead = True

    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < 1100:
                self.x += + self.velocity
            else:
                self.velocity *= -1
        else:
            if self.x - self.velocity > 100:
                self.x += self.velocity
            else:
                self.velocity *= -1

    def hit(self):
        if self.health > 1:
            self.health -= 1
        elif self.health == 1:
            self.health -= 1
            self.alive = False


class EnemyLvl2(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.health = 10
        self.velocity = random.randrange(-6, -4)

    def draw(self, screen, imageLeft, imageRight, imageAttack, deathImg):
        self.steps += 1
        if self.alive:
            self.move()
            if self.steps >= 48:
                self.steps = 0

            # initializing movements
            if self.attack:
                screen.blit(imageAttack, (self.x, self.y))
            else:
                if self.velocity > 0:
                    screen.blit(imageRight[self.steps // 4], (self.x, self.y))
                else:
                    screen.blit(imageLeft[self.steps // 4], (self.x, self.y))

            # health boxes
            pygame.draw.rect(screen, (255, 0, 0), (self.x + 18, self.y - 7, 50, 10))
            pygame.draw.rect(screen, (0, 255, 0),
                             (self.x + 18, self.y - 7, 50 - (5 * (10 - self.health)), 10))
        if not self.alive:
            if self.steps < 48:
                screen.blit(deathImg[self.steps // 6], (self.x, self.y))
            if self.steps == 48:
                self.dead = True


class Bullet:
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.fired = False
        if velocity > 0:
            self.velocity = velocity * 0.4
        else:
            self.velocity = velocity * -0.4

    def draw(self, screen, bulletImg):
        self.x -= self.velocity
        if self.fired:
            screen.blit(bulletImg, (self.x, self.y))
        if self.x <= 10:
            self.fired = False
