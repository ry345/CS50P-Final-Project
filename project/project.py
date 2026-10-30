#
# This is my CS50 project
# this is my platformer game
# you use space bar to let player jump and try to avoid the spikes
# enjoy


# stats
import pygame
import random
import csv
from pygame.locals import *
from pygame.mixer import *
import math
from time import sleep

YELLOW = (255, 255, 0)
LIGHT_GRAY = (191, 191, 191)
WIDTH = 1400

HEIGHT = 750

gfjhrhrht = 0
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AVOID THE SPIKES")
player_img = pygame.image.load("happy.png")
player_img = pygame.transform.scale(player_img, (70, 70))
spike_img = pygame.image.load("spike.png")
spike_img = pygame.transform.scale(spike_img, (20, 20))
barrier_img = pygame.image.load("barrier.png")
background = pygame.image.load("6.png")
background_width = background.get_width()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
ground = pygame.image.load("ground.png")
gameover = pygame.image.load("gameover.png")
gameover = pygame.transform.scale(gameover, (300, 300))
ground_width = ground.get_width()
ground_height = ground.get_height()
clock = pygame.time.Clock()
barrier_rect = barrier_img.get_rect()
spike_rect = spike_img.get_rect()
player_rect = player_img.get_rect()
playercounter = 0
font = pygame.font.Font(None, 100)
scroll = 0
groundscroll = 0
players = pygame.sprite.Group()
jump_sound = pygame.mixer.Sound("shoot.wav")
panels = math.ceil(WIDTH / background_width) + 2
spikes = pygame.sprite.Group()
barriers = pygame.sprite.Group()
intro_font = pygame.font.Font(None, 25)


class Spike(pygame.sprite.Sprite):

    def __init__(self, image, a, b):
        super().__init__()
        self.image = image
        self.image_rect = self.image.get_rect()
        self.a = WIDTH - self.image.get_width()
        self.b = (HEIGHT // 2) + 150
        self.alive = True
        self.BASE = 5
        self.add = 2
        self.gfjhrhrht = 0
        self.aaaaa = a
        self.bbbbb = b

    def update(self, player):

        self.image_rect.topleft = (self.a, self.b)
        keys = pygame.key.get_pressed()
        if self.image_rect.colliderect(player.image_rect):
            self.alive = False
        if self.alive == False:
            self.kill()

        if self.alive:
            self.image_rect.topleft = (self.a, self.b)

            self.a -= self.BASE
            self.gfjhrhrht += 1
            if self.gfjhrhrht % 100 == 0:
                # add spike speed
                self.BASE += self.add

            screen.blit(self.image, (self.a, self.b))
            if self.a < 230:
                self.a = WIDTH - self.image.get_width()

    def parallax_scrolling_background(self):
        # will increase in speed according to spike speed
        global scroll, groundscroll
        for i in range(panels):
            screen.blit(
                background, (i * background_width + scroll - background_width, 0)
            )
            screen.blit(
                ground, (i * ground_width + scroll - ground_width, 750 - ground_height)
            )
        if self.gfjhrhrht % 50 == 0:
            self.aaaaa += 1
            self.bbbbb += 1
        scroll -= self.aaaaa
        groundscroll -= self.bbbbb
        if abs(scroll) > background_width:
            scroll = 0
        if abs(groundscroll) > ground_width:
            groundscroll = 0


# player class
class Player(pygame.sprite.Sprite):
    score = 0

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.image_rect = self.image.get_rect()
        self.A = (WIDTH // 2) - 300
        self.B = (HEIGHT // 2) + 140
        self.alive = True
        self.jump = False
        self.jump_height = 50
        self.velocity = self.jump_height
        self.gravity = 5

    def update(self, spike, jump_sound):
        # die if collide
        global players
        self.image_rect.topleft = (self.A, self.B)
        if self.image_rect.colliderect(spike.image_rect):
            self.alive = False

            self.kill()
            die()

        if self.alive:

            screen.blit(self.image, (self.A, self.B))
            keys = pygame.key.get_pressed()
            # press space/up/w to jump
            if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
                self.jump = True

            if self.jump:

                self.B -= self.velocity
                self.velocity -= self.gravity
                if self.velocity < -self.jump_height:
                    self.jump = False
                    self.velocity = self.jump_height
                    jump_sound.play()

            Player.score += 1


def main(running=True):
    # main loop
    global playercounter, game_active, players, spikes
    a = int(randomness(2, 5, 2, 4))
    b = int(a * (3 / 10))

    player = Player(player_img)
    spike = Spike(spike_img, a, b)

    players.add(player)
    spikes.add(spike)
    # draw message
    message1 = intro_font.render(intro_part_1(), True, (0, 255, 0))
    screen.blit(message1, (0, 0))
    message2 = intro_font.render(intro_part_2(), True, (0, 255, 0))
    screen.blit(message2, (0, 30))

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        # update spike,
        # background,
        # ground,
        # player.
        spike.parallax_scrolling_background()

        player.update(spike, jump_sound)
        spike.update(player)

        pygame.display.flip()

    pygame.quit()


def die():
    # draws gameover image
    # draws score

    global game_active
    msg = font.render(f"score: {Player.score}", True, (255, 255, 255))
    screen.blit(msg, (500, 75))
    screen.blit(gameover, (500, 175))


def intro_part_1():
    # part 1
    # one line couldn't fit on the screen
    return "HOW TO PLAY: the small black object at the bottom is the spike, and you need to jump(w/space/up arrow) to avoid it."


def intro_part_2():
    # part 2
    return "The small smiley at the bottom is the player which you will be controlling. hope you enjoy my game.good luck!"


def fibonacci(n):
    # F(n) = F(n-1) + F(n-2)
    # i coded it as a challenge
    if n == 0:
        return 0
    if n == 1:

        return 1
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def biggest_value(arr):
    # the array must have something in it and not be empty
    # find biggest value
    if len(arr) == 0:
        raise ValueError("array is empty")
    largest_value = arr[0]
    for i in arr:
        if i > largest_value:
            largest_value = i
    return largest_value


def pythagoras(a, b):
    # pythagorean theorem: a² + b² = c² for a right angled triangle
    return math.sqrt((a * a + b * b))


def randomness(small, big, x, y):
    # generate random background scroll value
    lst = [random.randint(small, big) for _ in range(3)]
    lst2 = [random.randint(x, y) for _ in range(3)]
    mun = biggest_value(lst)
    num = biggest_value(lst2)
    # this is very very random
    # this was created as i wanted to find a use for pythagoras and fibonacci.
    return int(pythagoras(fibonacci(mun), fibonacci(num)) // 2)


if __name__ == "__main__":

    main()
