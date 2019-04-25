import os
import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode([500, 600])
screen.fill(pygame.Color('blue'))


def load_image(name, colorkey):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if colorkey != 0:
        image.set_colorkey(colorkey)
    return image
