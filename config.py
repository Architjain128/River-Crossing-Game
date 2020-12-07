#!/usr/bin/python
# -*- coding: utf-8 -*-
# constants

import pygame
pygame.init()

font = pygame.font.SysFont('monospace', 25, True)
title = pygame.font.SysFont('monospace', 90, True)

screen = pygame.display.set_mode((1000, 930))

# ===================================================================================================================================

icon = pygame.image.load('river.png')
l = pygame.transform.scale(pygame.image.load('lan.png'), (1000, 80))
bg = pygame.transform.scale(pygame.image.load('back.jpg'), (1000, 1000))
walkright = [pygame.transform.scale(pygame.image.load('r1.png'), (25,
             40)), pygame.transform.scale(pygame.image.load('r2.png'),
             (25, 40)),
             pygame.transform.scale(pygame.image.load('r3.png'), (25,
             40)), pygame.transform.scale(pygame.image.load('r4.png'),
             (25, 40))]
walkleft = [pygame.transform.scale(pygame.image.load('l1.png'), (25,
            40)), pygame.transform.scale(pygame.image.load('l2.png'),
            (25, 40)), pygame.transform.scale(pygame.image.load('l3.png'
            ), (25, 40)),
            pygame.transform.scale(pygame.image.load('l4.png'), (25,
            40))]
walkdown = [pygame.transform.scale(pygame.image.load('do1.png'), (25,
            40)), pygame.transform.scale(pygame.image.load('do2.png'),
            (25, 40)),
            pygame.transform.scale(pygame.image.load('do3.png'), (25,
            40)), pygame.transform.scale(pygame.image.load('do4.png'),
            (25, 40))]
walkup = [pygame.transform.scale(pygame.image.load('u1.png'), (25,
          40)), pygame.transform.scale(pygame.image.load('u2.png'),
          (25, 40)), pygame.transform.scale(pygame.image.load('u3.png'
          ), (25, 40)),
          pygame.transform.scale(pygame.image.load('u4.png'), (25, 40))]
char = [pygame.transform.scale(pygame.image.load('u4.png'), (25, 40)),
        pygame.transform.scale(pygame.image.load('do4.png'), (25, 40))]
blo = [pygame.transform.scale(pygame.image.load('thrones.png'), (100,
       20)), pygame.transform.scale(pygame.image.load('thronesd.png'),
       (100, 20))]
mo = pygame.transform.scale(pygame.image.load('shark.png'), (50, 50))
mov = [mo, pygame.transform.flip(mo, 180, 00)]
pearl = pygame.transform.scale(pygame.image.load('pearl1.png'), (20,
                               20))
win = pygame.transform.scale(pygame.image.load('win.png'), (500, 500))

# ===================================================================================================================================

pygame.display.set_icon(icon)
pygame.display.set_caption("ARCHIT's GAME")

# ===================================================================================================================================

clock = pygame.time.Clock()
milliseconds = 00
seconds = 00
milliseconds2 = 00
seconds2 = 00
w = 1
level = 1.2
level1 = 0.8
level2 = 0.8

levelcounter = 1
levelcounter1 = 1
levelcounter2 = 1

start = True
start2 = True

score0 = 00
score1 = 00
