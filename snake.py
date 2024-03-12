#!/bin/python3

import math
import random
import time
import pygame
from pygame.locals import(
    RLEACCEL,
    KEYDOWN,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_q,
)

size = 75
frame = 0
eat_frame = 0
speed = 15
score = 0

class Snake(pygame.sprite.Sprite):
    sprt1 = "sprite/pacsnake_tete.png"
    sprt2 = "sprite/pacsnake_tete2.png"
    sprt3 = "sprite/pacsnake_tete3.png"
    sprt4 = "sprite/pacsnake_tete4.png"
    sprt5 = "sprite/pacsnake_tete5.png"
    sprt6 = "sprite/pacsnake_tete6.png"
    sprt7 = "sprite/pacsnake_tete7.png"
    sprt8 = "sprite/pacsnake_tete8.png"

    def __init__(self, sprt = sprt1):
        super(Snake, self).__init__()
        x, y = (w-size)//2, (h-size)//2
        self.sprt = pygame.image.load(sprt).convert()
        self.sprt.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.sprt.get_rect()
        self.rect.move_ip(x, y)
        self.pos = (x, y)
        self.rot = 0
        self.angl = 0
        self.dir = (1, 0)

    def set_rot(self, keys):
        if keys[K_UP]:
            self.rot = 90
        elif keys[K_DOWN]:
            self.rot = -90
        elif keys[K_RIGHT]:
            self.rot = 0
        elif keys[K_LEFT]:
            self.rot = 180

    def turn(self):
        rot = self.rot - self.angl
        if rot == 0 or rot == 180 or rot == -180:
            return
        self.sprt = pygame.transform.rotate(self.sprt, rot)
        self.angl = self.rot
        self.dir = get_dir(self.angl)
        self.rect = self.sprt.get_rect()
        self.rect.move_ip(self.pos)

    def move(self):
        if frame == 0 and self.rot != self.angl:
            self.turn()
        x, y = self.pos
        dx, dy = get_dir(self.angl)
        dx *= speed
        dy *= speed
        self.pos = (x+dx, y+dy)
        self.rect.move_ip(dx, dy)

    def eat(self):
        global eat_frame
        new_sprt = ""
        delta = 3
        if (eat_frame == 0):
            new_sprt = Snake.sprt2
        elif (eat_frame == 1 and frame == delta % (size//speed)):
            new_sprt = Snake.sprt3
        elif (eat_frame == 2 and frame == (2*delta) % (size//speed)):
            new_sprt = Snake.sprt2
        elif (eat_frame == 3 and frame == (3*delta) % (size//speed)):
            new_sprt = Snake.sprt1
        if (new_sprt == ""):
            return
        self.sprt = pygame.image.load(new_sprt).convert()
        self.sprt = pygame.transform.rotate(self.sprt, self.angl)
        eat_frame = (eat_frame+1)%4

    def check_lose(self, body):
        width, height = scr_size
        left, top = self.pos
        right = self.rect.right
        bottom = self.rect.bottom
        check = left <= 0 or top <= 0 or right >= width or bottom >= height or pygame.sprite.spritecollideany(self, body)
        return check

    def lose(self, sound):
        screen.fill((0, 0, 0))
        sound.play()

        self.sprt = pygame.image.load(Snake.sprt1).convert()
        self.sprt = pygame.transform.rotate(self.sprt, self.angl)
        screen.blit(self.sprt, self.pos)
        pygame.display.flip()
        time.sleep(0.15)

        self.sprt = pygame.image.load(Snake.sprt2).convert()
        self.sprt = pygame.transform.rotate(self.sprt, self.angl)
        screen.blit(self.sprt, self.pos)
        pygame.display.flip()
        time.sleep(0.15)

        self.sprt = pygame.image.load(Snake.sprt3).convert()
        self.sprt = pygame.transform.rotate(self.sprt, self.angl)
        screen.blit(self.sprt, self.pos)
        pygame.display.flip()
        time.sleep(0.15)

        self.sprt = pygame.image.load(Snake.sprt4).convert()
        self.sprt = pygame.transform.rotate(self.sprt, self.angl)
        screen.blit(self.sprt, self.pos)
        pygame.display.flip()
        time.sleep(0.15)

        self.sprt = pygame.image.load(Snake.sprt5).convert()
        self.sprt = pygame.transform.rotate(self.sprt, self.angl)
        screen.blit(self.sprt, self.pos)
        pygame.display.flip()
        time.sleep(0.15)

        self.sprt = pygame.image.load(Snake.sprt6).convert()
        self.sprt = pygame.transform.rotate(self.sprt, self.angl)
        screen.blit(self.sprt, self.pos)
        pygame.display.flip()
        time.sleep(0.15)

        self.sprt = pygame.image.load(Snake.sprt7).convert()
        self.sprt = pygame.transform.rotate(self.sprt, self.angl)
        screen.blit(self.sprt, self.pos)
        pygame.display.flip()
        time.sleep(0.15)

        self.sprt = pygame.image.load(Snake.sprt8).convert()
        self.sprt = pygame.transform.rotate(self.sprt, self.angl)
        screen.blit(self.sprt, self.pos)
        pygame.display.flip()
        time.sleep(0.15)

        self.kill()
        screen.fill((0, 0, 0))
        pygame.display.flip()
        time.sleep(0.75)

class Snake_body(Snake):
    sprt1 = "sprite/fantome_rouge.png"
    sprt2 = "sprite/fantome_orange.png"
    sprt3 = "sprite/fantome_rose.png"
    sprt4 = "sprite/fantome_cyan.png"
    sprt = (sprt1, sprt2, sprt3, sprt4)
    def __init__(self, bp):
        r = random.randint(0, 3)
        sprt = Snake_body.sprt[r]
        super().__init__(sprt)
        self.prevbp = bp
        x, y = self.prevbp.pos
        self.angl = self.prevbp.angl
        self.rot = self.prevbp.rot
        self.dir = (0, 0)
        self.next_dir = get_dir(self.rot)
        dx, dy = get_dir(self.angl)
        self.rect.move_ip(-self.pos[0], -self.pos[1])
        self.pos = (x - speed*dx, y - speed*dy)
        self.rect.move_ip(self.pos)

    def move(self):
        x, y = self.pos
        dx, dy = self.dir
        dx *= speed
        dy *= speed
        x += dx
        y += dy
        self.pos = (x, y)
        self.rect.move_ip(dx, dy)
        px, py = self.prevbp.pos
        if self.next_dir != self.dir:
            ndx, ndy = self.next_dir
            ndx *= size
            ndy *= size
            if x + ndx == px and y + ndy == py:
                self.angl = self.rot
                self.dir = get_dir(self.angl)
        if self.rot != self.prevbp.angl:
            self.rot = self.prevbp.angl
            self.next_dir = get_dir(self.rot)
        

class Gum(pygame.sprite.Sprite):
    gum_size = 35
    offset = 2*size

    def __init__(self, snake_pos):
        super(Gum, self).__init__()
        self.sprt = pygame.Surface((size, size))
        pygame.draw.circle(self.sprt, (250, 250, 250), (size//2, size//2), Gum.gum_size/2)
        self.sprt.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.sprt.get_rect()
        x = random.randint(Gum.offset, w - Gum.offset - size)
        y = random.randint(Gum.offset, h - Gum.offset - size)
        while abs(x-snake_pos[0]) <= 3*size and abs(y-snake_pos[1]) <= 3*size:
            x = random.randint(Gum.offset, w - Gum.offset - size)
            y = random.randint(Gum.offset, h - Gum.offset - size)
        x += -(x%size) + size//2 + scr_offset[0]
        y += -(y%size) + size//2 + scr_offset[1]
        self.pos = (x, y)
        self.rect.move_ip(self.pos)

def get_dir(angl):
    rad = math.radians(angl)
    cos = round(math.cos(rad))
    sin = round(math.sin(-rad))
    return (cos, sin)

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
scr_size = screen.get_size()
w, h = scr_size
scr_offset = (w//2)%size, (h//2)%size
timer = pygame.time.Clock()

def game():
    global frame
    global speed
    global score
    snake = Snake()
    lst_bp = snake
    snake_body = pygame.sprite.Group()
    snake_body_hitbox = pygame.sprite.Group()
    gum = Gum(snake.pos)
    font = pygame.font.SysFont(None, 64)
    text_quit = font.render("Q or escape to quit", True, (100, 100, 100))
    text_rect = text_quit.get_rect()
    score_text = font.render("score: %d" % score, True, (100, 100, 100))
    eat_sound = pygame.mixer.Sound("sound/eat_sound.ogg")
    death_sound = pygame.mixer.Sound("sound/death_sound.ogg")

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    return
                snake.set_rot(pygame.key.get_pressed())
        snake.move()
        screen.blit(text_quit, ((w-text_rect.right)//2, (h-text_rect.bottom)//2))
        screen.blit(score_text, (0, 0))
        screen.blit(gum.sprt, gum.pos)
        screen.blit(snake.sprt, snake.pos)
        for body_part in snake_body:
            body_part.move()
            screen.blit(body_part.sprt, body_part.pos)
        if (eat_frame != 0):
            snake.eat()
        if snake.rect.colliderect(gum.rect):
            snake.eat()
            eat_sound.stop()
            eat_sound.play()
            score += 1
            score_text = font.render("score: %d" % score, True, (100, 100, 100))
            gum.kill()
            lst_bp = Snake_body(lst_bp)
            snake_body.add(lst_bp)
            if lst_bp.prevbp != snake:
                snake_body_hitbox.add(lst_bp)
            gum = Gum(snake.pos)
        pygame.display.flip()
        if snake.check_lose(snake_body_hitbox):
            for body_part in snake_body:
                body_part.kill()
            speed = 0
            snake.lose(death_sound)
            return
        timer.tick(30)
        frame = (frame + 1) % (size//speed)

game()
print("score:", score)
pygame.quit()