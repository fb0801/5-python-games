import tkinter as tk
import pygame
import math
import random
from tkinter import messagebox

class cube(object):
    #cube
    rows= 0
    w=0 

    def __init__(self,start, dirnx=1, dirny=0,color=(255,0,0)):
        pass

    def move(self, drinx,driny):
        pass

class snake(object):
    #snake
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x = 0
    y = 0

    for l in range(rows):
        x =x + sizeBtwn
        y=y + sizeBtwn

        pygame.draw.line(surface,(255,255,255), (x,0), (x,w))
        pygame.draw.line(surface,(255,255,255), (0,y), (w,y))


def redrawWindow(surface):
    global rows, width
    surface.fill(0,0,0,0)
    drawGrid(width, rows, surface )
    pygame.display.update() #update the screen

def randomSnake(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 500
    rows = 20# changeable
    win = pygame.display.set_mode((width, width))
    s= snake((255,0,0), (10,10))

    flag = True
    clock = pygame.time.Clock

    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(win)
    pass

rows=''
w =''
h =''

cube.rows = rows
cube.w =w

main()