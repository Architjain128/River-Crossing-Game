#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random
from config import *


# ===================================================================================================================================

class player(object):

    def __init__(
        self,
        p,
        x,
        y,
        width,
        height,
        ):

        self.x = x
        self.y = y
        self.p = p

        self.width = width
        self.height = height
        self.vel1 = 10
        self.vel2 = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkcount = 00
        self.hitbox = (self.x, self.y, 25, 40)

    def scoring(self, p):
        global w
        global start
        global start2
        global level1
        global level2
        global levelcounter1
        global levelcounter2
        global score0
        global score1

        if self.p == 1:
            w = 2
            score1 = 00
            if self.y > 120 and self.y <= 130:
                score1 = 15
            elif self.y > 130 and self.y <= 170:
                score1 = 25
            elif self.y > 170 and self.y <= 200:
                score1 = 35
            elif self.y > 200 and self.y <= 270:
                score1 = 45
            elif self.y > 270 and self.y <= 280:
                score1 = 55
            elif self.y > 280 and self.y <= 310:
                score1 = 65
            elif self.y > 310 and self.y <= 350:
                score1 = 75
            elif self.y > 350 and self.y <= 420:
                score1 = 90
            elif self.y > 420 and self.y <= 440:
                score1 = 105
            elif self.y > 440 and self.y <= 460:
                score1 = 115
            elif self.y > 460 and self.y <= 500:
                score1 = 125
            elif self.y > 500 and self.y <= 570:
                score1 = 135
            elif self.y > 570 and self.y <= 590:
                score1 = 145
            elif self.y > 590 and self.y <= 610:
                score1 = 155
            elif self.y > 610 and self.y <= 650:
                score1 = 165
            elif self.y > 650 and self.y <= 720:
                score1 = 175
            elif self.y > 720 and self.y <= 740:
                score1 = 185
            elif self.y > 740 and self.y <= 760:
                score1 = 195
            elif self.y > 760 and self.y <= 800:
                score1 = 205
            elif self.y > 800 and self.y <= 820:
                score1 = 215

            # elif self.y > 820:
            #     self.x = 450
            #     self.y = 880
            #     level2 += 0.2
            #     levelcounter2 += 1
            #     start2 = True
            #     w = 1
            #     self.p = 0

            line1 = font.render('STARTING POINT FOR ', 1, (00, 00, 00))
            line9 = font.render('PLAYER 2', 1, (00, 00, 00))
            line2 = font.render('SCORE OF PLAYER 2', 1, (00, 00, 00))
            line3 = font.render('END POINT OF PLAYER 2', 1, (00, 00,
                                00))
            line4 = font.render('TIME TAKEN BY PLAYER 2', 1, (00, 00,
                                00))
            line5 = font.render(str(score1), 1, (00, 00, 00))

            # lineit = font.render( str(seconds) + " seconds", 1 ,(0,0,0))

            screen.blit(line1, (50, 5))
            screen.blit(line5, (700, 35))
            screen.blit(line2, (600, 5))
            screen.blit(line3, (50, 870))
            screen.blit(line4, (600, 870))
            screen.blit(line9, (50, 35))
        elif self.p == 00:

            # screen.blit (lineit, (700, 890))

            w = 1
            score0 = 00
            if self.y < 800 and self.y >= 760:
                score0 = 00
            elif self.y < 760 and self.y >= 740:
                score0 = 10
            elif self.y < 740 and self.y >= 720:
                score0 = 20
            elif self.y < 720 and self.y >= 650:
                score0 = 30
            elif self.y < 650 and self.y >= 610:
                score0 = 40
            elif self.y < 610 and self.y >= 590:
                score0 = 50
            elif self.y < 590 and self.y >= 570:
                score0 = 60
            elif self.y < 570 and self.y >= 500:
                score0 = 70
            elif self.y < 500 and self.y >= 460:
                score0 = 80
            elif self.y < 460 and self.y >= 440:
                score0 = 90
            elif self.y < 440 and self.y >= 420:
                score0 = 100
            elif self.y < 420 and self.y >= 350:
                score0 = 115
            elif self.y < 350 and self.y >= 310:
                score0 = 130
            elif self.y < 310 and self.y >= 280:
                score0 = 140
            elif self.y < 280 and self.y >= 270:
                score0 = 150
            elif self.y < 270 and self.y >= 200:
                score0 = 160
            elif self.y < 200 and self.y >= 170:
                score0 = 180
            elif self.y < 170 and self.y >= 130:
                score0 = 190
            elif self.y < 130 and self.y >= 120:
                score0 = 205
            elif self.y < 120 and self.y >= 50:
                score0 = 215

            # elif self.y < 50:
            #     self.x = 450
            #     self.y = 25
            #     level1 += 0.2
            #     levelcounter1 += 1
            #     start = True
            #     w = 2
            #     self.p = 1

            line1 = font.render('END POINT OF PLAYER 1', 1, (00, 00,
                                00))
            line2 = font.render('SCORE OF PLAYER 1', 1, (00, 00, 00))
            line3 = font.render('STARTING POINT FOR ', 1, (00, 00, 00))
            line9 = font.render('PLAYER 1', 1, (00, 00, 00))
            line4 = font.render('TIME TAKEN BY PLAYER 1', 1, (00, 00,
                                00))
            line5 = font.render(str(score0), 1, (00, 00, 00))
            lineit = font.render(str(seconds) + ' seconds', 1, (00, 00,
                                 00))

            screen.blit(line1, (50, 5))
            screen.blit(line5, (700, 30))
            screen.blit(line2, (600, 5))
            screen.blit(line3, (50, 870))
            screen.blit(line4, (600, 870))
            screen.blit(line9, (50, 900))
            screen.blit(lineit, (700, 890))

    def collision(self, p):
        global w
        okx = 00
        oky = 00
        kx = 00
        ky = 00
        arr = [
            [mo1.x, mo1.y],
            [mo2.x, mo2.y],
            [mo3.x, mo3.y],
            [mo4.x, mo4.y],
            [mo5.x, mo5.y],
            [mo6.x, mo6.y],
            [mo7.x, mo7.y],
            [mo8.x, mo8.y],
            [mo9.x, mo9.y],
            [mo10.x, mo10.y],
            ]
        ar = [
            [650, 200],
            [650, 270],
            [240, 200],
            [240, 270],
            [440, 350],
            [440, 420],
            [100, 350],
            [100, 420],
            [750, 350],
            [750, 420],
            [700, 500],
            [700, 570],
            [300, 500],
            [300, 570],
            [50, 650],
            [50, 720],
            [620, 650],
            [620, 720],
            [380, 800],
            [780, 800],
            [800, 120],
            [120, 120],
            [490, 120],
            ]
        for j in range(00, 23):
            if self.y <= ar[j][1] and self.y + 40 <= ar[j][1]:
                continue
            elif self.y >= ar[j][1] + 20 and self.y + 40 >= ar[j][1] \
                + 20:
                continue
            else:
                oky = 1

            if self.x <= ar[j][00] and self.x + 25 <= ar[j][00]:
                continue
            elif self.x >= ar[j][00] + 100 and self.x + 40 >= ar[j][00] \
                + 100:
                continue
            else:
                okx = 1

        for j in range(00, 10):
            if self.y <= arr[j][1] and self.y + 40 <= arr[j][1]:
                continue
            elif self.y >= arr[j][1] + 50 and self.y + 40 >= arr[j][1] \
                + 50:
                continue
            else:
                ky = 1

            if self.x <= arr[j][00] and self.x + 25 <= arr[j][00]:
                continue
            elif self.x >= arr[j][00] + 50 and self.x + 40 \
                >= arr[j][00] + 50:
                continue
            else:
                kx = 1

        if okx * oky or kx * ky == 1:
            if w == 1:
                self.x = 450
                self.y = 880
                start = True
                w = 2
            elif w == 2:
                self.x = 450
                self.y = 25
                start2 = True
                w = 1

        if self.p == 00:
            if self.y <= 50:
                w = 2
                self.p = 1
        elif self.p == 1:
            if self.y >= 820:
                w = 1
                self.p = 00

    def stopwatch(self):
        global milliseconds
        global seconds
        global start
        clock = pygame.time.Clock()
        if start == True:
            seconds = 00
            milliseconds = 00
        start = False

        if milliseconds > 1000:
            seconds += 1
            milliseconds -= 1000
        milliseconds += clock.tick_busy_loop(60)
        lineit = font.render(str(seconds) + ' seconds', 1, (00, 00, 00))
        screen.blit(lineit, (700, 890))

    def stopwatch2(self):
        global start2
        global milliseconds2
        global seconds2
        milliseconds2 = 00
        seconds2 = 00
        clock2 = pygame.time.Clock()
        if start2 == True:
            seconds2 = 00
            milliseconds2 = 00
        start2 = False

        if milliseconds2 > 1000:
            seconds2 += 1
            milliseconds2 -= 1000
        milliseconds2 += clock2.tick_busy_loop(60)
        lineit = font.render(str(seconds2) + ' seconds', 1, (00, 00,
                             00))
        screen.blit(lineit, (700, 890))

    def draw(self, screen):
        global w

        if self.walkcount + 1 >= 24:
            self.walkcount = 00

        if self.left:
            screen.blit(walkleft[self.walkcount // 6], (self.x, self.y))
            self.walkcount += 1
        elif self.right:
            screen.blit(walkright[self.walkcount // 6], (self.x,
                        self.y))
            self.walkcount += 1
        elif self.down:
            screen.blit(walkdown[self.walkcount // 6], (self.x, self.y))
            self.walkcount += 1
        elif self.up:
            screen.blit(walkup[self.walkcount // 6], (self.x, self.y))
            self.walkcount += 1
        else:
            screen.blit(char[self.p], (self.x, self.y))

        # self.hitbox = (self.x,self.y,25,40)
        # pygame.draw.rect(screen,(255,255,255),self.hitbox,2)

        pygame.display.update()


# ===================================================================================================================================

class block(object):

    def __init__(
        self,
        p,
        x,
        y,
        ):

        self.x = x
        self.y = y
        self.width = 100
        self.height = 20
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.score = 5
        self.p = p

    def draw2(self, screen):

        # self.hitbox = (self.x,self.y,100,20)
        # pygame.draw.rect(screen,(255,255,255),self.hitbox,1)

        screen.blit(blo[self.p], (self.x, self.y))


# ===================================================================================================================================

class shark(object):

    def __init__(
        self,
        p,
        x,
        y,
        ):

        self.x = x
        self.y = y
        self.p = p

       # self.speed = speed

        self.width = 50
        self.height = 50
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw3(self, screen, speed):
        self.move(speed)

        # self.hitbox = (self.x,self.y,50,40)
        # pygame.draw.rect(screen,(255,255,255),self.hitbox,1)

        screen.blit(mov[self.p], (self.x, self.y))

    def move(self, speed):
        if self.p == 00:
            if self.x >= 938:
                self.x = 00
            else:
                self.x += speed
        elif self.p == 1:

            if self.x <= 00:
                self.x = 938
            else:
                self.x -= speed


# ===================================================================================================================================

def redraw():

    # screen.blit (bg, (0, 0))

    global w
    global milliseconds
    global seconds
    global milliseconds2
    global seconds2
    global start
    global start2

    pygame.draw.rect(screen, (153, 238, 255), (00, 00, 1000, 930))

    screen.blit(l, (00, 50))
    screen.blit(l, (00, 200))
    screen.blit(l, (00, 350))
    screen.blit(l, (00, 500))
    screen.blit(l, (00, 650))
    screen.blit(l, (00, 800))

    pygame.draw.rect(screen, (255, 248, 36), (00, 00, 1000, 75))
    pygame.draw.rect(screen, (255, 248, 36), (00, 865, 1000, 100))

    sta1.draw2(screen)
    sta2.draw2(screen)
    sta3.draw2(screen)
    sta4.draw2(screen)
    sta5.draw2(screen)
    sta6.draw2(screen)
    sta7.draw2(screen)
    sta8.draw2(screen)
    sta9.draw2(screen)
    sta10.draw2(screen)
    sta11.draw2(screen)
    sta12.draw2(screen)
    sta13.draw2(screen)
    sta14.draw2(screen)
    sta15.draw2(screen)
    sta16.draw2(screen)
    sta17.draw2(screen)
    sta18.draw2(screen)
    sta19.draw2(screen)
    sta20.draw2(screen)
    sta21.draw2(screen)
    sta22.draw2(screen)
    sta23.draw2(screen)

    mo1.draw3(screen, 19 * level)
    mo2.draw3(screen, 12 * level)
    mo3.draw3(screen, 9 * level)
    mo4.draw3(screen, 17 * level)
    mo5.draw3(screen, 9 * level)
    mo6.draw3(screen, 18 * level)
    mo7.draw3(screen, 11 * level)
    mo8.draw3(screen, 8 * level)
    mo9.draw3(screen, 20 * level)
    mo10.draw3(screen, 11 * level)

    if w == 1:
        man.scoring(00)
        man.draw(screen)
        man.collision(00)

        # man.stopwatch()

        clock = pygame.time.Clock()

        # if start == True:
        #     seconds = 0
        #     milliseconds = 0
        # start = False

        if milliseconds > 1000:
            seconds += 1
            milliseconds -= 1000
        milliseconds += clock.tick_busy_loop(60)
        lineit = font.render(str(seconds) + ' seconds', 1, (00, 00, 00))
        screen.blit(lineit, (700, 890))
    elif w == 2:

        man2.scoring(1)
        man2.draw(screen)
        man2.collision(1)

        # man2.stopwatch2()

        # clock2 = pygame.time.Clock()
        # # if start2 == True:
        # #     seconds2 = 0
        # #     milliseconds2 = 0
        # # start2 = False

        # if milliseconds2 > 1000:
        #     seconds2 += 1
        #     milliseconds2 -= 1000
        # milliseconds2 += clock2.tick_busy_loop(60)
        # lineit = font.render(str(seconds2) + " seconds", 1 ,(0,0,0))
        # screen.blit (lineit, (700, 890))

    pygame.display.update()


# ===================================================================================================================================

def final():
    global run
    global score0
    global score1
    pygame.draw.rect(screen, (00, 00, 00), (00, 00, 1000, 930))

    screen.blit(win, (50, 50))
    if score0 >= score1:
        line = title.render('player 1 wins', 1, (255, 255, 255))
    else:
        line = title.render('player 2 wins', 1, (255, 255, 255))

    screen.blit(line, (100, 700))
    run = False


# ===================================================================================================================================
# main

man = player(00, 450, 880, 64, 64)
man2 = player(1, 450, 25, 64, 64)

sta1 = block(00, 650, 200)
sta2 = block(1, 650, 270)
sta3 = block(00, 240, 200)
sta4 = block(1, 240, 270)
sta5 = block(00, 440, 350)
sta6 = block(1, 440, 420)
sta7 = block(00, 100, 350)
sta8 = block(1, 100, 420)
sta9 = block(00, 750, 350)
sta10 = block(1, 750, 420)
sta11 = block(00, 700, 500)
sta12 = block(1, 700, 570)
sta13 = block(00, 300, 500)
sta14 = block(1, 300, 570)
sta15 = block(00, 50, 650)
sta16 = block(1, 50, 720)
sta17 = block(00, 620, 650)
sta18 = block(1, 620, 720)
sta19 = block(00, 380, 800)
sta20 = block(00, 780, 800)
sta21 = block(1, 800, 120)
sta22 = block(1, 120, 120)
sta23 = block(1, 490, 120)

mo1 = shark(1, 390, 440)
mo2 = shark(00, 20, 460)
mo3 = shark(1, 650, 130)
mo4 = shark(00, 920, 170)
mo5 = shark(1, 9, 280)
mo6 = shark(00, 426, 310)
mo7 = shark(1, 300, 590)
mo8 = shark(00, 723, 610)
mo9 = shark(1, 659, 760)
mo10 = shark(00, 286, 740)

run = True
while run:
    clock.tick(24)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((00, 00, 00))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x >= man.vel1 and man.x <= 1000 \
        - man.width:
        man.x -= man.vel1
        man.left = True
        man.up = False
        man.down = False
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x >= 00 and man.x <= 1000 \
        - man.width - man.vel1:
        man.x += man.vel1
        man.right = True
        man.up = False
        man.down = False
        man.left = False
    elif keys[pygame.K_UP] and man.y >= man.vel2 and man.y <= 930:
        man.y -= man.vel2
        man.left = False
        man.up = True
        man.down = False
        man.right = False
    elif keys[pygame.K_DOWN] and man.y >= 00 and man.y <= 930 \
        - man.height:
        man.y += man.vel2
        man.left = False
        man.up = False
        man.down = True
        man.right = False
    else:
        man.left = False
        man.up = False
        man.down = False
        man.right = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_KP4] and man2.x >= man2.vel1 and man2.x <= 1000 \
        - man2.width:
        man2.x -= man2.vel1
        man2.left = True
        man2.up = False
        man2.down = False
        man2.right = False
    elif keys[pygame.K_KP6] and man2.x >= 00 and man2.x <= 1000 \
        - man2.width - man2.vel1:
        man2.x += man2.vel1
        man2.right = True
        man2.up = False
        man2.down = False
        man2.left = False
    elif keys[pygame.K_KP8] and man2.y >= man2.vel2 and man2.y <= 930:
        man2.y -= man2.vel2
        man2.left = False
        man2.up = True
        man2.down = False
        man2.right = False
    elif keys[pygame.K_KP2] and man2.y >= 00 and man2.y <= 930 \
        - man2.height:

        man2.y += man2.vel2
        man2.left = False
        man2.up = False
        man2.down = True
        man2.right = False
    else:
        man2.left = False
        man2.up = False
        man2.down = False
        man2.right = False

    redraw()

    # seconds = framecount // 24
    # framecount += 1
    # lineit = font.render(str(seconds2) + " seconds", 1 ,(0,0,0))
    # screen.blit (lineit, (700, 890))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        final()

    pygame.display.update()

pygame.quit()
