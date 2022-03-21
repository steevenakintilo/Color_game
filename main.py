#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## a
## File description:
## a
##

import pygame
from random import randint
import sys
from os import system
import pygame.freetype 

def write_id(path,x):  
    f = open(path, "w")
    f.write(str(x))    
    f.close            

def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()

def list_to_str(l):
    s = ""
    for i in range(len(l)):
        s = s + l[i]
    return (s)

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1280

def menu_loop():
    system("clear")
    pygame.init()
    pygame.mixer.init()
    GAME_FONT1 = pygame.freetype.Font("font.ttf", 75)
    GAME_FONT2 = pygame.freetype.Font("font.ttf", 200)
    all_collor = ["purple","blue","green","yellow","pink","brown","white","grey","black","orange"]
    purple = (191,64,191)
    blue =  (0,0,255)
    green = (0,128,0)
    yellow = (255,255,0)
    pink = (255,192,203)
    brown = (165,42,42)
    white = (255,255,255)
    grey = (204,209,209)
    black = (0,0,0)
    orange = (255,165,0)
    color_list = [purple,blue,green,yellow,pink,brown,white,grey,black,orange]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    rdm_num_one = randint(0,len(all_collor) - 1)
    rdm_num_two = randint(0,len(all_collor) - 1)
    rdm_num_one = randint(0,len(all_collor) - 1)
    clock = pygame.time.Clock()
    running = True
    color = (217,225,229)
    name = []
    l = []
    d = 430
    pos = []
    start = 0
    while running:
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    if event.type == pygame.QUIT:
                       quit()
            if pressed_keys[ord('x')]:
                quit()
            if pressed_keys[ord(' ')]:
                game_loop()
        screen.fill(color)
        GAME_FONT1.render_to(screen, (800,100) , "COLOR GAME", color_list[rdm_num_one])
        GAME_FONT1.render_to(screen, (700,250) , "PRESS SPACE TO START", white)
        GAME_FONT1.render_to(screen, (0,900) , "Press X to quit ", white)
        pygame.display.flip()
        clock.tick(30)

def game_loop():
    system("clear")
    pygame.init()
    pygame.mixer.init()
    GAME_FONT1 = pygame.freetype.Font("font.ttf", 75)
    GAME_FONT2 = pygame.freetype.Font("font.ttf", 200)
    all_collor = ["purple","blue","green","yellow","pink","brown","white","grey","black","orange"]
    purple = (191,64,191)
    blue =  (0,0,255)
    green = (0,128,0)
    yellow = (255,255,0)
    pink = (255,192,203)
    brown = (165,42,42)
    white = (255,255,255)
    grey = (204,209,209)
    black = (0,0,0)
    orange = (255,165,0)
    score = 0
    color_list = [purple,blue,green,yellow,pink,brown,white,grey,black,orange]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    rdm_num_one = randint(0,len(all_collor) - 1)
    rdm_num_two = randint(0,len(all_collor) - 1)
    if rdm_num_one == rdm_num_two:
        rdm_num_one = randint(0,len(all_collor) - 1)
        rdm_num_two = randint(0,len(all_collor) - 1)
    clock = pygame.time.Clock()
    running = True
    color = (217,225,229)
    wait = 0
    name = []
    l = []
    d = 430
    pos = []
    time = 30
    idx = 0
    high = print_file("highscore.txt")
    start = 0
    for i in range(100):
        pos.append(d)
        d = d + 100
    letter = 97
    for i in range(26):
        l.append(chr(letter))
        letter = letter + 1
    while running:
        if score > int(high):
            write_id("highscore.txt",str(score))
            high = print_file("highscore.txt")
        if time <= 0:
            idx = idx + 1
        if time > 0:
            idx = idx + 1
        if idx % 30 == 0 and time > 0:
            time = time - 1
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(name) > 0:
                        name.pop(len(name) - 1)
                    if event.type == pygame.QUIT:
                       quit()
                if event.key == K_ESCAPE:
                    game_loop()
            my_guess = list_to_str(name)
            if my_guess == all_collor[rdm_num_two] and time > 0:
                score = score + 1
                name = []
            if pressed_keys[ord('x')]:
                quit()
            if pressed_keys[ord(' ')] and time <= 0 and idx > 120:
                game_loop()
            if pressed_keys[ord(' ')] and time > 0:
                rdm_num_one = randint(0,len(all_collor) - 1)
                rdm_num_two = randint(0,len(all_collor) - 1)
                if rdm_num_one == rdm_num_two:
                    rdm_num_one = randint(0,len(all_collor) - 1)
                    rdm_num_two = randint(0,len(all_collor) - 1)
                name = []
            for i in range(26):
                if pressed_keys[ord(l[i])] and wait < 0:
                    name.append(l[i])
                    wait = 1
        wait = wait - 1
        print(wait)
        screen.fill(color)
        if time > 0:
            GAME_FONT2.render_to(screen, (825 - (len(all_collor[rdm_num_one]) * 25), 30), all_collor[rdm_num_one], color_list[rdm_num_two])
            GAME_FONT1.render_to(screen, (0,0) , "Score " + str(score), white)
            GAME_FONT1.render_to(screen, (0,75) , "Highcore " + str(high), white)
            GAME_FONT1.render_to(screen, (0,150) , "Time left " + str(time), white)
            GAME_FONT1.render_to(screen, (0,900) , "Press X to quit ", white)    
        else:
            GAME_FONT1.render_to(screen, (800,150) , "Times Up " + str(time), white)
            GAME_FONT1.render_to(screen, (650,650) , "Press space to restart and X to quit", white)
            GAME_FONT1.render_to(screen, (800,250) , "Score " + str(score), white)
            GAME_FONT1.render_to(screen, (800,350) , "Highcore " + str(high), white)
        if len(name) > 0 and time > 0:
            for i in range(len(name)):
                GAME_FONT2.render_to(screen, (pos[i]+100, 530), name[i], (30, 30, 30))
        pygame.display.flip()
        clock.tick(30)

menu_loop()